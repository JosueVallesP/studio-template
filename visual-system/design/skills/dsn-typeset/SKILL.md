---
name: dsn-typeset
description: Setting size, leading, tracking and measure, building or repairing a type scale, when text is too small to survive a feed, or type reads badly and the face is fine.
---

# Setting type

This skill sets type that has already been chosen: the size of each level, the space between the lines, the space between the letters, and the length of the line. Legibility is governed by the relationship between three quantities rather than by any one of them: the line length, the size and the space between lines move together, and changing one without recomputing the others is how a block of type that was fine at one size becomes unreadable at another.

## What this skill is for

Use it when someone wants to:

- set size, leading, tracking and measure on a piece being built
- build or repair a type scale and the named style set that sits on it
- decide the smallest type size that survives being viewed in a phone feed
- judge whether an existing block of text is legible at the size and distance it will actually be read
- work out why text looks wrong when the typeface is not the problem

The output is a scale of four to six named styles, each with its size, leading, tracking and expected character count, plus a verdict per test.

## Confidence

The rules here are practitioner accounts and arithmetic derived from them, not measured findings. Nothing in this file rests on a study of reading: no comprehension, reading-speed or recall result stands behind any setting, and the one body of measurement available records what other teams shipped rather than what read better. Rules marked **(thin)** rest on a single source and should be treated as one person's house style. Figures labelled **derived** are computed in this file from the canvas assumptions and can be rebuilt on different ones; the arithmetic is shown so you can.

Claims about what a setting signifies rather than whether it can be read, for instance that tight tracking reads as strength and loose as luxury, or that sharp serifs read as authority, are assertions about reception with nothing offered in support **(thin)**. On a feed where engagement is measurable, measure those rather than inherit them.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Em.** A unit equal to the current type size. At a 48px size, 1 em is 48px and 0.02 em is 0.96px. Ratios expressed in ems survive a size change; absolute pixel values do not.

**Working size and rendered size.** The working size is the number in the design file. The rendered size is how large the same text is when a viewer actually sees it, after the image has been scaled down to fit the column it appears in. These differ by the **downscale factor**: a 1080px-wide graphic shown in a feed column about 360px wide has a downscale factor of 3, so a 48px working size is a 16px rendered size. Rendered sizes in this file are called **effective pixels** to keep them distinct from working-file pixels.

**Baseline.** The invisible line the bottoms of most letters sit on. The round letters dip very slightly below it, which the type designer drew in deliberately.

**x-height.** The height of a lowercase x, measured from the baseline. It is the height of the letters a reader actually sees most of, so it governs legibility at small sizes far more than the nominal size does: two typefaces set at the same size can differ by a third in x-height and therefore in apparent size **(thin)**.

**Ascender and descender.** An ascender is the part of a letter rising above the x-height, as in b, d, h, k, l. A descender is the part dropping below the baseline, as in g, j, p, q, y. The distance from the top of the ascenders to the bottom of the descenders is the font's real vertical span, and it is close to 1 em in most text faces, which is why leading below about 1.05 makes descenders and ascenders collide.

**Counter.** The enclosed or partly enclosed white space inside a letter, for instance the hole in an o or the loop of an a. Counters are what let a reader tell letters apart at small size.

**Aperture.** The width of the opening where a counter is not fully closed, for instance the gap at the right of a c or the top of an a. A closed aperture makes a c read as an o once the type is small **(thin)**.

**Stroke weight.** The thickness of the lines a letter is drawn with. **Stroke contrast** is the difference in thickness between the thick and thin strokes within a single letter. High stroke contrast means the thin strokes are much thinner, and those thin strokes are the first thing to disappear when type is scaled down.

**Weight.** A named cut of a typeface at a given stroke thickness: light, regular, medium, semibold, bold, usually numbered 300, 400, 500, 600, 700. Adjacent weights are the two next to each other on that list.

**Measure.** The length of a line of text, counted in characters including spaces, not in pixels. Counting in characters rather than width is the whole point: the difficulty of finding the next line depends on how far the eye travels relative to the size of the letters, and a character count already has the size built into it, while a pixel width does not. A 860px line is a long line at 36px and a short one at 96px. To convert a column width into a character count, divide the width by half the type size, since the average character in a mixed-case grotesque occupies roughly 0.5 em **(thin)**: characters = width / (0.5 x size). That 0.5 figure is an estimate made for this file rather than a measurement, and it is checkable by setting the real string and counting.

**Return sweep.** The eye movement from the end of one line back to the start of the next. It is the thing that fails when a measure is too long: the eye has to travel further back and has less to aim at, so it lands on the line it just read or the one after the one it wanted.

**Leading.** The vertical distance from one line's baseline to the next, in a block of text. Set it as a ratio of the type size rather than as an absolute, so that changing the size later does not silently break it. Leading 1.40 at a 48px size is a 67px baseline-to-baseline distance.

