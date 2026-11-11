# voiceprint

Checks that `scripts/voiceprint.py` tells writers apart on texts it hasn't seen, so a change to the script that makes it worse gets caught.

## What it reads

The essay library that ships with the studio, `skills/fmt-substack-essay/library/essays/`: one file per essay, the writer in its frontmatter (`author:`) and the text under `## Essay`. A file whose text is only a paywalled preview has no plain `## Essay` heading and is left out, so the run uses 46 essays by six writers. Any other folder in the same shape, or a CSV with a text column and an author column, works too.

## What to run

```
python3 tests/studio/voiceprint/validate.py --length 300
python3 tests/studio/voiceprint/validate.py <folder or essays.csv> --author-col Author --length 300
```

Run it at `--length 150`, `300`, `600` and `1000` after any change to the script. `scripts/test-all.sh` runs it once at 300 with `--check`, which fails when a rate falls below its floor (own pieces read as theirs 80%, unseen writers read as off 65%, attribution 70%). It takes about fifteen seconds.

## What the output must show

For each writer, a profile is built from all but three of their essays; the comparison set is every other writer but one; the held-out writer stands in for an unknown author, the way a model's draft would. Writers with five essays or fewer are left out of the comparison (the library's paywalled writer is one). On the repo's library, the run gave:

| Length | Own held-out pieces at least "close" | Unseen writer "off" | Separation (median) | Attribution, 5 writers |
| --- | --- | --- | --- | --- |
| 150 | 86% | 55% | 0.85 | 68% |
| 300 | 83% | 68% | 0.89 | 75% |
| 600 | 80% | 79% | 0.92 | 76% |
| 1000 | 76% | 83% | 0.89 | 81% |

A change passes when no column drops by more than three points at any length. Update this table and the one in `skills/check-voiceprint/references/methods.md` when a change improves it. (The figures in `methods.md` came from an earlier run on a different copy of the library, so they won't match this table until it's updated.)
