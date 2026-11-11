#!/usr/bin/env python3
"""Three holes in check-mechanical.py closed in 0.80.0: numbers written as words, names the sources never
mention, and frameworks given a name the person never gave. Temp folder only.
Usage: python3 -I tests/studio/claims/run.py"""
import json, os, subprocess, sys, tempfile
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ok = True
def check(name, cond, extra=""):
    global ok
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"\n     {extra}"))
    ok = ok and cond
with tempfile.TemporaryDirectory() as t:
    open(os.path.join(t, "studio.manifest.yaml"), "w").write("version: test\n")
    os.makedirs(os.path.join(t, "material")); os.makedirs(os.path.join(t, "pieces", "p"))
    open(os.path.join(t, "material", "m.md"), "w").write("I call it the Event Question Method. We lost eleven clients in 2024.\n")
    open(os.path.join(t, "material", "c.md"), "w").write("I co-founded the studio in 2019. I helped one client rebuild their pricing.\n")
    os.makedirs(os.path.join(t, "bank", "map"))
    json.dump({"nodes": [{"id": "c1", "type": "claim", "text": "Daily posting matters most", "status": "held before", "dropped": "2026-10-27 · moved on",
               "versions": [{"quote": "Posting every day is what matters most for growth", "source": "x"}]}]},
              open(os.path.join(t, "bank", "map", "map.json"), "w"))
    def run(post, rows=()):
        body = "\n".join(f"| {a} | {b} | {c} | |" for a, b, c in rows)
        p = os.path.join(t, "pieces", "p", "draft-v1.md")
        open(p, "w").write(f"## Post\n\n{post}\n\n## Source map\n\n| Line or claim | Kind | Source ID or file | Note |\n| --- | --- | --- | --- |\n{body}\n| the point | writer | | |\n")
        return json.loads(subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "check-mechanical.py"), p, "--json"], capture_output=True, text=True, cwd=t).stdout)
    r = run("Last year we lost eleven clients.")
    check("an unsourced word number about people fails", any("eleven clients" in f for f in r["fails"]), r["fails"])
    r = run("Last year we lost eleven clients.", [("we lost eleven clients", "said again", "material/m.md")])
    check("a sourced word number passes", not any("written as a word" in f for f in r["fails"]), r["fails"])
    r = run("I wrote five trade-offs down.")
    check("a word number that's structure passes", not any("written as a word" in f for f in r["fails"]), r["fails"])
    r = run("This is the Three Layer Model at work.")
    check("a framework name the person never used is noted", any("named framework" in n for n in r["notes"]), r["notes"])
    r = run("This is the Event Question Method at work.", [("the Event Question Method", "said again", "material/m.md")])
    check("a framework name from their files passes", not any("named framework" in n for n in r["notes"]), r["notes"])
    r = run("So I read what Acme Corp did last year.")
    check("a name no source mentions is noted", any('"Acme Corp"' in n for n in r["notes"]), r["notes"])
    r = run("So I read what Acme Corp did.", [("Acme Corp case", "borrowed: verify", "acme.com/about")])
    check("a logged borrowed name passes", not any('"Acme Corp"' in n for n in r["notes"]), r["notes"])
    r = run("On Monday I'm posting it on LinkedIn.")
    check("days, platforms and I'm aren't names", not any("name \"" in n for n in r["notes"]), r["notes"])
    r = run("I founded the studio.", [("I founded the studio", "said again", "material/c.md")])
    check("co-founded said as founded is noted", any("co-" in n for n in r["notes"]), r["notes"])
    r = run("I co-founded the studio.", [("I co-founded the studio", "said again", "material/c.md")])
    check("co-founded kept passes", not any("co-" in n or "bigger" in n for n in r["notes"]), r["notes"])
    r = run("I led my clients through new pricing.", [("I led my clients through new pricing", "said again", "material/c.md")])
    check("helped one client said as led my clients is noted", any("bigger" in n for n in r["notes"]) and any("many" in n for n in r["notes"]), r["notes"])
    r = run("Posting every day is what matters most for growth.")
    check("a view they no longer hold fails", any("no longer holds" in f for f in r["fails"]), r["fails"])
    r = run("I used to think posting every day mattered most.")
    check("saying it as what they used to think passes", not any("no longer holds" in f for f in r["fails"]), r["fails"])
print("all passed" if ok else "some failed")
sys.exit(0 if ok else 1)
