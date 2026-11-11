---
name: dsn-spacing
description: Setting gaps, padding and margins, building or repairing a spacing scale, judging whether a layout has air, or speccing safe zones. Gives a spec and a grouping audit.
---

# Spacing and whitespace

This skill sets the gaps, padding, margins and empty regions on a piece, and judges whether a piece that already exists has enough air and whether its grouping is honest. The single idea underneath it is that two different decisions wear the one word "spacing", and what separates them is scale, not the kind of work you do. At small scale, spacing is a consistency problem: a short list of permitted values, applied the same way every time, because gaps of 14, 17, 22 and 31 each dragged by hand read as sloppy to a viewer who could never say why. At large scale it is a composition problem: deciding that one region of the piece will carry nothing, and holding that decision when the urge to fill it arrives. Constrain which values exist. Refuse to constrain how they are arranged.

## What this skill is for

Use it when someone wants to:

- set gaps, padding and margins on a piece being built
- build or repair a reusable spacing scale that someone else will have to apply
- judge whether a layout has enough air, and whether the air is doing anything
- check whether the gaps state true relationships between elements
- spec edge margins, safe zones and crop-safe boxes for a post graphic or carousel

The output is a short table of permitted values, a measured spec per canvas, and a pass or fail against each test in the table below.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file rests on a controlled comparison. In particular, nothing anywhere supports the claim that more empty space performs better: that case is argued from admired work and from critiques of weak work, with no measurement and no comparison. Read the register claims, that generous space reads premium and tight space reads urgent, as conventions that held in the places they came from. Rules and numbers marked **(thin)** rest on a single account, or are figures chosen for this skill rather than derived from anything, and should be treated as one house's style rather than consensus. On a feed where engagement is measurable, measure rather than inherit.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

These are the only terms this skill needs. The rest of the file assumes them.

**Gap.** The empty distance between two separate elements. Measured edge to edge, not centre to centre.

**Padding.** Empty distance inside a single object, between its own edge and its contents. The space between a button's border and its label is padding; the space between the button and the next button is a gap.

**Margin.** Empty distance between content and the edge of the canvas.

**Gutter.** The gap between two columns of a grid. Set by a grid, not by this skill, but it has to agree with the values here.

**Micro space.** Space whose job is to make information comfortable to take in: letter spacing, line height, padding inside an object, the gap between lines of one text block. On a 1080px canvas this is roughly the bottom two values of the ladder below.

**Macro space.** Space whose job is to carry the composition: canvas margins, gutters, the gap between one section and the next, and regions that carry nothing at all. Macro space moves the eye and sets the register. On a 1080px canvas this is roughly the top three values of the ladder below, plus whatever region you leave empty.

**Leading.** The vertical distance from one baseline of text to the next, usually stated as a multiple of the type size. A gap between lines of a paragraph is leading and is not a gap in the sense above. Set it with the skill that sets type, not here.

**Tracking.** Uniform space added to or removed from between every letter in a run of text.

**Measure.** The width of a line of text, in pixels or in characters per line. A measure that is too wide makes the eye lose its place returning to the next line.

**Geometric centre.** The arithmetic middle of a shape: half its width, half its height.

**Optical centre.** Where a shape looks centred. The two differ when the contents are visually lopsided. A text label with descenders, the parts of letters like g, p and y that drop below the baseline, sits optically low when its box is centred mathematically, because the descenders add measured height that does not read as ink.

**Lockup.** A fixed arrangement of two or more elements treated as one unit from then on: a logo with its wordmark, a two-line title with a rule under it.

**Token.** A named spacing value, such as `md` for 64px, used instead of typing the number. **Alias.** A second name for a token that states its purpose rather than its size, such as `button/horizontal-padding`, so that changing the purpose's value in one place changes every use of it.

**Step and ratio.** A step is one value on the ladder of permitted values. The ratio is the multiple between two adjacent steps: 32 to 64 is a ratio of 2.

**Whitespace.** Breathing room. It is tuned by measurement, and it does not have to be literally white or literally empty: a quiet texture or a soft background image can function as whitespace if separation and clarity survive it.

**Negative space.** A different thing. A second readable figure found inside the gap between other shapes, such as an arrow formed between two letters. It is found by trial and is a concept problem, not a measurement problem. Keep the two words apart in any brief. If you mean breathing room, say whitespace.

**Isolation, or clearance.** Noticeably more empty space around one element than the ladder gives anything else. This is how importance is made without changing size or colour.

**Downscale factor.** How much smaller the piece is seen than the file it was built in. For post graphics this skill uses the two figures in `reference/canvas-assumptions.md` at the plugin root: 3x nominal, meaning a 1080px-wide asset lands in a feed column of roughly 360px, and 4x as the stress test, meaning 270px.

