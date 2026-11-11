---
name: cd-system
description: Use after a direction is approved or changed, or to check a tool for drift. Turns the direction into tokens and pushes them one way out to the tools, recording where.
argument-hint: "[brand slug] [check | sync <tool>] [mode:non-interactive]"
---

# /cd-system

**Outcome:** `system/tokens.json` holds every value the direction implies, `system/bindings.yaml` says where the brand lives in each tool, and each tool's copy matches the repo.

**Done:** a person has approved the tokens; the package in `system/package/` builds every example and has passed a cold test; each tool in the config's `hands` list is synced or listed as skipped with a reason; `bindings.yaml` is current; both `context.md` files are updated; the run ends on one of the last lines below.

**Next:** `/cd-make`.

**Not:** deciding anything the direction didn't. If a value isn't implied by `direction.md`, it goes back to `/cd-direction`, not into the tokens.

## Step 0. Load and check

Resolve paths as `<plugin>/AGENTS.md` describes. Read `<brand>/context.md`, `direction.md`, `system/tokens.json` and `system/bindings.yaml`.

If `direction.md` isn't `status: approved`, stop: `System blocked: direction not approved`.

With `check` in the arguments, skip to Step 5.

## Step 1. Write the tokens

Read `references/tokens.md` before writing. It says how each line of the visual codes table becomes a token and what to do with values the direction leaves open. Skipping it tends to produce tokens that look complete but were invented.

Draft `system/tokens.json` in the W3C Design Tokens format, starting from the template's structure. Show the approver a short table of the values and apply them once they approve. In keep mode, every value must trace to the existing brand.

**Figma as source.** If `bindings.yaml` says `source_of_truth: figma`, read the values from Figma instead of the direction, show the approver the table the same way, and write `tokens.json` once they approve.

## Step 2. Build the package

Read `references/package.md` before building. It says what goes in `system/package/`, why the tokens are the one source, and how to run the cold test. Skipping it leaves the look in one session's memory, and the next agent has to guess.

Start from `<plugin>/kit/`. Carry over the art functions written during `/cd-direction`. Build the reference pieces and the three sheets, run the cold test, and fix the package until a cold agent's pieces match.

When the approver is still choosing between directions, package each one and say so in `context.md`. The tokens are approved when the approver picks.

## Step 3. Sync each tool

Read `references/sync.md`, then the `<plugin>/hands/<tool>.md` file for each tool in the config's `hands` list. Sync runs one way, from the repo out (or from Figma out, when Figma is the source).

For each tool, record ids and the date in `bindings.yaml`; that file needs no approval. A tool that can't be reached (Paper with no computer linked, a connector that isn't connected) is skipped with the reason, never faked.

Pushing to a client's shared Figma library needs approval. Creating or updating the brand's own Design System artifact and private files doesn't.

## Step 4. Train styles only from canon

A Recraft style or a Flora trained style needs canon images. With fewer than three canon pieces, skip style training; that's expected for a new brand and doesn't make the sync partial. When there's enough, follow `hands/recraft.md` or `hands/flora.md`, say the cost first, and wait for a yes above `credit_confirm_usd`.

## Step 5. Check for drift

For each tool in `bindings.yaml`, read its current values and compare them with `tokens.json`. List every mismatch as a table. Don't overwrite a mismatch without asking: a person may have changed it on purpose. Ask whether the repo or the tool is right, sync that way, and log their choice in `log.md`.

## Step 6. Close

Note what synced, what was skipped and any drift under "Last session" in the brand's `context.md`. When the tokens are approved and at least one tool is synced, set the brand's status to `producing`. Log the token approval in `log.md`. Update the brand's row in `<ws>/context.md`.

## Non-interactive runs

Run Step 5 only and report drift. Never change tokens and never overwrite a tool.

## Last lines

- `System synced (<tools>)`
- `System partial: <tools synced>; skipped <tool>: <reason>`
- `No drift`
- `Drift found: <n> mismatches`
- `System blocked: <reason>`
