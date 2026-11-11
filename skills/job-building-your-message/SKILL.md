---
name: job-building-your-message
description: >-
  A guided interview, one question at a time, that turns a person's positioning into a messaging framework built from things that happened: two or three authority moments (at least one a failure), the one enemy they fight (a practice or belief, never a person), their personal stakes and what the fight has cost them, the condition they're working toward, and an expanded thesis that filters every piece. Ends with five to seven decisions, a drafted About section and the first content pillars. Reads the canon and the Personal Monopoly document first and never re-asks a confirmed answer; what it finds goes into the canon as drafts. Use for /building-your-message, "build my message", "turn my positioning into content", "what should my story be", "I have my personal monopoly, what now", "find my enemy", "my content sounds generic", "help me with my About section".
---

# /building-your-message

Method by Josué Valles.

`/finding-your-personal-monopoly` finds what the person is in a market. This skill finds what they say. People don't connect with a strategy; they connect with the story underneath it, and this interview builds that story from things that happened: failures, the standard practice that burned them or their clients, the bets they made with their own time and money.

There are three levels a personal brand can sit at, and the session pushes toward the third:

- **About you:** your achievements. "I've worked with 50 companies and won three awards." There's nothing in it for the reader.
- **About their problem:** "I help SaaS companies fix churn." It works, and it sounds like every competent competitor, because solving problems is the price of entry.
- **About a change you make together:** "Too many good products die because founders treat retention as a number on a dashboard instead of a design problem, and we're changing that." This is the level where people take the message as their own and repeat it in rooms you're not in.

These are the three purpose levels on the strategy's character sheet (egocentric, customer-centric, purpose-centric, in `canon/strategy/brand-strategy.md`). When a draft line slips back to the first or second, name it and lift it.

## Where it sits

- **After the positioning.** It builds on a target association, a segment and the refusals: from the Personal Monopoly document (`canon/strategy/personal-monopoly.md`), or from `brand-strategy.md` when the interviews already confirmed them. Without either, it runs a catch-up of four questions at most (stage 0) and marks the result standalone; if the catch-up shows the position itself is unclear, say plainly that this session will be stronger after `/finding-your-personal-monopoly`, and let them choose.
- **Beside the brand tree.** Most of what it finds is brand tree material, gathered through stories: a costly choice is a value's evidence, the moment they saw the enemy is often the thesis's catalyst, what a failure taught them is a POV's ground. Before the brand tree, this session leaves those as drafts the interviews confirm. After it, the session starts from the confirmed values, POVs and thesis and spends its time on the enemy, the stakes and the About section.
- **Before the manifesto.** The manifesto (`/manifesto`) is the long public form of the same material: then, now and future, built on a confirmed thesis. This skill's framework is the working version, and its authority moments, enemy and vision are what the manifesto later draws on.
- It doesn't rebuild the positioning. If the person wants to reopen the thesis, the segment or the refusals, note it in the document and suggest `/finding-your-personal-monopoly` again.

`setup-about-you` (`/about`) writes a different page: one page about the person for any AI to read. The About section here is the public profile text other people read.

## What it reads first

