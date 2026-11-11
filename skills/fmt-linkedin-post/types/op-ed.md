# Type: op-ed

A post that asserts a position and defends it. What defines it is a **counterparty**: someone credible who would disagree. Without one the person has an observation, and observations belong in `shorties`. Method by Josué Valles, built from 135 vetted posts. One finding shapes everything below: the labels this corpus used to carry (Contrarian Take, Manifesto, Rant, Trend Read, Teardown, Original Research) sorted on tone, not construction. Posts with the same structure sat under different labels because one writer was angry and another was calm. This file sorts on how the post is built.

## What it's for

Being known for a position. An op-ed removes a belief, replaces one, teaches a mechanism, earns one, proves one, hardens one people already half-hold, or recruits readers into a problem, and which of those it does depends on the path. The one outcome anyone can measure is a sentence the reader could say out loud in a meeting that isn't theirs. It's also the type to use when the person has a take and doesn't know what shape it wants: routing says which path the material can carry, and the counterparty gate says when it can't carry an argument at all.

## Where it sits in the library

- **Hook moves:** mostly 6 (the common advice is wrong). Also 9 (the line someone said) when the opposing position is a quotation, 7 (the call-out) when the post opens angry, 2 (here's the actual document) or 11 (the finding) for an exhibit, 4 (put the reader in the room) for an incident, 1 (proof, then payoff) or 11 for a receipt, 13 (the reframe) when the post names a thing that had no name, and 17 (a bet on the future) only with the warning under "What substitutes for evidence".
- **Structures:** S4 (the argument) for most paths; S2 (the explained list) when a built case numbers its reasons; S5 (the breakdown) for an exhibit; S3 (the story arc) for an incident; S7 (the body is the hook) for a short axiom.
- **Inside moves:** M7 (the other side, taken seriously), M2 (the turn), M3 (the evidence pair), M6 (the analogy, when it carries the reasoning), M4 (the data line), M8 (the subject's own words) for an exhibit's verbatim line, M9 (the meaning line).
- **Closes:** C1 (the restated principle) when the restatement drops the hedge and becomes portable (see "Restating the thesis"; that is the reason the brief gives for choosing it); C3 (the small instruction); C2 (the question back) for an open question. Never a close that ends on evidence.
- **Inventory slots:** OPINION always. Then, by path: LINE or a public statement for a refusal, DOCUMENT, DATA or NEWS for an exhibit, STORY for an incident, RESULT, DATA or EXPERIMENT for a receipt, PATTERN for a built case's reasons.

What this file adds to card 6 and S4: the counterparty gate, seven paths routed on what the argument runs on, the constraints every op-ed holds, the devices ranked by what they move, what substitutes for evidence, the rules for concession, anger, length and restatement, and each path's failure tell.

## When it fits, and when it doesn't

It fits when the person holds a position someone credible would dispute, and has something to run the argument on. It doesn't fit when:

- **Nobody credible disagrees.** That's an observation: `shorties`. In the other direction, a shortie with no turn and evidence behind it is a statement, and a statement with evidence is an op-ed.
- **The post falls below about 45 to 55 words.** At that length it stops asserting and becomes a joke or a poll, which is `shorties` territory.
- **The list is the content.** A numbered post where each item pays its own way is `power-listicle`. A list-spined argument whose prose outweighs its list belongs here, as an op-ed with numbered paragraphs. A contrast rack of eight rows against three is an op-ed with a straw man in it, and as an op-ed it still has to pass the counterparty gate with the other side stated fairly. Two books and eight opinions is an op-ed with a reading list stapled on, judged as an op-ed.
- **The argument runs on this week's news.** When the material expires, `newsjacking` sets the clock and the split. An exhibit here is an object anyone can go and look at whose point doesn't depend on being recent: a study, an ad, a document.
- **The argument runs on someone else's story, told as a story.** That's `borrowed-story`, whose refuted-premise path and verification gate cover it. The incident path here is for one thing the person saw or lived.
- **The story is the post and the position is a line at the end.** That's `owned-story` with an exhortation stapled on, one of the shapes the counterparty gate caught in the corpus.
- **The number is there to show what the person sells.** That's `proof-post`. A receipt here spends the person's number to prove a belief that cuts against consensus.

## Facts and sources

The position is the person's, never the writer's. On the pipeline it traces to a confirmed POV, the thesis or a branch (`canon/person/`); on a direct piece, to a quoted line in `material/`, `inbox/` or `said today`. A POV whose confidence is `forming` or `exploring` feeds an op-ed only when the brief has `thinks_out_loud: yes` (`CLAUDE.md` rule 2), and then the post never states it as settled. That rules out the axiom path, which states a conviction without qualification, and makes the open question path its natural home.

The rest follows `CLAUDE.md` rule 1, row by row in the source map:

- **The opposing position.** A quotation someone said to the person is a LINE from their material or said today. A public statement is `borrowed: verify` with its source. A position attributed to a class ("founders who say...") is the person's PATTERN, cited. Never invent a quotation to give a refusal something to refuse.
- **An exhibit** (the study, the ad, the document) is `borrowed: verify`, with every figure and verbatim line sourced.
- **An incident or a receipt** is the person's STORY or RESULT, cited by ID or file. A receipt's number comes from `canon/bank/proof.md` or material, exactly as recorded.
- **Operator verbs** ("I've watched", "I tell my team") claim a vantage point, and a vantage point is a fact about the person. The source method says the verb works even when the observation can't be checked; in the studio it is used only when the sources give the person that vantage. Never write "I've watched this happen twice" without the two times.
- **Reductio, a named mechanism, an analogy that carries the reasoning** are `writer` lines, true whoever said them; the editor checks them for truth.

An op-ed argues, so `skills/craft-copylosophy` runs on it in full: the writer pass before drafting, the judge pass on the draft. The counterparty gate below and copylosophy's steelman ask for the same thing from two sides: a credible opponent, stated in the form its smartest defender would use. The premise copylosophy finds failing is usually what the post argues against.

## Step 1. The counterparty gate

Before routing: **who would disagree, and are they credible?** Name them as a role, a class of person or a school of thought. If the answer is "most people" with nobody specific behind it, or nobody at all, there's no op-ed. Twelve posts in the corpus failed this, and every one turned out to be something else: a shortie, an announcement, an owned story with an exhortation stapled on. Twelve of the corpus's fourteen no-counterparty posts sat under the old "Manifesto" label, which is where op-eds went to lose their opposition. Say so and route the material elsewhere rather than writing it.

## Step 2. Route on what the argument runs on

| The argument runs on | Path | Material test |
|---|---|---|
| Something someone else actually said | **Refusal** | Is there a quotation in a voice that isn't the person's, attributable to a recognisable role? |
| Several independent reasons plus a replacement | **Built case** | Can you fill in both "the reasons are ___, ___, ___" and "instead of X, do Y"? |
| An external object anyone could go and look at | **Exhibit** | Can you name the thing and cite one figure or verbatim line from it? |
| One thing that happened, with a turn | **Incident** | Does the material have a sequence of events and a moment where something flipped? |
| The person's own numbers, cutting against consensus | **Receipt** | Is there a figure only they could know, and does it contradict what people assume? |
| A conviction they'll state without qualification | **Axiom** | Can it be written with no "because" in it, and are there two more sentences that raise the abstraction rather than repeat it? |
| A tension they haven't resolved | **Open question** | Can the opposing position be written in one sentence they'd sign their name to? |

(The tests above are the source method's; where a slot would need to be filled, it is filled from the person's sources, as "Facts and sources" says, never written to pass the test.)

Two or three paths often open. Choose on what the post should do:

- **Refusal** removes a belief. It can't establish one.
- **Built case** replaces a belief. The slowest and the easiest to imitate.
- **Exhibit** teaches a mechanism. It borrows its authority from the object.
- **Incident** earns a belief. One data point, so the claim has to stay small.
- **Receipt** proves a belief with standing nobody else has. Unrepeatable: each number spends once.
- **Axiom** hardens a belief people already half-hold. It rests entirely on the person's standing.
- **Open question** recruits people into a problem. It converts nobody, and it can't be cited later as a position.

**If the material is only the person's opinion with nothing under it, axiom is the only path open,** and it's where five of the corpus's seven no-counterparty failures live. Route there only if the counterparty gate passed on real evidence.

## Step 3. What every op-ed holds

The draft stage writes against the chosen path's shape (read its exemplars first) and holds these seven. They hold across all 135 posts, and each does a job.

1. **The position goes in line one.** About 95 of 135 open with a complete proposition someone could lift out. LinkedIn cuts the post at "see more", and a thesis below that line is one most readers never see. The exception is the incident path, where the claim lands at 60 to 85% of the way through: the reader agrees with the facts before meeting the claim, which is worth a lot, and the post fails if the story can't hold them past the cut alone.
2. **The opposing position is visible:** quoted, attributed to a class, or personified in a character. If a reader can't point to the sentence where the other side appears, they can't tell what the post argues against, and neither can the writer.
3. **No named individual is the party in the wrong.** In all 135 posts, every named person is an ally, an authority recruited for the claim, or excused before the argument goes on ("Jensen Huang has 50 direct reports *because* he built a culture of extreme autonomy over decades"). The party in the wrong is always anonymous and plural. Naming makes it a grievance, and nobody shares a grievance.
4. **Every concession is closed before the end.** The other side never holds the last position.
5. **At least one concrete particular:** a figure, a proper noun, a verbatim quote, a physical object.
6. **The post never ends on evidence.** The last line of substance restates, prescribes, warns or asks. Nothing comes after it.
7. **The subject becomes something the reader is doing or believing now.** Even the exhibits turn this way: "Look at your latest subject line. If I can guess the end of the sentence before I finish reading it, you have lost me."

## Step 4. Devices that move belief, strongest first

**Reductio, the strongest thing in the corpus.** Nine posts, median 857 reactions against a baseline of 416. Hand the reader the opponent's premise and let them ride it into absurdity (post 353 in the exemplars). It works because it never asserts: there's no position of the writer's in it to attack, so the conclusion the reader reaches is their own.

**Naming a thing that had no name, strongest for agreement.** The lowest comment ratio of any device with above-baseline reach, which is what assent looks like next to argument. Once the reader uses the word, they hold the frame, and the argument ended without them noticing. It's the only device that survives the reader forgetting the post. If the draft describes a pattern for more than two paragraphs and it has no name, give it one. A name the person already uses is theirs and stays as they say it (`CLAUDE.md` rule 3); a new one goes to them as a suggestion.

**Cost accounting, as the unpriced ledger.** What the reader already pays without complaint, next to what they refuse to pay. "You'll spend £200k on a failed senior hire without blinking. You'll spend £2m on a go-to-market strategy that doesn't work. But £30k on developing the founder, suddenly it's 'soft stuff.'" It doesn't ask the reader to accept a new value; it shows their existing values applied unevenly, which is much harder to refuse. The figures come from the person's sources or a sourced case.

**The analogy that carries the reasoning.** Delete it: does the argument still stand? If yes, it's ornament, and ornament is a second thing to disagree with (house rule H1). If the analogy is the proof, keep it. "AI is 'levelling the playing field' in the same way that a virus that turns everyone into a zombie levels the playing field."

**The definition swap that installs a test.** A new definition moves belief only when it comes with a way to apply it tomorrow. "If you can't tell which one you're doing, the giveaway is who left the room feeling lighter."

**The one to avoid: the reframe in its "the problem isn't X, the problem is Y" form.** It's the commonest move in the corpus and the weakest: median 233 reactions against 416, and the highest comment ratio of any common device. The logic still works; what stopped working is its credibility. One corpus post reports a Maryland/DeepMind study naming "it's not X, it's Y" as a sentence-level tell of machine writing; another reports AlphaSense logging 73 corporate documents using "not just X, it's Y" in one quarter, after a handful across the previous two decades. In the studio the question is settled anyway: house rule H17 bans the construction. When the post's job is a new lens, use naming, reductio or cost accounting.

## Step 5. What substitutes for evidence

Most of these posts have no data. What a reader accepts instead, ranked by how much weight it carries:

1. **The worked example.** It's one case, and it's the only device that supplies a mechanism the reader can check against their own experience. They don't verify the anecdote; they verify that it matches something they've seen. The best ones change one variable and hold the rest: "I've watched a clever industry take get 40 likes, while a simple 'lesson learned' story got over 600. Same client." Those last two words do a control group's work. The example is the person's, from their sources.
2. **The named mechanism.** A causal story explaining why, which the reader can't disprove and can't dismiss either, because it fits what they already know. The strongest form demonstrates itself: the reader tests it on the sentence in front of them.
3. **Standing,** which is a licence, not proof. It buys permission to skip the argument, and it works best as a two-step: standing, then at once something it cost. Standing alone reads as a résumé; standing plus a cost reads as testimony.
4. **Numbers.** In half the corpus, load-bearing in a fraction. The ones that carry weight change a decision: "$69.99 a month → nearly $840 per year → So. Bye, Premium." The conversion is the argument.

Weakest: borrowed authority and dated predictions. Neither supplies a mechanism, and a dated claim is the one thing a reader can refuse for free. This is why hook move 17 sits at the edge of this type.

The corpus's own summary: before sending, ask whether this could have come from anyone else. If it could, it isn't good enough. That's the swap test (check 15a in the judge stage) said from the argument's side.

## Step 6. Draft

### Assert with operator verbs

Replace "I think", "I believe" and "I feel" with "I've watched", "I told him", "I tell my team", "I've seen". "I think X" invites "well, I think not-X", and the exchange is even. "I've watched X happen twice this year" is uneven: the reader can't counter it from an armchair, because what's claimed is a vantage point. In the studio the vantage point must be real and sourced (see "Facts and sources").

### Concession

32% of posts concede, and the payoff shows in reposts more than reach: 0.037 reposts per reaction against 0.026 for posts that concede nothing. A repost is a reader putting their name to the claim, and to repost something unqualified they'd have to defend the unqualified version. **A concession is what makes a claim safe to carry.**

Placement splits in two: 0 to 20% of the way through, or 60 to 90%, with the middle nearly empty. Early, it buys the right to assert. Late, it stops the reader building the objection the post already answered. In the middle it only dilutes. Write the post, find the paragraph where a hostile reader would first say "yes, but", and put the concession there.

### Anger

Fine, and sometimes the point, inside narrow rules. The house rules still apply, and strong language goes in only when it's the person's own (the exception principle in `skills/craft-house-rules`).

- **It goes in the first sentence.** The median first anger marker sits 6% of the way into the post; in posts with two or more, 1%. Anger is an opening declaration, never a build. It stands in for a credential the writer lacks, and it clears out the readers who disagree early.
- **Aim it at a reconstructed sentence, an act or an imbalance; never at a population or a platform.** A reader faced with anger at a category has to check whether they're in it, and the check is defensive. Anger at a described act invites them to witness it with the writer. One corpus post runs four parallel lines of restraint ("I don't tell legal how to do their job. I don't tell sales how to do their job...") and then one line of exasperation: the anger arrives as the conclusion of an argument about fairness, so agreeing costs the reader nothing.
- **Fire once.** Posts with three or more anger markers see the comment ratio nearly double and the repost ratio halve. Sustained anger turns sharing into argument: nobody puts their name to it, and everybody replies to it.

### Length

Median 190 words. Within one author's voice, longer does worse: across one 19-post series, the correlation between length and log reactions was minus 0.39, with a median of 857 reactions under 180 words against 190 over it.

The cleanest evidence is a natural experiment (posts 383 and 408 in the exemplars). Same author, same argument, the same closing paragraphs word for word. One states each point once, at 141 words, and got 982 reactions. The other states each point, translates it, restates all five under a TAKEAWAY header and closes with two more restatements, at 432 words, and got 166. **A sixfold penalty for explaining the joke.**

So delete the sentence that explains the sentence before it (house rule H32). The unstated conclusion is the only one a disagreeing reader can accept, because nobody told it to them; they reached it.

Go long only for something the length buys: a full concede-and-refute cycle, accumulation until the pattern can't be denied, a reversal that needs a first position held long enough to have been believed, or a proof that collapses if any line is dropped.

### Restating the thesis

A third of posts restate it, and the second statement is never a copy. The direction is consistent: **the first statement is hedged and specific, the second is unhedged and portable.** The body earns the right to drop the hedge. The changes that recur: an accusation becomes a maxim (so the reader can carry it without carrying the indictment), personal becomes universal, a claim becomes a consequence with a deadline. This is the reason that makes C1 the right close here; a restatement that only repeats the hook is still the weak default `../stages/moves.md` warns about.

Whatever the post closes on, it should be a sentence the reader could say out loud in a meeting that isn't theirs, and it goes last, because on a feed that's where the screenshot crops.

## Step 7. The path's failure tell

The writer runs these before handing the draft to the judge; the judge runs them again (check OP2).

- **Refusal.** Is the opposing position quoted, or did the draft paraphrase a mood? If nobody said the thing being refuted, the post ends up retracting in its last quarter to fence in a fight it never defined. Post 300 spends its final 25% doing exactly that ("To be clear: I'm not saying going viral is 'bad'..."), and the unquoted opening is what causes it.
- **Built case.** Do the reasons collapse into each other? Write the headings out and check that none restates another. And is there a named replacement, or does the post only remove? Removal without a replacement is refusal material at three times the length.
- **Exhibit.** Could a sceptical reader go and look at the thing? If not, it's an assertion dressed as an exhibit. Second tell: the post ends up debating the source's method instead of the person's claim.
- **Incident.** Does the post say out loud that one story is one data point? Every strong instance does ("this happens all the time", when the person's sources say it does). And is the verdict small enough for the story to carry? One dinner supports "attention is the constraint"; it can't support "content strategy is broken."
- **Receipt.** Can a reader without the person's record act on any of it? If not, add the generalisation. And check the number hasn't been spent before: search the person's shipped finals in `pieces/` and the body-of-work index for it.
- **Axiom.** Does each restatement raise the abstraction, or is it the same sentence louder? And has the counterparty survived into the text, or is it the person agreeing with themselves?
- **Open question.** Is the opposing side stated in a form the person would defend? If it arrives already dismissed, it's a refusal with a question mark on it.
- **All paths.** Count the anger markers; more than one costs the post. Find the sentence that explains the sentence before it, and delete it.

## Checks the judge adds

On top of the stage's checks, each a FAIL with the line quoted:

- **OP1. The counterparty.** The draft names, quotes or personifies a credible party who disagrees. "Most people" with nobody behind it, or nobody, is a FAIL, and the verdict says which type the material belongs to instead.
- **OP2. The path's tell.** The chosen path passes its tell in step 7.
- **OP3. Line one.** The position is a complete proposition in the first line, or the path is incident and the story holds the reader past "see more" on its own.
- **OP4. The other side is visible** in a sentence the judge can point to, and holds no position at the end: every concession is closed.
- **OP5. Nobody named is in the wrong.** Every named person is an ally, an authority or excused before the argument goes on.
- **OP6. The end.** The last line of substance restates, prescribes, warns or asks; it isn't evidence, and nothing comes after it.
- **OP7. A concrete particular** (a figure, a proper noun, a verbatim quote, an object) is in the post and sourced.
- **OP8. Anger.** No more than one marker, in the opening, aimed at an act, a sentence or an imbalance, never at a population or a platform.
- **OP9. The explained sentence.** No sentence explains the one before it, and a post over about 190 words says what the extra length buys (one of the four reasons under "Length").
- **OP10. Vantage and position are sourced.** Every operator verb has the events behind it in the person's sources; the position traces to a POV, thesis, branch or quoted line, and a forming or exploring POV appears only with `thinks_out_loud: yes` and isn't stated as settled.
- **OP11. A receipt's number** hasn't been spent in an earlier shipped piece.

## Things that look like rules and aren't

These vary by author only. Writing them in as rules produces posts that read like a template.

- First person: absent from 21 of the 135. (The studio's first-person check, check 17, still applies; the person can be present through what they did, saw or tell their team.)
- Second-person address: absent from 19.
- Numbered lists: fewer than a third.
- Quotation marks around the opposing view: only about a fifth quote; the rest paraphrase the practice. The refusal path is the exception, because its tell is a quotation.
- A closing imperative: a third, not a majority.
- Emoji, dividers, P.S. tails, link dumps. Eight posts add housekeeping after the real close, and in every case the argument ends cleanly one line before it starts.

## Examples

`op-ed/exemplars.md` holds eleven complete posts grouped by path, three anti-patterns, and the short version of one of them. Read the two or three for the path before drafting. They differ as much as possible on the surface while sharing a construction, so they can't be copied; what they share is the path. Read the anti-patterns whatever the path: post 408 against its short version, 383, is the clearest thing in the file about what length costs; 254 shows a post that concedes nothing and turns its audience into an opposition; 300 shows the retraction an unquoted refusal causes.
