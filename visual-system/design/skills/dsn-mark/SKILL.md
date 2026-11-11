---
name: dsn-mark
description: Designing or judging a logo, wordmark, monogram or symbol, when a mark feels wrong but measures right, or deciding if it is ownable. Gives a construction and a ladder.
---

# The mark

This skill covers one object: the mark itself, meaning the smallest fixed graphic that stands for a brand. A logo, a wordmark, a monogram, a symbol, an avatar. The single idea underneath it is that a mark does not carry meaning on the day it is drawn and cannot be made to. It is a container. Everything the brand does afterwards is what fills it, and the mark's job is to still be there, unchanged and recognisable, when the filling has happened. That reframes the whole craft. Simplicity, scalability and legibility stop being the point and become the entry requirement, and the real questions become whether the mark is distinct enough inside its own category to be recognised at all, and whether it is built well enough that nobody will need to quietly replace it in three years.

## What this skill is for

Use it when someone wants to:

- derive a mark's idea from a brand rather than from shapes they happen to like
- construct a mark so its proportions hold together under measurement
- correct letterforms and lockups that feel wrong but measure right
- test whether a mark is ownable inside its category, not merely competent
- judge someone else's mark, including an AI-generated one, and say why it fails

The output is a single-sentence statement of the mark's idea, a constructed mark built on two derived numbers, and a pass or fail at each rung of a reduction ladder.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. No controlled study backs any rule in this file, and the whole thing should be read as a method that has worked for working designers rather than as a result. Rules marked **(thin)** rest on a single source and should be treated as one person's house style: usable, but not something to defend as established practice.

Three limits worth naming before you use any of it. The central claim, that a mark accrues meaning rather than carrying it, rests on a small number of documented historical cases rather than on anything systematic. No source behind this skill shows a mark failing in the wild: every case study ends at client approval, which means duration is the merit criterion this skill names and the one thing nothing here tests. And the numeric thresholds in the Applied section are derived from this plugin's canvas assumptions rather than measured on a real device, so they are arithmetic from a stated premise, not measurement.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Mark.** The fixed graphic that stands for the brand. Four shapes it can take: a **wordmark**, the brand name drawn as the mark; a **monogram**, one or more initials drawn as the mark; a **pictorial mark**, a recognisable thing; an **abstract mark**, a shape that depicts nothing.

**Lockup.** The fixed arrangement of symbol and name used together, with the spacing between them specified so it is not re-decided each time.

**Baseline.** The line flat-bottomed letters sit on. **Cap line.** The line flat-topped capitals reach. **Cap height.** Baseline to cap line. **x-height.** Baseline to the top of a lowercase x, which is what actually governs how large type looks.

**Overshoot.** The amount by which a round or pointed form extends past the baseline and cap line. A circle whose diameter exactly equals the cap height reads smaller than a square of the same height, because only a sliver of the circle touches each line, so round forms are drawn slightly taller to compensate.

**Stem.** The main vertical stroke of a letter. **Bowl.** The closed curve of a b, d, o or p. **Shoulder.** The curve leaving a stem in an h, m or n. **Crossbar.** The horizontal stroke of an A, H or e. **Terminal.** The end of a stroke that does not finish in a serif or a join. **Counter.** The enclosed or partly enclosed white space inside a letter or shape, the hole in an o or an a. Counters are the first thing to disappear at small size, because they close up.

**Stroke contrast.** The ratio of a letter's thickest stroke to its thinnest. Low contrast means all strokes are near equal; high contrast means thick stems against hairline joins.

**Tracking.** Uniform space added or removed between every letter in a run. **Kerning.** Space adjusted between one specific pair. **Leading.** Vertical distance between successive baselines. **Measure.** The width of a column of text.

**Geometric centre.** The midpoint of a shape's bounding box, which is what software reports. **Optical centre.** Where a shape looks centred, which is where its visual weight balances. The two differ whenever a shape is asymmetric in weight, which almost every mark is.

**Tonal value.** How light or dark a shape reads when colour is removed and only lightness remains. Two colours of different hue can have the same tonal value, which is why a two-colour mark can collapse into one flat shape in greyscale.

**Reduction.** The set of degradations a mark must survive: small size, one colour, inversion, blur, a circular crop, and being seen upside down.

## Choosing what the mark has to do

