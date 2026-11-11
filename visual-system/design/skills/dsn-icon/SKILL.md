---
name: dsn-icon
description: Building or judging icons that must read small and look like a family, when two keep being confused, or a set stops communicating. Gives a stroke spec and a verdict.
---

# The icon set

This skill builds and judges families of small marks: interface icons, glyphs, bullets, arrows, number badges, anything that has to be identifiable at a size where almost nothing survives. The single idea underneath it is that an icon is read as a silhouette before it is read as a drawing, and a set is read as a row before any member is read on its own. Those two facts decide almost everything else. They are why the first thing you build is not an icon but the shared invisible frame every member will be drawn on, why the test that matters is run on a flattened shape by someone who does not already know the answer, and why the deliverable is a written specification rather than a folder of files. A set with no written rules is a coincidence that held for as long as one person was drawing.

## What this skill is for

- building a set of icons, glyphs or small marks that look like a family
- judging whether a set is consistent, and whether consistency has cost it clarity
- making a shape read at 16 to 24 pixels, or at the equivalent size inside a post graphic
- telling two icons apart when their subjects are nearly the same thing
- writing a spec someone else, or an agent, can apply without redesigning the set

## Confidence

The rules here are practitioner accounts and arithmetic derived from them, not measured findings. No icon in this method was ever tested on a user, both silhouette tests below are normally run on the designer's colleagues, and nothing here is backed by a controlled study. Read it as a craft method that has held up in production, not as a result. Rules marked **(thin)** rest on a single account and should be treated as one person's house style: keep them if they work for you, drop them without argument if they do not.

Two further limits. Every pixel figure here is a convention rather than a threshold, and the conventions conflict, which is why this file tells you to pick one value and hold it rather than telling you which to pick. And the optical-mass rule in principle 7 is the thinnest important claim in the method, which is why the next section derives it with arithmetic you can check instead of asking you to take it on trust.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

The rest of this file assumes these. None of them are optional vocabulary; each one names something you will have to decide.

**Canvas.** The fixed square frame every member of the set is drawn inside, stated in pixels. A 24 pixel canvas means every icon in the set is drawn in a 24 by 24 box, regardless of what shape it contains.

**Trim ring** (also called padding or the safe area). A band of fixed width just inside the canvas edge that no painted pixel enters. It exists because a mark drawn to the very edge of its frame gets clipped on render or composite, and the clip takes the outermost pixel of the drawing rather than empty space.

**Live area.** The canvas minus the trim ring on all four sides: the box the drawing lives in. On a 24 pixel canvas with a 2 pixel trim ring, the live area is 20 by 20.

**Keyline.** One shape, at one fixed size, used as an invisible guide that the dominant form of an icon is drawn to fill. Not a line on a page grid.

**Keyline family.** The keylines the whole set shares, one per basic shape class: a square for boxy subjects, a circle for round ones, a tall rectangle for upright ones, a wide rectangle for lying-down ones. Every member is built on one of them.

**Armature.** The canvas, the trim ring and the keyline family together. Two icons on the same armature are provably related; two that merely look similar are not.

**Silhouette.** The outline of the mark with every internal detail, stroke and colour removed, filled as one flat shape. The thing a reader's visual system resolves first.

**Negative space.** The space between and around the parts of a mark. At small sizes it is what makes two parts read as two parts, so it is part of the drawing rather than what is left over from it.

**Stroke weight.** The painted thickness of a line, in pixels. A 24 pixel icon drawn with 2 pixel lines has a stroke weight of 2.

**Stroke alignment.** Where the painted band sits relative to the geometric path it follows: **inside** keeps all the paint within the path, **centre** splits it half in and half out, **outside** puts it all beyond the path. It matters because a path can sit exactly on the live-area boundary and still paint into the trim ring, and how far it overruns is decided entirely by alignment.

**Cap.** How a stroke ends where its path stops: **butt** ends flush, **round** adds a semicircle of radius half the stroke weight, **square** adds a square of half the stroke weight. So a round or square cap makes a line longer than its path by half the stroke weight at each end, changing both apparent length and where the drawing actually reaches.

**Join.** How two strokes meet at a corner: mitred to a point, rounded, or bevelled flat.

**Terminal.** The visible end of a stroke: the cap plus any shaping you gave it. Named separately because a set can hold one cap setting and still have inconsistent terminals if some lines taper and others do not.

**Corner radius.** The radius of rounding on a corner of a filled shape, in pixels. Zero is a sharp corner.

**Geometric centre.** The midpoint of a bounding box, which is what every alignment tool gives you.