- `canon/strategy/personal-monopoly.md`, `canon/strategy/brand-strategy.md` (target association, segments, the character sheet's enemy and purpose level), `canon/strategy/audience.md`.
- `canon/bank/stories.md` and `proof.md` (authority moments), `canon/person/povs.md` (the enemy is usually what a POV rejects), `values.md` (costly choices), `thesis.md` (catalyst, `changes`, `implies`), `canon/manifesto.md` if it exists.
- `canon/progress.md`, `bank/map/findings.md` (or `canon/readback.md` in an older studio), `material/`, `inbox/` (run `python3 scripts/inbox-to-text.py` first) and `canon/voice/voice-guide.md`.

Sort each question the same three ways `/finding-your-personal-monopoly` does: a confirmed entry is said back with its ID and not asked; a draft or a line of their material is shown with its source and checked ("is this right, in these words?"); only a gap gets a fresh question.

If the person pastes a Personal Monopoly document they made outside the studio, read it, save it word for word to `material/<date>-personal-monopoly.md` with a one-line note at the top saying what it is, and treat it as material.

## How to run the session

The interview follows `skills/craft-interview` (its anchoring move included: an example of the depth wanted, from a far field, never presented as a real case) and the house rules (`skills/craft-house-rules`). Its pacing overrides craft-interview's default of three questions per step: up to four questions in a stage, one per message, five stages in about 35 minutes, and the exit tests decide when to move. Say why before each stage, play back each stage and show progress, as in `skills/job-personal-monopoly/SKILL.md` ("How to run the session"). Read `skills/job-personal-monopoly/references/interview-moves.md` for the probes and the ladder before stage 1, and `references/messaging-frameworks.md` here for the thinking and the teaching examples.

Two rules this module adds:

- **Events, not opinions.** An authority moment is a situation with an outcome. Stakes are money spent and jobs left. When someone answers with a belief, ask for the event behind it.
- **Failures outrank successes.** A failure with a lesson builds more trust than a win, and it's the story other people retell. If someone offers only wins, ask for the thing that went wrong, and say why you're asking.

## Stage 0: Orientation and catch-up

One message, ending with the first request (`CLAUDE.md` rule 7):

- What they'll have: a messaging framework (the moments that prove they can deliver, the broken practice they're fighting, why it's their fight, the better situation they're working toward), an expanded thesis tying it together, and five to seven decisions, including the words for their profile and their first content pillars.
- Why: the three levels above, said in two or three sentences.
- How: one question at a time with an example of the depth wanted, about 35 minutes, best in one sitting; dictation gets better stories than typing.
- The starting point. If the positioning is on file, say what you'll build on in three lines (the positioning thesis, the segment, and the anger from stage 2, which is usually the seed of the enemy) and ask "Still right?" If nothing is on file: "Do you have your Personal Monopoly document? Paste it in. If not, tell me what you do, who it's for, and the last time a client said why they picked you over someone else."

Without a document, run a catch-up of at most four questions covering value, uniqueness and segment, using the event questions in `/finding-your-personal-monopoly`, and mark the framework standalone.

## Stage 1: Authority moments

Open with: "Stage 1 of 5. Before anyone accepts your message, they need a reason to believe you can deliver, and credentials don't do that any more. Specific moments do. We're going to find two or three."

The shape you're assembling: **when <situation>, I <action> and <result>, which taught me <lesson>.** Let them tell it naturally; you assemble the parts. Start from `stories.md`: a story on file that has the shape gets checked, not retold.

Ask, one at a time:

1. "Tell me about a moment in your work you're proud of. What was the situation, what did you do, and what changed because of it?" The depth wanted, as an example: "our Q4 revenue came in 30% under target, I went through every deal in the pipeline and found we were selling to the wrong buyer, we changed the approach and hit 110% the next quarter."
2. "Now the opposite, and this one matters more. Tell me about a time something went badly wrong: a launch that flopped, a client that fired you, a bet that didn't pay off. What happened?"
3. "What do you do differently now because of it? When did you last do it?"
4. "Was there a time you had to work something out under pressure, with no playbook, and what you improvised became how you do things now? What happened?"

Two or three moments, at least one a failure. If they resist sharing a failure, say why you're asking: someone who only tells winning stories sounds like marketing, and someone who tells you what a disaster taught them sounds like someone who has done the work.

Before moving on, play back each moment's assembled shape and check it: "So when the orders tripled and the kitchen couldn't cope, you redesigned the workflow, and it taught you that scaling means rebuilding systems rather than adding people. Is that right?"

**Exit test:** two or three authority moments in full shape, at least one a failure with a lesson.

## Stage 2: The enemy

Open with: "Stage 2 of 5, and this is where the message gets its energy. Every message that spreads is fighting something, and the something is never a person. It's a practice, a belief or a system that hurts the people you serve."

Start from what's on file: the anger in the Personal Monopoly document, the `rejects` line of their POVs, the enemy on the character sheet. "Last time you said <the anger>. Let's see if that's your enemy."

Ask, one at a time:

1. "Tell me about the last time you watched someone like <their segment> do what everyone recommends and get hurt by it. What were they told to do?" The depth, as an example: "a food startup that believed it could scale like a software company, and found out it couldn't."
2. "Walk me through what it cost them: money, time, stress, chances they missed. As concrete as you can." The level wanted: "one founder burned two million on delivery logistics he didn't understand before the board pulled the plug", not "startups waste a lot of money".
3. "In that case, what stopped them from seeing it sooner, or getting out once they did?"
4. "Has it happened to someone else you've watched? Tell me about that one." A second case turns an anecdote into a pattern.

Good enemies are practices and beliefs, never people or companies. If they name a competitor or a public figure, redirect: the enemy is the belief that person spreads, because fighting a belief makes you principled and fighting a person makes you bitter. If they offer several, help them pick with the four questions in `references/messaging-frameworks.md` (most experience, hurts their segment, can prove a better way, most heat). One enemy; a message that fights three things fights nothing. Park the rest in the document.