This is a decision to make explicitly, before anything is drawn, because the two available jobs pull in opposite directions and a mark cannot be optimised for both at once.

**Job A: the artifact performs now.** The mark is simple, scalable, legible, professional, and correct for its category. It is judged on the day it ships, by whoever is in the room. This job is fully testable and everything in it can be checked in an afternoon.

**Job B: the mark accrues.** The mark means nothing on day one and is understood as a container that everything the brand subsequently does will pour meaning into. Its job is to survive long enough for that to happen: distinct from its neighbours, reproducible in every placement, and unchanged across years. It is judged years later, on whether it became the thing people recognise.

**The trade-off.** Job A pushes toward the conventions of the category, because conventions are what read as competent to a client and what guarantee legibility. That is also exactly what makes a mark interchangeable with its competitors. Job B pushes toward distinctness and mechanical durability, which on day one frequently looks arbitrary, unfinished or wrong, and which is hard to defend in a presentation against a mark that merely looks professional. You will not get both. Pick.

**How this skill resolves it.** Job A is hygiene: necessary, not sufficient. A mark that dies at 32px genuinely dies, so every one of those checks still runs and a failure is still a failure. But passing them is not merit. Merit is ownability inside the category and the ability to survive unchanged. If a mark passes every Job A test and also passes the swap test against twenty competitors, you have both. If it passes Job A and fails the swap test, you have a competent mark that will disappear, and that is a fail, not a pass with a note.

**The corollary: this skill refuses shape psychology.** The claim that squares read strong and reliable, circles read community, angled lines read speed and rounded emblems read togetherness is the strongest form of Job A thinking and has no mechanism under it. The support offered anywhere is a famous mark, an asserted meaning, and the declaration that the meaning explains the mark, which is post-hoc rationalisation of marks that are already famous. That is why the examples are always the same three or four. Do not use it as a reason and do not accept it as one.

Two things survive from that material. **Readability**, because it is testable: a shape either reads as the thing at 32px or it does not. And **association**, which is real but cultural, local, and the client's to supply rather than yours to assert. Ask the client what a colour or form means in their market and record the answer; do not derive it from a chart.

## The principles

Six rules. Each names the test that checks it, and the tests are in the table below.

**1. One idea, sayable in one sentence, before anything is drawn.** Not one shape: one claim, in words, about what the mark asserts. The mechanism is that an idea which needs two sentences is two ideas, and two ideas drawn into one mark produce a composite that reads as neither. If you cannot say it in a sentence, the mark is already too complicated and no amount of refinement will fix that. *Test:* the sentence test.

**2. Design for accrual, not for inherent meaning.** Since the mark will not mean anything on day one, its job is to be a container that survives long enough to be filled. Three properties follow and nothing else matters as much: distinct from its neighbours, reproducible in every placement it will ever appear in, and unchanged across years. Everything else is decoration on top of those. *Test:* the swap test.

**3. Optical beats measured, every time.** Where the software's measurement and your eye disagree about alignment, centring or spacing, the eye wins and the measurement is wrong. The mechanism is that perception responds to distributed visual weight while software responds to bounding boxes, and the two coincide only for shapes that are symmetric in weight. Centre an asymmetric symbol on its bounding box and it will look pushed to one side, because more of its mass sits on one side than the other. *Test:* grid off, eye on.

**4. The unit system comes from inside the design, never imported.** Derive exactly two numbers from the artwork itself, one spacing value and one thickness value, and build everything from those two and their integer multiples. The mechanism is that a repeating unit is what makes a set of shapes read as one object rather than as several, and a unit taken from the design is guaranteed to fit it while a unit taken from outside is not. Three ways to derive them: measure the cleaned paper sketch's own line spacing and line thickness; duplicate a piece of the mark and use it as the measuring unit **(thin)**; or pick the smallest piece of whitespace in the mark, call it 1x, and multiply. An externally chosen ratio, including the golden ratio, is not a derivation. *Test:* two numbers.

**5. It must survive reduction.** Small, one colour, inverted, blurred, cropped to a circle, upside down. Colour should enhance a concept and never rescue one, so build in black first and add colour last. The mechanism is sequencing rather than taste: a mark designed in colour has usually been using colour to separate shapes that are not separated by form, and when it flattens to one colour those shapes merge. Discovering that at the end means retrofitting white gaps into finished artwork to keep its segments apart, which is a repair, not a design. *Test:* the reduction ladder.