**Optical centre.** Where a shape looks centred, which is a different point whenever its mass is unevenly distributed. A triangle inside a circle is the standard case: aligning its bounding box to the circle's centre leaves it looking as though it has slid toward its own point, because a triangle's mass sits toward its base. Fix it by eye, then measure what you did so the correction repeats across the set.

**Optical mass.** How heavy a mark looks, as distinct from how large its bounding box is. Two marks can occupy identical boxes and look clearly unequal, which is the whole reason a keyline family uses different dimensions for different shapes.

**Detail density.** How much incident a mark carries: number of distinct parts, corners and separate strokes. Members with very different detail densities do not read as a family even when every measurable rule is held.

**Semantically adjacent.** Two subjects a reader could confuse because they mean nearly the same thing: file and document and page and note; send and share and upload and export. These pairs are where sets fail in use, and making them more consistent makes them worse.

**Whole-pixel.** A dimension, position or stroke weight that is an integer number of pixels. A value like 7.25 lands a painted edge across a pixel boundary, and the renderer resolves that by half-filling the boundary pixel, which reads as blur.

**Boolean operation.** Combining shapes by union, subtraction or intersection. These routinely leave stray sub-shapes of near-zero area behind, invisible at working zoom and visible as specks at export.

**Live stroke.** A stroke still stored as a stroke rather than converted to a filled outline. It is a rendering instruction, not geometry, so it may or may not scale with the artwork when someone resizes the icon downstream.

**Fill icon and line icon.** A fill icon is a solid shape; a line icon is an outline of the same subject at some stroke weight. The same silhouette carries noticeably more optical mass as a fill, which is why the choice is made once for the family rather than per member.

**Downscale factor.** The ratio between the pixel size of the working file and the size a reader sees. Working at 1080 pixels wide for a phone feed means a nominal factor of 3, so a 48 pixel element is seen at about 16 points. That figure and the 4x stress case are derived in `reference/canvas-assumptions.md`.

## The mechanism: why a circle has to be drawn bigger than a square

A keyline family is a set of different dimensions for different shapes, and the reason it exists is that perceived size tracks a shape's **area** far more closely than it tracks its bounding box. Draw a circle and a square with the same bounding box and the circle looks smaller, because it is: a circle inscribed in a square of side s has area πs²/4, which is 78.5 percent of the square. The missing 21.5 percent is the four corners, and the eye reads the shortfall as the circle being undersized rather than as the circle being round.

So the correction is arithmetic. To give a circle the same area as a square of side s, set the diameter d so that πd²/4 = s², which gives d = 2s/√π, or d ≈ 1.128s. **A circle's diameter has to exceed a square's side by about 13 percent to look the same size.** That single ratio is the content of the whole convention, and you can check it against the widely copied 24 pixel figures below: a square keyline of 18 and a circle keyline of 20 is a ratio of 1.111, against the computed 1.128, so the published circle is about 1.5 percent smaller than exact area matching would give.

Run the same check across all four keylines of the 24 pixel convention and the areas come out as follows.

| Keyline | Dimensions | Area in square pixels |
|---|---|---|
| Square | 18 x 18 | 324 |
| Tall rectangle | 16 x 20 | 320 |
| Wide rectangle | 20 x 16 | 320 |
| Circle | ⌀20 | π x 10² = 314.2 |

All four land within 3.1 percent of each other on area, while their bounding dimensions differ by as much as 11 percent. So it is an equal-area system rather than a lookup table, which means you can extend it to shapes nobody has published figures for. Set your square keyline at side s, then solve for any other shape:

- **Circle:** diameter = 1.128s.
- **Rectangle of aspect ratio r:** short side = s/√r, long side = s√r. At r = 1.25 that is 0.894s by 1.118s, which on an 18 pixel square gives 16.1 by 20.1, reproducing the published rectangles.
- **Equilateral triangle:** side ≈ 1.52s. A triangle also needs optical centring, since its mass sits toward its base.
- **Regular hexagon, flat to flat:** height ≈ 1.075s.
- **Diamond, meaning a square rotated 45 degrees:** diagonal = s√2 ≈ 1.414s.

Check the result by eye at final size, because area matching is a good model of perceived size and not a perfect one: a shape with long thin extensions reads lighter than its area says, and a compact shape reads heavier. Where the eye and the arithmetic disagree, the eye wins and you record what you changed.

The claim that a keyline family exists to equalise apparent size is **(thin)**. The arithmetic above stands without it, which is why this file carries the arithmetic rather than the claim.

## Shape: what to use it for, and what to refuse

Three claims get made about shape here. Two are usable, one is not, and the difference matters because the unusable one is the most quotable.