**Dead band.** A strip along each canvas edge that carries nothing at all, because assets get clipped and re-rendered at the edges.

**Reading margin.** A wider strip inside the dead band that carries nothing that has to be read. Decoration may enter it. A word may not.

**Chrome zone.** The region of the frame a platform overlays with its own interface: slide counters, position dots, caption previews, swipe affordances, avatars and headers. Anything you need read must stay out of it.

## The one idea

**The list of permitted values governs the vocabulary. The composition governs the pattern.**

The split that decides which decision you are making is scale, micro against macro, and it is a split in the space itself rather than a split between kinds of design work. The same two jobs exist on a 1080px post graphic and on an interface screen, and in both the small gaps are a comfort floor while the large ones are the composition.

**Micro space is governed by a list.** Its enemy is inconsistency. One caught inconsistency is expensive out of proportion to its size, because it is the only kind of error a non-designer can verify, and having verified one they discount the parts they cannot check. The fix is a short list of permitted values, chosen once.

**Macro space is governed by nerve.** Its enemy is timidity. A layout where every gap is on the list and nothing is empty passes every mechanical check and says nothing. The fix is deciding that a large region carries nothing, and not filling it later.

A list of permitted values cannot produce emphasis, because emphasis is a difference and a list applied uniformly removes differences. Merge the two halves and you get the characteristic failure of system-driven work: evenly spaced, competent, lifeless, forgettable.

## The principles

**1. A gap is a statement about relationship.** Elements closer together read as belonging together, and that reading lands before anything is read as language. So a wrong gap states a wrong relationship: a caption sitting equidistant between two images claims to belong to neither, and that claim arrives before the copy does. Spacing errors are meaning errors, not tidiness errors.
*Checked by the ratio check and the squint test.*

**2. Decide whether you are setting micro or macro space before you drag anything.** Micro makes information comfortable to take in. Macro carries the composition and moves the eye. They are tuned by different criteria, so a session that mixes them produces either a layout that is pleasant to read and says nothing, or one that is striking and illegible. Name the job out loud, then set the value.
*Checked by the job-naming step in Mode A.*

**3. Micro space is a floor, not a lever.** Raise it until the text is comfortable at the size it will actually be read, then stop. Adding micro space past comfort buys nothing and eats the macro space the composition needs. Small gaps do direct attention, by principle 1, so the useful question about any gap is not its size but its purpose: is it here to make reading comfortable, or to make the eye go somewhere. Ask that of every gap, and the answer is independent of magnitude.
*Checked by the comfort read.*

**4. Isolation is emphasis, so isolate exactly one thing. (thin)** Importance is made by clearance around the important element: more empty space around it than the ladder gives anything else. Isolate two elements and you have isolated nothing, because the reading is comparative and there is no longer a comparison. The count of one is this skill's, not inherited.
*Checked by the isolation count.*

**5. A scale earns its keep by the ratio between steps, not the base number.** A ladder of 12, 14, 16, 18 cannot express a boundary, because 18 beside 14 does not read as a separation. The load-bearing part is the ratio, and the floor is roughly 1.5x, derived from the downscale: at 3x, a 1.125 ratio puts 48 next to 54, which is 16 against 18 once rendered, two pixels apart, so it is one value wearing two names. At 1.5x, 16 next to 24 renders as 5.3 against 8, which is a difference of half the smaller value and survives. Use 1.5x to 2x between steps, and cap the values used on any one frame at five. **(thin)** The cap of five is a figure chosen for this skill; no account states a count.
*Checked by the step-visibility test and the gap audit.*

**6. A scale tells you a gap is legal, not that it is right.** Scale is a relationship rather than a dimension, which is why the amount cannot be briefed numerically and has to be judged by eye against the whole piece. Once the measurable checks pass, one question remains: does the empty region enable something nameable, one clear focal point, a readable thumbnail, a legible structure, or is it merely absent. A large empty region in a piece with nothing to say is a thin piece at larger scale, and the right answer here often looks unimpressive.
*Checked by the recall test and the ultimate test.*

**Why a five-value grammar and not just a good eye.** Hand-dragged spacing is not mainly ugly, it is detectable, which is the argument for a list on a single piece. The argument for writing the list down, naming its values and keeping it is about volume and other people: a standard has to survive its weakest executor. One person making one piece can hold spacing in their eye. Twenty pieces over three months, or any piece made by a freelancer, an assistant or an agent, cannot, because the only thing that transfers between people is the list of permitted values and the names on them. Five values are learnable in one sitting and checkable in one glance, which is the reason the cap is five rather than twelve. A ladder that only its author can apply has not paid its setup cost, it has moved that cost into every future piece.

