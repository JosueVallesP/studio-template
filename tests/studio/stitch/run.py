"""Checks that check-stitch finds a sentence lifted word for word from the person's material and
passes the same fact said fresh. Run from anywhere: python3 tests/studio/stitch/run.py
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "material")


def run(*args):
    r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "check-stitch.py"), *args, "--sources", SRC],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


cases = []
def case(name, ok):
    cases.append((name, ok)); print(("ok   " if ok else "FAIL ") + name)

code, out = run(os.path.join(HERE, "stitched.md"))
case("stitched: the lifted sentence fails", code == 1 and "lifted, not marked verbatim" in out and "drain me" in out)
case("stitched: the declared quote passes", "quote on purpose" in out and "junior person" in out)
code, out = run(os.path.join(HERE, "fresh.md"))
case("fresh: said-fresh fact passes", code == 0 and "lifted, not marked verbatim" not in out)
case("fresh: the declared quote still counted", "quote on purpose" in out)
code, out = run(os.path.join(HERE, "fresh.md"), "--cap", "0")
case("cap: over the cap fails", code == 1 and "the cap is 0" in out)

if any(not ok for _, ok in cases):
    print("stitch: FAILED"); sys.exit(1)
print("stitch: every case passed")