**Refused: shapes carry inherent personality.** The familiar triad says squares read strong, stable and dependable, circles soft, friendly and adaptable, triangles wild, energetic and dangerous. There is no mechanism behind it, no prediction it makes that could fail, and no test on anyone who did not already know both the shape and the intended personality before looking. Every demonstration offered for it is a finished design read backwards. Its honest version, which some of its own teachers give, is a prompt for getting unstuck when you cannot decide what to draw. Use it that way if it helps. Never use it as a reason, put it in a spec, or defend a drawing with it.

**Carried: geometric difference, because it is testable.** A square is boxy, squat, flat-sided and right-angled. Those are facts about squares rather than feelings about them, and they support a checkable claim: shapes that differ geometrically are faster to tell apart. That is the basis of the adjacent-pair test below.

**Carried, and the most important mechanism here: resemblance to the referent.** A mark for fire is drawn pointy because flame is pointy; a mark for rock is boxy because rock is boxy. The shape reads because it looks like the thing it denotes, which is the whole job of an icon and has nothing to do with psychology. Testable in one move: show the silhouette, ask what it is.

One further piece of perceptual ground is worth keeping, because it underwrites consistency rather than affect: elements near each other or alike are perceived as belonging together. That is why a shared armature and a repeated shape vocabulary make a family, and why unequal internal gaps break one.

## The principles

Each rule names the test that checks it. The tests are in the table further down.

**1. The silhouette is the thing that must read.** Everything after it is refinement on a shape that already works, or decoration on one that does not. The mechanism is order of resolution: the outline resolves before anything inside it, so an unreadable silhouette cannot be rescued by internal detail, and at small sizes the detail is gone anyway. *Test:* solid-fill silhouette.

**2. Readability beats cohesion wherever the two conflict.** A set can be made to match so thoroughly that its members stop communicating, which is a failure even though the set looks tidy, because an icon nobody can identify has no remaining purpose. Consistency is a means to a family, not the goal. *Test:* set-row comparison, then re-run the silhouette test on any member you adjusted for cohesion.

**3. Every member is built on one shared armature at one size.** One canvas, one trim ring, one keyline family, all fixed before anything is drawn. This is what makes members provably related rather than approximately similar: relatedness becomes a measurement instead of an opinion, so a new member can be checked by someone who was not there. *Test:* keyline overlay.

**4. Leave a trim ring and let nothing enter it, including paint that overruns its path.** The reason is mechanical: a mark drawn to the frame edge gets clipped on render, and the clipped pixel is drawing rather than margin. The part everyone misses is that a path inside the live area can still paint outside it, through stroke alignment and through caps. **(thin)** The usual figure, 2 pixels on a 24 pixel canvas, is inherited rather than derived, and the people who publish it routinely work to about double it. *Test:* trim breach check.

**5. One stroke weight, one corner radius, one cap, one join, one terminal, held across the set.** The holding-constant is the craft. **(thin)** The numbers are conventions and they conflict: as a fraction of canvas the common weights are 6.25 and 8.33 percent, which is a visibly heavier house style rather than a disagreement about a threshold. Pick one fraction, convert it to whole pixels, write it down. *Test:* measurement against the spec, plus the whole-pixel audit.

**6. Members must be distinguishable from each other, not merely from nothing.** An icon that reads perfectly alone can still be unusable because the icon beside it reads the same. When two subjects are semantically adjacent, similar proportions make them harder to separate, and the fix is unlike dominant geometry rather than more consistency. **(thin)** Nobody working on icons raises this problem; it is reasoned across from people drawing casts of characters. *Test:* adjacent-pair test.

**7. Equalise optical mass across the set, by measurement first and then by eye.** Use the equal-area arithmetic to get every member onto a comparable footing, lay the set out in a row at final size, and fix whichever member reads heavy, light, busy or empty. **(thin)** Hold the counter-position as a limit: equalise until members stop being distinguishable and you have traded principle 6 for tidiness. The residual you accept is a judgment; the direction of travel is not. *Test:* set-row comparison and the equal-area check.

**8. Budget detail by the size the mark will ship at, not the size you draw at.** Detail that reads at hero scale is noise at 24 pixels, and a noisy silhouette is the second most common way a mark stops being identifiable. The constraint on reduction is that the reduced version still reads as the same family. *Test:* size-down test and detail-density check.

**9. Centre nested elements optically, then record the offset.** Mathematically centring a shape whose mass is unevenly distributed looks wrong, so you nudge it by eye. The skipped step is the second one: measure the nudge and put it in the spec, or the next member gets a different nudge and the set drifts. **(thin)** *Test:* keyline overlay.

**10. The written spec is the deliverable. The icons are a by-product.** A set survives contact with other people only if its rules are enumerated. A set a stranger cannot extend is a folder of files plus a sentence about consistency. *Test:* spec-handoff test.