## How to work

### Mode A: setting spacing on a piece

1. **Inventory the content first, then name the job.** Count the text blocks, the groups and the images. Rooms of text leave nothing empty to compose with, so the job is micro spacing and the deliverable is comfort. Three lines and a photograph make it a composition, and the deliverable is one empty region. Write down which of the two you are doing before touching anything, per principle 2.

2. **Cut before you space, if you own the copy.** Ask of each element whether the piece still makes sense without it, and delete what survives that question. One deleted element buys more space than any gap adjustment can, because it removes both the element and the two boundaries around it. If the copy is client-supplied or legally fixed, skip this step and adapt to what you were given instead. The error to avoid is attempting a minimal composition on content that cannot be reduced, which produces either an illegible piece or a mockup that cannot be built.

3. **Pick the ladder.** Five permitted values on any one frame, ratios of 1.5x to 2x, base chosen for the canvas and derived in the Applied section below. Scope each value to the properties it is legal for, so that a value available as a corner radius cannot be picked as a gap; a value that can be misused eventually will be, and at that point the ladder has stopped being a ladder. Alias each value to its intent, `button/horizontal-padding` rather than `space-xs`, so that one edit propagates to every use instead of to every value that happens to share a number.

4. **Set micro space to the comfort floor.** Leading inside paragraphs, the gap between paragraphs, padding inside components. Read the result at the size it will be seen, not at the size you are working at. Stop at comfortable, per principle 3.

5. **Group, then separate.** Tighten what belongs together first, then open the boundaries between groups on the ratio in principle 1. Tightening is the cheaper half, and it is also how you manufacture macro space without deleting information, which is the honest middle option between cutting copy and shrinking gaps below their comfort floor. The mechanism is boundary arithmetic. Three standalone lines take three boundaries, and the boundaries cost more than the lines do: at a within-group value of 32 and a between-group value of 64, three separated lines spend 64 + 64 = 128px on separation, while the same three lines consolidated into one block spend 32 + 32 = 64px inside it and one 64px boundary at its edge, releasing 64px as a single empty region you can compose with. The saving grows with the count: five statistics set as five groups spend four boundaries, and set as one row spend one. A heading, a date and a byline become one stack. Every word survives, and what drops is the number of things the eye has to place, which is what was eating the space. Do this before tightening any gap below its comfort floor: a gap taken from the floor is paid for in legibility, a gap taken from consolidation is paid for by nothing. The limit is honesty. Consolidate only elements that genuinely belong together, or you have bought space by stating a false relationship, which is principle 1 run backwards.

6. **Spend macro space on exactly one element,** the one the piece exists for. Everything else gets ladder values. If two elements both seem to deserve it, the piece has not decided what it is about, and that decision belongs to the brief rather than to the spacing.

7. **If the piece needs force, go asymmetric and then anchor it. (thin)** Weight gathered on one side makes the eye hunt, which is the effect you want, but it needs a counterpoint on the light side: a small block of text, a rule, a shadow. Without one, tension reads as an unfinished file rather than a decision, and at thumbnail size the two are indistinguishable. Keep the anchor small enough that it does not rebalance the layout, which means it should be the smallest thing on the piece rather than a second focal point.

8. **Vary the intervals, within the ladder.** 32, 32, 32, 32 and 16, 16, 128, 32 are both legal; only the second has structure. Every change of interval has to sit on a real structural boundary, or it reads as the inconsistency it looks like.

9. **Fix padding inside objects last, and optically.** Align each label to its shape's geometric centre, then correct by eye, because descenders and uneven icon shapes sit optically low when centred mathematically. Keep the gaps across a row of icons equal to each other even when the icons are not the same width, since the eye reads the gaps rather than the boxes.

10. **Run the checklist and then the tests in table order,** ending with the degraded-state check.

### Mode B: judging something that exists

Run in this order and stop at the first failure. Consistency is checked before judgement, and the order is not a preference: an inconsistency found after the polish invalidates the polish, because fixing a gap that states a wrong relationship moves the elements the polish was tuned against, so the taste judgement then has to be made again on a layout that no longer exists. Consistency is also the half that measurement can settle, so settling it first leaves only the part where argument is the method.

