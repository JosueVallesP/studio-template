---
name: job-manifesto
description: >-
  Writes the person's manifesto from their confirmed canon: why they do what they do and why others should care, carrying their thesis, philosophy and POVs and the three tenses (then, now, future) set in relation to their cause. Two outputs: the full internal version the studio draws from, and a public version whose form and voice follow the brand. Built from a structural study of 28 manifestos; every claim traces to a confirmed entry, every belief carries its ground, and it fails the moment another name could go on it. Use for /manifesto, "write my manifesto", "what do I stand for, in one piece", after the thesis is confirmed and before the visual identity.
---

# /manifesto

Method by Josué Valles, the studio's author. The structural findings are from a study of 28 manifestos (list at the end).

## What it is

The manifesto shows why this person does what they do and why others should care. It brings the top of the person layer into one piece: the thesis, the philosophy, the POVs, and the three tenses (defined once in `skills/craft-three-tenses`), set in relation to the cause, not the person's life story:

- **Then:** how things were. A good that was lost, or an earlier attempt that failed.
- **Now:** what's broken, with evidence.
- **Future:** what should be, and what the person is building toward.

## Where it sits

After the thesis is confirmed (`canon/person/thesis.md`, `status: confirmed`) and before the visual identity. The manifesto feeds `setup-visual-identity`: `craft-contradiction` starts from the association the person wants to be known for (the thesis gives it) and looks for two opposite sides already true of them (the then, the now and the vow are where those tensions sit). No visual version at this stage.

## What it reads

In this order, and nothing else for facts about the person (`CLAUDE.md` rule 1):

1. `canon/person/thesis.md`: the claim, its catalyst and catalyst story, who it's for, what it changes, the falsifier.
2. `canon/person/philosophy.md`: the premise the POVs share.
3. `canon/person/povs.md`, confirmed entries only, each with its ground and its condition.
4. `canon/person/values.md` and `behaviors.md`: what wins when things conflict, and what they do that someone could film.
5. `canon/bank/stories.md` and `proof.md`: the evidence for the now, and the story of a value that cost them something.
6. `canon/vehicle/vehicle.md` and `canon/strategy/brand-strategy.md`: the goal, who this is for, the anti-associations, the channel the brand lives on.
7. `canon/voice/voice-guide.md` and the right side of `bank/rewrites/`, then `skills/craft-house-rules` for the method and the rules.

When something is missing, say which interview unlocks it (`skills/setup-brand-tree/interviews/`), and offer a draft only if the person wants one now: `status: draft`, with a line at the top of the draft saying the piece isn't settled until that interview has run.

## What 28 manifestos share

Nearly every one uses most of these moves, roughly in this order. They're the material to compose from, not a template to fill:

1. A frame that says why this exists now (a moment, a story, an image, a question; the strongest open with an awakening before any belief).
2. Who "we" are, or who is speaking, often defined by practice.
3. A founding claim or philosophy, stated early; everything else argues from it.
4. The broken now.
5. An opposing force: more often a system, a habit or a mood than a person.
6. Evidence: a pattern of charges, or numbers.
7. The beliefs as a list.
8. An honest concession or an answered objection, in the reader's words.
9. A vision of the future.
10. A close that turns outward: a call, a vow, a pledge, an invitation.

What the study says about the tenses: the present dominates; the past appears as a lost good or a failed predecessor; the future is the tense most often thin or missing, with rules standing in for it. Brand manifestos almost always skip the past. A manifesto with a real then, now and future already stands apart.

## How the person's layers map onto the moves