**11. Treat no number here as a principle.** Pick one value per property and hold it, which matters far more than which value you pick. The conflicts are laid out under "Choosing the numbers" below.

## How to work

### Mode A: building a set

1. **Fix the canvas and the trim ring.** Choose the canvas from what you are shipping into rather than from taste: the smallest size the set will be used at, scaled by a whole-number factor so every derived figure stays on whole pixels. A canvas that is a multiple of 16 keeps both common stroke fractions integral. Set the trim ring as a fraction of canvas and keep that fraction when you scale.
2. **Build the keyline family before drawing anything.** Set the square keyline first, as a fraction of the live area, then derive the circle, the rectangles and any extra shape with the formulas above. Check the results by eye at final size before trusting them, and record any adjustment.
3. **Decide fill or line for the whole family, once.** One decision for the set, not per member, because the two carry different optical mass for the same silhouette. Mixing within a set is contested: one position forbids it, one allows it to express state such as selected against unselected, one ships fill and line as two parallel complete sets. Any of the three is defensible. Deciding per icon as you go is not.
4. **Harvest before you derive.** **(thin)** Drop icons that already work onto your armature and see which keyline each one lands on. Faster than reasoning the family out from nothing, and it occasionally reveals that a keyline you planned is unused and one you did not plan is required.
5. **Draw the dominant form onto its matching keyline.** The dominant form is the one shape a reader would name if they could only name one. Fill the keyline with it, then place internal elements optically rather than mathematically, per principle 9.
6. **Build a shared shape vocabulary and reuse it.** Enumerate the recurring parts: the corner, the terminal, the curve radius, the arrow head, the container, the badge. One parent shape repeated through every member is what reads as a family. A member built from parts outside the vocabulary is the drift you will not notice until there are thirty of them.
7. **Hold two size tiers inside each member, not four.** **(thin)** Keep the ratio between big and small elements the same across the set, because ratios borrowed from a differently proportioned member are a recognisable kind of wrong. An icon has too few parts for more than two tiers.
8. **Run the gap and pixel audits.** **(thin)** Set internal gaps equal to the stroke weight, then check them with a rectangle of exactly the stroke weight in a loud colour dropped into every gap. Confirm nothing sits on a fractional pixel.
9. **Write the spec as named features with named treatments.** See the section below. This is the deliverable.
10. **Prepare for output.** Convert live strokes to filled outlines before export, since a live stroke may not scale with the artwork downstream. Re-check the trim ring afterwards, because converting a centre or outside aligned stroke moves the painted edge outward. Sweep in outline view for stray sub-shapes.
11. **Run the size-down test last**, at the smallest shipping size, at 100 percent zoom on a real display.

### Mode B: judging a set

1. Lay every member in a row, final size, one colour, grid off.
2. Name the member that reads heavier, lighter, busier or emptier than the rest, and say on which of those four properties.
3. Silhouette-test the three weakest members cold, on someone who has not seen them and does not know the subject list.
4. Overlay the keyline family and report any member off its armature or breaching the trim ring.
5. Measure stroke weights, corner radii, caps, joins and internal gaps. Report every value that is not the set's value.
6. Find the semantically adjacent pairs and check they are distinguishable from each other rather than merely identifiable alone.
7. Report whether consistency has cost clarity anywhere, naming the member.
8. Read the spec and say whether a stranger could add a member with it.

## Writing a spec someone else can apply

The useful formulation is not "keep it consistent". It is an enumerated list of named features, each with one named treatment, so every recurring element has exactly one decided answer. Write out every one of these, with a value:

canvas size, trim ring width, keyline family and each dimension, fill or line, stroke weight, stroke alignment, cap, join, terminal shaping, outer corner radius, inner corner radius, internal gap, minimum element size, permitted angles, number of size tiers and the ratio between them, arrow head construction, container shape, badge shape, colour treatment, and the export format with whether strokes are outlined.

The test of a spec is not whether it reads well. It is whether someone who did not design the set can add a member to it, and whether you can tell from the result that they were following the spec rather than guessing. The failures it prevents are the expensive ones: visual drift, where assets start looking as though they came from a different brand because the direction moved between jobs, and production friction, where every new request restarts the same argument about proportions, weight and format from zero.

Keep one distinction in the spec's preamble, because it settles arguments that otherwise go in circles: whether a mark is good is one question, and whether it is good for this set is a different one. A mark can pass the first and fail the second, and the spec is what makes the second answerable by someone other than its author.

## Choosing the numbers, and then holding them

These conventions conflict openly, and the genre presents them as settled. Stated plainly so you stop looking for the right answer:

