---
name: craft-sales-copy
description: The standard for any copy that sells or asks for something, in every job that writes it (an offer page section, a sales page, a pamphlet, a nurture email, an invitation, a call follow-up). Where the words come from, the truth tests a selling line has to pass on the day it goes out, the care-not-leverage gate, three drafts and a judge in a fresh context. Used by /offer-designer, /pricing-tests, /pamphlet-power, /turning-prospects-into-collaborators, /diagnosis-call, and for public lines by /finding-your-personal-monopoly, /building-your-message and /articulation-ladder; the judge runs stages/judge.md. Use whenever the studio drafts a line meant to get someone to buy, book, reply or say yes.
---

# Selling copy

Method by Josué Valles, the studio's author.

Selling copy is where a studio is most tempted to cheat, because the usual tools of the trade are an invented testimonial, a deadline nobody set and a number nobody can check. This standard is the reason the studio's sales copy can be trusted. It sits under the house rules (`skills/craft-house-rules`), which apply in full, and adds what's particular to copy that asks for something.

The idea behind it: a reader who buys because the copy described their situation better than they could has been helped. A reader who buys because the copy pressed on a fear or invented a reason to hurry has been used, and they usually find out. The first kind of sale makes the next one easier. The second makes every later page harder to believe.

## Where the words come from

In this order:

1. **The reader's own words.** `canon/strategy/audience.md`: the `language_bank`, the `quotes` behind each desire, the `struggling_moment`, `tried`. Openings, problem statements and objections come from here first, quoted or said again close to how the reader said them. When the file is empty or has no language bank, say so and offer `/understand` before the copy; if the person wants the copy now, use what they say their buyers say (`said today`) and mark the piece `kind: test`.
2. **The person's own words.** `material/`, `inbox/`, what they say today, and the canon (stories, proof, POVs, voice guide). Their reasons, their stories and their claims, kept as close to how they said them as the house rules allow.
3. **The vehicle.** `canon/vehicle/vehicle.md`: the offer's name, who it's for, the outcome, how it works, the price, the calls to action word for word (`C` entries). A `draft` offer feeds copy only after the person confirms it in the session (`CLAUDE.md` rule 2).
4. **Real outside cases** (`borrowed: verify`), for an object lesson or an analogy, with the source named.

Each line of the copy goes in the draft's source map as `CLAUDE.md` rule 1 defines it.

## The truth tests

Every selling line passes these on the day it would be published or sent. The judge checks each one.

1. **Every price, result, client, number, testimonial and guarantee comes from the person.** A price is in the vehicle or said today. A result is a proof entry (`canon/bank/proof.md`) or the person's words with the client's permission noted. A testimonial is quoted from a real message the person supplied, with who said it and whether they agreed to be named. When one is missing, ask, or leave the slot out of the copy. Never write a stand-in.
2. **True today, not true if things go well.** "I'm starting a series" is true on day one; "I've interviewed X and Y" is true only after X and Y. A line that becomes true only once the launch works is out.
3. **Scarcity and urgency only when they're real, with the reason said.** A cohort capped at twelve because the person runs the calls themselves is real; say why. A deadline is real when something actually changes on that date (the cohort starts, the price goes up and the person will hold to it). A countdown that resets, a "only a few spots left" nobody counted, a bonus that "expires" and comes back next week: none of these goes in.
4. **A value figure is a real price.** A "worth $X" next to a component appears in public copy only when the component sells for that price on its own, from the person or from a sourced market price. Every other value estimate stays in the working document as a pricing check (`/offer-designer`, step 7) and never reaches the reader.
5. **Care, not leverage** (`skills/job-understand`, the gates). Name the reader's pain in their words so they feel understood, then help. Don't press on it, don't make it worse than they said it is, and don't make a reader feel stupid for not buying. A fear the research doesn't show isn't used. A WON'T statement goes in only when `audience.md` marks it confirmed.
6. **Transparent selling.** When a piece leads to a paid next step, the piece says so plainly. The free or cheap thing is complete and useful on its own; the paid step continues it, never reveals that the first one was a trap.
7. **The person stays who they are.** Nothing the stop list or the anti-associations in `canon/strategy/brand-strategy.md` rule out, however well it would sell.

