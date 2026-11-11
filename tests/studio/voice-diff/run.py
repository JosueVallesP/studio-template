"""Checks voice-diff --source on two things: a draft that sounds surer than the person (a bound dropped,
a modal made stronger, a booster added, an "I" sentence turned general), and a term of the person's
swapped for another word. Every case runs in a temp folder. Run from anywhere: python3 -I tests/studio/voice-diff/run.py
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SCRIPT = os.path.join(ROOT, "scripts", "voice-diff.py")

cases = []
def case(name, ok, out=""):
    cases.append((name, ok)); print(("ok   " if ok else "FAIL ") + name)
    if not ok and out: print("     " + out.replace("\n", "\n     ")[:1500])


def run(source, draft, guide=None):
    with tempfile.TemporaryDirectory() as tmp:
        if guide is not None:
            open(os.path.join(tmp, "CLAUDE.md"), "w").write("# test studio\n")
            os.makedirs(os.path.join(tmp, "canon", "voice"))
            open(os.path.join(tmp, "canon", "voice", "voice-guide.md"), "w").write(guide)
        s, d = os.path.join(tmp, "source.md"), os.path.join(tmp, "draft.md")
        open(s, "w").write(source + "\n"); open(d, "w").write(draft + "\n")
        r = subprocess.run([sys.executable, "-I", SCRIPT, d, "--source", s, "--corpus", os.path.join(tmp, "none"), "--json"],
                           capture_output=True, text=True, cwd=tmp)
        try:
            return r.returncode, json.loads(r.stdout), r.stdout + r.stderr
        except ValueError:
            return r.returncode, {}, r.stdout + r.stderr


def sure(rep, key):
    return rep.get("sureness", {}).get(key, [])


SRC = "In my experience, this usually works for small teams."

code, rep, out = run(SRC, "This works for teams.")
case("dropped bound: 'usually' and 'in my experience' gone is flagged", any("usually" in f["lost"] for f in sure(rep, "bound_dropped")), out)
case("dropped bound: the 'I' sentence turned general is flagged", len(sure(rep, "first_person_gone")) == 1, out)
case("dropped bound: a flag, never a fail", code == 0, out)
case("dropped bound: the hedge rate drops from source to draft",
     rep.get("sureness", {}).get("source_hedges_per_1000", 0) > rep.get("sureness", {}).get("draft_hedges_per_1000", 1), out)

code, rep, out = run(SRC, "This usually works for small teams, in my experience.")
case("kept bound: a draft that keeps 'usually' and the 'my' passes",
     code == 0 and not any(sure(rep, k) for k in ("bound_dropped", "modal_stronger", "booster_added", "first_person_gone")), out)

code, rep, out = run(SRC, "This usually works for small teams.")
case("kept bound, lost 'my': no bound flag, the first-person collapse is flagged",
     not sure(rep, "bound_dropped") and len(sure(rep, "first_person_gone")) == 1, out)

code, rep, out = run("Writing every week might help you find your voice.", "Writing every week will help you find your voice.")
case("stronger modal: 'might help' to 'will help' is flagged",
     any(f["from"] == ["might"] and f["to"] == ["will"] for f in sure(rep, "modal_stronger")) and code == 0, out)

code, rep, out = run("Writing every week might help you find your voice.", "Obviously writing every week might help you find your voice.")
case("booster: 'obviously' added is flagged", any("obviously" in f["added"] for f in sure(rep, "booster_added")), out)
case("booster: the kept 'might' raises no bound or modal flag", not sure(rep, "bound_dropped") and not sure(rep, "modal_stronger"), out)

TERM_SRC = 'What you need is a "body of work" that people can find.'
code, rep, out = run(TERM_SRC, "What you need is a portfolio that people can find.")
case("term: 'body of work' swapped for 'portfolio' is flagged",
     [f["term"] for f in rep.get("terms_lost", [])] == ["body of work"] and code == 0, out)

code, rep, out = run(TERM_SRC, "What you need is a body of work that people can find.")
case("term: a draft that keeps 'body of work' passes", rep.get("terms_lost") == [], out)

code, rep, out = run(TERM_SRC, "Ship a portfolio on Tuesday.")
case("term: no flag when the draft doesn't talk about the same thing", rep.get("terms_lost") == [], out)

GUIDE = "# Voice guide\n\n## Vocabulary\n- Phrases they use: body of work, bar test\n- Terms they coined: <…>\n- Words they'd never use: portfolio\n"
code, rep, out = run("Your body of work grows a little every single week.", "Your portfolio grows a little every single week.", guide=GUIDE)
case("term: a voice-guide vocabulary term with no quotes is flagged",
     [f["term"] for f in rep.get("terms_lost", [])] == ["body of work"], out)

code, rep, out = run("The Personal Monopoly is the mix of things only you bring to the work.",
                     "Your positioning is the mix of things only you bring to the work.")
case("term: a capitalised term of theirs swapped out is flagged", [f["term"] for f in rep.get("terms_lost", [])] == ["Personal Monopoly"], out)

if any(not ok for _, ok in cases):
    print("voice-diff: FAILED"); sys.exit(1)
print("voice-diff: every case passed")
