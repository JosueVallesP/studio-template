---
name: cd-review
description: Use on every piece before a person sees it, or on any image to check against a brand. Independent personas return pass, revise or sent back per draft with findings.
argument-hint: "[brand slug] [piece slug | path to an image] [mode:non-interactive]"
---

# /cd-review

**Outcome:** a new round in `pieces/<piece>/review.md` with a verdict per draft (pass, revise, sent back) and findings that each name the draft, the reviewer, the rule or brand line it rests on, what's wrong, and what would fix it.

**Done:** every selected persona ran on every draft (or the review says which didn't and why); findings are merged without duplicates; each draft has a verdict; the round is added to `review.md`; the run ends on one of the last lines below.

**Next:** back to `/cd-make`, which acts on each draft's verdict, or to a person.

**Not:** fixing drafts. Review says what's wrong and what would fix it; `cd-make` does the fixing. And not approving: a pass means "ready for a person," never "approved."

## Step 0. Load

Resolve paths and load rules, learnings and the format spec as `<plugin>/AGENTS.md` describes. Read `<brand>/direction.md`, `system/tokens.json`, `brief.md` (the "Proof of caliber," audience and associations sections), the piece's `visual-brief.md`, and the file list of `canon/`.

Every draft needs a rendered image in `drafts/` that a reviewer can look at. If a draft only exists inside a tool, export or screenshot it first (each `hands/` file says how). If a draft can't be rendered, stop: `Review blocked: <draft> has no image`.

**Image-only route.** Given a path to an image instead of a piece, review it against the brand with no visual brief. Skip the personas the catalog marks as needing a brief, and write the review to `<brand>/reviews/<YYYY-MM-DD>-<image name>.md`.

## Step 1. Pick the personas

Read `references/persona-catalog.md`. Fidelity and caliber always run. The others run when the catalog's condition matches this piece. Skipping the catalog means running everything on everything, which buries the findings that matter.

## Step 2. Run them independently

Read `references/dispatch.md` before starting any reviewer. It lists exactly what each reviewer's prompt must carry; a reviewer missing the brand files or the learnings will judge against generic taste instead of this brand.

Run each persona as its own sub-agent, in parallel when the host allows. If sub-agents aren't available, run them one after another yourself, reading each persona file fresh, and note in the round that the reviews weren't independent.

## Step 3. Merge

Read `references/findings.md` for the finding format and how to set severity. Merge duplicates (two personas flagging the same thing become one finding naming both). Drop findings with no rule, learning or brand line behind them; taste with no source is the reviewer's default. Keep every "Possible new default" note the sameness reviewer returns, whatever its source; `cd-learn` reads them.

## Step 4. Verdict per draft

- **pass:** no `must` findings.
- **revise:** one or more `must` findings that a new draft can fix.
- **sent back:** a finding marked "Sends back: yes" (the idea itself is thin, generic or has no shape). That goes to the brief's author, not to another draft.

Add a new section to `review.md` headed `## Round <n>: <date>`. Never overwrite an earlier round; the history of what reviewers said and what people later decided is what `cd-learn` learns from. In the section: the verdict table (draft, verdict, count of must and should findings), then findings grouped by draft, `must` before `should` before `consider`, then the "Possible new defaults" notes.

## The last line

One line sums up the round, taking the first that applies: any draft blocked, then any sent back, then any to revise, then all passing.

## Non-interactive runs

Run normally. Review never needs a person, and never approves anything.

## Last lines

- `Review blocked: <reason>`
- `Review: sent back (<reason>)`
- `Review: revise (<n> drafts, <n> must findings)`
- `Review: pass (<n> drafts)`