1. **Gap audit.** List every distinct gap and padding value on the piece, against the ladder and the five-value cap.
2. **Ratio check.** Name the intended relationship of every adjacent pair first, then measure. This is the highest-yield check in the list, and it is arithmetic rather than taste.
3. **Edge sweep.** Distance from every element to every canvas edge, against the dead band, the reading margin, the chrome zone and the crop-safe box.
4. **Isolation count.** Must be one.
5. **Visual checks, in order:** squint test, then recall test, then the thumbnail test at 270px, then the masked-anchor test if the layout is asymmetric.
6. **Report** what passed, what failed, and the smallest change that fixes each failure, ordered by how much it moves.

## Tests

Each returns a verdict decidable from this file alone. An observer with the export, a ruler and the content brief can run all of them except where noted.

| Test | Catches | Verdict |
|---|---|---|
| **1. Gap audit** | Values off the ladder, and improvised vocabulary | List every distinct gap and padding value. Pass only if each value is a ladder step and the count of distinct values is five or fewer. A sixth value means you are improvising. Zones (dead band, reading margin, chrome zone) are not gaps and are not counted here. |
| **2. Ratio check** | False relationships, including equidistant orphans | Name each adjacent pair as same group, adjacent groups or unrelated, then measure. Pass only if every between-group gap is at least one full ladder step above the largest within-group gap, which on the doubling part of the ladder is 2x, and every section break is one further step above that. Fail if any within-group gap anywhere exceeds any between-group gap, which means the layout is stating a relationship that is not true. |
| **3. Step-visibility** | A ladder too dense to express a boundary | Render two adjacent steps side by side, then view at 360px wide. Fail if you cannot see that they differ. |
| **4. Comfort read** | Micro space below its floor, or past it | Read one paragraph at the size it will be seen, 360px wide for a post graphic. Fail if you lose your place returning to the next line, or if any line of a group reads as belonging to the group below it. Then fail in the other direction if lines of one paragraph read as separate statements. |
| **5. Isolation count** | Absent emphasis, and competing emphasis | Count the elements with noticeably more clearance than the ladder gives anything else. Pass only on a count of exactly one. Zero means the ladder was applied as a pattern. Two or more means nothing is emphasised. |
| **6. Edge sweep** | Content that clips, or gets overlaid by platform interface | Measure every element to every edge. Fail on anything inside the dead band, anything that must be read inside the reading margin, anything that must be read inside the chrome zone, and on any load-bearing element outside the crop-safe box. |
| **7. Squint test** | Wrong grouping, and absent emphasis | Blur the export until no word is readable, then say what belongs to what and what matters most. Pass only if the group count matches what you intended and one element is clearly first. A wrong group count is a ratio-check failure: go back to test 2. The right groups with nothing standing out is a test 5 failure: take clearance from everything else and give it to one element. |
| **8. Recall test** | Clutter that the squint test passes | Look away from the piece and describe it: what it was about, and the one thing you remember. Pass only if you can name the one thing without hesitating. Hesitation is a fail even when every measurable test above passed, because a piece can blur into clean, correct, well-separated groups and still leave nothing behind. The mechanism it is tied to runs clutter to confusion, confusion to a piece nobody scans, unscanned to unmemorable, and unmemorable to never acted on, so this is the only test in the table that reaches the consequence the piece exists for. The fix is almost always fewer elements rather than more space. It costs nothing to run and it is the last check before shipping. **(thin)** |
| **9. Macro-space fraction** | A composition with no empty region at all | Export, fill every element's bounding box with black, and read the white fraction. Fail below 30 percent. **(thin)** |
| **10. Thumbnail** | Macro balance that only works at full size | View the export at 270px wide, which is the 4x stress case. Fail if the structure is unreadable or the first element is no longer first, however well it reads at 1080. A piece that survives only 360px is at the edge rather than safe. Checking at 162px as well is stricter than anything this plugin assumes. **(thin)** |
| **11. Masked-anchor** | Asymmetry that is unfinished rather than deliberate | On an asymmetric layout, hide the counterweight and look again. Fail if the layout looks the same with it hidden, since the anchor is then doing no work, and fail the other way if hiding it makes the layout look correct, since the asymmetry was the error. |
| **12. Carousel frame-drift** | Margins that jitter on swipe | Overlay every slide. Fail if the dead band, the reading margin or the first baseline of the headline moves by any amount between slides. |
| **13. Degraded-state** | Macro space that existed only for the demo content | Re-render with the longest real content you will ship, the worst image, the missing field, the translated string. Pass only if the composition survives all of them. A headline that wraps to three lines where the layout assumed two eats the empty region the composition was built on. **(thin)** |

## Deciding whether a borrowed spacing number transfers

