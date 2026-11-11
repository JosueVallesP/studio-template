---
name: dsn-sequence
description: Sequencing a carousel or spread, when slide one lands and the rest merely continues, or judging a deck's shape. Gives the sequence, its turns and a per-frame budget.
---

# Sequencing a multi-frame piece

This skill decides the order of frames in a piece a reader moves through one frame at a time: a carousel, a deck, a spread. It covers what each frame has to do to earn the next one, which frames are built by hand and which are refilled from a template, and how the copy and pixel budget divides across a set rather than across a single canvas. The single idea underneath it is that a sequence is not a stack of good frames, it has a shape, and the common failure is a strong first frame followed by frames that continue rather than progress. Continuation reads as competence while the reader stops learning anything, which is why nobody reports it as a problem and the deck simply underperforms.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file was tested on readers, and every judgement in the material behind it is a designer's own eye rather than an outcome. Rules marked **(thin)** rest on a single account and should be treated as one person's house style rather than as a standard.

Two further limits matter more here than the usual ones. First, the mechanics of holding many frames together come from print, where a reader sees two facing pages at once and can look back for free. A carousel reader sees one frame, then the next, seconds apart, and cannot easily return. Every instruction about seams, open loops and the closing frame is carried across that gap rather than observed in the format it is applied to. Second, the question this skill exists to answer, whether frame four says something frame three did not, is not a question the print material asks at all; it sequences the reader's eye, not the progression of meaning. Treat the eye-level instructions as better supported than the meaning-level ones.

The pixel arithmetic in the Applied section is checkable, but the premise under it is an estimate of how a phone renders a feed rather than a measurement of one.

## What this skill is for

- sequencing a carousel before any file is opened
- diagnosing a deck whose first frame works and whose middle goes slack
- deciding which frames are built by hand and which are refilled from a template
- building a body template a crew or an agent can refill without the set coming apart
- computing how much copy a given frame count can actually carry on a given canvas
- judging a finished deck and saying where its shape breaks

This skill governs only what happens between frames, and assumes each frame already stands up on its own. See "Where this skill should lose" for what owns the inside of a frame.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Frame.** One canvas in the set. One carousel slide, one page, one screen.

**Seam.** The gap between one frame and the next, crossed by a swipe.

**Turn.** A change the frame causes in what the reader knows, believes or expects. A frame turns if it forces a change, reinforces a change that just happened, or shows an attempt failing. Written as "from X to Y", about the material and never about the wording.

**Currency.** The kind of thing a sequence trades in. Three of them: **information**, which ends in a reveal; **position**, meaning a belief or stance, which ends in a shift; **obstacle**, meaning something external, which ends in a result.

**Promise, body, payoff.** The three objects a sequence is made of. The promise is what the first frame says will change. The body is what accumulates. The payoff is the delivery. All three have to be in one currency.

**Want.** An ending that leaves something open rather than closing it, so the reader is still carrying the piece.

**Open loop.** An unanswered question a frame leaves deliberately, which is the reader's reason to cross the seam.

**Affordance.** A visual instruction to continue: an arrow, the word "swipe", a progress dot. Separate from the open loop, and usually removable, because position in a set already tells a reader there is more.

**Magnitude.** How large a turn is, sorted as minor, moderate or irreversible. A sorting instrument, not a measurement. **(thin)**

**Template.** A single frame structure, with fixed margins, fixed type sizes, a fixed dominance order and named fields, that someone other than its author refills with new content.

**Hand-tuned.** Built once for its own content, by eye, and not refillable. The opposite of templated.

**Rank.** The reading order inside one frame. Rank 1 is what a reader sees first, rank 2 second.

**Dominant element.** The largest-weight thing in a frame, which carries rank 1.

**Footprint.** The bounding box an element occupies, in pixels, including the space it visually claims.

**Live area.** The canvas minus its margins. Everything load-bearing sits inside it.

**Margin.** The clear band between the canvas edge and the live area.

**Column and gutter.** The live width divided into equal vertical bands (columns) separated by equal gaps (gutters). Element widths snap to whole columns plus the gutters between them.

**Measure.** The length of one line of text, counted in characters including spaces. Not the width in pixels.

**Leading.** The distance from one text baseline to the next, stated as a multiple of the type size. Leading of 1.4 on 51px type puts baselines 71px apart.

**Downscale factor.** How much smaller the asset renders than the file it was built in. A 1080px-wide asset in a feed column of roughly 360 device-independent pixels is a 3x downscale, so a 36px element renders as 12pt.

**Strip render.** All frames of the set laid out in one row at 25 percent, read as a single image. It turns the set's density pattern into something visible at a glance.

