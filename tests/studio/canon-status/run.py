#!/usr/bin/env python3
"""Rule 2 in the scripts: check-mechanical.py fails a retired ID and notes a draft or an unready bank
entry; cites.py lists the open pieces that still cite an entry and skips shipped ones.
Builds a small studio in a temp folder; touches nothing in the repo.
Usage: python3 -I tests/studio/canon-status/run.py"""
import json, os, subprocess, sys, tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
POVS = """# POVs

## P1 · Ask about events
status: confirmed
claim: Questions about what happened get better answers than questions about beliefs.

## P2 · Old view
status: retired
claim: Posting daily matters most.

## P3 · Forming view
status: draft
claim: Most interviews stop too early.
"""
IDEAS = """# Idea bank

## I1 · A raw note
status: raw
raw: "something"

## I2 · A ready note
status: ready
raw: "something else"

## I3 · A number from a call
status: ready
raw: "we had fifty clients"
heard: recorder, check with the person
"""
def draft(ids):
    rows = "\n".join(f"| line {i} | said again | {i} | |" for i in ids)
    return f"""## Post

Ask what happened this week, and the belief comes out inside the story.

## Source map

| Line or claim | Kind | Source ID or file | Note |
| --- | --- | --- | --- |
{rows}
| the general point | writer | | |
"""
def brief(status):
    return f"---\nid: x\nstatus: {status}\nsources: P2\n---\n"

ok = True
def check(name, cond, extra=""):
    global ok
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"\n     {extra}"))
    ok = ok and cond

with tempfile.TemporaryDirectory() as t:
    open(os.path.join(t, "studio.manifest.yaml"), "w").write("version: test\n")
    os.makedirs(os.path.join(t, "canon", "person")); os.makedirs(os.path.join(t, "bank"))
    open(os.path.join(t, "canon", "person", "povs.md"), "w").write(POVS)
    open(os.path.join(t, "bank", "ideas.md"), "w").write(IDEAS)
    open(os.path.join(t, "canon", "core-summary.md"), "w").write("Leans on P2 and P1.\n")
    for pid, st, ids in [("open-one", "drafted", ["P1", "P2"]), ("shipped-one", "shipped", ["P2"]), ("other", "briefed", ["P1"])]:
        d = os.path.join(t, "pieces", pid); os.makedirs(d)
        open(os.path.join(d, "brief.md"), "w").write(brief(st).replace("sources: P2", "sources: " + " ".join(ids)))
        open(os.path.join(d, "draft-v1.md"), "w").write(draft(ids))

    def mech(ids):
        p = os.path.join(t, "pieces", "open-one", "draft-v9.md"); open(p, "w").write(draft(ids))
        r = subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "check-mechanical.py"), p, "--json"], capture_output=True, text=True, cwd=t)
        os.remove(p)
        return json.loads(r.stdout)

    r = mech(["P1"]);  check("a confirmed ID passes", not any("P1" in f for f in r["fails"]), r)
    r = mech(["P2"]);  check("a retired ID fails", any("P2 is retired" in f for f in r["fails"]), r)
    r = mech(["P3"]);  check("a draft ID is a note, not a fail", not r["fails"] or not any("P3" in f for f in r["fails"]), r)
    check("the draft note names rule 2", any("P3 is a draft" in n for n in r["notes"]), r)
    r = mech(["I1"]);  check("a raw idea is a note", any("I1 is `raw`" in n for n in r["notes"]) and not any("I1" in f for f in r["fails"]), r)
    r = mech(["I2"]);  check("a ready idea says nothing", not any("I2" in n for n in r["notes"] + r["fails"]), r)
    r = mech(["I3"]);  check("an entry a recorder heard and nobody confirmed fails", any("I3 holds a number" in f for f in r["fails"]), r)

    c = subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "cites.py"), "P2", "P1", "P9", "--json"], capture_output=True, text=True, cwd=t)
    out = json.loads(c.stdout)
    pieces = [h["piece"] for h in out["P2"]["open_pieces"]]
    check("cites.py finds the open piece citing P2", pieces == ["open-one"], out)
    check("cites.py skips the shipped piece", "shipped-one" not in pieces, out)
    check("cites.py names the core summary", out["P2"]["core_summary"] is True, out)
    check("cites.py finds both open pieces for P1", sorted(h["piece"] for h in out["P1"]["open_pieces"]) == ["open-one", "other"], out)
    check("cites.py finds nothing for an unused ID", out["P9"]["open_pieces"] == [] and out["P9"]["core_summary"] is False, out)

print("all passed" if ok else "some failed")
sys.exit(0 if ok else 1)
