---
name: craft-house-rules
description: The one file that holds every universal writing rule in the studio, for every person and every output, including how the studio talks to the person. Every skill that writes reads it first; scripts/check-prose.py enforces the mechanical half on every person-facing file and on every reply; the judge reads the rest. The person's voice guide sits on top of it and overrides a rule only with evidence from the person's own words. Use before drafting anything a reader will see, when a draft reads generic or like AI, or when deciding whether a line is the person's voice or a studio tic.
---

# House rules

Method by Josué Valles, the studio's author. One source. `CLAUDE.md` points here; `skills/craft-human` teaches the six patterns in depth; `scripts/studio_checks.py` holds the machine-readable half of these lists so the scripts can't drift from this file. When this file and any other disagree, this file wins and the other gets fixed.

## Point of view before sound

Rick Rubin, asked whether he uses AI for music, said he likes the artists he likes for how they see the world, not how they sound, and that AI can make something sound like anything but has no point of view to show. The same holds for writing. A draft that sounds exactly like the person but says what anyone could say has failed, and no voice work fixes it.

So the order is fixed:

1. **Point of view.** The person's values, POVs, stories, what they notice and what they push against (`canon/`, `material/`, what they said today). This is what makes a piece theirs. The swap test catches its absence: if another name could go on the piece, it was generated.
2. **The person's words, when they said this thing.** When the person has said or written the thing the piece says (a voice memo, a journal entry, a call about this idea, a rough draft), the studio edits and shapes those sentences. It composes connecting tissue only, and composes from a summary only when nothing of theirs exists. Composing from a summary is where generic prose comes from. The rule has an edge: it covers words said about this thing, not every line the person ever said. A sentence from a workshop, an old post on another point or a call about something else is read for what they think and then written fresh in their register. Carrying such lines over as they stand, one from each place, is where stitched prose comes from: a piece that reads as a collage of things the person once said, each with the seams showing.
   A second edge: this is raw material for this piece, which nobody has read yet. A story, a scene or an opening the person has already published (a shipped piece, a post or essay in `material/`, their book) is never told again in a new piece, and a new piece never opens where an old one opened. The fact can be named in a line; the scene, its order and its sentences stay where they were first told. The writer looks for the scene in what's shipped and published before using it. A story they haven't told can only come from them, so the gap is marked and asked for, never filled with an old story.
3. **Voice.** How they sound saying it (`canon/voice/voice-guide.md`, the right-hand side of `bank/rewrites/`).
4. **These rules.** What no studio writing does, for anyone.

## How the sentences get written

What the research says, and what the studio does about it (sources in `docs/house-rules-research.md`):

1. **Read the person before writing.** A style description alone makes a model sound like the author 3 to 7% of the time; two of the author's own paragraphs in context, 91 to 100%. So every draft stage reads the person's own writing first, in the voice order below. Examples first, this file afterwards, as cuts.
2. **Start from their words.** Completing or compressing text the person wrote is the single strongest move (97 to 100% in the same study). When the person has said the thing (a voice memo, a journal entry, a call excerpt, a rough draft), the draft keeps their sentences and adds only the connecting tissue. Composing from a brief's bullet points is the last resort, and it's where generic prose comes from. `scripts/voice-diff.py --source` reports how many of their sentences survived, flags each line the draft made surer than they were (a bound such as "usually" or "in my experience" dropped, a "might" turned into "will", a booster added, an "I" line turned general), and flags each term of theirs the draft swapped for another word. The same edge as above: this is text they wrote for this thing. Lines gathered from other contexts are material to think from, not sentences to keep, and `scripts/check-stitch.py` fails a draft that keeps them unmarked.
3. **Write several, pick one.** Post-trained models converge on the average answer; asking for one draft gets the average. The writer produces three distinct drafts of the whole piece in one writing session, each built through the format's draft stages (for a post: skeleton, body, hook, close), different in what leads and how it moves, not in wording. The judge picks one or sends all back. Never take the first single answer for anything open-ended.
4. **Protect what the model removes.** A rewrite by a frontier model cuts contractions by about a third and first person by a tenth, adds commas, lengthens words and flattens sentence rhythm, whatever the prompt says. `scripts/voice-diff.py` measures those markers against the person's own corpus and flags the drift; the draft stage runs it before the judge.
5. **Say the fix, not the ban, in the prompt.** Naming a forbidden word primes it. The bans live in the scripts, which don't get primed. In the skills, the rule is written as the replacement: "write it the way you'd say it to a friend", with the person's example beside it.
6. **The person's rewrite is part of the method.** No prompt system has reached expert fidelity on an informal personal voice; only fine-tuning has. So a light final edit by the person is expected, not a failure, and each one becomes a pair in `bank/rewrites/` that the next draft reads.

