"""Checks that map-render builds the page, the tree and the canvas from a good map, and refuses a map that
breaks a rule in skills/job-map/references/map-data.md. Run from anywhere: python3 tests/studio/map/run.py
"""
import copy, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RENDER = os.path.join(ROOT, "scripts", "map-render.py")
GOOD = json.load(open(os.path.join(HERE, "good.json"), encoding="utf-8"))

cases = []
def case(name, ok, out=""):
    cases.append((name, ok)); print(("ok   " if ok else "FAIL ") + name)
    if not ok and out:
        print("     " + out.strip().replace("\n", "\n     "))


def render(m, *extra):
    d = tempfile.mkdtemp()
    p = os.path.join(d, "map.json")
    json.dump(m, open(p, "w", encoding="utf-8"))
    r = subprocess.run([sys.executable, "-I", RENDER, p, *extra], capture_output=True, text=True)
    return d, r.returncode, r.stdout + r.stderr


# A good map builds all three files.
d, code, out = render(GOOD)
case("good map builds", code == 0 and "built" in out, out)
md = open(os.path.join(d, "findings.md"), encoding="utf-8").read() if code == 0 else ""
page = open(os.path.join(d, "map.html"), encoding="utf-8").read() if code == 0 else ""
canvas = json.load(open(os.path.join(d, "map.canvas"), encoding="utf-8")) if code == 0 else {}
case("page: names what was read, public and private", "6 separate pieces, 4 public and 2 private" in md, md[:400])
case("page: the left-out line is there", "left out what clients said" in md)
case("page: the review findings come first, the rest after", md.find("## The 3 to look at first") < md.find("## Everything else the map found"))
case("page: the spine shows, counted in pieces", "## Your spine" in md and "In 3 pieces, from 2022-03 to 2025-05-12" in md, md)
case("page: quotes carry their source and privacy", "(call-01, 2025-05-12, private)" in md)
case("page: root questions are listed", "## Questions for the interviews" in md and "charged what you thought" in md)
case("page: next step is the review while findings are open", 'Say "review my map"' in md)
case("tree: one page, data inside, no outside scripts", page.startswith("<!doctype html>") and '"Ines Okafor"' in page and "<script src" not in page)
case("tree: theme tokens for light and dark", ":root{" in page and "prefers-color-scheme: dark" in page)
ids = {n["id"] for n in canvas.get("nodes", [])}
case("canvas: every node and edge is there", len(canvas.get("nodes", [])) == len(GOOD["nodes"]) and len(canvas.get("edges", [])) == len(GOOD["links"]))
case("canvas: edges point at nodes", all(e["fromNode"] in ids and e["toNode"] in ids for e in canvas.get("edges", [])))

# The page passes the house rules (quotes are skipped by the checker).
prose = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "check-prose.py"), os.path.join(d, "findings.md"), "--mode", "prose"],
                       capture_output=True, text=True)
case("page: no house-rule fails", "FAILS" not in prose.stdout, prose.stdout)
shutil.rmtree(d, ignore_errors=True)

# A view the person no longer holds is marked, listed, and needs its date and reason.
m = copy.deepcopy(GOOD)
c5 = next(n for n in m["nodes"] if n["id"] == "c5")
c5["status"] = "held before"; c5["dropped"] = '2026-10-27 · "I used to think that, not anymore"'
m["links"].append({"from": "c5", "to": "c1", "kind": "replaced_by", "evidence": [m["sources"][0]["id"]]})
d, code, out = render(m)
md = open(os.path.join(d, "findings.md"), encoding="utf-8").read() if code == 0 else ""
case("held before: builds, and the page lists it", code == 0 and "## Views you no longer hold" in md, out + md[-300:])
shutil.rmtree(d, ignore_errors=True)
m2 = copy.deepcopy(m); next(n for n in m2["nodes"] if n["id"] == "c5").pop("dropped")
d, code, out = render(m2)
case("held before: refused without a date and reason", code != 0 and "needs dropped" in out, out)
shutil.rmtree(d, ignore_errors=True)
m3 = copy.deepcopy(GOOD); m3["links"].append({"from": "c5", "to": "c1", "kind": "replaced_by", "evidence": [m3["sources"][0]["id"]]})
d, code, out = render(m3)
case("replaced_by: refused from a claim still held", code != 0 and "replaced_by" in out, out)
shutil.rmtree(d, ignore_errors=True)

