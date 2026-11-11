---
name: fmt-linkedin-post
description: Write, improve or check a LinkedIn text post or hook that carries one idea to a reader, built from the person's real material. The idea and what the reader needs to get it decide the shape and length; then a library of 57 idea briefs, 18 hook moves, 9 body structures and 357 sorted example posts supplies the parts. Use for any request to write a LinkedIn post, fix a hook, judge a post draft, or plan which kind of post some material can carry. Not for the post's visual, carousel or field guide (use fmt-post-visual).
---

# LinkedIn post

A post carries one idea to a reader. What the reader needs in order to get that idea (the questions they'd ask, in the order they'd ask them) decides the shape and the length. Only then come the moves: the hook that raises the first question, the inside moves that answer the rest, the close. Each move is a job done to the reader, chosen for the material the person has. This skill carries the library of those moves and runs the chain that uses it: the library is a drawer of parts, never a plan the idea has to fit.

## Files in this folder

- `library/hook-moves.md`: 18 hook moves. Each card has the job, the mechanism, what it needs, the shape, how it fails, what it is good for, and examples.
- `library/body-moves.md`: 9 structures, 9 moves inside the body, 6 closes, and the tables showing which structure and close each hook move tends to sit with in practice (a check on a choice, not the way to make it).
- `library/content-moves-sorted.csv`: the index of 357 real posts tagged with hook move, structure, inside moves, close, media type and engagement, with each post's hook (column `Hook`), notes, post URL and visual URL. The examples the chain pulls come from here.
- `library/posts/<ID>.md`: the full text of each post, one file per ID, with its tags in the frontmatter and the hook and body notes. Read the full post of every example you pull, not the hook line alone. To add a post, add a row to the CSV and a file here with the same ID.
- `library/wiki.md`: the front page of the library wiki. It links every idea brief, hook move, structure, move inside the body, close and post type, and each of those entries (in `library/wiki/`) lists the posts that use it and the briefs those posts belong to. The entries point to the cards in `hook-moves.md`, `body-moves.md` and `types/`; the cards stay the source.
- `library/idea-briefs.md` and `library/briefs/<brief>.md`: 57 idea briefs. Each names the idea under a group of posts, the post in one sentence, what a person needs in order to write their own version, the questions to answer, how it fails, the hooks and shapes its example posts used, its close neighbors, and the example posts with a line on how each carries the idea. `idea-briefs.md` sorts the briefs by what the person has and by what the reader leaves with. Use a brief when the person has no idea yet, to find example posts by idea, or to check whether the material on file can carry a post: the brief's "What you need" list is the test. Each post's frontmatter has a `brief` line that links to its brief (`none` when the post carries no reusable idea); give a new post that line too.
- `stages/moves.md`, `stages/draft.md`, `stages/judge.md`: the three stages.
- `types/<type>.md`: the ten post types, each a method built from vetted posts of its kind, with its own gates, steps and judge checks, and its examples in `types/<type>/`. A type adds to a hook move's card; it never replaces the chain. The moves stage picks one (step 3g).

## Post types

| Type | File | What it is |
|---|---|---|
| owned story | `types/owned-story.md` | something the person did, ran, decided or was wrong about |
| borrowed story | `types/borrowed-story.md` | someone else's true story carrying the person's claim, with a verification gate |
| arbitraged content | `types/arbitraged-content.md` | a book, podcast, quote, person or event borrowed to carry the person's own idea |
| newsjacking | `types/newsjacking.md` | this week's news plus the person's read on it |
| op-ed | `types/op-ed.md` | an argument for one of the person's POVs |
| power listicle | `types/power-listicle.md` | numbered lessons, each a claim the reader keeps |
| simple listicle | `types/simple-listicle.md` | a list of things outside the post to go and get (books, tools, people) |
| proof post | `types/proof-post.md` | a result the person produced, turned into an enquiry |
| shortie | `types/shorties.md` | one idea in 15 to 80 words |
| super-specific how | `types/super-specific-how.md` | a procedure the reader can run on Monday |

The person can ask for one by name ("write a borrowed story about this", `/borrowed-story`); otherwise the moves stage offers the one the material fits.

## Where things come from and where they go

- **Material** comes from the four places `CLAUDE.md` rule 1 names: what the person says, `material/`, `inbox/`, and the canon and idea bank (by ID). The moves stage reads them first and only asks the person about what's missing.
- **The brief** is the piece's `brief.md`, made from `templates/piece/brief.md`. The moves stage fills it, including its format plan section.
- **Voice** follows the voice order in `skills/craft-house-rules`.
- **Drafts and reviews** go in the piece's folder as `draft-vN.md` and `review-vN.md`.

## Which stage to run

| The person brings | Run |
|---|---|
| A topic, an idea, raw material, or "write a post about X" | `stages/moves.md` (idea, shape, moves), then `stages/draft.md` (skeleton, body, hooks, close), then `stages/judge.md` |
| A brief already filled in | `stages/draft.md`, then `stages/judge.md` |
| A draft they wrote or got elsewhere | `stages/judge.md` |
| "Which move should I use for this?", "what shape should this post take?" | `stages/moves.md` only |
| A finished post that needs a visual | Hand it to `fmt-post-visual` |

Read the stage file before running it. Each stage reads the library cards it needs; do not work from memory of the cards.

## Rules that hold across all three stages

- The idea before the shape, the shape before the moves. Write the idea in one sentence, work out the reader's questions, and let them set the shape and the length. Then pick moves for the beats.
- Inventory before moves. A move is available only when the material it needs is there. Never invent a number, a name, a quote or a story to open a gate.
- Draft in stages, never in one pass: the skeleton, then the body, then the hook written against the body, then the close.
- Draft and judge are separate passes. The pass that wrote the draft does not judge it. On a second draft, the judge starts from the beginning.
- Supplied copy and source quotes: CLAUDE.md rule 3.
- The house rules (`skills/craft-house-rules`) (section D of `stages/judge.md` checks them) are failure conditions, not preferences. They apply to every post the chain produces, for every person it is used for.

## Voice

The draft stage follows the voice order in `skills/craft-house-rules` ("The voice order"): the rewrite pairs, the voice guide when it exists, five to eight of the person's own pieces from `material/`, and plain writing only when none of those exists.

## Improving the chain

When a post fails in the judge or in the feed, the fix is usually in a card, not in a stage: a gate that was too loose, a "how it fails" item that was missing, a close that should have been ruled out. Edit the card. A set of about 20 briefs with known-good outcomes is still to come (`tests/README.md` says so); until it exists, rerun the tests in `tests/studio/` that touch the post chain after any change to a card or a stage.
