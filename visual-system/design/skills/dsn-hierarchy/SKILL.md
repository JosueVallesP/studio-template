---
name: dsn-hierarchy
description: Use when a design has no clear first thing, two elements compete for first look, or someone asks why a layout is not landing. Gives a rank list and a computed ladder.
---

# Visual hierarchy

This skill decides what a viewer notices first in a piece, in what order they notice the rest, and then expresses that order in size, weight, colour, position and space. Hierarchy is a ranking, and the ranking is a decision made in words before any value is set in the design file. A frame gets a hierarchy whether or not anyone chose it: when nobody ranks, emphasis lands on whatever was easiest to make loud, reliably the logo, the largest image and the number with the most digits, and the piece ends up asserting something nobody decided to assert.

## What this skill is for

Use it to:

- decide what a viewer notices first in a post graphic, carousel slide or poster
- fix a design where several things compete and none wins
- say where a piece's hierarchy breaks and name the smallest change that repairs it
- set the type steps, spacing scale and accent rules for a body of work so a run of posts reads as one person's

The output is a three-line rank list, a type and spacing ladder computed for the canvas, and a verdict on each test in the table below.

## Confidence

The rules here are practitioner accounts of what has worked, not measured findings. Nothing in this file rests on eye-tracking, a controlled comparison or a reader test, so every judgement in it is a designer's own eye reported as a method. Most of it also comes from one practitioner rather than from several who arrived at the same place independently, so rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than craft consensus. Figures marked **(thin)** were inherited or chosen for this file rather than derived from anything, and a different figure would be equally defensible.

One claim needs its own warning, because it is load-bearing here and unsupported anywhere. The claim is that a reader who arrived with a question will hunt for the answer to that question and ignore whatever the designer made loud, including the big bold thing. Nothing corroborates it, and the opposite model, that the design sets the order and the reader follows it, is what the rest of the material behind this skill teaches. It is marked **(thin)** everywhere it appears, in principle 3, in the reader classification in Mode A, and in the carousel rules. Treat it as high value and unconfirmed: worth designing for, not worth asserting to a client as established fact.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Rank.** A position in the noticing order: rank 1 is seen first, rank 3 last. A rank is held by content, not by a style. "The headline" is a rank holder; "bold" is not.

**Channel.** One property used to express a rank. The working channels are size, weight, colour, position, surrounding space, and the addition of an extra element such as a border or a tag. Counting channels means counting how many of these are doing work on one element.

**Weight.** How heavy a typeface's strokes are, from light through regular and semibold to bold. A weight change alters how dark a block of text looks without changing how much room it takes.

**Tonal value.** How dark or light something looks when colour is ignored. Two different hues can share a tonal value, which is why a red logo and a grey caption can look equally prominent in a black and white print.

**Optical weight.** How heavy an element looks rather than how large it measures. Dark, dense, saturated, detailed or sharp-edged things look heavier than light, sparse, desaturated, plain or soft-edged things of the same area, so a small dark square can balance a large pale photograph.

**Geometric centre and optical centre.** The geometric centre is the exact middle, found by halving width and height. The optical centre sits slightly above it, because a thing at the exact middle looks a little low. On a 1080 by 1080 canvas the geometric centre is 540, 540 and the optical centre is around 540, 486.

**Silhouette and bounding box.** The bounding box is the rectangle a file occupies; the silhouette is the visible outline inside it. A cut-out figure with an outstretched arm has a bounding box far wider than the arm, so a gap measured to the box is not the gap a viewer sees.

**Cut-out.** An image whose background has been removed, so its silhouette and bounding box differ.

**Micro space and macro space.** Micro space is space inside a group: letter spacing, line height, padding. It controls reading comfort. Macro space is space between groups: margins, gutters, the gap between a headline block and a footer. It controls grouping, and it is where hierarchy lives.

**Letter spacing, also called tracking.** The uniform gap added between all characters in a run of type.

**Line height, also called leading.** The vertical distance from one text baseline to the next, usually a multiple of the type size. Type at 144px with 1.1 line height puts baselines 158px apart.

**Measure.** The length of a line of text, in pixels or in characters per line.

**x-height.** The height of a lowercase x. Two typefaces at the same size differ in apparent size and in how small they can go before they stop being readable, because their x-heights differ.

**Accent colour.** One colour reserved for promotion and used on nothing else. The cap counts elements carrying the accent, not hues in the palette.

**Contrast ratio.** The ratio between the tonal values of two colours, written as 4.5:1 and computed by a contrast checker. 1:1 is invisible, 21:1 is black on white.

**Downscale factor.** How much smaller a piece is seen than the file it was built in. A 1080px asset in a feed column about 360 points wide has a downscale factor of 3, so a 48px element is seen at about 16pt.

**Fused unit.** Two or more elements deliberately made into one point of interest, so they share one rank instead of taking a rank each. A colour block behind a headline is a fused unit; so is a number set tight against its label.

