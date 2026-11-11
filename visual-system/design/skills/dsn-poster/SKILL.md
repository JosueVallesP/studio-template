---
name: dsn-poster
description: One frame carrying an idea alone with no next slide, every element looking necessary when something must come out, or deciding if it is finished. Gives one composition.
---

# The single frame at full strength

This skill builds and judges one canvas that has to work alone. The single idea underneath it is that a frame with no second surface cannot defer anything: there is no later slide to hold the proof, no caption that gets read, no next frame to carry the part that did not fit. Everything the viewer will ever get from the piece arrives in one look, at one size, in a condition you do not control. So the governing decision in a single frame is not what to include. It is what to cut, and the cut has to be made against the seconds the frame actually gets rather than against how necessary each element feels while you are looking at it full size on a desk.

## What this skill is for

Use it when someone wants to:

- carry one idea in a frame that has no second page, no scroll and no next slide
- decide what to cut when every element seems necessary
- build a composition where the type is the image rather than a label on one
- judge whether a single frame is finished, and say why
- translate poster thinking onto a 1080 x 1080 square or a 1080 x 1350 post graphic

The output is one composition with its numbers stated: element count, level count, type sizes, the gaps between them, and a list of what came out.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file has been tested against an outcome, so nothing here establishes that one arrangement communicates better than another. Rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than as a general result. Every pixel figure in Applied is computed from the canvas assumptions at the plugin root: the arithmetic is checkable, the assumption it starts from is reasoned rather than measured.

Four things this file does not reach. It covers no motion, no ordering across frames and no print production. It covers no non-Latin setting, right-to-left or vertical composition. Accessibility beyond the contrast arithmetic below is absent. And the crop behaviour of any specific platform is unknown, so the margin figure treats cropping as a hazard to clear rather than as a specification.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

These are the only terms this file needs. The rest of it assumes them.

**Frame.** The one canvas, edge to edge, including its margins.

**Level.** One rank in the reading order, carrying one class of content. A headline is a level. A headline plus a subhead plus three bullets is three levels.

**Channel.** One carrier of meaning inside the frame: the words are one channel, a picture is another, colour can be a third. Two channels saying the same thing is the commonest hidden surplus.

**Fringe.** A single band of identification or administrative text at the outside edge of the frame, read last or not at all: a handle, a credit, a date. The fringe is not a level, because nothing in it has to be read for the frame to work.

**Dwell budget.** The number of seconds the frame actually gets in front of one viewer, written down before any element is placed. One to two seconds in a feed or passing a billboard; ten to thirty in front of a wall someone has stopped at. **(thin)**

**Measure.** The width of a line of type, counted in characters rather than pixels, because readability tracks characters per line and not physical width.

**Leading.** The vertical distance from one baseline to the next, baseline being the invisible line the letters sit on. Quoted here as a multiple of the type size: leading of 1.05 on 120px type is 126px.

**Visible gap.** Leading minus type size. The actual white you see between two lines. Use this rather than leading when comparing gaps, because leading includes the height of the letters.

**Tracking.** Uniform space added between every letter in a run of text. **Kerning** is space adjusted between one specific pair of letters. Tracking is a setting; kerning at display size is hand work.

**Counter.** The enclosed white inside a letter: the hole in an o, the loop of an e, the bowl of an a. A counter that closes up when the frame is seen small is the first thing to fail in a type-led frame.

**Geometric centre.** The exact midpoint of the frame: half the width, half the height.

**Optical centre.** The point that reads as centred, which sits above the geometric centre, because a block placed at the exact midpoint reads as sitting low. Taken here as 5 percent of the frame height above geometric centre.

**Tonal value.** How light or dark something is, independent of its hue. Stated here as relative luminance on a scale where 0 is black and 1 is white.

**Contrast ratio.** (lighter value + 0.05) divided by (darker value + 0.05), using relative luminance. A ratio of 3:1 is the floor for type rendering at 18pt or larger; 4.5:1 is the floor for anything smaller.

**Ground.** What the frame sits on. A post graphic has two grounds, light and dark, on one device, because the app background changes under the same asset.

**Silhouette.** What is left of the composition when you blur it past readability: the arrangement of dark and light masses with no legible word in it.

**Register.** The tone the frame arrives in, named in one word: urgent, warm, clinical, apologetic, ceremonial. Every frame has one whether or not you chose it.

**Downscale factor.** How much smaller the frame is seen than it is built. A 1080px asset in a phone feed column of about 360 points is seen at a third of its built size, so the downscale factor is 3.

## Why poster thinking transfers, and where it inverts

A poster and a feed graphic are the same problem at opposite viewing distances. A poster fails by being invisible from across the street, and because it is approached it wins a second close reading, so its permitted complexity is set by where it hangs: a placement seen in passing needs larger elements, higher contrast and more space, while a placement someone can stand in front of permits more information. A feed graphic fails by being passed over while fully visible, inside a second, at the same size as every competitor's frame. There is no approach, so the thumbnail is not a preview of the viewing condition, it is the whole viewing condition. Four decisions change as a result.

