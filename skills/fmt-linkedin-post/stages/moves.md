# Content moves: the idea, the shape, then the moves

This stage decides what a post will be before anyone writes a line of it: the one idea, what a reader needs to get it, the shape and length that follow from that, and only then the moves from the library that do each part's job. It does not write the post. It ends with a brief the drafting step can follow.

Library files (relative to this stage file):
- `../library/hook-moves.md`: 18 hook moves with job, mechanism, what it needs, how it fails, good for.
- `../library/body-moves.md`: 9 structures, 9 inside moves, 6 closes, and the table of which structure each hook move tends to sit with.
- `../library/content-moves-sorted.csv`: the index of 357 posts tagged with hook move, structure, inside moves, close, media type and engagement, with the hook (column `Hook`), the notes and the URLs. Columns: ID, Source, Hook, Hook move, Secondary hook move, Structure, Inside moves, Close, Hook note, Body note, Engagements, Comments, Reposts, Post URL, Visual URL, Media.
- `../library/posts/<ID>.md`: the full text of each post. Read it for every example you pull.

Read the cards for the moves you are considering. Do not work from memory of them.

## Why this order

A post exists to carry one idea to a reader. Ideas differ in what they need. One only lands if the reader sees it happen; one goes against what the reader believes and needs an argument; one is something to do and needs steps; one needs two sentences and nothing more. A shape picked before the idea is clear forces the idea to fit it: a small idea gets stretched, a big one gets cut, and readers start to recognize the pattern after a few posts.

So the order is: what the person has, the idea, what the reader needs, the shape, then the moves. Two things stay fixed from the old order. Material still comes first, because a move picked before the material is checked is where invented facts come from. And the library still matters: it holds proven ways to do each part's job. It just comes in after the shape, as a drawer of parts, not as a plan.

The library shows strong pairs between hook moves and structures (a scene hook usually leads into a story, a contrarian hook into an argument). Those pairs exist because both follow from the same thing, the material and the idea. They're a useful check on a choice; they don't make it.

## Step 1. Inventory what the person has

Read before you ask. In this order:

1. The brief, if one exists (`brief.md` in the piece's folder): its parent ID, source IDs, material and outcome.
2. `canon/core-summary.md`, then the canon entries the brief points to: the stories (`canon/bank/stories.md`), the proof (`canon/bank/proof.md`), the POVs, the branch.
3. The idea bank entries the brief names, or the ones linked to the same branch or POV, and the credibility bank (`bank/credibility.md`): the entries that back this POV or branch, which fill RESULT, DOCUMENT (an `artifact`), LINE (a `said-about`) and the proof under any move.
4. `canon/strategy/channels/linkedin.md`, if it exists: this channel's job, its mix for the quarter, what's off the table here and the selling rule. A move that works against the channel's job drops out in step 4a the same way one that works against PURPOSE does.

Fill each slot below from what you read, and write the ID next to it (`STORY S4`, `RESULT R2`). Which entries count: `CLAUDE.md` rule 2. Then ask the person about the slots that are still empty, aimed at the slots most likely to be full for them. Three questions at most in this step; one question is one thing the person has to decide. When no person is present (a crew agent), questions go to the brief's Open questions and the piece is `briefed` or `blocked` as the strategist's rule says. When no canon exists yet (the skill is used on its own), ask first for the slots the strongest move needs.

Be literal. If something is not there, leave it empty; do not infer it.

```
RESULT      a number or outcome they can state (revenue, saves, clients, years, deals, a before/after)
METHOD      a repeatable process or framework they actually use
STORY       a specific moment they lived, with details they remember exactly (time, place, a line someone said)
DOCUMENT    something real they can quote verbatim (a memo, a letter, a test, an email, a book passage)
OPINION     a belief they hold that some of their audience would push back on
PATTERN     something they have seen repeat across a sample (clients, colleagues, people they have studied)
BORROWED    a true story about a recognizable person or company, with a specific action they can verify
NEWS        something that happened recently, with a source
DATA        a survey, study or analysis they ran or can cite exactly
EXPERIMENT  something they did for a defined period and can report on
ADMISSION   something true about them that most people in their position would not say
LINE        an exact sentence someone said to them (a client, an investor, a reader)
LAUNCH      a real thing they just made or started
```

Also record:

```
PURPOSE     what this piece is for: trust with buyers, leads, reach, being known for a point of view, recruiting, relationships with peers
AUDIENCE    who it's for, as a segment ID and one line
```

PURPOSE is this piece's job, not the person's overall goal. Take it from the brief's outcome, or from the layer mix in `canon/strategy/content-plan.md` and the channel's job in `canon/strategy/channels/linkedin.md`. The person's overall goal lives in `canon/vehicle/vehicle.md`; don't restate it here. Take AUDIENCE from the brief's segment, or from `canon/strategy/brand-strategy.md`. With no canon, ask.

If the request is "write a post about X" and neither the canon nor the person gives any material, stop and ask for it. Do not proceed on topic alone.

### The idea brief, when one fits

`../library/idea-briefs.md` lists 57 idea briefs by what the person has. When the idea in hand matches one, read that brief (`../library/briefs/<brief>.md`) and hold the inventory against its "What you need" list. Every need the inventory can't meet is a gap: say which one in a line, and either ask for it (inside this step's question budget) or pick the next brief or shape the material can carry. Never fill a need with an invented fact. Write the brief's name in the format plan as `IDEA BRIEF`, or `none`. A brief names the idea and the material; the reader's questions still decide the shape.