- **Stroke weight on a 24 pixel canvas** splits evenly between 2 pixels and 1.5 pixels, which as fractions of canvas are 8.33 and 6.25 percent.
- **Whether decimal stroke values are legitimate** has one position banning them as blurry and another shipping 1.5 as a house standard. The ban and the 1.5 recommendation sometimes appear within a minute of each other, which is reason to treat both as taste.
- **Corner radius** has at least three incompatible answers: a specific 2 pixels, a preference for odd numbers such as 3 or 5 with no reason offered for oddness, and "round it to the maximum".
- **Whether stroke weight stays constant or scales with canvas size** has positions on both sides and no stated reconciliation, though the obvious one is constant within a size and scaled across sizes: hold stroke at a constant fraction, say 6.25 percent, giving 1 pixel at 16, 1.5 at 24, 2 at 32 and 4 at 64, then thin deliberately at the largest sizes if the mark starts reading as a graphic rather than an icon.
- **Trim ring width** is published as a fraction that is not constant across the published sizes, and the people publishing it work to roughly double their own figure while still calling it tight.

So: **pick one value per property, write it down, hold it.** Where this file gives a figure it is reporting a convention, not a threshold. The derivations are different in kind: the equal-area formulas, the cap overshoot arithmetic and the stroke-alignment arithmetic can all be checked with a calculator and do not depend on anyone's preference.

## Applied to carousel and post graphics

The canvases are square 1080 x 1080 and portrait 1080 x 1350, with a nominal downscale factor of 3 and a stress case of 4, per `reference/canvas-assumptions.md`.

### Case 1: a row of icons beside body type

The constraint is the type, so derive the icon from it. Body type at 48 pixels renders at 48 / 3 = 16 points, which is readable, and at the 4x stress case 48 / 4 = 12 points, which is the stated floor. Take a typical sans with a cap height of about 0.70 of the em, so the cap height is 48 x 0.70 = 33.6 pixels. An inline icon reads as matched to the type when its dominant form matches cap height rather than when its box matches the line.

So the square keyline wants to be about 34 pixels. The square keyline is 18/24 = 0.75 of the canvas in the convention, so canvas = 33.6 / 0.75 = 44.8 pixels. Round to 48, because 48 is a multiple of 16 and exactly twice the 24 pixel convention, which keeps every derived figure whole. The family then scales by 48 / 24 = 2:

| Feature | Figure at 48 px canvas | Derivation |
|---|---|---|
| Trim ring | 4 px | 2 x 2 |
| Live area | 40 x 40 | 48 minus 4 each side |
| Square keyline | 36 x 36 | 18 x 2 |
| Circle keyline | ⌀40 | 20 x 2 |
| Tall rectangle | 32 x 40 | 16 x 2 by 20 x 2 |
| Wide rectangle | 40 x 32 | as above, rotated |

Check the square keyline against the target: 36 against 33.6 is 7.1 percent taller, which is close enough to accept and is the kind of residual you record rather than chase. Check equal area: square 36 x 36 = 1296; circle ⌀40 gives π x 20² = 1256.6, which is 3.0 percent under. Exact area matching would want d = 1.128 x 36 = 40.6, so the 40 is 1.5 percent small, the same residual as at 24 pixels.

Now the stroke. At 6.25 percent of canvas it is 48 x 0.0625 = 3 pixels; at 8.33 percent it is 48 x 0.0833 = 4 pixels. Both are whole pixels, which is why the multiple of 16 was worth rounding to. Which one to pick is decided by the type beside it: a regular-weight sans at 48 pixels has stems of roughly 48 x 0.08 = 3.8 pixels. So a 4 pixel icon stroke matches the type's stems and a 3 pixel stroke reads lighter than the type. If the icons should sit as equals with the text, take 4. If they should recede, take 3 and say in the spec that the recession is deliberate.

Take 4. Internal gaps then equal 4 pixels, which renders at 4 / 3 = 1.33 points nominal and 4 / 4 = 1 point at the stress case. One point is the edge of existing, so the size-down test at 25 percent is not optional here: the specific failure to look for is two gaps closing into one mass.

Two overruns now become computable rather than vague. With a 4 pixel stroke and **round caps**, each line extends half the stroke weight past its path end, so 4 / 2 = 2 pixels. A path drawn exactly to the live-area boundary therefore paints 2 pixels into a 4 pixel trim ring, consuming half of it. The fix is arithmetic: with round or square caps, stop paths 2 pixels short of the live area. With **outside stroke alignment** the whole 4 pixels sits beyond the path, so a path on the live-area boundary consumes the entire trim ring and the mark is flush with the canvas edge, which is the clip failure the trim ring exists to prevent. Centre alignment consumes 2 of the 4. Inside alignment consumes none. Set alignment to inside and record it.

