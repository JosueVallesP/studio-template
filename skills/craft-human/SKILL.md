---
name: craft-human
description: The standard that makes studio writing read like a person talking, under whatever voice, tone and register the person has. Six patterns that mark text as machine-written, what to do instead, and a worked before-and-after. Every writer reads it before drafting; check-human tests drafts against it. Use when drafting anything a reader will see, or when a draft "reads like AI".
---

# Writing like a person

This standard is part of `skills/craft-house-rules` (rules H27 to H32), which holds every universal rule and the drafting method; read that first. One thing comes before any of this: point of view. A draft that passes all six patterns but says what anyone could say has still failed, because what makes text alive is how the person sees, not how they sound.

This standard sits under every voice guide. A voice guide says how one person sounds. This says what every person's writing has that generated text doesn't, and it applies to every draft the studio makes, for every person, before the voice guide is applied on top.

The goal is not to beat a detector, and the studio doesn't try: the detector reads a piece at the two points `CLAUDE.md`'s detector paragraph names, and its label is reported, not chased. In the studio's runs so far, a draft the model wrote has scored as model-written whatever its patterns; in one run, a post assembled from the person's own lines scored 93% AI with no pattern flagged. The goal is text a reader takes as one person talking to them. Detectors like Pangram are one more reading of the draft, and `check-human` records the score when a key is available, but the standard is the six patterns below. A draft that passes them reads human whether or not anyone runs a detector.

## The six patterns

Generated text has a shape. Six features of that shape show up together, and removing them is most of the work.

### 1. Nobody is in the room

Machine text has no speaker and no occasion. Nobody is saying it, to nobody, for no reason that's happening now. A person writes because something prompted it: a question they keep getting, a thing that happened this week, an argument they just had.

Do instead: put the speaker and the occasion in, early. Who is talking, to whom, and why now. "People often ask me why..." is a person. "AI can only repeat what you believe" as an opening line is a billboard.

### 2. Every sentence weighs the same

Generated sentences run eight to fourteen words, declarative, same shape, same weight, one after another. The rhythm is a metronome. People write one long run-on with an "or" in the middle and then a two-word line.

Do instead: let sentence length vary the way it does in speech. A long sentence that carries several things loosely, then a short one. Don't engineer it; write the thought the way you'd say it and the variation comes.

### 3. Ladders and triads

"So people tweak the tone. Then the voice guide. Then the prompt." Three parallel fragments climbing to a point. Also: lists of three for rhythm, paired fragments, "X. Y. Z." sequences. These are the single most recognizable machine move, because they're what a model learned good writing looks like.

Do instead: say the three things in one loose sentence with "or" and "and", the way a talker does. "So people spend hours on the tone or the voice guide or the prompt." If three things need listing, list them as a list.

### 4. A landing line on every paragraph

Each paragraph ends on an aphorism that closes the loop: "That average is what generic means." "Tone work on an empty foundation just makes empty drafts sound nicer." Every paragraph becomes a small speech with a button on it.

Do instead: let most paragraphs just stop and move on. A person explains one thing and goes to the next. One landing line in a whole piece can be good; one per paragraph is a tell.

### 5. No stance

Machine text states; it doesn't lean. People lean on words: "actually believe", "far too long", "a bit off", "not necessarily", "I'd say", "to be honest". These carry the speaker's attitude toward what they're saying, and that attitude is most of what makes text sound like someone.

Do instead: let stance words in where a talker would use them. This is where the standard meets the writing rules' ban on adverbs that don't do work. The two agree once you see what each is for: the ban is on decoration ("truly", "deeply", "quietly", "incredibly"), words that dress up a claim. Stance words do a job: they tell the reader how hard the speaker is leaning. "Far too long" is a stance; "incredibly important" is decoration. Keep the first kind, cut the second.

A related point on signposts. "Here's why:" and "My answer boils down to this:" are how a talker sets up an explanation. They're fine when the explanation follows at once. What stays banned is the withhold-then-reveal use, where the signpost replaces the explanation or delays it for effect ("Here's the thing." followed by a one-word reveal).

### 6. Every loop closed

Generated text explains everything, qualifies everything and leaves no gap. The logic is airtight and the reader has nothing to do. People explain one thing at a time, skip steps the reader can fill, and leave a thread hanging.

Do instead: explain the thing you're explaining and stop. Trust the reader with the step between. Don't pre-answer every objection; answer the one that matters and leave the rest.