**The cut goes one level deeper.** A poster's third level is read late. A feed graphic's third level is usually not read at all, so it is cost with no return. The arithmetic for why it cannot be rescued by setting it smaller is in Applied: the third level collides with the size floor, not with the vertical room.

**You cannot win by being bigger.** Every frame in the column is the same width. A poster can out-shout its neighbours by being physically larger. A graphic can only out-rank them inside its own edges, so every contrast you have is internal.

**The ground moves.** A wall is one ground. An app is two, and the same asset sits on both within one scroll. Any difference carried by hue alone, with no difference in tonal value behind it, is not a difference here.

**Dwell is set for you, at the low end.** You do not get to choose the feed's dwell budget. Design every post graphic as the passing case, never the stopped case.

## The principles

Each names the test that checks it. The tests are in the table below.

**1. Write the one idea in a sentence before anything is placed.** Not one focal point, which is the ranking of elements inside a frame and belongs to the skill that owns focal points. One *idea*: what the viewer leaves with if they leave with nothing else. Two ideas in one frame produce a frame carrying neither, because the viewer resolves the tie the cheapest way available, which is to keep scrolling. *Test:* one-sentence idea.

**2. Put the message in its shortest, simplest and most urgent form.** Urgent does separate work from short: a brief message can still carry no reason to look now, and brevity buys nothing where every competing frame is also brief. Shorten until the remaining words state a reason to care within the dwell budget, then stop. *Test:* the reduction pass, scored by reduction accounting.

**3. Make every element name its job in words, or take it out.** Complete this sentence for each one: "without this, the viewer cannot ____." An element whose sentence does not finish is in the frame because it was available, not because it was needed. This audit is the only mechanism that distinguishes a decided frame from an assembled one. *Test:* job sentence.

**4. Set the cut depth from the viewing condition, not from taste.** The same content in two placements is two different pieces, and the difference is not a style preference: the permitted element count is a function of available seconds. Write the seconds first and derive the count from them. The seconds themselves are a working bracket rather than a measurement **(thin)**, and should be replaced if anyone measures them. *Test:* element ceiling.

**5. Treat type alone as the default composition, not as the austere option.** The minimum a graphic frame can do is typography. At post-graphic size this is not a stylistic position, it is usually the only thing that fits: the arithmetic in Applied shows that a picture plus a headline plus a fringe does not clear the size floor on a 1080 canvas, and one display line does. *Test:* blur silhouette.

**6. Make the frame say what it is about with the words covered.** A layout that would fit any subject carries nothing beyond its own words, and where the words may not be read that means it carries nothing. The failure has a precise form: no discernible structure, no hierarchy, and nothing in the arrangement belonging to this subject rather than any other, so the same frame would serve a different topic without one change. **(thin)** *Test:* subject-blind read.

**7. Check a type-led frame at four scales, and give each scale its own criterion.** A letterform at display size is a drawn shape rather than a set one, and the space around it is part of the shape rather than the gap left after it. Render four things separately and judge each on its own terms: the single character, where the counter must stay open at the stress test; the word, where the visible gap between every adjacent pair of letters must sit within about a fifth of the widest of those gaps; the line, where its intended edge must align to within half a character width; and the layout, which is the blur silhouette. A type-led frame fails most often because only the last of the four was looked at, since a balanced layout can hold a badly spaced lump. **(thin)** *Test:* four-scale hold.

**8. Name the register in one word and assign it to an element.** A frame optimised only for clarity still arrives with a tone attached, and if you did not choose that tone you inherited it. Two signs carrying identical information, built under the same clarity constraint in different places, can read as strict warning and as apology. **(thin)** Clarity is not neutral; it has a house register, and the house register is cold. *Test:* register statement.

**9. Hold the fringe to one band, and make the gap to it larger than any gap inside the frame.** There is a legitimate home for content that cannot be cut and must not rank: a single band at the outside edge, read outward or downward, last of all. **(thin)** One band only. A second band is a third level wearing a different name, and it costs what a third level costs. The gap rule is what makes the band read as fringe rather than as content, and it is checkable by subtraction. *Test:* gap ladder.

## How to work

### Mode A: making one frame