**Counterweight, also called the anchor.** An element placed in the opposite region from an off-centre rank 1, carrying enough optical weight to read as the other end of a relationship.

**Cold reader and tasked reader.** A cold reader is scrolling with no question in mind. A tasked reader arrived with one, from a search, a saved post, a link, or from having read five slides of a carousel on purpose.

## The principles

1. **Rank before style.** Write the reading order in words, with the design file closed, before any value is set, because an order written afterwards describes the layout instead of deciding it. The giveaway is that rank 1 turns out to be whatever was already biggest. Checked by the rank-list date test.

2. **One first place.** Exactly one element holds rank 1, or one fused unit does. **(thin)** Two things at rank 1 is not strong emphasis, it is no emphasis, because rank exists only as a difference and two identical differences cancel. Checked by the squint test, then the pair test on whatever two things survive it.

3. **Rank is a noticing order, not an importance order.** **(thin)** Derive the rank from what a reader needs in order to understand the next thing, not from what matters most, because the most important element often cannot be understood without something else arriving first. A landing page puts the headline above the video even when the video is the point, since a viewer needs the headline to know what the video is of. The thing a reader stops for and the thing you most want them to know are two different slots. Checked by the sentence test.

4. **Make same-type elements identical before adding any emphasis.** **(thin)** Contrast is relative, so a rank only exists as a departure from a uniform field, which means every unchosen difference between elements of the same type reads as an error and steals the departure you were saving. Two cards share size, weight, colour, padding, corner radius and height; three images share dimensions; four captions share everything. Until this passes, emphasis adds noise rather than rank. Checked by the cohesion diff test.

5. **Give rank 1 two channels, rank 2 one, and rank 3 none.** **(thin)** One channel usually loses in a hostile feed, and four channels at once reads as shouting rather than as ranking, so two is the working allocation. Rank 3 gets none because it is the flat field the other two are read against: if rank 3 is styled, there is nothing left to depart from. The exception is a dense block of running text, where weight alone is the right single channel, because weight ranks items inside a paragraph without grabbing at the whole frame. Checked by the channel count test.

6. **Demote the neighbours instead of promoting the subject.** **(thin)** Size, weight and colour are all relative, so making the important thing louder raises the floor for everything beside it and the next element gets the same treatment in turn, which is how a frame ends up with three competing first places. Quietening rank 2 and rank 3 produces the same difference at lower cost and leaves headroom. Checked by the demote check.

7. **Rank 1 is the claim.** **(thin)** Whatever is first is what the reader leaves with, regardless of what the caption says, so a true element placed at rank 1 with nothing at rank 2 to compare it against can arrange true parts into a false impression. A figure at rank 1 with no baseline, no period and no comparison asserts more than the data supports. Checked by the claim test, with the worked case in the Applied section.

## How to work

### Mode A: making something

1. **Write the sentence** a reader should be able to repeat afterwards. Not the headline, the takeaway. Ranks 1 and 2 together have to rebuild it, so write it before you know what will be large.

2. **Classify the reader as cold or tasked, and never average the two.** A cold reader is scrolling with no question, so the rank is yours to set and the strongest designed contrast wins. A tasked reader arrived with a question, and a tasked reader hunts for the answer and skips designed salience, so the answer goes at rank 1 whether or not it is what you wanted to sell. **(thin)** Averaging produces the worst of both: a cold-reader hook sitting on a tasked-reader layout hooks nobody and answers nothing. A carousel contains both kinds of reader and gets classified per slide, not per deck.

3. **Write the rank list.** Three entries, one line each, naming actual content rather than slots.

   - **Rank 1:** what a stranger stops for, which need not be the most important thing. On an event post, the artwork or the line of tension.
   - **Rank 2:** what makes rank 1 mean something. The event name and what it is.
   - **Rank 3:** what an already-convinced reader needs. Date, venue, link, logo.

   Three, because each rank needs a visibly distinct expression and one frame carries about three distinguishable steps before the fourth stops reading as a step. **(thin)** A layout with several distinct regions gives each region its own two or three rather than stretching one ladder across all of them.

4. **Run the pair test on any two elements that both seem to need prominence, then fuse or demote.** If they can become one point of interest, fuse them and give the unit one rank. If they cannot, one of them is rank 2.

5. **Flatten the whole frame, then promote once.** Set every element to one size, one weight and one colour first. Flattening is what makes the promotion legible, and it is the fastest way to discover that the cohesion diff was failing. Then give rank 1 two channels, rank 2 one, rank 3 none.

6. **Compute the ladder, build the spacing scale, place, then run the tests.** The arithmetic for both is in the Applied section. Treat any second promotion as requiring a demotion somewhere else, so the frame's total loudness stays fixed.

### Mode B: judging something that exists

