# Content draft

Input: the piece's `brief.md`, with its one idea, material, purpose and format plan (QUESTIONS, SHAPE, LENGTH, HOOK MOVE, OPENING when the person picked one, INSIDE MOVES, CLOSE, EXAMPLES, WATCH FOR). If there is no brief, or its format plan is empty, run the moves stage first. Do not draft from a topic.

If the format plan has no QUESTIONS or SHAPE line (a brief written before the moves stage worked out the reader's questions), run the moves stage's steps 2 and 3 on the brief first, add the lines, and note it under Brief defects. Don't change anything else in the brief.

What the writer reads at this stage, and nothing else:

- `pieces/<id>/packet.md`, built by `python3 scripts/packet.py pieces/<id>` after the moves stage. It holds the writer's sheet, the brief, the few cards the plan picked (cut out of the libraries by their headers), the type's draft step when there is one, and the voice: the rewrite pairs, the voice guide when it exists, and five to eight of the person's own pieces. If there's no packet, build it first.
- This file, for the procedure.

The libraries, the full house rules, `craft-human` and `craft-copylosophy` are not read here. The cards the plan picked are in the packet; the rules the writer needs are on the sheet; the judge reads the rest in its own context. A writer with the whole repo in front of it follows the most concrete rule it last read, and that is how posts came out stitched and over-built. Self-check at the end: `python3 scripts/self-check.py <draft> [--source <their raw words>]`.

## Why this order

The post is written in stages, not in one pass from the first line to the last: the skeleton, then the body, then the hook, then the close. The skeleton is where the shape gets decided and checked, while it's still cheap to change. The hook comes after the body, so it promises what the body actually delivers instead of a shape the body then has to fit.

## Before writing

1. Read the packet top to bottom once: the sheet, the brief, the cards, the voice. Then read the one idea and the QUESTIONS in the format plan again. Keep the idea sentence in front of you the whole time; every line either helps the reader get it or goes.
2. The cards for the shape and the inside moves are in the packet; keep each mechanism sentence in front of you. If the plan names a TYPE, the packet carries its draft step; follow it and its path, and where the type and a card disagree, the type wins, since it was built from posts of that kind.
3. The plan's EXAMPLES line holds the hook line of each pulled post; that is all the writer reads of them. Other people's posts in full, at the moment of writing, are where borrowed tics and borrowed shapes come from. The moves stage read them to pick the moves, and the judge can open them.

## Step 1. The skeleton

Turn the QUESTIONS into beats: one line per beat, in plain words, saying what the beat tells the reader (the answer to its question), with the source it stands on (an ID, a file, `said today`, `writer` or `borrowed: verify`). Name the file or ID, not the quoted words: the skeleton is where the post's meaning gets decided, and a beat built around a quote comes out as that quote with a frame around it. A beat the sources can't carry is cut, not stretched; if the idea needs it and nothing of theirs carries it, mark the piece blocked and say what's missing. A thin source bank makes a shorter post.

Then read the beats alone, in order, as a stranger would:

- **Does the idea come through?** Someone who read only the beats should be able to say the idea sentence back. If not, a beat is missing or in the wrong place.
- **Does each beat earn its place?** Cover each beat in turn. If the reader loses nothing without it, cut it.
- **Is any question left hanging?** If a beat raises a question the next one doesn't answer, and the idea needs it answered, add the beat.

The skeleton may change the plan: a beat cut, a beat added, two merged, the order changed. When it does, say what changed and why in one line under Brief defects. When the skeleton shows a different shape would carry the idea more clearly, say so there too and keep to the plan's shape; the judge decides whether the shape fits.

The skeleton is a working file, not prose: no hook, no sentences to polish. On the direct path the person has already agreed to the outline (`/post` stage 3); keep to it, and put any change the skeleton forces under Brief defects.

## Step 2. The body

Write the body from the skeleton as one person talking, the way the person would say it to a friend. Don't draft beat by beat; prose written that way comes out in blocks, each with its own little ending. Then check every beat is there.

The reader's questions are scaffolding. They decide what the post covers and in what order; they never appear on the page. The body answers them the way a good talker does, by saying the next thing the listener needed before they had to ask. No question-and-answer pairs ("Why does this matter? Because..."), no questions as headers, no FAQ. A question belongs in the post only when the person would ask it out loud in that spot, and one is usually the most a post can carry.

The material is the facts, not the post. Around them, write: why the idea holds, how the thing works, what it means for the reader, the objection and the answer, an analogy if one makes it clearer. When a beat needs an example the material doesn't hold, use a real, checkable case (a known company, campaign, or moment from history or the news), marked `borrowed: verify` (`CLAUDE.md` rule 1). Never invent a client, a story, a number or a scene for the person and present it as theirs.

Keep the person's facts exact. If they said "18 clients in the past 1.5 years", that is the number. Do not round, dramatize or reorder it to sound better. But write the fact fresh, from what it means and in their register; don't carry the source's sentence over. Their words stay word for word only when the exact words are the point (a term they coined, a number as they said it, a line the post is about), marked `verbatim` and inside the cap of two. A line that keeps eight or more of the source's words without that mark fails `check-stitch` (H34). Two more things never go in: an example the person used to teach (a workshop case, a figure they gave to illustrate) written as something they did or refuse, and a beat stretched from a fragment that doesn't carry it. When the person has written about this thing (a memo, a journal entry, a draft on this idea), their sentences are the draft and the connecting tissue is yours; that is the one case where keeping their sentences is the method (`skills/craft-house-rules`, "The person's words, when they said this thing").

What each shape usually needs is below, as a check after the body is written, not a form to fill. The beats decide; when a part listed here isn't in the beats, the skeleton already said why or the idea doesn't need it.

**The argument**
- Claim (the hook's claim, now stated plainly)
- The other side, taken seriously: the reader's objection in the words they would use, one to three lines
- Evidence one: a specific case, with a number or a name
- Evidence two: a different case, not the first one twice
- The turn: one line
- The meaning line: one or two sentences, in the plainest words available

**The story arc**
- Setup: one or two lines, the smallest amount of context that lets the next beat land
- Complication: the thing that went wrong or the resistance
- What they did
- The turn: one line
- Result
- The meaning line

**The explained list / the bare list**
- Items in an order that means something (the order learned, most important first)
- Explained list: for each item, one to three sentences that add a reason or a case, never a restatement
- Bare list: one line per item, every item a real thing
- No item added to reach a number

**The breakdown**
- Context block: two to four lines, only the facts the parts use
- Numbered parts, each with a name and what it did, specific actions not qualities
- Takeaway: one or two lines, no bigger than the breakdown supports

**The experiment report**
- What was done and for how long
- Findings as observations, each one something that surprised
- Verdict

**The script**
- The frame in one line, then stay in character to the end

**The announcement**
- The news in one line
- The origin: the gap or the frustration
- What it is and who it is for
- One ask

**The body is the hook**
- Nothing. If the brief says S7, the hook is the post. Resist adding.

Whatever the structure, the turn is one line, and the meaning line comes after the material has already made the point. One meaning line in the whole post; if other paragraphs are ending on a neat summary too, cut those (house rule H30).

## Step 3. Hooks, written against the body

Now write three hooks. All three use the plan's hook move. They differ in which piece of the material leads, not in the move. When the plan has an OPENING line (the person picked it before any of this was written), the body was written to keep its promise and all three hooks start from it: keep its move and its meaning, and sharpen only the wording; an opening the person wrote themselves is supplied copy and stays as written. If the body can't keep the opening's promise, say so under Brief defects rather than changing the opening.

For each hook, check two things in one line:

- **The mechanism.** Read the move's mechanism sentence. For proof then payoff: does this proof earn this payoff? For the line someone said: is the line verbatim and is the response unexpected? For the common advice is wrong: would the reader actually defend this advice? If the check fails, the hook is not done.
- **The promise.** The hook raises the first question in the skeleton, and the body you just wrote answers it. A hook that promises more than the body gives (seven steps when the body has four, a secret when the body has a principle) fails, however good it sounds.

The hook is the first one to three lines. It must work before the reader clicks "see more".

## Step 4. Close

Write the close the plan chose, or none if the last beat is the strongest line. Offer one alternative. The restated principle is allowed only when the brief gives a reason; it is the most used close in the library and the weakest.

- Question back: a question with a one-line answer the reader can give in public
- Small instruction: one action, under a minute, that uses the idea
- Open door: one offer, directly related, after a post that earned it
- The aside: a real detail that drops the register
- No close: end on the last beat if it is the strongest line

## Step 5. Assemble and strip

Put the hook, the body and the close together and remove anything that was scaffolding. Read it once as a reader on a phone. Then the length test: cover each paragraph in turn; if the reader loses nothing, cut it. The post ends when the reader has the idea. Then apply the house rules (`skills/craft-house-rules`) as cuts, not as a checklist to tick. One more cut for LinkedIn: anything that reads as a copywriter instead of a person (stacked one-line paragraphs for effect, rhetorical questions in a row, a "here's the thing"). Keep the first-person presence the moves stage asks for.

Supplied copy and source quotes: CLAUDE.md rule 3.

## Three drafts

The house rules ask for three distinct drafts, written in one session and each built through the steps above, and the judge picks. All three keep the skeleton's beats; they differ in what leads, which hook, and how the sentences move, never in the idea. When the plan has an OPENING line, all three keep that opening's move and promise and differ in the wording around it and how the body moves; never in which opening or which kind of post. A draft that drops, adds or reorders a beat says so in its one line. Write the body of each fresh; don't make B and C by editing A.

## Output

```
SKELETON       the beats, one line each, with the source each stands on, and any change to the plan's questions
HOOK OPTIONS   three, each with a one-line mechanism check and promise check
POSTS          three distinct full drafts (A, B, C): different in what leads and how the body moves (with a picked OPENING, in the wording around it); say in one line what each one bets on
POST           the one you would pick, and why in one line (the judge may pick another)
CLOSE ALT      one alternative close
PARTS MAP      which lines are the turn and the meaning line, and which lines carry which beat (so the judge can find them)
BRIEF DEFECTS  anything in the plan or brief that didn't hold (a beat the idea didn't need, a question it did, a card number and description that disagree, examples that don't fit), what you did, and why
ARGUMENT CHECK the writer pass of craft-copylosophy: the premises and the refined thesis
```

Save it as `draft-vN.md` in the piece's folder (from `templates/piece/draft.md`): the three drafts under `## Post A`, `## Post B` and `## Post C` (a revision of the one draft the judge picked goes under a single `## Post`), the other blocks where the template puts them, with a source map in the five kinds of `CLAUDE.md` rule 1 and the argument check below it. If no piece folder exists, give it in the reply.

Hand the output and the brief to the judge stage. Do not revise based on your own reading; that is the judge's job.