## Step 2. The idea

Write the post's idea in one sentence, in plain words, before anything else. It's the sentence a reader should be able to repeat to a friend.

- If the piece comes from an idea card (an idea bank entry with a `shape:` block from `/shape`), start from its translated line, and take what it says the idea gives the reader.
- If a brief already has "The one idea", start from that.
- Otherwise find it in the material from step 1: what is this person actually saying?

Three tests before going on:

1. **Cold.** Would a stranger get the sentence with no context from the person's other work? If not, add the missing context to the sentence.
2. **One idea.** If the sentence holds two ideas joined by "and", pick the stronger one for this post and note the other as a second post.
3. **More than a platitude.** What does the reader currently do or believe that this cuts against? If nothing, it's a platitude: find the angle that makes it bite, or say so.

If the idea can't be said in one sentence, the thinking isn't done and no shape will fix it. With the person present, say so in one line and offer `/think about <the topic>`. With no person present (a crew agent), put the question in the brief's Open questions and set the piece `blocked`.

## Step 3. What the reader needs, and the shape that follows

### 3a. What the idea gives the reader

Something to **do**, a way to **see**, a reason to **believe**, or a **direction** to head in (the same four as `/shape`). Take it from the idea card when there is one.

### 3b. Where the reader starts

One or two lines: what the reader (AUDIENCE from step 1) believes or does about this today, and whether they'd push back on the idea. A reader who already agrees needs a different post from one who thinks the opposite.

### 3c. The reader's questions

A post is the answer to the questions a reader would ask, in the order they'd ask them, between the first line and getting the idea. Write those questions down, in the reader's plain words, numbered. Usually two to five.

- Start from where the reader starts (3b). The first question is the one the opening raises.
- Each next question is the one the last answer raises. "Why would that be true?" "What about the obvious objection?" "So what happened?" "How do I do that?"
- Stop when the reader has the idea and can use it. A question the idea doesn't need answered stays out, however interesting the material behind it.
- Some ideas raise no question at all: the sentence is the post.

Each question becomes one beat of the post. These are the reader's questions, never lines of the post: they decide what the post covers and in what order, and the reader never sees them. The writer writes the lines.

### 3d. The shape

The questions decide the shape. Read them and name the structure they add up to:

| The reader's questions sound like | Shape | Card |
|---|---|---|
| What happened? Then what? What did you do? | the story arc | S3 |
| Why would that be true? What about the obvious objection? | the argument | S4 |
| Which ones? Why each? (the idea really is several separate things of the same kind) | the explained list | S2 |
| Where do I go to get them? (things outside the post: books, tools, people) | the bare list | S1 |
| How did that work? What made the difference? | the breakdown | S5 |
| What did you try, and what did you find? | the experiment report | S6 |
| (the reader knows the genre; the point is the gap between what's said and what's meant) | the script | S8 |
| What is it, who's it for, why now? | the announcement | S9 |
| (no question; the sentence lands on its own) | the body is the hook | S7 |

Steps the reader runs ("How do I do it? In what order?") are the explained list with an order that means something; the super-specific how type is built for them.

A list is a claim that these things, and only these, matter. If the questions only add up to a list because the material came as bullet points, the shape is wrong; go back to 3c.

When the questions fit two shapes, name both and say which one reads more clearly for this reader, in one line. When they fit none in the table, write the beats as they are and say so; the table holds the common shapes, not every shape.

### 3e. Length follows from the beats

The post is as long as the beats need, and no longer. No target word count. A beat that only needs half a sentence gets half a sentence. If the beats come to more than a post can carry, the idea is probably two posts or an essay; say so.

### 3f. Check the beats against the material

Go down the beats. Any beat that states a fact about the person (a result, a story, a client, a number) needs material from step 1 behind it. A beat that explains, argues or brings in a case from the world is the writer's job and needs none (`CLAUDE.md` rule 1).