1. Ask for the rank list and the sentence. If neither exists, reconstruct the rank from the file by running the shrink test, and say in the report that you reconstructed it, because a reconstructed rank is evidence about the file rather than a statement of intent.
2. Run the shrink test first, since it is the only branching diagnosis and it tells you which of the others will matter. Then the rest of the table, then the checklist as counts, then the anti-patterns as named states.
3. Report what passed, what failed, and the smallest change that repairs each failure, ordered by how much it changes the first look.

## Tests

An observer with the render, a blur or squint, a greyscale toggle, a ruler and a contrast checker can run all of them.

| Test | Catches | Verdict |
|---|---|---|
| **1. Shrink** | A rank that exists on the artboard and not in the feed | Display the piece at 25 percent of its built size, or on a phone at arm's length, and name the first thing you see out loud before looking again. Pass only if it is the written rank 1. Two or more things named means competing firsts; nothing nameable means a flat field; the wrong single thing means something unranked is carrying contrast. |
| **2. Rank-list date** | A rank reverse-engineered from the layout | Ask for the written rank list and when it was written relative to the file. Fail if it came after the layout, or does not exist. |
| **3. Squint** | Two or more elements competing for first look | Squint or blur the render until type is unreadable, and count the shapes that still read as separate. Pass on one. Two or more, flatten and promote once. Zero is a flat field. |
| **4. Pair** | Two rank 1s that an element count reports as one | Cover everything except the two candidates and say whether they read as one unit or two things. One unit shares a single rank; two things means one is rank 2. |
| **5. Sentence** | A rank built on the wrong content | Rebuild the written takeaway from ranks 1 and 2 alone, ignoring rank 3. Fail if it does not survive, and repair rank 2 rather than rank 1. |
| **6. Claim** | A true element arranged into a false impression | Read rank 1 alone and write down what it asserts. Fail if that assertion is broader than the content supports, and put the comparison, baseline or period at rank 2. |
| **7. Cohesion diff** | Unchosen differences that read as errors | Compare every element of the same type field by field on size, weight, colour, padding, corner radius and height, in the frame and across slides. Fail on any difference you cannot give a reason for, and fix before any emphasis work. |
| **8. Channel count** | Under-promotion and over-promotion together | Count channels on each rank: size, weight, colour, position, surrounding space, added element. Pass on two, one, zero. Any other distribution fails. |
| **9. Demote check** | Emphasis used as the only tool | Ask what changed the last time you wanted something noticed more. Fail if the answer is that you made it louder, and quieten its neighbours instead. |
| **10. Greyscale** | A rank carried by hue alone, which disappears for readers with colour vision deficiency | Desaturate to black and white and run the shrink test again. Fail if the rank order changes, and move the rank into size, weight or space. |
| **11. Gap audit** | Equal gaps everywhere, so spacing carries no information | Measure every gap to the visible silhouette and sort into within-group and between-group. Fail unless every within-group gap is at least one full step below every between-group gap on the scale in use. |
| **12. Arrow removal** | Ranking done by decoration rather than by the elements | Delete every arrow, box, rule and divider, then read the piece. Same order, leave them out permanently. Different order, the size and weight step is missing. |
| **13. Cover** | An off-centre element with no counterweight, or a counterweight too light to hold it | Cover the counterweight with a blank rectangle and say out loud what the frame looks like. If you say deliberate, the composition holds without it. If you say it slid or it is cut off, uncover: if your answer changes to deliberate, the counterweight is load-bearing and must not be lightened or moved. If your answer does not change, the counterweight is too light. Raise its optical weight one step, darker, denser or larger, without raising its rank, and run the test again. |

## Contrast channels and how fast each one spends

The two workhorses are size and weight, because both survive compression, downscaling and a greyscale render.

Colour spends fastest. One element per frame carries the accent, because a second accented element halves the first one's force rather than adding to it. **(thin)** Space is the strongest channel that adds nothing to the frame: surrounding an element with more room than anything else gets promotes it by absence, so it costs no ink and no complexity. Faces outrank almost everything in a frame, so use a person only when the person is the subject, and never as decoration beside the claim.

One ordering of channels is in circulation and runs, strongest first: motion, task-relevant information, white space around a focal point, humans and faces, colour, size, weight, imagery, added elements, misalignment. **(thin)** Only the top two come with a reason: motion reads as a possible threat, and goal-directed search beats designed salience. Everything below those two is asserted in sequence with no comparison attached, so use the ordering as a rough prompt for which channel to reach for and do not repeat it to anyone as a ranking.

**Step size.** Size contrast is relative, so if everything is big, nothing is. The principle to follow is the smallest step that survives the real viewing condition, which is a small step for a document held at arm's length and a large one for a compressed feed thumbnail. A 1.2x step reads clearly on a printed page and vanishes entirely at a downscale factor of 3. Working figures: about **2x between rank 1 and rank 2 in feed conditions**, and **1.3 to 1.5x when the piece will be read up close**. **(thin)** Derive the actual pixel values from the canvas, as in the Applied section, rather than taking these ratios straight.