### Case 2: one icon as a slide's hero mark

Scale the convention to the full square canvas: 1080 / 24 = 45, so trim ring 90, live area 900, square keyline 810, circle ⌀900, rectangles 720 x 900. Stroke at 6.25 percent of 1080 is 67.5 pixels, which is not whole, so either accept a half pixel at a size where it is invisible, or round to 68, or take the 8.33 percent figure which gives exactly 90.

Rendered, a 90 pixel stroke is 90 / 3 = 30 points. That is a poster weight, and the useful conclusion is that at hero scale the 24 pixel stroke fraction has stopped being a legibility figure and become purely a style choice. The detail budget inverts with it: at 1080 the smallest reliable feature is the shared 36 pixel working floor, which is 3.3 percent of the canvas, against 24 pixel icon detail where the equivalent floor is the stroke itself. You can afford detail here that would be noise in the row. If the set contains both uses, the hero version is a different member of the family drawn to the same vocabulary, not the small one scaled up.

### What follows for a carousel specifically

- **Set-row comparison is the highest-value check available**, because a carousel presents the set in sequence across slides. An unequal member is visible there in a way it never is on a working artboard.
- **A deck is a set even when the marks are not icons.** Arrows, rules, containers, bullets and number badges are members and belong in the spec. They drift first, because nobody thinks of them as designed.
- **Dark ground is a second case this method does not cover.** Light strokes on dark bloom optically and generally need thinning, and none of the arithmetic here tells you how much. Treat any dark-ground stroke weight as needing its own eye check, and take thresholds from the skill that owns contrast.

## Tests

Every verdict here is decidable by someone holding only this file and the artwork.

| Test | Catches | Verdict |
|---|---|---|
| **1. Solid-fill silhouette** | A mark that is not identifiable at all | Flatten to one flat fill, no detail, no colour, no stroke. Show it to someone who has not seen the set and does not know the subject list, and ask what it is. Fails if they cannot name the subject or a close synonym in one attempt. |
| **2. Negative-space fill** | Blob collapse, before it ships | Fill only the space between and around the parts and leave the parts empty. Fails if any two parts that should read separately are joined in the filled version. |
| **3. Set-row comparison** | A member out of family on weight or busyness | Every member in a row, final size, one colour, grid off. Ask which one is odd. Fails if any member is named by two separate viewers, or if you can name one on a property: heavier, lighter, busier, emptier. |
| **4. Keyline overlay** | A member off the shared armature | Place the keyline family over the finished icon at low opacity. Fails if the dominant form does not fill its matching keyline to within about 5 percent on both dimensions, or if any painted pixel sits in the trim ring. |
| **5. Equal-area check** | A keyline family that does not actually equalise | Compute the area of every keyline. Fails if the largest and smallest differ by more than about 5 percent, or if the circle's diameter is not within 3 percent of 1.128 times the square's side. |
| **6. Spacer-box gap check** | Internal gaps that are not the set's gap | Make a rectangle exactly the stroke weight in a loud colour and drop it into every internal gap in every member. Fails on any gap the rectangle does not fit, or any gap it fits with visible space left over. |
| **7. Whole-pixel audit** | Half-pixel blur at render | List every dimension, position and stroke weight in the file. Fails on any non-integer value, unless the canvas is large enough that the value is below one third of a rendered point, in which case record the exception. |
| **8. Trim breach check** | Paint in the trim ring from caps, from alignment, or after conversion | Add half the stroke weight to every path end carrying a round or square cap, and fail if the result crosses the live-area boundary. Fail separately if stroke alignment is anything other than inside while a path sits within half a stroke weight of that boundary. Re-run after converting strokes to outlines and fail if any member's bounding box grew past the live area. |
| **9. Outline-view sweep** | Stray sub-shapes from boolean operations | Switch to outline or wireframe view after every boolean operation. Fails on any sub-shape you did not intend, including ones too small to see at working zoom. |
| **10. Redraw from memory** | A family whose rules are too complex to be rules | Put the reference away and draw one member again. Fails if it differs from the original on any specified feature: stroke weight, corner radius, cap, number of parts, which keyline it sits on. |
| **11. Shape-ingredient check** | Parts that are not in the family's vocabulary | Cut each component shape out of a finished member and look at it alone. Fails on any part whose corner, terminal or curve is not on the spec's enumerated list. |
| **12. Adjacent-pair test** | Members identifiable alone and confusable together | List every pair of semantically close subjects. Show both silhouettes side by side, in random order, to someone holding the two labels but not the mapping, and ask which is which. Fails on any pair they get wrong or cannot answer. **(thin)** |
| **13. Size-down test** | Detail budgeted for the drawing size | Render at the smallest shipping size, 100 percent zoom, physical display, never scaled in the editor, then re-run tests 1 and 3 there. Fails if a member that passed at drawing size fails at shipping size. **(thin)** |
| **14. Detail-density check** | A member that matches every measurable rule and still looks foreign | Count distinct parts, corners and separate strokes per member. Fails if any member exceeds roughly twice or falls below roughly half the set's median on any of the three. |
| **15. Spec-handoff test** | A set that cannot be extended | Give the spec and one existing member to someone who has never seen the set, and ask for the next icon you need. Fails if the result needs correcting on any feature the spec names, and fails separately if you cannot tell they were following the spec rather than guessing. |
| **16. Stroke-beside-type check** | A stroke that fights or disappears next to its type | Measure the stem width of the type the icons sit beside, at final size. Fails if the icon stroke differs from the stem by more than about 25 percent either way and the spec does not call the difference deliberate. |