**Overlay.** Body frames stacked on top of each other at partial opacity, so anything that moves between them shows as a doubled edge.

**Grey-boxing.** Replacing every image with a flat grey rectangle of the same footprint, so a layout is judged on structure rather than on photography.

## The principles

Six rules. Each names the test that checks it; the tests are in the table below.

1. **Build every middle frame so that it exists because of the one before it.** A set whose treatment changes frame to frame denies the reader the continuity that lets them read a frame without relearning how, and a set whose treatment holds but whose content restates gives them continuity with nothing to spend it on. The failure is the second one and it is invisible from inside any single frame. Checked by the continuation test.

2. **Write every frame's turn as "from X to Y" before you build it, and cut any frame you cannot write one for.** A frame that forces no change, reinforces none and shows no attempt failing is an item in a list, not a step in a sequence. Run this first in any diagnosis, because it is the one question a rewrite cannot answer: new wording can make a frame feel like it moves without changing what moved. Checked by the turn ledger, then the bait check on any repair.

3. **Pay the promise, the body and the payoff in one currency.** A body accumulating evidence under a closing frame that asks for an identity change has paid out in a currency it never collected. When a deck reads flat and no individual frame is bad, this is almost always the fault, and the repair is three lines on frame 1 rather than anything in the middle. Checked by the alignment diff.

4. **Vary the magnitude of the turns on purpose, rising toward the payoff.** Uniform intensity cancels itself: three equal turns in a row read as boring even though things are technically happening. The mechanism underneath it is density alternation, keeping breathing space next to anything dense so the eye has somewhere to rest, and setting rhythm by alternation rather than by making every frame loud. **(thin)** Note that the density account paces one spread taken in at a single glance, so applying it to frames seen seconds apart is carried across the seam rather than observed. Checked by the magnitude profile.

5. **Leave one open loop on every frame, and let position supply the affordance.** A frame owes the next one a reason to arrive, and the reliable version of that is an unanswered question rather than an arrow. Cut the copy down to the amount that creates interest and no more. Then delete every affordance, read the deck, and add back only what position does not already supply. **(thin)** Checked by the stop test, and by the count and affordance inventory.

6. **Use one structure for the whole set and let the content supply the variation.** A heading size is a property the set keeps rather than a decision remade per frame, so it stays fixed even on the one frame where a larger heading would sit better; the cost of that single improvement is the reader relearning the frame. **(thin)** Held long enough, repetition becomes a language the reader can be trained in, so that a circle reliably meaning "a quote follows" turns the template from a constraint into an asset. **(thin)** Checked by the overlay test and the substitution refill.

## The sequence shape

Six positions. A nine-frame deck has one frame per position with the progression expanded; a twelve-frame deck expands the progression further and takes a second rest. The position map is a working structure for this format rather than an inherited one. **(thin)**

1. **Promise.** States what will change and in which currency, and stops a scroll. Hand-tuned.
2. **Turn.** Makes the promise cost something: it contradicts, complicates or prices what frame 1 offered. This position decides whether the piece is a sequence at all, and it is the one most often spent on an agenda, a definition or a credential, all of which continue rather than progress.
3. **Progression.** One to seven frames, one turn each, same currency, rising magnitude.
4. **Rest.** One deliberately sparse frame immediately before the payoff, built as the body template with fields removed rather than as a new layout. It survives refilling for exactly that reason, and a sparse frame built another way does not.
5. **Payoff.** The promised currency delivered, and the only legitimate place for the set's one structural break.
6. **Want.** Leaves something open rather than closing it. A piece whose job is replies takes the open want; a piece whose job is credibility resolves instead, because an audience that needs resolution to believe you reads withholding as evasion. Never both.

**One rest per five progression frames. (thin)** Below five progression frames there is nothing to rest from. Above ten, a single rest is swallowed by what surrounds it.

Frame count follows from the positions rather than from a target length: four fixed positions (promise, turn, payoff, want) plus one rest plus p progression frames comes to 5 + p. The six to twelve range this skill works in is a working range for the format rather than a derived figure. **(thin)**

## Hand-tuned against templated

Tension is tuned per instance and detunes silently under substitution: the same off-centre arrangement that reads as deliberate with one headline reads as a mistake with a headline two words longer, and nothing in the file reports the change. So anything someone else refills, including you next week and including an agent, is built for stability rather than for tension. This is a reasoned default rather than a measured finding.

- **Hand-tuned, outside the template: frame 1 only.** One exposure of under a second against a hostile feed, so it is the one frame that can carry unresolved tension. Built by whoever owns the hook.
- **Templated: frames 2 through the last, including the last frame's structure.** Stable balance, one fixed dominance order, identical throughout. The line on the last frame changes; its frame does not.
- **One break, at the payoff.** The rest frame is not a break, because it is the same structure with fields removed.