## The craft

What makes selling copy good, once it's honest:

- **Describe their situation better than they can.** The reader decides whether to keep reading on whether the first lines are about them. Lead with their words, not the offer.
- **One reader, one offer, one next step.** Every page and email has one call to action, from the vehicle's `C` entries word for word.
- **Say why for every claim.** "This works because..." with the mechanism, the way the house rules ask (H7). A claim with no reason is a claim the reader has heard before.
- **Answer the real objections in the reader's words.** From the research (`tried`, the reasoning column) and from calls, not from a list of objections people usually have.
- **Plain over hype.** No "transform", "unlock", "revolutionary", no capital letters for emphasis, no exclamation marks the person doesn't use. If the material is good, it lands without adjectives.
- **The swap test.** Put a competitor's name, or for an invitation another recipient's name, in place of the one on the copy. If the rest still works, it's a template, and the fix is more of what only this person, or only this recipient, did. The judge runs it as check 15.
- **Read it aloud as a voice note to one buyer.** Anywhere the person would stumble or wince is a line that isn't theirs yet.

## Three drafts and a judge

The same chain as `/post`, applied to selling copy.

1. **Open the piece folder** `pieces/<yyyy-mm-dd>-<slug>/` with `brief.md` from `templates/piece/brief.md`: `path: direct`, `status: briefed`, `format: craft-sales-copy`, `channel`, `kind: cornerstone` for a sales page or a pamphlet, `test` for everything else, and one line in the body saying the copy kind (offer section, sales page, sales page section, pamphlet section, nurture email, invitation, follow-up, positioning line, about section, ad line). For a sales piece, `channel` takes one of four values instead of a file in `canon/strategy/channels/`: `page` (a sales page, an offer page, a profile's About section or headline), `email`, `linkedin-dm` (a direct message, an invitation) or `pamphlet`. An ad line takes the channel file of the platform it runs on when there is one, or `page`. The Material section lists every price, result, testimonial and offer line with its source.
2. **Read before writing.** Five to eight of the person's own pieces (`craft-house-rules`, "How the sentences get written"), the rewrite pairs `python3 scripts/rewrites.py pick` lists, and the audience file's language bank for this segment.
3. **Write three distinct drafts** in `draft-v1.md`, as `## Post A`, `## Post B` and `## Post C`, so the check scripts read each one on its own, different in what leads and how it moves (the reader's struggling moment first; the person's story first; the mechanism first), not in wording. Fill the source map and the argument check (`skills/craft-copylosophy`, writer pass).
4. **Run the scripts:** `python3 scripts/check-prose.py <draft>` and `python3 scripts/voice-diff.py <draft>`. Fix every fail before the judge sees it.
5. **Hand it to the judge in a fresh context.** In Claude Code, the `judge` agent, told that the judge stage is `skills/craft-sales-copy/stages/judge.md`. In the app, a new chat: "judge the copy in pieces/<id> with skills/craft-sales-copy/stages/judge.md". The judge picks one draft or sends all three back, and writes `review-v1.md` from `templates/piece/review-direct.md`.
6. **One revision on revise**, from the review's THE ONE THING line, judged again from the start in a fresh context. After that, the person decides: use it, fix the open lines themselves, or one more pass.
7. **Show it** as the person would paste it, with the verdict and any open fail as one plain line. Their rewrite, when they make one, goes to `bank/rewrites/` as a pair when they ship it (`/review`, "ship it").

Long copy (a pamphlet, a sales page) runs this chain one section at a time; the calling skill says how.

## Never

- Never invent a testimonial, a result, a client, a number, a deadline, a limit or a value.
- Never use a fear, a WON'T or a pain the research doesn't show.
- Never let a selling line be true only if things go well.
- Never judge the copy in the pass that wrote it.

## Studio notes

When this standard made you guess, write one line per guess to `studio-notes.md`.
