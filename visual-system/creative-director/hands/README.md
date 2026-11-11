# Hands

One notes file per tool, plus `jobs.md`. `cd-make` reads `jobs.md` to find which tool and which feature fit the job, then reads that tool's file. `cd-system` reads each tool file it syncs.

Every tool file has the same parts, rules first: what to use the tool for and not, a feature map (each feature, the job it serves, and whether it has been tested), how a brand lives in it, how to work the connector, cost, and gotchas. A test log comes last. It records what happened when the tool made a real piece, as evidence for the rules, and it is not a set of instructions. Notes come from real runs, not from the connector's tool list. A note not yet backed by a run says "untested."

## The first test (October 30, 2026)

One LinkedIn framework card for the studio owner's Engraved Swirl brand (keep mode), run through all six tools. The brief, every draft and the generator code are in `examples/engraved-swirl-test/brands/josue-valles/pieces/2026-10-30-body-of-work/`. Spend: 6 Recraft credits and $0.08 of Flora.

| Tool | Verdict |
| --- | --- |
| Figma | Best for rule-drawn art: generator code ran inside the file, full density, live text, bound variables |
| Claude Design | Good for type layouts; art goes in as an image; tokens need converting; review needs a local render |
| Recraft | Holds a trained look cheaply; ignores layout instructions; vectors too messy to edit |
| Flora | Good second step for fixing details; weak at clearing exact areas |
| Paper | Faithful, but large art can't be pasted; best for light layouts tweaked by hand |
| D2 | Exact structure, boxes only; font loading has two traps |

## The second test (same day): features beyond plain generation

Figma motion (keyframes and `export_video`): works. Recraft `erase_region`: works; `image_to_image`: fails to keep layout. Flora multi-reference: carries the look, drops layout, and turned milestones into gravestones. Flora free actions: included in the plan. Total spend for both rounds: 11 Recraft credits and $0.13 of Flora.

When a tool keeps behaving the same way across pieces, `cd-learn` proposes an edit to its notes. To add a tool, write a new file in this shape and add its name to `hands` in the workspace config. No skill changes.