**Line height, and where it differs from leading.** In CSS and in Figma, the line-height field sets the height of the **line box**, the invisible rectangle each line of text occupies. Within a paragraph at a single size, line box height and baseline-to-baseline distance are the same number, so there leading and line height are interchangeable. They stop being interchangeable at the edges of the block: the difference between the font's natural height and the line box is split equally above and below every line, including the first, so a block set at line height 1.4 sits roughly ((1.4 - 1.0) / 2) x size below the top of its own frame, about 10px at a 48px size. Align the first baseline to your grid, not the text frame. In InDesign the leading field is an absolute baseline-to-baseline measurement in points, and its automatic value is 120 percent of the size, so it behaves as a ratio and reports as an absolute. The old notation "12 on 14" means 12pt type with 14pt baseline-to-baseline, which is 2pt of *added* space, not total; so a leading quoted as "2 points" is the added kind and one quoted as "120 percent" or "1.2" is the total kind. Everything in this file is the total kind.

**Tracking, and how it differs from kerning.** Tracking is one value applied uniformly to every letter pair in a run of text, expressed as a fraction of the em, usually as a percentage. Kerning is an adjustment to one specific pair, for instance the gap inside "AV" or under the arm of a "T" in "To". When this file says change the tracking, you change one field on a style and every pair in that run moves together. When it says kern, you select individual pairs on one line and move them by eye. Tracking is a scale decision made once per level; kerning is a hand correction applied to display type only. Tracking is also expressed in thousandths of an em in some tools, where 20 means 0.02 em, which is 2 percent.

**Optical and geometric.** A geometric judgement is made by measurement; an optical one is made by eye against what the eye reports. Kerning is optical by definition, because equal measured gaps between letter pairs do not look equal: the gap beside a round O and the gap beside a straight-sided H carry different amounts of white.

**Type scale and ratio.** A type scale is the set of sizes a piece is allowed to use. A ratio scale generates them by repeated multiplication from a base size: base 48 at a ratio of 1.25 gives 48, 60, 75, 94. Ratio names are borrowed from musical intervals and carry no perceptual claim, so treat them as labels on a dropdown: major second is 1.125, minor third 1.2, major third 1.25, perfect fourth 1.333. A **step** is one multiplication. A **ramp** is the whole generated list, which is longer than the set of sizes a piece should use.

**Named style.** A saved definition combining size, leading, tracking, weight and case under one name, so that one edit propagates to every instance. A **style set** is the four to six named styles a piece is allowed.

**Rag.** The uneven edge of left-aligned text on its right-hand side. A **staircase rag** is a rag whose line ends step evenly in one direction, which draws a diagonal the reader sees as a shape rather than as text. A **river** is a vertical channel of white running down through several lines of a justified block, caused by word spaces stretching to fill the measure and happening to align. A **one-word last line** is a paragraph whose final line holds a single word.

On the last of those: name the artifact rather than the term. The words widow, orphan and runt are used with swapped meanings by different practitioners, so "a one-word last line" and "a heading left alone at the bottom" cannot be misread and the terms can. Use the descriptions.

## The mechanism: leading is set from the character count, not from the size

A type scale looks like a list of sizes and behaves like a list of measure-and-leading pairs.

A long measure needs more leading, because the eye travels further back on the return sweep and needs a wider band of white to land on. A short measure needs less, because a wide white band stops holding the lines together as a block and starts separating them into unrelated strips. Size enters only through the measure: at a fixed column width, a larger size puts fewer characters on the line, which is a shorter measure, which wants tighter leading.

That is why leading appears to fall as size rises. Measured across shipped design systems, display type sits near 1.20 and body type near 1.47, and the obvious reading is that the cause is size. It is not. Display is set tight because a display line in a wide browser column holds about eighteen characters; body is set loose because a body line holds about sixty. Take that same display ratio and apply it to a display line running the full width of a wide column and it fails, because now the measure is long. Take the body ratio and apply it to a twenty-character column and it fails in the other direction, because the lines come apart. The correlation with size is real and the attribution to size is wrong, which is why a scale copied from a product system fails on a post graphic.

So the rule is: never copy a leading value out of a scale row. Count the characters on the line and set the leading from the count.

## The principles

**1. Fix the two extremes from constraints, then fit the ratio to them.** The floor is the smallest size that is still readable once the piece has been scaled down to the width it will be seen at. The ceiling is the size at which the longest real display string holds the number of characters you want on the line. The ratio is whatever connects the two across the number of steps you need. Choosing a ratio first and fitting the content to it is the common order and it is backwards: it produces headlines that do not fit beside captions nobody can read, because neither end was ever a constraint. Checked by the style audit, and by stating both extremes and their derivation before any ratio is named.