**4 and 8 as base units.** A convention with a partial reason. Half-pixel rounding comes from non-integer scaling, so a multiple of 4 is a hedge against it. The reason does less work than people think: at an integer density any whole-pixel value survives, so 4 has no privilege there. The case where it does matter is non-integer downscaling, which is exactly the post-graphic case, where 1080 is divided by 3 or 4. That is also why the convention does not transfer: 4 and 8 are device-independent pixels chosen for an interface seen at full size, and a 4px gap on a 1080 canvas renders at 1.3px nominally and 1px in the stress case, which reads as nothing at all. Keep the ratios, raise the base. **(thin)**

**Powers of two specifically.** Convention. A 1.5x ladder works for the same perceptual reason, which is that the step has to survive division by 3.

**Any absolute value borrowed from a tutorial or a component library.** Take the ratio and discard the absolute. The absolute was chosen for a canvas of a size you did not see, at a viewing distance you cannot check, and a spacing value carries no meaning apart from the canvas width it was chosen on. If you cannot state the canvas width a number came from, you cannot use the number.

**A ladder does not make the choice.** In practice the gap that lands is found by trial: a value is set, judged too tight, enlarged, judged again, and settled by eye. The ladder constrains the vocabulary so that the trial runs between four legal values rather than between every integer. Expect to iterate, and expect the final figure to be one of the five.

## Anti-patterns

- **Even-and-dead.** Every gap on the ladder, every gap the same, nothing emphasised. *Fix:* multiply the clearance on the one element the piece exists for, taking that space from everything else rather than from the canvas (Mode A step 6 and step 8).
- **Spacing by eye with no ladder.** *Fix:* snap each value to the nearest step, then re-run the ratio check, because snapping frequently collapses a boundary you were relying on.
- **Cluttered.** No region empty, nowhere to look first. *Fix:* delete, then group, then space, in that order. Adding gaps around too many elements makes a piece cramped and scattered at the same time. This is what the recall test catches when the squint test passes.
- **Equidistant orphan.** A caption, logo, date or call to action the same distance from two groups. *Fix:* decide what it belongs to and halve the gap on that side. If it belongs to nothing, it needs a full between-group gap on both sides, which usually turns out to mean there is no room for it.
- **Timid whitespace.** A region left slightly less busy rather than empty. *Fix:* commit it or reclaim it. There is no middle setting, because a half-committed region reads as an element that failed to arrive.
- **Padding drift inside objects.** Labels off-centre inside buttons and chips, unequal gaps across an icon row. *Fix:* align to the geometric centre, then correct optically (Mode A step 9).
- **Claustrophobic lockup.** A logo or a two-line title packed tight against itself. *Fix:* one ladder step more and no more, since a lockup fails in both directions and the next step up detaches the parts from each other.
- **Text group that ate its macro space.** *Fix:* consolidate what belongs together (Mode A step 5), then cut copy until the empty region returns.
- **Asymmetry with no anchor.** Reads as an unfinished file rather than a decision. *Fix:* Mode A step 7, then test 11.
- **Emptiness mistaken for restraint.** *Fix:* principle 6. If the empty region enables nothing nameable, the piece is thin rather than minimal, and more space will make it worse.

Each of these has a condition where it is the right answer instead: even spacing when the subject is a texture or a repeating set, equal clearance on a three-column comparison where ranking the columns would be a lie, density when urgency is the message. Emptiness is a register, not a universal virtue.

## Applied to a post visual or carousel

The canvas sizes, the 3x nominal downscale and the 4x stress test come from `reference/canvas-assumptions.md` at the plugin root. Everything else below is derived here, step by step, so the arithmetic can be followed to the same answer or corrected. The zone values are reasoned from how platforms crop and overlay rather than read off a published specification, so confirm them against a live export before a launch that matters.

### Deriving the ladder at 1080px

The base step is the smallest gap that still reads as a deliberate separation in the worst case the piece will be seen in. At the 4x stress factor, a gap of 4px renders at 1px and a gap of 8px renders at 2px, which read as two shapes touching rather than as two shapes with space between them. 16px renders at 5.3px nominally and 4px in the stress case, which is the first value that still reads as a gap after division by 4. So the base step is **16**.

From 16, apply principle 5: ratios of 1.5x to 2x, taking 2x while the values are small enough that a 1.5x step would be invisible, then 1.5x once they are large.

| Token | px | Derivation | Use |
|---|---|---|---|
| `xs` | 16 | base, from the 4x stress case | Inside a chip or pill; a label to its own object |
| `sm` | 32 | 16 x 2 | Lines of one text group; an icon to its label |
| `md` | 64 | 32 x 2 | Related blocks: eyebrow to headline, headline to subhead |
| `lg` | 128 | 64 x 2 | Between groups. The gap that means "a different thing" |
| `xl` | 192 | 128 x 1.5 | Section break; clearance around the emphasised element |
| `field` | 288 and up | 192 x 1.5 | Deliberate macro emptiness |

