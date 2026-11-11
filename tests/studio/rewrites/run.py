#!/usr/bin/env python3
"""Runs the rewrites test: scripts/rewrites.py against the five fixture pairs in root/.
Checks the order `pick` gives the writer and the counts `tally` gives /end.
Usage, from anywhere: python3 tests/studio/rewrites/run.py"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "..", "..", "scripts", "rewrites.py")
ROOT = os.path.join(HERE, "root")


def run(*args):
    return subprocess.run([sys.executable, SCRIPT, *args, "--root", ROOT], capture_output=True, text=True).stdout


ok = bad = 0
def check(name, got, want):
    global ok, bad
    if got == want:
        ok += 1; print(f"ok   {name}")
    else:
        bad += 1; print(f"FAIL {name}: expected {want}, got {got}")

# Open same-format pairs first (one tagged new, one untagged), then open other-format, then closed same-format.
picked = [line.split("\t")[0] for line in run("pick", "--format", "fmt-linkedin-post").splitlines()]
check("pick order", [os.path.basename(p) for p in picked],
      ["2026-10-10-P001.md", "2026-10-01-P000.md", "2026-10-14-E001.md", "2026-10-15-P003.md", "2026-10-12-P002.md"])
check("pick --n", len(run("pick", "--format", "fmt-linkedin-post", "--n", "2").splitlines()), 2)
check("pick essay first", os.path.basename(run("pick", "--format", "fmt-substack-essay").splitlines()[0].split("\t")[0]),
      "2026-10-14-E001.md")

# P001's review names W2, so that change was flagged; H19, W1 and W3 were missed.
t = json.loads(run("tally", "--since", "2026-10-10", "--json"))
check("tally pairs", t["pairs"], 4)
check("tally changes", t["changes"], 7)
check("tally counts", [t["missed"], t["flagged"], t["new"], t["piece"], t["untagged"]], [3, 1, 2, 1, 0])
check("tally missed rules", sorted(m["rule"] for m in t["missed_lines"]), ["H19", "W1", "W3"])
check("tally sentence", run("tally", "--since", "2026-10-10").splitlines()[0],
      "4 rewrites, 7 changes: 3 broke a rule the reviews missed, 1 broke a rule a review had named, 2 are new, 1 was about the piece only.")
check("tally empty", run("tally", "--since", "2027-01-01").strip(), "No rewrites since 2027-01-01.")
check("tally untagged", json.loads(run("tally", "--since", "2026-10-01", "--json"))["untagged"], 1)

print(f"{ok} passed, {bad} failed")
sys.exit(1 if bad else 0)