**2. A step has to be visible at rendered size, not at working size.** A ratio of 1.125 puts a 48 beside a 54. Divide both by a downscale factor of 3 and that is 16 beside 18, a difference of two effective pixels, so the two levels are one level wearing two names. Checked by the step visibility test.

**3. Set leading from the character count on the line.** Count the characters on the longest real line, then set the ratio from the count: under 25 characters wants roughly 1.05 to 1.20, 25 to 50 wants 1.30 to 1.45, and 50 to 75 wants 1.40 to 1.55 (**derived** from return-sweep distance; the bands stated by practitioners are by role rather than by count, 0.80 to 1.20 for headings and 1.20 to 1.60 for body **(thin)**, which is the same gradient with the cause misnamed). Above 75 characters, narrow the column rather than add more leading, because leading cannot repair a measure. Checked by the character count test, then the leading-against-count test, then the return sweep.

**4. Keep every descender clear of the line below.** The font's ascender-to-descender span is close to 1 em, so a leading ratio below about 1.05 drives descenders into the ascenders beneath them (**derived**: the figure is this file's estimate of the span, not a measurement of your font, so run the test rather than trusting the number). The failure is visible before it is a collision: a descender reaching the bottom of its own text frame means the white band below the line has already stopped reading as a gap. Checked by the descender test. A failure here cannot be compensated anywhere else in the file.

**5. Tracking runs opposite to size, because what it adjusts is the contrast between letter shapes.** At display size the gaps between letters already read clearly, so leaving the default open spacing makes the word fall into separate letters and closing it slightly makes the word one shape, which is what a display line should be. At small size the letters are close to merging, so opening the spacing restores the distinction between them. Negative tracking at the top of the scale, zero in the middle, positive at the bottom. Checked by the tracking triangulation test.

**6. Caps always need positive tracking, and running text never needs any.** Capital letters were spaced by the type designer to sit in a lowercase run, so a string set entirely in caps comes out too tight. Tracking lowercase running text damages it instead: readers recognise a word by the outline its ascenders and descenders make, and spreading the letters destroys the outline. Tracking belongs to caps, small caps and display only. Checked by the tracking triangulation test.

**7. A level needs two properties changed, not one.** Size alone at a small ratio is not a level, and neither is weight when the weights are adjacent: regular beside medium reads as a mistake rather than as emphasis. Skip at least one weight between any two levels in use, and skip three where you want strong contrast. This is also why five weights is a sensible requirement when choosing a family **(thin)**: with four you cannot skip one and still have a top and a bottom. Checked by the weight gap test.

**8. Kern display type by hand, and never kern running text.** Automatic kerning is built from pairs measured at text size and it fails on large type and on caps, where the gaps are large enough for the eye to judge directly. Kerning is optical, so the only verdict is what the eye reports at the real size. On running text, hand kerning is wasted work and risks introducing inconsistency between two instances of the same pair. Checked by the detail sweep.

**9. Cap the style set at six named styles and build every value from the scale.** Four is enough for most single-frame graphics: one display line, one subhead, one body style and one label. A seventh named style means a decision was improvised rather than derived (**derived**: a product design system typically carries around sixteen text styles because it covers dense application screens, and a post graphic has neither the surfaces nor the rendered room for them). Save them as styles, not as local overrides, so one edit propagates. Checked by the style audit.

**10. Set paragraph spacing to at least 1.5 times the line box, and do not indent as well as space.** The lines inside a paragraph are already a group held together by their leading, so the gap that separates one paragraph from the next needs only to be clearly larger than that leading, not as large as the gap between two different blocks of content. Indenting and spacing together marks the same boundary twice. Checked by the style audit.

**11. Align left, and centre only short lines, three at most.** Centring costs the reader the fixed left edge their eye returns to on every sweep, which only matters once there is enough text for the sweep to repeat. A single-frame graphic is closer to a poster than to a page of running text, so a centred display lockup of two or three lines is normal and a centred paragraph is not. Do not justify: even on a fixed canvas that never reflows, word spaces stretch to fill the measure and rivers open inside the block. Checked by the detail sweep.

**12. Nothing below the rendered floor exists as a level.** If a level cannot be read at the width the piece will be seen at, the fix is to delete the level and fold its content into the one above, or to cut the content. Nudging the size up by a step inside the same scale just moves the failure. Checked by the floor check.

**13. Re-run the whole scale against the longest real string before you call it done.** A scale built against sample copy is a scale tested once. The way it actually fails is on its twentieth use, when the headline is two words longer than the one it was fitted to. Checked by the content stress test.

## What carries to a fixed canvas, and what does not

Most available guidance assumes a screen of unknown width rendering text live at the size you typed. A fixed image in a feed has one known width, one rendering, and every size divided by the downscale factor before anyone sees it. Sort the guidance by which of those it depends on.

