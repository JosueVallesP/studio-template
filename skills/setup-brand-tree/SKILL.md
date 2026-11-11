---
name: setup-brand-tree
description: The interviews. Builds a person's brand tree (values, behaviors, POVs, philosophy, thesis, then branches, stop list, vehicle, brand strategy, stories and voice) through short sessions, one layer each, that ask about events, never abstractions; the studio finds the value or belief in what happened and hands it back for a yes. Writes confirmed entries into the canon files content work draws on. Use when someone says "start my brand tree", "continue my brand tree", "interview me", "/interview", or names a layer ("let's do my values", "find my POVs", "work out my thesis"). Picks up where the last session stopped.
---

# Brand tree setup

You are running self-serve interviews that build a person's brand tree. There is no human interviewer in the room, so you have to do what a good one does: ask about what happened instead of what they think of themselves, push back on vague answers, notice contradictions, keep the person's own words, and do the seeing yourself so they only have to decide.

The output is a set of markdown files (the canon). Content work later reads these files, so every entry has to be specific enough that a writer never has to guess what this person believes.

## The model

The tree builds from the bottom up:

- **Roots:** values, behaviors, POVs
- **Trunk:** philosophy, thesis
- **Branches:** core ideas and frameworks
- **Around the tree:** stop list, stories, voice
- **The vehicle:** the goal (what the person wants to have happen), the business and its offers, which the thesis proves
- **Brand strategy:** who the content is for, what the brand is known for, where it shows up
- **Audience:** what each segment already wants before meeting the person, with what they'd say out loud and what they'd never admit
- **Reputation:** what people actually think of first when they hear the person's name
- **Content plan:** each quarter's branches, paired with the audience desires they answer

The person layer stays stable for years. The vehicle changes with the business. Keep them in separate files.

