# Reading a report

What each part of a voiceprint report means and what to do about it. Read `methods.md` for where the measures come from.

## The verdict

| Verdict | Fit | What it means | What to do |
| --- | --- | --- | --- |
| Reads like you | 25% or more | The draft sits as close to the person's writing as a fair share of their own pieces, on word habits and on style. | Fix any flags below, then move on to the judge. |
| Close | 10% to 25% | It matches on the whole, with a few habits off. A normal result: some of the person's own pieces score here. | Fix the top flags once, in the person's way. |
| Off | under 10% | At least one of the two measures puts it further out than nearly all of the person's own pieces. | Look at the flags. Usually the draft is missing a few strong habits (contractions, sentence variety) or carries the studio's (long words, -ly adverbs, AI-typical words). Revise once. |
| No verdict yet | | Too little of the person's writing, or the tool can't tell their pieces from the comparison set at this length. | Use the flags, tell the person plainly, and grow the samples: more of their writing in `material/`, and more rewrite pairs in `bank/rewrites/`, whose studio side joins the comparison set. |

**Fit** is the share of the person's own pieces the draft is at least as close as. It's computed twice, once on word habits and once on style, and the report takes the lower number, so a draft can't pass on one and hide a miss on the other. The line under the verdict shows how the person's own pieces score the same way, which is the scale to read the draft against.

**Separation** is how often, at the draft's length, the tool can tell the person's pieces from the comparison pieces. 50% is a coin flip. Below 70% the report gives no verdict. Above 85% it calls the reading reliable. This only holds as far as the comparison set looks like the real competition: other writers in the person's formats and the studio's own drafts.

**Impostor test.** The share of 100 random trials in which the draft sat closer to the person's pieces than to any comparison piece, with the same test run on the person's own pieces and the comparison pieces for scale. It looks at word habits only. When it says yes and the verdict says off, the draft is on the person's topics but not in their style.

## What to change

Each flag names a measure where the draft falls outside the person's usual range (the middle 70% of their pieces, plus a margin), the draft's value, their range, and one plain fix. Flags come in order of how far outside the draft falls.

Fix them in one pass, in the way the person would say it. A flag says what's missing, never how to fake it. "You contract more than this draft does" means contract the words they'd contract out loud, not sprinkle in contractions until the number moves.

Ignore a flag when the piece calls for it: a list post will have more one-line paragraphs than an essay, a story will have more "I". The comparison is with the person's usual writing across formats, so format-driven flags are expected.

## The measures

| Measure | What it counts | Why it matters |
| --- | --- | --- |
| Average and typical sentence length | Words per sentence; a line break ends a sentence, as in a post. | One of the steadiest habits a writer has. |
| Sentence length variety | How much sentence lengths spread around their average. | People mix short and long. Even lengths are one of the clearest signs of machine text. |
| Short and long sentences | Share of sentences of 7 words or fewer, and of 25 or more. | Shows where the variety comes from. |
| Words per line or paragraph; one-sentence lines | How the text is broken up on the page. | Moves with format as much as with the writer. Compare like with like. |
| Average word length; long words | Letters per word; share of words with 9 or more letters. | Long words are where the studio's habits creep in ("facilitate" for "help"). |
| Vocabulary range | Moving-average type-token ratio over 50-word windows. | Varied wording can mean a thesaurus at work; plain talkers repeat words. |
| Contractions | it's, don't, you'll, per 100 words. | Spoken writing contracts. AI text often doesn't. |
| I, we, you | Pronoun rates per 100 words. | Who's in the room: a speaker, a team, a reader. |
| Openers | Share of sentences starting with And, But, So or Because, and with I. | Conversational writing starts sentences the way people talk. |
| Punctuation | Commas, questions, exclamation marks, colons, semicolons, dashes, ellipses, parentheses, quote marks, per 1,000 words. | Each writer has a few marks they lean on and a few they never use. |
| Capitals for emphasis | Words in all capitals, per 1,000 words. | A habit some people have and most don't. |
| Numbers | Figures written as digits. | Moves with topic; read it with the piece in mind. |
| -ly adverbs | Words ending in -ly that work as adverbs, per 100 words. | Extra adverbs are a common studio habit. |
| AI-typical words | Words often reported as overused in AI text (delve, landscape, leverage, seamless, unlock and others). | A flag, not proof. The house rules hold the full lists. |

## Words

The writer targets list the person's **marker words** (words they use in far more pieces than other writers do) and **anti-markers** (words others use that they rarely do). Small words are the reliable part: nobody chooses "so" or "really" on purpose. Other marker words are often topic words; the person decides which are habits.

## Rules you break yourself

The house rules fail or flag patterns that mark machine-written text, and some people use one of them in their own writing all the time. The profile runs the same checks a draft gets over each of the person's pieces and records, for each rule, how many uses, the rate per 1,000 words, the share of their pieces that use it and up to three quotes. A pattern in at least 30% of their pieces, or more than twice per 1,000 words, and in at least three pieces, is listed under "Rules you break yourself". A use is one sentence that shows the pattern.

Each listed rule is a question for the person, asked through `proposals.md` (kind `voice rule`, with the counts and quotes): "You write 'it's not about X, it's about Y' in 5 of your 6 pieces. Is that yours?" A yes goes in the voice guide's "House-rule exceptions" as `- rule H17: "<their line>" (<source>)`. From then on the scripts flag each use of that rule instead of failing it, so the judge still sees every one. For the rules matched word by word (a longer word, an adverb, machine vocabulary, the word "expert"), the list names the words they use, and those words make better phrase exceptions than the whole rule.

The lines below the list (patterns used now and then) stay under the house rules. A pattern the person uses once in fifty pieces isn't a habit, and the studio doesn't write it for them.

In a score report, "Above your own rate" holds every listed pattern to the person's rate: a draft that uses one at least twice and more often than most of their pieces do gets a line, excepted or not.

## The rewrite patterns

`patterns` reads every pair in `bank/rewrites/` and lists measures that moved the same way in most of the person's rewrites, and words they kept adding or cutting (counted net: rewrites that added a word minus rewrites that cut it). Treat each line as a question for the person: "In 7 of 9 rewrites you added contractions. Is that a rule for your writing?" A yes becomes a voice-guide proposal with the counts as evidence. A pattern that would hold for anyone goes to `studio-notes.md` as a candidate house rule.

## Building a good comparison set

The comparison set decides what "different" means, so it decides what the tool can see.

- **In `bank/voiceprint/others/`,** as files or a CSV with a text column. Never the person's own writing.
- **Same formats as the person.** Posts against posts, essays against essays.
- **Similar topics,** so topic words don't do the work that style should.
- **The studio's own drafts.** These matter most, because the question the studio asks is whether a draft sounds like the person or like the studio. The studio's side of every pair in `bank/rewrites/` joins the comparison set on its own, read in place.
- **At least 20 pieces,** more for short formats.