**6. Letterforms are a family.** Once rhythm, angle, balance, stroke weight and stroke contrast are set for one character they apply across every character, and the tell of a half-trained hand is one character out of family: a correct letter next to five others that share a different set of rules. Judge it the way you would judge a group of relatives who all share a build except for one. *Test:* the master comparison.

## How to work

### Mode A: making a mark

1. **Set the mode: evolution or revolution.** The criterion is stated, not felt. Revolution when the brand must put distance between itself and something that went wrong, because continuity is the problem. Evolution when it only needs to move forward, in which case you deliberately carry one recognisable element through, which gives existing customers something to recognise. In evolution mode one technique is worth knowing: plot the points where the existing mark's lines intersect, join those dots, and look for new forms in the result **(thin)**.

2. **Ask for exclusions, not just aspirations.** Clients volunteer what they want and almost never volunteer what must not happen, so ask directly and write the answers down as a do-not-do list **(thin)**. An exclusion is worth more than an aspiration because it is falsifiable: you can check a draft against it.

3. **If the brand serves two audiences, find which one is underserved.** Brands routinely brand themselves at whoever pays. Find the side whose absence breaks the paying side's value, and check whether the brand speaks to them at all **(thin)**. A jobs board where employers pay and candidates apply is branded at employers by default, but if nobody applies the employers wasted their money, so the candidate side is the one carrying the risk.

4. **Get the voice before the geometry.** Write five words the brand would never say, five it would overuse, and one sentence it would post **(thin)**. The voice sets the emotional temperature and the mark has to match it, because a brand that speaks calmly cannot carry a shouting mark and the mismatch is visible to readers who could not name it.

5. **Survey the category and find the gap.** Open twenty marks from the client's industry, put them on one artboard at the same size, delete every brand name, and ask how many could swap places unnoticed. Then decide deliberately whether to differentiate or to comply, and write down which you chose and why. Run the same pass on colour: pull a three-swatch palette from each competitor's site and lay them side by side. If every competitor has an accent colour and the client has none, that is a gap you can state as a fact rather than an opinion you have to defend.

6. **Open the real placements before the artboard.** Mockups first, not last, with the brand name set in plain text and nothing designed yet. The mechanism is tunnel vision: a mark crafted on a white artboard is crafted against the wrong background, at the wrong size, with no competing elements, and it will look like a different object the moment it sits in its real context. Seeing the real environment first changes what you draw.

7. **Sketch on paper, including the bad ones.** Two mechanisms. Constraint: a vector program offers too many moves and a pencil removes the distraction of all of them. And externalisation: an idea that seems terrible in your head often opens other avenues once it is down, and one that seems amazing frequently does not survive being drawn. Paper is the test, not your head.

8. **Generate from the brand's own material, three ways.** *Word association:* expand seed words into two maps, then combine pairs across the maps. *Abstract value made concrete:* take an abstract word the brand owns and find the physical form of it, so "disconnect" becomes an unclosed shape or a broken link and "obscure" becomes occlusion or cropped characters. *Name to primitive:* take what the name literally denotes, reduce each referent to a base shape, then combine them **(thin)**. A deli named after a mix of onion, carrot and celery becomes a circle, a triangle and a rectangle combined, with the gap between them carrying the third ingredient.

9. **Expect the idea to arrive from outside the brief.** The best concepts routinely come from an off-hand remark or a photograph rather than from the brief: a client explaining their own name mentions rooting for the underdog, and that becomes the mark; a team notices the shape of the client city's skyline. The operative instruction is to listen to everything the client says, not only to the parts you have decided are important.

10. **Build in black, from a restricted inventory, on units derived from the design.** Clean the chosen sketch on paper first, derive the two numbers from it, and construct against those. Reuse shapes rather than drawing freehand curves: assemble the mark from a small set of repeated pieces, like a jigsaw. The mechanism, and this is what the golden-ratio material is actually doing when it appears to work, is that a restricted shape inventory produces consistent curvature across the whole mark, and consistent curvature is what reads as resolved.

11. **Correct optically, one change at a time, verifying direction before continuing.** Fix one character or one element, stop, and confirm the fix moved in the right direction before applying the same correction to everything else. Duplicate before each edit so you can fall back and so the sequence of changes stays visible and reviewable.