| Move | Comes from |
| --- | --- |
| The frame and the why | The thesis's catalyst, and the story of a value that cost them something |
| Then, now, future | Their POVs and stories, set in relation to the cause |
| The founding claim | The philosophy |
| The broken now and its evidence | POVs with their ground; proof and stories |
| The opposing force | What their POVs argue against; the anti-associations |
| The beliefs list | The confirmed POVs, each with its ground |
| The concession | The conditions on their POVs (when each isn't true), the stop list |
| The vision | The thesis, told as the future it proves |
| The vow | Their behaviors, stated so someone could check them |
| The invitation | The vehicle: who this is for and how they can join |

The thesis is the claim the whole manifesto argues.

## The structure follows the material

No fixed template. Pick the shape from what the person's material is strongest in:

- Lots of evidence and proof: a declaration (principles, evidence, verdict, pledge; the 1776 shape).
- A strong origin story: open with the awakening (Futurism, the Hacker Manifesto, Port Huron).
- A clear method: a program (who we are, how the world works, what we'll do, how you help; Bauhaus, Stallman).
- A sharp opposing force: a letter to that force (Barlow).

Patagonia's "Don't Buy This Jacket" is the closest single model for a personal brand: an anthem's provocation built on a charter's evidence and promises.

Moves worth borrowing, as possibilities: rewrite one word of a text the audience reveres (Seneca Falls on 1776); one concrete metaphor for an abstract complaint (King's bad check); answer objections in the reader's own words (Marx, Stallman); headings as the reader's questions (GNU); take the insult used against you and make it your banner (the Hacker Manifesto); "X over Y" pairs plus the concession that keeps them fair (Agile); answer an earlier manifesto by adding what it missed (Software Craftsmanship); indict yourself with evidence (Patagonia); state your decision rules and admit they're a choice (Bezos, 1997); move from "we believe" to "I swear" (Dogme 95); open by questioning your own work (Rams); the old order against the new in one two-column table (Haraway); describe the principles as how you already behave (Burning Man); follow the beliefs with a program (Bauhaus).

## Form and voice

Both follow the person, by rule, not by guess. Propose each with its reason; the person decides.

**The public form follows how people meet the brand** (from the vehicle and the channel strategy):
- A body-of-work brand on a long-form channel (Substack, a site): an essay-length manifesto.
- A brand people meet in short posts: a short cut, every line keeping its ground, so it never turns into generic virtues.
- A practice or business brand: a charter, with vows clients can check.

**The voice follows who actually stands behind it:**
- "We" only when the person speaks for a real group (a community, their clients, a team, a movement). A "we" with nobody behind it is borrowed authority.
- Otherwise "I" throughout.
- The voice guide decides everything else.

## How it runs

1. Check the inputs. Name what's missing and which interview unlocks it.
2. Pick the shape from the material, and the form and voice from the brand. Say the choice and the reason in two lines.
3. Draft the full version, three times (`craft-house-rules`, "How the sentences get written"): different in which move leads and how it moves, not in wording. The person's quotes carry the beliefs where their words are strong; the writer connects and frames, and adds no belief.
4. Run the gates (below), `scripts/check-prose.py` and `scripts/voice-diff.py` on each. Hand the three to the `judge` agent with the gates; it picks one or sends all back.
5. Cut the public version from the chosen full one, in the form the brand calls for.
6. The person reads both. Their edits become pairs in `bank/rewrites/`. The full version goes to `canon/manifesto.md` as `status: draft` until they confirm it (rule 6); the public one to `pieces/<date>-manifesto/`.

## Gates

It doesn't ship until:

1. **Every claim traces** to a confirmed entry or the person's words. The writer connects and frames; it adds no belief.
2. **Every belief has its ground.** This separates it from claims with nothing behind them.
3. **The swap test passes.** If another person could sign it, it fails.
4. **All three tenses are present**, and the future is more than one closing line.
5. **The now carries evidence:** a story, a number, a pattern.
6. **At least one honest concession** or answered objection.
7. **The vow is checkable.** Someone could tell whether the person kept it.

## A living document

Bezos re-attached his 1997 letter every year; Mozilla added an addendum instead of rewriting; Mau called his "incomplete". When the canon changes, the librarian proposes an addendum, not a rewrite.

## Never

- Never add a belief, a story or a fact the canon doesn't hold.
- Never fill a missing tense with a generality.
- Never write "we" for a group that doesn't exist.
- Never make a visual version here; that comes after the identity.

## The 28 manifestos studied

Political and founding: the US Declaration of Independence (1776), the Communist Manifesto (1848), the Declaration of Sentiments (1848), the Port Huron Statement (1962), "I Have a Dream" (1963), the GNU Manifesto (1985), Barlow's Declaration of the Independence of Cyberspace (1996). Art and design: the Futurist Manifesto (1909), the Bauhaus Manifesto and Program (1919), the Manifesto of Surrealism (1924), First Things First (1964, 2000), Dogme 95 (1995), Bruce Mau's Incomplete Manifesto for Growth (1998), Dieter Rams' ten principles. Tech, work and ideas: A Cyborg Manifesto (1985), the Hacker Manifesto (1986), the Cluetrain Manifesto (1999), the Agile Manifesto (2001), the Manifesto for Software Craftsmanship (2009), the Mozilla Manifesto (2007, 2018), Stop Stealing Dreams (2012). Brand and personal: Apple's "Think Different" (1997), the Holstee Manifesto (2009), the lululemon manifesto (1998), Patagonia's "Don't Buy This Jacket" (2011), Burning Man's Ten Principles (2004), Kickstarter's PBC charter (2015), Amazon's 1997 shareholder letter.
