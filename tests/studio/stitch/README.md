# Stitch test

`material/workshop.md` is a short fake transcript. `stitched.md` lifts one of its sentences into a post and marks it `said again`; `fresh.md` says the same fact in new words. `run.py` checks that `scripts/check-stitch.py` fails the first and passes the second, that a run inside a `verbatim` row passes as a quote on purpose, and that the verbatim cap fails when it's over. Run: `python3 tests/studio/stitch/run.py`.