**If you are hand-tuning frame seven, the template is wrong.** Rebuild it against the real content range rather than the mock. Drive the template from the content and not the other way around: a template needing a vertical, a square and a horizontal image fails on a topic that produced only verticals, and the operator who discovers that is under deadline.

**The unit is the pair, not the frame.** Print treats the spread as the unit and asks at least one element to cross the gutter, so the two pages join into one thing. A carousel has no gutter, so the unit is the frame plus the swipe out of it, and two rules replace what the gutter was doing. **Judge every frame against its predecessor, never alone**, because a frame that reads well in isolation while repeating its predecessor's claim is the exact defect this skill exists to catch. And **carry one element across each seam**: a colour, a running count, a repeated shape, or a sentence finished on the next frame.

The licence to explore belongs to whichever frame appears once and so has nothing to be consistent with. In a set this size that is worth exactly one frame, and it belongs to the payoff.

## How to work

### Mode A: sequencing

1. **Write the sequence sheet before opening any file.** The promise in one sentence, its currency named as information, position or obstacle, the payoff, and the want. Nothing else happens until those four exist.
2. **Write one line per frame naming its turn as "from X to Y".** Any frame you cannot write this for is cut or merged. Run the turn ledger on the sheet rather than on a built deck, where a cut still costs nothing.
3. **Mark each turn minor, moderate or irreversible,** rising toward the payoff, with the rest frame at zero.
4. **Sketch three sequence orders as thumbnails on paper.** Placements, not designs. Three is a working minimum rather than a measured one **(thin)**; the reason to sketch at all is that it catches the problems you otherwise find with the file half built, in particular forgetting to leave room for a field and then dropping it in as an afterthought.
5. **Compute the frame budget for your canvas** before building anything: margins, live area, columns, the type scale, and the character ceiling per field. The Applied section does this on both canvases.
6. **Build frame 1 alone,** hand-tuned, to the rank and tension targets the single-frame skills set.
7. **Build the body template once,** from the longest real heading and the longest real body block you actually have, then derive the rest variant and the payoff break from it.
8. **Fill, then run the tests straight down.**

### Mode B: judging

1. **Ask for the sequence sheet.** With none, reconstruct the shape and say that you reconstructed it, because a reconstruction always reads tidier than what was built.
2. **Run the first-and-last read before looking at anything between.** Then the turn ledger, then the alignment diff, in that order. An alignment repair applied over a failed ledger produces a bait hook: a deck that feels like it moves and does not. Then the remaining tests in table order.
3. **Report what passes, what fails, and the smallest change that fixes each failure,** ordered by impact, naming the test behind each finding.

## Tests

In this order. Each returns a verdict decidable by a reader who has only this file.

| Test | Catches | Verdict |
|---|---|---|
| **1. Continuation** | A frame that continues instead of progressing | Delete one middle frame and read its two neighbours in sequence. Fail if the pair still states every claim the three stated. Cut or merge the deleted frame. |
| **2. Turn ledger** | A list wearing the shape of a sequence | One row per frame, marked F (forces a change), R (reinforces one that just happened), X (shows an attempt failing) or `none`, with a written "from X to Y" for every F, R and X. Fail if `none` rows outnumber the rest: the material is the problem and reordering will not fix it. Fail separately if there are zero `none` rows, because the ledger was not run honestly. |
| **3. Bait check** | A rewrite that re-signposts without changing anything | After any rewrite of frame 1, re-run the ledger and diff it against the previous one. Fail if no row's letter and no row's from-X-to-Y text changed. |
| **4. Alignment diff** | Promise and payoff in different currencies | Three passes, each with no knowledge of the others: name the currency from frame 1 alone, name what the body accumulates from the body frames alone, name what the ending pays out from the last frame alone. Fail unless all three name the same one of information, position, obstacle. Blindness is the mechanism: anyone who has read the whole deck harmonises the three by inference. |
| **5. Magnitude profile** | Uniform intensity | Label each frame minor, moderate or irreversible and read the column top to bottom. Fail on three identical labels in a row. Fail if the last progression frame is not the highest label before the rest. Fix by reordering, never by making a frame louder. **(thin)** |
| **6. Stop test** | A frame with no reason to leave it | For each frame n from 1 up to the frame before the payoff, cover everything after n and write down in one sentence the question n left unanswered. Fail at any n where you cannot write the sentence: the deck ends there whatever follows. |
| **7. Overlay** | Template drift | Stack the body frames at full size, each at partial opacity. Fail if the heading's first baseline, the left margin, the body block's top edge or the dominant element's bounding box moves by more than zero pixels between any two body frames. |
| **8. Substitution refill** | A template that is actually hand-tuned | Refill every templated frame with the longest and the shortest real string each field will carry, images grey-boxed. Fail if any field exceeds its computed character ceiling, overflows the live area, or needs a size change to fit. |
| **9. Strip render** | A flat set, and decoration mistaken for structure | Lay every frame in one row at 25 percent. Fail if the row reads as even density with no visibly sparse frame. Fail separately if anything you called load-bearing has disappeared, because at 25 percent a 36px element is nine pixels tall and was never load-bearing at stress either. |
| **10. Want check** | The wrong ending for the job | Read the last frame alone and write "closes" or "leaves a want". Then write which one the piece's job needed. Fail on a mismatch. Fail if you wrote both. |
| **11. Count and affordance inventory** | A false count, and decoration doing the content's work | List every stated number and every arrow, dot and swipe label. Fail if a stated count differs from the actual frame count by any amount. Then delete every affordance, read the deck, and fail for each one whose absence you cannot notice. |
| **12. Floor check** | Elements nobody can see | Measure every load-bearing element in the working file. Fail below 36px. Fail below 48px if the piece must survive the 4x stress case, since 36px renders at nine points there. |
| **13. Recital** | The shape you actually built, as against the one you intended | Hand the deck to a person who has not seen it, take it back, and ask what they remember in order. Fail if their order differs from the built order, or if they cannot name the change between the first frame and the last. This is the only test here that touches a real reader. |