A limit the argument needs is not a closed loop. When copylosophy (or the LinkedIn judge's check 20) requires the post to state a condition ("that's one company and one comparison"), that sentence is honesty, not over-explaining, and never counts toward this pattern.

## The tells that survive a cleanup

A draft can pass the six patterns and every word list and still read as generated, because the model swaps one set of habits for another. `scripts/studio_checks.py` flags these (`second_gen`), as notes for the judge, never fails:

- **Staged sincerity:** "Let me be honest:", "Honestly?", "Real talk", "The hard truth is" opening a line. State the fact flat. Inside a sentence, "honestly" can be stance; the flag is only for the frame.
- **Staged rhythm:** "No X. No Y. Just Z.", "All the X. None of the Y.", "Stop X. Start Y.", a negation list ("no setup call, no templates, no waiting"), a one-word paragraph. A list of three concrete, named things is fine.
- **Colon reveals:** "The result: clients stayed." Say it as a sentence ("The clients stayed").
- **Weasel sources:** "studies show", "research suggests", "many argue". Name the source or cut the claim.
- **Hedges:** "could potentially", both-sides balance ("while X offers benefits, it has challenges"), "despite these challenges".
- **Shapes from current models:** a parenthetical aside every sentence or two, a bold lead-in on every bullet, sentences chained with semicolons, an opening "-ing" clause ("Leveraging our data, we...").
- **A framework the person never named,** wisdom-shaped sentences nobody would disagree with, every section the same length. The judge reads for these; the script can't.

**Vary the fixes.** If every reveal becomes ", because..." and every negation list becomes "There's nothing to X", those are the new tics. Fix each one the way the sentence needs.

These lists age with the models. They were last checked on 2026-10-27; the librarian's studio-notes pass rechecks them about every six months against the person's rewrite pairs.

## What not to do

Don't plant mistakes. Typos, odd spacing and "5 mins" help a detector score and read as planted the moment a reader notices. The six patterns are the work; cosmetic flaws are not.

Don't add stance words to a draft that has none as a finishing step. They come from writing the thought as speech in the first place. If a draft needs stance words bolted on, the draft was written the machine way and needs to be said again.

Don't break the voice guide to pass this standard. The standard is under the voice. A person who writes in short clean sentences still varies their length; a formal person still has an occasion and a stance.

## A worked pair

The same idea, written twice. Read them against the six patterns.

Before:

> AI can only repeat what you believe. If you've never written it down, it repeats the internet.
> So people tweak the tone. Then the voice guide. Then the prompt. The drafts still read like someone else wrote them.
> I understand why. Those are the fixes within reach. You can rewrite a prompt in five minutes. But every one of those fixes changes how a sentence sounds, and none of them gives the AI anything to say. You end up with polished sentences sitting on top of nothing.
> What's missing is the foundation. Your values. Your positions. The things you believe are true about your field that most people in it get wrong.

After:

> People ask me why their posts still read like everyone else's when they draft them with AI. I usually give the same answer:
> AI can only repeat what you actually believe. If you've never sat down and written that out, it'll fill the gap with whatever it finds on the internet.
> So people spend hours on the tone or the voice guide or the prompt, and the drafts still read a bit off.
> Here's why:
> Those are all fixes to how a sentence sounds. You can rewrite a prompt in five minutes, but it won't change what the post says, and that's the part that was missing.

What changed: a speaker and an occasion arrived (pattern 1). The sentences stopped weighing the same (2). The "tone. Then the voice guide. Then the prompt." ladder became one loose sentence with "or" (3). The landing lines went (4). "Actually", "a bit off", "I usually" came in (5). The explanation got looser and left the reader a step to take (6). Note that "most people in it get wrong" in the before version also breaks the writing rules on their own terms.

## Signposts

"Here's why:", "Here's the thing:", "So:" are things a talker says before an explanation. They stay when two things are true: the explanation follows at once, in the next sentence, and the person would say it out loud at that point. They go when they're a drum roll before a line that doesn't explain anything (a landing line, pattern 4), or when they turn up in every piece in the same place, which makes them a template. One per piece at most, and never the same one twice in a row across pieces. The test is the specimen above: "Here's why:" works there because the next sentence answers it.

## How to apply the bar test

The house rules end on a principle (H33): if a person wouldn't say it to a friend at a bar, cut it. Here is the check that applies it the same way every time. A word or construction fails the bar test when it is absent from the person's own material and voice samples (`material/`, the approved samples in `canon/voice/voice-guide.md`, the right-hand side of the pairs in `bank/rewrites/`) and a plainer one exists that says the same thing. The judge quotes the line, names the plainer word or construction, and marks it a fail under the writing rules. A word the person does use passes, however formal it looks; a word with no plainer equivalent passes too.

## How the studio uses this

- Every `fmt-` skill's draft stage reads this before writing and says the draft out loud in its head before putting it down.
- `check-human` reads every draft for the six patterns and marks the lines. Its mechanical half is `scripts/check-human.py`, which measures patterns 1 to 4 and the decoration adverbs; the judge reads patterns 5 and 6. The script's counts are evidence for the verdict rule below, not fails.
- A draft that shows three or more patterns, or one pattern in three or more places, gets check-human's `fix`, which the editor's gates table grades revise, whatever else it gets right. Two patterns, each in one or two places, pass.
- The voice guide is applied after this standard, never instead of it.
