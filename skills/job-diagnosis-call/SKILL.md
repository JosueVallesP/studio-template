---
name: job-diagnosis-call
description: Prepares for, rehearses or debriefs one sales or discovery call run as an honest diagnosis - draw out the buyer's real outcome in their words, say back what you heard, tell them honestly whether and how you can help, separate belief from cash, and leave the decision with them. Prep and debrief are saved in the call's folder under pieces/; a follow-up message runs three drafts and a judge; the buyer's words go to /understand. Use for /diagnosis-call, "prep me for a sales call", "I have a discovery call", "let's rehearse the call", "debrief my call", "how did that call go", "write the follow-up".
---

# /diagnosis-call

Method by Josué Valles, the studio's author, from Blake's Kollege calls (2023).

A sales call goes badly in two ways. The seller pitches: credentials, a program, a list of what's included. Or the seller freezes and hopes the buyer says yes on their own. Blake's alternative treats the call as a diagnosis. You find out exactly what the person wants and why, say back what you heard in their words, tell them honestly whether and how you can help, and leave the decision with them. "There's no manipulation… your intention going into it has to be I'm going to help this person no matter what."

This skill helps in three ways: preparing for a call, rehearsing one with the studio playing the buyer, and debriefing one from notes or a transcript. The cases below are real moments from the calls; the people are described by what they do. Use them to show the move, and never in a piece (they aren't checkable sources).

## Why it works

- **Accurate diagnosis shows authority better than credentials do.** "Accurate diagnosis always proves that you are an authority." When he rewrote one member's sales video, he pushed the member to talk about the viewer's experience rather than his own credentials.
- **The buyer's words carry the sale.** In a mock sales call, Blake wrote down only the prospect's words and repeated them back, and the prospect said "I felt extremely heard."
- **The stated want is rarely the real one.** In a role play, a member who makes videos said he wanted a better video setup. Asking "why" got to watch time, to followers who follow him for who he is, and to a business big enough to change how his life would go. Blake's response: "You might not need this video setup."
- **Letting go of the sale protects both people.** Blake called this "daddy energy": go to accurate diagnosis and help them make an empowered decision. He warned that pushing can tip into manipulation; a deal he once took felt like "a lubricated forced decision."
- **Buyers need two beliefs.** A guest on an early call put it this way: belief in the method or vehicle, and belief that you're the right person to deliver it. Someone can like you and still doubt the method.

## The call

This is the shape of a call, not a script. Calls with warm referrals, past clients and strangers each sound different, and a call with an old client may skip half of it.

1. **Set your intention.** Before the call, decide you'll tell them the truth even if the truth is that they don't need you. If they only need something small, give it away; in the role play, Blake suggested the member could just be given a gear list for free.
2. **Ask and listen.** Open with what brought them here. Then "tell me more." Keep asking why each thing matters until you reach what it changes in their life or business. Ask about what happened ("What made you book this now?"), not what they think in general.
3. **Write down their words.** Sort what they say into problem, goal and context. Keep their phrases exactly, especially the ones they repeat.
4. **Diagnose.** Say what you think is really going on, in plain words. Point out what doesn't add up, kindly. If you can't help, say so.
5. **Show the path in their words.** Lay out the phases of working together using what they told you: "Do you remember how you told me you don't know what to teach your students? Well in this phase…" In the role play, Blake laid out one to one before one to many, then the channel, then the gear, then a content structure, and said: "This is us working together."
6. **Name the price plainly.** Once, without apology or a list of extras.
7. **Separate belief from cash.** This step is the studio's one description of the move; `/pricing-tests` points here. If they hesitate, ask: "Money completely aside… are you convinced it will work?" If the doubt is about the method or about you, go back to the diagnosis. If it's "literally just a money thing," ask what they have on hand and what they can set aside each month, and build a payment plan from those two numbers, with a small saving for paying early if the person wants to offer one.
8. **Let a no be a no.** If they're on the fence for reasons about themselves, don't argue. Blake gave fence-sitters "no worries" when filling his first beta group. If the problem will show up for them later, offer to follow up then. One member pressed a prospect who would only have the problem in a few months, out of his own need for the sale, and saw afterwards he should have offered a follow-up instead.

No scarcity tricks or hype (`skills/craft-sales-copy`, truth test 3). Blake: "all that hype stuff is going away."

## What it reads

- `canon/vehicle/vehicle.md`: the offer (`O` entry), the price, payment options. A draft offer or price is used in prep only after the person confirms it in the session.
- `canon/strategy/audience.md`: the segment's desires, the struggling moment and the language bank, so the prep questions start near where this buyer is likely to be. Never as a script of what the buyer will say.
- `canon/bank/proof.md`: real results, if the buyer asks.
- Earlier calls with the same buyer in `pieces/*-call-<who>/`, and anything the person drops in `inbox/` (run `python3 scripts/inbox-to-text.py` for a transcript).

**How it relates.** `/pricing-tests` sets the price this call names, and its test plan points to step 7 here for separating belief from cash. `/turning-prospects-into-collaborators` opens many of these conversations; its transition plan hands to this skill when a guest says yes to a call. `/offer-designer` changes the offer when calls keep showing the same gap.

## Where it saves

One folder per buyer: `pieces/<yyyy-mm-dd>-call-<who>/`, dated by the first call.

- `prep.md`: the prep sheet.
- `rehearsal.md`: the feedback from a rehearsal, when there was one.
- `debrief.md`: the debrief, with the buyer's words.
- A follow-up message, when there is one, as a piece in the same folder (`brief.md`, `draft-v1.md`, `review-v1.md`), through `skills/craft-sales-copy`.

The folder has no `brief.md` until a follow-up is drafted, so `/status` doesn't count prep and debriefs as content.

## How to run the skill

Ask which mode the person wants: prep, rehearse or debrief. Then one question at a time. People who find live selling hard hear this first: the job on the call is to listen and diagnose, which people who know their work well already do with clients every day.

### Prep

Gather: who the buyer is and how they arrived; what the person already knows about them; the offer and price; what a good outcome of the call would be (a sale, a clear no, a referral). Then write `prep.md`:

- three to five open questions to start with, in plain words, about what happened ("What made you reach out this week?");
- the "why" ladder to follow if the first answers stay on the surface;
- what would make this a poor fit, so they can say so honestly;
- the price and any payment options they're willing to offer, as they stated them;
- one line on their intention for the call.

Don't script answers for the buyer or guess their objections in detail. The point is to listen.

### Rehearse

Play the buyer, using only what the person told you in prep. Say at the start that this is practice and you'll give feedback at the end. Stay realistic: answer at the surface first, the way buyers do, and go deeper only when asked good questions. Raise a money concern at the price if it fits the buyer. Never add facts about the buyer the person didn't give.

Afterwards, write `rehearsal.md` with feedback on:

- how much they talked compared with how much they listened;
- whether they reached the buyer's real outcome or stopped at the first answer;
- whether they used the buyer's words when presenting the path;
- whether they separated belief from cash;
- any moment that sounded like pressure or a pitch;
- one thing to try differently next time.

Offer to run it again.

### Debrief

Ask for notes, a transcript or their memory of the call. Then write `debrief.md`:

- what the buyer said, sorted into problem, goal and context, in their exact words, each quoted with where it came from (the transcript line, the notes, or "the person's memory");
- the buyer's phrases worth reusing;
- the call checked against the eight steps: where it went well and where it slipped;
- what the call taught about the offer itself. Blake treated calls as research, and told one member the product improves fastest through one-to-one conversations.

Then three handoffs, each the person's choice:

- **The buyer's words** are first-party research, the closest source there is. Offer `/understand` with the debrief as its source, so they go into the audience file's language bank as drafts for the person's yes. This skill doesn't write to `audience.md` itself.
- **If there was no decision,** draft a short follow-up that reflects what the buyer said, in their words, and makes the next step easy, with no pressure. It runs through `skills/craft-sales-copy` (copy kind `follow-up`): three drafts, the judge in a fresh context. The follow-up's own gate: every line about the buyer quotes or says again something the debrief records, and it would still be worth reading if they never buy.
- **If the call showed a gap in the offer,** the buyer's words go on the offer as evidence along the route in `skills/setup-brand-tree/SKILL.md` ("Where a picked-up belief goes"): a log line on a `draft` `O` entry, or, on a `confirmed` one, a proposal in `proposals.md` (kind `change to O<n>`). Then offer to run `/offer-designer`.

## How to behave

- Keep it a conversation. One question per turn.
- Never invent what a buyer said. In a debrief, work only from what the person shares, and mark guesses as guesses.
- Be honest in feedback, and kind. If a call involved pressure, say so plainly.
- Treat the steps as principles, not a checklist.
- Everything this skill writes follows the house rules (`skills/craft-house-rules`).

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
