---
name: job-shape
description: Finds the ideas in raw material (a call transcript, a voice memo, a journal entry, notes, an old post, idea bank entries marked raw) that can stand on their own, tests each one against the chain a reader goes through (complete, legible, transferable, unexpected, useful), says what each one gives the reader and at what level, and suggests the form and the move. Writes idea cards to the idea bank for the person's yes. Use for /shape, "fill my idea bank", "go through all my material", "find the ideas in this", "is this idea any good?", "what shape should this take?", "what's in this call?", or whenever capture has filed entries and nobody has judged them yet.
---

# /shape

Method by Josué Valles, the studio's author.

Valuable content changes what a reader does. People read for what helps them, even when they don't notice that's why; nobody cares about a story, an idea or a tactic unless it does something for them. So an idea only lands when it moves, step by step, from being about the speaker to being about the reader. Shape is the skill that does that moving, in two jobs:

1. **Find the clip.** Pull out an idea that stands on its own, the way a good short is cut from a long interview. Bible scholars call a passage that holds together as a unit a pericope; a random verse thrown at someone cold means nothing to them. Most of what a person says in an hour leans on something they said ten minutes earlier.
2. **Translate it.** Close the distance between the world the idea came from and the reader's world. The idea stays the same; its context, frame and form change so the reader can use it.

Virality isn't the goal. An idea that clears every step below is one people pass on, because it's useful to the next person too.

## Where it sits

- `role-capture` is the fast intake: it splits raw input into one entry per idea, in the person's words, and files them. Shape is the judging: it reads what capture filed (or raw material directly) and decides which entries are ideas worth a piece, what each one needs, and what shape it takes.
- Shape hands to `/post`, `/essay` and `/visual`, whose moves stages pick the specific move from their libraries. Shape says what kind of thing the idea is and why; the format skill says which of its moves fits (on LinkedIn, 18 hook moves and 9 structures; on Substack, 16 title moves, 15 openings and 13 structures).
- Shape never drafts. It writes idea cards.

## What it reads

