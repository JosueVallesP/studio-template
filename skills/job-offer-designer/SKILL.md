---
name: job-offer-designer
description: Designs or redesigns one offer end to end, so the value is plain to the buyer and the price follows from it. Starts from what the buyer already wants (the audience research and the person's calls), maps every problem before, during and after, turns each into a solution, picks how each is delivered (trim and stack), adds only real scarcity, urgency, bonuses and a guarantee, names it, checks the price, and writes the offer document. A new offer goes to the vehicle file as a draft entry for the person's yes (a change to a confirmed offer goes to proposals.md instead); offer page copy runs through craft-sales-copy. Use for /offer-designer, "help me build an offer", "how do I package this", "what should I include", "I need bonuses", "what guarantee should I use", "name my program", "value stack", "redesign my offer".
---

# /offer-designer

Method by Josué Valles, the studio's author, built on Alex Hormozi's *$100M Offers* (2021): the value equation, the Grand Slam offer, trim and stack, the four enhancers and MAGIC naming are his.

The idea: never compete on price. Make the offer so plainly worth more than it costs that the price stops being the question. You get there by solving every problem the buyer meets on the way to the outcome they already want, delivering each solution in the cheapest way that still feels like real help, and then removing the risk of saying yes.

**The value equation** is the lens for every decision:

> Value = (Dream outcome × Perceived likelihood of achievement) / (Time delay × Effort and sacrifice)

Make the top bigger: an outcome the buyer wants more, and more reason to believe they'll get it. Make the bottom smaller: results sooner, with less effort. Every part of the offer moves at least one of the four, or it goes.

## What it reads

- `canon/vehicle/vehicle.md`: the goal, the business, existing offers (`O` entries), the constraints (hours a week, what limits the work). An existing offer is the starting point for a redesign.
- `canon/strategy/audience.md`: the segment's desires (`D` entries), `will`, `tried`, the reasoning, the struggling moment, the language bank. This is where the dream outcome and the problems come from.
- `canon/bank/proof.md` and `canon/bank/stories.md`: what the person has delivered and for whom. The likelihood side of the equation rests on these.
- `canon/strategy/brand-strategy.md`: who it's not for, the stop list and the anti-associations.
- `material/`, `inbox/` (run `python3 scripts/inbox-to-text.py` first): sales calls, client emails, past offers.
- When the canon is empty, `config/intake.yaml` and what the person says today.

**How it relates.** The vehicle interview (`skills/setup-brand-tree`, `references/questions.md`) asks for the goal and the offers; when its `O` entry is confirmed, start from it. `/understand` builds the audience file; when it's empty, the problems below come only from the person's calls and their own account, and the offer is marked as untested with buyers. `/pricing-tests` runs the price in full; step 7 here is a check, and when `/pricing-tests` has run, start from its number. `/diagnosis-call` is how the offer gets tested in conversation.

## How to run it

One question per turn. Ask about things that happened (`skills/craft-interview`): "Tell me about the last client who almost didn't buy. What stopped them?" works; "What are your customers' objections?" doesn't. Say at the start what you're doing, why, what they'll have at the end and roughly how long (about an hour for a new offer, less for a redesign), as `CLAUDE.md` rule 7 asks.

Get three things first, then gather the rest as you go:

1. What they sell, or want to sell, and how it's delivered now.
2. Who buys it, as specifically as they can say it; a `G` segment if there is one.
3. The outcome the buyer is after.

For a redesign, ask them to describe the current offer first, and frame every step as a change to it.

### Step 1: The dream outcome

The dream outcome is what the product makes possible, not the product. A gym membership isn't it; the body that gets compliments is. An accounting service isn't it; never worrying about taxes and keeping more money is.

Take it from the buyer's words: a desire in `audience.md`, a line from a sales call, what a client said when they signed. Sharpen it into one sentence written from the buyer's side: specific enough to measure where the outcome is measurable, felt where it isn't, something they'd pay almost anything for if it were certain. Say it back with its source and ask: "Is this what your buyers are after, or closer to it?" (`CLAUDE.md` rule 3). If the only source is the person's guess, say so; it stays a guess until a buyer says it.

### Step 2: Every problem in the way

List every problem, obstacle, fear and doubt between the buyer and the outcome, in three phases:

- **Before** they start: what stops them beginning, what they tried that failed (`tried`), what they don't know they need to know, what they're afraid of.
- **During:** what makes them want to quit halfway, the confusion and frustration they hit, outside obstacles, skills or resources they lack.
- **After** they get the outcome, or don't: new problems that success creates, keeping it going, how others see them now.

Then run each phase through eight dimensions: **speed** (too slow?), **ease** (too hard?), **quality** (will the result be good enough?), **variety** (do they need options?), **personalization** (does it feel generic?), **support** (help when stuck?), **access** (can they reach what they need?), **exclusivity** (does it feel like theirs?).

Each problem carries its source: a quote from the research, a call, a client email, or `said today` from the person. Show the list by phase and ask what they've seen happen that's missing: "Think of the last client who stalled halfway. What was going on?"

### Step 3: Problems into solutions

One solution per problem, stated as the outcome the buyer gets, not as "fixes X", and only ones the person's business can really deliver within the constraints in the vehicle file. Show them as problem and solution pairs, grouped.

### Step 4: Delivery (trim and stack)

For each solution, two or three ways to deliver it, from this matrix:

| | Done for you | Done with you | Do it yourself |
| --- | --- | --- | --- |
| **One to one** | Highest value, highest cost | High value, high cost | Medium value, low cost |
| **Small group** | High value, medium cost | Medium to high value, medium cost | Medium value, low cost |
| **One to many** | Medium value, medium cost | Medium value, low cost | Lowest value, lowest cost |

And the medium: text (guides, templates, checklists, workbooks), audio (calls, recorded trainings), video (walkthroughs, live sessions), live (coaching calls, workshops, small groups), software (dashboards, calculators, automations).

**Trim.** Score each way on two things: what it costs the person to deliver (time first, for a one-person business) and how much the buyer would value it.

- High cost, low value: cut it.
- Low cost, high value: keep it. These carry the margin.
- High cost, high value: keep it only if it's the thing that sets the offer apart.
- Low cost, low value: cut it; it adds complexity and nothing else.
- A starting rule of thumb: total delivery cost under about 30% of the price. Check the hours against the vehicle's constraints too; an offer the person can't deliver at their hours is worse than no offer.

**Stack.** Put the winners together into one offer the buyer can look at and think "this covers it". Show it as a table: solution, the way it's delivered, the format, why this way.

### Step 5: The enhancers

Four things that raise the value of saying yes now. Each passes the truth tests in `skills/craft-sales-copy` before it goes in.

**Scarcity**, only when it's real: seats capped because the person runs every call, the person's own hours, a cohort that starts on a date. Say why the limit exists; the reason is what makes it believable. Never a limit the person won't hold to.

**Urgency**, only when something really changes on a date: the cohort starts, the price goes up and stays up, the season ends (tax season, the start of a school year). Say the reason.

**Bonuses** that remove the objections buyers have after they've seen the core offer:

1. Name the objection, from a call or the research.
2. Design the bonus so that objection stops mattering.
3. Name it plainly (step 6).
4. Describe what it is and how it's delivered.
5. Say why it's included, so it reads as care and not as a gimmick.

Three to five bonuses is a starting default; more than seven overwhelms. Each answers a different objection. Bonuses that cost little to deliver and help a lot are the best kind; digital ones cost almost nothing per buyer. The common pairs are in `references/offer-library.md`. A standalone value for a bonus is a pricing check (step 7); it appears in public copy only as a real price (`skills/craft-sales-copy`, truth test 4).

**A guarantee.** Every offer has some way of taking the risk off the buyer. The types, from most to least aggressive, and when each fits, are in `references/offer-library.md`. Name it plainly so people remember it, keep any conditions reasonable and stated, and pick it with the person against their own risk and cash. Refund rates are usually lower than people fear; the person's own refund history, if they have one, is the number to use, not a general one.

Show the full enhancer plan with the reason for each.

### Step 6: The name

MAGIC, from Hormozi. Not every name needs all five; the good ones hit three or four.

- **M: a magnetic reason why now.** Only a true one: a new method, a season, the first cohort.
- **A: announce who it's for.** The segment, in the words they'd use for themselves.
- **G: give them a goal.** The outcome from step 1.
- **I: indicate a time frame.** Only one the person can keep for most buyers.
- **C: complete it with a container word.** What kind of thing it is (the library is in `references/offer-library.md`).

Offer three to five names. Test each: could the person say it out loud to a client without wincing, and does it say what the thing is? A plain name they'll use beats a clever one they won't. A name with a coined term follows the naming gate in `skills/job-shape` (the pattern already shows up in their material at least three times); a new term the person adopts goes on the "Terms they coined" line of `canon/voice/voice-guide.md` marked `draft`, with its plain definition, the date and this offer as its source (the route in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes").

### Step 7: Check the price

Price follows the value to the buyer, never the cost to deliver.

1. **The value stack, as a check.** For each part, ask "what would someone reasonably pay for this on its own?", using real prices where they exist: what the person charges for it alone, what the buyer's real alternative costs (the tests in `/pricing-tests`). Add them up. This number stays in the working document.
2. **The 10x reading.** Read the stack against the asking price and write the ratio in the working notes. Hormozi's starting points: total ÷ 10 is a safe price; ÷ 5 needs strong proof behind it; ÷ 3 only with a long record of results. They're his starting points, not laws; say so. A low ratio is a reading to talk through, never a gate. When the value looks thin, don't pile on parts: run the remove test in `/pricing-tests` (step 4, "the $30K test": what could come out so the part that matters carries the price).
3. **The virtuous cycle.** A higher price means the buyer invests more, shows up more, gets better results and tells people. A low price runs it backwards: low effort, poor results, refunds. Ask: "At this price, will your buyer take it seriously enough to do the work?"
4. **Push back on a price set by fear,** plainly and kindly, with the reason. Then run `/pricing-tests` if they haven't.

Never state a price to the person as theirs. Suggest a range with the reasoning; the person names the number.

### Step 8: The offer document

Write it to `pieces/<yyyy-mm-dd>-offer-<slug>/offer.md`:

```
# <Offer name>

## Who it's for
<The segment, in their words, with the source>

## The outcome
<The dream outcome, with its source>

## What's included
### The core
<What it is, how it's delivered, which problems it solves>
### Bonus 1: <name>
<What it is, the objection it answers, why it's included>
(more bonuses)

## The guarantee
<Its name and full terms>

## Scarcity and urgency
<What's limited or dated, and the real reason; or "none">

## Price
<The person's number, or the range with its reasoning, marked waiting for their yes>

## Working notes (not for the page)
| Part | What the buyer gets | Standalone check | Source of the check |
| ... |
Total: <sum> · 10x reading: <ratio> · Delivery cost: <hours and money, against the vehicle's constraints>

## Still open
<Problems with no source yet, guesses waiting on a buyer, anything to confirm>
```

Then, for the person's yes (`CLAUDE.md` rule 6), along the route in `skills/setup-brand-tree/SKILL.md` ("Where a picked-up belief goes"):

- **A new offer, or a redesign of a `draft` one:** the `O` entry in `canon/vehicle/vehicle.md` with `status: draft` and a log line naming the offer document, filled from it (name, for, outcome, how it works, price only if they named one, and `availability:` open, waitlist or closed if they said which). No proposal.
- **A redesign of a `confirmed` offer:** the entry stays as it is. The change goes to `proposals.md` only (`templates/proposals.md`, kind `change to O<n>`), quoting the document and asking one question.

## Quality checks

Before showing the document, check it against these and name any that fail:

1. **Value to price,** as a reading. Write the 10x ratio from step 7 and say plainly what it suggests. When the value looks thin, the next move is the remove test in `/pricing-tests`, not more parts.
2. **Everything ties to the outcome.** Remove any part that doesn't.
3. **The real objections are covered.** The top five from calls and the research are each answered by the core, a bonus or the guarantee.
4. **Scarcity and urgency are true.** Would the person defend each one in public? If not, it goes.
5. **The "stupid to say no" test,** Hormozi's: if you were this buyer, would passing on it feel like losing something real? If not, the offer needs more work.
6. **Deliverable.** Can the person deliver all of it, at their hours? An offer that can't be kept is worse than none.

## Common mistakes

- **Listing features** instead of tying each part to the outcome and a problem it solves.
- **Weak bonuses:** extra stuff that answers no objection.
- **No guarantee.** Some way of taking the risk off is always possible; the question is which.
- **Pricing by cost,** adding a margin to what it costs to deliver.
- **Unnamed parts.** "Module 1" and "Bonus PDF" tell the buyer nothing.
- **Fake scarcity.** It ends trust for good.
- **Solving problems the buyer doesn't have.** Every problem has a source.
- **Too many parts.** Fifteen or more and it feels like work; combine them.
- **Ignoring the after.** Most offers stop at before and during.
- **Competing on price.** Lowering the price to win starts the cycle running backwards.

How the method bends for services, digital products, physical products, high-ticket and low-ticket offers is in `references/offer-library.md`.

## Offer page copy

When the person wants the page or a section of it (the outcome, what's included, the guarantee), run `skills/craft-sales-copy`: three drafts, the judge in a fresh context, the copy kind `offer section`. The copy uses only what the person has confirmed in the document; working-notes numbers never reach the page.

## What it says to the person

After each step, the result in a few lines and the one question for the next step. At the end: the offer in two sentences, the price question if it's still theirs to answer, what's still open, and the next step (`/pricing-tests` for the price, `/diagnosis-call` to test it on a real buyer, or the page copy).

## Never

- Never state a price, result, client or testimonial the person didn't give.
- Never put a value figure in public copy that isn't a real standalone price.
- Never add scarcity, urgency or a deadline the person won't hold to.
- Never confirm an offer in the canon. It stays `draft` until the person says yes.
- Never invent a buyer's problem, objection or words. Each has a source or is marked as the person's guess.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
