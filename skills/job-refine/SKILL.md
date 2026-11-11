---
name: job-refine
description: >-
  Takes any piece the person brings (a draft of theirs, a studio draft, a post that feels flat, a cornerstone essay before it ships) from good to great through craft-refine: checks it against the bar (theirs, on strategy, legible, valuable), finds the single deepest constraint, fixes it, compares it against the best of its kind, and judges it in a fresh context. Says one thing, not twelve. Use for /refine, "this feels flat", "make this better", "is this ready?", "push this one further".
---

# /refine

Read `skills/craft-refine/SKILL.md` first; this command runs it on one piece.

## What it takes

A piece: pasted text, a file in `pieces/<id>/`, or a draft the person wrote themselves (saved to `pieces/<id>/draft-v1.md` under one `## Post`, with a brief from `templates/piece/brief.md` that sets `path: direct` and `written_by: the person`, as the template defines it, so the pairs and the judge work the same way). Plus, when the person says it, `kind: test` or `kind: cornerstone`; otherwise the format and channel decide (`craft-refine`, "The bar depends on the piece").

## How it runs

1. **The bar.** Read the piece against the four parts of great. Relevance: run the swap test and trace the facts to the person's material; strategy: check the thesis, the branch, the reader in `canon/strategy/`. If either fails, stop and say so: "This isn't yours yet" or "This doesn't serve what you're building toward"; offer `/shape` or the strategist. Don't polish it.
2. **The one constraint.** Walk the seven levers deepest first (`craft-refine`). Run `python3 scripts/check-prose.py <draft>` and `python3 scripts/voice-diff.py <draft>` for the hygiene fails, which get fixed regardless and aren't the one thing. Name the deepest failing lever with the quoted line.
3. **Fix it, compare, cut.** Fix that one lever in a fresh pass of the paragraphs it touches; keep what passed. Pull the two or three best examples of the same move from the format's library and the person's own best pieces; hold the piece against them for what they do, never their words. Cut what isn't working.
4. **Judge.** Hand the piece to the `judge` agent (or a fresh chat) with the format's judge stage. The pass that fixed never judges.
5. **Stop or go round.** A test piece stops: the verdict, the one thing fixed, the person decides. A cornerstone goes one more round from step 2, with the comparison written out, then the person's final read.
6. **Learn.** If the person edits the result, the pair goes to `bank/rewrites/` with its changes tagged (`scripts/rewrites.py`).

## What it says

Under 120 words for a test piece: the verdict, the one thing and its fix with the line quoted, and the next step ("ship it", "one more pass", or "fix those two lines yourself"). A cornerstone adds what the comparison showed, two or three lines.

## Never

- Never polish a piece that fails relevance or strategy.
- Never hand back a list of notes. One thing, then the verdict.
- Never judge your own fix.
- Never run a third round on a test piece unasked.
