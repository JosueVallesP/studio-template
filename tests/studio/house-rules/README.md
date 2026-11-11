# house-rules

Checks the house rules a script can decide, one short passage at a time, under the same check the scripts and hooks use (`scripts/studio_checks.house_check`).

## What's here

`cases.json`: one case per passage, with an `id`, the `text`, what it must do (`expect`: `fail`, `flag` or `pass`) and, for a fail or a flag, the `rule` that must fire. A case may set `reply: true` to be checked as one of the studio's replies, `allow` for words the person's voice guide lets through (the exception principle), and `strict: true` when a pass must have no flags either.

## What to run

```
python3 tests/studio/house-rules/run.py
```

## What it must show

Every case as expected and the last line `N passed, 0 failed`. Add a case whenever a rule changes or a real draft gets through that shouldn't have.