**Exit test:** one enemy, stated as a belief or practice, with a concrete account of what it costs the segment.

## Stage 3: Personal stakes

Open with: "Stage 3 of 5. Anyone can claim an enemy. What makes people believe you is evidence that the fight costs you something. This stage is about why it's your fight and not only your marketing angle."

Start from `values.md` (a value's `cost` field is exactly this) and the thesis catalyst. Then, one at a time:

1. "When did this practice first touch you, or someone you cared about? What happened?"
2. "What did choosing this work cost you? A job you left, money you spent, a safer path you didn't take, a position you took in public that people didn't like. What happened, and when?" The depth, as an example: "I left a $120K restaurant job to stop founders repeating the mistakes I'd watched destroy good ideas." Then: "If your true version is more modest, that's fine, and we'll write the modest one."
3. "What have you started building that isn't finished yet? Why does it matter to you that it gets finished?"

Question 2 is the investment proof, and it separates a mission from a marketing angle. "I'm passionate about helping businesses grow" carries nothing; if that's all you get, say so kindly and ask for the event: when did they decide to do this, and what did the decision cost?

Not everyone has a dramatic origin story, and you never manufacture one. If the honest answer is that they found the work interesting and got good at it, then the years and the reputation they built are the stake, and the framework says so. A modest true story beats an inflated one, because an inflated story collapses the first time someone asks a follow-up.

**Exit test:** a personal reason and at least one investment or risk, both of which happened.

## Stage 4: Vision

Open with: "Stage 4 of 5, and it's short. You've told me what you're fighting. Now let's see what winning looks like."

1. "Think of the client for whom your way already worked. What's different about their week now, compared with before?"
2. From that answer, draft the vision yourself, as a condition and not a conquest, and ask them to correct it: "Together we're building <the condition>." For scale, as an example: "an industry where food innovation is backed by operational reality" describes a state of affairs; "transforming the industry" describes the author's ambition.

Keep it concrete and honestly sized. A solo consultant isn't ending an industry's dysfunction, and claiming to sounds inflated. The vision is usually the mirror of the enemy's cost: whatever the practice costs people, the vision is that cost gone.

**Exit test:** one or two sentences describing the better situation, concrete enough to picture and modest enough to believe.

## Stage 5: The expanded thesis

Open with: "Last stage before I write it up. I'll put all of it together into your expanded thesis, and your job is to tell me which version sounds like you."

Write two or three versions, different in what leads (the identity, the enemy, the vision), assembled from their words, with the lines each came from:

> "I'm the only <unique identity> who provides <specific value> to <target network> because I refuse to <key exclusions>, which allows me to <resulting advantage>. I'm fighting against <the enemy> because <personal stakes>, and together we're building <the vision>."

The first sentence is the positioning thesis from `/finding-your-personal-monopoly`; carry it over, don't rebuild it. Without one, use the catch-up material and mark the first sentence provisional. The same honesty rule holds: if "the only" isn't true, write "one of very few" or drop the frame. Edit together until they say yes without hedging.

This is not the brand tree's thesis (`canon/person/thesis.md`, the claim their body of work proves). If that thesis is confirmed, check the expanded thesis against it and name any clash, quoting both, and ask which is true (`skills/setup-brand-tree`, "Name contradictions").

**Exit test:** an expanded thesis they'd say out loud to a stranger without wincing.

## Stage 6: Write it up

Read `references/document.md` and follow it. Two halves: the framework (what's true) and the decisions (what to do with it).

- **The framework document** is for the person. Write it once, to them, in their words, every claim carrying its source. Save it to `canon/strategy/messaging-framework.md`, `status: draft`, `source: /building-your-message, <date>`; add `person_confirmed: <date>` when they say yes. Run `python3 scripts/check-prose.py --mode prose` on it and fix every fail.
- **The About section** (100 to 150 words, from the thesis, one authority moment and the enemy) is a piece other people will read. It runs through `skills/craft-sales-copy` as one piece, `pieces/<yyyy-mm-dd>-about-section/`, with the copy kind `about section` and `channel: page` (the brief's body names the profile it's for): that standard's three drafts (different in which authority moment leads), scripts and judge in a fresh context. The judge's check 12 for this kind: every claim traces to the session or the canon; the authority moment carries its four parts; the enemy is a practice or belief; it sits at the third level, not the first. The chosen draft goes in the document.
- **The first public shot at the enemy,** if it's a decision, is a post: hand it to `/post` with the enemy, the authority moment and the ground as the material. Don't draft it here.

## Where what it finds goes

The route in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes": a new finding is a `draft` entry in its canon file with `quote`, `sources` (`said in /building-your-message, <date>`) and a `log` line; a change to a confirmed entry goes to `proposals.md` (`proposed_by: /building-your-message`), naming the file and ID. A draft is confirmed in the session only on the person's yes with every required field present (`skills/setup-brand-tree/references/fields.md`). Rule 6 holds throughout.

| What the session found | Where it goes |
| --- | --- |
| Each authority moment | `canon/bank/stories.md`, an S entry: `raw` in their words, who, when, what, result, `permission` asked. The result, if it has a number, also goes to `canon/bank/proof.md` as an R entry |
| The lesson inside a moment, when it's a claim about how their field works | `canon/person/povs.md`, a P entry with the moment as its ground; the condition asked, or confidence `forming` |
| The enemy | The enemy line of the character sheet in `brand-strategy.md`, as a draft, pointing at the P ID whose `rejects` it is; if the POV doesn't exist yet, that POV goes in as a draft first. Its cost and why people can't escape it go to the segment in `canon/strategy/audience.md` (`reasoning`, `tried`) |
| What the fight cost them (the investment proof) | `canon/person/values.md`: the `cost` of the value it shows, as a draft value if none fits, built from the costly choice, never from what they say they value. The story itself to `stories.md` |
| The moment they first saw it | The `catalyst` of `canon/person/thesis.md` when the thesis exists; otherwise a story, linked in its `links` field as a catalyst candidate |
| The vision | `canon/person/thesis.md` (`changes`): a proposal (`kind: change to <ID>`) if the thesis is confirmed, a draft field if it's draft; otherwise kept in the framework document until the thesis session |
| The expanded thesis | `canon/strategy/messaging-framework.md`, the framework document itself, which is the one place it lives; `brand-strategy.md` points to that file from "Known for" rather than holding a copy. Never into `thesis.md` |
| The content pillars | `canon/person/branches.md`: a pillar that's an existing branch cites its B ID; a new one is a draft B entry with only the fields the session filled. The content plan picks the quarter's branches (`strategy-brand`) |
| Something seen across answers (three failures with one lesson, an enemy every story assumes) | `proposals.md`, kind `seen`, with the quotes and one question (rule 8) |

Update `canon/canon-index.md` and the layer table in `canon/progress.md`, and tell the person in one or two sentences what went into their files as drafts.

## When they have no idea

Run the ladder in `skills/job-personal-monopoly/references/interview-moves.md`, with this module's examples on rung 2 (they're in `references/messaging-frameworks.md`):

- **Stuck on authority moments:** the consultant fired after two weeks whose failure became the habit of starting every engagement with stakeholder interviews. Ask whether anything in their history rhymes: a failure that turned into their method.
- **Stuck on the enemy:** "A good enemy is a belief that smart people hold and that hurts your people anyway. For a restaurant consultant, it was the belief that food companies can scale like software companies. Tell me about the last time you watched that kind of belief go wrong in your world."
- **Stuck on stakes:** show the difference between "I'm passionate about operational excellence" and "I left a job because I watched three good startups die from this", and ask what choosing this work cost them. Modest is fine.

On rung 3, this module's behavioral questions: what story do you find yourself telling new clients in the first meeting; what standard practice have you talked someone out of in the last year; what did you argue about at your last job; what decision in your career would your family call irrational? On rung 4, the homework: for a missing authority moment, write down the three hardest situations of their career this week, in plain notes, and drop them in `inbox/`; for a missing enemy, for two weeks, note every time they think "why does everyone do it this way". The framework marks the gap plainly, and filling it is decision one.

## What goes wrong

- **Accepting beliefs instead of events.** "I believe in putting clients first" is not an authority moment, a stake or an enemy. Ask what happened.
- **Letting them skip the failure.** A framework built only on wins reads like a brochure.
- **A person as the enemy.** Redirect to the belief the person spreads.
- **Manufacturing an origin story.** Write the modest true version.
- **Several enemies.** Pick one and park the rest.
- **Rebuilding the positioning.** It's a settled input here.
- **Stopping at the thesis.** The decisions, the About section and the pillars are what they came for.

## Never

- Never invent a moment, a cost, a number, a client or a quote. Every fact about the person comes from the four sources in `CLAUDE.md` rule 1.
- Never confirm a canon entry without the person's yes, and never change a confirmed one; that's a proposal.
- Never present an anchor or teaching example as a real case of theirs.
- Never put the expanded thesis in place of the brand tree's thesis.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