1. **Write four lines: the idea in one sentence, the viewer, the placement, and the seconds.** Nothing downstream is decidable without all four, and the seconds are the one people skip.
2. **Derive the element ceiling from the seconds.** Two to four elements total at one to two seconds, counting the fringe band as one. Not two to four groups: two to four elements. The derivation is in Applied. **(thin)**, because it inherits the dwell figures.
3. **Inventory every candidate element and write its job sentence** (principle 3). Then group them into four piles: the claim, what makes the claim credible or actionable, identification, and everything else.
4. **Run the reduction pass in the order below** until what remains fits the ceiling. Write down what came out.
5. **Decide whether type is the image or a label on one, before choosing a typeface,** because the answer changes what the typeface has to do. A label can be any competent face. An image made of letters has to hold at four scales.
6. **Set the frame: margins, live area, columns, gutters.** Compute them from the canvas rather than inheriting them, as in Applied. If the project already has a grid from the skill that owns grid construction, use that and keep its ratios.
7. **Set the three type sizes and the three gaps,** then check the gap ladder by subtraction.
8. **Kern the display line by hand.** At display size the spacing between specific letter pairs is visible, and the default pair spacing of most faces was tuned for text sizes.
9. **Run every test in the table, in order, then the ultimate test.**

### Mode B: judging one frame

Stop at the first failure. A fix upstream invalidates everything tuned after it, so continuing past a failure produces a report of consequences rather than causes. Run tests 1 to 15 in the table order, which is this one: idea, subject-blind read, job sentences, element ceiling, level count, duplicate channel, reduction accounting, then the arithmetic (floor, measure, step, gap ladder, both grounds), then blur silhouette, four-scale hold and register. Then report passes and fails, with the smallest fix for each, ordered by impact, in the form set out under "Writing the output".

## Cutting when everything seems necessary

The reduction pass, in order. Each step removes a different class of element, and running them out of order removes the wrong things, because the later steps are more painful and people reach for them first.

1. **Duplicates across channels.** If the picture already says it, the headline must not say it again. Each half looks necessary when you examine it alone, which is why this surplus survives. Keep the stronger carrier and delete the other: the frame gets quieter without losing any meaning.
2. **Elements whose job sentence does not finish.**
3. **Elements sharing one job sentence.** Two proofs of one claim is one proof and one decoration. Keep the one a stranger can verify fastest.
4. **The entire third level, when the dwell budget is under two seconds.** Not trimmed, removed. This is the step people refuse and the one the feed requires.
5. **Demote to the fringe, once.** The single band from principle 9, for what cannot be cut and must not rank.

Record what came out, every time. An empty frame produced by cutting and an empty frame produced by never deciding are indistinguishable at thumbnail size, and the record is the only thing that separates them.

### When the same frame has to be filled again

If the frame will carry different content every week, declare one variable zone rather than re-deciding the layout each time: fix a rectangle whose position and size never change, and let only the words inside it change. **(thin)** On the square canvas in configuration A below, that zone is the support line's slot, 900px wide by 54px tall at a fixed y, with the display block and the fringe band constant above and below it. The frame is then decided once and the gap ladder checked once. A zone allowed to grow is not a variable zone: a second line adds 54px plus one visible gap to the block height, which moves the optical centring and invalidates every gap below it. So the zone's measure limit, 33 characters at 54px, is a hard cap rather than a guide.

## When type is the image

Check the frame at the four scales of principle 7, not at layout scale alone. **(thin)** Four moves then make a frame of nothing but words carry weight.

**Lowercase to build mass.** Lowercase lets line spacing and letterforms condense into a weightier block than the same words in capitals, because capitals need tracking to be readable in a run and tracking is the opposite of mass. **(thin)**

**One accent, picking out only what ranks.** Not the content generally. One colour marking one or two items, the title and the one word that carries the claim, and nothing else. The accent's contrast against the ground has to be computed, not assumed, and Applied shows an accent that works on paper failing on a dark screen ground.

**Scale as the only hierarchy.** With no picture competing for attention, the size step between levels can be very large, and this is the one place a feed graphic can afford more contrast than a wall can.

**The typeface becomes the subject.** It carries the register by itself, because there is nothing else in the frame to carry it. Choosing it belongs to the skill that selects typefaces; what changes here is that the choice is no longer a detail.

## Rules you will meet elsewhere, and which to apply

Poster tradition carries hard rules that were argued rather than tested, and several are still repeated as law. Each one is either a mechanism, which survives because it converts into a procedure, or a position, which does not. Handle them as follows.

**Apply: purposeful, never casual or passive.** A mechanism. It converts into the element-by-element audit in principle 3.

**Apply: the shortest, simplest, most urgent form.** A mechanism. It converts into the reduction pass.

**Discard: sans-serif only, no excuse for any other letterform.** A position argued on theoretical grounds, not a legibility result, and it rules out faces that work.

**Discard: lowercase only.** A position argued by analogy to political levelling, with no perceptual claim attached. The mass effect of lowercase is real and is in the section above; the reason originally given for it is not evidence of anything.

**Discard: all linear directions at once, reading order abandoned for effect.** The rule most likely to damage a small frame, because it trades legibility for urgency in the one condition with no legibility to spare.

**Discard: ornament excluded, any, no exception.** Keep the audit the ban forces, drop the ban, which rules out things that do work.

