---
name: cd-intake
description: Starting a brand, or reopening a brief when the person's work or goals changed. Interviews them, sets the mode, and judges the references they like against who they are.
argument-hint: "[person's name or brand slug] [mode:non-interactive]"
---

# /cd-intake

**Outcome:** a brand folder whose `brief.md` a stranger could design from: the person's layers from values to content, the proof of their caliber, who the brand is for, what it should make people feel, the mode with its reason, and their references judged for fit.

**Done:** every section of `brief.md` is filled or listed under Open questions; the mode is set with a reason; `references.md` has a fit judgment for every reference; the person has checked every line marked `(inferred)`; `log.md` and both `context.md` files are updated; the run ends on one of the last lines below.

**Next:** `/cd-direction`.

**Not:** choosing colors, type or any visual direction. Intake records what is true and what exists. Direction decides.

This is the step where quality is won or lost. A thin brief gets a polished but interchangeable brand. Use the most capable model available and take the time the person gives you.

## Step 0. Find or make the workspace

Resolve `<plugin>`, `<ws>` and `<brand>` as `<plugin>/AGENTS.md` describes. Read `<plugin>/AGENTS.md` now if you haven't this session; it holds the write boundaries this skill follows.

If no workspace exists, this is the only skill allowed to make one. Ask the studio owner to confirm the folder, then copy everything inside `<plugin>/workspace-template/` into it, including the hidden `.creative-director/` folder and the hidden `learnings/.last-run` file. Ask who runs this studio and write that name to `studio_owner` in the config. In a non-interactive run, don't create one: end on `Intake stopped: no workspace`.

Read `<ws>/context.md`.

## Step 1. Find or make the brand folder

Make the slug from the person's name: lowercase, hyphens, no accents (`josué-valles` becomes `josue-valles`). If `<brand>` exists, this is a reopen: read its `context.md` and `brief.md`, ask what changed (in a non-interactive run, use only the documents provided), and update only those sections. Otherwise copy `<ws>/<brands_root>/_template/` to `<brand>`, then ask the studio owner who signs off for this brand. Write that name to `approver` in the frontmatter of `brief.md`, or leave it empty when the studio owner signs off.

## Step 2. Read everything before asking anything

Collect what already exists and fill the brief from it first, so the interview only asks what's missing:

- Documents the person shares: a Personal Monopoly document, a messaging framework, a bio, a deck, notes.
- Their site and public profiles. For a site, a teardown gives you the existing colors, type and layout; use the `site-teardown` skill when it's available, otherwise fetch and read the pages.
- Past pieces they're proud of, and ones they aren't.
- Their own material for future pieces: headshots, logo and mark files, a bio, talk descriptions, testimonials they have permission to use.

Write what you find into `brief.md`, marking every line that is your reading rather than their words with `(inferred)`. Save other people's work they like to `<brand>/references/`, and their own material to `<brand>/assets/` with a line in its README.

## Step 3. Settle the mode first

Read `references/modes.md` before asking anything about style. Skip it and you'll run the wrong interview: keep mode needs an inventory of the existing brand, while new and rebrand need the full diagnosis.

Ask about the mode before anything else, record it in the brief's frontmatter with the reason in the person's words.

## Step 4. Run the interview

Read `references/interview.md` before the first question. It holds the question bank, the order, and how to push past vague answers. Without it, you'll collect adjectives instead of evidence.

Ask one question at a time and wait. Ask only what Step 2 didn't answer. Keep the person's exact words. If they ask you to skip questions, fill the gaps yourself and mark them `(inferred)`.

## Step 5. Collect and judge their references

Read `references/references-check.md` before asking about references. It covers what to ask beyond "what brands do you like," and how to tell someone a look they love doesn't fit them.

Fill `references.md`: every reference, liked or disliked, with their reason, what it signals, and whether it fits them.

## Step 6. Check with the person

Show the person three things, briefly: the lines marked `(inferred)`, the mode and its reason, and the "Reading" paragraph from `references.md`. Fix what they correct. Remove the `(inferred)` mark from lines they confirm.

## Step 7. Close

1. Append to `<brand>/log.md`: `- <date> · intake · approved · "<anything they said about the brief>" · reviewer: <person>`.
2. Rewrite `<brand>/context.md` (status: `direction` if the brief is complete, `intake` if paused) and the brand's row in `<ws>/context.md`.
3. End on one last line.

## Non-interactive runs

With no person present, do Steps 0 to 2 only (and only with an existing workspace), mark everything `(inferred)`, list what the interview must still cover under Open questions, and end on `Brief paused: needs interview`.

## Last lines

- `Brief complete (mode: <mode>)`
- `Brief paused: <what's missing>`
- `Intake stopped: no workspace`