**Size to rank, not to fill.** A size encodes a rank, so the only question a size answers is which rank the element holds. Enlarging an element to close a gap promotes it by accident, and the tell is a rank 3 item sitting at rank 1 size with nothing else about it changed.

**Contrast ratio.** WCAG 2.1 AA asks for 4.5:1 for normal text and 3:1 for large text and for user interface components, where large means 18pt or above as rendered, or 14pt bold. Use those two numbers as an accessibility floor and nothing more. A piece can pass 4.5:1 everywhere and still have no hierarchy, because the floor says a thing is readable, not that it is first. Judge prominence with the squint and shrink tests instead. Extending the 4.5 figure from text legibility to general element prominence is a house convention rather than a standard, so do not cite it that way. **(thin)** Hue-only contrast, where two colours differ in hue but share a tonal value, is what the greyscale test exists to catch.

## Space, placement and counterbalance

**Pick one spacing base and double it.** The doubling is the mechanism rather than the numbers: a ten percent difference between two gaps does not read as a rank difference and a hundred percent one does, so each step has to be twice the one below it to be perceived as a step at all. **(thin)** Apply the scale to micro space and to macro space alike. Inherited scales such as 4 / 8 / 16 / 32 or 8 / 16 / 32 / 64 are borrowed from interface work, where the reason is whole-pixel rendering on screen, and a non-integer downscale voids that reason, so derive the scale from the canvas instead, as the Applied section does.

**Every gap within a group is smaller than every gap between groups, by at least one full step on the scale.** This one relation does the grouping, because elements close together are read as one group and elements separated by more are read as two. The relation is the rule; the one-step quantification is a working minimum chosen here, since smaller differences do not reliably read as a boundary. **(thin)** It is not a mandate for minimalism: tight spacing throughout reads as energy and still satisfies the relation.

**Measure every gap to the visible silhouette, not to the bounding box.** A broad shape needs more room than a thin rule at the same measured gap, and a cut-out figure with an outstretched arm gets its gap measured from the hand rather than from the edge of the image file. **(thin)** The bounding box is invisible to a viewer, so arithmetic done on it produces gaps that look wrong while measuring right.

**Align on a shared edge instead of drawing a divider.** Two elements that begin on the same left edge, or sit on the same baseline, read as related across a wide gap, because the shared edge does the connecting a box or rule would otherwise have to do, so the gap can be large without the pair coming apart. **(thin)**

**Only box what you want noticed, and use a gap everywhere else.** A box is an emphasis channel, so it promotes whatever is inside it whether or not you meant that, which is why boxes drawn to tidy a layout end up ranking it. **(thin)** Where the job is separation rather than emphasis, a gap does it at no cost in rank.

**Counterbalance: placing rank 1 deliberately far into the space.** Pushing rank 1 hard into one side of the canvas is the move that gets a layout tension instead of arrangement, because a centred rank 1 states a position while an off-centre one states a direction. **(thin)**

The mechanism of the failure is what decides whether the move works. When an element sits far off centre, the empty region opposite it stops reading as space and starts reading as absence: the eye goes looking for the other end of the relationship, and if there is nothing there the frame reads as though something fell off the page or the element slid out of position. The fix is not to recentre. The fix is to answer the imbalance with a counterweight in the opposite region, carrying enough optical weight to read as the other end: a quiet block of type, a rule, a mass of flat colour, a small dark shape, anything with presence. Without one the frame is not asymmetric, it is lopsided, and the two look completely different to a viewer even though both measure as off-centre.

Two constraints on the counterweight. It must be lower rank than the element it answers, because a counterweight that matches rank 1 in optical weight is a second rank 1 and the pair test will catch it. And it must be heavy enough to hold, which is a judgement about how it looks rather than how it measures: a 120px dark square can answer a 600px pale photograph, while a 400px pale caption may not. Both constraints are decided by the cover test, which is the test to run on any deliberately off-centre layout.

**Placement.** For readers of left-to-right, top-to-bottom scripts: rank 1 at top-left or at the optical centre, rank 3 at bottom-right. A Z path suits minimal work, posters and billboards; an F path suits text-heavy layouts and web pages; plain top-to-bottom suits a letter or a card. Reverse the whole arrangement for a right-to-left audience. The F and Z names are conventions with a plausible basis rather than measured findings, accounts of what each one describes differ, and the hedge worth keeping is that these are paths most viewers can use rather than paths they all follow. **(thin)** Keep the placement conclusion, which is stable across every account, and check the pattern names against usability research before repeating them to a client.

**Flow.** A correctly expressed rank has already built the flow: large, then medium, then small makes a direction by weight alone, with no arrow required. Where a nudge genuinely helps, use the subject rather than a graphic: a gaze, a pointing hand, a product angled toward the type. A piece that needs an arrow to be read in the right order is missing the size and weight step.

## Anti-patterns

Named states, each with its repair. The first two are the broad ones that produce most of the rest.