**Carries over unchanged: everything unitless or perceptual.** Every ratio and its name. Leading and tracking expressed as ratios of the size. The measure band expressed in characters. The weight-skip rule. x-height, aperture, counter and stroke contrast as criteria for small-size legibility. The idea of four role levels, display, heading, body and label, as a useful division of labour **(thin)**.

**Does not carry, and why:**

- **Root-relative units.** A unit defined as a fraction of a document's root size has nothing to be relative to on a canvas, because a canvas has no root size.
- **Fluid size formulas and width-breakpoint variants.** Both solve the problem of text reflowing across unknown viewport widths. A fixed canvas has one width. What it needs instead is a floor, because the single rendering is a uniform downscale rather than a reflow.
- **Absolute default sizes.** A 16px body, a 12px minimum, a 48 to 96 display range: these are all stated in units as seen by the viewer. On a canvas the unit shrinks before anyone sees it, so multiply every one of them by the downscale factor before use.
- **Multiples of four, and baseline grids.** The reason for multiples of four is whole-pixel rendering at integer device ratios, which avoids half-pixel rounding. A non-integer downscale voids that reason entirely. A baseline grid exists so type aligns across columns and flowed text, and a single-frame graphic has neither.
- **Heading-level semantics and interaction states.** Importing a six-level heading structure is how a graphic ends up with six heading styles it cannot use, and a static image has no hover or focus state to style.

**The sharpest consequence: a feed graphic cannot use the bottom of any scale.** A scale generated downward from a base body size produces several steps that are already discarded as too small when read at full size on a screen. Divide all of them by the downscale factor and three or four more go with them. This is why the style count falls from sixteen to four or five: the floor arrives early.

## How to work

### Mode A: setting type on a piece

1. **Inventory the text by role.** Write down every string the piece carries and what job it does: one display line, a subhead, a body block, two labels. The role count sets the style count.
2. **Confirm the typeface before the scale.** Anything that will be read small needs a large x-height and open apertures, so that a c does not become an o once downscaled, and it needs low stroke contrast, so the thin strokes survive. Two typefaces maximum, paired across categories on matching x-heights. If the family does not offer five weights, you cannot skip one. Choosing the face is a different skill's job; confirming it meets these constraints is this one's.
3. **Derive the floor.** Smallest readable rendered size, multiplied by the downscale factor.
4. **Derive the ceiling.** Size the display line so the longest real string holds the number of characters you want on the line.
5. **Fit the ratio** across the number of steps between floor and ceiling, round the generated decimals to whole or even numbers, and run step visibility on every adjacent pair.
6. **Set leading per step from the character count** on that step's longest real line, then run the descender and return-sweep tests.
7. **Set tracking per step** on the sign rule, judged at real size: negative at display, zero at body, positive at label, extra positive on caps. Then kern the display line by hand, pair by pair.
8. **Build and name the style set.** Base name plus up to two modifiers, with the role as the base: `display`, `heading-lg`, `body`, `body-bold`, `label-caps`. Save as styles.
9. **Set paragraph spacing** to at least 1.5 times the body line box, and set alignment left.
10. **Run the tests in order**, ending with the arm's-length read.

### Mode B: judging type that already exists

Run the tests in this order and stop at the first failure, because fixing leading changes nothing downstream but fixing the measure or the size invalidates every leading and tracking value tuned after it.

1. **Style audit.** List every distinct size, weight, leading and tracking value in the file, against the declared scale and the six-style ceiling.
2. **Floor check**, then **character count** on the longest real body line, then **leading against that count**, then **descender**. This is the spine of the review and all four are arithmetic.
3. **Step visibility, weight gap and tracking triangulation**, all judged at rendered size rather than in the working file.
4. **Detail sweep.** One-word last lines, staircase rags, rivers, non-uniformly scaled type, letter collisions at display size.
5. **Content stress.** Add six words to the headline and re-render.
6. **Report** what passed, what failed, and the smallest fix for each, ordered by impact, keeping arithmetic failures separate from judgement calls.

## Tests

Run in this order. Every verdict is decidable by a reader who has only this file, a render and a phone.

