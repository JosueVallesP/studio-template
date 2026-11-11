# Test: a buyer from the Tally form through the first post

A fictional buyer, Dana Whitfield, who coaches new engineering managers. It tests the whole path a real buyer takes before any interview: the Tally export, the converter, the one-command build, `/start`, the quick wins with Figma and Notion not connected, and the first post from her own material.

## Files

- `tally-export.csv`: one submission, with the form's titles as columns (the upload links are fake, so downloads fail on purpose).
- `inbox/`: her material, to copy into the built studio's `inbox/` after the build (it stands in for the uploads).
- `first-run-draft-v2.md`: the post the first run produced, for comparison.

## How to run it

1. `bash scripts/make-client.sh tests/studio/quickstart-dana/tally-export.csv --dir /tmp/studios --no-github`
2. Copy `inbox/*.md` into `/tmp/studios/dana-whitfield-studio/inbox/`.
3. In that folder, as Dana: `/start`; "set up my Figma" (not connected); "skip it, and skip the dashboard too"; "write a post from this"; `/start`; then change `hours_per_week` in `config/intake.yaml` and say "set up my studio".

## What good looks like

- `/start` welcomes her once, by name, and gives one next step each time. The second `/start` mentions the first post waiting for her call.
- The visual kit and dashboard steps say one step each ("connect it in Claude's settings, under Connectors, then say ...") and write "waiting on Connectors"; the skips are written as `- [x] ...: skipped <date>`.
- The first post uses only facts from her material, passes `check-mechanical.py`, and is judged by `stages/judge.md` against the material, with no score.
- The intake rebuild keeps `config/tools.md` connections, the ticks and skips in `canon/setup-progress.md`, and the setup section of `YOUR-STUDIO.md`.

## First run (v0.16, 2026-10-22)

The post was strong (a head of engineering's own line, her 140 managers, the 4% against 15% result), but a literal run would have stalled: the editor agent judged against a canon that didn't exist, the belief gate stopped the draft, the intake rebuild wiped progress and tool settings, the welcome repeated on every `/start`, and the first post was never mentioned again. Fixed in 0.20.

## Second run (v0.20, 2026-10-22)

All nine earlier problems fixed. The post opened on her podcast line ("When nine managers all hit the same wall in week three, that's not nine personal problems, that's a missing piece in how you promote people.") and was judged FIX (now revise) twice, which showed there was no rule for a post still failing after one revision. That rule, a quick-start review template, a full verdict ladder, and a rebuild that kept reopening the quick wins were fixed in 0.21.