- **Rank reverse-engineered from the layout,** which rationalises whatever was already biggest, and **emphasis as the only tool,** which raises the floor every time it is used. Fix: write the rank from the sentence and the reader classification, re-express it from a flattened frame, and demote neighbours rather than promoting subjects.
- **Position-only rank.** Works on the artboard and dies in a square crop, because position is the one channel a crop can remove. Fix: carry the rank in size and weight as well.
- **Three competing firsts.** Everything bold and large, several elements in the accent. The sign is the squint test returning two or more shapes. Fix: flatten to one value set, promote once, and treat any second promotion as requiring a demotion elsewhere.
- **Brand-first ranking.** The logo competing with the product name, so from a distance a viewer cannot tell what the thing is. Fix: logo to rank 3, permanently, out of the accent.
- **Decoration at rank 1.** An illustration or a stock face outranking the claim. Fix: if it is not the subject, delete it rather than shrink it, because a shrunk decoration still occupies rank 2.
- **Boxes and arrows doing the ranking.** Fix: run the arrow removal test, re-separate with macro space, build the size and weight step, and add a box back only if the order held without it.
- **Task-blind rank.** A how-to where the answer someone arrived looking for sits at rank 3 behind a hook. Fix: reclassify the reader as tasked and promote the answer, accepting the cost to the hook.
- **Isolated number at rank 1.** A large figure with no baseline, period or comparison. Fix: rank 2 carries the comparison. The repair is more information, not better styling.
- **Flat field with no winner.** One size, one weight and one colour everywhere, usually a frame that was flattened and never promoted. The sign is the squint test returning nothing rather than too much. Fix: give rank 1 two channels and rank 2 one.
- **Equal gaps everywhere.** Every gap the same value, so the spacing is tidy, carries no information, and leaves the viewer inferring groups from content alone. Fix: reset every gap onto the doubling scale, then run the gap audit.
- **Scaled to fill a hole.** An element enlarged because there was empty space beside it. Fix: return it to the size its rank earns, or make it rank 1 deliberately and re-express everything else.
- **Unanchored imbalance.** An element pushed far off centre with nothing opposing it, so the frame reads as lopsided rather than asymmetric. Fix: add a counterweight in the opposite region, or bring the element back toward the optical centre, then run the cover test.

## Applied to a post visual or carousel

Canvas sizes and the downscale factors come from `reference/canvas-assumptions.md` at the plugin root, so the numbers stay consistent across skills: square post graphics are 1080 by 1080, portrait post graphics and carousel slides are 1080 by 1350, the nominal downscale factor is 3, and 4 is the stress test. Everything below is computed from those four facts.

### The type ladder, computed

The smallest rendered size that stays reliably readable on a phone is about 12pt, and a typeface with a small x-height needs more. That floor plus the downscale factor fixes the bottom of the ladder: to survive the nominal factor of 3 the file floor is 12 x 3 = **36px**, and to survive the stress factor of 4 it is 12 x 4 = **48px**. Build upward using the step ratios, 2x from rank 2 to rank 1 in feed conditions and 1.5x from rank 3 to rank 2.

**Stress-safe ladder, the default for anything shipping to a feed.** Rank 3 at 48px, rank 2 at 48 x 1.5 = 72px, rank 1 at 72 x 2 = 144px. At a factor of 4 that renders as 12pt, 18pt and 36pt; at a factor of 3, as 16pt, 24pt and 48pt. Every rank clears the floor in both conditions.

**Nominal-only ladder, for a piece that will not be cropped or shown small.** Rank 3 at 36px, rank 2 at 54px, rank 1 at 108px, giving 12pt, 18pt and 36pt at a factor of 3. At a factor of 4 rank 3 lands at 9pt, below the floor, which is what the stress test exists to catch. Use this ladder only after checking how the piece actually renders.

The type ladder and the spacing scale are separate systems and need not share values: a 48px type size and a 36px gap sit happily in one frame.

### The spacing scale, computed

A spacing step has to land on a whole point after division by both downscale factors, otherwise the same gap rounds differently in different conditions and two steps collapse into one. A step divisible by both 3 and 4 is divisible by 12, and doubling from 36 keeps every step there:

**36 / 72 / 144 / 288.** Divided by 3: 12 / 24 / 48 / 96pt. Divided by 4: 9 / 18 / 36 / 72pt. Every value is whole in both conditions and each step is double the one below it, so each reads as a step.

Assign them: within-group gaps at 36 or 72, between-group gaps at 144. That puts within-group at least one full step below between-group, which satisfies the gap audit, and 144 against 36 is two steps, which is comfortable rather than marginal.

**Margin.** The margin has to be at least as large as the largest between-group gap inside the frame, otherwise the frame edge binds content more tightly than the internal group boundaries do and the grouping inverts. With between-group gaps at 144, the margin is **144px**, so the content column on a 1080 canvas is 1080 - (2 x 144) = **792px**, and on a 1080 by 1350 slide the content area is 792 by 1062. A sparse frame wanting a 288px internal separation raises the margin to 288 and drops the column to 1080 - 576 = 504px, which only works with very little in the frame. That is the trade, computed rather than preferred.

