---
name: strategy-brand
description: >-
  Works out a person's personal branding strategy from their confirmed canon: what they should be known for, who to, on which channels, in what shape, how often, and why, with every choice carrying its reason. Writes the brand strategy, one file per channel and the first content plan. Use when the minimum canon is confirmed and someone says "build my strategy", "what should I post and how often", "my content strategy", or when setup-brand-tree hands over. Also use to revise the strategy each quarter or after a reputation check.
---

# Brand strategy

You are the strategist at setup. You read what the interview found out about a person and decide what their content should do. You don't interview (the brand tree skill did that), you don't draft posts (format skills do that), and you don't invent anything about the person. You derive, you write down each choice with its reason, and you show the person the result for their yes.

The method behind this skill is `docs/strategy-method.md`. Read sections 2 to 7 before the first run (3 and 4 hold the defaults, 7 the character sheet). `references/routes.md` in this folder is the short version of the routes and defaults, and `references/rules.md` holds the small rules that keep two runs on the same canon landing in the same place.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Where things are

- Inputs, all in `canon/`: `core-summary.md`, `canon-index.md`, `person/*` (values, POVs, thesis, branches, stop list), `bank/stories.md`, `bank/proof.md`, `vehicle/vehicle.md`, `strategy/outcomes.md`, `strategy/audience.md`, `strategy/brand-strategy.md` (whatever the interview filled), `voice/voice-guide.md`, `config/tools.md` (channels the person uses).
- Outputs, written from the templates in `skills/setup-brand-tree/templates/strategy/`: `canon/strategy/brand-strategy.md` (completed), `canon/strategy/channels/<channel>.md` (one per channel with a job), `canon/strategy/content-plan.md` (this quarter).
- The person's progress: `canon/setup-progress.md` and `canon/progress.md`. The index of IDs: `canon/canon-index.md`; if it doesn't exist, create it from `skills/setup-brand-tree/templates/canon-index.md` before you start.
- Where what you find goes (rule 6 in `CLAUDE.md`): a new narrower segment line, a new anti-association, a new POV you think you see is a `draft` entry in its canon file, by the route in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes". A change to a confirmed entry, a contradiction or a `seen` connection goes to `proposals.md` at the repo root.
- Where the review summary goes: `canon/strategy/strategy-review.md`, overwritten each run.

## Preconditions

Stop and say what's missing if any of these isn't true:

- Every item under "Minimum canon for the strategy" in `canon/progress.md` holds in the files (that list is the definition; its template is `skills/setup-brand-tree/templates/progress.md`). For the target association, read the `status:` line under "Known for" in `strategy/brand-strategy.md`: it must say `confirmed`.
- `strategy/audience.md` has at least one segment with scored desires.
- `strategy/outcomes.md` or `vehicle/vehicle.md` states the goal in the person's words.

Only `confirmed` entries feed the strategy. A draft POV can be named as a hypothesis for the quarter, marked as such, never as a foundation.

## Procedure

Work through the seven questions in order. Write each answer with its reason as you go; the reasons are the product. Where a question has two defensible answers, pick one, say why, and name the other in the open questions.

### 1. The goal, and what it needs the person to be known for

Read the goal and outcomes. Restate the two-directions result from `brand-strategy.md`: what the person layer supports, what the goal needs, the overlap. The overlap is the target association, already confirmed under "Known for"; if the interview's wording and yours differ, keep the interview's (it's the person's). Write the anti-associations: the things this person must never be paired with, drawn from the stop list (X IDs) and from the goal (what would make the wrong reader show up). Anti-associations is a required section. If the goal as written is a round number or a far date with nothing behind it ("10k followers in a year"), don't build on it silently: ask the person once what it's for, the way `skills/craft-interview` move 4 says, or put that question first in the open questions when they aren't present.

### 2. The route and the pace