- The input the person gave: a transcript, a memo, a journal entry (only entries whose frontmatter says `visibility: open` and has no `never:` line; never `private`), notes, an old post, or "the call from Tuesday" (find it in `inbox/` or `inbox/done/`; if it isn't there and a call recorder is connected, pull it first as `skills/setup-sources` says, under "Pulling").
- Or the whole material ("fill my idea bank", "go through all my material", or a yes to the offer `/post` makes when the bank is empty): read everything in `material/`, oldest first, and `inbox/done/`, one file at a time, and run the chain on each. File the credibility in the same pass, as `skills/role-capture` step 3a says: the results, clients, things said about them and the rest go to `bank/credibility.md`, paired with the idea cards they back. Cards and entries go to the banks as each file is done, so a long sweep that stops halfway keeps what it found. Skip ideas already in the bank. Report at the end in a few lines: how many idea cards and credibility entries, the three strongest ideas, the views with nothing behind them yet, and the files that held none.
- Or, with nothing given: `bank/ideas.md` entries with `status: raw` or `strength: maybe`, newest first, and anything capture filed since the last `/shape` (each run ends by writing one line to `sessions/log.md`: `<date> · shape · <n> cards, <n> credibility entries`; read the date from the latest one).
- For the reader's side: `canon/strategy/audience.md` (who the reader is, what they already know, the awareness stage), `canon/core-summary.md`, the content plan's branches. Without a canon, the reader is whoever the person said they write for in `config/intake.yaml`.
- `skills/craft-house-rules` for the writing of the cards, and `CLAUDE.md` rules 1 and 3 for what can and can't change.

## Job 1: find the clip

Read the whole input first. Then list every candidate idea, in the person's words (the `raw` text), and run each through the chain. Each step is something that has to happen in the reader for the idea to change what they do:

| What happens in the reader | Criterion | Test | If it fails |
| --- | --- | --- | --- |
| They understand it | **Complete** | Would a stranger get it cold, with no context from the call? | Add the missing context: who, what situation, why it came up |
| | **Legible** | Does it fit a shape people already know how to follow? | Give it a familiar shape (Job 2) |
| They see it's about them | **Transferable** | Does it hold for someone in a different field or situation than the person in the call? | Lift it from the case to the principle; keep the case as evidence |
| Their pattern breaks | **Unexpected** | Is it more than a platitude? It can be logical, even obvious once said, but it isn't common practice: what does the reader currently do or believe that this cuts against? | Find that practice or belief. If there's none, it's a platitude: drop it, or find the angle that makes it bite |
| They can act | **Useful** | Afterwards, can they see something differently or do something in their own world without much friction? | Name the shift or the action |

"Unexpected" passes on the idea or on the frame. An old truth from an angle that breaks the reader's pattern counts; a cliché doesn't, however well phrased.

**No fixed number.** Bring back every idea that clears the chain, strongest first, plus any near-miss that one question to the person would fix. A fixed number makes you pad a thin transcript or cut a rich one. If a call holds one good idea, bring back one. If it holds none, say so; that's a true result, not a failure.

**Only what needs attention.** The steps an idea passes stay silent. For any step it fails, one plain sentence on what's missing and the question that would fix it ("This only works for agencies right now. Who else has this problem?").

## Job 2: translate it

Two questions decide the form:

1. **What does it give the reader?** Something to **do**, a way to **see**, a reason to **believe**, or a **direction** to head in.
2. **At what level?** From a tactic for tomorrow up to a strategy for years.

| It gives the reader | The forms it tends toward |
| --- | --- |
| Something to do | Steps, a checklist, a before-and-after |
| A way to see | A contrast, a reframe, a framework, a named pattern |
| A reason to believe | A story with proof, a case, evidence |
| A direction | A principle, a vision, a then-now-future |

Then the translation move. Each has a principle behind it and a gate that makes it fail honestly instead of producing filler. These are possibilities to choose from, never a checklist:

- **Divide** (lists, types, steps, frameworks, 2x2s). A list is a claim that these things, and only these, are what matters; what's left out is the point. Every item is the same kind of thing at the same level (Barbara Minto, *The Pyramid Principle*: one grouping logic, no overlaps, no gaps), and the order means something. *Gate:* could any item be swapped for a generic one without anyone noticing? Does the list make a claim someone could disagree with? A 2x2 only works when the axes are independent and every quadrant has a real example.
- **Contrast** (compare, before and after, reframe, tension). People understand a thing by what it isn't. The useful comparison isn't with the opposite but with the thing the reader currently confuses it with. *Gate:* the reader has to believe today that the two are the same, or close.
- **Reveal** (breakdown, zoom in and out). Show the step nobody sees between the visible result and its cause; move between the specific case and the principle (S.I. Hayakawa's ladder of abstraction). *Gate:* does it show a step the reader didn't know existed?
- **Transfer** (analogy, borrowed story). Good analogies share how the parts relate, not how things look (Dedre Gentner's structure-mapping). *Gate:* the relation carries over, and the analogy predicts something true about the original. A borrowed story is real and sourced (`borrowed: verify`), never made up.
- **Name**. A name turns a pattern into something people can hold and repeat. *Gate:* the pattern already shows up in the person's material at least three times. Otherwise it's a label on a one-off.

## The fidelity gate

Translation changes the context, the frame and the form. It never changes the idea. But people don't always say what they mean on the first try, so the gate isn't "word for word". It follows `CLAUDE.md` rule 3:

- The raw words stay in the card with their source.
- The translated idea goes beside them, and the person is asked: "Is this what you meant, or closer to it?"
- If they take it, it's theirs. If they say keep mine, that's final. If they say "that's what I was trying to say", the sharper version becomes theirs.
- Facts about the person never move (rule 1). The reasoning, framing and analogies are the studio's own work and are marked as such.

## What it writes

Idea cards, as entries in `bank/ideas.md` (the template's fields, plus a `shape:` block), one per idea that cleared the chain or is one question from clearing it:

```
shape:
  gives: <do / see / believe / direction>
  level: <tactic / practice / principle / strategy>
  form: <the form it tends toward, one line>
  move: <divide / contrast / reveal / transfer / name>, and why in one line
  fails: <the one or two steps it fails, each as a plain sentence and the question that fixes it; or none>
  translated: "<the idea said for the reader, in one or two sentences; waiting for the person's yes>"
  reader_belief: "<what the reader currently does or believes that this cuts against>"
```

An existing entry gets the block added; a new one from raw material gets the full entry, `raw` word for word. A card waiting for the person's answer to the fidelity question is `status: shaped` (shaped and waiting for a yes, so `/tidy` never archives it as stale), then `ready` on their yes, or back to `raw` when the answer shows something is still missing. A card that cleared everything and got its yes is `ready` and `wanted_now` if it fits a branch this quarter.

**The seed record** (the idea bank template defines it). A new entry starts at `stage: seed`. A fail that is a doubt about whether the idea holds (the believe step: no evidence beyond the person, a case it doesn't survive, an objection a reader would raise) also goes in the seed's `pushback` as `open`, with the date, `from /shape` and the question, so it comes back later instead of staying buried in `fails`. A fail about how it's said (complete, legible) stays in `fails` only. The person's yes to the translated line is them confirming what the idea says, which is what moves a seed to `sprouting`: say so in the same breath ("That moves it from seed to sprouting.") and set it, unless they say not yet. Then bring the first wind (the idea bank template defines it): one objection, their answer into `pushback`. When several cards get their yes in one session, one objection each, after the last card, one at a time. An answer to an open pushback question goes into that line in their words.

## What it says to the person

Strongest first. For each idea: the translated line, what it gives the reader, the suggested form in plain words ("a before-and-after: what the client thought onboarding was, what it turned out to be"), and only the fails with their questions. Then the fidelity question for anything it rewrote. For a card drawn from a journal entry, ask the journal's question first, before the card goes into the bank: "There's an idea in <day>'s entry about <topic>. Want me to keep it?" (`skills/job-journal`, "Using an entry means asking"). On a no, nothing is filed, and the entry's idea isn't raised again. On a yes, the card is filed with `source: journal <date>` and `permission: anonymize` when it touches anyone else. Then what it left out and in one line why ("the rest was about that project only"). Under 150 words for a thin call; a rich one takes what it takes, one idea per paragraph.

Then the offer: "/post", "/essay" or "/visual" with the card's ID, for whichever the form points to.

## Never

- Never draft. The format skills draft.
- Never reword the `raw` field. The translation goes in `shape.translated`, beside it.
- Never invent context to pass "complete". If the context isn't in the material, ask for it.
- Never pass "unexpected" on phrasing alone. A platitude said well is still a platitude.
- Never pad to a number or cut to one.
- Never read a journal entry marked `private`.
- Never write to the canon. A connection across entries (a belief that keeps showing up in three coats) goes to `proposals.md` as `seen` (`CLAUDE.md` rule 8), after checking the open proposals and the cap in `templates/proposals.md`; a new belief stays an idea card.

## Studio notes

Where this skill made a run guess (a chain step that was hard to judge, a form that didn't fit the table), one line in `studio-notes.md`.