The `field` step is 288 rather than 256 because 256 is only 1.33x on 192, which is below the 1.5x floor principle 5 sets, so a 256 field and a 192 section break fail this skill's own step-visibility test when placed near each other. Six tokens exist; five is the cap on any one frame, so a frame using `sm`, `md`, `lg` and `field` has one value in hand.

The boundary ratio in test 2 follows from the same ladder: a between-group gap has to be at least one full step above the largest within-group gap, because a difference below one step is by construction a difference a viewer cannot see. On the doubling part of the ladder that is 2x, so a 32px within-group gap demands at least 64px between groups, and a section break demands at least 128px.

### Square, 1080 x 1080

- **Dead band 64 all four sides.** Set to the `md` step so edge clearance lands on the ladder. Nothing at all inside it. **(thin)**
- **Reading margin 108, which is 10 percent of 1080.** Nothing that must be read inside it. 108 is not a ladder step, and that is allowed: a zone is not a gap, and test 1 does not count it. **(thin)** It is also not the grid margin, which `dsn-grid` owns and sets at 72 on this canvas. This is a content-exclusion zone measured from the canvas edge, so a piece can carry both, with the grid's columns starting at 72 and nothing that must be read placed before 108.
- **Measure capped at 864.** This is what the reading margin leaves: 1080 minus 2 x 108 = 864. Set headlines to this cap or they wrap unpredictably between one font rendering and another.
- **Macro budget: at least 30 percent of the canvas empty,** measured by test 9 rather than estimated. **(thin)**

### 4:5, 1080 x 1350

- Same 64 dead band and 108 reading margin, for the same reasons.
- **Crop-safe box.** If the asset can ever be shown square, only the centre 1080 x 1080 survives. 1350 minus 1080 = 270, and centred that is 135 at the top and 135 at the bottom available for atmosphere but not for anything load-bearing. A crop anchored to the top instead takes all 270 off the bottom, so design to the stricter case and keep load-bearing content inside the centre 1080.
- **The extra height buys macro space, not another element.** 270px is one more line of a 48px headline plus its leading and a boundary, which is why it reads as room for one more line; spend it on the empty region instead, or the 4:5 version of a square piece is just a tighter square piece.

### Mobile edges

- **Bottom 180px, chrome zone.** Platform overlays occupy roughly the bottom 60 points of a feed card, and 60 x 3 at the nominal downscale is 180px. Position indicators, slide counters, caption previews and swipe affordances sit here. Nothing you need read goes in it. **(thin)**
- **Top 80px.** Avatar and header overlays on some surfaces, roughly 27 points x 3. Keep text clear of it. **(thin)**
- **Handle and logo** sit inside the reading margin, in the same corner on every piece. Never in the dead band, where they clip, and never in the chrome zone.
- Where the viewing condition is unknown, default to the harder one: 4x, cropped square, with chrome.

### Worked example: a square promo graphic

**Before.** A 1080 x 1080 piece: a photograph across the top half, then an eyebrow, a three-line headline, a two-line subhead, a date line, a logo at bottom left and a call to action at bottom right. Measured: photograph to eyebrow 18, eyebrow to headline 22, headline line to line 14, headline to subhead 26, subhead to date 26, date to logo 26, logo baseline to bottom edge 48, headline set to a measure of 980. Bounding boxes blacked out leave 18 percent white.

**Diagnosis, computed.**

- Test 1, gap audit. Distinct values: 14, 18, 22, 26, 48, which is five, so the count passes. None of the five is a step on the ladder, so the test **fails** on legality. The piece has an improvised vocabulary that happens to be short.
- Test 2, ratio check. Intended relationships: headline lines are one group, the photograph is a separate group, eyebrow and headline are adjacent groups, subhead is a separate group, date and logo are one group. Largest within-group gap is 14, so the minimum between-group gap is one full step above it, 28. Photograph to eyebrow is 18, which is 1.29x, so the photograph reads as part of the text block. Headline to subhead is 26, which is 1.86x and still short of 28. Subhead to date is 26 against a required section break of 56. All three **fail**. The date sits 26 above the logo and 26 below the subhead, so it is an equidistant orphan and belongs to neither.
- Test 4, comfort read. The 14px line-to-line figure is leading rather than a gap, and at 980 measure the line length is 113 px per line at 360px wide, so the eye loses its place on return. **Fails.**
- Test 5, isolation count. The largest clearance anywhere is 48, against a `field` of 288. Nothing is isolated, so the count is zero. **Fails.**
- Test 6, edge sweep. The logo baseline sits 48 from the bottom, inside the 64 dead band and well inside the 180 chrome zone, so the logo clips on some surfaces and is overlaid on others. The call to action is in the same strip. **Fails.** Measure 980 exceeds the 864 cap, so the headline runs into the reading margin on both sides. **Fails.**
- Test 9, macro-space fraction. 18 percent against a floor of 30. **Fails.**
- Test 10, thumbnail. At 270px the gaps 14, 18, 22 and 26 render at 3.5, 4.5, 5.5 and 6.5px, a spread of 3px across every boundary on the piece, so all five groups collapse into one block. **Fails.**