**Discard: red and black as a pairing.** Symbolic in origin, not a colour finding. Applied computes a case where red fails outright.

**Resolve in favour of legibility when optics and legibility conflict.** Ranking a page's visual character above the legibility of its text was arguable about a page held in the hand at full size. At a third of built size that condition does not exist: legibility is the binding constraint and visual effect is the variable.

**Keep the scope limit.** These methods were scoped to short dramatic text, labels, logos and catchphrases, and not to sustained reading. They belong in the frame, not in the caption under it.

## Anti-patterns

Two broad approaches that fail predictably.

**Designing from the format's own back catalogue.** Every previous year's poster for the same event shares one attitude despite having different authors, because each fitted itself into the succession, so work drawn from them inherits the category's register instead of the subject's. *Fix:* take the register from outside the category entirely. That is a different starting point, not more skill applied to the same one.

**Importing the prohibitions as rules.** No ornament, no serifs, no capitals, read as law. *Fix:* the section above, rule by rule.

Specific failures, each with the smallest fix.

**Two ideas in one frame.** *Fix:* make two pieces. The frame is not divisible and splitting is cheap.

**Picture and headline saying the same thing.** *Fix:* delete one. Which one is an editorial call; keeping both is not a call at all.

**A third level nobody reaches.** *Fix:* cut it, or demote its content into the single fringe band.

**An interchangeable frame.** *Fix:* one decision that could only belong to this subject, in the type, the crop or the colour. One, not three.

**Type set rather than drawn.** The blurred frame is a grey rectangle. *Fix:* widen the size step, kern the display line by hand, treat the word as a shape before treating it as text.

**Diagonals and competing reading directions on a feed graphic.** *Fix:* keep the dynamic in one element and leave the reading order conventional.

**Empty because nothing was decided.** Identical to load-bearing emptiness in every mechanical check. *Fix:* produce the cut record. If nothing came out, the frame is unfinished rather than sparse.

**Inherited register.** A warm subject in a cold frame, because clarity was the only stated goal. *Fix:* name the register, then name the element delivering it.

**Difference carried by hue alone.** Two elements of the same tonal value in different colours separate on your monitor and merge at thumbnail size on the other ground. *Fix:* put a tonal value difference behind every hue difference, and compute it.

## Applied

Both canvases come from `reference/canvas-assumptions.md` at the plugin root: square 1080 x 1080, portrait 1080 x 1350, nominal downscale 3x, stress test 4x. Every number below is computed from those four figures and can be recomputed. One estimate is borrowed convention rather than derivation: average character width for a normal-width sans is taken as half the type size **(thin)**, and should be replaced by measuring the actual face.

### The frame, computed once for both canvases

**Margin: 90px on all four edges of both canvases.** The margin's job is to keep content clear of platform cropping and app chrome, and that hazard is measured in rendered pixels rather than as a fraction of the canvas, so it does not scale with the taller frame. The 90 is derived here from that hazard and is not a shared constant: the canvas file fixes sizes and downscale factors, declines to fix any crop-safe margin, and fixes nothing about grids. So the 900px live width, the 4 columns and the 198px column below all rest on this 90 and on the 36px gutter, and `dsn-grid`, which owns grid derivation, closes a different grid on a 72px margin. 90px renders at 30pt at 3x and 22.5pt at 4x, both comfortably visible as a decision rather than as an accident of cropping.

Live areas that follow:

- Square: 1080 minus 180 by 1080 minus 180, so **900 x 900**.
- Portrait: 1080 minus 180 by 1350 minus 180, so **900 x 1170**.

**The live width is identical on both canvases. Only the height changes, by 270px.** Every horizontal number below therefore holds on both, and the entire difference between the two ratios is a vertical budget of 270 extra pixels, which at 3x is 90pt of extra rendered height.

**Spacing step: 36px, doubling.** Derivation: the smallest gap that still reads as a gap at the stress test is about 9pt rendered, so 9 x 4 = 36px in the working file. The ladder is 36, 72, 144, 288. The same 36px is also the nominal-case type floor below, which means one number serves both spacing and size.

**Columns: 4, at 198px, with 36px gutters.** Derivation: for n columns across a 900px live width with 36px gutters, column width is (900 minus 36(n minus 1)) divided by n. That gives 432 at 2 columns, 276 at 3, 198 at 4, and 120 at 6. A column is only useful if it holds a short word at the second type size, and a seven character word at 54px is 7 x 27 = 189px. So 198px at 4 columns is the finest grid that holds a word in one column, and 120px at 6 columns holds four characters, which is alignment theatre. **Four columns is the floor of usefulness on a 1080 canvas.**

### Type sizes, and why there is no third level

**Nominal-case floor: 36px.** The smallest size you can rely on rendering is about 12pt, and at the 3x nominal downscale that is 12 x 3 = 36px in the working file.

