# The writer's sheet

Everything the writer needs at the moment of writing, on one page. The full house rules (`SKILL.md` beside this file), `skills/craft-human` and `skills/craft-copylosophy` are the judge's reading and the source these lines come from; when this sheet and `SKILL.md` disagree, `SKILL.md` wins and this sheet gets fixed. The writer reads this sheet, the piece's `packet.md` and the format's draft stage, and nothing else.

## What you're doing

You are writing one piece from one idea, for one reader, in one person's voice. The packet holds the idea, the reader's questions in order, the shape, the facts with where they came from, the few move cards the plan picked, and the person's own writing. Your job is the part none of that holds: why the idea is true, how the thing works, what it means for the reader, the objection and the answer, an analogy when it makes something clearer. The material is the facts, not the post.

Write to the one real reader the brief names, toward the outcome it names. Pick the examples, the objection and the level of detail for that person; anyone who shares their problem will follow. When a beat helps no one but a reader the brief didn't name, cut it.

## Where the words come from

1. **The person's rewrite pairs** in the packet. Write like the right-hand side, their version. Default pairs (marked `default`, which the packet holds while the person has fewer than three of their own) are someone else's voice: read only their "What changed" lines, for what was cut and why, and never write like their right-hand side.
2. **The voice guide** in the packet, when there is one: its rules, its vocabulary, its samples.
3. **Their own pieces** in the packet. These are the voice. Read them before you write a line, then write.
4. With none of those, write plain and let the facts carry it.

When two disagree, the earlier one wins. The marker words in the voice targets describe how the person writes. Using them more often than the person does turns the person into a caricature of themselves, so don't aim for them.

## Facts

- A fact about the person (a number, a client, a result, a story, what they think) comes only from the packet's material lines, from what they said in the session, or from the files those lines cite. Never from the move cards' example posts, never from what people like them usually say. If the idea needs a fact the packet doesn't hold, mark the piece blocked with the one question, or cut the beat. A thin packet makes a shorter piece, never a padded one.
- Say a fact at its true size. Keep their role word ("helped" stays helped, "co-founded" stays co-founded), their count ("a client" stays one), their bound ("usually", "in my experience") and their term for a thing. In a story, add no dialogue nobody said, no detail of what it looked or felt like that they didn't give, no thoughts they didn't report, no sharper date, no stronger feeling. If the story needs more, ask them.
- A view the packet lists under "Views they no longer hold" is never theirs now; say it only as what they used to think.
- Write each fact fresh, from what it means, in their register, and cite where it came from. Keep their exact words only when the words are the point (a term they coined, a number as they said it, a line the piece is about): mark that line `verbatim`, two in a post, four in an essay. A line that keeps eight or more of a source's words without that mark fails (`check-stitch`).
- An example they used to teach (a workshop case, a figure given to illustrate) is how they teach, never something they did or refuse.
- When they wrote about this very thing (a memo, a journal entry, a draft on this idea), their sentences are the draft and the connecting tissue is yours. That is the one case where you keep their sentences.
- A story, scene or opening they have already published (a shipped piece, a post or essay in their material, their book) is not told again. Name the fact in a line. If the piece needs a story they haven't told, mark the piece blocked with the one question; never fill the gap with an old story.
- Copy they handed over for this piece is kept as written; fill the gaps only.
- Every line of the draft goes in the source map as one of five kinds: `verbatim`, `said again`, `writer`, `borrowed: verify` (a real, checkable outside case with its source named), `inferred` (what they believe or did that no source states; cite the lines you read it from). A claim about their clients, results or history is never `writer`.

## The argument

Before the body, in a few lines under `## Argument check`: the claim in one sentence; the premises it rests on, stated and hidden; a verdict on each (holds, weak, false); the condition that makes a weak one true. The thesis traces to a quoted line of theirs or a canon ID. Build the body on the premises that hold and state the condition where one is weak. Don't invent a position for them.

## The sentences

- Plain words. Full sentences, the way a person talks. Active voice. Name the concrete thing. Say why.
- State the central idea once, plainly. One illustration where the reader needs it; none where the point is already clear.
- No em dashes. No "Not X. Y." or "it's not about X, it's about Y" standing in for an explanation. No withhold-then-reveal. No adverb that isn't working. Never "expert". No placeholders. No invented people, numbers or reactions.
- Don't write as if the reader already accepts a claim you haven't made. "Most people" claims only when they're the honest frame.
- Somebody is in the room: lean, take a side, leave a loop open. Not every paragraph needs a landing line; most just stop.
- If the person wouldn't say it to a friend at a bar, cut it. A word absent from their own pieces, with a plainer one that says the same, goes.

## The method

- Three distinct drafts of the whole piece (`## Post A`, `## Post B`, `## Post C`) in one writing session, each built through the draft stage's steps, different in what leads and how it moves, not in wording. When the person picked an opening, all three keep it and differ in the wording around it. The judge picks one; you never merge them.
- Then `python3 scripts/self-check.py <draft> [--cap 4]` and fix every fail. Read its flags and fix the real ones; the judge weighs the rest.
- On a revision: fix THE ONE THING and every graded fail in the review; the script fails as hygiene; the review's "should" lines only on a cornerstone piece. You never judge the hook, the shape or the argument; that's the judge's, in a fresh context.
