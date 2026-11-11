# Routing: who owns what, and what wins

Three plugins work as one system. This file is the only place that says which one owns each job and which source wins when two disagree. When another file seems to say otherwise, this file wins and that file gets fixed.

- **creative-director** (this repo) owns the brand folder, the order of work and every approval.
- **art-direction** (`github.com/JosueVallesP/art-direction`, skills named `ad-*`) supplies methods that a step here calls by name.
- **design** (`github.com/JosueVallesP/design`, skills named `dsn-*`) supplies craft checks and the default numbers for a canvas.

The dependency runs one way: this repo points at art-direction and design, art-direction points at design, and nothing points back up.

Always call a skill by its full name (`dsn-contrast`, `ad-brief`). Never write "the design plugin's critique" or any other description of a skill, because other plugins with similar names can be installed in the same account.

## One owner per job

Inside a workspace, each job has one owner. The last column lists procedures in the other plugins that do a similar job. Do not run those inside a workspace.

| Job | Owner | What it writes | Called from the other plugins | Not used inside a workspace |
| --- | --- | --- | --- | --- |
| Intake | `cd-intake` | `brief.md` | Nothing | `dsn-identity` Mode A steps 1 to 3 (its own intake) |
| References | `cd-intake` Step 5 | `references.md` | Nothing | `dsn-identity` Mode A step 4 and the "Moodboards that constrain" section of `dsn-image` |
| Direction | `cd-direction` | `direction.md`, the only direction a brand has | Two tests from `ad-rules`, see below | `ad-rules` Mode A (it would write a second direction) and `dsn-identity` Mode A step 5 |
| The mark and the identity inventory | `cd-direction` decides, `cd-make` draws | The "The mark" row of the visual codes in `direction.md`, then a piece | `dsn-mark` for drawing or judging a mark. `dsn-identity` Mode A steps 6 to 12 for clear space, minimum size and the variant list | |
| Tokens | `cd-system` | `system/tokens.json` | `dsn-tokens` principles 5 to 7 when a scale has to be derived | The naming scheme in `dsn-tokens` (three layers, plural raw names). Names follow `skills/cd-system/references/tokens.md` |
| The package | `cd-system` Step 2 | `system/package/`, from `kit/` | Nothing | Drawing a piece by hand outside the package's script |
| Making | `cd-make` | Drafts in `pieces/<piece>/drafts/` | The `dsn-*` skill that `skills/cd-make/references/craft.md` names for the question. `ad-brief` before any image-model prompt, see below. `ad-board` only when the approver asks for a reference board as a piece | |
| Review | `cd-review` | `review.md`, with the verdicts pass, revise and sent back | `dsn-contrast` for any text over a photo, a gradient or a saturated colour | `ad-critique`. Its verdict "approved as is" never counts as an approval here |
| Learning | `cd-learn` | `learnings/`, proposed rule edits | Nothing | |

`ad-critique` is for work that has no brand folder: someone else's draft, a portfolio, a piece made outside this system.

## Direction: the two tests from ad-rules

`cd-direction` Step 3 runs these on the "Never" list and the visual codes table before its own tests.

1. **Falsifiability** (`ad-rules` test 1). Beside each line of the never list, name a draft that would break it. A line with no such draft gets rewritten until one exists, or removed.
2. **Threshold completeness** (`ad-rules` test 8). Every figure in the visual codes carries its unit, and every pixel size names the canvas width it was set for.

No other part of `ad-rules` runs. Its clause count (four to eight) does not apply to `direction.md`.

## Making: before an image-model prompt

When a draft will come from an image model (Recraft or Flora), `cd-make` Step 3 does this first:

1. Write the in-frame checks with `ad-brief` (its "acceptance criterion": binary checks a second reader can answer from the image alone). Build them from the visual brief, the never list and the recurring shapes.
2. Save them in `piece.md` under a heading "In-frame checks".
3. After generating, run the checks on every return before review. A return that fails one is not saved as a draft.

The tool notes in `hands/` hold what each image model did in real tests. Where they disagree with the image-model sections of an `ad-*` skill, the tool notes win.

## What wins when two sources disagree

Highest first. A source lower in the list never overrides one above it.

1. **The approver's decision in this session**, written to `log.md`.
2. **The measured floors**: the type floor in design's `reference/canvas-assumptions.md` and the contrast floor that `dsn-contrast` measures. They apply to every piece of text someone must read.
3. **The brand**: the never list, the locked list, `tokens.json` and `canon/`.
4. **Learnings**, for the cases each one names.
5. **Taste rules**: the workspace's `taste/rules/`, then the plugin's.
6. **The format spec** in `formats/`.
7. **`ad-*` methods.**
8. **`dsn-*` craft defaults**, including the default system for a 1080 canvas.

### When a brand value fails a measured floor

A token can sit below the type floor, or a brand colour pair can fail the contrast floor. Then:

- If the text is decoration that nobody has to read, and the token's `$description` says "decorative, not meant to be read", use the token. The floor does not apply.
- Otherwise do not use the value below the floor, and do not change the brand. Make the draft at the floor, write the conflict under "Waiting on a person" in the brand's `context.md`, and mark the draft "floor conflict" in `piece.md`. The approver then either accepts the larger value as a change to the brand (rank 3) or accepts the smaller value for that piece (rank 1). Either choice is logged.

## When a plugin is missing

If a step calls a `dsn-*` or `ad-*` skill and it is not installed, do not improvise its content. Write "skipped: <skill name> not installed" in `piece.md` (or in the review round, for `cd-review`), carry on with the brand's own rules, and tell the studio owner at the end of the run which checks did not run.

## Words

`CONCEPTS.md` holds this repo's words. The other two plugins use some of the same words for other things. Inside a workspace these names apply:

| Say | For | Not |
| --- | --- | --- |
| brand brief | `brief.md` | "the brief" alone |
| visual brief | `pieces/<piece>/visual-brief.md` | "the brief" alone |
| image spec | what `ad-brief` writes for one image | "brief" |
| direction | `direction.md` | the clause set `ad-rules` writes |
| never list | the "Never" section of `direction.md` | "prohibition", "proscription" |
| canon | approved pieces in `canon/` | "key frame", "exemplar" |
| hand | a tool in `hands/` | "maker", "executor" (those words mean whoever makes the piece, a person or a tool) |