**Caps.** Three type sizes, two weights, one accent element per frame. **(thin)** Each additional size, weight or accent is another channel competing for the same first look, and a run of posts built on the same three sizes reads as one person's work while a run built on nine does not. Pick the three once and reuse them.

### Worked example: single-frame square post graphic

**Before.** A 1080 by 1080 square. Content: the figure 340%, the label "increase in reply rate", a logo, an abstract decorative illustration, and a URL. As built: the figure at 200px centred, the logo 180px wide in the brand red, the illustration filling the right half of the frame, label and URL both at 48px, every gap in the frame set to 60px. No rank list exists.

**Diagnosis, computed.**

- Rank-list date, test 2. No list. **Fails.** Reconstruct from the file and say so.
- Shrink, test 1. At 25 percent the canvas is 270px. The figure renders at 50pt, the logo at 45pt wide, the illustration at about 135px of area. The first thing named is the illustration, because area beats type at that size. **Fails** on the wrong single thing: something unranked is carrying contrast.
- Squint, test 3. Three shapes survive the blur: the figure, the logo and the illustration. **Fails** with competing firsts.
- Channel count, test 8. The figure carries size and centred position, so two. The logo carries the accent colour and a large area, so two. The illustration carries area and texture, so two. Three elements at a rank 1 allocation. **Fails.**
- Greyscale, test 10. Desaturated, the logo loses its prominence completely while the figure keeps its own, which shows the logo's rank was carried by hue alone. **Fails.**
- Gap audit, test 11. Every gap is 60px, so within-group and between-group are zero steps apart. **Fails.** Separately, 60 is not a step on any doubling scale in use here, so it could not be one step below anything even if the sorting were right.
- Claim, test 6. Rank 1 read alone says 340%, which asserts a large increase with no baseline, no period and no comparison. **Fails**, and the repair belongs at rank 2.
- Contrast ratio. The label at 48px renders at 16pt at a factor of 3 and 12pt at a factor of 4, both below the 18pt large-text threshold, so it needs 4.5:1 rather than 3:1. At a mid grey on white it sits near 3.2:1. **Fails** the floor.

**After.**

- Sentence: reply rates nearly tripled after the opening line was cut. Ranks 1 and 2 have to rebuild that.
- Rank list. Rank 1: 340% against a 100% baseline, Q1 to Q3. Rank 2: reply rate after cutting the opening line. Rank 3: logo, URL.
- Ladder: stress-safe. Rank 1 at 144px, rank 2 at 72px, rank 3 at 48px. Rendered at a factor of 4 that is 36pt, 18pt and 12pt.
- Channels. Rank 1 takes size at 144px plus the accent colour, so two. Rank 2 takes weight only, semibold at 72px in the body colour, so one. Rank 3 takes nothing: 48px regular in the body colour, with the logo desaturated out of the accent. Channel count now reads two, one, zero and **passes**.
- Fusing. The figure and its baseline comparison are set as one unit, 36px apart, so they share rank 1 rather than competing. The pair test on them returns one unit and **passes**.
- Spacing. Margin 144. Within the rank 1 unit, 36. Between that unit and the rank 2 line, 72. Between the rank 2 line and the rank 3 footer, 144. Sorted: within-group at 36 and 72, between-group at 144, so the smallest between-group gap is one full step above the largest within-group gap. Gap audit **passes**.
- The illustration is deleted rather than shrunk, because it is not the subject and a shrunk decoration still holds rank 2.
- Contrast. Rank 2 at 72px renders at 18pt at a factor of 4, which meets the large-text threshold, so 3:1 is permitted there. Rank 3 at 48px renders at 12pt, so it needs 4.5:1; set it to a grey measuring 4.6:1 against the background.
- Shrink, rerun. At 25 percent the rank 1 unit renders at 36pt with 144px of clear space around it and nothing else at that size. The first thing named is the figure with its baseline. **Passes.** Greyscale, rerun: rank 1 still wins on size and surrounding space. **Passes.**

### Worked example: a seven-slide carousel

**Before.** 1080 by 1350 slides. Slide 1 carries the logo large at the top, the words "7 lessons", and a photograph of a face. Body slides have headings at 84px, 72px and 96px on slides 2, 3 and 4, with heading top edges at 180px, 216px and 180px. A call to action sits on every slide at 72px in the accent red.

**Diagnosis, computed.**

- Cohesion diff, test 7. Heading sizes run 84, 72, 96 and top edges run 180, 216, 180, so five unchosen differences across four slides, each read in sequence and each reading as an error. **Fails**, and nothing else gets fixed until it passes.
- Brand-first ranking. The logo holds rank 1 on slide 1, so a viewer at thumbnail size cannot tell what the deck is about. **Fails.**
- Accent cap. The accent appears on all seven slides, breaking the one-accent cap seven times, and the call to action competes with every heading. **Fails.**
- Shrink on a body slide. The call to action at 72px is the only coloured element in an otherwise grey frame, and colour outranks size at that scale, so the first thing named is the call to action rather than the heading. **Fails** on the wrong single thing.

