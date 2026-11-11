# drafts

Checks that the check scripts read a draft with three candidates (`## Post A`, `## Post B`, `## Post C`) draft by draft, as `templates/piece/draft.md` lays it out.

## What's here

`three.md` holds three drafts of the same post; only Post B breaks house rules (an em dash, a reveal and two decoration adverbs). `single.md` holds one clean `## Post`, the shape of a revision.

## What to run

```
python3 tests/studio/drafts/run.py
```

## What it must show

Each script reports A, B and C under their own headings, only B fails, `--draft A` checks one draft alone, the detector and the voiceprint reading refuse to run three times and ask for `--draft`, and `self-check.py` says fix on the three and pass on the single. Last line: `9 passed, 0 failed`.