12. **Resolve the lockup last, and let it override the symbol.** Match the symbol's stroke weight to the type's stem width or the pair reads as two logos stuck together. Expect the symbol's orientation to change for the lockup rather than for its own sake: a symbol developed standing alone frequently does not flow beside text and has to be flipped. Match a secondary line's width to the primary line with tracking rather than with size, within the limit computed in the Applied section. Putting the symbol inside a letter is a common move and usually reads clunky.

13. **Run the reduction ladder, then add colour last.** If anything will ever be printed, choose in CMYK first and then find the nearest spot colour **(thin)**, because spot inks and screen RGB both reach brights that the four-colour process cannot hold, so a bright orange chosen on screen prints muddy and the client discovers it on delivery.

14. **Mirror, rotate and repeat the finished mark before you stop.** System and campaign assets turn up here and nowhere else, cheaply. A mark mirrored can produce a second usable form; a shape from the discard pile can become the photo frame used across all the collateral. Ten minutes of this is the highest-yield time in the whole process.

15. **Present in context, with three to five directions and your opinion on each.** Mockups are what make a client able to judge at all: shown a mark on a white page they will critique the wrong things, because they have nothing to judge it against. Planting a deliberate non-favourite to calibrate the reaction is a standard move, either as a radical stretch concept that must still be on brief and still be good, or as a deliberately plain control. Name what that is: an anchoring device. It is legitimate when every option presented is one you would actually make, and it is manipulation when it is not.

### Mode B: judging a mark

1. **Say the idea in one sentence from the mark alone**, without reading the brief. If you cannot, that is the finding and you report it first.
2. **Run the reduction ladder** and report the first rung that fails, not all of them.
3. **Run the swap test** against twenty category marks with the names removed.
4. **Audit optically:** overshoot on round and pointed forms, symbol stroke weight against type stem width, optical against geometric centre, and the mark upside down, which stops you reading text and forces you to see shapes, exposing misalignment you had been reading past.
5. **Audit the letterform family** against a drawn master, per the section below.
6. **Name what is carrying the concept.** Remove colour: if the concept dies, colour was carrying it. Remove the gradient, the shadow, the custom terminal, one at a time. Whatever kills it was doing the work, and if that thing is not form, there is no concept yet.
7. **Check for unintended reads.** Marks routinely carry a second read nobody intended: blocks that read as pointing backwards, bistable like an optical illusion; an A that reads as two separate words; a shape combination that reads as a face. Check letter identity too, because an E can read as a C, and that is usually fixed by pushing one corner in rather than by redrawing.
8. **Report** per the Writing the output section.

## What a grid does, and what it does not do

A grid is a repeating unit laid over the artwork so that spacings and thicknesses can be held consistent. It is a construction aid applied to a design that already exists, and it belongs in the later stages of the work. Decide what the mark is before bringing it to a grid.

The failure to avoid is treating the grid as generative. A grid does not produce an idea. Starting from one produces marks that are arrangements of circles, because circles are what grids are made of, and the result is a mark that measures beautifully and claims nothing. The sequence that works is: idea in words, sketch on paper, derive two numbers from the sketch, then construct, then turn the grid off and correct by eye.

The second failure is treating the grid as proof. The elaborate construction diagrams in portfolio presentations, with the anchors and the tangent circles and the golden spirals, are generated from already-finished artwork at the click of a button. They are a presentation asset and they show professionalism to a client, which is a real and legitimate function. They are not evidence that the mark was built rigorously, and you cannot read rigour off one. Judge the mark.

So the grid's actual job is narrow and worth doing: two numbers, one spacing value and one thickness value, repeated everywhere, plus a small set of reused angles. That is the whole benefit. Where the grid and the eye disagree, the eye wins, and spacing does not have to land on the grid, particularly beside type, because type has to be balanced optically and type's own spacing was never built to your unit.

## Correcting letterforms against a drawn master

This is the most delegable procedure in the skill, because it replaces taste with a reference. **(thin)** Set the same word in a well-drawn typeface from a reputable foundry, convert it to outlines, and compare your letterform against it point by point. Five things to compare.