**Stress-case floor: 48px.** Anything that must still be readable at the 4x stress test needs 12 x 4 = 48px. The two floors deliver the same 12pt and differ only in the viewing case they survive, so every size below says which one it is being held to.

**A step is one level only if it survives division by the downscale factor.** A difference of under about 4pt rendered reads as the same level wearing two names, so the working-file difference between two sizes must be at least 4 x 3 = 12px, and at least 16px to hold at 4x.

Two configurations follow, and which one you use is decided by one question: does the fringe carry anything the viewer has to act on?

**Configuration A, fringe is identification only (a handle, a credit).** Display 120px, support 54px, fringe 36px. At 4x these render 30pt, 13.5pt and 9pt. The fringe sits below the 12pt floor at the stress test, which is acceptable precisely because nobody has to read it: it says who made this, and a viewer who wants it will stop and look.

**Configuration B, fringe carries an action (a URL, a date someone must note).** Display 120px, support 72px, fringe 48px. At 4x these render 30pt, 18pt and 12pt, so all three clear the floor. Support has to rise to 72px because 60px against a 48px fringe is a 3pt rendered difference at 4x, which is one level wearing two names.

**Now the third level, on both canvases.** A third content level needs a fourth distinguishable size, since the fringe already occupies the floor. Working downward from configuration B: 120, 72, 48, and then anything below 48 is under the stress floor. Working with A: 120, 54, 36, and a fourth size between 54 and 36 would be around 45px, rendering 11.25pt at 4x, below the floor. Either way there is no size left.

**So the ceiling is two content levels plus one fringe band, and it is set by the size floor rather than by vertical room.** This is why the extra 270px on the portrait canvas does not buy a third level, and it is the most load-bearing piece of arithmetic in this file.

### Measure, and why a post graphic cannot carry a paragraph

Characters per line is live width divided by half the type size.

- Display at 120px: 900 / 60 = **15 characters per line**.
- Support at 54px: 900 / 27 = **33 characters per line**.
- Support at 72px: 900 / 36 = **25 characters per line**.
- Fringe at 36px: 900 / 18 = **50 characters per line**.

Comfortable continuous reading needs roughly 45 to 75 characters per line. The largest type that could deliver 45 characters on a 900px measure is 900 / 45 = 20px per character, so a 40px size. 40px renders 13.3pt at 3x and 10pt at 4x, below the floor. Going the other way, the smallest stress-safe size is 48px, which gives 900 / 24 = 37 characters, and 37 is below 45.

**There is no size on a 1080 canvas that both sets a readable paragraph measure and clears the floor.** The live width is the same on both canvases, so this holds for the portrait frame too. A post graphic carries phrases. If the content needs a paragraph, the frame is the wrong container and the paragraph belongs in the caption or in a multi-frame piece.

### Worked example: one post graphic, before and after

**Before.** A 1080 x 1080 square carrying eight elements.

1. Headline: "Most content operations fail for one reason: the owner is the only resource that cannot be substituted" (102 characters)
2. Subhead: "A field note on one-person publishing" (37 characters)
3. An abstract illustration
4. Three bullet points
5. A logo
6. The handle "@josuevalles" (12 characters)
7. "November 2026"
8. A "read more" arrow

**Diagnosis, computed.**

- *Element ceiling.* Dwell budget is one to two seconds, because this is a feed. Ceiling is four elements including the fringe. Eight against four. **Fails by a factor of two.**
- *Level count.* Headline, subhead, bullets, illustration: four content levels against a ceiling of two. **Fails.**
- *Display measure.* 102 characters at 15 per line is 6.8, so seven lines. Block height for n lines is (n minus 1) x leading plus size, and display leading at 1.05 of 120px is 126px, so seven lines is 6 x 126 + 120 = 876px. Live height is 900px. **The headline alone consumes 97 percent of the frame.** It cannot be set at display size, and setting it smaller removes the display level.
- *Subhead measure.* 37 characters at 33 per line is two lines at 54px. A two line support level against a seven line display level is not a second level, it is a second paragraph.
- *Fringe.* Handle, date and arrow is three items in a band that holds one. **Fails principle 9.**

**After, computed.**

*Cut record, by reduction pass step.* Step 1 removed the illustration, which said the same thing as the headline. Step 2 removed the arrow, whose job sentence does not finish on a static image. Step 3 removed the logo, which shares its job sentence with the handle. Step 4 removed the three bullets, the whole third level. Step 5 demoted the date out of the frame entirely rather than into the fringe, because the fringe band holds one item and the handle is the one that identifies.

*Headline rewritten to fit.* Three lines at display size is the budget, so 3 x 15 = 45 characters maximum. "The owner is the only unsubstitutable part" is 41 characters, which is 2.73 lines, so three. Block height is 2 x 126 + 120 = **372px**.

*Support rewritten to one line.* 33 characters maximum at 54px. "One-person publishing" is 21 characters. One line, height **54px**.