## Failure patterns

Named concretely so you can recognise one in the hour it happens.

**Blob collapse.** Parts bunched close enough that at shipping size the silhouette is a single mass, so the mark reads as a shape rather than a thing. Caught by tests 2 and 13, and by nothing at drawing size.

**Noisy silhouette.** The opposite failure: so much contour incident that no part of the outline is diagnostic, so nothing is identifiable even though everything is visible.

**Scale-ratio mismatch.** Element-size ratios borrowed from a differently proportioned member, so a small part is small in a way that does not match the rest of the set.

**Under-filled container.** A narrow mark floating in a live area it does not use, reading small and light next to members that fill theirs. The usual cause is drawing the subject at its natural proportions instead of to the keyline.

**Cohesion bought with clarity.** Every rule held, the row beautiful, and two members no longer telling a reader which is which. The tidiest sets fail this most often, because the pressure that produced the tidiness is the pressure that erased the difference.

**Indistinguishable members.** Semantically adjacent subjects drawn with the same dominant geometry. Each passes the silhouette test alone and the pair fails test 12, which is the only test that would have caught it.

**Optical-centre miss.** A nested element aligned to its bounding box, looking as though it has slid toward its own mass. Common with triangles, arrow heads and anything asymmetric inside a circle.

**Corner clog.** Strokes merging where a curve turns tight, so a corner reads as a filled blob. Shows up at shipping size and not before.

**Half-pixel blur and the ragged diagonal.** Fractional values landing paint across pixel boundaries, and arbitrary angles rendering broken. The 45 degree case is mechanically sound because it lands cleanly on a square pixel grid; claims about other specific increments minimising half pixels are not, and no reason is ever given for them.

**Trim breach on conversion.** Inside the live area as live strokes and outside it as outlines, because the stroke was centre or outside aligned. Caught by test 8 only if you re-run it after converting.

**Live stroke shipped.** The icon is scaled downstream, the stroke does not scale with it, and the set's weight changes at one size and nowhere else.

**Artifact litter.** Specks of leftover geometry from boolean operations, invisible at working zoom and visible at export.

**Wrong-size reuse.** A mark crafted at one size displayed at another, so its stroke fraction and detail budget are both wrong. The remedy is to ship the sizes you intend to be used rather than to allow resizing.

**Visual drift.** Members added over months, each one reasonable, the set no longer a set. The signature is that no single member looks wrong.

**Drawing every icon before writing the spec.** The spec then describes what happened rather than ruling on what comes next, so it cannot adjudicate the next member.

**Shape psychology used as a reason.** A drawing defended by what a square supposedly means. Refused above.

**Treating a convention as a threshold.** Arguing about 1.5 against 2 pixels as though one were correct. The argument has no answer; writing either one into the spec ends it.

## Checklist

- [ ] Canvas and trim ring fixed, as fractions that stay whole when scaled
- [ ] Keyline family derived by area and checked by eye before drawing
- [ ] Fill or line decided once, for the family
- [ ] Existing icons harvested to learn which keylines are needed
- [ ] Shared shape vocabulary enumerated and reused
- [ ] Optical mass equalised across members, residuals recorded
- [ ] One stroke weight, radius, cap, join and terminal, measured and confirmed
- [ ] Stroke alignment set to inside, cap overshoot computed
- [ ] Gaps match the stroke
- [ ] No fractional pixels
- [ ] Two size tiers, ratio shared across the set
- [ ] Semantically adjacent pairs distinguishable from each other
- [ ] Spec written as named features with named treatments
- [ ] Strokes outlined, trim re-checked after conversion, artifacts swept
- [ ] Size-down test run at real size on a real screen