**Overshoot.** Round and pointed forms must pass the baseline and cap line. Too much overshoot is as wrong as none, and the failure mode of a geometric monogram is almost always none, because the shapes were drawn to a grid that had no overshoot in it. Fix by scaling the round character optically, in single percent steps, and recheck at each step.

**Stroke relationships.** In a well-drawn face the bowl's curve and the shoulder are slightly thicker than the vertical stem, and the diagonal is wider than the vertical, because a curve passing the baseline tangentially presents less ink to the eye at the same measured width. Check yours against the master and expect to find them equal, because equal is what you get by drawing with a uniform stroke. Equal is the defect.

**Contrast era.** The ratio of thick to thin strokes is a period marker. High contrast belongs to a particular era of type, and a letter whose contrast ratio does not match the rest of its family reads as imported from a different time, which is a thing viewers notice without being able to name.

**One flourish, not every letter.** A custom terminal on one character reads as craft. The same move on all of them reads as a theme, and a theme is a style applied rather than a letter drawn.

**Name the part.** Terminal, crossbar, bowl, shoulder, stem, counter, overshoot. Naming the part is how a correction gets communicated instead of gestured at, and a correction nobody can repeat is not a correction.

Use the master as a reference for how letters are drawn. Do not use it as artwork to copy.

## Tests

In this order. Each returns a verdict decidable with nothing but this file and the mark.

| Test | Catches | Verdict |
|---|---|---|
| **1. Sentence** | A mark with no idea, or two ideas | Without reading the brief, write the mark's claim as one sentence. Fail if you cannot, or if it takes two sentences, or if the sentence is a description of the shape rather than a claim. |
| **2. Swap** | A competent mark that will disappear | Twenty category marks plus yours, same size, all names deleted. Count how many could trade places with yours unnoticed. Fail if the answer is more than zero. |
| **3. Reduction ladder** | Everything that small size and one colour expose | Run six rungs in order and report the first failure. 1: scale to 25% in steps. 2: flatten to one colour. 3: black on white, then white on black. 4: blur until edges are soft, or glimpse for one second. 5: crop to a circle and render at 32pt. 6: turn it upside down. Fail at the first rung where you cannot name the shape, or where two parts merge, or where a counter closes. |
| **4. Two numbers** | A decorative unit system | Measure every gap and every stroke width in the finished mark. Fail if the values are not one spacing number, one thickness number, and integer multiples of those two. |
| **5. Grid off, eye on** | Geometric centring mistaken for balance | Hide every guide, draw a box around the lockup, shrink it to thumbnail size, squint. Fail if one side feels heavier. Then nudge and recheck, and keep the nudge if the second look is better. |
| **6. Master comparison** | A letter drawn with a uniform stroke | Set the same word in a well-drawn face, outline it, overlay. Fail on any stroke relationship that is equal in yours where the master's is unequal, and on any round form that does not overshoot. **(thin)** |
| **7. Unintended read** | A second read you cannot see because you know the intent | Show the mark to three people with no priming and ask what they see. Collect the wrong answers rather than arguing with them. Fail on any wrong answer given by two of the three. |
| **8. Carrying** | A concept that is actually an effect | Remove colour, then gradient, then shadow, then any custom detail, one at a time. Fail if the mark stops reading when anything other than form is removed. |
| **9. Thirty-minute redraw** | Memorability, which no other test here can fail | Show the mark to someone, wait thirty minutes, ask them to draw it from memory. Fail if what they draw is not recognisably your mark. **(thin)** |
| **10. Two grounds** | A one-colour mark that only works on one background | Render the single-colour mark on white and on black. Fail if the same value does not clear a 4.5:1 contrast ratio on both, unless you are shipping two versions and have said so. **(thin)** |

## Anti-patterns