*Vertical layout on the square, configuration A.* Content block is 372 + 72 (one step up the spacing ladder, because the levels are different ranks) + 54 = **498px**. Optical centre is 5 percent of 1080 above geometric centre, so 540 minus 54 = **y 486**. Centring a 498px block on it puts the top at 486 minus 249 = **y 237** and the bottom at **y 735**. The top margin is at y 90, so the block clears it by 147px. The fringe band sits on the bottom margin: 1080 minus 90 minus 36 = **y 954** to y 990.

*Gap ladder, by subtraction.* Visible gap inside the display block is 126 minus 120 = **6px**. Visible gap inside the support level does not apply at one line. Gap between the two levels is **72px**. Gap from the content block to the fringe is 954 minus 735 = **219px**. The sequence 6, 72, 219 increases monotonically outward. **Passes.**

*The same content on 1080 x 1350.* Every horizontal number is unchanged: 900px live width, 4 columns at 198px, 15 characters at display, 33 at support, same three type sizes, same two-level ceiling. Optical centre moves to 675 minus 67.5 = **y 607.5**. The 498px block centred there runs from 607.5 minus 249 = **y 358.5** to **y 856.5**. The fringe band moves to 1350 minus 90 minus 36 = **y 1224**. The gap to the fringe becomes 1224 minus 856.5 = **367.5px**, against 219px on the square.

*So the 270 extra pixels buy exactly one of two things.* Either more air, which is the 367.5px fringe gap above, or one more display line: four lines is 3 x 126 + 120 = 498px of display, making the content block 498 + 72 + 54 = 624px, which centred on y 607.5 runs from y 295.5 to y 919.5, still clearing the top margin by 205.5px and leaving a fringe gap of 1224 minus 919.5 = 304.5px. Four lines at 15 characters is **60 characters of headline instead of 45**. Take the air or take the fifteen characters. Taking both puts the block inside the margin.

### Both grounds, computed

The frame sits on a light app ground, taken as white at relative luminance 1.0, and a dark one, taken as near black at 0.0. Give the frame its own opaque ground so the internal contrast fight is independent of the app, and then the app only has to leave the frame's edge visible.

*Frame edge.* For the frame to read as an object on both grounds, its own luminance Lf must satisfy 1.05 / (Lf + 0.05) of at least 1.5 against white, so Lf no more than 0.65, and (Lf + 0.05) / 0.05 of at least 1.5 against black, so Lf at least 0.025. A dark ink ground at **Lf = 0.05** gives 1.05 / 0.10 = **10.5:1** against white and 0.10 / 0.05 = **2.0:1** against black. The edge is strong on one ground and soft on the other, which is the honest reading: an edge is never equally present on both.

*Type on that ground.* Display at 120px renders 40pt, above the 18pt threshold, so it needs 3:1. Support at 54px renders 18pt at 3x and 13.5pt at 4x, so take it as below the threshold and hold it to 4.5:1. Fringe at 36px renders 12pt, below the threshold, 4.5:1. An off-white at Lt = 0.80 gives 0.85 / 0.10 = **8.5:1** for all three. Clears everything.

*The fringe is the one element that cannot be dimmed.* Dimming it to Lt = 0.35 gives 0.40 / 0.10 = 4.0:1, which fails the 4.5:1 floor for type under 18pt. The minimum is Lt = 0.40, giving 0.45 / 0.10 = exactly 4.5:1. The display line can be dimmed much further, to Lt = 0.25 for 0.30 / 0.10 = 3.0:1, because it is large text.

*The accent, where the inherited rule fails.* An accent must clear 3:1 against the ground if it marks display type, so (La + 0.05) / 0.10 of at least 3, meaning La at least 0.25. A saturated yellow sits near La = 0.70: 0.75 / 0.10 = **7.5:1**, passes. A saturated red sits near La = 0.21: 0.26 / 0.10 = **2.6:1**, fails. On a white paper ground the same red gives 1.05 / 0.26 = **4.0:1** and passes for large text. **Inverting the ground inverts whether the accent works**, which is why the red and black pairing from poster tradition is not transferable to a dark screen frame without recomputing it.

*Verification.* Render at 33 percent and at 25 percent, on both grounds, on an actual phone. The thumbnail is not a check on the piece. It is the piece.

## Tests

Run in this order. Each returns a verdict decidable from this file alone.