## Anti-patterns

Broad approaches worth naming:

- **The listicle with no spine.** Ten tips in any order, each individually fine. **Fix:** reorder so every frame depends on its predecessor, or make the finite set the promise instead, which is legitimate when the count is visible and true.
- **Continuation dressed as progression.** Each frame restates the premise in new words with rising confidence. This is the native output of a generator, because a sensation of progress is the thing it has in surplus. **Fix:** the turn ledger with a named from-X-to-Y per frame, run by someone other than whoever wrote it.

Specific failures:

- **Agenda or credential at position 2.** "Here is what we will cover", a face, a track record. **Fix:** delete it, or move it to the last frame. Position 2 carries the turn.
- **Payoff on frame 1.** The hook gives away the answer, so the body has nothing left to collect. **Fix:** frame 1 promises the currency, not the conclusion.
- **Currency switch at the close.** The body accumulates evidence and the last frame asks for an identity shift. **Fix:** pay out in the currency collected, or re-promise at frame 1 and run the bait check.
- **Uniform intensity.** Every frame a zinger, or every frame dense. **Fix:** install the rest frame on purpose, as the template with fields removed.
- **Hand-tuned frame seven, or a template the content cannot fill.** A layout needing three image orientations for a topic that produced one. **Fix:** inventory the real content range first, then rebuild the template from it.
- **A count that is not true.** "7 lessons" across eleven frames. **Fix:** make it true. A visible finite set is a real promise and a cheap one to break.
- **Decoration carrying the swipe.** Arrows and swipe labels doing work the content should do. **Fix:** delete every affordance, read the deck, add back only what position does not supply.
- **Resolution where you wanted a reply.** Nobody replies to a tidy summary. **Fix:** end on the want, unless the piece's job is credibility, in which case keep the resolution and expect fewer replies.
- **A break with no reason.** One frame restyled because it felt flat. **Fix:** a flat frame is a turn problem, not a styling problem.
- **Progress dots nobody can see.** Slide numbers built at 24px, which render at eight points. **Fix:** build them at 36px or drop them and let the count live in words.

## Applied: a nine-frame carousel, computed on both canvases

Both canvases are 1080px wide: the square at 1080 x 1080 and the portrait at 1080 x 1350. Both land in the same feed column of roughly 360 device-independent pixels, so both carry a 3x nominal downscale and a 4x stress case, and **type sizes are therefore identical on the two canvases.** The only thing that differs is live height. Everything below is derived from those two facts.

### The shared numbers

**Margins and live area.** Side margins are 1080 / 12 = 90px on both canvases, which renders as a 30pt clear band. Live width is 1080 - 180 = **900px on both**. The 90px margin is derived here from 1080 / 12 and is not a shared constant: `reference/canvas-assumptions.md` fixes the canvas sizes and the downscale factors and fixes nothing about margins. Every figure in this section depends on that 90 and on the 36px gutter below, so a piece built on another skill's margin recomputes all of them rather than importing these.

On the square, top and bottom margins are also 90px, so live height is 1080 - 180 = **900px**. Live area 900 x 900 = 810,000px².