- **A construction grid presented as evidence of rigour.** Generated after the fact, usually automatically. It proves a plugin ran.
- **The golden ratio offered as justification.** The mechanism is a restricted shape inventory, and any consistent ratio set does the same work. 1.618 is a convention here, not a principle.
- **Colour rescuing the concept.** If flattening to one colour kills it, there is no concept yet, and adding a gradient is not a fix.
- **Centring on the bounding box.** Visual weight, not geometry.
- **Shape psychology as a reason.** No mechanism anywhere under it.
- **Designing on a white artboard.** Produces over-detailed marks that fail in every real placement, and you find out at handoff.
- **Correct-for-the-category as the goal.** A mark that conforms perfectly conforms so well that it disappears, which is a fail with good manners.
- **A convention adopted without a stated reason.** All-lowercase, a single weight, a circular container: each is fine with a reason and a liability without one. One real case for refusing all-lowercase: beside a lowercase symbol it would have read as a doubled letter.
- **Settling on the first iteration.** The cheapest and most common failure available. Do not ship iteration one, and do not treat "it already works" as a reason to stop.
- **Keyword-searching a palette generator.** Typing the brand's industry into a colour tool and taking what comes out. The competitor-gap pass in Mode A step 5 replaces this and produces a defensible answer instead of a mood.

## Applied to a personal brand mark and a 1:1 avatar

This is the dominant case for a LinkedIn or Substack operator, and it is the hardest version of the reduction ladder, because the avatar is the mark's primary placement rather than its smallest one. Canvas assumptions, including the downscale factor used below, are in `reference/canvas-assumptions.md`: a 1080px asset lands in a feed column near 360 device-independent pixels, so the nominal downscale is 1080 / 360 = 3x, and the stress case is 4x.

**What the avatar placement actually is.** A circular crop, 32 to 48pt beside a name, on both a light and a dark app background. **(thin)** Work at the strict end: 24pt, which is where the smallest avatar placements sit.

**Minimum feature size, computed.** Draw at 1080 x 1080. A 24pt avatar on a 3x-density screen is 24 x 3 = 72 device pixels. The reduction factor from the working file is 1080 / 72 = 15. A feature needs at least two device pixels to read as a feature rather than as a smudge, so its size in the working file must be at least 2 x 15 = 30px. Round up to 32px. At the more common 32pt avatar the factor is 1080 / 96 = 11.25 and the floor is 23px, so 32px covers both. This is the number that governs the whole mark: **no stroke, gap or counter in the avatar version may be narrower than 32px at 1080.**

**What the circular crop eats.** The circle inscribed in a 1080 square has diameter 1080. The largest square that fits inside that circle has side 1080 / sqrt(2) = 763.7, so 764px, centred. That leaves (1080 - 764) / 2 = 158px trimmed from each side, and the crop removes 1 minus pi/4 of the square's area, which is 21.5 percent. So every element of the mark lives inside a centred 764px square, and the 158px band around it is sacrificial. A mark that fills the 1080 square loses a fifth of itself here.

**A worked monogram.** Idea in one sentence, then the two numbers. Thickness unit t = 36px, chosen because it clears the 32px floor and because 36 = 12 x 3, which is this plugin's working-file floor for a 12pt rendered element **at the nominal 3x downscale**, so one number serves both constraints. The stress-case floor is 12 x 4 = 48px, and t is deliberately not set there: a stroke is a mark that has to be seen rather than text that has to be read, and the ladder check below is what holds it, since t at the 4x reduction is 9px and still solid. Spacing unit s = 1.5t = 54px, giving the gap series 54, 108, 162. Counters get 1.5t = 54px minimum, because a counter equal to the stroke width closes up before the stroke disappears. Cap height H = 10t = 360px, which sits comfortably inside the 764px safe square and leaves room for the glyph's width. Overshoot on round forms: 1.5 to 2 percent of cap height **(thin)**, so 360 x 0.015 = 5.4px to 360 x 0.02 = 7.2px, meaning a circular O is drawn at 371 to 374px diameter against a square H of 360. At 24pt that overshoot is 5.4 / 15 = 0.36 device pixels and individually invisible, which is the point: it is not a visible detail, it is the thing that stops the O reading small.

**Verify against the ladder.** Rung 1, 25 percent of 1080 is 270px, and t at 270 is 36 / 4 = 9px, still solid. Rung 5, 24pt circular: t is 36 / 15 = 2.4 device pixels, which clears the two-pixel floor by a margin of 0.4. That margin is the entire safety budget, so a decorative detail at half the stroke width, 18px, lands at 1.2 device pixels and will not survive. Cut it.

