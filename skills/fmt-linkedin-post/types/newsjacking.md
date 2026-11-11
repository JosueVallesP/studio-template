# Type: newsjacking

Someone else's news, carrying the person's read. Method by Josué Valles, built from 15 vetted posts, median 225 words, range 47 to 350. The news share of those posts runs from about 1% to 74% of the words, the widest spread of any type in the library, and getting that share right is most of the job. This is also the only type whose material expires, and almost everything below follows from that.

## What it's for

A post that reacts to something the person didn't cause: a launch, a study, an announcement, an acquisition, a layoff, a viral thread, a public statement. Everyone already has the news, and it's free. The post exists for the person's read of it, the thing the reader can't get from the headline. Good for reach, fast, and for a reputation as someone who has a view on what happens in their field. It's also the type to reach for when the person has an item and no angle: the routing table in step 2 says which construction the item can carry, and says so when it can't carry any.

## Where it sits in the library

- **Hook moves:** mostly 10 (news, plus a take), which is card 10's whole job. Also 17 (a bet on the future) for the Reaction Forecast and the prior-position move, 11 (the finding) when the news is a study's number, 7 (the call-out) as a secondary move when the read attacks a practice, and 9 (the line someone said) when the newsmaker's own words open the post.
- **Structures:** S4 (the argument) for nearly every construction; the library sorts 10 to S4 and the corpus agrees. S7 (the body is the hook) for the Single-Datapoint and the shortest Retrievals. S3 (the story arc) for a Sequence Chronicle or a character sequence told in beats. S5 (the breakdown) when the item is something the person can take apart, such as a launch they operated.
- **Inside moves:** M1 (the context block) carries the reporting, M2 (the turn) is the crossing sentence, M4 (the data line) and M3 (the evidence pair) carry Counter-Evidence and the Character Verdict's alternative-proving fact, M8 (the subject's own words) anchors every attack, M7 (the other side, taken seriously) is the Counter-Evidence concession, M9 (the meaning line) is the generalisation.
- **Inventory slots:** NEWS, plus the OPINION it carries. Some constructions need a second slot: DATA for Counter-Evidence, BORROWED or DOCUMENT for the Retrieval, LAUNCH or EXPERIMENT for First-Person Operation, LINE or private material for Insider Dissent. Without an opinion of the person's, the post is a repost and fails the swap test.

What this file adds to card 10: the swap test as the first gate, nine constructions with their material tests, the clock and what each clock word costs, the gap rule for how much to report, the crossing sentence and the bridge noun, the three sources of standing, and the exposure rules for naming people and splitting claims.

## When it fits, and when it doesn't

It fits when something happened recently, it has a source, and the person has a read on it that depends on this item and not on any item like it. It doesn't fit when:

- The person has the news and no read. Ask what it made them think, or what it changes for the people they work with. If there's still nothing, it's a `/scout` find for later, not a post.
- The read survives the swap test (step 1). Then the person has an opinion and a headline stapled to it. The opinion may be a good `op-ed`; write it there, with the news as one piece of evidence at most, or without it.
- **The boundary with `op-ed`:** an op-ed asserts a position and defends it against a counterparty, and the item, if there is one, is evidence. A newsjacking post is about the item: the read only exists because this thing happened. Test: delete the news. If the post still stands with a different example, it's an op-ed.
- **The boundary with `borrowed-story`:** a borrowed story is someone else's story that has finished, told so it proves the person's claim, and it doesn't expire. Newsjacking material is still moving and dated. When the event is months old and the post retells it as a story, it has crossed over; use `borrowed-story` and its verification gate. When the post pairs an old event with a newer one (step 3), it stays here.
- **The boundary with `arbitraged-content`:** arbitraged content borrows attention from a famous person, book or moment in history to deliver the person's idea, and the source can be any age. Newsjacking borrows the attention of the week. If the item is a classic the person is reading for the first time, it isn't news to the reader.
- **The boundary with `shorties`:** a single striking number with one line of reaction can be either. The Single-Datapoint gate in step 2 decides: if the number needs no setup and breaks an assumption the reader holds, it's a 47-word newsjacking post; if it needs a sentence of setup, it's not this construction.
- The person caused the news (their launch, their funding round, their hire). That's 18 (the announcement) or `owned-story`. First-Person Operation is the exception: the person didn't cause the news, but they used the thing and have output to show.

## Facts and sources