**After.**

- Slide 1 runs two ranks and no third. Rank 1 is the line a stranger would repeat, the tension or the claim, at 144px. Rank 2 is the promise of what is inside, at 72px. The logo comes off entirely, or drops to 48px in the bottom margin out of the accent, and the face comes off unless the deck is about the person.
- The measure checks out before the type is set. Average character advance for a sans-serif runs near half the type size, so 144px type is about 72px per character and the 792px column holds 792 / 72 = 11 characters per line. A 40-character headline is four lines, and at 1.1 line height that is 4 x 144 x 1.1 = 634px of the 1062px content height, leaving 428px for rank 2 and the gaps.
- Body slides run two ranks: heading at 96px, body at 48px, a 2x step rendering at 24pt and 12pt at a factor of 4, both clear of the floor. Heading top edge locked at 144px, and heading size, weight, colour and position plus body size and measure identical on every slide. Rank inside equal cards with a tag or a rule, never by resizing one card, because a resized card breaks the cohesion diff for every slide after it.
- The call to action sits at rank 3 on slides 1 through 6, at 48px in the body colour, and becomes rank 1 on slide 7 only, at 144px with the accent. One accented element per slide, meaning the same thing throughout: if the accent marks the takeaway on slide 2, it marks the takeaway on slide 5.
- Pacing: impact, then linger, then release. Put one deliberately sparse slide, a single line at 96px and nothing else, immediately before the close, so the final ask reads as an arrival rather than an interruption. **(thin)**
- A reader who reached the middle of the deck is a tasked reader. **(thin)** Whatever they came for gets rank 1 on its own slide, at the cost of the hook, rather than sitting at rank 3 behind more setup.

### Worked case: why rank 1 is the claim

**Before.** A published election map. Every county is coloured by which candidate carried it. The projection is accurate, the boundaries are right, every county's colour is correct, and the caption underneath states the popular vote share accurately. Alongside it runs a headline about overwhelming popular support for the winning side.

**Diagnosis.** Run the claim test: read rank 1 alone and write down what it asserts. Rank 1 here is not the caption and not the headline. It is area, because area is the loudest channel in the frame and the map is almost entirely one colour. Area encodes land. The land split runs near 80 to 20, while the vote split ran near 50 to 50, because people are not distributed evenly across land. So rank 1 asserts a landslide. The caption, which carries the true ratio, is at rank 3, and the shrink test says what happens to rank 3 in a feed: it is not read. Every element in the frame is true. The impression is false, and it was built entirely out of true parts.

**After.** Rank 1 stays the map, because the map is what a reader stops for and that is what rank 1 is for. Rank 2 changes: it carries the comparison that rank 1 cannot carry itself, two bars at 72px showing vote share side by side, placed inside the frame and inside the margin rather than as a caption below it. Now ranks 1 and 2 together rebuild the true sentence, which is what the sentence test asks for, and the headline is written from those two ranks rather than from the map alone.

**What generalises.** A caption cannot repair a rank. Whatever holds rank 1 is the assertion the piece makes, so the question to ask of any rank 1 is not whether it is true but what it claims, and anything it claims beyond the content has to be answered at rank 2.

## Checklist

- [ ] Rank list and sentence written before the file, and ranks 1 and 2 rebuild the sentence
- [ ] Reader classified cold or tasked, per slide for a carousel
- [ ] One element or one fused unit at rank 1, naming something the piece can support
- [ ] Rank 1 on two channels, rank 2 on one, rank 3 on none
- [ ] Type ladder computed from the canvas floor, with every rank clearing 12pt at the stress factor
- [ ] Three type sizes or fewer, two weights or fewer, one accent element per frame
- [ ] Within-group gaps a full step below between-group gaps, measured to the silhouette
- [ ] Margin at least as large as the largest between-group gap
- [ ] Text at 4.5:1, large text and user interface components at 3:1, rank surviving desaturation
- [ ] Same-type elements identical, in the frame and across slides
- [ ] No box, arrow, rule or divider the layout does not already imply
- [ ] No off-centre element without a counterweight that survives the cover test

## The ultimate test

Shrink the piece to 25 percent, or look at it on a phone at arm's length, and name the first thing you see out loud before you look again. If it is the written rank 1, the hierarchy works. If not, the repair follows the branch test 1 returns: for competing firsts, flatten and promote once; for a flat field, give rank 1 a second channel; for the wrong single thing, find what is carrying contrast unranked, usually a face, a logo or a misplaced accent.

Where it is possible at all, hand the piece to a person and ask what they looked at, in order. That recital is the only test here that touches a real reader rather than the designer's own eye, and it is the one worth running when the stakes justify the minute it costs.

## What an agent can run, and what it cannot