| Test | Catches | Verdict |
|---|---|---|
| **1. Floor check** | Levels that only exist at full zoom | Export at full size, view at the width the piece will be seen at (a 1080px asset at 360px, then again at 270px for the stress case). Read the smallest string you need read. Fail if any required string cannot be read at 360px. Record separately whether it survives 270px. |
| **2. Character count** | An over-long measure, and display type set across a full column | Set the longest real string and count characters including spaces on its longest line. Fail if a display line exceeds 25, if a body block over four lines falls outside 50 to 75, or if a body block of four lines or fewer falls outside 25 to 50. Change the column or the size, never the leading. |
| **3. Leading against count** | Leading copied from the wrong row of a scale, in either direction | Take the count from test 2 and read the band for it: under 25 characters, 1.05 to 1.20; 25 to 50, 1.30 to 1.45; 50 to 75, 1.40 to 1.55. Fail if the set ratio falls outside the band for its own count, even when it matches a published average for its size. |
| **4. Descender** | Leading below the font's real vertical span | Zoom to a line pair where a descender (g, j, p, q, y) sits above a capital or an ascender. Fail if any two strokes touch. Fail separately if any descender crosses the lower edge of its own text frame. |
| **5. Return sweep** | A measure and leading combination that reads badly despite correct arithmetic | Read the body block once, top to bottom, at shipping size and shipping measure. Fail if you lost your place or re-read a line. |
| **6. Step visibility** | A ratio too small for the canvas, which is the standard failure when a product scale is reused | Place two adjacent sizes side by side and view at rendered width. Fail if you have to compare the edges of the two strings to see a difference. Fix by raising the ratio or deleting a level, never by raising the top. |
| **7. Weight gap** | Adjacent weights reading as an error rather than as a level | List every weight in use by its numeric value (300, 400, 500, 600, 700). Fail if any two in use are adjacent on that list. Fail separately if the lightest weight in use breaks up at rendered width. |
| **8. Tracking triangulation** | Tracking inherited rather than chosen, and untracked caps | Render the string three times: as set, one step tighter, one step looser. Keep whichever reads fastest. Fail if the middle option won without the other two being rendered. For caps, also render the same words in sentence case: fail if the caps string is not visibly looser than its twin, and fail any caps string longer than three words regardless of tracking. |
| **9. Style audit** | A scale used as a size menu | List every distinct size, weight, leading and tracking value in the file. Fail if any value is not a step of the declared scale. Fail separately if the count of named styles exceeds six, or if any value is a local override rather than a style. |
| **10. Detail sweep** | The faults that survive a correct scale | Fail on a paragraph ending in a one-word line, on a rag that steps evenly in one direction across three or more lines, on a visible vertical channel of white inside a justified block, on any text scaled non-uniformly to fit, and on any two letters colliding at display size. |
| **11. Content stress** | A scale fitted to one sample string | Add six words to the headline and two lines to the body, then re-render. Fail if the fix required a smaller size, a different leading ratio, or moving the column. |
| **12. Arm's-length read** | Everything the arithmetic cannot see | See "The ultimate test". |

## Anti-patterns

