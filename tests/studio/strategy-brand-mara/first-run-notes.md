# Test notes: strategy-brand run on the Mara Lindqvist canon

For the skill's author. Blunt on purpose.

## Where the instructions were unclear, contradictory or missing

1. **Gate 1 ("has the person been this reader") does not fit the main case the skill serves.** A fractional CFO, a coach, a consultant: none of them has *been* the founder they sell to. Read literally, Mara fails gate 1 and the skill says "write it as a blocker and stop." Read for intent (the method's examples are about selling to heads of sales without having been a revenue leader), she passes on R1 to R3. I passed her and flagged it. The skill should say what counts: has the person done the thing the reader wants done, or lived the reader's situation, or neither. Right now the expert credibility position in step 4 and gate 1 in step 3 answer the same question in two different ways.

2. **Gate 2 ("is the reader on the channel") has no source in the canon.** The skill points at `config/tools.md` and "the audience research". `config/tools.md` only lists the person's channels, not the reader's. `audience.md` has no field for where the reader is. So the gate can only be assumed. Either add a field to the audience template (where this reader reads, how checked) or tell the strategist to ask the person during step 8.

3. **`canon/canon-index.md` is listed as an input and step 8 says to update it. It doesn't exist.** The brand tree interview never created it. The skill should either create it from the template or not list it.

4. **`canon/setup-progress.md` is placeholder text** (`owner: <person's name>`, `stage: brand tree, not started`) with ticked boxes under it. Not this skill's fault, but this skill is told to update it, and it's unclear whether to fix the placeholders too. I left it alone since the person hasn't said yes.

5. **"Reach versus relationships" and "A1 versus A2" are two axes and the skill treats them as one.** Branches.md puts the A1/A2 split in the plan as "70/30 toward one". The content plan template asks for "reach versus relationships". A2 content (frameworks for the whole segment) is reach inside the pond; targeted pieces and DMs are relationships. I wrote 70/30 for both and said what each means, but a reader could think they're the same number by coincidence. Define both in one sentence in the skill or drop one.

6. **Step 5 says DMs and the profile are channel jobs, but the channel template is per platform.** "Turn a reader into a conversation" (DMs, profile) and "get found" (feed) are both LinkedIn. I folded them into one LinkedIn file with two jobs. The skill should say that's the intent, or the method table should say which jobs share a file.

7. **The newsletter case is unhandled.** The person "wants" a newsletter that doesn't exist. The skill says list channels the person "uses or wants", so it gets a file, but the template has no field for "starts when" or "doesn't exist yet", and the format skills would read a channel file for a channel that isn't live. I added a Start line under Cadence. Add it to the template.

8. **Cadence arithmetic against capacity is left entirely to judgment.** "About 4 hours a week" is in the canon; the branch default is "2 or 3 pieces a week plus one targeted piece every week or two" plus "10 to 20 connection requests a day" plus a newsletter. There's no guidance on how long a piece or a request costs, so trimming to capacity is a guess (see below). Even a rough rule (a post plus its judging pass is about an hour; requests are ten minutes a day) would make two runs land on the same number.

9. **Step 8 writes a summary but says nowhere to put it.** The task gave me a path (`canon/strategy/SUMMARY-for-review.md`). The skill should name one, or say it's said in chat only. Also: the tool I run in refused to write a file named `SUMMARY-*.md` as a "report file"; a name like `strategy-review.md` would avoid that.

10. **"Only confirmed entries feed the strategy" and "a draft POV can be named as a hypothesis" is fine, but the content plan template's "This quarter's branches" asks for two.** With one confirmed branch the second slot is forced. I used it to say "no second branch, B2 is a draft". Say that a single branch is allowed.

11. **No instruction for the proof bank's `permission` field.** R1 and R3 are "public, aggregated only", stories are "anonymize". The channel and plan files should carry those constraints into the mix lines (I did, via X5), but the skill never says to read `permission`. The format skills will need it; the strategist should pass it on.

12. **Step 1 says anti-associations come from the stop list "and from the goal".** Good, but then there's no ID for a goal-derived one and the template line format wants an X ID. I wrote "No X ID; proposed for the stop list". Either say to route goal-derived ones through `proposals.md` or let the template take "none".

13. **The branch picker quietly assumes LinkedIn.** Branches.md and the method talk about "the channel" and mostly mean LinkedIn. Fine for this test, but the skill never says to pick the primary from where the reader is versus where the person already is when the two differ.

## Template fields with no sensible source in the canon

- `brand-strategy.md` › Relationships › "Around the buyer: authority figures, peers, community voices, cultural layer". The interview template doesn't ask for it. Empty.
- `brand-strategy.md` › Reputation checks table. Empty by nature in the first run; the template should say so instead of leaving a blank table that looks like an omission.
- `brand-strategy.md` › Character sheet › Purpose level › "what would move it up". The canon has no philosophy file (`person/philosophy.md` isn't in Mara's canon at all). I wrote the generic answer.
- `channel.md` › Connections › "Who to connect with: the lists". No Dream100, ICP or peers list exists anywhere in the canon. The template assumes they do. I wrote the roles and said the lists are a first task.
- `channel.md` › "Raise to: n when condition". Nothing in the canon about when she'd want more. Guessed a condition.
- `content-plan.md` › "The reputation gap: target association against the latest reputation check". No check exists. Wrote "the whole distance".
- `content-plan.md` › Desire and branch pairs › WON'T for D2: unconfirmed in the canon, so left as "none", correctly, but the template doesn't say what to do with an unconfirmed WON'T.
- `channel.md` for the newsletter: "What they're doing when they meet a piece", tool, list size, pitch line. None exist. Reader section is inferred, the rest is noted as missing.

## Things I had to guess

- Connection requests per day (5). Branch default 10 to 20; trimmed for a Friday-only writer. Pure judgment.
- Newsletter start (second month) and cadence (fortnightly). Judgment from four hours a week.
- Reach versus relationships 70/30 and the layer shares (40/30/15/10/5). Derived from A2 "deep, mostly branches" and the awareness stage, but the numbers themselves are mine.
- The wait times in "After they engage" (two weeks, 60 days). Taken from the method's sources, not from anything about Mara.
- That the quarter runs 2026-10-26 to 2027-01-31. The template wants a quarter label and today is mid-quarter; the skill doesn't say whether to use calendar quarters or 13 weeks from start.
- That the LinkedIn profile is the "show the vehicle" surface. No site in the canon.
- Which POV the enemy rests on (P1 over P4). Defensible from the target association, but the skill says "one or two" and gives no tie-break.

## What I did not do

- Did not set any `status: confirmed`. No yes from the person.
- Did not update `setup-progress.md` or create `canon-index.md`. Step 8 says to do both after the yes.
- Did not write to `proposals.md` (it doesn't exist in this copy). The narrower segment line and the goal-derived anti-association are in `brand-strategy.md` marked as proposals instead. The skill should say where a strategist's proposals go; CLAUDE.md rule 6 says `proposals.md`.

## How long the run felt

- Files read: 4 instruction files (CLAUDE.md, SKILL.md, references/branches.md, docs/strategy-method.md sections 1 to 9, since 2 to 6 don't stand alone without 3 and 4), 14 canon and config files, 4 templates, plus a grep into docs/spec.md for the awareness-to-mix rule the skill cites but doesn't restate. About 23 files.
- Written: brand-strategy.md about 1,500 words, linkedin.md about 1,000, newsletter.md about 700, content-plan.md about 1,000, the summary about 700. Around 4,900 words into canon/.
- The reading is the heavy part. The method doc alone is about 5,000 words and the skill says read sections 2 to 6, but section 3 (channel architecture) and 4 (branches) are where the actual defaults live, and 7 (character sheet) is needed for step 4. Say "read 2 to 7" or move the defaults the skill needs into references/.
- The derivation itself is quick once the canon is in hand; most of the time went to deciding what to do when the skill and the canon didn't line up (points 1, 2, 5, 7, 8 above). Each of those is a place where two runs on the same canon would produce different strategies.