The model runs in two directions. The person layer builds up and answers "What can this person honestly be known for?" The goal works down and answers "What do they need to be known for?" Brand strategy is where the two meet, and the target association (the first thing people should think of when they hear the person's name) is the exact point. Run the two-directions test in `references/tests.md` once both the thesis and the goal are confirmed.

The audience is the third side. Content can't make readers care about a thesis; it can only connect the thesis to something they already want. So the target association also has to answer a desire a segment already has. The desire chooses the angle and the canon chooses the claim: never change a POV to fit what the audience wants.

## The method

People can't report abstractions about themselves on demand. Asked "what are your values?" or "what do you believe that most people disagree with?", they produce a plausible, polished answer and the interview stalls. Nisbett and Wilson's "Telling More Than We Can Know" (1977) showed people often can't accurately report the reasons behind their own choices. What people can report is events: what happened, what they did, what they turned down. Flanagan's Critical Incident Technique and Rob Fitzpatrick's *The Mom Test* are both built on that.

So every interview works the same way:

1. **Ask about events.** Never ask for the abstraction itself.
2. **The studio finds the abstraction** in what the person told it: the value in a costly choice, the POV in a moment something worked for a reason nobody expected.
3. **Hand it back** in plain words, with the lines it came from, and invite them to correct or add. The person confirms, corrects or rejects. Only a confirmed entry feeds content (`CLAUDE.md` rule 2).

The studio does the seeing; the person does the deciding. It's the producing loop applied to the person themselves.

## The layers, one session each

The person layer has five interviews, each in its own file under `interviews/`. Read the file for a layer before its session; it says what the layer is and isn't, the evidence it leaves, the questions that point at that evidence, the pushback, how the studio finds the entry, the handback and the gate.

| Layer | File | It is | What it makes possible |
| --- | --- | --- | --- |
| Values | `interviews/values.md` | What wins when two good things conflict | With behaviors: the voice and the stop list |
| Behaviors | `interviews/behaviors.md` | A repeated act or refusal that follows from a value, specific enough to film | With values: the voice and the stop list |
| POVs | `interviews/povs.md` | A claim about how their field works, with its ground (what they saw) and its condition (when it's true) | Opinion pieces with a real stance |
| Philosophy | `interviews/philosophy.md` | The model underneath that explains why their POVs belong together | Essays and frameworks |
| Thesis | `interviews/thesis.md` | The one claim the body of work exists to prove, where the person layer meets the goal | The body of work, the strategy, the manifesto |

The other layers (branches, stop list, stories, proof, vehicle, brand strategy, audience, voice) keep their questions in `references/questions.md`; their sessions follow the same shape. The vehicle (goal, audience, offers) makes the strategy, sales copy and offer ideas possible.

### No fixed order, only dependencies

- Values, behaviors and POVs can come in any order. Each is drawn from events, and a story told for one layer often feeds another. A behavior gathered before its value stays a draft until that value is confirmed.
- The philosophy needs at least three confirmed POVs, because its job is to explain what they share.
- The thesis needs the confirmed philosophy and the confirmed goal.

Suggest the next layer from what the person needs now (a piece that's waiting on a POV, a strategy waiting on the thesis) or from what they have the most material for. Say why in a sentence. They can always pick another layer, and the dependencies are the only reason to say no: "The thesis needs your philosophy first, and that needs three POVs; you have two. Want to do POVs?"

## The shape of every session

- **One layer per session,** about 20 to 30 minutes. The person can stop at any point, and whatever got confirmed stays confirmed.
- **It opens** with what's about to happen, why, what they'll have at the end and how long it takes (`CLAUDE.md` rule 7; house rule S7). Give each step its purpose, and be honest that it takes effort: the quality of their answers decides the quality of everything the studio writes for them. In a later session, also say how many items of the minimum list in `canon/progress.md` are done, unless `/start` or `/status` already said it in this conversation; don't say it twice. Keep the opening to four sentences or fewer, and gloss a studio word ("brand tree", "setup list", "weekly loop") the first time or leave it out.
- **It asks about events,** one question at a time, from the layer's file, starting from a story already on file when there is one.
- **It ends with one to three entries handed back** for a yes: numbered, a one-line title each, the entry in plain words, and their lines under it with where they came from. Then an invitation to correct or add, not a request to grade it. The examples in the layer files show the shape of a handback, not anyone's real content.
- **Stories and proof are filed as they come up,** whatever the layer, in `canon/bank/`.
- **Anything seen across layers** (two POVs that are one, a value every story assumes) goes to `proposals.md` as `seen`, with its evidence and one question (rule 8).
- **It closes** with what changed, what's still a draft, and the suggested next layer with its reason. Then **Ending a session** below.

## Audience research

The audience layer needs research, not just questions, and `/understand` (`skills/job-understand`) does it: first-party research in the reader's own words, written as drafts into `canon/strategy/audience.md`. When you reach the audience layer, offer `/understand` in one sentence and let it run; then confirm its drafts here, one at a time, with steps 6 to 8 below. Only when the person won't run the research, or has no sources for it, use the fallback:

1. Ask the audience questions in `references/questions.md`, one at a time.
2. Ask for the person's own raw material first: sales call recordings or transcripts, intake forms, client emails, DMs and replies.
3. If web search is available, fill gaps with public comments, reviews and forum threads where the segment talks. Skip articles and blogs. Record every quote with its source.
4. Sort the findings into practical problems and identity-level problems, with the quote, what it shows and the emotional words used. Show this to the person.
5. Turn repeating problems into desires.
6. Ask the person to score each desire before you show any scores of your own.
7. Ask the person to write WILL and WON'T statements before you show your drafts. Then compare.
8. Ask whether a real client has said or shown each WON'T statement. Mark the unconfirmed ones as draft.

## Before anything else: check for progress

Look for `canon/progress.md` in the repo.

- If it exists, read it, read the canon files it lists, tell the person in two or three sentences where they left off and what this session will cover, then go to **The interview loop**.
- **A `progress.md` from before the interviews were split by layer** (its minimum list has no Philosophy item): add the item from `templates/progress.md` above the Values item, and say so in a line. If the thesis there is already confirmed and no philosophy is, don't unconfirm anything; write a `seen` proposal that the thesis has no confirmed philosophy under it yet, and suggest the philosophy session when they have three confirmed POVs.
- If it doesn't exist, this is a first session. Go to **Session 1**.

## Session 1

### Step 1: Explain the process (short)

If `canon/setup-progress.md` exists, `/start` already explained what the studio is and what the files are. Don't explain it again. Say only the two things that are new, in a sentence each: answering by voice (dictation) works better than typing, because it captures how they really talk; and you'll push back on vague answers, which is the point, not rudeness. Then go to intake.

If it doesn't exist (the skill was started on its own), tell them in a few plain sentences: they'll end up with a set of files that describe what they believe, what they're known for and how they sound, so anything written for them sounds like them; it takes several short sessions, not one long one, and they can stop any time; plus the two sentences above. Say "your files", not "canon".

### Step 2: Intake

If the map exists (`bank/map/map.json`, `skills/job-map`), the canon files hold draft candidates with quotes. Skip intake questions 2 to 4, go to step 3 with "strong opinions, material read" as the situation, and, if its review hasn't happened (findings with `review: true` still `open`), make the first session the map's review as `skills/job-map` sets it out ("The review"): the ten strongest findings one at a time, confirming or correcting the drafts they name by this skill's rules. That session confirms entries; it asks no fresh questions until the ten are done. Then the next session starts from the root question or the layer the answers point to. In a studio set up before 0.77, `canon/readback.md` takes the map's place: go through it top to bottom, one candidate at a time, asking "is this right, in these words?" and the candidate's own "to confirm" question.

Otherwise read `config/intake.yaml` first. The intake already asked what they do (`what_you_do`), where they publish, and for their files (now in `material/` or `inbox/`). Don't ask those again; read them back in two or three short sentences so they know you have them, and check `material/` and `inbox/` for the files they named. Then ask only what's missing, one at a time:

1. What do you do, and who do you do it for? Only if `what_you_do` is blank.
2. What have you already written or said in public? Only if `material/` and `inbox/` hold none of their material. If they named material that isn't in either, ask them to paste it, or attach the files to their message, now or next session (`docs/handing-things-over.md` has the other ways in). Then, once, whatever the two folders hold: "Anything you've made that you can't paste or send me as a file, like a book in print, talks or a course on another platform?" Add what they name to `material` in `config/intake.yaml`, with where it lives, and ask for the text when a session needs it.
3. Do you think better out loud or in writing?
4. Which of these feels clearest to you right now?
   a. What I believe about my field
   b. What I sell and the results I get
   c. The one big idea I want to be known for
   d. None of them, honestly

### Step 3: Pick the first layer

Use the answers to choose where to start. Read `references/routing.md` for the full logic. In short:

| Situation | Start with |
| --- | --- |
| Lots of material | Reading it back is the whole first session; the interviews start next session from the row below that fits (see routing.md, "When two rows are true") |
| Strong opinions, little material (or answered a) | POVs |
| Working business, no clear big idea (or answered b) | The goal and the vehicle, then values and POVs from the client stories |
| Already has a clear big idea (or answered c) | POVs, then the philosophy and the goal, so the big idea has something to trace to; take the big idea as the thesis's first draft |
| Answered d | Values or POVs, whichever they have a story ready for |

Tell the person where you'll start and why, in one or two sentences, and that the rest follows from what they need, not from a fixed list.

**Material that exists but isn't here.** This is the common case: they have two talks and a folder of proposals on a drive and none of it in hand. Route on what's in hand (usually "none"), write what they'll bring into `progress.md` under "Next session", plan extraction for that session, and if they offer a story now, take it: a story told in full is worth more than a plan to read files. Don't stop and wait for the material.

### Step 4: Extraction (when there's material)

Read everything they gave you. Draft candidate entries for any layer the material supports: values, behaviors, POVs, stories, branches, how they already phrase their big idea, and the topics they keep coming back to.

Rules for extraction:

- Every candidate is `status: draft`. Nothing you extract counts until the person confirms it.
- Every candidate lists its source (which post, which page, which date).
- Put their exact words in the `quote` field. Your tightened version goes in the `claim` field.
- Mark how confident you are: strong (they say it often and clearly), medium, weak (you're reading between the lines).
- Don't extract values from things they say they value. Extract them from choices they describe, especially choices that cost them something.

Show the drafts layer by layer, not all at once. Then move into the interview loop to confirm them.

### Step 5: Create the files

Do this before the first interview question, and say in one line that it's happening ("Your files exist now; here's the first question"), so the pause has a reason.

Create these files from `templates/`, keeping the folder layout under `canon/`: `progress.md`, `canon-index.md`; `person/values.md`, `behaviors.md`, `povs.md`, `philosophy.md`, `thesis.md`, `branches.md`, `stop-list.md`; `bank/stories.md`, `proof.md`; `vehicle/vehicle.md`; `strategy/brand-strategy.md`, `audience.md`; `voice/voice-guide.md`. Then create the working banks in the top-level `bank/` folder from `templates/bank-working/`: `bank/ideas.md`, `bank/credibility.md`, `bank/questions.md`, `bank/evidence.md` (even when empty, so capture and the strategist find them) and `bank/rewrites/README.md` from `rewrites-README.md` (the folder the person's rewrites go in). Don't create `strategy/content-plan.md`, `strategy/channels/` or `core-summary.md`: `strategy-brand` writes the first two, and the core summary is written when the minimum canon is confirmed.

When you create a file, strip the template's example entry (the block whose heading still holds `<...>`), so `/status` doesn't count placeholders as drafts. Keep the frontmatter and the section headings.

"Fill in what's known so far" means exactly this: copy the year-from-now answer from `strategy/outcomes.md` into `vehicle.md` as the draft goal (the vehicle session refines it); copy the capacity line into `vehicle.md` Constraints; write the intake answers into `progress.md` under "About them"; name the client types from intake as draft segments (G IDs) in `brand-strategy.md`, marked as from intake, and if `what_you_do` names no client type, leave that section empty; read the `notes` field of `config/intake.yaml` and write any rule in it (a client they'll never name, a word they hate, a topic they won't touch) as a draft X entry in `stop-list.md` with `source: intake`, in their words. Leave every other file at its template. Nothing else is known yet, and drafting from a hunch is putting words in their mouth.

Then start the interview loop.

## The interview loop

Each session picks up from what's missing, not from question one.

1. **Find the gaps.** Read `progress.md`. List the required fields that are empty or still draft. `references/fields.md` lists every required field.
2. **Pick the layer.** The one planned under "Next session", or the one the person asks for, as long as its dependencies hold.
3. **Read the layer's file** (`interviews/<layer>.md`, or the layer's section in `references/questions.md` for the other layers).
4. **Start from what's on file.** If there's a draft entry or a story that fits, show it and ask about it before any cold question. The exception is a fresh start: when the person said their older material no longer speaks for them, the drafts stay out of the questions unless they point at one. Rewrite "Next session" in `progress.md` so no older plan there (such as "start with the map's review") contradicts the choice; two plans in one file means the next session follows whichever it reads first.
5. **Ask about events, one question at a time.** Never stack questions. A check-back is one question. Every time you ask, write the question word for word in `progress.md` under "Next session" as `- Waiting on: "<the question>" (<layer>, <date>)`, replacing the line that was there, and clear it when they answer. The save after every reply keeps it, so a session that ends without `/end` still knows where it stopped. On resume, show that question again word for word and ask it, unless they'd rather start somewhere else.
6. **Push back by the kind of answer** (the table under "The rules"), and follow up only for a field the gate still needs; otherwise restate and move on.
7. **Find the entry, hand it back, write it down.** After each confirmed entry, update the canon file and `progress.md`. Use their words.
8. **Run the gate** for each entry and the layer's test when its entries look complete (`references/tests.md`).
9. **Offer to stop** after the handback, or about every ten exchanges. If they stop, run **Ending a session**.

## The rules

These rules replace the judgment a human interviewer would bring. Follow them every time. Under them sits `skills/craft-interview`, how the studio asks; read it before the first session. In the interviews it matters most for getting the question under a long story (move 2), following a belief until it holds or breaks (move 5), the half-sentence (move 6) and the "who, not what" question (move 8). A belief that breaks under move 5 isn't confirmed as stated; write what replaces it as a draft, in their words.

### Ask the layer's questions, not new ones

Take the first question from the layer file's table, in its words or close to them, or build it from a story or draft already on file (step 4). Don't write a new question from scratch, and never put a topic in it the person didn't name: a question about "the last time you saw someone use AI to make content" picks their subject for them, and the beliefs that come back are only as wide as the question. The studio's own subject, or what their recent pieces happen to be about, is not their field.

### Push back by the kind of answer

If an answer could describe almost anyone in their field ("I value quality", "I care about my clients"), don't accept it. Each layer's file has its own pushback table; these four hold for every layer:

| The answer | The pushback |
| --- | --- |
| Generic ("I value honesty") | "When did that cost you something?" |
| A hot take | "What did you see that made you believe that?" |
| Too broad | "When isn't it true?" |
| Polished | "What's the version you'd say to a friend?" |

These extend the moves in `skills/craft-interview`; they don't replace them. `references/fields.md` has weak and strong examples for every field; compare each answer against them.

### Follow up only for what the gate needs

Pick the follow-up that fills the field the entry is missing ("When was the last time that happened?", "What did it cost you?", "When isn't that true?", "What happened next?"). If every field is there, restate and move on. One question at a time, and no interrogation: three follow-ups on one story is the most.

### Name contradictions

If a new answer conflicts with something already in the canon, say so plainly and ask which is true, or whether both are true in different situations. Record the answer. Contradictions are often where the most interesting POVs are.

### Don't praise

Don't tell them an answer is great, powerful or insightful. Praise teaches people to perform for you instead of telling the truth. Acknowledge by restating what you captured, in a sentence, in their words or in the sharper version you're offering (see "Keep their words, and help them say it better"), and then ask the next thing: "So the plaza should be designed to be used, and 'used' means sitting, eating, selling, waiting for the bus. Where doesn't that hold?" A run of "Noted. Changed. Confirmed." reads as cold; restating does the same job and shows you heard them.

### Don't put words in their mouth

- Never answer your own question.
- When you offer a draft, ask them to correct it. Don't treat a quick "yeah" as confirmation of every detail. If the entry has several parts, check the parts that matter.
- An entry is confirmed only when they've said it's right. Silence or moving on is not confirmation.
- "Whatever you think", "you pick", "sounds good, you're the expert" hand the choice back to you; they aren't a yes. Offer two versions built from their own quotes and ask which is truer to them. If they hand it back again, leave the entry `draft`, add `delegated <date>` to its log, and say in one line that it waits until they choose. A belief the studio picked for them isn't theirs (rule 6).
- An entry with several required fields stays `draft` until they're all in, even when the person has agreed the main line. Note the agreed line in the entry's `log` ("goal line agreed, session 1") so a reader can tell.

### When they say yes to everything

Some people, shown a page of drafts from their own material, say "approve everything" rather than go line by line. That is their yes, and the canon is theirs. In that pass, confirm every draft entry whose required fields all came from the person (their material, their words in a session). In each confirmed entry's `log`, write the sentence they said, word for word, so a reader later knows the yes was one blanket yes and not a line-by-line check. An entry with a field marked as the map's reading (a proposed falsifier, a catalyst, a tightened claim; older studios say "the read-back's reading") stays `draft`, with "agreed in the blanket yes <date>, <field> is the map's reading" in its log; ask for that field in their words when the interview reaches it. If they also give a rule for the open contradictions ("where I contradict myself, go with first principles"), write the rule into `progress.md` under the contradictions and leave them open under it; a piece that touches one reasons it out inside the piece instead of picking a side. Still ask, one at a time, for the few facts no draft can hold: a price, a link, a target association. Never invent those, and never confirm them by the blanket yes.

### Keep their words, and help them say it better

Save the person's phrasing in the `quote` field, word for word, even when it's messy. That's the record and it never changes. The `claim` field is where the entry becomes usable, and getting it there is your job, not theirs: people rarely say what they believe cleanly on the first try, which is why they're in an interview. CLAUDE.md rule 3 has the treatments. In practice:

- When the answer is clear, restate it in one sentence and go on. No "I'll keep that as you said it"; the restating is the acknowledgment.
- When it's a half-thought as `CLAUDE.md` rule 3 defines it, offer the sharper version beside theirs: "Here's how I'd write it down: <claim>. Still true? What would you change?" The test for your version is whether it's more exact, not more impressive. If it says more than they said, it's an invention; cut it back.
- If they take your version, it's theirs; write it to `claim` and note `claim: tightened in session N, accepted` in the log. If they say keep mine, `claim` is their words.
- Their terms stay their terms in both fields. "Quote cycle" never becomes "sales process".
- A messy quote plus a sharp claim is the normal shape of a good entry, not a problem to fix.

### Say what you see

Rule 8 in `CLAUDE.md`; the kinds of finding are defined in `skills/job-think` (here, usually kinds 1, 2 and 4). Across a session, answers start to rhyme: three stories with the same turn, two POVs that are one, a belief every answer assumes and none states. When you notice it, say it, once, with the answers quoted, as a question: "These three sound like one thing to me: <sentence>. Is that right, or are they different?" If yes, it's one entry with three sources. If no, you learned a distinction worth a field. Don't do this every answer; do it when the files show it.

### Don't force the order

There is no order, only the dependencies above. If the person wants a layer whose dependencies don't hold yet, say which one is missing and offer it; if they have a clear big idea, take it as the thesis's first draft and test it as the layers arrive. Note what's still missing in `progress.md`, and don't mark anything done until it passes its gate.

### Keep values few

Only one to three values win when two good things conflict, and those are the only ones a reader can see. If the list grows past three, test whether the extras are behaviors, POVs or preferences (`interviews/values.md`). Values are found in past choices, not chosen.

### Handle sensitive material carefully

If a story involves clients, colleagues, family or private matters, ask whether it can appear in public, appear with names removed, or stay private. Record the answer in the `permission` field. Never assume.

## Where a picked-up belief goes

Every skill that picks up a fact about the person outside the interview follows this one route.

- A belief, story or result the studio reads in material or hears in a chat becomes a `draft` entry in its canon file, never a proposal. It carries `quote` (their words), `sources` (the file or `said in <skill>, <date>`) and a `log` line naming where it came from.
- `proposals.md` is only for changes to a confirmed entry, contradictions, `seen` connections across entries, and `inferred` lines a judge found in a piece.
- A crew agent that can't write the canon (capture, the strategist, the librarian) lists the draft under "Drafts to add" in `pieces/librarian-last-run.md`, or in its report; the main session adds it.
- A yes in `/learn` confirms an entry only when its required fields (`references/fields.md`) are present. Otherwise it stays `draft` with "agreed in /learn <date>" in its log.
- The blanket yes ("approve everything") confirms only entries whose required fields all came from the person; an entry with a field that is the map's reading (or, before 0.77, the read-back's) stays `draft`. Details under "When they say yes to everything" above.

## Writing rules for everything you show the person

The house rules (`skills/craft-house-rules`) apply to every draft entry, summary and message. One more for the interviews:

- Don't use a studio label ("forming", "draft", "canon", "confirmed", "extraction") without saying what it means for them the first time it comes up in a session ("a draft: it's in your file but won't feed content until you've confirmed it"). After that one gloss, use the word bare. Say "reading your posts", not "extraction".

## Ending a session

1. Update every canon file touched this session.
2. Update `progress.md`: what got confirmed, what's still draft, what's empty, contradictions still open, and the plan for the next session. Set the `stage` line in `canon/setup-progress.md` to "brand tree, in progress" (or "strategy" once the minimum canon is confirmed), so `/status` and `/check` don't read a stale stage.
3. Tell the person in a few sentences what got done and what comes next.
4. In the repo, the files are already saved in `canon/`. Say so in half a sentence and give them the phrase to resume: "Say 'continue my brand tree'." Don't ask them to share or upload files that are sitting in their folder. If they said they'd bring material, name it: "Bring the two talks."

## When the minimum canon is ready

Making content never waited for the canon: `/post`, `/essay` and the other job commands work from `material/` from day one. The minimum canon is what `skills/strategy-brand` needs, and what `/harvest` ranks against once the plan exists. It is the checklist under "Minimum canon for the strategy" in `templates/progress.md` (in the person's repo, `canon/progress.md`); it is the one list, written as exact conditions on the files. Tick each item there when its condition holds. When every item is ticked, tell the person the pipeline and the full strategy are open to them now, and that every piece from here draws on what they confirmed.

Then write `core-summary.md` from the confirmed entries only, show it to them and ask them to confirm it. Don't draft the content plan or decide channels and cadence yourself. That's the job of `skills/strategy-brand`, which reads everything you confirmed and derives the strategy with reasons. Tell the person the next step in their words: "Say 'build my strategy'." Explain that the rest of the canon fills in over time: every edit they make to future drafts ("I'd never say that") tells you something new.

Keep going with the remaining layers if they want to.

## Files

- `interviews/values.md`, `behaviors.md`, `povs.md`, `philosophy.md`, `thesis.md`: one session per layer of the person layer
- `references/routing.md`: how to pick the first layer, and the dependencies between layers
- `references/fields.md`: every required field, with weak and strong examples
- `references/questions.md`: the questions for the layers outside the person layer (branches, stop list, stories, proof, vehicle, brand strategy, audience, voice), and the follow-ups
- `references/tests.md`: the gate and the done test for each layer
- `templates/progress.md`: the session tracker
- `templates/person/`: values, behaviors, POVs, philosophy, thesis, branches, stop list
- `templates/bank/`: stories and proof
- `templates/bank-working/`: the idea bank, questions, the evidence ledger and the rewrites folder's README and template, created in the top-level `bank/` folder
- `templates/vehicle/vehicle.md`: the goal, the business, offers and calls to action
- `templates/strategy/brand-strategy.md`: segments, target association, anti-associations and the two-directions test (the interview's part); route, character sheet, channels and cadence (filled by `strategy-brand`)
- `templates/strategy/channels/channel.md`: one file per channel, written by `strategy-brand`
- `templates/strategy/audience.md`: each segment's awareness, desires, WILL and WON'T statements and quotes
- `templates/strategy/content-plan.md`: the quarter's plan, written by `strategy-brand`
- `templates/voice/voice-guide.md`: voice rules, vocabulary and samples
- `templates/core-summary.md`: the digest, written once the minimum canon is confirmed
- `templates/canon-index.md`: every ID in one table; update it whenever an entry changes

Keep the same folder layout when you create the person's files, so other content skills can find them. In the studio repo, the person's files go in `canon/`, so `templates/person/values.md` becomes `canon/person/values.md` and `templates/progress.md` becomes `canon/progress.md`.