On the portrait, top and bottom margins are 1350 / 10 = 135px, so live height is 1350 - 270 = **1080px**. Live area 900 x 1080 = 972,000px².

**The portrait buys 180px of live height and nothing else.** That is the entire budget difference between the two canvases, it is 20 percent more height, and every per-canvas divergence below is that 180px being spent.

**Columns and gutters.** Six columns across the 900px live width with a 36px gutter, so the smallest visible unit and the smallest gap are the same number: (900 - 5 x 36) / 6 = (900 - 180) / 6 = **120px per column**. Column plus gutter is 156px. Two columns are 276px, three are 432px, four are 588px.

**The type scale.** A step must survive division by 3. At the 36px nominal-case floor, a 1.125 ratio puts 36px next to 40.5px, which renders as 12pt next to 13.5pt: one level wearing two names. Require at least four points of rendered separation at the floor, so the ratio must be at least (12 + 4) / 12 = 1.333. Use **1.414**, the square root of two, because one step clears that minimum and two steps are exactly 2x, which is the rank 1 to rank 2 separation a single frame needs.

| Working file | At 3x | At 4x stress |
|---|---|---|
| 36px | 12pt | 9pt |
| 51px | 17pt | 12.75pt |
| 72px | 24pt | 18pt |
| 102px | 34pt | 25.5pt |
| 144px | 48pt | 36pt |
| 204px | 68pt | 51pt |

**The floor is 36px nominal and 48px at stress,** since 36px renders at nine points under a 4x downscale, below the twelve points you can rely on.

**Spacing.** Same ratio, same numbers: 36 / 51 / 72 / 102 / 144 / 204. In practice three steps do the work: 36px to separate within a group, 72px to separate two groups, 144px for a structural void. The gap between rank 1 and rank 2 must be smaller than the gap from either to the margin, or the two stop reading as one group.

**Contrast.** Large text under WCAG AA is 18pt or above, which needs 3:1; everything else needs 4.5:1. Rendered at 3x, 36px is 12pt and 51px is 17pt, so **both need 4.5:1**; 72px is 24pt and above, so **3:1 is sufficient from 72px up**. Under the 4x stress case, 72px falls to 18pt, exactly at the threshold, so hold 4.5:1 on 72px as well if the piece has to survive stress. A seam element carried across frames at 36px needs 4.5:1 or it disappears in the strip render, which is test 9 and test 12 catching the same mistake from two directions.

**Measure.** Average character advance in a typical sans is roughly half the type size. So the live width of 900px carries 900 / (51 / 2) = **35 characters per line at 51px**, 900 / 51 = **17.6 characters per line at 102px**, and 900 / 72 = **12.5 characters per line at 144px**. For continuous prose the readable range is 45 to 75 characters, and 35 is well under it, which is the arithmetic proving a carousel body block is not prose: it is a short block, and it has to be written as one.

### The nine frames

Nine frames is the shape's smallest clean count: promise, turn, four progression frames, rest, payoff, want.

**Frame 1, the promise.** Hand-tuned, outside the template. Rank 1 is the line a stranger would repeat. Rank 2 is the currency of what is inside, not the brand, not a face, not the count. Unresolved tension: off-centre mass with a genuinely empty top third. It also teaches the reader how to read frame 2, so a colour that means "takeaway" here means that for the rest of the set.

Budget on the square, against 900px of live height: empty top third is 900 / 3 = 300px. Rank 1 at 102px with 1.1 leading is 112px per line, four lines is 448px. Group gap 72px. Rank 2 at 51px with 1.4 leading is one line of 71px. Total 300 + 448 + 72 + 71 = **891px against 900**. Nine pixels of slack, so **cap rank 1 at four lines, 70 characters, ten to eleven words** on the square.

Budget on the portrait, against 1080px: empty top third is 360px, the same blocks come to 951px, leaving **129px of slack**. That buys either a fifth line of rank 1 (112px, taking rank 1 to 88 characters and thirteen words) or 129px more void. Spend it on the void. Frame 1's job is one exposure against a hostile feed, and the extra height buys tension more cheaply than it buys two more words.

**Frame 2, the turn.** First templated frame, and it prices the promise. If frames 1 and 3 read the same with frame 2 removed, you have an agenda frame wearing a headline. Built to the body template below.

**Frames 3 to 6, the progression.** Four frames, one turn each, same currency, identical structure, identical dominance order, one element across each seam, magnitude rising.