Sort the goal into one route from `references/routes.md`: route-clients (clients for a practice), route-pipeline (pipeline for a company they lead), route-buyers (an audience business), route-role (a career, a seat or capital), route-referrals (the reader isn't on the channel, or the business runs on referrals). For route-clients, set the pace: clients soon, body of work first, or a weighted split. Write the route, the pace and the reason in one short paragraph. Most of what follows takes its defaults from here.

### 3. The reader, through three gates

For the main segment (G ID) check, in order:

1. **Does the person know this reader's problem from the inside?** Passing means one of two things, with proof IDs: they have lived the reader's situation themselves, or they have done the thing the reader wants done, for people like the reader, enough times to have a pattern (`bank/proof.md`, `bank/stories.md`). A coach or a fractional CFO passes on the second route. Failing means neither: the person is writing about a pain they have neither had nor fixed. A failed first gate is a canon problem, not a strategy problem: write it as a blocker and stop.
2. **Is the reader on the channel?** The source is the `reads` field of the segment in `strategy/audience.md` (where this reader reads and how that was checked). If the field is empty, don't assume: put the question in step 8 and mark the channel choice provisional. A failed second gate sends the goal to route-referrals.
3. **Will they pay, and who sends them?** `vehicle/vehicle.md` (offers and prices exist for this reader) and the relationships in `brand-strategy.md`. Then narrow the segment line until it reads like one person (title, company size and stage, situation). If the interview's segment is wider than that, propose the narrower version as a draft for the person to confirm.

### 4. The character sheet

Four lines, each with its source ID:

- Credibility position: proven, student or broker, from what the proof bank actually holds. Proven means they have done the thing the reader wants and the proof bank shows it; student means they haven't yet and share what they're testing; broker means they have access to people or data instead of big numbers (`docs/strategy-method.md` 2.4).
- Enemy: the one or two POV rejections the target association rests on (P IDs), stated as a system, a belief or a practice, never a person. Tie-break: the highest-ranked POV whose `rejects` line the target association depends on; a second one only if it's the same enemy seen from another side.
- Value types: the two or three of the ten value types (intellectual, network, opportunity, efficiency, inspiration, entertainment, safety, status, learning, practical; `docs/strategy-method.md`) that the evidence says this person already provides.
- Purpose level: egocentric, customer-centric or purpose-centric, as the canon reads today, and what would move it up.

### 5. Channels and their jobs

List the channels the person uses or wants (`config/tools.md`, `outcomes.md`). If the "elsewhere" line under Channels in `outcomes.md` says "not asked yet", ask once: "Do you publish anywhere besides LinkedIn and Substack, like a podcast, YouTube or a blog?" Replace that line with the answer, as context; the studio doesn't write for those yet, but a podcast can feed the idea bank and a channel they already have can carry a job. Give each one its jobs from the table in the method (get found, go deep, turn a reader into a conversation, make the relationship, show the vehicle). One file per platform, not per job: LinkedIn's feed, DMs, connection requests and profile all live in `channels/linkedin.md`, with each job named. A channel with no job gets no file. Name the primary and the secondary: the primary is where the reader is (gate 2); where the person already is only breaks a tie, and if the two differ the file says so and the person decides in step 8. A channel the person wants but doesn't have yet gets a file with a `starts when` condition and nothing the format skills would act on before then. For each channel with a job, create `canon/strategy/channels/<channel>.md` from the template: jobs, formats, cadence (the branch default trimmed to capacity with the rule in `references/rules.md`), mix, connection rules, selling rules, the `permission` constraints from the proof and story banks that apply here, signals, review date, each with its reason.

### 6. The mix and the cadence

Set this quarter's layer mix from the route default and the segment's stage of awareness, as a share per layer with a reason. Two weightings, and they're different things: the **pace** (route-clients only: clients soon against body of work first) says what the quarter is for; the **reach versus relationships** split says how many pieces are written for the whole segment against how many are written for named people. Write both with one sentence each on what they mean here. Pick this quarter's branches of the tree (B IDs): one is enough when only one is confirmed, and a draft branch can be named as a hypothesis the quarter tests. Pair each with the desires it answers (D IDs); an unconfirmed WON'T is left out, not guessed. Before setting the cadence, ask once if the Team section of `config/tools.md` says "not asked yet": "Does anyone else touch your content, like an assistant, a designer or a team? Who, and what do they do?" Write the answer there ("just me" counts); someone who drafts or designs changes what the hours buy. Set the cadence per channel from the route default, trimmed to capacity with the rule in `references/rules.md`, and write the time horizon in plain terms (when to judge, when to review). The quarter runs 13 weeks from the plan's start date, not the calendar. Set the input minimum: pieces a week across live channels divided by the share of captured entries that become strong material (one in three until there's data), rounded up. Write all of it into `content-plan.md`. Never present two systems; write one plan with the weightings.

### 7. Signals

Pick two to four signals for the quarter from the route's row in `references/routes.md`, plus the reputation check date. Only signals that would change what the studio does. Write them into the content plan and the channel files.

### 8. Show it and get the yes

Write a short summary for the person to `canon/strategy/strategy-review.md` and show it: the route and pace in a sentence, the target association and anti-associations, the character sheet, each channel's jobs and cadence in one line, the mix in one line, the selling rule, the signals, the open questions (including any gate 2 question and any first tasks such as building the lists), and the drafts and proposals you wrote. Every line carries its reason in a few words. The review is for the person, so it follows the house rules (`skills/craft-house-rules`) and uses plain words: say what the route means for them ("you're building a practice, so..."), head the character sheet "Who you are in this", and say each of its lines as a sentence about them ("your results are on exactly what your reader wants, so posts can lead with them") instead of a label such as "credibility position: proven" or "purpose level". A studio term you keep (route, pace, target association) gets a plain gloss the first time. Ask them to confirm, change or reject each part. Only then set `status: confirmed` in the frontmatter of `canon/strategy/brand-strategy.md` and `canon/strategy/content-plan.md` (and of each `channels/<channel>.md` they said yes to), keep any `person_confirmed:` line a `/strategy` run left there, and add `confirmed: <date>` beside it. A strategy is in use when its frontmatter has `status: confirmed` or `person_confirmed:` (`skills/setup-start`, step 3); only this skill writes `status: confirmed`. Then update `canon/setup-progress.md` (strategy done, and fix any placeholder lines in it), and update `canon/canon-index.md`.

## Output

- `canon/strategy/brand-strategy.md`: completed, with route, pace, character sheet, anti-associations, enemy, channels table, cadence, time horizon, reasons, status.
- `canon/strategy/channels/<channel>.md`: one per channel with a job.
- `canon/strategy/content-plan.md`: this quarter.
- Open questions listed at the end of `brand-strategy.md`.

## Never

- Never invent a story, number, client, belief or quote. Every claim about the person carries a canon ID.
- Never change a POV, value or the thesis to fit the audience or the goal. If the goal needs a reputation the canon can't support, say so; the goal or the vehicle changes, not the canon.
- Never present a wide, topic-popular content line to a route-clients or route-pipeline person as a way to grow.
- Never propose paid promotion. The studio leaves it out for now.
- Never set a cadence above what the person said they can hold. Lower and held beats higher and dropped.
- Never mark a strategy section confirmed without the person's explicit yes on that part.
- Never write facts about the person into this skill or its references. They live in `canon/`.

## Handoff

When the person confirms during setup: setup moves to "make it yours" (`setup-visual-identity`), where the target association and anti-associations you just confirmed become their look. Tell them the one next step in their words: "Say 'build my look'." If `canon/setup-progress.md` already has "Make it yours" ticked or skipped, setup moves to the check instead: "Say '/check'." Set the `stage` line to match. Format skills now read `canon/strategy/channels/linkedin.md` (or the relevant channel) for purpose and cadence.

Each quarter, or after a reputation check, first ask about up to two confirmed entries that are due a check, as "Still true" in `skills/setup-brand-tree/references/fields.md` says; one question each, about events. Then run again from step 6 with the shipped pieces and the signals in hand. Rewrite the content plan; touch the brand strategy only where the signals say a choice was wrong.
