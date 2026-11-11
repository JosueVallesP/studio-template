---
name: setup-check
description: >-
  The last setup stage. Confirms the studio works for this person: every file and script in place, the manifest and the instance in step, the minimum canon met and the strategy confirmed, and then one test piece run through the whole crew to the producer's gate. Ends with a pass, or a list of what's missing in the person's words. Its install half also runs on its own at the first session after a new studio version arrives, so a pushed update that broke something is caught before the person meets it. Use when setup-start reaches the check stage, or when someone says "check my setup", "is everything working", "/check".
---

# Setup check

You are the last thing between setup and the first real week. A person who passes this can run the studio alone. A person who doesn't gets a short list of what to fix, not a shrug.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Procedure

### 1. The install

Run `bash scripts/setup-check.sh`. It checks the studio files, the scripts, the manifest against `studio-source.md`, the person-owned folders, the minimum canon, the confirmed strategy, the channel files, the voice guide, and that the canon itself has no em dashes. Every FAIL line names the fix. Stop here if anything fails; say what to do in one line each, in the order that unblocks the most.

**On the `interviews-skipped` path** (`stage: interviews-skipped` in `canon/setup-progress.md`, written by `/start` when the person skips the interviews): the minimum canon and the confirmed strategy are not expected, and the script reports them as "not yet", not as fails. Check what the direct path needs instead: the install lines pass, `material/` or `inbox/` holds at least one text file of theirs, and, if a strategy exists, its frontmatter has `person_confirmed:` or `status: confirmed`. Then skip step 2's pipeline run and make one test post through `/post` (`skills/job-post`) from their material, judged by the `judge` agent in a fresh context. Pass when the install passes and that post reached its review with no invented material. Write the result as in step 3 and set the stage to `setup done`.

### After an update

When a new studio version reaches the instance (pushed into a built-for-you studio, or `/update`), the session-start hook runs `scripts/setup-check.sh` once and prints an `AFTER UPDATE` block with only the FAIL and warn lines. Nobody asked for it, so it waits like any finished work (CLAUDE.md rule 9): after the person's first message is handled, one line per problem in plain words with what fixes it, and an offer to make the safe fixes (`/tidy` for a size warning, the step a FAIL line names). A check that passes says nothing to the person. The checked version is kept in `sessions/.checked-version`. The test piece in step 2 never runs after an update; it belongs to setup.

Two parts of the script exist for this: **Routing** fails when a studio command is missing from CLAUDE.md's routing table, and **Size** warns when a bank or log the studio reads often has grown past the point where a session wades through it instead of reading it. A size warning is never a fail.

### 2. The test piece

Run one piece through the crew with the real canon, so the person sees the whole chain once before it matters:

1. **Capture.** Ask the person for one thing that happened this week they have an opinion about, two or three sentences. Run `role-capture` on it. One entry, `ready`.
2. **Build it.** Run `/post` (`skills/job-post`) on that entry, with the person in the room for the stops: what they're saying, the openings, the outline. This is where they meet the first wind and see their idea's record grow.
3. **Draft.** The writer drafts in a fresh context, as `/post` hands it over. Confirm `scripts/check-mechanical.py` passes on the draft.
4. **Review.** The `judge` agent reviews it in a fresh context (or a new chat). Whatever the verdict, that's the result; don't rerun to get a pass.
5. **Show the person** the draft, the review's verdict, its gates and its should lines, side by side, and say what each file is and where it lives. This is the moment they learn what the studio does and doesn't do for them.
6. Leave the piece at `reviewed`. Shipping it is their call, later, through `/review`. Don't push them to ship a test.

### 3. The verdict

Setup needs no shipped piece; this test piece is the one that runs through the crew, and `reviewed` is enough. Pass when the install script passes and the test piece reached `reviewed` with no invented material (the fidelity gates passed, whatever the format and craft checks said). Write the result to `canon/setup-progress.md`: the check item ticked, the date, the test piece's ID. Set the stage to `setup done`.

Otherwise, list what's missing in the person's words, one line each, in the order to fix it, and leave the stage where it is.

### 4. What comes next

Tell them, in a few lines: `/status` is their front door from now on; `docs/operating-guide.md` is the one page on the week (capture, decide, review); the first real week starts with `/capture` and `/brief`. Then stop. Don't mention Notion, Figma or other channels unless `config/tools.md` says they use them. Notion and Figma are quick wins with their own skills (`setup-notion`, `setup-figma`): if one is wanted and not connected, say in one line the phrase that sets it up.

## Never

- Never fix the canon yourself to make a check pass. A missing confirmed entry is the person's to confirm.
- Never rerun the editor to get a better verdict. The test shows the real thing.
- Never ship the test piece.
- Never write facts about the person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
