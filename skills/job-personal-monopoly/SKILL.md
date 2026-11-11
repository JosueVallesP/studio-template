---
name: job-personal-monopoly
description: >-
  A guided interview, one question at a time, that takes a consultant, coach, freelancer, solo operator or founder from "I help everyone with everything" to a written Personal Monopoly document: the value they provide (from what they've already done), the rare crossing that makes it theirs, the exact people it's for, what they refuse, a one-sentence positioning thesis, and six to eight decisions with a first move each. Reads the canon and material first and never re-asks a confirmed answer; what it finds goes into the canon as drafts. Use for /finding-your-personal-monopoly, "find my personal monopoly", "help me position myself", "I don't know how to describe what I do", "I'm competing on price", "who should I target", "what's my angle", "I want to charge more", or a bio, headline or service list shared with "what's wrong with this?".
---

# /finding-your-personal-monopoly

Method by Josué Valles.

A personal monopoly isn't being the best at one thing. Being the best at one thing means competing with everyone in your field forever. A personal monopoly means being one of very few people who combine two or three things that rarely go together, for a group of people who need exactly that combination. An accountant who used to run a kitchen doesn't compete with accountants: most accountants know numbers and not restaurants, most chefs know restaurants and avoid the numbers, and restaurant owners who are busy but not profitable will pay for the one person who knows both.

The person already has the raw material. They've done the work, solved problems, and watched their field do things in ways that annoy them. Nobody has pulled it out of them and arranged it. That's this skill's job, and it does it by asking about what happened, never about what they think of themselves (`skills/craft-interview`).

The frame the session works through is one sentence:

**Strategy is the unique value you as a person provide to a specific network, through deliberate choices about what you won't do.**

Four parts: the value (what people actually got from you), what makes it unique (the monopoly), the specific network (named tightly enough that the right person thinks it was written for them) and what you won't do (the refusals that make the rest stronger).

## Where it sits

The brand tree interviews (`skills/setup-brand-tree`) build what the person believes, layer by layer. This skill builds where they stand in a market, in one sitting. The two meet at the target association in `canon/strategy/brand-strategy.md`: the first thing people should think of when they hear the person's name.

- **Before the brand tree,** for someone with a working practice who needs positioning this month. Everything it finds lands in the canon as drafts, so the interviews confirm them later instead of asking again. It gives `/strategy` a draft target association, a segment and proof to work from.
- **After the brand tree,** it skips every stage the canon already answers and spends the session on the crossing and the decisions. A confirmed thesis, POVs and proof make it shorter and sharper.
- **Instead of the brand tree,** never. It finds a position; it doesn't find values, a philosophy or a thesis in the brand tree's sense, and the writer still needs those for pieces that sound like the person.

A note on words. The method calls its one-sentence result a thesis. In the studio that sentence is a **positioning thesis**: what you provide, to whom, and why you can. The brand tree's thesis (`canon/person/thesis.md`) is a different thing: the one claim the person's body of work exists to prove. Say this to the person in one line when stage 5 comes, so they don't mistake one for the other.

The related command: `/building-your-message` is the next step (it turns this position into a story, an enemy and an About section).

## What it reads first

Before the first question, read:

- `canon/progress.md`, `bank/map/findings.md` (or `canon/readback.md` in an older studio) and `canon/canon-index.md` if they exist: what's confirmed, what's draft, what the map found.
- `canon/bank/proof.md` and `stories.md` (stage 1), `canon/person/povs.md` (stage 2), `canon/strategy/brand-strategy.md` and `audience.md` (stage 3), `canon/person/stop-list.md` and `behaviors.md` (stage 4), `canon/vehicle/vehicle.md` (offers and prices, for the decisions).
- `material/` and `inbox/` (run `python3 scripts/inbox-to-text.py` first), `config/intake.yaml` and `canon/strategy/outcomes.md`.

Then sort each stage's questions three ways, before asking anything:

| What the files hold for this question | What you do |
| --- | --- |
| A confirmed entry | Don't ask. Say it back in one line with its ID ("Your best result on file is R2, the onboarding rebuild") and use it. If the person wants to change it, that's a proposal (below), not a fresh answer. |
| A draft entry, or a line in their material | Show it with its source and ask "is this right, in these words?", the way the map's review does. A yes with every required field present confirms it (`references/fields.md` in `skills/setup-brand-tree`). |
| Nothing | Ask the stage's event question. |

A stage the canon fully answers takes one message: what's on file, and "anything to add before we move on?"

## How to run the session

The interview follows `skills/craft-interview` and the house rules (`skills/craft-house-rules`, Part 2 included). Its anchoring move (an example of the depth wanted, from a field far from theirs, never presented as a real case) is the one this skill uses before most questions. What's particular to this skill:

- **Pacing.** This skill's own pacing overrides craft-interview's default of three questions per step. It's set in `references/interview-moves.md` ("Pacing"): five to seven exchanges in each of stages 1 and 2, fewer in the later stages, one question per message, about 40 minutes in all. A stage the files already answer takes one message, and the exit tests decide when to move, not the count.
- **Say why before you ask.** One line of context before each stage, and before a single question where it helps.
- **Refuse category answers, but know the ladder.** "I provide strategic value" is a label. By default, sort silently against the frameworks in `references/frameworks.md` and never open with a list, because people handed a menu pick the label that sounds best rather than the one that's true. When someone can't answer at all, run the ladder in `references/interview-moves.md` ("When they have no idea"): guess from their material, then teach with two or three named examples, then switch to behavioral questions, then homework. Never read out a bare list of labels and ask them to choose.
- **Push back once, then move.** One sharper follow-up. If it's still vague, note it as thin and keep going.
- **Play back what you heard** at the end of each stage, in a line or two, and ask whether you got it right.
- **Show progress:** "That's stage 2 of 5 done."
- **When they stall, guess.** Two or three specific guesses built from what they already said. Correcting is easier than generating.

Read `references/interview-moves.md` before stage 1.

## Stage 0: Orientation

One message that ends with the first question (`CLAUDE.md` rule 7: what's about to happen, why, what they'll have, how long). Keep the structure, adapt the words, and leave out anything the person already heard from `/start`:

- What they'll walk out with: a written document (the value they provide, what makes it theirs, who it's for, what they'll refuse), a one-sentence positioning thesis to run decisions through, and six to eight decisions with a first move each, small enough to start this week.
- What a personal monopoly is, with the accountant who ran a kitchen.
- The four-part sentence above, and that the session walks through it in order.
- How it works: one question at a time, each with an example of the depth wanted; about 40 minutes; best in one sitting. If canon or material already answered some of it, say so and how much shorter that makes it.
- The honest part: the document can only be as good as what they give, the studio won't invent anything about them, and stories beat short answers. Answering by voice (dictation) gets better stories than typing.

Then, if `config/intake.yaml` doesn't already say it: "What do you do, and who pays you for it right now?" After that, one more: "What made you want to sort this out today?" That second answer matters more than it looks. Someone who just lost their biggest client needs a different document from someone who's fully booked and wants to double their rate.

Pick the track:

- **Track record:** they have paid clients or shipped work. Everything runs as written.
- **Cold start:** new to working for themselves, or switching fields. Same questions; the hunting ground is jobs, internal projects, side work, volunteer work. Never fill a gap with invented evidence. A thin document that says "your first job is to go get proof" beats a full one built on air.

## Stage 1: The value you provide

Open with a line like: "This is stage 1 of 5. Before we can find what's unique about you, we need what people actually got from you, not what your website says."

Ask, one at a time, skipping what the proof and story banks already hold:

1. "Think about the last twelve months. Tell me about one person or company that's better off because of you. What was going on before you got involved, and what changed?" Show the depth: "something like: a founder's biggest plan was losing money, and three months after the pricing was rebuilt, revenue on it was up".
2. "Give me another one." Repeat until there are three or four. Ask for numbers and timeframes where they come naturally; don't interrogate someone for metrics they never tracked.
3. "Has anyone brought you a problem that other people had already tried and failed to fix? What happened?"
4. "Tell me about the last time someone asked for you by name, rather than for your job title or your company. What did they want?"
5. "Pull up the last few messages where a client thanked you. What did they say, in their words?"
6. "Look at the last five messages that asked you for help. What did each one ask about?"

Sort what you hear against the ten value types in `references/frameworks.md`, silently. Close the stage by naming the two or three types you heard, in plain words, each tied to something they said, and ask whether that lands.

**Exit test:** two or three value types, each with at least one real example.

## Stage 2: What makes it unique

Open with: "Stage 2 of 5, and this is the stage that finds your monopoly. Plenty of people deliver what you just described, so we're looking for why you deliver it differently, and that reason usually hides in the parts of your history that look irrelevant."

Ask, one at a time, starting from any POV or story on file:

1. "Walk me through how you got here: roles, industries, detours, the things you'd leave off a CV." Show the depth with an odd sequence from a far field ("investment banking, then teaching, then a startup").
2. Don't ask which two of those rarely go together. Give your own read: you can usually see the odd combination before they can. "From what you said, the rare part looks like <A> plus <B>. Is that right?"
3. "What's the last piece of standard advice in your field you told a client to ignore? What happened when they did?"
4. "Tell me about a time you saw something in a client's situation that the people around them had missed. What let you see it?"
5. "Where have you spent time that most people in your field never get into? A room, a set of numbers, a group, a job. What did you see there?" Show the depth: "something like: two hundred pitch meetings from both sides of the table".
6. The most useful question in the session: "When did you last get angry watching how something in your field was done? I don't mean mildly annoyed. What happened, and who paid for it?"

Question 6 usually produces the sharpest material, because anger points at a better way they can already see. If the answer is lukewarm, use the heat probe: "What did that cost the people it happened to?"

Then draft two or three candidate monopolies, out loud, in this shape, and let them pick and edit:

> "You're one of very few people who <A> and <B>, which means you can <what that lets you do that others can't>."

Each candidate is built only from what they said in this session or what's on file, and each part shows its source when you hand it back.

**Exit test:** a crossing of two or three things, phrased so a stranger could repeat it back.

## Stage 3: Who it's for

Open with: "Stage 3 of 5. A monopoly only counts if it's a monopoly for someone specific. We'll start from the people you've already served well rather than from a market you'd like to have."

If `brand-strategy.md` has a confirmed segment (a G entry), say it back and ask only what it lacks. Otherwise, one at a time:

1. "Of everyone you've worked with, who got the best result? Describe them: size, stage, role, what was happening in their business at the time."
2. "What did those best ones have in common?"
3. "Think of the last call that left you with more energy than you started with, and the last one that drained you. Who was on each?"
4. "Who was the last person who understood what you do within thirty seconds? And the last one who never quite got it?"

Then draft the specificity sentence for them and let them correct it. Drafting works far better than handing someone blanks:

> "I help ______ who are struggling with ______ because they are ______ and want to ______."

Every blank needs concrete detail. "Entrepreneurs" fails. "Solo consultants billing 100k to 300k who are excellent at the work and have never written down how they do it" is the depth wanted. The five layers for sharpening a segment are in `references/frameworks.md`.

Then a short reality check, one question each, skipping what `audience.md` already answers:

- Roughly how many of these people exist?
- Can they pay? (Point to their prices in `vehicle.md` when they're there.)
- Do they know they have this problem, or do you have to teach them first? (This is the awareness stage in `audience.md`.)
- Are they looking for a fix right now, or living with it?

If the answers say the segment can't pay or barely exists, say so plainly and help them adjust. Better now than in six months.

**Exit test:** all four blanks filled with concrete detail, and a segment that exists and can pay.

## Stage 4: What you refuse

Open with: "Stage 4 of 5, and it's the one people usually skip. A monopoly is built as much from what you turn down as from what you take on, because every refusal makes your yes worth more."

Start from `stop-list.md` and any refusal in `behaviors.md`. Then, one at a time:

1. "Tell me about a recent project that drained you even though it paid well. What was it?"
2. "Which client or project in the last year gave you the worst return for the effort you put in?"
3. "Look at last month's work. Which parts could you have handed to any competent person with no loss to the client?"
4. "What did you say yes to in the last three months that the people we just named wouldn't hire you for?"

Turn each answer into a refusal with a reason: "I don't take X, because Y." The reason points back at the segment or the value; a refusal without a reason reads like laziness. Watch for soft ones: "I won't work with rude clients" is what everyone says. "I won't take projects under 10k, because they need the same setup as a 60k one and the setup is where the value is" is the depth wanted. The five kinds of trade-off are in `references/frameworks.md`; take refusals from two or more kinds rather than three of one.

**Exit test:** three refusals, each with a reason that connects to stage 1, 2 or 3.

## Stage 5: The positioning thesis

Open with: "This is the last stage before I write it up. I'll compress all of it into one sentence, and your job is to tell me which version sounds like you." Add the one line on words from "Where it sits".

Write two or three versions yourself, different in what they lead with (the identity, the value, the refusal), not only in wording:

> "I'm the only <unique identity> who provides <specific value> to <specific network>, because I refuse to <key exclusions>, which lets me <resulting advantage>."

Each version is assembled from their words; under each, the lines it came from. Ask which one sounds most like them and what they'd change, and edit together until they say yes without hedging. If none can honestly carry "the only", write "one of very few" or a plain sentence. Never force a claim the evidence doesn't carry.

**Exit test:** one sentence they'd say out loud to a stranger without wincing.

## Stage 6: Write it up

Read `references/document.md` and follow it. Two halves: what's true, and what to do about it. The decisions half is what makes the session worth their time.

- **The document** is for the person. Write it once, to them, in their words, with every claim carrying its source (a canon ID, `material/<file>: "<their words>"`, or `said today`). Save it to `canon/strategy/personal-monopoly.md` with `status: draft` and `source: /finding-your-personal-monopoly, <date>` in the frontmatter; when they say yes to it, add `person_confirmed: <date>`. Run `python3 scripts/check-prose.py --mode prose` on it and fix every fail.
- **The public lines in it** (the "what to say" decision: a headline, a one-liner, the opening of a bio) are a piece other people will read. They run through `skills/craft-sales-copy` as one piece, `pieces/<yyyy-mm-dd>-positioning-lines/`, with the copy kind `positioning line`: that standard's three drafts, scripts and judge in a fresh context. The judge's check 12 for this kind is: every claim traces to the session or the canon, and nothing claims more than the evidence carries. The chosen line goes in the document.

## Where what it finds goes

Nothing this skill finds is confirmed by the skill. It follows the route in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes": a new finding becomes a `draft` entry in its canon file, with `quote` (their words), `sources` (`said in /finding-your-personal-monopoly, <date>`, or the file) and a `log` line; a change to a confirmed entry goes to `proposals.md` (template in `templates/proposals.md`, `proposed_by: /finding-your-personal-monopoly`), naming the file and ID it would change. A draft entry is confirmed in the session only when the person says it's right and every required field is present (`skills/setup-brand-tree/references/fields.md`); otherwise it stays draft with "agreed in /finding-your-personal-monopoly <date>" in its log. Rule 6 holds throughout.

| What the session found | Where it goes |
| --- | --- |
| Results with a before and after (stage 1) | `canon/bank/proof.md`, R entries, numbers exactly as given, with `permission` asked ("with names, without names, or not at all?") |
| The stories behind them | `canon/bank/stories.md`, S entries, `raw` in their words |
| The two or three value types | The value types line of the character sheet in `canon/strategy/brand-strategy.md`, as a draft with the R and S IDs as evidence; `strategy-brand` reads it |
| The standard advice they told a client to ignore, the anger, what they saw that others missed (stage 2) | `canon/person/povs.md`, P entries: the claim, what it rejects, the ground from the story, the condition asked or left empty (confidence `forming` until they name one) |
| The crossing (the monopoly) | The target association under "Known for" in `brand-strategy.md`, as a draft. If a target association is already confirmed, the crossing goes to `proposals.md` as `kind: change to <ID>` naming that line |
| The segment and the specificity sentence (stage 3) | A G entry in `brand-strategy.md` (situation, believes, wants, their words); the near-misses under "Not for" |
| Size, ability to pay, awareness, urgency | `canon/strategy/audience.md` for that segment (awareness, and the counts beside anything said) |
| Content or positioning refusals (topics, claims, fights they won't pick) | `canon/person/stop-list.md`, X entries, `why` in their words |
| Work and client refusals ("I don't take X, because Y") | `canon/person/behaviors.md`, A entries of type `refusal` when they describe something they already do; otherwise `canon/vehicle/vehicle.md` under Constraints as a rule they've decided on |
| The positioning thesis | `canon/strategy/personal-monopoly.md`, the document itself, which is the one place it lives; `brand-strategy.md` points to that file from "Known for" rather than holding a copy. Never into `canon/person/thesis.md` |
| Something seen across answers (two stories with the same turn, a belief every answer assumes) | `proposals.md`, kind `seen`, with the quotes and one question (rule 8) |

Update `canon/canon-index.md` and the layer table in `canon/progress.md` (create both from `skills/setup-brand-tree/templates/` if the brand tree hasn't run, and strip the example blocks). Tell the person in one or two sentences what went into their files as drafts and that the interviews confirm them, so nothing gets asked twice.

## What goes wrong

- **Skipping the orientation.** A question with no context feels like a form, and people give short answers to forms.
- **Accepting the first answer.** The first is the rehearsed one; the second or third is where the real material sits.
- **Reading the frameworks out loud too early.** They came for clarity about themselves, not a lesson in categories.
- **Flattery.** If the evidence is thin, say so and make finding evidence the first decision. Telling someone they're rare when they're not is worse than useless, because they'll act on it.
- **Inventing detail.** If they said "a few clients", the document says "a few clients".
- **Batching questions.** One at a time.
- **Re-asking what's confirmed.** The files answered it; say it back and move on.
- **Stopping at the thesis.** The sentence is the summary. The decisions are the point.

## Never

- Never invent a client, a result, a number, a quote or a story. Every fact about the person comes from the four sources in `CLAUDE.md` rule 1.
- Never confirm a canon entry without the person's yes, and never change a confirmed one; that's a proposal.
- Never present an anchor example as a real case or as the person's view.
- Never promise revenue or a price result.

## Studio notes

When this skill made you guess (a finding with no clear canon home, a stage the canon half-answered), write one line per guess to `studio-notes.md`.