**Runs mechanically, with no human judgement:** the cohesion diff, the gap audit, the channel count, the contrast ratio checks, every checklist item that is a count or a ratio, the logo and call-to-action placement checks, the type ladder arithmetic, and the count of directional cues. An agent can also render at 25 percent and in greyscale, which turns the shrink and greyscale tests into one glance each.

**Needs a human holding the brief:** the rank order itself, because it depends on the claim and the reader and neither of those is in the design file; whether rank 1 is a thing a stranger would actually stop for; and the pair and cover tests, which ask what something looks like rather than what it measures.

**Agent default to override explicitly:** a model asked to emphasise will emphasise everything, because every element in a frame has an argument for mattering. The instruction has to be stated as *demote, do not promote*, or the native output is the three-competing-firsts frame every time. Separate the reviewer from the maker as well, since the agent that wrote the hook is the worst available judge of whether that hook carries a claim.

## Where this skill should lose

**When the question is where things sit in the frame rather than which is first.** Use `dsn-composition`, the skill that owns arrangement across the whole canvas. This skill produces a rank order and the channels that express it, and stops there.

Three files touch placement and they divide by the question being asked. This one decides which element is first and how much separation each rank needs. `dsn-composition` decides where each element sits and what path the eye takes between them. `dsn-balance` decides whether the arrangement tips and what counterweight it needs. Practical version: if the fix is to make a different element the loud one, you are here. If the fix is to move something, or to add weight on the opposite side without changing what is loudest, you are not.

**When the question is symmetry, asymmetry and optical weight in their own right.** Use `dsn-balance`, the skill that owns how a frame distributes weight. The counterbalance material here is the slice of that subject hierarchy needs, which is how to place rank 1 far off centre without the frame reading as broken. Anything beyond that, including balancing elements of equal rank, belongs there.

**When the question is whether a pair of colours is measurably readable.** Use `dsn-contrast`, the skill that owns the ratio arithmetic, the published thresholds and the conformance verdict. The channels themselves are this file's subject and not that one's: size, weight, colour, position and space, used as devices for expressing a rank, are ranked and given step ratios here. That file does one thing, which is to take two values and return whether they clear a floor. The two results are independent, so run both: a frame can clear every floor there and still have the wrong element loudest, and a frame can rank correctly here and still be unreadable.

**When the question is the spacing system for a body of work.** Use `dsn-spacing`, the skill that owns the scale and the gap system. The scale derived here is the minimum a single frame needs to pass the gap audit.

**When the question is type size, line height, measure or typeface choice.** Use `dsn-typeset`, the skill that sets type, and `dsn-typeface`, the skill that chooses one. The ladder here gives three sizes and nothing about how to set them into readable text.

**When the question is margins, columns and gutters across a family of layouts.** Use `dsn-grid`, the skill that owns the grid. The margin computed here is one number for one canvas.

**When the question is which colour the accent should be.** Use `dsn-palette` to choose it and `dsn-color` to apply it. This file only says that there is one accent and that it carries a rank.

**When the question is the order and pacing of a multi-part piece.** Use `dsn-sequence`, the skill that owns sequence. The carousel rules here govern the hierarchy inside each slide and the cohesion across slides, not what the slides should say or in what order.

**When the frame has no second surface and the question is how many elements survive at all.** Use `dsn-poster`, the skill that decides the element count and level count one standalone frame can carry, and what gets cut to reach that number. This file ranks whatever survives the cut and never decides how long the list may be, so if the answer you need is "three of these five have to go", that decision is made there and you come back here to rank the three.

Three things are outside this file entirely rather than owned by a neighbour. Data graphics: nothing here governs axis prominence, annotation weight or which series to emphasise, and while rank 1 is the claim transfers, the technique does not. Motion: it is the strongest attention channel available and nothing here governs video, animated carousels or scroll-triggered movement, since the ladder and step ratios were derived for a still frame. The only motion rules anywhere in this plugin are the thin ones in `dsn-identity`, and they govern consistency of duration and easing across a brand rather than how movement ranks a frame. Accessibility beyond two contrast ratios and a greyscale test: semantic heading order, screen-reader reading order, alt text and focus order are absent, they are absent from every other file here too, so do not treat a passing contrast ratio as an accessibility review.

## Writing the output

Plain words and full sentences. Name the actual element, setting or measurement rather than characterising it: "the logo is at 180px and reads before the product name at 25 percent" beats "the brand feels dominant". Give the principle first and the change as an option, since the right move depends on a brief you may not have. Name the test each finding came from, so the person can rerun it themselves and get the same verdict. Show the arithmetic whenever a pixel value is involved, because a reader who can follow the numbers can correct them, and a reader given a bare number can only accept or reject it. Say which tests passed as well as which failed, since a pass and a test never run look identical in a list of failures. Where a figure is a working default rather than a derived value, say so in the same sentence you use it.

Sources, corroboration, disagreements, discards and what these sources do not cover are in `references/provenance.md`.
