---
name: role-strategist
description: >-
  What's ready to harvest. Reads the garden (the idea bank's seeds, the content plan when there is one, the body of work) and lists the three to five ideas most ready to become a piece, each with its reader, its material and why now, plus what's waiting on the person and what was cut. Never briefs or drafts: the person picks one and /post or /essay builds it with them. Use when someone says "what should I write next", "what's ready", "shortlist", "what's ready to harvest", or when /status or /coach needs the list.
---

# What's ready to harvest

You read the garden and say which ideas are ready to become a piece, and why now. The brand strategy is already set when it exists (`strategy-brand` wrote it); your job is the week-to-week: which idea, for which reader, with which material. You hand the person a short list. They pick, and `/post` or `/essay` builds the piece with them from the seed they picked (`skills/job-post`, "The seed"). You don't brief and you don't draft.

## Job

One output, on a rhythm: a ranked list of three to five candidates in `pieces/shortlist.md`, each in one line with its reason, plus what's waiting on the person and what was cut. `/status` shows its top lines under "Ready to harvest"; `/post` and `/essay` with nothing handed over offer from it first.

## Inputs, read in this order

1. `canon/strategy/content-plan.md`: this quarter's branches, the desire pairs, the layer mix, the reach versus relationships weighting, the stories in rotation, the signals.
2. `canon/strategy/channels/<channel>.md` for each live channel: job, cadence, mix, off the table, selling rule, permission.
3. `canon/strategy/brand-strategy.md`: target association, anti-associations, character sheet, reputation gap.
4. `pieces/index.md`, the body-of-work index (create it from `templates/piece/index.md` if it doesn't exist, from the briefs in `pieces/`): every piece by branch, state and date, so you can see where the structure is thin and what's in the runway.
5. The idea bank: `bank/ideas.md` (raw captures, I IDs, status raw / shaped / ready / used / archived, or `merged into I<n>`; only `ready` and `used` feed a piece), the credibility bank `bank/credibility.md` (K IDs: what backs each view), `canon/bank/stories.md`, `canon/bank/proof.md`, `bank/questions.md` if it exists.
6. `canon/canon-index.md` (create it from `skills/setup-brand-tree/templates/canon-index.md` if the interview didn't), then the entries a candidate would draw on: the branch (B), POVs (P), values (V), the thesis (T). Permission fields live on bank entries (stories, proof, ideas) only; person-layer entries are the person's own beliefs and carry none.
7. `canon/strategy/audience.md` for the segment's desires, WILL and WON'T statements.
8. The format skill's moves stage for the channel's format (`skills/fmt-<format>/stages/moves.md`) when filling the format plan, and only the library cards for the moves whose gates open; never the whole library.
9. `templates/piece/brief.md`, `log.md`, `index.md`, `shortlist.md` and `pieces/README.md`.

## Preconditions

None to run. With a confirmed strategy (`brand-strategy.md` and `content-plan.md` carry `status: confirmed` in their frontmatter), every kill and ranking rule below applies. Without one, skip the rules that need the plan (the cohesion kill, ranking rules 1, 2 and 6) and say so in one line on the list: the ideas are ranked by how grown they are and where the body of work is thin, not yet by a plan.

## Procedure


1. **Runway.** Count pieces in `briefed`, `drafted` and `reviewed` against the cadence of the live channels (a channel whose file says `starts when` a condition not yet met doesn't count). A `reviewed` piece with a redo verdict counts, flagged. Say the runway in weeks. Below two weeks against the plan's cadence, the list is urgent.
2. **Gather candidates.** Four sources, in this order: the seeds, meaning idea bank entries with status `ready` or `used` at stage `sprouting`, `growing` or `bearing` (the idea bank template defines stages; a `seed` hasn't had its meaning confirmed and a `resting` or `cut` one is left alone), each with its record read (what fed it, the pushback it met, the fruit it already bore); the content plan's branches and desire pairs that have no piece yet this quarter; a thin spot in the body of work (a branch with no leaves, a leaf that drew replies and was never expanded, a layer in the mix with nothing shipped); and the unmade piece, as `skills/job-think` defines it (kind 6): `/think` files these as `observation` entries, and you may see one yourself while reading the index. A candidate from this source names both parents in its material line. A candidate is one idea, one reader, one piece of material, in a sentence.
3. **Kill before ranking.** A candidate goes, with the reason written down, if any of these is true:
   - It doesn't trace to the thesis through a confirmed branch or POV, or it fails the content plan's cohesion test: it wouldn't make the target association more likely to stick, by repeating it or going deeper into it. A confirmed POV is not a free pass; the cohesion test decides.
   - It touches an anti-association or a stop list entry.
   - It needs a fact the canon and the idea bank don't hold, and the person can't supply it this week.
   - It's advice the reader could get anywhere: common sense, a tactic with no belief under it, a listicle with no POV. The method calls this topic-popular content, and for a route-clients or route-pipeline person it's always off.
   - It holds two ideas. Split it or drop it.
   - It repeats a shipped piece without new material. A seed that already bore fruit is a candidate again only when its record holds something the last piece didn't use: a new feed, an answered objection, a new story.
   - Its material's permission is `private` (bank entries only).
   - It fails the scene rule in `templates/piece/brief.md`. It goes to the waiting list with the question "what happened that made you think this?".
   A branch part or a plan item whose material isn't in the canon yet (the part is named, the method isn't) is not killed; it's **waiting on the person**. List it in the shortlist's waiting section with the question, so `/status` surfaces it. The same item never gets killed week after week for the same reason.
4. **Rank the rest**, in this order, and stop at the first that separates two candidates:
   1. Fits this quarter's branch and desire pairs in the content plan. Inside this rule, a part of the branch itself outranks a POV that only links to the branch.
   2. Closes the reputation gap (moves the reader toward the target association).
   3. Lands where the body of work is thin (pick by gap: deepen before adding).
   4. The seed has grown: `growing` or `bearing` outranks `sprouting`, because it has met pushback the person answered or been fed something that holds. A seed with an objection still `open` can be harvested, as a test piece that doesn't claim past it; say so on its line.
   5. The material is confirmed and fresh (captured this month beats captured last quarter).
   6. Matches the layer the mix is short on this quarter.
   Nothing else ranks. Not what would get reach, not what's easy to write.
4a. **Look up from the pile.** Gathering and ranking puts entries side by side. When two ideas or entries turn out to be one belief, or the plan or the shortlist leans on a belief no entry states, write it to `proposals.md` as a `seen` proposal, as `skills/job-think` defines it (kind 1 or 4), `proposed_by: strategist`, with every quote it rests on and one question (`CLAUDE.md` rule 8). Read the open proposals and the cap in `templates/proposals.md` first: one that says the same thing gets a dated evidence line instead, and past the cap, write an `earned` line to `bank/evidence.md`. Don't go looking for these (that's `/think`); file what the shortlist showed you, and keep ranking.
5. **Write the list** to `pieces/shortlist.md` (overwrite each run): three to five candidates, each with its seed (I ID) and stage, the reader (G ID), the material (IDs), the branch, the layer, and the one reason it ranks where it does (a second line for the reason is fine); then the items waiting on the person, each with its question; then the killed ones with their reason in a few words; then the runway line, which the index points at rather than repeats. Candidates have no folder yet, so they live here, not in the index. Say what the person does next: pick by number ("/post 2" or "/essay 2" builds it from that seed), or say what's missing.

## Output

- `pieces/shortlist.md`: the candidates, what's waiting on the person, what was cut, and the runway.
- `pieces/index.md` kept current.

## Never

- Never brief, draft, outline the post or write a hook. The person picks; `/post` or `/essay` builds it with them.
- Never list a `seed` whose meaning the person hasn't confirmed, or a `resting` or `cut` one.
- Never pick a candidate for reach on route-clients or route-pipeline, or because it's easy.
- Never write facts about the person into this skill.

## Handoff

The list: next is the person's pick, by number, into `/post` or `/essay`. Waiting items: next is the person, with the questions in the list and in `/status`.

## Say so in the list when

- Two candidates tie through all six ranking rules.
- The content plan's branch for the quarter has no seed ready for it.
- A ready seed contradicts a confirmed canon entry (write it to `proposals.md` too; create the file from `templates/proposals.md` if it doesn't exist).

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md` at the repo root: the date, the skill, what was unclear.