# After the review, the next step changes.
m = copy.deepcopy(GOOD)
for f in m["findings"]:
    f["status"] = "yes"
d, code, out = render(m)
md = open(os.path.join(d, "findings.md"), encoding="utf-8").read() if code == 0 else ""
case("after the review: next step is update or the interviews", "update my map" in md and "review my map" not in md, md[-400:])
case("after the review: status shows in plain words", "Status: you said yes." in md)
shutil.rmtree(d, ignore_errors=True)


def refused(name, mutate, expect):
    m = copy.deepcopy(GOOD)
    mutate(m)
    d, code, out = render(m)
    case("refuses: " + name, code == 1 and expect in out and not os.path.exists(os.path.join(d, "findings.md")), out)
    shutil.rmtree(d, ignore_errors=True)


refused("a root that states a value", lambda m: m["nodes"][7].__setitem__("text", "You value honesty."), "must be a question")
refused("an outright claim with no quote", lambda m: m["nodes"][0]["versions"][0].pop("quote"), "needs the quote")
refused("a finding with one quote", lambda m: m["findings"][1]["evidence"].pop(), "at least 2 quotes")
refused("a private-only finding quoting a public piece", lambda m: m["findings"][0]["evidence"].append({"quote": "x", "source": "post-01"}), "only private sources")
refused("a source that doesn't exist", lambda m: m["nodes"][2]["versions"][0].__setitem__("source", "post-99"), "isn't in sources")
refused("a link to nowhere", lambda m: m["links"].append({"from": "c1", "to": "c99", "kind": "supports", "evidence": ["post-01"]}), "'c99' isn't a node")
refused("a link with no evidence", lambda m: m["links"][0].__setitem__("evidence", []), "needs at least one source")
refused("more than ten in the review", lambda m: m["findings"].extend(
    [dict(m["findings"][1], id=f"x{i}", review=True) for i in range(8)]), "at most ten")
refused("more than five spine claims", lambda m: [n.__setitem__("spine", True) for n in m["nodes"]] and None or
        m["nodes"].extend([dict(m["nodes"][2], id=f"y{i}", spine=True) for i in range(4)]), "the spine is three to five")
refused("an unknown privacy mark", lambda m: m["sources"][0].__setitem__("privacy", "secret"), "public or private")

# Receipts: with the person's files beside the map, every quote must be in them word for word.
def with_files(m, posts_text):
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "bank", "map"))
    os.makedirs(os.path.join(d, "material"))
    open(os.path.join(d, "material", "posts.md"), "w", encoding="utf-8").write(posts_text)
    p = os.path.join(d, "bank", "map", "map.json")
    json.dump(m, open(p, "w", encoding="utf-8"))
    r = subprocess.run([sys.executable, "-I", RENDER, p], capture_output=True, text=True)
    return d, r.returncode, r.stdout + r.stderr

POSTS = ("Your price is a promise about the client you\u2019ll take.\n\n"   # a curly apostrophe in the file
         "I lost my biggest client the week I raised my rates. Losing them was the best pricing data I ever got.\n\n"
         "Discounts teach clients what you think you're worth.\n\nClimb the pricing ladder one rung a quarter.\n")
d, code, out = with_files(GOOD, POSTS)
case("receipts: quotes found in the files pass, curly quotes evened out", code == 0 and "Checked" in out, out)
case("receipts: files that aren't there are named, not failed", "Couldn't check" in out and "essays.md" in out, out)
shutil.rmtree(d, ignore_errors=True)
m = copy.deepcopy(GOOD)
m["nodes"][2]["versions"][0]["quote"] = "Losing them was the worst pricing data I ever got."
d, code, out = with_files(m, POSTS)
case("receipts: a quote that isn't in the files stops the build", code == 1 and "isn't in post-02's files" in out
     and not os.path.exists(os.path.join(d, "bank", "map", "findings.md")), out)
shutil.rmtree(d, ignore_errors=True)

# --check builds nothing.
d, code, out = render(GOOD, "--check")
case("--check reports and builds nothing", code == 0 and "checks out" in out and not os.path.exists(os.path.join(d, "map.html")), out)
shutil.rmtree(d, ignore_errors=True)

if any(not ok for _, ok in cases):
    print("map: FAILED"); sys.exit(1)
print("map: every case passed")
