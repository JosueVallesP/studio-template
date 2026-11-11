"""Checks that the draft scripts read a draft file with Posts A, B and C draft by draft.

three.md holds three drafts; only Post B breaks house rules (an em dash, a reveal, two decoration
adverbs). single.md holds one clean ## Post. Run from anywhere: python3 tests/studio/drafts/run.py
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
THREE, SINGLE = os.path.join(HERE, "three.md"), os.path.join(HERE, "single.md")


def run(script, *args):
    r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", script), *args],
                       capture_output=True, text=True, env={k: v for k, v in os.environ.items() if k != "STUDIO_DRAFT"})
    return r.returncode, r.stdout + r.stderr


def sections(out):
    """The output under each === Post X heading."""
    parts, cur = {}, None
    for line in out.splitlines():
        if line.startswith("=== Post "):
            cur = line.split()[-1]; parts[cur] = ""
        elif cur:
            parts[cur] += line + "\n"
    return parts


cases = []
def case(name, ok):
    cases.append((name, ok)); print(("ok   " if ok else "FAIL ") + name)

code, out = run("check-mechanical.py", THREE)
s = sections(out)
case("mechanical: three drafts, each checked", sorted(s) == ["A", "B", "C"])
case("mechanical: only B fails", "FAIL" in s.get("B", "") and "FAIL" not in s.get("A", "x") and "FAIL" not in s.get("C", "x"))
case("mechanical: exit 1 when one draft fails", code == 1)
code, out = run("check-mechanical.py", THREE, "--draft", "a")
case("mechanical: --draft A checks A alone and passes", code == 0 and "=== Post" not in out)
code, out = run("check-prose.py", THREE, "--mode", "piece")
s = sections(out)
case("prose: B fails, A and C pass", "FAILS" in s.get("B", "") and "fails: none" in s.get("A", "") and "fails: none" in s.get("C", ""))
code, out = run("check-human.py", THREE, "--detector")
case("human: the detector won't fan out over three drafts", code == 2 and "--draft" in out)
code, out = run("voiceprint.py", "score", THREE)
case("voiceprint: the reading won't fan out over three drafts", code != 0 and "--draft" in out)
code, out = run("self-check.py", THREE)
case("self-check: three drafts, one bad, says fix", code == 1 and "self-check: fix" in out)
code, out = run("self-check.py", SINGLE)
case("self-check: one clean ## Post passes", code == 0 and "self-check: pass" in out)

bad = sum(1 for _, ok in cases if not ok)
print(f"{len(cases) - bad} passed, {bad} failed")
sys.exit(1 if bad else 0)