**After, computed.**

- Consolidate the date into the logo stack at `sm` 32, which removes one boundary and the orphan at once: two boundaries of 26 become one group with a 32 internal gap. Boundary saving, per Mode A step 5: before, 26 + 26 = 52 spent on separation; after, 32 spent inside the group and one 128 boundary at its edge.
- Snap the rest: eyebrow to headline `sm` 32, same group. Headline to subhead `md` 64, adjacent groups, which is 64 / 32 = 2x, one full step. Pass. Subhead to the logo group `lg` 128, section break, which is 128 / 64 = 2x again. Pass.
- Set the headline measure to 864 and let it take three lines at that width. Leading comes from the type skill, not from here.
- Crop the photograph shorter to open `field` 288 above the headline, making the headline the single isolated element. Isolation count is now one.
- Move the logo group so its lowest pixel sits at 896, which clears the chrome zone: 1080 minus 180 = 900, and the reading margin only required 1080 minus 108 = 972, so the chrome zone is the binding constraint and 896 clears it by 4.
- Distinct gap values now used: 32, 64, 128, 288, which is four, one under the cap. The 64 dead band and the 108 reading margin are zones and are not counted.
- Blacking out the new bounding boxes leaves 34 percent white, above the 30 percent floor. At 270px the gaps render at 8, 16, 32 and 72px, so each boundary is at least double the one below it and the group structure survives the stress case.

### Carousel

- **Freeze the frame, vary the density inside it.** The dead band, the reading margin and the first baseline of the headline are identical on every slide, because a margin that drifts by even a few pixels jitters as the slide snaps into place, and this is the one spacing error the format makes unmissable. Inside that fixed frame, a dense slide after two airy ones is a tempo change, and tempo is what stops a ten-slide carousel reading as a form. **(thin)**
- **One isolated element per slide, not per carousel,** because each slide is seen alone. **(thin)**
- **Cover slide.** The one place for an oversized element bleeding off the frame edge, pointed at the headline, because a cover is first seen at thumbnail size and a bleeding element is the only thing that survives 270px intact. **(thin)**
- **Last slide.** The call to action is the isolated element, and it must clear the 180px chrome zone. Check this on a real export every time, since this is the specific way a carousel loses its call to action.

## Checklist

- [ ] Every value on the ladder; five or fewer distinct values on any one frame
- [ ] Each value scoped to its legal properties and aliased to an intent name
- [ ] The intended relationship named for every adjacent pair; no equidistant orphans
- [ ] Exactly one element isolated
- [ ] Intervals vary, and every change of interval sits on a real structural boundary
- [ ] Asymmetry survives the masked-anchor test
- [ ] At least 30 percent of the canvas empty, measured rather than estimated
- [ ] Edge sweep passes: dead band, reading margin, chrome zone, crop-safe box, measure cap
- [ ] Legible at 270px; carousel frames identical slide to slide
- [ ] Every test in the table run, ending with the degraded-state check

## The ultimate test

Name what the largest empty region on the piece is doing, in one sentence, without using the words clean, modern or minimal. If the sentence says what the emptiness lets a reader do, it is composition and the piece is finished. If the only honest sentence is that the region is empty, the piece is thin at larger scale, and no further spacing will fix it: the fix is upstream, in what the piece has to say. Every mechanical test in the table can pass while this one fails, which is why it is last.

## What an agent can run, and what it cannot

**Can run, mechanically:** the gap audit; the ratio check, given a stated group structure; the step-visibility test; the edge sweep; the measure cap; carousel frame-drift by overlaying slides; value hygiene, meaning scoping and alias coverage; the macro-space fraction by blacking out bounding boxes and reading the white fraction; the isolation count, given a clearance threshold; a crude squint test by blurring, thresholding and counting connected regions; the thumbnail render at 270px; and the degraded-state render.

