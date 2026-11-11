---
name: craft-copylosophy
description: Tests an idea, a brief or a draft for false premises, rebuilds the argument, finds the reasoned contrarian thesis and refines it until every premise holds. In the studio the writer runs its writer pass before drafting and the editor or judge runs its judge pass on the finished draft, where a false premise is a redo. Use when a piece argues something, when someone says "test this argument", "does this hold", or "copylosophy".
---

# Copylosophy

Method by Josué Valles, the studio's author.

## In the studio

The method is kept whole here; three things change when it runs inside the studio:

- **The belief comes from the person's files.** Entry point 2 (starting from scratch) is replaced by them: on the pipeline, the person's positions are their confirmed POVs (`canon/person/povs.md`), their thesis and branches. Never invent a position for them.
- **Each caller runs one pass**, defined in the table below; no other file defines them. Output never goes in the brief; the brief is the producer's.
- **Writing rules.** The house rules (`skills/craft-house-rules`) apply; `craft-human` holds the human-writing standard. The person's voice guide (`canon/voice/voice-guide.md`) sits on top of both.

| Caller | Steps | Output goes |
| --- | --- | --- |
| Writer pass (`role-writer`, `job-post`, `job-essay`, the format draft stages), before drafting | 1 to 3, 5, 6 and 10 (the refined thesis), plus the belief gate (step 9) run against the files: on the pipeline, the thesis traces to a confirmed POV, thesis or branch; on a direct piece, to a quoted line in `material/`, `inbox/` or `said today`. When nobody is present, no question is asked and the gap goes under `## Brief defects`. When the person is present and confirms a new thesis, it goes to a `draft` POV entry in `canon/person/povs.md` (`proposals.md` only when it changes a confirmed entry) | The draft's `## Argument check` |
| Judge pass (`role-editor`, the `judge` agent, the format judge stages), on the finished draft | 1 to 3, 5 and 6: a verdict per premise. A `false` verdict is a redo, graded in `skills/role-editor`'s gates table. Then the chain check below | The review |
| Either pass, for a piece that tells a story or shows a result and doesn't argue | The short version: the claim, the hidden premises, and the logic and epistemology lenses only | As above |

Facts about the person never live in this file. It names the canon file to read.

### The chain check (judge pass)

Premise verdicts test each claim alone. A piece can pass all of them and still not follow from one step to the next, because every line was written to fill a slot and nobody read the whole argument as one argument. The chain check reads it that way. The judge runs it on the finished draft, in the fresh context, after the premise verdicts.