| Test | Catches | Verdict |
|---|---|---|
| **1. One-sentence idea** | Two ideas in one frame | State what the viewer leaves with. Fails if it takes two sentences. The frame is not divisible, so split the piece rather than compressing the sentence |
| **2. Subject-blind read** | A frame any subject could wear | Cover every word and show it to one person who has not seen the piece. Ask what it is about. Fails if their answer does not name the actual subject area **(thin)** |
| **3. Job sentence** | Elements present because they were available | Complete "without this, the viewer cannot ____" for each element. Any sentence that does not finish is a cut |
| **4. Element ceiling** | Complexity set by taste rather than placement | Count elements, fringe band counting as one, against the dwell budget. Fails above four at under two seconds **(thin)** |
| **5. Level count** | A third level that will not be read | Count content levels, excluding the fringe. Fails above two on either 1080 canvas |
| **6. Duplicate channel** | One meaning carried twice | Write what the picture says and what the words say, as two sentences. Fails if deleting either sentence leaves the claim intact. Delete that carrier |
| **7. Reduction accounting** | Emptiness that was never earned | Produce the list of what came out. Fails on an empty list. A sparse frame with no cut record is unfinished, not minimal |
| **8. Floor check** | Type that disappears at the stress test | Divide the smallest size that must be read by 4. Fails below 12pt. Identification-only text in the fringe is exempt and must be declared exempt |
| **9. Measure arithmetic** | A headline that cannot be set at display size | Characters in the longest line, divided by (live width / (size / 2)), rounded up, gives lines. Multiply (lines minus 1) by leading, add size. Fails if that block exceeds the live height minus the fringe band and margins |
| **10. Step check** | One level wearing two names | Subtract adjacent type sizes. Fails under 12px, or under 16px if both must hold at the stress test |
| **11. Gap ladder** | A fringe that reads as content | Compute visible gaps: inside a level, between levels, to the fringe. Fails unless the three increase monotonically outward |
| **12. Both grounds** | Difference carried by hue alone | Compute the contrast ratio of every type colour against the frame ground, and of the frame ground against white and against near black. Fails below 3:1 for type at 18pt rendered or larger, 4.5:1 below that, 1.5:1 for the frame edge on either ground |
| **13. Blur silhouette** | Type set rather than drawn | Blur until no word is readable. Fails if no separate mass can be pointed to. Fails also if two masses of similar area and similar tonal value sit at similar distance from the centre, because then nothing takes the first look. Passes only if one mass is the largest or the darkest and you can point at it before the others |
| **14. Four-scale hold** | A type-led frame checked only at layout scale | Four separate renders. Character: fails if any counter closes up at 4x. Word: fails if the visible gap between any adjacent letter pair differs from the widest such gap by more than about a fifth of that widest gap. Line: fails if its intended edge is out by more than half a character width. Layout: test 13. A failure at any one fails the frame **(thin)** |
| **15. Register statement** | A tone inherited rather than chosen | Name the register in one word, then name the element delivering it. Fails if no element can be named **(thin)** |
| **16. Thumbnail read** | Everything above, at once | The ultimate test below |

## Checklist

Decision
- [ ] Idea, viewer, placement and seconds written before the file was opened
- [ ] Element ceiling derived from the seconds, not chosen
- [ ] Register named in one word and assigned to an element
- [ ] Type-as-image or type-as-label decided before the typeface

Frame
- [ ] Margins, live area, columns and gutters computed from the canvas
- [ ] Three type sizes set, each checked against the floor and the step
- [ ] Every element carries a finished job sentence
- [ ] Reduction pass run in order, with the record of what came out
- [ ] At most two content levels and one fringe band
- [ ] Gap ladder increases monotonically outward

Verification
- [ ] Every test above run and its verdict written down
- [ ] Contrast ratios computed, not eyeballed, for both grounds
- [ ] Rendered at 33 percent and 25 percent on a phone, on a light and a dark ground
- [ ] Every received rule applied was classified as a mechanism or a position

## The ultimate test

**Show the frame at its real viewing size, once, for the dwell budget, then take it away.** Ask the person what they are left with. If they say the idea back in their own words, the frame is finished. The diagnoses are ordered, so take the first one that matches.

- **Two things named, or hesitation between two.** The frame carries two ideas. Principle 1.
- **An element named rather than an idea.** The ranking put the most available asset above the claim. This is a focal point problem rather than a cut problem, and it belongs to the skill that owns ranking inside a frame.
- **Nothing registered at all.** Either the cut did not go deep enough for this dwell budget, principle 4, or the frame never became a shape worth looking at, principle 5. Run the blur silhouette to tell them apart: an even field with no separate mass in it points at the second.
- **Described accurately, but no subject named.** It failed the subject-blind read. Principle 6.

**A frame that contains the message and does not deliver it has communicated nothing,** and the only way to find out which one you built is to put it in front of somebody for the real number of seconds.

## What an agent can run, and what it cannot

**Can run, mechanically:**

- the element count and the level count against the dwell budget
- the job-sentence audit, as a written pass over the element inventory
- duplicate-channel detection, from a described picture plus the copy
- reduction accounting, as a diff between the draft inventory and the final one
- all of the arithmetic: margins, live area, columns, gutters, characters per line, block heights, the gap ladder, the step check, the floor check
- every contrast ratio, from stated colour values
- the blur silhouette and the thumbnail renders at 3x and 4x on both grounds
- the four-scale inspection, as four renders at four crops
- classifying each received rule as a mechanism or a position

