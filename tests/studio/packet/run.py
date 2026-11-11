"""Checks that scripts/packet.py builds a writer's packet from a brief: the sheet first, the brief's
sections, only the cards the plan names (never a whole library), the type's draft step when a TYPE is
named, and the voice. Uses the writer-editor-mara brief. Run from anywhere: python3 tests/studio/packet/run.py
"""
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BRIEF = os.path.join(ROOT, "tests", "studio", "writer-editor-mara", "piece", "brief.md")

cases = []
def case(name, ok):
    cases.append((name, ok)); print(("ok   " if ok else "FAIL ") + name)

piece = os.path.join(ROOT, "pieces", "_packet-test-" + next(tempfile._get_candidate_names()))
os.makedirs(piece)
try:
    text = open(BRIEF, encoding="utf-8").read().replace("SECONDARY MOVE  none", "TYPE            power listicle, path B\nSECONDARY MOVE  none")
    open(os.path.join(piece, "brief.md"), "w", encoding="utf-8").write(text)
    r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "packet.py"), piece], capture_output=True, text=True, cwd=ROOT)
    out = r.stdout + r.stderr
    packet = open(os.path.join(piece, "packet.md"), encoding="utf-8").read() if os.path.exists(os.path.join(piece, "packet.md")) else ""
    case("packet written and reported", r.returncode == 0 and "words:" in out and packet)
    case("sheet comes first", packet.startswith("# The writer's sheet"))
    case("the brief's idea is in", "## The one idea" in packet)
    cards = re.findall(r"^## ([A-Z]{0,2}\d+)\. ", packet, flags=re.M)
    case("the named cards are in", {"S3", "M9", "M2"} <= set(cards))
    case("the whole library is not", len(cards) < 12 and "## 1. Proof, then payoff" not in packet)
    case("the type's draft step is in, the judge's checks are not", "## Step 3. Draft" in packet and "## Checks the judge adds" not in packet)
    case("the voice section is in", "# The voice" in packet and "## Rewrite pairs" in packet)
finally:
    shutil.rmtree(piece, ignore_errors=True)

if any(not ok for _, ok in cases):
    print("packet: FAILED"); sys.exit(1)
print("packet: every case passed")