1. **Write the chain.** The piece as numbered steps, from the first claim to the conclusion and then the close, one step per move in the argument, each with the draft's line quoted. A story or an example is a step too: write what it is offered as proof of.
2. **Name the one idea** in one sentence. If it takes "and" to say it, the piece carries more than one idea.
3. **Check every link.** Each of these is a fail, named with the two steps it sits between:
   - **Shifted test or term.** A criterion or a key word means one thing in one step and something else in another (a split by "would two people agree" that becomes a split by "can I write a rule for it").
   - **A group nobody defined.** A category, list item or option appears that no earlier step set up (a two-way split that turns into three, with "the middle" never said).
   - **Example next to the claim, not under it.** Read alone, the evidence shows a different claim from the one it's used for, and a line like "it works the same way" carries the gap.
   - **Taken back.** A concession that weakens the claim instead of stating the condition under which it holds ("I'm not saying X can't..." right after saying X can't).
   - **The close breaks the body.** The ending, the instruction or the test given to the reader contradicts a step, or drops one the body made (a three-way split, then "if it's not the first kind, take it back").
   - **Two ideas.** Step 2 needed an "and", and the piece doesn't have room to carry both fully.
4. **Write the chain into the review** under its own heading, the fails marked on the steps where they sit, so the writer and the person can see where it breaks.

Each fail is graded by the format's judge stage (its "the chain holds" check). The chain check never rewrites; it shows where the argument breaks.

## Run on its own (`/copylosophy`)

The whole method: all three entry points, every step of the engine, the full output format.

- **What they hand over decides the entry point:** their own idea or draft (pasted, or a piece in `pieces/`) is entry 1; nothing yet is entry 2; someone else's post, article or ad is entry 3.
- **Entry 2 starts from the files.** Read the confirmed POVs, the thesis and branches (`canon/person/`), `material/` and `bank/ideas.md` first, and look for the corrections the person keeps making. Bring those back as candidates with their words quoted. Ask the three questions only when the files are thin, and anchor each in an event ("When did you last correct a client on this? What did they believe?"), because a real moment gives a truer answer than a general one (`skills/craft-interview`).
- **Every lens runs,** ethics and aesthetics included. Research (step 4) names every source; a case the copy will use is marked `borrowed: verify`.
- **Saved to** `pieces/<id>/argument-check.md` when it ran on a piece; otherwise to `pieces/<yyyy-mm-dd>-<slug>/argument-check.md`, a folder that holds only that file until a piece is made from it. The output format below, as written.
- **The belief gate is the only road to the canon.** A refined thesis the person says yes to becomes a `draft` POV entry in `canon/person/povs.md`, with their words in `quote`, the source (`said in copylosophy, <date>`, or the file), the ground and the condition the engine found, and a `log` line, as `skills/setup-brand-tree/SKILL.md` ("Where a picked-up belief goes") says. When it refines a confirmed POV, it goes to `proposals.md` as `kind: change to P<n>` instead, and the confirmed entry is never edited directly (rule 6). The person confirms a draft entry in an interview or in `/learn`; this skill never marks one confirmed.
- **Copy.** Edits to their own draft are suggestions, each with its reason, and their wording stays everywhere else (rule 3). A new piece isn't written here: hand the refined thesis to `/post` or `/essay`, which write three drafts and send them to a judge in a fresh context (rule 4). Step 11's order is what the writer reads there.


## What it does

Copylosophy helps people write copy and content that is logically sound, makes sense, and says something true the reader hasn't heard a hundred times. When a piece goes against common advice, it does so because the common advice rests on a premise that fails, and the copy shows which one.

It does three things:

1. **Tests ideas.** It finds the argument underneath a piece of content, checks every premise, and refines the thesis until it holds.
2. **Finds reasoned contrarian positions.** It looks for where the person's experience contradicts common advice, and turns that gap into a thesis.
3. **Writes the copy.** It turns the refined thesis into a piece that carries the argument without showing the scaffolding.

It shows its thinking so the user learns to do this on their own.

## Principles

- **Sound first, contrarian second.** A true idea that agrees with common advice beats a clever idea that doesn't hold. Contrarian is never the goal on its own.
- **The belief comes from the person.** Never invent a position for the user to defend. Find positions in their experience, their work and their material, and use research to test those positions.
- **Say when something holds.** If an argument is sound, say so. Never invent problems to look thorough.
- **Argue against the strongest version.** Before disagreeing with anything, state it the way its smartest defender would.
- **Teach as you go.** Name each pattern you find and give the user a question they can use to catch it themselves.
- **Keep the user's words.** When the user supplies copy, suggest edits and explain them. Don't rewrite their lines.

## Before writing anything

The house rules (`skills/craft-house-rules`) govern every piece of copy this skill produces and the analysis itself, with the person's voice guide on top. Copy that argues needs a few more, which this method has always carried:

- Each sentence follows from the one before. Use transitions that show the logic (so, because, if, which, but, that means), and skip the ones that only add drama.
- Define a term the moment it appears, and keep each key word to one meaning from the first line to the last.
- Words like always, never, everyone, best and biggest each make a claim. Support it, narrow it, or cut it.
- Name the stake. If the writer benefits from the reader believing this, say so plainly.
- Pair a result or a credential with what it doesn't prove.
- Check every fact the argument uses. If you can't, leave it out.
- Name the real advice or a real source instead of saying what "everyone tells you".
- End when the argument is complete: the principle and the conditions for using it, with no summary or slogan after.

For the samples to read, follow the voice order in `skills/craft-house-rules` ("The voice order"); outside a studio with no files to read, ask for a few pieces of their writing. If they have none, use the writing rules alone.

## Entry points

The user can start in three ways. All three run through the same engine and can end in copy. If it isn't clear which one the user wants, ask.

### 1. Their own idea or draft

The user pastes an idea, a thesis or a draft.

1. Run the engine on it.
2. Show the full analysis.
3. Give the refined thesis and the specific edits you'd make, keeping their wording everywhere else.
4. Check whether the refined thesis contradicts a common belief. If it does, point that out and offer to build the piece around it.
5. Offer to write or rewrite the copy.

### 2. Starting from scratch

The user has no idea yet. Find one in their experience, never in a list of industry opinions. Asking someone to argue against common advice they never questioned produces a position they don't hold.

Ask one question at a time and wait for each answer. Start with whichever of these fits the user best:

1. What do you find yourself correcting, over and over, with clients or people in your field?
2. Think of a time you did something one way and later changed how you do it. What happened that made you change?
3. Tell me about the last job where you didn't do it the way people in your field usually would. What did you do instead, and what happened?

Question 1 is usually the richest. If someone corrects the same belief every week, they already hold a reasoned contrarian position.

The user can also paste raw material instead of answering: call transcripts, notes, voice memos, old posts. Read through it for claims that disagree with common advice, list them, and ask which ones they stand behind.

Once a candidate idea surfaces, ask the follow-ups that test it, one at a time:

4. Who is this for, and what are they trying to get?
5. What would a smart person who disagrees with you say?
6. When is your view not true?

Questions 5 and 6 do most of the work. Their answers usually show where the thesis needs a condition or a narrower scope.

Then state the thesis back in one sentence, confirm it with the user, and run the engine.

### 3. Someone else's content

The user pastes a post, article, ad or other piece.

1. Work out what the author meant, using context: who they are, who they write for, what prompted the piece. Separate what they meant from what they said.
2. Steelman it. State its strongest version.
3. Run the engine.
4. If a premise fails, ask the user whether the correction matches what they've seen in their own work. Only build a response if it does.
5. Offer to write the response as the user's own piece, built on the correction. The response argues with the idea, never the person.

## The engine

Run every step. Show the results in the output format below.

### Step 1: Find the claim

Reduce the piece to the one sentence it argues. Many pieces argue something they never state outright.

### Step 2: Separate the justification from the instruction

Many pieces give a reason, then tell the reader to do something. Write both down. Check whether the instruction actually follows from the reason, and whether a key word means the same thing in both. This step exposes most bad advice.

Example: "Everyone needs a personal brand" justifies itself with one meaning of brand (your reputation, which everyone already has) and instructs with another (the practice of posting and publishing, which not everyone needs).

### Step 3: Rebuild the argument

List the premises that lead to the conclusion, stated and hidden. Mark the hidden ones. False premises usually hide in what the writer assumed but never said.

### Step 4: Research

Use research for two jobs:

- **Steelman the common view.** Find what the common advice actually says and who says it, from real sources. This lets the copy name the real advice instead of describing what "most people" think.
- **Test the claim.** Check the facts, and look for evidence that would break the thesis before a reader finds it.

Also check incentives: who spreads this advice, and do they benefit from it? An incentive doesn't make a claim false, but it's a reason to test it harder. If the user benefits from their own claim, the copy should say so.

For a short test of a single idea where the logic alone settles it, you can skip research. Say that you skipped it.

### Step 5: Test each premise through the lenses

Every lens runs every time. In the writer and judge passes (the table above), ethics and aesthetics are optional, since no gate rests on them; on a standalone run they run like the rest. Each one asks one question. See the lens reference below.

### Step 6: Give a verdict on each premise

Use four verdicts: **sound**, **weak** (partly true, or true only under conditions), **false**, or **hidden** (unstated, then judged as one of the other three).

### Step 7: Find the contrarian thesis

Where a premise fails, the correction is a candidate thesis. Each kind of failure produces a different kind of contrarian idea:

| Failure | What it looks like |
|---|---|
| Wrong premise | The common view rests on something untrue, or on evidence that only counts the winners. |
| Wrong goal | The common view chases a stand-in for what the reader actually wants. |
| Wrong category | The common view treats something as a kind of thing it isn't. |
| Wrong cause | Two things show up together, and the common view assumes one causes the other. |
| Wrong scope | Something true for one group gets sold as true for everyone. |
| Wrong reading | A famous idea gets repeated against its original meaning. |
| Shifting word | A key word means one thing in the reason and another in the instruction. |

Write two to four candidate theses. Include the obvious overcorrection and the obvious counter-cliché, so the user can see why they fail.

If no premise fails, say so. The piece holds, and it doesn't need a contrarian angle to be worth writing.

### Step 8: Run the provocation tests

A candidate thesis must pass all five:

1. **Can you name the premise that fails?** If you can only say the common view is wrong, without showing where it breaks, it's provocation.
2. **Did you argue against the strongest version?**
3. **Does it admit where the common view is right?** A reasoned position has conditions.
4. **Does it survive its own run through the engine?** Contrarian theses hide bad premises too.
5. **Would it be worth saying if nobody reacted?**

Then check for counter-clichés. Some ideas sound contrarian but are just the other well-worn side of the same debate ("you already have a personal brand," "your work speaks for itself"). Reject them unless the engine shows they hold and add something.

### Step 9: The belief gate

Ask the user: "Do you believe this? Would you say it to a client without being asked?" If not, drop it, however good it sounds.

### Step 10: Refine the thesis

Rewrite the surviving thesis so every premise holds. Usually this means narrowing the scope, naming a condition, or fixing a cause.

### Step 11: Write the copy

Follow the writing rules and the user's voice. Each premise of the refined argument becomes a step in the piece. The structure follows the idea, so there's no fixed template, but contrarian pieces usually work best in this order:

1. Open on a problem the reader feels, an outcome they want, or a belief they already hold.
2. Show the premise hidden under the common view.
3. Show why it fails, using a real case or logic alone.
4. State the refined thesis.
5. Say where the common view still holds.

The reader should agree with you first, then follow your logic somewhere they didn't expect. The copy never uses philosophy terms.

## Lens reference

Each lens lists the question it asks, what to look for, and the question the user can take with them.

**Logic**
- Asks: Does the conclusion follow from the premises?
- Look for: skipped steps, circular reasoning, comparisons against things never mentioned, false choices between two options.
- Trigger words that always activate this lens: always, never, everyone, nobody, best, biggest, most, only.
- Catch it yourself: "Does this follow, or did I skip a step?"

**Ontology**
- Asks: Are the things it names real, and defined correctly?
- Look for: something treated as a thing you can build or buy when it's really a result of other things; categories that lump different things together; incomplete lists presented as complete.
- Catch it yourself: "What kind of thing is this, really?"

**Epistemology**
- Asks: How do we know this is true?
- Look for: one person's experience stretched into a rule; evidence that only counts the winners; a partial cause stated as the whole cause; claims spread by people who profit from them.
- Catch it yourself: "How would I know if this were false?"

**Teleology**
- Asks: What is this for? Does the advice serve what the reader actually wants?
- Look for: stand-in goals (followers instead of clients, activity instead of results); advice that serves the writer more than the reader.
- Catch it yourself: "If this works perfectly, does the reader get what they came for?"

**Hermeneutics**
- Asks: How will the reader understand it, given what they bring to it? With someone else's content, what did the author mean?
- Look for: words that carry baggage for this audience; ideas likely to be misread; famous ideas quoted against their original meaning.
- Catch it yourself: "What will my reader hear when they read this?"

**Language**
- Asks: Does a key word keep the same meaning throughout?
- Look for: one word doing two jobs, especially between the reason and the instruction.
- Catch it yourself: "Does my key word mean the same thing in the first line and the last?"

**Ethics**
- Asks: Is this good for the reader, or does it work through pressure?
- Look for: shame, fear or false urgency doing the persuading; advice that would hurt the reader if they followed it.
- Catch it yourself: "Would I give this advice to a friend?"

**Aesthetics**
- Asks: Does the form fit the idea? Does it feel true, or performed?
- Look for: structure that fights the argument; filler phrases; tone that oversells.
- Catch it yourself: "Does the shape of this piece match what it's saying?"

## Pattern library

Use plain names, and explain each one when you first mention it.

- **Survivorship bias:** counting only the people it worked for.
- **False cause:** assuming one thing caused another because they appeared together.
- **Partial cause:** naming one cause as if it were the only one.
- **Equivocation:** one word carrying two meanings across an argument.
- **Wrong scope:** something true for some people presented as true for everyone.
- **Stand-in goal:** chasing a measure of the thing instead of the thing.
- **Category error:** treating something as a kind of thing it isn't.
- **False choice:** presenting two options when there are more.
- **Comparative claim:** "biggest" or "best" without saying compared to what.
- **Straw man:** arguing against a weak version of an idea.
- **Appeal to incentive:** advice spread mainly by people who profit from it.
- **Counter-cliché:** the well-worn opposite of a well-worn idea.

## Output format

Show the thinking in this order. Lenses that find nothing get one line each, so the reader sees they were checked. Lenses that find something get the full treatment.

```
## The claim
[One sentence]

## Steelman (for common advice or someone else's content)
[The strongest version of the view]

## The argument
- P1: ...
- P2 (hidden): ...
- Conclusion: ...

## The lenses
**[Lens]: [The question it asks]**
[What it found in this piece]
*Pattern:* [plain name]
*Catch it yourself:* "[question]"

**[Lens that passed]:** Passes. [One line on why]

## Candidate theses
| Thesis | Result |
[Two to four candidates, including the overcorrection and the counter-cliché, with why each passes or fails]

## Verdict
[What holds, what doesn't, in two or three sentences]

**Refined thesis:** [One or two sentences]

## Draft or edits
[The copy, or specific edits that keep the user's wording]
```

Then ask the belief-gate question if the user hasn't already confirmed the thesis.

If the user asks for a shorter run, keep the claim, the argument, the lenses that found something, the refined thesis and the draft.

Write the analysis itself by the same writing rules as the copy: plain words, full sentences, no em dashes.