## The ultimate test

Hand the spec and one existing member to someone who has never seen the set, ask them to add the icon you most need next, and look at what comes back. If it belongs, the system is real. If it only belongs after you fix it, you have a folder of icons and a sentence about consistency.

## What an agent can run, and what it cannot

**Can run, fully.** Measurement of every stroke weight, corner radius, gap and dimension against the spec. The whole-pixel audit. The equal-area check. Keyline overlay geometry, including whether a dominant form fills its keyline and whether any painted pixel enters the trim ring. Cap overshoot and stroke-alignment arithmetic. Set-row comparison for which member is heaviest or busiest, since both reduce to counting filled pixels and counting parts. The detail-density count. Checking a proposed new member against a named-feature spec, feature by feature. Describing a silhouette cold, which is a genuine silhouette test provided the agent has not seen the labelled original or the subject list.

**Cannot run.** The final optical-mass judgment, which it can flag by measurement but a person should confirm, because the residual the arithmetic cannot model is exactly the part that needs an eye. Dark-ground stroke compensation. The real size-down test, which needs a physical display at 100 percent rather than a resampled image. Whether the chosen metaphor is right for the audience, which is a question about readers rather than shapes.

**Worth delegating deliberately.** The silhouette test and the adjacent-pair test, because both are void if the tester knows the intended answer. The person who drew the set cannot run either, and nor can an agent that has read the subject list. Give the tester the shapes and withhold the labels.

## Where this skill should lose

**When there is one mark rather than a family.** Use `dsn-mark`, which owns single logos and wordmarks: how a mark carries an identity on its own and what makes one memorable. Close this file as soon as the answer stops depending on the other members, because almost every rule here is a rule about relatedness.

**When the question is where the set sits in a larger system.** Use `dsn-identity`, which owns how the parts of a visual system relate and what else has to change when the set changes. This file assumes the surrounding system is already decided.

**When the question is whether something is legible enough, in numbers.** Use `dsn-contrast`, which owns legibility thresholds and ratios, including the dark-ground case this file names as a gap. This file will tell you a 1 point gap is at the edge of existing; it will not tell you the minimum contrast a stroke needs against its ground.

**When you need the page structure the icons sit in.** Use `dsn-grid`, which owns margins, columns and gutters on a canvas. A keyline is not a page grid, and confusing the two is the most common misreading of this file.

**When the icon has to relate to type.** Use `dsn-typeset`, which owns type size, leading, measure and weight. This file derives an icon from a type size it takes as given; it does not set the type.

**When the question is which colours the set uses.** Use `dsn-palette` for building the palette and `dsn-color` for applying it. This file treats colour as one line in the spec and says nothing about choosing it.

**When the small marks are a multi-frame piece's furniture rather than an icon family.** Progress dots, slide numbers and anything repeated at the same spot on every frame of a carousel are placed and paced by `dsn-sequence`, which decides what crosses each seam and where it sits. This file decides whether those shapes are identifiable at the size they are rendered at and whether they read as siblings, and it supplies the small-size floor that disqualifies most of them. Practical split: how many dots and where the row goes is that file; whether a dot at that size is a dot or a smudge is this one.

**When the spec has to be handed to a build step or an agent as named values.** Use `dsn-tokens`, which turns a figure into a name that resolves and states the rule producing the next one. This file writes the spec and owns every number in it: the keyline size, the stroke weight, the corner radius, the optical compensations and the minimum size. Giving those numbers names, so that nobody retypes a stroke weight and quietly changes it, is that file's job and is worth doing for any set someone else will extend.

## Writing the output

When judging, report in this order:

1. What each weak member reads as, cold, from silhouette alone, in the tester's own words.
2. The odd member from set-row comparison, and on which of the four properties.
3. Every measured value that departs from the set's value, listing the member, the feature, the spec value and the actual value.
4. Any place consistency has cost clarity, naming the member and the pair it is confusable with.
5. Whether the spec would let a stranger add a member correctly, and which named feature is missing if not.
6. One verdict: shippable, revise named members, or no system yet.

Give measurements rather than characterisations: "stroke 3 px against a spec of 4, on two of eleven members" beats "the weights look a bit inconsistent". Say which tests you ran and what each returned, including the passes, because a pass and a skipped test look identical in a summary that only lists failures. Where a finding rests on a convention rather than a derivation, label it as a convention at the point you use it, and where it rests on reasoning carried across from drawing casts of characters rather than icons, say so, because that is the part a reader is entitled to disagree with.

Sources, corroboration, conflicts, derivations, discards and what the method does not cover are in `references/provenance.md`.