The body template budget, on the square: heading at 102px, up to three lines at 112px is 336px and 53 characters. Group gap 72px. Body at 51px, up to four lines at 71px is 284px and 140 characters. Seam element at 36px with 72px clearance is 108px. Total 336 + 72 + 284 + 108 = **800px against 900**, leaving 100px. That absorbs a fourth heading line (112px, which it does not quite cover) or a fifth body line (71px), so in practice **one or the other, not both**, and the ceilings are 53 characters of heading and 140 characters of body.

On the portrait the same blocks leave **280px**. That is one image band of 280 x 900, which is 252,000px² or 26 percent of the live area, or roughly 70 more characters of body, but not both. Note what the image band cannot be: at 26 percent of the live area it does not dominate the frame, so the heading still carries rank 1 and the image supports. A dominant element wants two to three times the weight of everything else **(thin)**, and 280px of band under 336px of heading does not reach it.

**Frame 7, the rest.** Three to eight words at 144px, no image, maximum void, the body template with fields removed. At 144px the measure is 12.5 characters per line, so eight words at roughly 6.5 characters each is 52 characters, which is 4.2 lines at 158px leading, or 663px. On the square that leaves 237px of void; on the portrait, 417px. The rest frame is the one place the portrait's extra height is pure gain.

**Frame 8, the payoff.** The promised currency delivered, and the set's one break. Build the break as a reprise rather than as a new idea: use frame 1's rank pair moved one step up the scale, so rank 1 is 144px and rank 2 is 72px. Three lines of rank 1 is 474px and 37 characters; two lines of rank 2 at 101px leading is 202px and 50 characters; with a 72px gap that is 748px, which fits both canvases. A reader reads a reprise as deliberate and a new layout as a mistake, and in the file those two are identical, which is why the break is specified rather than left to taste.

**Frame 9, the want.** Two fields: one line that leaves something open, and one ask. Rank 1 is the open line at 144px; the ask is rank 2 at 72px and small. The ask is rank 1 on this frame and rank 3 everywhere else.

### What nine frames can actually hold

Square: frame 1 at 70 + 35 characters, five body frames at 53 + 140, the rest at 52, the payoff at 37 + 50, the want at 37 + 50. That is 105 + 965 + 52 + 87 + 87 = **1,296 characters, roughly 200 words for the whole deck.**

Portrait: the body frames gain roughly 70 characters each, so 1,296 + 350 = **1,646 characters, roughly 255 words.**

Carry that figure into the sequence sheet. Two hundred words across nine frames is twenty-two words per frame, which is the real reason a frame cannot both explain and turn: there is no room to do both, so the body block states the turn and nothing else.

### Twelve frames

Promise, turn, six progression frames, two rests, payoff, want: 4 + 6 + 2 = 12. Six progression frames exceeds one rest per five **(thin)**, so the second rest sits in the middle of the progression, after frame 5 or 6, and the first sits in its usual place before the payoff. Copy budget rises by the two extra progression frames and falls by the extra rest: 1,296 + (2 x 193) - 141 = **roughly 1,540 characters on the square**, about 240 words.

### The strip render, computed

Nine frames at 25 percent is 270px each. With 36px gaps that is (9 x 270) + (8 x 36) = 2,430 + 288 = **2,718px of width**, which does not fit a 2,560px display. Render at 23 percent instead: 248px per frame gives (9 x 248) + 288 = **2,520px**. Portrait thumbnails are 248 x 310, square ones 248 x 248. Twelve frames need 23 percent with 18px gaps: (12 x 248) + (11 x 18) = 3,174px, so split the strip into two rows of six rather than shrinking further, since below about 20 percent the density pattern stops being readable.

### Before, diagnosis, after

**Before.** A nine-frame deck on the portrait canvas. Frame 1 states a claim. Frames 2 to 8 each restate it with a new example, each heading at 102px, each body block at 51px, every frame clean. Frame 9 summarises and asks for a comment. Nothing in it is ugly and it did not land.

**Diagnosis, computed and run in order.** Turn ledger: frames 2 through 8 are seven rows, six marked `none`, one marked F. Six `none` against one F fails test 2 on the first clause, which says the material is the problem. Alignment diff, three blind passes: frame 1 names information, the body accumulates information, the last frame asks for a position shift. Two of three match, so test 4 fails on the ending. Magnitude profile: minor, minor, minor, minor, minor, minor, minor. Three alike in a row fails test 5 at frame 4 and never recovers. Stop test at n = 4: no sentence can be written, so the deck ended at frame 4. Overlay: clean, zero drift, test 7 passes. Strip render at 23 percent: nine thumbnails of even density with no sparse frame, so test 9 fails. Floor check: progress dots at 24px, which renders at eight points, failing test 12. Count inventory: the deck says "7 lessons" and runs nine frames, failing test 11.