- If a beat needs a fact that isn't in the inventory, ask for it in one question (counted in step 1's budget), or take the next shape the questions allow and say why.
- Never fill a beat with an invented fact to keep a shape.

### 3g. The post type

A post type (`../types/<type>.md`, listed in `../SKILL.md` under "Post types") is a tested method for one kind of post. Each type file says where it sits in the library: the hook moves, structures and inventory slots it uses.

1. **If the person named a type** ("a borrowed story", "make it a listicle", a type command such as `/power-listicle`), read that type file now and run its fit test ("When it fits, and when it doesn't") against the inventory and the idea. The person's choice stands: the type's path sets the shape. If the reader's questions point to a different shape, say so in one line ("this reads more like an argument than a list; want it as a list anyway?") and let them choose. With no person present, follow the type and note the clash under the brief's Open questions. If the material can't carry the type, say so, name the type it can carry, and let them choose. Never fill a type with invented material.
2. **If they didn't**, check whether the shape and the material match one type's "Where it sits in the library". When one does, name it beside the shape in one line ("an argument, as an op-ed"). When none matches, go without one; most posts don't need a type. A type the studio offers follows the shape the reader's questions set; it never changes the shape, and when it would, the questions win and the type drops.
3. **Once a type is chosen,** read its file in full, and the examples file in its folder. Run its steps in order where they say to (most bind the claim, pick a path, and add a gate). Write `TYPE` in the format plan. The draft stage follows the type's draft step; the judge runs its "Checks the judge adds".

## Step 4. The moves for each beat

Now the library. Each beat has a job; the library holds proven ways to do it.

### 4a. The opening: the hook move

The hook raises the first question and makes the promise the rest keeps. A hook move fits when its gate is open (the material it needs is in the inventory) and it opens this shape.

| Hook move | Needs (from inventory) | Good for |
|---|---|---|
| 1. Proof, then payoff | RESULT + METHOD (the payoff must come from that exact result) | trust, leads, saves |
| 2. Here's the actual document | DOCUMENT + one fact that makes it worth seeing | reach, trust |
| 3. Someone notable did something odd | BORROWED (odd, specific, verifiable) + an OPINION it carries | reach |
| 4. Put the reader in the room | STORY with exact details and a turn | being seen as a person, relationships |
| 5. Then and now | RESULT as a before and after, both specific, with a cause they can explain | trust, reach, origin stories |
| 6. The common advice is wrong | OPINION that denies advice the audience follows, with a real argument | point of view |
| 7. The call-out | OPINION as a shared grievance + standing (they are inside the group) | reach, loyalty; costs some readers |
| 8. The pattern I keep seeing | PATTERN with a real sample and one concrete trait | trust |
| 9. The line someone said | LINE, close to verbatim, with an unexpected response | relationships, leads |
| 10. News, plus a take | NEWS + an OPINION the headline does not give | reach, fast |
| 11. The finding | DATA with a surprising number | trust, reach, reposts |
| 12. The numbered promise | a real list where every item earns its place, sitting on another move | saves, followers |
| 13. The reframe | OPINION as a new lens that explains more than the old one | being remembered for an idea |
| 14. The honest version | a genre of speech the audience knows + inside knowledge | reach, likability |
| 15. The admission | ADMISSION + a reason it matters beyond confession | trust, relationships |
| 16. Do this right now | METHOD as a check that takes under a minute and reveals something | leads |
| 17. A bet on the future | OPINION as a dated, specific prediction with reasoning | point of view |
| 18. The announcement | LAUNCH + an existing audience + an origin | converting an audience, not growing one |

Procedure:

1. Mark every move whose gate is open. Usually three to six.
2. Drop the ones that don't open this shape. A move opens the shape when the question its hook raises is the first question in 3c. A "put the reader in the room" hook opens a story; it doesn't open an argument the reader has to be talked into.
3. Filter by PURPOSE using the "good for" column. A move that works against the goal drops out (a call-out when the goal is trust with buyers; an announcement when the goal is reach). The channel's job in `canon/strategy/channels/linkedin.md` filters the same way.
4. Rank the rest by the strength of the material. A number beats a vague result. A verbatim line beats a paraphrase. A story with a turn beats a story without one.
5. Read the full card in `../library/hook-moves.md` for the top two. Check the "how it fails" list against the material now. If the material fails the gate on inspection (the proof does not earn the payoff; the borrowed story is not verifiable), drop the move and say so.
6. Offer the top two, each in one line: what in the inventory makes it available and what it would buy. Say which one you'd pick and why.