**Cannot:** decide how much macro space the piece deserves, which is the irreducible call; tell load-bearing emptiness from a thin piece, which requires knowing what the piece is for; run the recall test, which requires a memory it does not have; tell an anchored asymmetric layout from a broken one; set the register, which is a brief decision; correct optically; decide which element is worth isolating, which is the argument of the piece; or judge whether a quiet texture still reads as breathing room. On that last one, default to real emptiness: a texture that is slightly too busy fails silently, because it still looks like a decision rather than an error, while genuine emptiness cannot fail that way. Use texture as whitespace only when you can run the squint test on the real export.

## Where this skill should lose

**When the question is where the edges and the columns are.** Use `dsn-grid`. A grid distributes space too, so the split is by what the space is measured from. The grid owns space measured from the canvas: the page margin, how many columns there are, the gutter between them, and which columns an element spans. This skill owns space measured from the content: the gap between two elements, the padding inside one, and the size of the region left carrying nothing. Concretely, deciding that the margin is 72 and that the body text starts in column 2 of 6 is grid work. Deciding that the gap under the eyebrow is 32 and the gap under the headline is 64 is this skill. When a grid already exists, its margin and gutter win over the dead band and ladder values here, because an element snapped to a column cannot also be snapped to a different edge value, and the grid's figures are what every other element on the page was placed against. Keep this skill for the vertical gaps between content groups, which a column grid does not set, and for the within-group to between-group ratio. Where both set a boundary ratio, take the stricter: a grid demanding four of its own units between groups already satisfies the one-step rule in test 2. Two figures are this skill's even though they look like grid figures, and they outrank the grid when they conflict with it: the safe zone and the crop-safe box a platform imposes. A grid is derived from the canvas you chose; a safe zone is a constraint the delivery surface applies to it, so if a 72px margin puts a date inside a region the feed may crop, the margin moves and the grid gets recomputed around the safe figure. The base unit everything else is a multiple of is also set here, and the grid takes it from this skill rather than choosing its own.

**When the question is leading, tracking or how wide a text column should be.** Use the skill that sets type, `dsn-typeset`. This skill treats the comfort floor inside a paragraph as given and will not tell you what it is. Any figure here described as a gap between lines of a paragraph is really leading, and setting it here will fight whatever set the type.

**When the question is which element should be first.** Use `dsn-hierarchy`. This skill can give one element clearance, but it cannot tell you which element deserves it, and principle 4 is unusable until that is decided elsewhere.

**When the question is which region of the frame is the empty one.** Use `dsn-composition`, which owns where each element sits and the path the eye takes between them. The division on empty space is worth stating because both files claim part of it: this skill decides how large an empty region is and holds the decision that it carries nothing, and that file decides which region it is and what the emptiness points the eye at. A piece can have exactly the right amount of air in exactly the wrong place, and that repair is placement, not a gap value.

**When the question is whether the weight sits right.** Use `dsn-balance`. Mode A step 7 and test 11 only ask whether an asymmetric layout has an anchor at all. How much counterweight, and where, is balance work.

**When the question is what the values should be named and how they propagate across many pieces.** Use `dsn-tokens`. Mode A step 3 gives the minimum, five values scoped and aliased. A naming system, a two-tier structure of primitives and semantic aliases, and the discipline of single-point propagation are a larger job than one piece needs.

**When the question is how a multi-slide sequence should pace.** Use `dsn-sequence`. The carousel rules here freeze the frame and set the gaps inside it; what goes on which slide, and in what order, is sequence work.

**Not covered anywhere in this skill, and worth knowing before you rely on it:** optical margin alignment and hanging punctuation, which is where most of the remaining quality in a text block lives; baseline grids and vertical rhythm as a system; how a spacing ladder should behave across breakpoints, since every value here is a fixed pixel value for a fixed canvas; print safe areas, bleed, trim and binding gutters, where a margin has to survive a guillotine; accessibility minimums, including minimum touch target size and the text-spacing criterion that lets a user override your values, which is a real gap for anything interactive; and non-Latin, vertical and right-to-left settings, where micro-space conventions differ materially.

## Writing the output

Plain words, full sentences. Name the element and the measurement: "the 32px gap under the eyebrow", not "the vertical rhythm". Give the computed figure and the threshold it was checked against, so the reader can disagree with the threshold rather than with your judgement: "26 against a required 28" beats "too tight". Lead with the principle, then the numbers as options, because the right amount depends on the piece. Say which tests you ran and what each returned, including the passes, since a pass and a test you skipped look identical in a summary that only lists failures. Report measurable failures as failures and judgement calls as judgement calls, and label a figure marked thin as a working default at the point you use it.

Sources, corroboration, the disagreements between them and how each was resolved, the unreliable figures, the independent audit and what none of it covers are in `references/provenance.md`.