**After.** The seven restating frames collapse to four progression frames, each with a written turn. The 965 characters of body those four frames can carry on the portrait, 4 x 210, is less than the seven frames held, so the cut is also a copy cut and the sequence sheet has to be rewritten rather than trimmed. One rest frame at 144px goes in before the payoff, giving the strip its sparse frame. The payoff moves to frame 1's rank pair one step up, 144px over 72px, as the single break. The closing ask changes from a position shift to the information currency the body actually collected, then the ledger is re-run to confirm a row changed. Progress dots go from 24px to 36px or out entirely, and the count changes from seven to the true nine or the frames change to make seven true.

### What a crew can be handed

1. **The sequence sheet,** signed off before any file opens: promise, currency, turn and magnitude per frame, payoff, want.
2. **One frame-1 file per deck,** built by the hook owner, never a template, because tension does not survive refilling.
3. **One body template** with the computed character ceiling on each field, 53 for the heading and 140 for the body on the square, derived from the longest real heading in hand rather than from the mock, plus the fixed 90px margins, the fixed dominant footprint and one accent.
4. **One rest variant and one payoff break** as separate files, so nobody invents either under deadline.
5. **A last-frame template** with the want line and the ask as separate fields.
6. **A per-deck checklist** attached before the deck is handed back. **(thin)**

**What a crew cannot be handed:** frame 1's tension tuning, whether the payoff break is apt, and the turn material itself, which has to be confirmed by the person it happened to rather than proposed on their behalf.

## Checklist

- [ ] Sequence sheet written before the first file, with the promise's currency named
- [ ] Every turn written as from-X-to-Y, none unnameable
- [ ] Promise, body and payoff in one currency, checked by three blind passes
- [ ] Magnitude rising, no three alike in a row, one rest per five progression frames
- [ ] One open loop per frame, no affordance doing work position already does
- [ ] One structure across body frames, one element across each seam
- [ ] One break, at the payoff, built as frame 1's rank pair one step up
- [ ] Character ceilings computed for the canvas and respected by the longest real copy
- [ ] Nothing load-bearing below 36px, or below 48px if the piece must survive stress
- [ ] Survives longest and shortest real copy, grey-boxed, and reads as a density pattern in the strip
- [ ] Any stated count is true, and the ending is want or resolution on purpose

## The ultimate test

**The first-and-last read.** Show someone frame 1 and the last frame, nothing between, and ask what they think happened.

- They name the change and the middle feels missing: the shape is there.
- They name the change and nothing feels missing: the middle was decoration. Cut the deck down and rebuild the progression as turns.
- The two read as different pieces: the currency switched. Fix the promise, then re-run the turn ledger to check you did not re-signpost nothing.
- They cannot name a change at all: there is no sequence here, whatever the frames look like. That is a finding about the material rather than about the design, and the repair is a different piece.

## What an agent can run, and what it cannot

**Can run from the file:** the overlay diff across body frames; the substitution refill with the longest and shortest real copy and grey-boxed images; the strip render and the character-ceiling arithmetic; the floor check at 36px and 48px; the contrast ratios against the 4.5:1 and 3:1 thresholds; the count and affordance inventory, with the stated count against the actual frame count and every arrow and label listed; the last-frame classification, reported as the lines themselves rather than as a verdict; and the three alignment passes, which must be issued as three prompts with no shared context, because run as one prompt the model harmonises the three readings and returns a clean bill every time.

**Cannot run:** whether anything turned, which is a question about the world; the magnitude of a turn, since nothing supplies a scale; whether frame 1 is a thing a stranger stops for; whether the payoff break is apt, since in the file a deliberate break and a mistake are identical; and whether the want is one a real reader would act on.

**The default to override explicitly.** A generator asked to extend a sequence produces frames that feel like progress and change nothing, fluently, because a sensation of progress is what it has in surplus. So the turn ledger has to demand a named from-X-to-Y and has to come back with some `none` rows, and the agent that wrote the deck is the worst available judge of whether it moves.

## Where this skill should lose

A multi-frame piece touches nearly everything else in this plugin, so the division is worth stating precisely. **This file owns the ordering and every across-frame decision: how many frames the piece needs at all, which frame does what job, what crosses each seam, which frames are templated, and how a budget divides across a set. The single-frame skills own everything that happens inside any one frame.** When a finding is about one frame, close this file.

The frame count is this file's call, and it is the one decision readers arrive from the single-frame side expecting to find there. The arithmetic is here: a frame count multiplied by what one frame of that canvas can carry, measured against the copy. `dsn-poster` is what tells you a single frame has run out of room, because it computes the measure ceiling that proves a paragraph will not fit. Turning that finding into a number of frames, and deciding what each one holds, happens here.

