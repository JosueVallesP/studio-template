#!/usr/bin/env python3
"""Quotes that claim to be the person's exact words are checked against the file they cite:
check-mechanical.py on verbatim rows, check-proposals.py on open proposals. Temp folder only.
Usage: python3 -I tests/studio/receipts/run.py"""
import json, os, subprocess, sys, tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ok = True
def check(name, cond, extra=""):
    global ok
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"\n     {extra}"))
    ok = ok and cond

MATERIAL = "We ran the workshop twice.\nProjects under $10K drain me, because they take the same setup as the large ones\nTwo smart people can disagree.\n"
def draft(rows):
    body = "\n".join(f"| {l} | {k} | {s} | {n} |" for l, k, s, n in rows)
    return f"""## Post

Small projects take the same setup as big ones, so I stopped taking them.

## Source map

| Line or claim | Kind | Source ID or file | Note |
| --- | --- | --- | --- |
{body}
| the general point | writer | | |
"""
PROPOSALS = """# Proposals

## 2026-10-20 · kind: seen
proposed_by: librarian
proposal: You keep saying "Projects under $10K drain me" and turning small work down.
evidence:
  - 2026-10-20 · material/workshop.md · "Two smart people can disagree."
question_for_the_person: Is this a rule you hold?
status: open

## 2026-10-21 · kind: contradiction
proposed_by: tidy
proposal: Two lines pull against each other: "I take every project that comes" and "Projects under $10K drain me".
question_for_the_person: Which holds now?
status: open

## 2026-10-01 · kind: seen
proposal: "A line nobody ever wrote down anywhere."
status: declined 2026-10-02
"""

with tempfile.TemporaryDirectory() as t:
    open(os.path.join(t, "studio.manifest.yaml"), "w").write("version: test\n")
    os.makedirs(os.path.join(t, "material")); os.makedirs(os.path.join(t, "pieces", "p"))
    open(os.path.join(t, "material", "workshop.md"), "w").write(MATERIAL)
    def mech(rows):
        p = os.path.join(t, "pieces", "p", "draft-v1.md"); open(p, "w").write(draft(rows))
        r = subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "check-mechanical.py"), p, "--json"], capture_output=True, text=True, cwd=t)
        return [f for f in json.loads(r.stdout)["fails"] if "verbatim row" in f]
    check("an exact quote passes", not mech([("Projects under $10K drain me, because they take the same setup as the large ones.", "verbatim", "material/workshop.md", "")]))
    check("framing outside the quotation marks is fine", not mech([('In my workshop I say: "Projects under $10K drain me."', "verbatim", "material/workshop.md", "")]))
    check("a changed word fails", mech([("Two smart people can disagree on those.", "verbatim", "material/workshop.md", "")]) != [])
    check("a file that isn't there fails", mech([("Two smart people can disagree.", "verbatim", "material/gone.md", "")]) != [])
    check("supplied copy is exempt", not mech([("A line they pasted today.", "verbatim", "said today", "supplied")]))
    check("a said again row isn't checked word for word", not mech([("Small work costs as much setup as big work.", "said again", "material/workshop.md", "")]))

    open(os.path.join(t, "proposals.md"), "w").write(PROPOSALS)
    r = subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "check-proposals.py")], capture_output=True, text=True, cwd=t)
    check("an open proposal with an invented quote fails", r.returncode == 1 and "I take every project that comes" in r.stdout, r.stdout)
    check("an open proposal with real quotes passes", "kind: seen" not in r.stdout.split("FAIL")[1] if "FAIL" in r.stdout else False, r.stdout)
    check("a closed proposal isn't checked by default", "nobody ever wrote" not in r.stdout, r.stdout)

print("all passed" if ok else "some failed")
sys.exit(0 if ok else 1)