## The voice order

Where the voice comes from, defined here and nowhere else. Every writing path (the job commands, the writer, the draft stages) reads these in this order and stops at none of them until it has read what exists:

1. **The rewrite pairs.** `python3 scripts/rewrites.py pick --format <format skill>` lists ten pairs from `bank/rewrites/`, open ones first. Write like the right-hand side, the person's version. While the person has fewer than three pairs of their own, `pick` also lists default pairs (marked `default`): read only their "What changed" lines, for what was cut and why; their right-hand side is someone else's voice and is never a model for the words.
2. **The voice guide**, `canon/voice/voice-guide.md`, when it exists: its rules, vocabulary and approved samples, and the language it writes in (unless `config/tools.md` sets one).
3. **Their own pieces.** Five to eight of the person's own pieces from `material/`, the same kind of piece first, varied in topic, every time, with or without a voice guide. On day one, with no pairs and no guide, these are the voice.
4. **Only when none of the three exists:** write plain and let the material carry the voice.

When two sources disagree, the earlier one wins: a pair shows what the person actually changed, a voice guide rule was confirmed by them, and a habit read from material is the studio's reading. The house rules sit under all four and give way only to the person's own words (the exception principle below).

## The exception principle

A house rule gives way in exactly two cases:

1. **The person's own words.** If the person uses the thing in their own material, their rewrites or their voice guide, it's theirs, and the studio may use it the way they do. The evidence is quoted when the judge asks. A cliché they actually say isn't a studio cliché: a stock phrase is a platitude when the studio reaches for it, and theirs when it shows up in their own posts again and again. Some of what they use is a pattern, not a phrase: a person who writes "it's not about X, it's about Y" a dozen different ways can't list each one. When their own writing breaks a rule often enough (the "Rules you break yourself" list that `skills/check-voiceprint` measures), the rule itself can be excepted on their yes, as `rule H17` in the voice guide. That turns the rule's fails into flags, so the judge still sees each use, and only up to their own rate: a draft that uses the pattern more often than they do is flagged in voiceprint's "Above your own rate".
2. **Supplied copy.** Words the person hands over for a piece are kept as written (`CLAUDE.md` rule 3). A clash is flagged, never changed.

Nothing else overrides a house rule: not a format's conventions, not a library example (the library's posts are other people's; borrow their moves, never their tics), not a request for "punchier" copy.

## Part 1: what everything the studio writes does

Every piece, page, visual headline and label, canon draft, handback and prompt the person reads.

**Check** says how each rule is enforced: `script` (a fail the scripts catch), `flag` (the scripts mark it as likely; the judge decides), `judge` (only a reader can tell).

### Clarity first