**When the question is which element is first look inside a frame.** Use `dsn-hierarchy`. It owns the rank list, the rank 1 to rank 2 step and the ladder for the canvas. This file only says which frame carries which rank job: rank 1 is the repeatable line on frame 1, the heading on a body frame, and the open line on the last frame.

**When a frame tips, or you are choosing between symmetry and tension.** Use `dsn-balance`. It owns the stability call inside a frame. This file takes one consequence of it, that tension detunes under substitution, and uses that to decide which frames are hand-tuned. Stated from both sides: that file decides whether a given layout survives having its content swapped, and this file decides which frames of the set are therefore built by hand and which are refilled from a template.

**When the question is how to arrange one frame at all.** Use `dsn-composition` for where the elements sit, what path the eye takes between them, and which region of the frame is left empty. How large an empty region is comes from `dsn-spacing`, and which element should be first comes from `dsn-hierarchy`. This file assumes every frame already passes all three.

**When you need the grid rather than a grid.** Use `dsn-grid`. The six columns, 120px column width and 36px gutter above are derived in this file from its own 90px margin and 36px spacing step, which is why they do not match that file's 72px margin, 24px gutter and 136px columns. Neither set is wrong; they start from different margins and each closes. That file owns grid derivation, so when a project needs one grid across several skills, take the triple from there and recompute the frame budgets, the character ceilings and the spans here against it. What is not allowed is running this file's column width inside that file's margin.

**When you need the spacing scale rather than three steps from it.** Use `dsn-spacing`. It owns the scale and the grouping rules; this file uses 36, 72 and 144 and the rule that a within-group gap is smaller than a between-group gap.

**When you need the type scale, leading, tracking or measure.** Use `dsn-typeset`. The 1.414 ratio, the six sizes and the character-per-line arithmetic above are its material applied to a set. If the piece needs a different scale, get it there and recompute the ceilings here.

**When the piece is one frame.** Use `dsn-poster`. It owns carrying one idea in one frame and deciding when one frame is done. The two files are complements, and a carousel's frame 1 is closer to its problem than to this one's.

**When text might be unreadable, or type is going over a photograph.** Use `dsn-contrast`. It owns the ratios. This file only states which threshold applies at which rendered size and that a 36px seam element has to clear 4.5:1.

**When you are choosing or rescuing the photography.** Use `dsn-image`. This file computes the image band's footprint on the portrait canvas and says it cannot dominate a body frame; which image goes in it is not a sequencing question.

**When the template has to become named values an agent applies.** Use `dsn-tokens`. The template described here is a layout with ceilings; turning it into a named, derivable set someone else can apply correctly is that skill's job, and a template handed to a crew without it drifts.

**When two pieces do not read as the same brand.** Use `dsn-identity`. It owns coherence across pieces. This file owns coherence across the frames of one piece, which is a smaller and more mechanical problem.

**When the progress dots, slide numbers or small glyphs are the question.** Use `dsn-icon`. It owns small marks that have to read at small sizes and look like a family. This file only supplies the floor that disqualifies most of them, 36px at the nominal case and 48px at the stress case.

Three things are not overlaps and should not be looked for here: which palette, which typeface and what a mark should be. A sequence constrains them to one carried accent and one fixed structure and says nothing else about them.

Four things are outside this skill entirely. **Timed or animated sequences**, where reveals are paced by the clock rather than by a swipe, and nothing here transfers. The only motion rules anywhere in this plugin are the thin ones in `dsn-identity`, and they govern consistency of duration and easing across a brand rather than how a reveal is paced, so expect little when you go there. **Sets longer than about twelve frames**, where the position map degrades and a chapter structure is needed that this file does not teach. **Threads and newsletters**, where a reader sees several units at once and can scroll back freely, which removes the seam this skill is built around. And **whether the claim is true**, since shape tells you nothing about truth.

## Writing the output

Plain words, full sentences, and the actual frame number, field or measurement rather than an abstraction: "frame 4 restates frame 3's claim with a new example and turns nothing" beats "the middle loses momentum". Name the test each finding came from, including the passes, because a pass and a test nobody ran look identical in a summary that only lists failures. Give the principle first and the change as an option. Show the arithmetic whenever you quote a pixel figure or a character ceiling, so the reader can follow the numbers to the same answer rather than taking them. Label a working default as a working default at the point you use it. When a point rests on carrying a print mechanism across the seam rather than on something observed in this format, say so in the same sentence.

Sources, corroboration, single-source flags, disagreements and what was searched and not found are in `references/provenance.md`.