**Rung 3, computed.** A single-colour mark that must sit on both the light and dark app background cannot use an arbitrary mid grey. Contrast ratio against white is (1.0 + 0.05) / (L + 0.05) and against black is (L + 0.05) / 0.05, where L is relative luminance. Those two are equal when (L + 0.05) squared = 0.0525, so L = 0.179 and the ratio is 4.58:1 on both grounds. In practice #767676 has L = 0.181, giving 4.54:1 on white and 4.62:1 on black. Anything lighter than that pivot fails on white and anything darker fails on black, so a one-value mark for both grounds is pinned to roughly that grey, which is usually unacceptable for a brand. The real answer is two versions, a dark one for light grounds and a light one for dark grounds, specified in the lockup rules. The 4.5:1 threshold itself is borrowed from text contrast guidance rather than derived for marks **(thin)**; use it as a working default and say that you did.

**The lockup, and the conflict it creates.** On a 1080 x 1350 portrait slide, put the name at cap height C = 96px, which renders at 96 / 3 = 32pt and is comfortably the hero of the slide. A semibold sans has a stem width near 12 percent of cap height, so 96 x 0.12 = 11.5px, round to 12px. Principle 12 says match the symbol's stroke to the type's stem, so the lockup symbol's stroke is 12px. But the avatar version's stroke is 36px, three times heavier. **These are two drawings of the same symbol, not one drawing used twice.** Shipping the lockup symbol as the avatar puts a 12px stroke through a 15x reduction, giving 0.8 device pixels, and it vanishes. Shipping the avatar symbol into the lockup puts a 36px stroke beside a 12px stem, and the pair reads as a heavy icon glued to light type. Specify both, and say which goes where.

**Gutter between symbol and name.** Start at half the cap height, 96 / 2 = 48px, then nudge optically, because a round symbol needs less gap than a square one at the same measured distance: its edge curves away from the type while a square's edge stays parallel. Compute the start, then run grid off, eye on, and keep the nudge.

**Matching a secondary line by tracking, and when it stops working.** Principle 12 says match width with tracking rather than size, and that rule has a computable range of validity. Say the primary wordmark "MARK" sits at C = 96px and measures 290px wide, and the secondary "STUDIO" at C = 48px measures 230px. The deficit is 60px over 5 inter-letter gaps, so 12px per gap. At C = 48 the em is roughly 48 / 0.7 = 69px, so 12 / 69 = 0.17 em of tracking. Tracking past roughly 0.25 em starts reading as separated letters rather than a word, so 0.17 em is inside the limit and the rule works. Now take a long secondary: "DESIGN STUDIO" at C = 32px measures 198px against a primary of 712px. The deficit is 514px over 12 gaps, so 42.8px per gap, and at C = 32 the em is about 46px, making that 0.93 em. Four times the limit. **So the tracking match only works while the width deficit is under about 20 percent of the primary's width.** Beyond that, shorten the secondary line or raise its size. The inherited rule is correct inside a range and silent about the range, so compute it before applying it.

**Three more things specific to this case.** The name is already present beside an avatar, so the mark does not have to say it, and this is the one case where an abstract mark or a monogram has an easier job than a pictorial one. Design to fit a square from the outset rather than fitting a wide mark into one later **(thin)**, because the app icon and the favicon are both square and both non-negotiable. And deployment has changed: the placements that matter now are an email signature, a feed avatar and the small thing beside a URL, all of which can be changed in an afternoon, where signage and vehicles could not. **(thin)** Treat the mark as changeable and the system as the durable thing.

**Prefer a system over a fixed mark.** A logo system is a graphical framework with endless permutations rather than a single fixed artifact: a form built so it can hold any colour, any fill, any crop, and still be the same mark. **(thin)** For a personal brand that posts daily this is the right default, because the mark then functions as a design asset that generates covers, slide corners and section markers, rather than as one object to slap on everything.

## Checklist

- [ ] Job named: artifact-now or accrual, with the trade-off acknowledged
- [ ] Mode set: evolution or revolution, with the criterion stated
- [ ] Exclusions asked for and written down
- [ ] Underserved audience identified, if there are two
- [ ] Voice captured before any geometry
- [ ] Category surveyed, gap named, differentiate-or-comply decided deliberately
- [ ] Real placements open before the first sketch
- [ ] Sketched on paper, bad ideas included
- [ ] Idea sayable in one sentence
- [ ] Built in black, two numbers derived from the design
- [ ] Minimum feature size computed against the smallest placement
- [ ] Optical corrections made one at a time, direction verified
- [ ] Lockup resolved, symbol stroke matched to type stem, second weight specified if needed
- [ ] Reduction ladder run, first failure recorded or none
- [ ] Swap test run against twenty category marks
- [ ] Colour added last, CMYK-first if it will ever print
- [ ] Mark mirrored and rotated to find system assets
- [ ] Presented in context, every option one you would actually make