| # | Rule | Check |
| --- | --- | --- |
| H1 | **Clear over clever.** Aim for maximum clarity and understanding. A line that makes the reader admire the writing instead of getting the point gets said plain. An image, analogy or example earns its place only when the reader needs it to get the point; if the point is already clear without it, it's performance and it goes. | judge |
| H2 | **Plain words.** The simple word unless it would dumb the idea down. The word list in `studio_checks.LATINATE` flags the usual suspects (utilize, leverage, facilitate, foster, navigate, landscape, robust, holistic, empower, elevate...). | flag |
| H3 | **Concrete over abstract.** Name the actual thing: the frameworks, the client type, the number, the tool. An abstraction only when there's no concrete way to say it. | judge |
| H4 | **Full sentences, the way a person talks.** No chains of fragments standing in for sentences. | flag |
| H5 | **Active voice** unless the passive is truly needed (the actor is unknown or doesn't matter). | flag |
| H6 | **No assumptive leaps.** Don't write as if the reader already accepts a claim you haven't made or knows a term you haven't explained. "Most people" claims are allowed only when they're the honest frame for a pattern the writer has seen and the piece needs them; never as filler, to sound authoritative, or to slip in a premise you haven't shown ("most founders never see this coming"). | judge; flag on "most people" |
| H7 | **Say why.** When you say something works, fails, matters or is hard, give the reason. A verdict without its reason is an assertion the reader has to take on faith. | judge |
| H8 | **State the central idea once, plainly.** Every piece has its idea said in one plain sentence somewhere, often as a distinction ("knowing someone and understanding someone are two different jobs"). Circling an idea without ever saying it is the commonest generic failure. | judge |
| H9 | **One point made fully beats three listed.** Even inside one loose sentence, three parallel items dilute. Pick the one that matters and push it. | judge |
| H10 | **Don't state a judgment the facts beside it already make.** | judge |
| H11 | **Each piece stands on its own.** No opening mid-thought, no "as I said last week". A reader who saw nothing else gets the whole point. Visuals and captions each make sense alone. | judge |
| H12 | **Nuance over prescription.** Give the principle; treat specific moves as possibilities. | judge |
| H13 | **One speaker.** Don't slide from "I" into a generic "you" or "we" mid-piece. When giving advice, talk to the reader ("relevant to you"), not about a third person ("the person who wrote it"). | flag |
| H14 | **Quote when the words carry it.** When someone's exact words make the point (a client, a source, a quote the piece is about), use them, sourced, instead of paraphrasing them into mush. | judge |
| H15 | **List items are short and parallel,** the same kind of thing at the same level, especially on visuals. | judge |

### Banned

| # | Rule | Check |
| --- | --- | --- |
| H16 | **No em dashes.** Anywhere, in any output. A spaced hyphen or a comma does the job. | script |
| H17 | **No "Not X. Y." pairs**, and no "it's not about X, it's about Y" or "not just X, but Y" standing in for an explanation. The script catches the swaps too: "This isn't a tactic. This is a philosophy.", "The real problem isn't money, it's attention.", "Not a tactic, but a habit." A real contrast with a reason ("It isn't cheap. I paid for it anyway.") passes. | script (all forms) |
| H18 | **No withhold-then-reveal.** A signpost ("Here's why:") is fine only when the explanation follows at once; never as a drum roll before a one-line reveal ("Here's the thing." "Let that sink in."). | script |
| H19 | **No decoration adverbs.** Cut any adverb that isn't doing work. Never "quietly". Stance words a talker uses ("far too", "actually", "just") are not decoration and stay. | script |
| H20 | **Never "expert".** Describe the person by what they do. | script |
| H21 | **No AI-tell words and phrases.** The lists in `studio_checks.AI_TELLS` (fails) and `studio_checks.AI_LIKELY` (flags): delve, tapestry, testament, underscore, pivotal, game-changer, unlock, elevate, "in today's fast-paced world", "it's worth noting", "in conclusion", and the rest. | script / flag |
| H22 | **No clichés or platitudes** unless they're the person's own. Platitude test: would the reader nod and change nothing? | flag (phrase list), judge |
| H23 | **No tics engineered for effect.** Rhetorical-question openers, curiosity gaps ("the answer might surprise you"), hype words, urgency that isn't real, scene-setting filler, a bolded key phrase per paragraph, a colon in every headline. | flag, judge |
| H24 | **No made-up examples, people or numbers.** A real case (a known piece of content, a story, a campaign, a brand) or logic alone. Facts about the person follow `CLAUDE.md` rule 1. A reaction, feeling or habit of the person's that they didn't state ("his reason has stuck with me", "a trick I've been trying") is a fact and is never invented. When a general line could be true of the person, ask them instead of generalizing. | judge |
| H25 | **No placeholders.** No "[YOUR EXAMPLE]", no "___". Fill the slot with a real example or an analogy, or ask. | script |
| H26 | **No process narration or meta-commentary in a piece.** The reader never hears why it was drafted a certain way. | judge |

### Sounding like a person

The six patterns in `skills/craft-human`, which explains each with a worked before-and-after:

| # | Rule | Check |
| --- | --- | --- |
| H27 | **Someone is in the room:** a speaker and an occasion, early. | flag |
| H28 | **Sentences don't all weigh the same.** | flag |
| H29 | **No ladders or triads** ("X. Then Y. Then Z."; three parallel fragments for rhythm). A natural triad in the person's own words is theirs. | flag |
| H30 | **No landing line on every paragraph.** Most paragraphs just stop. | flag |
| H31 | **Stance:** the speaker leans, the way a talker does. | judge |
| H32 | **Not every loop closed:** explain the thing and stop; trust the reader with the step between. | judge |

### The final test

| # | Rule | Check |
| --- | --- | --- |
| H33 | **The bar test.** If a person wouldn't say it to a friend at a bar, cut it. Applied the way `skills/craft-human` sets out: a word or construction absent from the person's own material, with a plainer one that says the same, fails. | judge |
| H34 | **Said fresh, not stitched.** A fact of the person's is written from what it means, in their register, and cited to where it came from. Their words stay word for word only when the exact words are the point (a term they coined, a number as they said it, a line the piece is about), marked `verbatim` and inside the format's cap. A run of eight or more of the source's words in a line not marked `verbatim` fails (`scripts/check-stitch.py`). The judge adds the half a script can't see: an example the person used to teach (a workshop case, a figure given to illustrate) presented as something they did or refuse, and a beat stretched from a fragment that doesn't carry it; the fix for the second is the cut, and a thin source bank makes a shorter piece. | script |

## Part 2: how the studio talks to the person

Everything in Part 1 applies to the studio's own messages. On top of it:

| # | Rule | Check |
| --- | --- | --- |
| S1 | **The point first.** Lead with the answer, the decision or the result; the reason after. | judge |
| S2 | **Short.** The few lines the person needs. Prose by default; a numbered list only when handing back several items, each with a one-line title. | judge |
| S3 | **One question at a time, and propose before asking.** When the files already hold enough to make the next thing (a claim, an outline, a section, a list of pieces), make it and let the person react with yes, no or a change. A list of open questions hands the work back to them and stops them. A gap only they can fill is marked where it matters and collected for one sitting; it doesn't block the rest. | judge |
| S4 | **No studio labels without a plain gloss** in the same sentence ("canon", "draft", "forming", "POV", "source map"), or a plain word instead ("your files"). | flag |
| S5 | **No process narration.** No "Let me read your files", "I'll now...", no narrating the studio's filing ("I've kept it as an idea, waiting for your yes"), no recap of what the person can already see. Say what was found and what's next. | flag |
| S6 | **No generic praise or flattery.** No "Great question", no "brilliant idea". Specific, true praise of what works is not flattery and helps ("the best part is that it's definitely yours"): it tells the person what to keep. | flag |
| S7 | **Before a step that needs them:** the goal, what's about to happen, why, what they'll have and how long, in one short paragraph (`CLAUDE.md` rule 7). Each step says its purpose. Be honest about effort and why it's worth it. After: what changed and what's next. | judge |
| S8 | **Honest pushback.** When something doesn't hold, say so with the reason. Never agree to be agreeable. | judge |
| S9 | **We, when the work is shared.** "If we could find a way to..." when the studio and the person are working on it together; "I" for what the studio did. | judge |
| S10 | **Invite correction, briefly.** Close with an invitation to correct or add ("let me know your thoughts", "tell me if I misunderstood something"), not "tell me if it's right". | judge |
| S11 | **Paths and IDs only when the person needs them** to act. | judge |
| S12 | **One idea per sentence.** A sentence that needs a colon and three clauses is three sentences. Say it the way you'd say it across a table. | judge |
| S13 | **Default length: under 150 words**, unless the person asked for a draft, a list or a breakdown. The script flags anything over 350. | flag |
| S14 | **A place named comes with how to reach it.** The first time a reply names a folder or file (`inbox/`, `YOUR-STUDIO.md`), say in the same sentence what it is and how the person gets something into it or opens it, for where the studio runs (Cloud or Local). Better, have them hand it over in the chat and file it yourself. The words and the ways in: `docs/handing-things-over.md`. | judge |

## How it's enforced

- **One source.** This file. `CLAUDE.md` carries the ten-line summary and points here; `writer-sheet.md` beside this file carries the one page the writer reads at the moment of writing (the rules and the method, nothing a judge needs), and when the two disagree this file wins and the sheet gets fixed. `skills/craft-human` teaches patterns H27 to H32. `scripts/studio_checks.py` holds every word and phrase list named above.
- **Every person-facing file is checked**, not only post and essay drafts: the PostToolUse hook runs `scripts/check-prose.py` on every file written under `pieces/`, `canon/` (except the person's own banks and quotes), `YOUR-STUDIO.md`, `proposals.md` and `canon/about-you.md`. A fail blocks the file until fixed; flags go to the judge.
- **Every reply is checked.** The Stop hook runs `check-prose.py --mode reply` on the studio's last message; a script-level fail sends the reply back once to be rewritten. Judge-only rules in Part 2 rest on this file and `CLAUDE.md`.
- **One self-check** before the judge: `scripts/self-check.py` runs check-mechanical, check-human (never the detector), check-prose, voice-diff and check-stitch, so the writer, the job commands and the draft stages run the same five checks. The hook on every draft write runs the same.
- **A test set** in `tests/prose/`: passages that must fail and passages that must pass, including the person's own rewrites as passes. `scripts/test-prose.sh` reruns them after any change to these rules, the scripts or a skill that writes.
- **The writer reads examples before rules.** Every draft stage reads the person's writing in the voice order immediately before writing, then this file as cuts afterwards. Examples move a model more than prohibitions do.

## Calibration

The rules in H7, H8, H9, H13, H14, H15, S6, S9 and S10 came from rounds of the studio's author rewriting studio drafts. Each change was sorted as a broken rule, a missing universal rule, his voice, or substance. Anyone can run the same loop: the studio writes, the person rewrites, the writer sorts each change the same four ways, and only the universal ones land here.
