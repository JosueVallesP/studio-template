---
name: job-post
description: One LinkedIn post, end to end, from one command. Takes whatever the person hands over (something that happened, a thought, something they read, an old piece, or nothing, in which case it reads the idea bank and their material) and builds the post with them in stops: what they're saying (built and tested with copylosophy, backed by their files or a scout), three to five openings each tied to the kind of post it leads into, the outline, then the draft, judge and human check, without a strategist or a producer. Works on day one with no canon; uses the voice guide, the strategy and the canon when they exist. Use for /post, "write a post", "make me a post", "post about this".
---

# /post

The person wants a post and they want it now. This skill gives them one through the same chain every post runs (`skills/fmt-linkedin-post`: moves, draft, judge), and skips everything built for the week-to-week loop: the shortlist, the brief approval, the editor, the librarian. What it keeps is what makes a post good: real material, one idea said plainly, a shape that comes from what the reader needs to get that idea, moves whose required material lines are all present in the inventory (the gate list in the moves stage), the person's voice, a judge who didn't write it, and the human check.

Every post lands in `pieces/`, so `/status`, `/review` (ship, hold, kill) and `/librarian` see it.

## What a post is made from

Facts about the person, in this order, and nothing else:

1. **What they hand over now.** Text pasted in the chat, a file they name, or what they say when asked. What a person tells you in the session is their word; it counts the same as a file.
2. **`material/`**: what they've already made (posts, essays, transcripts, stories, notes). Read it. This is the main source when the canon is thin or empty.
3. **`inbox/`**: what just happened, not yet captured. Run `python3 scripts/inbox-to-text.py` first so exports and Word files are readable.
4. **The canon and the working banks**, when they exist: entries in `canon/bank/stories.md`, `canon/bank/proof.md`, `canon/person/povs.md`, `bank/ideas.md` and `bank/credibility.md`, used as `CLAUDE.md` rule 2 says.

No fact about the person is invented. A number, a name, a client, a quote, a result or a story that isn't in one of these four places doesn't go in the post. If the best move needs one, ask for it in one question, or pick the next move.

The rest of the post is yours to write. The material gives the scene, the number, the opinion; you give what makes it a post worth reading: why the idea is true, how the thing works, what it means for the reader, the counterpoint and your answer to it, an analogy, a real and checkable example from the world when the material has none (a known company, a known campaign, a moment from history or the news), and the general point the material supports. Each line goes in the source map under one of the kinds in `CLAUDE.md` rule 1. A post that only re-says the person's old sentences in a new order isn't a post, and in the studio's runs so far a post built that way has scored as model-written.

## What shapes the post

- **Voice:** the voice order in `skills/craft-house-rules` ("The voice order"), the one definition every writing path follows: the rewrite pairs (`python3 scripts/rewrites.py pick --format fmt-linkedin-post`), then `canon/voice/voice-guide.md` if it exists, then five to eight of the person's own pieces from `material/`, and plain writing only when none of those exists. On day one, with no pairs and no guide, their own posts are the voice.
- **Who it's for and what it should do:** set at stage 1, before the argument (see "The reader and the job" there). The channel's job, the mix and the selling rule come from `canon/strategy/channels/linkedin.md` if it exists; otherwise `canon/strategy/outcomes.md` or `config/intake.yaml` from the intake.
- **Language:** `config/tools.md` if it sets one; otherwise the language of the material; if the material mixes languages, ask which.
- **The standards:** `skills/craft-human` on every post, the writer pass of `skills/craft-copylosophy` (defined in its "In the studio" section), and the house rules (`skills/craft-house-rules`).

## Procedure

The post is built with the person, one decision at a time, and each decision is shown on its own before the next one is built on it: what they're saying, then how it opens, then the outline, then the draft. A wrong turn caught at the first stop costs a sentence to fix; caught in a finished draft, it costs the draft. The person never gets a finished post with only "do you like it?" to say about it.

Three contexts, as before: the planning here (stages 1 to 3), the draft in a fresh one (stage 4), the judge in another (stage 5). The pass that plans reads the libraries and the rules; the pass that writes reads the packet and nothing else; the pass that judges never wrote a word of it.

### The words the person sees

