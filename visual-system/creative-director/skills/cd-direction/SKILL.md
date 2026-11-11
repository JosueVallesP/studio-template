---
name: cd-direction
description: Use after cd-intake to turn a brand brief into a visual direction a designer or agent can work from, or to revise one. Finds the contradiction, or locks existing rules.
argument-hint: "[brand slug] [revise: what to change]"
---

# /cd-direction

**Outcome:** a `direction.md` specific enough that two designers working from it would make similar choices: the target association, how it shows the person's caliber, the visual codes, the recurring shapes, the never list, and (in new and rebrand modes) the contradiction that ties it together. Approved by a person.

**Done:** `direction.md` is complete for the brand's mode, every test in its Tests table has an answer, a person has approved it (status `approved`, with name and date), `log.md` and both `context.md` files are updated, and the run ends on one of the last lines below.

**Next:** `/cd-system`.

**Not:** making finished pieces, or writing tokens. Direction decides; the system encodes.

This is the step most likely to produce polished but interchangeable brands. Use the most capable model available. Every choice in the direction needs a line in `brief.md` or `references.md` behind it. A choice with no source is the model's default, and defaults are what make brands look the same.

## Step 0. Load

Resolve paths and load rules and learnings as `<plugin>/AGENTS.md` describes: always `caliber.md` and `copy-on-visuals.md`, `keep-mode.md` in keep mode, and any learning about directions or this brand. Read `<brand>/context.md`, `brief.md`, `references.md`, the file list of `assets/`, and `canon/` if it has anything.

If `brief.md` has Open questions that block direction (no proof of caliber, no associations, no audience), stop and end on `Direction blocked: brief incomplete (<what>)`.

## Step 1. Route by mode

Read the brief's `mode`, then read exactly one of these before writing anything:

- `keep`: read `references/keep-extract.md`. Skipping it means inventing a direction for a brand whose job is to stay the same.
- `refresh`: read `references/refresh.md`. Skipping it means changing the very parts people recognize.
- `rebrand` or `new`: read `references/contradiction.md`. Skipping it means picking opposites because they look interesting, which is the costume failure.

Follow that reference to fill `direction.md`.

## Step 2. Caliber, shapes and the never list (every mode)

Whatever the mode, fill these three sections of `direction.md`:

- **How it shows caliber.** Which lines in "Proof of caliber" the look carries, and the specific risk for this person: are they more likely to be oversold or undersold? Use `<plugin>/taste/rules/caliber.md`.
- **Recurring shapes.** Three to six shapes, objects or scenes that come from the person's own thesis, field or metaphors, each with a line on why it belongs to them. These let the work be recognized without repeating one scene. In keep mode, list the ones the existing brand already uses.
- **Never.** Concrete, checkable things this brand never does. Draw them from the "avoid" section of the brief, the references that didn't fit, and the contradiction's failure modes.

## Step 3. Run the tests

First run the two checks "Direction" in `<plugin>/ROUTING.md` names on the never list and the visual codes. A never line nobody could break, or a figure with no unit, gets rewritten before the tests below.

Fill the Tests table in `direction.md`. In keep mode, mark the contradiction tests (truth, one sentence, removal, felt) "n/a: keep" and answer the rest. The swap test matters most: if the direction would fit another person in their field just as well, go back to the step it points to. Don't patch a failed test with words.

## Step 4. Propose

Set `status: proposed`.

**In new and rebrand modes,** read `references/show-directions.md` and show the approver three directions, each across the same eight boards with the same content. Skipping it means the approver chooses from a paragraph, and the choice then takes many rounds. Keep only the chosen direction in `direction.md`. Directions the approver liked but did not choose stay on the canvas as the record.

**In keep and refresh modes,** show a short version: the target association, the locked list, the visual codes table and the never list. Offer, without doing it unasked, to make two or three quick sample applications with `/cd-make` so they can see the direction before approving.

## Step 5. Approve and close

Only the approver approves. When they do, set `status: approved`, fill `approved_by` and `approved_on`, add a row to Change history, and append to `log.md`. If they reject or change parts, revise and propose again; log each round with their words.

Rewrite `<brand>/context.md` (status `system`) and the brand's row in `<ws>/context.md`.

## Revising an approved direction

With `revise:` in the arguments, change only what the approver asked, bump `version`, propose the change as a diff, and treat approval exactly as above. In keep mode every revision needs approval, however small.

## Non-interactive runs

Draft the direction through Step 3. Wherever a reference says to ask or decide with the person (sharpening the target association, choosing between two contradictions, a refresh that may be a rebrand), write the question under "Waiting on a person" in the brand's `context.md`, keep both options in the proposal, and carry on. Leave `status: proposed`, never approve, and end on `Direction proposed: waiting on approval`.

## Last lines

- `Direction approved (v<n>)`
- `Direction proposed: waiting on approval`
- `Direction blocked: <reason>`