## The ultimate test

Not whether it is good. Whether it can still be used, unchanged, in ten years, by people who will give it whatever meaning they end up giving it.

The practical form of the question: if this brand becomes well known, does this mark become the thing people recognise, or the thing that has to be quietly replaced first? Stop judging the splash the mark makes when it lands and start judging how long it stays above water. Those are different competitions, and almost every argument about a new mark is conducted in the wrong one.

## What an agent can run, and what it cannot

**Can run, fully:** the reduction ladder, every rung, since each is a render and a named failure. Two numbers, by measuring every gap and stroke. The swap test, given the twenty category marks. The unintended-read check, by describing what it sees before being told the intent. The master comparison, given both outlines. The optical audit for overshoot and for stroke-to-stem matching. Naming what carries the concept, by removing one attribute at a time. Every computation in the Applied section.

**Cannot run:** the thirty-minute redraw, which needs a person and a delay. Cultural association, which belongs to the client. The final optical nudge, which is a judgment about felt weight that an agent should propose and a person should confirm. And the duration question, which no test answers in the present.

**Worth delegating deliberately:** the swap test and the unintended-read check, because both are corrupted by knowing the intent. Whoever made the mark is the worst available person to run them.

## Where this skill should lose

**When the question is which typeface to use for a wordmark.** Use `dsn-typeface`. This skill tells you to compare a drawn letterform against a well-drawn master and says nothing about how to choose one.

**When the question is how to set type: size, leading, tracking, kerning, measure.** Use `dsn-typeset`. This skill specifies a lockup's internal relationships and stops at the edge of the lockup. Anything that is running text rather than a mark belongs there.

**When the question is which colours the brand uses.** Use `dsn-palette`. This skill only says build in black, add colour last, and check two grounds. Constructing the set is a different job.

**When the question is a set of small shapes that must work as a family.** Use `dsn-icon`. One mark and a system of twenty icons share vocabulary but not method: a mark optimises for distinctness and an icon set optimises for internal consistency and immediate readability, and those pull apart.

**When the question is everything the mark sits inside.** Use `dsn-identity`. Layouts, templates, photography treatment, rules for who may use what where. This skill ends when the mark and its lockup are specified. If you are asking what the brand looks like rather than what the mark is, close this file.

**When the question is whether a specific colour pair is readable.** Use `dsn-contrast`. The two-grounds arithmetic here is a single derivation for a single case and is not a general method.

**When the question is the page the mark sits on.** Use `dsn-grid`, which owns the margin, the column count, the gutter and which columns an element spans. The construction grid in this file is scaffolding for one drawing: it governs proportions inside the mark and sets no position on any canvas, so reading it as a layout grid is the most common misuse of this file. The related question of how much clear space must surround the mark, stated in units of the mark itself so it survives a billboard and a 1080 pixel square, is `dsn-identity`.

**When the numbers in the construction have to be handed over as named values.** Use `dsn-tokens`. This skill settles the two derived numbers a mark is built on and the lockup's internal ratios; giving them names that a build step resolves is that file's job, and it decides none of the numbers.

## Writing the output

When judging, report in this order and nothing else:

1. The mark's idea in one sentence, as you read it cold.
2. The first rung of the reduction ladder that fails, or none.
3. The swap-test result as a count.
4. What is carrying the concept.
5. Ranked findings, each naming the defect and the test that caught it, and leaving the fix to the designer.
6. One verdict: ready, revise, or no concept yet.

Give numbers with their units and never a characterisation: "the counter closes at rung 5, measured 22px against a 32px floor" beats "it gets muddy when it's small." Say which tests you ran and what each returned, including the passes, because a pass and a skipped test look identical in a summary that only lists failures. Label a borrowed default as a borrowed default at the point you use it. If a finding rests on a rule marked **(thin)** in this file, say so inside the finding. Do not rewrite the mark in prose and do not offer encouragement.

Sources, corroboration, contested claims, claims refused and what was read and left out are in `references/provenance.md`.