People don't think in premises, theses, hook moves or shapes, and they shouldn't have to learn them to get a post. The studio's labels stay in the files. To the person, it's "what you're saying", "why it's true", "when it holds", "the opening", "what the post would be" (a story, a list, an argument, a borrowed story) and "the outline". Never ask "what's your premise?" or "what's your thesis?": people freeze on those. Ask about what happened, what they think, what they keep telling clients, what bugged them in something they read (`skills/craft-interview`).

### Where they start

Whatever they hand over is a fine start, and none of it needs to be an argument yet:

- **Something that happened** (a call, a client moment, a result): ask what they took from it, then go to stage 1.
- **A thought, a hunch or a rant**: that's the raw idea; go to stage 1.
- **Something they read or watched** (a link, a post, an article, a video): read it in full (fetch the link, or pull the transcript as `skills/setup-sources` says), ask what they agree or disagree with, and go to stage 1 with their reaction as the idea and the piece as an outside source.
- **A finished long piece of theirs** (an essay, a talk, an article, a long post): the post is a clip, not a smaller copy. Run step 1 of `skills/job-adapt` ("One idea per piece"), offer the two or three ideas a post can carry whole, one line each, and set `adapted_from:` to the source file. Their pick goes to stage 1.
- **A number or a seed** ("/post 2", "/post I14"): a number is that candidate in `pieces/shortlist.md` (`skills/role-strategist`, what's ready to harvest); an I ID is that seed. Its seed record is the material; go to stage 1.
- **Nothing** ("/post" alone): when `pieces/shortlist.md` is from this week, offer its top three first, one line each. Otherwise read the idea bank first (`bank/ideas.md`, entries `ready`, then `raw`), with the credibility bank beside it (an idea with a strong result behind it is a stronger first post), then `material/` and `inbox/` (run `python3 scripts/inbox-to-text.py` first). Offer the three strongest in three lines (a story with a turn, a result with a number, an opinion someone would push back on, an outside piece that serves one of their views) and say which you'd pick and why. If the bank is empty and `material/` is large, also offer, in one line, to go through all of it and fill both banks (`/shape`, "the whole material"), so next time there's a list to pick from.
- **A type by name** ("/post borrowed story", `/power-listicle` and the rest in `skills/fmt-linkedin-post/SKILL.md`, "Post types"): stage 1 still runs; at stage 2 the openings all lead into that type, and the moves stage checks the material can carry it (step 3g). When the studio suggests a type the person didn't ask for, the reader's questions win: a type is offered only when it fits the shape they point to.
- **They already know what they're saying, or already have an opening**: start at the stage they're at. Run the earlier stage's checks on what they gave, without the questions, and raise only what fails ("this holds, except it's only true for clients who already trust you; want to say that?").

A topic with no material behind it ("something about pricing") is a question to the person, not a post.

Open the piece folder as soon as there's something to keep: `pieces/<yyyy-mm-dd>-<slug>/` with `brief.md` from `templates/piece/brief.md`; `path: direct`, `status: briefed`, `format: fmt-linkedin-post`, `channel: linkedin`. Fill `parent`, `segment` and `desire` with canon IDs when they exist; otherwise `none (direct)` and one line in words for the reader. The brief fills in as the stages go; the person never has to read it.

**The seed.** Every post grows from one seed in the idea bank (the template there defines the record). Name it in the brief's `seed:` line: the entry they picked, or the entry that holds what they handed over. When what they handed over isn't in the bank yet, file it there first as `skills/role-capture` says (their words in `raw`, `stage: seed`), so the post and the idea stay linked. Then, as the stages go:

- Their yes at stage 1 confirms what the idea says. A seed still at `seed` moves to `sprouting`: say so in one line and set it. Stage 1's premise tests are its first wind (the idea bank template defines it), so no separate objection follows: record the doubt it met and their answer in `pushback`, as the next line says.
- Each doubt the argument meets in stage 1 (a premise that didn't hold at first, a case it fails, where it stops being true) goes in the seed's `pushback` with their answer in their words. A doubt they couldn't answer stays `open` and the post doesn't claim past it.
- An outside find from scout that the post uses goes in the seed's `fed`.
- When the draft is written, add the piece to the seed's `fruit` as `drafted`. The librarian marks it `shipped` when it ships.

### Stage 1: what you're saying (stop for a yes)

#### The reader and the job

Before the argument, settle two things, because the argument is built for them: who has to read this, and what it should get done for that reader. A post written for nobody in particular reads well and could have come from anyone; the same idea, written for one person, gets the examples, the objection and the level right.

- **One real reader.** A person, not a segment: a client the person had a call with, someone who left a comment or asked a question, a buyer whose objection they keep hearing, a peer who does what their readers do. Name them, or describe them by what they do and what they believe now ("a coach two years in who thinks posting more will fix her pipeline"). Look in this order: what the person said today, `bank/questions.md`, the audience file (`canon/strategy/audience.md`, its PFDG entries), the credibility bank's clients, then `material/`. "Founders", "my audience" or "people like me" isn't a reader yet: ask for the last one of them they talked to. A post goes to many people; it's written for this one, and the others who share their problem get it too.
- **The job.** What this reader should think, feel or do after reading, in one line, and what the post is for the person (trust with buyers, leads, reach, being known for a point of view), from the channel file or the intake when they say. Also whether it's a test piece or a cornerstone (`kind:` in the brief; most posts are tests).
- **Guess, then confirm.** Don't open with these as questions. Infer both from what they handed over, the strategy and the banks, and put them at the top of the stage 1 message below, each marked "my guess" when it's inferred. If nothing points anywhere, ask one question: "Who's the last person who needed to hear this, and what should they do after reading it?"
- **The shape still comes later.** The format isn't decided here: the idea and this reader's questions decide it at stage 2. If the person already said "a short post" or "a list", note it and let stage 2 test it.

Build the argument with them. This is the writer pass of `skills/craft-copylosophy` (its "In the studio" table), run as a conversation instead of in the background: find the claim in what they gave (step 1), separate the reason from the instruction (step 2), lay the argument out (step 3), test each premise (steps 5 and 6), and, when the idea goes against common advice, the contrarian and provocation tests (steps 7 and 8). The belief gate (step 9) traces the point to their words: a confirmed POV or branch when the canon exists, otherwise a line in `material/`, `inbox/` or `said today`.

- **Ask, don't fill.** Where a step needs something only they know (why they believe it, the case that taught them, the client it doesn't work for), ask, anchored in an event: "When did you last tell a client this? What did they believe before?" Three questions at most in this stage, one at a time. When their answer is a half-thought, offer the sharper version beside it and ask if it's still true (`CLAUDE.md` rule 3).
- **Back it up.** Say what already stands behind it: their credibility bank first (`bank/credibility.md`, entries that back this view or match it), then the canon's proof and stories, then `material/`. Anything that builds trust they mention in this stage (a result, a client, something a client said) goes to the credibility bank as `said today`, as `skills/role-capture` step 3a says, and any idea they say on the way goes to the idea bank, so both banks grow while the post is made. When the argument needs more than they have (a real case, the best argument against, a number), offer once to look outside: "I can look for a real case or someone arguing the opposite. Want me to?" On a yes, run `skills/job-scout` on this one idea (its "Called from a piece" note): up to three finds, each with its source, filed as outside entries and shown in a line each. A find is never their view; in the post it's `borrowed: verify`.
- **Show it, plainly, in one short message:**
  - who it's for: the one reader, in a line;
  - what it should do: what that reader thinks, feels or does after, and what it's for (test or cornerstone in a word);
  - what you're saying, in one sentence a stranger would get;
  - why it's true, in two or three plain reasons;
  - when it holds, and where it doesn't;
  - what the reader does or believes now that this cuts against;
  - what backs it up (theirs, and any outside find).
  Then one question: "Is that who it's for and what you think? Yes, or tell me what's off." A correction to the reader or the job is taken as they say it; if it changes what the argument has to do (a different reader believes something else now), rebuild the argument lines for that reader before showing them again.
- **On a yes,** write the reader to the brief's "The reader" (`One real reader:` line), the job to Outcome and Purpose, and `kind:` to the frontmatter; the sentence to "The one idea", the reasons and conditions to the brief's Material and Not saying as they fit, and save the full check to `pieces/<id>/argument-check.md` (the copylosophy output format). A new belief they confirmed here goes to a `draft` POV entry in `canon/person/povs.md`, with their quote, the source and a log line, as `skills/setup-brand-tree/SKILL.md` ("Where a picked-up belief goes") says; `proposals.md` only when it changes a confirmed entry.
- **If it won't hold,** say which part breaks and what would fix it (a condition, a narrower claim, a different case). If it can't be said in one sentence after that, the thinking isn't done: offer `/think about <the topic>` and stop. A post can't fix an idea that isn't finished.

A post that only tells a story or shows a result, and doesn't argue, gets the short version (the claim, the hidden premises, the logic and evidence lenses) and a one-line stage 1: "For <the reader>, so they <the job>. The point of this one is X. Right?"

### Stage 2: the openings (they pick)

Run `skills/fmt-linkedin-post/stages/moves.md` steps 1 to 4a with the agreed sentence as the idea: the inventory, what the reader needs and their questions, the shapes those questions allow, and every opening whose material is there (its gate open). Then offer three to five openings, each one written out as the first line or two of the post, and each one tied to the post it leads into, in plain words:

> 1. "We lost the client in week two, and it was the best thing that happened to the offer." Leads into a story: what happened, what you changed, what it means for anyone onboarding a client.
> 2. "Three things I check before I take on a client." Leads into a list, one reason each.
> 3. "In 1982 Toyota let any worker stop the line." Leads into a borrowed story that proves the same point.

Rules for the set:

- **Different openings, different posts.** Each option leads into a different kind of post, or into the same kind from a different piece of material. Five ways of saying one opening is one option.
- **Only posts the idea can really be.** Every option leads into a shape the reader's questions allow (moves stage, 3c and 3d) and that the material can fill (3f). A list only appears when the idea really is several separate things; a borrowed story only when there's a real, checkable case behind it, found in their files or by the scout. If the idea only allows two kinds of post, offer the honest few, not five.
- **No invented material.** An opening that needs a number, a client or a story they haven't given doesn't make the list. If one would be strong with one missing fact, say so in a line: "If you can tell me how many clients that was, this one opens it."
- **Your pick.** Say which you'd pick and why, in one line.
- **A move they saved.** Read `bank/swipe-file.md` (the teardowns; never `bank/swipe/`, the whole pieces) if it exists. When an entry's `carries` names this idea's view or story, or one of its `moves` fits a shape the reader's questions allow, one of the options may use that move, built from the person's own material like any other. Say where it came from in a few words ("the move from the Rogan post you saved: your status is something the reader knows and the other person doesn't"). It counts as one of the three to five, never an extra, and only when the move fits the idea; a saved post is never a reason to change what they're saying. The option borrows the move and nothing else: no line, phrase, name or story from the saved piece. If the person wants to see the saved piece, show it from `bank/swipe/<ID>.md` here in the main session; the writer still gets only the move.

They pick one, mix two, or rewrite one. Their pick sets the format plan's HOOK MOVE, SHAPE and TYPE, and their exact words go in a new OPENING line. An opening they wrote themselves is supplied copy (`CLAUDE.md` rule 3). Then run the rest of the moves stage (4b to step 5) on the pick.

### Stage 3: the outline (stop for a yes)

Show the post before any sentence of it is written, in plain words:

- the opening they picked;
- the beats, one line each, as what each one tells the reader, in order;
- where each beat's facts come from, in a word (your story about week two, the Toyota case, the reasoning);
- the length in a phrase ("short, five or six short paragraphs").

Then one question: "Is this the post? Yes, or tell me what to move, cut or add." Take their changes into the brief's QUESTIONS and plan, then build the packet: `python3 scripts/packet.py pieces/<id>`, and say its word count in one line.

### Skipping the stops

If they say "just write it", or nobody is there to answer (a scheduled run, or a question already unanswered), make each call yourself, go straight through, and say at the top of the result what you took: the reader and the job, the sentence, the opening and why, and the kind of post. If they skip a stop they asked for earlier, say in one line what they lose: a draft built on a point they haven't agreed to.

### Stage 4: the draft (a fresh context)

In Claude Code, hand the piece to the `writer` agent, in the foreground. In the app, open a new chat and say "draft the post in pieces/<id>". The writer reads `skills/craft-house-rules/writer-sheet.md`, `skills/role-writer` ("Inputs" and "Procedure"), the packet and the format's draft stage, and nothing else: not this chat, not the libraries, not the full house rules. It runs `role-writer` steps 1 to 8 (step 1 reads the packet, which already holds the inputs) with these differences:

- **The stops are the approval.** The person agreed to the sentence, the opening and the outline; there's no separate brief to approve.
- **The opening they picked leads.** The three drafts keep its move and its promise; they differ in the wording around it and how the body moves, never in which opening or which kind of post. An opening the person wrote is kept as written. The outline they agreed to at stage 3 is the only plan stop: the writer's skeleton is a working file built from it, never shown for a second yes.
- **The four sources.** A material line cites a canon ID when there is one, otherwise the file and the line it rests on, or `said today:` for something the person told you in the chat, written into the brief's Material section by the planning stages.
- **Questions come back, not out.** Where the writer would stop and ask (a missing scene, as the scene rule in `templates/piece/brief.md` defines it, a fact the post needs, a point that doesn't hold), it sets `status: blocked` with the one question in `log.md` and stops. The main session asks the person in one question, writes the answer into the brief as `said today`, rebuilds the packet and hands the piece back.
- The writer sets `status: drafted`; the next actor is the judge.

### Stage 5: the judge (a fresh context)

In Claude Code, hand the piece to the `judge` agent, in the foreground. If anything else starts before the review lands (an intake question, an interview), the post waits its turn (`CLAUDE.md` rule 9). In the app, open a new chat and say "judge the post in pieces/<id>". The judge runs `skills/fmt-linkedin-post/stages/judge.md` against the brief, the draft and the material files only, with the grades from the gates table in `skills/role-editor`; it never sees this chat. On the first judged draft it makes the piece's one detector call and records the label as a reading. It writes `review-v1.md` from `templates/piece/review-direct.md`.

On revise: one revision, from the review's THE ONE THING line (`skills/craft-refine`), in the `writer` agent again (a fresh context, the packet plus the review's fails), bumped to v2 and judged again from the beginning in a fresh context, with no second detector call. On a second revise, stop drafting: show the post with each remaining fail as one plain line under it, and the person chooses: post it as it is, fix those lines themselves, or one more pass. On redo: if the judge found a different idea or the wrong kind of post (check 5 of the judge stage), go back to the stage that decided it (stage 1 or stage 2), show what the judge saw in two lines, and ask before drafting again.

### Show it

Give them the post as they'd paste it, the judge's verdict word (pass, revise or redo) with any fail still open as one plain line, and two short lines: what in the material would make a second post, and, when the canon is empty, what the interviews add (the studio stops guessing the voice and the reader from a few files). Set `status: reviewed`. The kind of post and why don't need saying again; they chose it.

End with the decision that's theirs: "If you like it, post it, then say `/review` and 'ship it' so the studio records it. If you rewrite it first, paste your version when you ship: the studio keeps the pair and writes more like you next time. Say what to change, or 'kill it', otherwise. Say `/visual` for the picture."

## When the canon exists

Everything above still holds. Two things change:

- Material lines cite canon IDs, and the judge checks them against the canon as `stages/judge.md` already does.
- If `canon/strategy/channels/linkedin.md` sets a selling rule or a mix, the post follows it (no CTA when the rule says this isn't a selling piece; the channel's purpose fills PURPOSE).

There is one way to make a piece, and it's this one: the person shapes the idea in the stops, the writer drafts, the judge reads it cold, and the person decides. "What should I write next" is the list of what's ready to harvest (`skills/role-strategist`), and a pick from it comes back here.

## Rules

- Facts about the person come only from the four sources. Never from the topic, the hook move's example posts, or what people like this person usually say. The reasoning, the framing, the analogies and the world examples are yours; write them, mark them as rule 1 says, and make sure they're true.
- Who it's for and what it should do come first, guessed from the files and confirmed with what they're saying; a post is never planned for "everyone" or a segment name alone.
- What they're saying comes before any opening, the opening before the outline, and the outline before any sentence. Each is shown and agreed before the next is built on it when the person is here.
- The person picks the opening from three to five real options, each tied to the post it leads into. The studio never picks a kind of post the reader's questions don't call for or the material can't fill.
- The pass that plans never drafts, and the pass that drafts never judges. Three contexts, every time, even when the post looks fine. The writer sees the packet, not the planning.
- Supplied copy and source quotes: CLAUDE.md rule 3; the cap on source quotes is the default in `templates/piece/draft.md`.
- One post per run. If the material holds more, say so.
- A direct post never confirms anything in `canon/`. What the post reveals about the person (a belief stated three times, a story they keep reaching for) follows `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes", if it's worth keeping.
- Everything in the house rules (`skills/craft-house-rules`) applies.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`: the date, the skill, what was unclear.