- **The invisible step.** Two levels a 1.125 ratio apart on a canvas that will be downscaled. *Fix:* raise the ratio, or merge the two levels, which is usually the right answer because the piece did not need the level.
- **Leading from the wrong row.** A 1.10 ratio across sixty characters, so the lines fuse into a block; or a 1.50 ratio across eighteen, so the headline falls into separate strips. *Fix:* count the characters and reset the ratio, in whichever direction the count says.
- **Leading set in absolute pixels before the size is final.** Change the size later and the ratio breaks silently, with no error and no visible moment of breaking. *Fix:* set a ratio and let the tool compute the absolute.
- **The scale used as a size menu.** A ten-step ramp generated, then a step picked per element by eye, often on a body size inherited from screen defaults. *Fix:* four to six named styles derived for this canvas, and delete the rest of the ramp.
- **Tracking on the wrong level.** Caps left at default spacing, or running text opened up to fill a space it did not fill. *Fix:* positive tracking of roughly 4 to 8 percent on caps at small sizes (**derived** by converting one practitioner's pixel adjustments at a 12px size into percentages, and wider than the 0 to 3 percent measured at label level across shipped systems, so treat the band as a starting range and triangulate), and zero on running text. Never fix a rag or a one-word last line with tracking.
- **Centred or justified paragraph.** *Fix:* left align anything over three lines, keeping a centred display lockup if the piece wants one.
- **One-word last line.** *Fix:* cut or add a word, or change the measure by one step.
- **Stretched or condensed by scaling.** Scaling a letterform non-uniformly distorts the drawing and breaks the match between its horizontal and vertical stroke weights. *Fix:* use a condensed or extended cut of the family, or change the size.
- **Icon stroke that does not match the text beside it.** A hairline icon next to a semibold label reads as two different materials in the same lockup. *Fix:* match the icon stroke weight to the stroke weight of the adjacent text.
- **A caption level below the rendered floor.** *Fix:* delete the level and fold its content into the label, or cut the content.

Each of these has a condition under which it is the right choice instead: tight display leading on a two-word lockup, untracked caps in a typeface whose caps were spaced to stand alone, a single weight when the piece is austere on purpose, a centred three-line lockup on a poster-shaped frame.

## Applied to a post visual or carousel

Canvas sizes and the downscale factor come from `reference/canvas-assumptions.md` at the plugin root, so the numbers stay consistent across the skills that share it. **Confirm the downscale factor against a real export before a launch that matters**, because every number here moves with it.

### The derivation

**The downscale factor.** A 1080px-wide graphic lands in a phone feed column of roughly 360px. 1080 / 360 = **3x**. A stress case of 4x covers a narrower column, a smaller phone and a cropped asset shown smaller.

**The floor.** The smallest reliably readable rendered text is about 12 effective pixels **(thin)**; shipped label sizes as low as 10 exist in measured systems, so treat 12 as a cautious working floor rather than a threshold. 12 x 3 = 36, so **nothing in the working file below 36px at the nominal case**, and 12 x 4 = 48, so **nothing below 48px for a piece held to the stress case**. Both figures are the same 12pt rendered and differ only in the viewing condition they survive, so quote the case alongside the number. Comfortable paragraph text is 16 to 18 effective pixels, so 16 x 3 = **48px as the body step**, which lands on the same value as the stress-case floor by coincidence rather than by derivation.

**The text column.** The canvas is 1080 wide with 72px margins on each side, which leaves 1080 - (2 x 72) = 936px of usable width. The 72px margin and the 936px usable width are the grid skill's numbers, taken as an input here. Text is then capped narrower than that, at **860px**, and that cap is set here rather than there, because the usable width is a grid decision and the text measure is a reading decision. A piece built on a different margin takes its usable width from that grid and recomputes this cap, since 860 is a reading cap inside 936 and not a constant.

**The ceiling.** A display line should hold 15 to 25 characters (**derived**: the 50 to 75 band is scoped to continuous body text, and no measured display band exists, so this one is constructed from the requirement that a display line read as one shape). At 0.5 em average character width on an 860 column: 20 characters needs 860 / 20 = 43px per character, so 43 / 0.5 = 86px of type size. 15 characters needs 860 / 15 = 57.3px per character, so 57.3 / 0.5 = 115px. The range is 86 to 115. Take **96px**, which lands at 860 / (0.5 x 96) = 17.9 characters, so 18. Cross-check from a different direction: a mobile headline ceiling of 40px on a 428px-wide phone frame **(thin)** scales to 40 x 1080 / 428 = 101px on a 1080 canvas, and the same figure on a 390px frame gives 111px. So the cross-check gives 101 to 111 against the first route's 86 to 115. 96 sits inside both and below the cross-check, which is the conservative side. It is a chosen value inside a derived range, not a corroborated measurement.

**The ratio.** 96 / 48 = 2.0, across three steps. The cube root of 2 is 1.2599, so the ratio needed is **1.26**, which sits just above the major third of 1.25. Check it forward: 48 x 1.26 = 60.5, round to 60; 60.5 x 1.26 = 76.2, round to 76; 76.2 x 1.26 = 96.0. One step down from 48 at 1.25 is 48 / 1.25 = 38.4, round to 38, which clears the 36 floor by 2px, so a label level is legal and nothing exists below it.

**Why not a smaller ratio.** Three quarters of shipped product systems use a major second of 1.125, which suits a long ramp covering dense application screens. Here it fails: 48 x 1.125 = 54, and 54 / 3 = 18 against 48 / 3 = 16, a difference of two effective pixels. A five-step scale on a canvas divided by 3 cannot afford a step nobody can see. The majority figure is an artifact of ramp length rather than of perception.

### The scale at 1080 x 1080 and 1080 x 1350

| Style | Size | Leading ratio | Line box | Tracking | Chars at 860 | At 3x | At 4x |
|---|---|---|---|---|---|---|---|
| `display` | 96 | 1.10 | 106 | -1.5% | 18 | 32.0 | 24.0 |
| `heading` | 76 | 1.15 | 87 | -1.0% | 23 | 25.3 | 19.0 |
| `subhead` | 60 | 1.20 | 72 | -0.5% | 29 | 20.0 | 15.0 |
| `body` | 48 | 1.40 | 67 | 0% | 36 | 16.0 | 12.0 |
| `label` | 38 | 1.45 | 55 | 0 to +2%, caps +4 to +8% | 45 | 12.7 | 9.5 |

Line boxes: 96 x 1.10 = 105.6, 76 x 1.15 = 87.4, 60 x 1.20 = 72.0, 48 x 1.40 = 67.2, 38 x 1.45 = 55.1, each rounded to a whole number. Character counts: 860 / (0.5 x size) = 1720 / size, giving 17.9, 22.6, 28.7, 35.8, 45.3.

**The leading column is set from the character count, not from the size.** The display row takes 1.10 at 18 characters, tighter than the 1.21 measured for display type in product systems, whose display rows sit in a wide browser column. The label row takes 1.45 at 45 characters, looser than the 1.42 measured at label level.

**The 4x column is the honest problem in this scale.** At the stress factor the label renders at 9.5 effective pixels, below the floor, and the body renders at 12.0, exactly on it, so the scale passes at 3x and fails at 4x below the subhead. Raising the whole scale does not fix it, because the ceiling is fixed by the 18-character display line and raising the bottom collapses the ratio. Scope the levels instead: **nothing that must be read goes below the subhead at 60px**, which renders at 15 effective pixels under the stress factor. The label level carries strings a reader can afford to lose, a handle, a date, a source line, and is never where a call to action goes. It clears the nominal floor by 12.67 - 12 = 0.67 effective pixels, which is the real answer to whether this canvas has a caption level: it does not.

**Where this scale meets a single-frame poster.** `dsn-poster` does not use the display 96, body 48 and label 38 rows above. It derives three sizes of its own from the canvas floor on a 900px live width, 120 for display and then either 72 and 48 or 54 and 36 depending on whether the smallest level has to be read, and for a single frame those supersede this ladder. The split is by scope: this file builds a scale for type set across many surfaces, that file sizes three lines on one frame. Where a project needs both and the two disagree, **this ladder wins and the floor check is re-run against it**, because a scale whose steps a reader cannot distinguish is the failure the ladder exists to prevent.

**Paragraph spacing.** At least 1.5 times the body line box: 1.5 x 67 = 100.5, so round up to **104px**, which is also an even number and a clean step.

**Tracking in absolute terms**, for checking what a percentage means at each size: display at -1.5% of 96 is -1.44px; label caps at +4% of 38 is +1.5px and at +8% is +3.0px.

### Square 1080 x 1080

- Four styles per frame, five at most. A display line, a subhead, a body block and a handle already fill a square.
- Usable height after a 72px top margin and a 182px bottom allowance for caption and username chrome is 1080 - 72 - 182 = 826px. At a body line box of 67, that is 826 / 67 = 12 body lines if the frame held nothing else, so in practice four to six.
- Two display lines at 18 characters each is 36 characters of headline. That is the real constraint on a square graphic and it is a copy constraint rather than a type one: the fix is a shorter headline, not a smaller size.

### Portrait 1080 x 1350

- The same five steps hold. Usable height is 1350 - 72 - 182 = 1096px, against 826 on the square, so the extra 270px buys 270 / 67 = 4 more body lines or 270 / 106 = 2.5 more display lines. It buys lines at the same size. It does not buy a sixth size and it does not buy a larger display step, because the display step is capped by the character count on the 860 column, which has not changed.
- If the asset can be centre-cropped to square on any surface it appears on, only the centre 1080 x 1080 survives, so anything that must be read sits between y = 135 and y = 1215. Compute that boundary before placing type, not after.

### Carousel

- **Freeze the style set and the first baseline position across every slide.** Type that drifts between slides jitters on swipe, and a one-step size drift reads as a mistake rather than as emphasis.
- **One display step per slide, not one per carousel.** Each slide is seen alone, so each needs its own first thing to read.
- **The cover slide carries the only string that must survive a thumbnail**, so size that string against the thumbnail rather than against the feed. The thumbnail width is not in the shared canvas assumptions, so measure it on a real post before trusting any number for it: at a thumbnail a third of feed width, the effective downscale is 9x and a 96px display line renders at 10.7 effective pixels, which is below the floor. Which string must survive is decided by the skill that owns rank order.
- **On the last slide, a call to action at label size fails**, because the label level is the one scoped for losable strings. Put it at body or subhead, clear of the bottom chrome allowance.

## Checklist

- [ ] Floor and ceiling derived and stated, ratio fitted afterwards
- [ ] Four to six named styles, every value a step of the scale, nothing below the rendered floor
- [ ] Leading set from the character count on each level's longest real line
- [ ] Step visibility, descender and return sweep all pass
- [ ] Tracking signed per level, caps tracked, running text at zero
- [ ] No two weights in use adjacent; lightest weight holds at rendered size
- [ ] Two typefaces maximum, matched x-heights, display line kerned by hand
- [ ] Paragraph spacing at least 1.5 times the line box; left aligned over three lines
- [ ] No one-word last lines, staircase rags, rivers or non-uniformly scaled type
- [ ] Re-run against the longest real string and the stress downscale factor

## The ultimate test

**The arm's-length read.** Export at full size, scale the image to the width it will actually be seen at, and read the piece once from the top on a phone held at arm's length. Three things must happen, in this order: the display line reads first and reads whole; the body block reads straight through with no line lost or re-read; every string you needed read is readable.

Each failure names its own diagnosis. A lost line means the leading is wrong for the measure, so count the characters and reset the ratio. A display line that does not read first means either the ratio is invisible at rendered size or the weight gap is too small, and the step visibility and weight gap tests separate those two. A string that cannot be read sits below the floor, and the fix is to delete the level rather than nudge the size.

## Where this skill should lose

**When the question is which typeface, or which two.** Use `dsn-typeface`. That skill owns choosing and pairing: it takes a brief and returns a family name, a pairing and a weight list. This skill begins where that one ends, with the family already chosen, and owns setting it. The handoff is concrete in both directions. Going in, this skill needs three things from that one before it can start: the family name, a list of at least five available weights, and confirmation that the face has a large x-height, open apertures and low stroke contrast if anything will be read small. Coming back, if a legibility failure survives every setting change available here, that is, the size is at the ceiling for its character count, the leading matches its count, the tracking has been triangulated, and the string is still hard to read, then the cause is the drawing of the letters rather than the setting of them, and the fix is a different face. Close this file and open that one.

**When you do not yet know which element should read first.** Use `dsn-hierarchy`. That skill produces the rank order; this one turns a rank order into sizes, weights and spacing. Running this first means building a scale and then discovering the wrong string is at the top of it.

**When the problem is the gap between blocks rather than between lines.** Use `dsn-spacing`. Leading is the space inside a text block and belongs here. The space between a heading and the paragraph under it, between the paragraph and the image, and around the whole lockup belongs there, along with the spacing scale those gaps come from.

**When the measure is wrong because the column is wrong.** Use `dsn-grid`. That skill owns the margin, the column count, the gutter and therefore the column width this skill treats as a fixed input. If test 2 fails and no legal size fixes it, the column is the thing to change, and it changes there.

**When the text might be unreadable for reasons other than size.** Use `dsn-contrast`. Everything in this file is about whether the letters are large enough and spaced well enough. None of it tells you whether the text colour has enough separation from what sits behind it, and a correctly set 48px body over a photograph can be entirely unreadable.

**When the names and the structure matter more than this one canvas.** Use `dsn-tokens`. This skill names five styles for one canvas. Naming conventions that survive across a whole system, the rename tests, and the layering of raw values under semantic ones live there.

**When the icons are the problem.** Use `dsn-icon`. The rule here says match the icon stroke to the stroke weight of the adjacent text, which is all this skill can tell you. Building a set with a consistent keyline and stroke spec is that skill's work, and that skill derives its sizes from a type size it takes from here, so settle the scale first.

**When a single standalone frame quotes two or three sizes that conflict with the scale here.** Use `dsn-poster` for the cut, the element count and how many levels one frame can hold, and keep the scale here. The precedence runs one way and both files state it the same way: where a standalone frame's quoted sizes and this skill's ladder disagree, the ladder wins. What then gets re-run against the ladder is that file's floor check, meaning the test that the smallest surviving size still reads at the distance and column width the piece ships in. If a ladder step fails that floor, the step is too small for that format and the frame needs fewer levels, not a smaller step.

**When the type is not running text, or not on one canvas.** Three cases leave this file. A wordmark, monogram or lockup is drawn and optically corrected for one fixed use rather than set to carry arbitrary copy, and belongs to `dsn-mark`; this skill stops at the edge of a lockup. How many words each frame of a multi-frame piece may carry, meaning the copy budget divided across a set rather than fitted to one canvas, belongs to `dsn-sequence`; this skill supplies the character count a given size and column produce, and that file decides how many frames the copy needs. A headline over a photograph is set here, but whether the picture offers a region quiet enough and large enough to hold it, and which picture to use instead if it does not, belongs to `dsn-image`.

## What an agent can run, and what it cannot

**Can run:** the whole derivation, given a canvas size, a downscale factor and a column width, including the ratio fit and the rounding; the style audit and the style count; the floor check and step visibility, both as rendered-pixel arithmetic; characters per line, from glyph widths or from a measured render, and leading against that count; the descender test, by comparing the font's ascender and descender metrics against the line box; the weight gap and tracking sign checks; paragraph spacing against the line box; and detection of one-word last lines, staircase rags and justified blocks.

**Cannot run:** the return sweep or the arm's-length read, both of which need eyes reading continuously; kerning judgements, which are optical by definition; the choice of typeface, which is a brief decision; how many characters a display line should hold, which is a decision about tone between a terse eighteen and a discursive thirty; and anything about what a setting signifies rather than whether it can be read.

Three things neither an agent nor this file covers, which is where the remaining quality in a set text block sits: optical margin alignment, pulling a line's first glyph slightly past the column edge so a quote mark or a round letter does not make the edge look ragged; hanging punctuation, the same move applied to the right edge; and optical centring, judging a lockup's centre by weight rather than by width. All three are hand work, judged by eye at real size.

## Writing the output

Plain words, full sentences. Name the style and give the measurement: "the 38px label renders at 12.7 effective pixels and at the stress factor it renders at 9.5, so the handle will not be read" beats "small text has legibility issues". Give the mechanism first and the number second, as an option, because the number depends on the canvas and the font while the mechanism does not. Say which tests you ran and what each one returned, including the passes, since a pass and a test you skipped look identical in a summary that only lists failures. Label every figure as derived, measured or inherited at the point you use it, so that an inherited figure can be overridden later without anyone thinking they broke a rule.

Sources, corroboration, the disagreements between them and every figure that was discarded are in `references/provenance.md`.
