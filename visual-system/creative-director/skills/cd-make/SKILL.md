---
name: cd-make
description: Making any visual a brand needs, including formats no skill was built for. Takes a visual brief, picks the tool, drafts, and runs review before a person sees it.
argument-hint: "[brand slug] [piece slug or a description of what to make] [mode:non-interactive]"
---

# /cd-make

**Outcome:** two or three reviewed drafts of one piece, in the brand's look, that each carry the visual brief, ready for a person to pick, change or reject.

**Done:** `pieces/<piece>/` holds the visual brief, the drafts, `piece.md` and a `review.md` from `/cd-review`; drafts that failed review were revised or dropped; the approver has seen the survivors; `log.md` and both `context.md` files are updated; the run ends on one of the last lines below.

**Next:** a person picks. A piece goes into `canon/` only when a person asks for it.

**Not:** deciding whether an idea is worth making. That belongs to whoever wrote the visual brief. This skill can send a brief back; it doesn't rewrite the idea.

## Step 0. Load

Resolve paths and load rules, learnings and the format spec as `<plugin>/AGENTS.md` describes. Read `<brand>/context.md`, `direction.md`, `system/tokens.json`, `system/bindings.yaml`, and the file lists of `canon/` and `assets/`.

Check the brand is ready:

- `direction.md` must be approved, or stop: `Make blocked: no approved direction`.
- No token the piece needs may have an empty value, or stop: `Make blocked: token <name> is empty`.
- The brand's status must be `producing`, which `cd-system` sets once tokens are approved. Otherwise the tokens may still be placeholders: stop on `Make blocked: system not built`.

**Sample route.** When `/cd-direction` asks for sample applications of a proposed direction, skip both checks. Take values from the visual codes table in `direction.md` instead of `tokens.json`, write the visual brief yourself with `written_by: cd-direction`, skip the idea gate, and label every draft "sample, direction not approved." Samples still go through review.

## Step 1. Get the visual brief

Read `references/visual-brief.md` first. It's the contract between this skill and whatever writes the brief, including which gates apply to which kind of piece.

- If `pieces/<piece>/visual-brief.md` exists, use it.
- If not, and the config's `visual_brief_source` is `content-system`, tell the studio owner the brief should come from their content system and ask whether to write one here instead. In a non-interactive run, stop on `Make blocked: no visual brief`.
- Otherwise create the piece folder from `<ws>/<brands_root>/_template/pieces/_piece-template/`, then write the brief with the studio owner, one question at a time. Non-interactive: `Make blocked: no visual brief`.

Run the gates that apply. If one fails, write the reason under "Returned" at the top of the brief, set `status: returned` in `piece.md` and end on `Brief returned: <reason>`. A generic idea on a beautiful canvas is still generic.

## Step 2. Pick the format and the tool

Use the format spec named in the brief. If there isn't one, write the size and constraints into `piece.md` and note that the format has no spec yet.

Read `references/choose-hand.md`, then the chosen tool's `<plugin>/hands/<tool>.md`. Choose only from tools listed under `hands` in the config. Record the choice and the reason in `piece.md`.

## Step 3. Make the drafts

Set `status: drafting` in `piece.md`.

For any diagram, framework, chart or field guide, read `references/visual-method.md` before drawing. Without it you'll reach for a familiar template shape instead of the one the idea needs.

When the question in front of you is craft rather than brand, hierarchy, grid, spacing, type, colour, contrast, imagery or sequence, read `references/craft.md`. It routes each question to the design plugin skill that owns it, and carries the two shared canvas facts. The order of what wins is in `<plugin>/ROUTING.md`: the brand beats a craft default, and a measured floor beats the brand. Record in `piece.md` any case where you followed one over the other.

Make two or three drafts that differ in a real way (a different mechanic or a different composition), not three versions of one layout. Use only values from `tokens.json`, shapes from "Recurring shapes," words from the brief, and material from `assets/`. Mark any word you add yourself as proposed. Save each draft to `pieces/<piece>/drafts/` as a rendered image, with its source next to it (a file, a link to the tool, or both).

Before sending a prompt to an image model (Recraft, Flora), follow "Making" in `<plugin>/ROUTING.md`: write the in-frame checks first.

Before any paid generation, say the cost. Above `credit_confirm_usd`, wait for a yes; in a non-interactive run, skip that tool instead.

## Step 4. Review before anyone sees it

Run `/cd-review <brand> <piece>`, then read the verdict table in `review.md` and act per draft:

- **pass:** keep it.
- **revise:** fix what its findings say. Review again, up to two rounds in total.
- **sent back:** set `status: returned` in `piece.md` and end on `Brief returned: <reviewer's reason>`, even if other drafts passed. The idea needs work before more drawing.
- **blocked:** end on `Make blocked: review couldn't run (<reason>)`.

Drop a draft that still needs revising after two rounds, and note why in `piece.md`. If no draft survives, end on `Make blocked: no draft survived review`.

## Step 5. Show the approver

Set `status: ready` in `piece.md`. Show the surviving drafts with one line each on what differs between them and what the review said. Ask which to keep, change or drop. Log every decision in `log.md` with their words. A change request starts a new round at Step 3.

If they approve one, set `status: approved` in `piece.md`. Ask whether it should go into `canon/` to guide future work. Promote it only if they say yes, following "Brand admin" in `AGENTS.md`.

## Step 6. Close

Rewrite `<brand>/context.md` (Recent pieces table) and the brand's row in `<ws>/context.md`.

## Non-interactive runs

Run Steps 0 to 4 on an existing visual brief. Set `status: ready` in `piece.md`, leave the surviving drafts for the approver and end on `Drafts ready (<n>)`.

## Last lines

- `Drafts ready (<n>)`
- `Piece approved: <piece>`
- `Brief returned: <reason>`
- `Make blocked: <reason>`