On the direct path with the person present (`/post` stage 2), step 6 widens: skip the filter in item 2 that holds every move to one shape, and offer three to five openings across the shapes the reader's questions allow (3d) and the material can fill (3f), each written out as the post's first line or two and tied to the post it leads into, in plain words. The person's pick sets the SHAPE, the HOOK MOVE and the TYPE; their exact words go in OPENING. The reader's questions still decide which shapes are on the table; the opening decides which of those this post is.

Moves stack. Name a secondary move when it is clearly there (proof under a list, a story under a reframe).

If no gate opens for this shape, say so, and say what would open one: "If you can name the number of clients, proof then payoff becomes available." If a gate opens only for another shape, the material is pointing at a different post; say that too. Never pick a move and fill it with invented material.

### 4b. The pairing check

Look up the hook move and the shape in the table in `../library/body-moves.md` ("Notes from the full sort"). When they're a common pair, go on. When they aren't, that's allowed, and sometimes it's the point; write one line in the plan saying why this idea needs this pair. If you can't say why, one of the two choices is wrong: recheck 3c first.

### 4c. Inside moves, beat by beat

For each beat, name the inside move that does its job, when one does: the turn (M2), the evidence pair (M3), the analogy (M6), the other side taken seriously (M7), the meaning line (M9) and the rest in `../library/body-moves.md`. Read each card you name. A beat that needs no named move gets none.

Read the shape's card too. Its parts are what that shape usually needs (an argument the reader would push back on needs the other side taken seriously; a story needs a complication before the turn). Use them as a check on the beats: when the card names a part the beats skip, either the beats missed a question or the idea doesn't need it. Say which, in one line.

### 4d. The close

The close answers the reader's last question, or ends on the last beat when nothing is left to ask. If the last question is "what do I do now?", a small instruction. If the post leaves the reader with something to say back, a question back. If the last beat is the strongest line, no close. The restated principle is the most used close in the library and the lowest performing; use it only when the material gives a reason.

## Step 5. Pull examples

1. Filter `../library/content-moves-sorted.csv` by the shape first (the "Structure" column), then prefer rows whose "Hook move" starts with the chosen move's number. Sort by Engagements, descending. Take three to five. If the set is thin, widen to the shape alone and say so.
2. Read each in full from `../library/posts/<ID>.md`, with its notes. The examples show the jobs done well; their wording is not a model. Many break the writing rules (dashes, "Here's the truth", stacked fragments). Take the job they do, never their phrasing or their beat order. If the piece has a visual, prefer examples whose `Media` column says carousel, infographic or image, so you see how the words and the picture split the job.

## Output: the brief for drafting

Write the brief into the piece's `brief.md`, made from `templates/piece/brief.md`. If `/post` or `/essay` already started it, fill in what's missing and leave the rest as it is.

The shared sections:

- **The one idea**: the sentence from step 2.
- **Fractal shape, reader, outcome, not saying, call to action, open questions**: as the template asks, parent line included.
- **Purpose**: PURPOSE from step 1.
- **Material**: the filled inventory slots, each as the template's Material section says. For example: `STORY S4: "..."`.

The format plan section, which this stage owns:

```
GIVES           do, see, believe or direction, and at what level (3a)
READER NOW      what the reader believes or does about this today, and whether they'd push back (3b)
QUESTIONS       the reader's questions in order, numbered; each is one beat (3c)
SHAPE           code and name, from the questions; the runner-up if there was one (3d)
LENGTH          in plain words, from the beats (3e); a guide, never a target
TYPE            the post type file and its path, if one was chosen (3g); otherwise none
TYPE NOTES      what the type's checks need on record (the newsjacking clock word, the proof post's permission, a simple listicle's contents page as lead capture), or none
HOOK MOVE       number and name, one line on why it's available, how it opens this shape and what it buys
OPENING         the opening the person picked, as they saw it or rewrote it (direct path); otherwise none
SECONDARY MOVE  if any
PAIRING         common, or the one line on why this idea needs an uncommon pair (4b)
INSIDE MOVES    per beat, where a beat has one (4c)
CLOSE           which one, and why (4d)
EXAMPLES        IDs of the pulled posts, with the full hook line of each
WATCH FOR       the "how it fails" items for this move that this material is closest to tripping
```

If no piece folder exists (the skill is used on its own), give the person the same plan in the reply.

Hand the brief to the drafting step. The draft stage turns the questions into a skeleton before it writes a sentence.

## Rules that apply to everything downstream

The house rules (`skills/craft-house-rules`) apply, and supplied copy and source quotes follow `CLAUDE.md` rule 3. The judge checks them as failure conditions. One more for LinkedIn:

- First-person presence: the reader must be able to see the writer in the post, not just facts about the subject.

## What comes next

Drafting is `draft.md` and judging is `judge.md`, run as separate passes so the judge never grades its own work. Hand the brief to the draft stage.
