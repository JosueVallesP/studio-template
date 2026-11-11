"""The one self-check a draft gets from whoever wrote it, before it goes to the editor or the judge.

Usage:
  python3 scripts/self-check.py <draft> [--source <file with the person's raw words>] [--draft A] [--cap 4]

Runs, in order, the five scripts every writing path used to list separately:
  check-mechanical.py   house rules a script can decide, the source map, IDs, numbers
  check-human.py        the machine-writing patterns (never --detector: that call is the judge's)
  check-prose.py        the house rules in piece mode
  voice-diff.py         drift from the person's own markers (says so and passes when there's no corpus yet)
  check-stitch.py       the person's sentences lifted word for word from material/, inbox/ or canon/ and not
                        marked verbatim; the verbatim cap (--cap, default 2; pass --cap 4 for an essay)

A draft file with Posts A, B and C is checked draft by draft; --draft A checks one. Exit 0 when all
five pass, 1 when any of them needs a fix, with each script's output under its own heading. This
script never calls the detector and never writes a file.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [
    ("check-mechanical", []),
    ("check-human", []),
    ("check-prose", ["--mode", "piece"]),
    ("voice-diff", []),
    ("check-stitch", []),
]


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-") or "--detector" in args:
        print(__doc__); sys.exit(2)
    draft = args[0]
    if not os.path.isfile(draft):
        print(f"self-check: no file at {draft}"); sys.exit(2)
    pick = []
    if "--draft" in args:
        i = args.index("--draft")
        pick = args[i:i + 2]
    source = []
    if "--source" in args:
        i = args.index("--source")
        source = args[i:i + 2]
    cap = []
    if "--cap" in args:
        i = args.index("--cap")
        cap = args[i:i + 2]
    needs_fix = []
    for name, extra in STEPS:
        cmd = [sys.executable, "-I", os.path.join(HERE, name + ".py"), draft, *extra, *pick]
        if name == "voice-diff":
            cmd += source
        if name == "check-stitch":
            cmd += cap
        print(f"######## {name}", flush=True)
        r = subprocess.run(cmd)
        print(flush=True)
        if r.returncode != 0:
            needs_fix.append(name)
    if needs_fix:
        print("self-check: fix (" + ", ".join(needs_fix) + "). Fix every fail; read the flags against "
              "skills/craft-house-rules and fix the real ones; then run this again.")
        sys.exit(1)
    print("self-check: pass")


if __name__ == "__main__":
    main()
