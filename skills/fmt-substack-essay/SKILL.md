---
name: fmt-substack-essay
description: Write, improve or check a Substack essay that carries one idea (usually a branch of the person's body of work), built from their real material using a library of 16 title moves, 9 subtitle jobs, 15 opening moves, 13 essay structures, 19 long-form inside moves and 57 sorted essays from six newsletters. Use for any request to write an essay or a newsletter issue for Substack, fix a title, subtitle or opening, judge an essay draft, or plan which kind of essay some material can carry. Not for LinkedIn posts (use fmt-linkedin-post) or the essay's images (use fmt-post-visual).
---

# Substack essay

An essay is a title and subtitle that earn the open, an opening that earns the scroll and says what the reader will get, a body that keeps that promise across sections, and a close the reader leaves with. Each part is a move: a job done to the reader, chosen for the material the person has, not for the topic. This skill carries the library of those moves and runs the chain that uses it.

It works like `fmt-linkedin-post`, with two differences that come from the library:

- **The hook is three things.** The title, the subtitle and the opening each do their own job, and the reader meets them in that order. The title is read in an inbox next to dozens of others; it does more of the work than a LinkedIn hook does.
- **The title doesn't pick the structure.** On LinkedIn the hook move predicts the body. Here it mostly doesn't, so the structure is chosen from the material (a real progression asks for a ladder, a method you've used asks for a protocol or a worked case), and the title is chosen to sell what that structure delivers.

## Files in this folder

- `library/hook-moves.md`: 16 title moves, 9 subtitle jobs, 15 opening moves. Each move card has the job, the mechanism, what it needs, the shape, how it fails, what it's good for, and examples.
- `library/body-moves.md`: 13 essay structures, the 19 inside moves long-form adds on top of the nine LinkedIn ones, 9 new closes, the furniture (paywalls, plugs, sign-offs), and the notes from the sort.
- `library/essays-sorted.csv`: the index of 57 essays tagged with title move, subtitle job, opening move, structure, inside moves, close, furniture, access and engagement relative to the writer's own set, with the opening lines, notes and URLs.
- `library/essays/<ID>.md`: the full text of each essay, one file per ID, with its tags in the frontmatter. Read the full essay of every example you pull. Paid essays hold only the free preview. To add an essay, add a row to the CSV and a file here with the same ID.
- `stages/moves.md`, `stages/draft.md`, `stages/judge.md`: the three stages.

The inside moves M1 to M9 (context block, the turn, evidence pair, data line, side-by-side, analogy, other side taken seriously, subject's own words, meaning line) have their cards in `../fmt-linkedin-post/library/body-moves.md`. The essay library uses the same codes and doesn't repeat them.

## Where things come from and where they go

- **Material** comes from the four places `CLAUDE.md` rule 1 names: what the person says, `material/`, `inbox/`, and the canon and idea bank (by ID). The moves stage reads them first and only asks the person about what's missing.
- **The idea** comes from a confirmed POV or a branch (`canon/person/povs.md`, `canon/person/branches.md`). An essay carries one idea. A POV of forming or exploring confidence can carry an essay only with `thinks_out_loud: yes` in the brief (`CLAUDE.md` rule 2).
- **The channel's job, cadence, mix and selling rule** come from the channel file the strategy wrote for Substack (`canon/strategy/channels/substack.md`, or `newsletter.md` if that's the name it used).
- **The brief** is the piece's `brief.md`, made from `templates/piece/brief.md`. The moves stage fills its format plan section.
- **Voice** comes from `canon/voice/voice-guide.md`. Any rule the person has about essays (how to open, what kind of examples to use, how to sign off) lives there, not in this skill.
- **Drafts and reviews** go in the piece's folder as `draft-vN.md` and `review-vN.md`.

## Which stage to run

| The person brings | Run |
|---|---|
| An idea, a branch, raw material, or "write an essay about X" | `stages/moves.md`, then `stages/draft.md`, then `stages/judge.md` |
| A brief already filled in | `stages/draft.md`, then `stages/judge.md` |
| A draft they wrote or got elsewhere | `stages/judge.md` |
| "What should I call this?", "fix my title", "fix my opening" | `stages/moves.md` steps 1, 3 and 4 on the draft's idea, then `stages/draft.md` step 2 only, against the body that exists |
| "What kind of essay is this?" | `stages/moves.md` only |
| An essay that needs a featured image or a diagram | Hand it to `fmt-post-visual` |
| An essay that should become LinkedIn posts | `fmt-linkedin-post`, one post per leaf, each pointing back to the essay |

Read the stage file before running it. Each stage reads the library cards it needs; do not work from memory of the cards.

## Rules that hold across all three stages

- Inventory before moves. A move or a structure is available only when the material it needs is there. Never invent a number, a name, a quote, a story or a case to open a gate.
- One essay, one idea. Every section serves it. If the material holds two ideas, it's two essays.
- Draft and judge are separate passes. The pass that wrote the draft does not judge it. On a second draft, the judge starts from the beginning.
- Supplied copy and source quotes: CLAUDE.md rule 3.
- The house rules (`skills/craft-house-rules`) (section E of `stages/judge.md` checks them) are failure conditions, not preferences. They apply to every essay, every title and every subtitle.
- Each essay stands on its own. A reader who never read the last one can follow it.

## Voice

The draft stage follows the voice order in `skills/craft-house-rules` ("The voice order"): the rewrite pairs, the voice guide when it exists (including any rules about essays), five to eight of the person's own pieces from `material/`, and plain writing only when none of those exists.

## Improving the chain

When an essay fails in the judge or in the inbox, the fix is usually in a card, not in a stage: a gate that was too loose, a "how it fails" item that was missing, a pairing that doesn't hold. Edit the card. Essay test briefs with known-good outcomes are still to come (`tests/README.md` says so); until they exist, rerun the tests in `tests/studio/` that touch the writing chain after any change to a card or a stage. Six cards rest on one example each and are marked thin (T12, T13, T15, O12, E12, E13); a larger library should fill them out or merge them.