Two kinds of fact live in this type, and `CLAUDE.md` rule 1 treats them differently.

- **Facts about the news** (a name, a date, a figure, a quote, who did what) are `borrowed: verify` in the source map, and the row names and dates the source: the outlet, the link, the publication date, and the date the writer read it. A study's figures cite the study, not the article about it, when the writer can find the study. A figure from an outside case is `borrowed: verify` even when it's the hook.
- **Facts about the person** (their prior position, their tenure, a client, what they've seen, a friendship with the newsmaker, private material for Insider Dissent) come only from the four sources: the session, `material/`, `inbox/`, and the canon and idea bank. Standing (step 5) is where this bites hardest. "I've spent twenty years watching this" is a fact about the person and is never written from inference. The prior-position move needs the prior in the person's own words, with a date, from their material or from them today.

When the person pasted the item, ask where it came from and when. When the writer finds it, `/scout` files it as an outside entry with its source. Recent news is the one place the model will often meet events it has never seen. **Unfamiliarity is not evidence of falsehood.** A single-pass check flagged a post in the borrowed-story corpus as fabricated, and it turned out to be entirely true. Check the source, not the flag. And don't paper over a gap: if the writer can't verify a figure, say which one, and hedge it in the post (step 6).

The source method had its own voice notes and its own review. In the studio, the house rules replace the voice notes, and the judge runs in a fresh context (`CLAUDE.md` rule 4); the checks at the end of this file are what that judge adds.

## Step 1. The read, and the swap test

The person isn't reporting. The post is their read of the news, and the swap test comes first because it kills most drafts.

**The swap test.** Replace the subject with a comparable one: McKinsey with Accenture, Meta with Amazon. If nothing in the commentary needs to change, the person has a stock opinion with a headline stapled to it.

The corpus's clearest failure of this test sits inside a post that drew 1,163 reactions. It runs a 114-word block quote from a study on AI workload intensification, then spends its last 73 words on the psychology of people who disagree about AI. Those 73 words could sit under any negative AI study without a word changed.

**The related tell: evidence and claim with different subjects.** If the evidence is about one thing and the conclusion about another, it's two posts stapled together, and the news does no work in either.

This is a separate test from the general swap test in the judge (check 15a, could another name go on the post). That one swaps the writer; this one swaps the news.

## Step 2. Route on what the item contains

| The item contains | Construction | Material test |
|---|---|---|
| A discretionary decision by a named actor | **Character Verdict** | Is there a second publicly verifiable fact showing a different decision was available? If the actor had no real choice, there's no verdict to render. |
| A claim or practice you can quote word for word | **Counter-Evidence** | Does the person already hold a specific outside result, with numbers, that bears on it? If the rebuttal is "I disagree", this path stays shut. |
| A new position on a line the audience has lived through | **Trajectory Placement** | Can you name three positions, two of them already past and verifiable? Two states is a before and after and won't hold the weight. |
| A named victim of a mechanism that also reaches the reader | **Class Escalation** | Is it the identical mechanism (same company, same policy, same button), and not merely a similar risk? |
| An earlier documented artefact by or about the subject | **The Retrieval** | Does the news contradict it (irony) or carry it out (thesis)? If the artefact needs a sentence of explanation to land, this path stays shut. |
| Three or more actors acting in a public chain | **Sequence Chronicle** | Was each step triggered by the one before? Shuffle the steps: if nothing breaks, it's a list of reactions, not a chain. |
| Something the person can operate themselves | **First-Person Operation** | Can they produce quotable output that didn't exist before they touched it? An announcement, a funding round or a hire fails. A shipped tool passes. |
| A newsmaker the person actually knows | **Insider Dissent** | Does the person have non-public material about this exact event they can quote? Without it, this collapses into commentary on someone else's news. |

Two special cases with hard gates:

- **Single-Datapoint.** About 47 words, one number, an immediate pivot. Can the writer state the whole event as one number in under fifteen words with no explanation, and does that number break an assumption the audience holds? If the number needs a second sentence of setup, this case stays shut and the post needs one of the eight above.
- **Reaction Forecast.** Predicting the discourse before the event lands. Both gates are hard: the event has a date and hasn't happened yet, and the discourse has recurring factions whose lines the writer can write in advance. Step 3 says what it costs.

If nothing passes, say so and say what's missing (usually the alternative-proving fact, the numbers, or the third position). The idea goes back to the bank with that ask.

### The harder calls

- **Character Verdict lives or dies on the alternative-proving fact.** The corpus example renders its verdict in three words, "It's a choice", and pays for it with two imported facts about the same actor, one of them "Meta just posted record profits this quarter." The post states its own precondition out loud: "This isn't some distressed company making hard choices." An adjective about the actor's character with no matching fact asserts bad faith instead of showing a choice. Both Character Verdict posts in the corpus end by speaking to a specific human, which no other construction does: one to the people laid off, one to the subject.
- **Trajectory Placement doesn't judge the actor.** The hire is a thermometer. That's the whole difference from Character Verdict, and mixing them produces a post that can't decide whether it's diagnosing or prosecuting.
- **Counter-Evidence concedes before it strikes, and the concession does structural work.** It's what makes the numbers land as a ruling instead of cherry-picking. The corpus's best instance steelmans the thing it attacks with a metric few readers can evaluate: "0.44 mean absolute error on a 5-point scale, beating every baseline they tested." That number's job is to prove the writer isn't dismissing the technology out of ignorance, and to set up a far more damaging admission from a friendly witness. **Search a Counter-Evidence draft for a numeral and for a concession phrase. Zero of both means the post is disagreeing loudly, not ruling on anything.**
- **Insider Dissent is the only construction that has to repair what it strains.** The corpus example runs about 81 words of specific credit before the critique and 87 words of de-escalation after it. Step 6 has the full list.

## Step 3. Set the clock

**The hook sets the shelf life; the event doesn't.** A post whose first line carries the news dies with the news. A post whose first line carries the interpretation outlives it.

| The hook carries | Corpus example | Shelf life |
|---|---|---|
| Raw news and a date | "BREAKING: Meta laid off 8,000 people today via 4am emails." | about 24 hours |
| Raw news and a date | "Kylie Jenner lost 15 million Instagram followers yesterday." | about 72 hours |
| An image made from the news | "Fortune 500 CEOs are now paying McKinsey to explain why a 24-year-old with a ring light is eating their lunch." | weeks |
| A contrast | "While everyone's building AI companies, Mark Cuban just invested 7-figures in... an events company." | weeks |
| A bare fact, no date, no name | "1,000,000 views on a 6hr 22min YouTube video is absolutely insane to me." | no limit |

The instructive case is the McKinsey post. The actual news is one sentence, and the writer moves it down to paragraph two. The hook turns the hire into a scene. The hire being three weeks old costs nothing, because the reader never met it as breaking news.

### What each clock word costs

- **"BREAKING:"** buys the most urgency and licence to be rough. It costs credibility with anyone who saw the news six hours earlier, and stamps the post with a date in the person's archive for good.
- **"today"** buys presence, the sense of standing inside the event. It costs everything after about 36 hours, and the person can't reshare their own post.
- **"yesterday"** gives near-recency while admitting the person wasn't first. Much cheaper than "today", because it survives a weekend.
- **"This week"** gives currency at a seventh of the decay rate of "today".
- **"just"** is the cheapest clock word and the most used. Recency with no date, elastic enough to cover a fortnight.
- **"going viral"** asserts currency and dates nothing.
- **"a few months after"** is a looking-back clock. It buys a story shape instead of urgency, and it's what a late writer uses.
- **No clock word** gives up the urgency and buys unlimited runway.

One corpus post welds itself to a single calendar day at five separate points: impossible to rewrite or reshare, dead by Wednesday. That's a fair trade, but make it a decision and not an accident. Record the choice in the format plan's TYPE NOTES line.

### When the person is late

Four moves, all from the corpus:

1. **Change the unit of time.** Stop reporting the event and report the pattern it belongs to. A consulting hire isn't breaking news, so the post makes it a point on a longer clock: "Every disruption follows the same arc: Denial / Consultants / Panic acquisitions / Irrelevance."
2. **Pair the old event with a newer one.** "This comes a few months after his prediction on the resurgence of live events." Two events make a story where one only made news.
3. **Drop the clock word.** A fact with no date is never late.
4. **Turn lateness into thought.** "I've been thinking about him all week." The delay becomes the reason the post exists, and only when it's true of the person (rule 1).

**The move the corpus never makes is apologising for being late.** None of the fifteen says "I know this is old news, but".

## Step 4. Split the post: report the gap, not the event

Put on the page exactly the facts a sceptical reader needs to reach the conclusion without trusting the writer. Then stop.

**The working test: delete any reported sentence. If the read still stands, that sentence was filler.**

What pushes the reporting share up:

- **The meaning lives in the exact wording.** A paraphrase of a study's findings or an investor's own thesis destroys the evidence. One corpus post gives 99 of its 175 words to two quotes.
- **Cast size.** Reporting grows with the number of actors the writer has to name for the event to make sense.
- **The person is accusing someone.** Show the source, define the mechanism, and steelman the accused.
- **The claim is about a person's character.** Character claims hold up only as sequences. The corpus's 350-word post runs five beats: contract, refusal, threats, cost, aftermath. Remove the threats and the refusal is cheap. Remove the cost and it isn't a sacrifice.

What pushes it down:

- **The person's contribution is a model, not evidence.** Nine words of news can fund 275 words of stage theory.
- **The audience already has the event.** One post reports nothing at all, because everyone reading knew the thing had shipped.

**The demonstration worth taking in:** one corpus post spends 216 words on a layoff most readers had already seen the headline for, and almost none of them on the headline. It spends them on details nobody else reported: the 4am timing, the countries, the work-from-home instruction, the internal programme name. It never explains who Meta is. A different post, written for an audience it doesn't assume knows the subject, does explain who its subject is. The variable that decides it is the gap between what the reader knows and what the conclusion needs.

**Low reporting isn't free.** The post that reports 9% pays with 81 words establishing who the subject is and why the writer's opinion counts. Where the post doesn't report, it supplies standing or specifics in equal measure.

### The crossing sentence

Every post in the corpus has one sentence you can point to where reporting stops and the read starts. This is the turn (M2), and the brief names it. **If you can't point at it, the writer has smeared the read across the report as adjectives** ("wild", "huge", "incredible"). That isn't a read; it's a repost with garnish.

### The generalisation

Every post moves from the specific event to a claim about the reader's world (M9). Six of eight in one half of the corpus land it in the final quarter. It holds in four cases:

- **A concrete noun carried across the bridge.** A term from the reported material reappears inside the generalisation: "cutting management layers" becomes "mid and late-career worker" becomes "that ladder led straight to the exit"; "$2.6B valuation" appears word for word in both the report and the claim; "seven-figure consulting fees" becomes "a 200-slide deck" becomes "won't wait for a recommendation deck."
- **The reader sits inside the identical mechanism.** The Kylie Jenner post widens her lost followers to everyone who built a business on a platform they don't own. Same company, same policy, so the post needs no analogy. (The corpus says it as a "not X, this is Y" pair; in the studio it goes in as one full sentence, since H17 bans the pair.)
- **The writer marks it as a forecast, not a finding,** and it deflates, so being wrong costs nothing.
- **It inverts material already quoted,** so the reader does the extending and the post never says what it means for them.

Where it strains: nothing carries across; the evidence's subject differs from the claim's; an unattributed absolute lands after an attributed argument; made-up illustrations do the work of evidence (also H24); the writer offers one precedent as a universal.

### The ending

**All fifteen posts end on the writer's material.** If the last sentence's subject is the newsmaker doing something, the post has no destination.

## Step 5. Standing

The person is commenting on an event they had no part in. Standing comes three ways, and **no post in the corpus does none of the three.**

- **Supplied:** stated, and sized to the claim. The strongest instance doubles as the model's evidence: "I've seen this pattern before. At Discovery, we brought in digital consultants around 2010. By 2015, every major firm had a 'digital transformation' practice." Two dates, one employer, one checkable industry fact. The most careful instance runs a disclaimer first and the tenure 274 words later: "I don't know him personally" ... "I've spent twenty years watching what happens when". The disclaimer is what licenses the tenure: having ruled out insider access, the writer can only be offering experience of the pattern, which is what he then offers. Supplied standing is always a fact about the person, from the four sources.
- **Borrowed:** quote someone with more authority. In one corpus post the writer's only move is the archivist's, and the standing belongs entirely to the quoted party; the post is honest about that. Another holds evidence the reader can't get and reports it in the third person, so it reads as independent backing instead of self-promotion.
- **Demonstrated:** show the knowledge instead of claiming it. One post has no credential sentence and earns its close by command of the field's talk: "a scam that has worse performance and burns more tokens", "the PDF they made 5 minutes ago." Nobody outside the field writes those lines. Another has no first person anywhere; its credential is naming an internal programme. **Naming something the reader couldn't have known stands in for a biography.**

**None of the fifteen writes "As a [job title]."** The two posts that assert the least have the most specifics per word. That's the trade.

A post with no "I" at all meets the studio's first-person check (judge check 17) only through demonstrated standing the reader can see as the writer's knowledge. If the read has nobody behind it, add one sentence of the person's.

**Placement flips function.** A duration credential placed before the evidence demands belief; placed after it, it confirms.

### The prior-position move

Using the news as evidence for something the person already held. It answers "why you": anyone can report the layoff; only the person had the position beforehand. It costs more than it looks. The reader has to grant the past with no receipt, and the person has staked identity, not opinion. If the news reverses, the standing reverses with it.

**The rule: it works when the prior is more specific than the vindication, and reads as gloating when the vindication is more specific than the prior.** The corpus's working version names a year, an employer and an estimate it got wrong. The failing version says "I told you 2026 will be the year of 'I told you so'", which names no prior claim at all, so the vindication has nothing to attach to. The prior position is the gloat.

Three questions separate them:

1. **Can the person state the prior as something someone could have disagreed with?**
2. **Is the vindication aimed at a structure or at people?** Aimed at a structure, the reader can join in. Aimed at a class of people, the reader has to check which side they're on.
3. **Does the news revise the prior, or only confirm it?** The strongest instance says: "But digital disruption unfolded over a decade. Creator disruption however is happening in quarters." The writer's own model was wrong about the speed. That one "But" turns prophecy into thinking.

In the studio, the prior has to exist in the person's material or their words today, with its date. A prior the writer reconstructs is an invented fact.

### When the post predicts

**Predict the reactions, not the event.** A reader can check a predicted benchmark result, and it can be wrong. A prediction that the bulls will be bullish can't miss. The corpus's prediction post feels like a bold call and carries almost no risk: its one specific line is satire, so nobody can check it. The writer spends specifics where checking can't reach. No post in the corpus makes a dated, specific, first-person forecast that events could prove wrong. The look of nerve comes three ways: predict the reaction, not the event; predict what is already the base rate while framing it as contrarian; or quote someone else putting their neck out. Card 17 asks for a bet specific enough to be wrong; when the person wants that, it's a 17 post with the news as context, and the person has to supply the bet.

## Step 6. Exposure

### Naming a real, reachable person

The armour goes up as the target gets closer.

1. **Name the person when they are the news,** or when the reader needs to check a public exchange.
2. **Don't name them when they're an instance of a type and the argument is about the type.** The corpus's sharpest attack never names its target: "There's an interview going viral with the CEO of a young startup that just raised $106M at a $2.6B valuation." Two numbers and a source link make him easy to identify, but withholding the name means he isn't tagged, notified or made the subject. The harm claim then targets what he said, not the man: the word "rhetoric" appears three times.
3. **Attack needs a disclosure of closeness; praise needs a disclosure of distance.** "He's a friend, and he built a better version of my own product" against "I don't know him personally." Each answers in advance the charge its stance invites. Both are facts about the person and come from the four sources.
4. **Move off the individual as soon as the post makes its point.**
5. **Hedge the one description you can't source.** One post does it in three characters: "fires some (fair?) shots at the CTO."
6. **Let the subject's own words do the damage.** Every attack in the corpus rests on a direct quote from its target (M8), and in the studio that quote has a `borrowed: verify` row.

**Criticising someone the person knows** needs all six of these: the conflict disclosed up front, including the unflattering part; specific praise before the criticism; the criticism as a question, not a verdict; a shift from the person to a category; a receipt showing the person said it privately first; and a warm sign-off. A wrong figure inside a question is a slip; inside an assertion it's a mistake.

### Claim-splitting

The corpus uses eight hedging techniques: attributing ("what people now call", "reportedly", "tells me"), direct quotation, a linked source, a question, vague quantities, words that mark how sure the writer is, conceding first, and scare quotes. **One structural move matters more than all of them.**

In eleven of the fifteen posts the perishable fact sits at the top and the durable claim below it, **and the second doesn't depend on the first being exactly right.** If the follower count is 12 million and not 15, "Your list is your business" still stands. If the company drops the pilot programme without a word, the progression claim still holds.

The two exceptions are the two most exposed posts in the corpus, for the same reason: in both, the payload is a moral verdict on a specific sequence of facts. "It's a choice" depends on the record profits being real and the layoff being discretionary. "And I find that genuinely admirable" depends on the refusal, the threats and the cost all being as described. Neither survives if the facts move.

**The rule: don't let the conclusion depend on any fact the person couldn't defend tomorrow.** If it must, hedge that fact specifically (one corpus post hedges only its softest claim, "reportedly jumped nearly 300%", and nothing else) and accept that this is a post the person may have to stand behind instead of walk back. Tell the person before it ships.

## Checks the judge adds

On top of the stage's checks, each a FAIL with the line quoted:

- **NJ1. The news swap.** Swap the subject for a comparable one. If the read needs no change, FAIL as "stock opinion with a headline". Also FAIL when the evidence and the claim have different subjects.
- **NJ2. The construction's gate.** The draft names its construction, and the material passes that construction's test in step 2: the alternative-proving fact for a Character Verdict, a numeral and a concession for Counter-Evidence, three positions with two verifiable for Trajectory Placement, the identical mechanism for Class Escalation, steps that break when shuffled for a Sequence Chronicle, quotable output for First-Person Operation, non-public material that puzzles instead of flattering for Insider Dissent, one number with no setup for a Single-Datapoint.
- **NJ3. The news facts.** Every name, date, figure and quote about the news has a `borrowed: verify` row with its source and date, or the draft hedges it and marks the row `source: not found`. A flat statement with neither is a FAIL, graded as "Outside example unverified" in the gates table in `skills/role-editor`.
- **NJ4. The clock.** The format plan's TYPE NOTES line records the clock word and the shelf life it buys. A post welded to one day without that decision is a FAIL. No apology for being late.
- **NJ5. Filler.** Delete each reported sentence in turn; any whose deletion leaves the read standing is a FAIL.
- **NJ6. The crossing sentence.** One sentence can be pointed to where reporting stops and the read starts. A read smeared across the report as adjectives is a FAIL.
- **NJ7. The bridge.** A concrete noun from the report carries into the generalisation, or the reader sits inside the identical mechanism. A generalisation about a group the reader isn't in ("some people", "these founders"), with nothing connecting it to the reader's Monday, is a FAIL.
- **NJ8. The ending.** The last sentence is the writer's material, not the newsmaker doing something.
- **NJ9. Standing.** Supplied, borrowed or demonstrated, at least one; never a job title. A duration credential before the evidence is a FAIL. Supplied standing traces to the four sources (check 18).
- **NJ10. The prior.** If the post uses a prior position: the prior is in the person's sources with its date, is more specific than the vindication, is something a reader could have disagreed with, and aims at a structure, not a class of people.
- **NJ11. Exposure.** A named person is the news, or the reader needs the name to check a public exchange. Every attack carries a quote from its target. Criticism of someone the person knows meets all six conditions in step 6.
- **NJ12. The split.** The conclusion doesn't depend on a fact the person couldn't defend tomorrow, or the draft hedges that fact on its own and the writer told the person.

## Things that look like rules and aren't

These vary across strong posts in the corpus. The house rules still apply to all of them.

- Emoji: one post uses seven, twelve use none.
- Links: only two posts link at all, and the post citing a named study with a specific error metric isn't one of them. (The source map still names the source, whether or not the post links it.)
- All-caps labels: "BREAKING:" and "CONTEXT:" do different jobs, and thirteen posts use neither.
- Line breaks: one post is a single 259-word block; another is 24 fragments.
- Lists: numbered, unnumbered, emoji bullets, or none.
- Sign-offs and closing questions: two of fifteen each.
- First person: one post uses "I" zero times; another more than fifteen.
- Hedging in general: the third-highest performer hedges constantly. What matters is only whether the post hedges its central claim, and that post doesn't.
- Length: 47 to 350 words, a spread of more than seven times.
- Register: one post consoles, one praises, one attacks, one shrugs.

**Not free, and set by the construction:** whether the post names real people. A Sequence Chronicle needs a cast, Insider Dissent needs a relationship, and the Retrieval posts name no one because their construction has no room for one.

## Examples

Twelve complete posts are in `newsjacking/exemplars.md`, grouped by construction. Each opens with its news and read split and its crossing sentence, the most useful single fact about any post in this type. Read the ones for the construction before drafting. Three are worth reading as a set: post 173 revises its own prior in public, post 123 vindicates a prior it never stated, and post 66 places its credential after the evidence. Together they cover the whole range of the prior-position move. Posts 52 and 374 pair on exposure: the only two whose conclusion depends on the facts being exactly right, and so the two the writer can't walk back.