**Cannot:**

- decide which single idea the frame carries, which is the whole editorial act
- judge whether the blurred silhouette is worth looking at, which rests on an eye
- choose the register, which is a choice rather than something derivable from the content
- tell load-bearing emptiness from an undecided frame, because they are identical in every mechanical check and only the cut record separates them
- decide which of two duplicated channels to keep
- run the ultimate test, which needs a person who has not seen the piece

## Where this skill should lose

**When the decision is about what one frame does relative to another, close this file.** Use `dsn-sequence`, which owns ordering and every across-frame decision: what frame three does given frame two, where the turn lands in a carousel, what the last frame has to repeat because the first is no longer on screen, and whether a piece should be one frame or six. The boundary in the form you will meet it: "does this frame work on its own" is this file; "does this frame work *here*, in this position" is not. A frame that passes every test here can still be the wrong third slide, because nothing here knows what the viewer already saw. Two cases always belong to sequence: anything deferred to a later frame, and anything repeated across frames, since repetition is invisible inside one frame. The reverse direction holds too and is easy to miss: a frame that sits inside a set is still this file's problem whenever it has to work alone, which covers a carousel's first frame, since that is the only one the feed shows before a swipe, and any frame that will be reposted or screenshotted on its own. Use both files on such a frame. This one decides whether it stands up with nothing around it, and that one decides whether it is the right frame in that position.

**When the question is which element ranks first inside the frame.** Use the skill that owns focal points and reading order, `dsn-composition`, and the one that owns ranking by level, `dsn-hierarchy`. This file decides how many levels a single frame can hold and what gets cut to reach that number. It does not decide which of the survivors wins the first look.

**When you need the grid itself.** Use `dsn-grid`, which owns grid construction and the choice between grid types. The four column grid computed above is the floor of usefulness on a 1080 canvas, not a grid design, and a project with a real grid should use that one and keep its ratios.

**When you need the type scale, leading or measure as a system.** Use `dsn-typeset`. The three sizes above are the single-frame case derived from the canvas floor. A project setting type across many surfaces needs a scale, and if its ladder conflicts with the three sizes here, the ladder wins and the floor check is what you re-run against it.

**When choosing the typeface.** Use `dsn-typeface`. Principle 5 says the typeface becomes the subject in a type-led frame, which raises the stakes on that choice without making it here.

**When the frame contains a photograph or illustration that survives the cut.** Use `dsn-image` for cropping, treatment and how a picture and type share a frame. This file mostly argues the picture out of a post graphic on arithmetic. When it stays, how it is handled is not here.

**When the grounds and the colour relationships are the problem.** Three files split this and none of them is the one above. Use `dsn-contrast` for whether a specific pair of values clears a measured floor, `dsn-color` for what each colour is doing in the frame and how it behaves against its neighbours, and `dsn-palette` for building or repairing the set the frame draws its colours from. The ratios computed above are a verification pass on one frame, not a way to build a colour system, and if you find yourself inventing a colour while working in this file, the invention will not survive the next twenty pieces.

**When the surviving elements are placed and the frame still sits heavy on one side.** Use `dsn-balance`, which owns the stability call: whether the frame should read as symmetrical, asymmetrical or deliberately unstable, and what counterweight each target needs. This file decides how many elements and levels the frame can hold and what gets cut; how stable the survivors are arranged is decided there. A frame cut correctly to three elements can still tip, and nothing in this file will report it.

**When the piece is not a single frame at all.** If the content needs a paragraph, the measure arithmetic above says the frame is the wrong container. That is not a brief to compress harder. It is a brief to use a different format. Take that finding to `dsn-sequence`, which owns the frame count: it computes how many frames a given body of copy needs on a given canvas and what each one carries, and the finding this file produces, that one frame has run out of room, is the input it needs.

## Writing the output

Plain words, full sentences. Name the element and give the number: "the frame holds five elements against a ceiling of four at a one second dwell budget", not "the composition feels cluttered". Give the mechanism before the change, and give the change as an option rather than as an instruction, because the cut is editorial even when the count that forced it is not.

Show the arithmetic whenever a number decides something. "The headline is 102 characters, which is seven lines at 15 characters per line, which is 876px of a 900px live height" is checkable and settles the question. "The headline is too long" is a preference.

Say which tests you ran and what each one returned, including the passes, because a pass and a test you skipped look identical in a summary that only lists failures. Separate the mechanical findings from the editorial ones, and say which is which: an element count is not arguable and an idea judgement is a reading.

When you apply a received rule, say whether it is a mechanism that survives or a position that was argued, because a reader who cannot tell the audit from the prohibition will apply a political argument about capital letters to a post graphic and believe they are following a rule.

Sources, corroboration, disagreements, discards and what the material does not reach are in `references/provenance.md`.
