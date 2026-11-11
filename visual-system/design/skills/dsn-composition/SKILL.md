---
name: dsn-composition
description: Arranging a frame, deciding what reads first, a layout that looks wrong with nobody able to say why, or a template others fill. Gives the arrangement and its tests.
---

# Composition

This skill decides one thing: **how position, size and emptiness enforce the order in which a viewer's eye touches the elements of a frame.** The order itself is decided before this file opens, by the skill that ranks elements in words; this file is what makes the frame obey it. A frame with no decided order is not read in a random order, it is skipped, because a viewer who cannot tell what to look at first does not hunt for the answer.

## What this skill is for

Use it when someone wants to:

- arrange a frame: decide what reads first, second and third, and enforce it
- diagnose a layout that looks wrong without an obvious reason
- build a template someone else fills repeatedly: a post graphic, a carousel
- judge a draft before it ships and say what to change, in order of impact

The output is a named focal point, a level ladder with the type sizes and spacing computed for the canvas, a grid with its arithmetic closing, and a verdict per test.

## Confidence

The rules here are practitioner accounts rather than measured findings. Nothing in this file has been tested against an outcome, and every judgment behind it reduces to whether a trained eye thought the frame worked. Rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than settled craft, and several of the movement and flow rules are thin in a way the surface does not show: they look widely held and are not. A number that was inherited rather than worked out is marked thin as well; a number that can be computed from the canvas is computed below instead of asserted.

One further limit: no rule here distinguishes a strong composition from a merely correct one. The mechanics can be run to completion by someone with nothing to say, and they will return a well composed frame that communicates nothing.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Frame.** The bounded rectangle the composition lives in, at its final proportion. Not the artboard you happen to be working on.

**Canvas.** The working file's pixel dimensions. This skill uses two, from `reference/canvas-assumptions.md` at the plugin root: square 1080 x 1080 and portrait 1080 x 1350, the latter a 4:5 ratio.

**Viewing size.** The pixel or point size the piece will actually be *seen* at, which in a feed is roughly a third of the canvas width. Distinct from build size, the size you are looking at while making it.

**Downscale factor.** Canvas width divided by viewing width. This skill uses 3x as the nominal case and 4x as a stress test, both from the canvas file. A 48px element in the working file is seen at about 16pt nominally and 12pt under stress.

**Level.** One rank in the reading order. Level one, written L1, is the first thing read; L2 the second, and so on.

**Focal point.** The single element L1 consists of. The entry point into the frame.

**Carrier of difference.** One visual property doing the work of separating a level from the level below it: size, weight, colour, shape, texture, type style, position, or the emptiness around it. A level separated by size alone has one carrier.

**Margin.** The empty band between the frame edge and the content area.

**Column and gutter.** A column is one vertical division of the content area; a gutter is the fixed gap between two adjacent columns.

**Span.** How many columns an element occupies, counting the gutters in between. An element spanning four of six columns is four column widths plus three gutters wide.

**Measure.** The width of a line of text, stated in pixels here rather than characters. A long measure makes a line hard to track back from; a short one breaks it into fragments.

**Leading.** The vertical distance from one baseline of type to the next, where a baseline is the invisible line the letters sit on. Leading is an absolute distance, not a multiplier, although it is usually set as one.

**Baseline grid.** A fixed vertical rhythm, stated as one interval, that every leading value in the piece is a whole multiple of. Its purpose is that baselines in different columns land on the same lines.

**Negative space.** Deliberately empty area. **Passive** negative space serves legibility: the air around type and between a block and the frame edge. **Active** negative space serves sequence: a gap large enough to chunk the elements into groups, which is what imposes order without adding an element.

**Tonal value.** How light or dark an element reads when colour is removed, on a scale from white to black. Two elements can differ strongly in colour and share a tonal value, in which case they merge in greyscale and in a blurred render.

**Furniture.** The recurring elements present on every piece in a set regardless of its content: name, handle, slide number, logo.

**Full bleed.** An image or field running to the frame edge with no margin on at least one side.

**Friction.** Deliberate visual roughness, meaning tight leading, collision, overlap, noise or disruption, introduced to arrest the eye.

**Lead room.** The empty space ahead of a subject that is moving or looking in a direction. Space behind such a subject reads as the frame having run out.

**Register.** The overall tone the arrangement projects: quiet, chaotic, luxurious, urgent. A chaotic subject in a minimal arrangement is a register mismatch.

**Irregularity.** One deliberate break from a system the rest of the piece obeys: an element off the grid, an interruption in a pattern, or a stylistic collision.

**Thumbnail.** The piece rendered at its real viewing size, not a zoomed-out view of the artboard.

## The principles

1. **Pick one focal point per frame and say what it is in one sentence.** **(thin)** The mechanism is enforceability: a rank with two items at the top cannot be enforced by any of the carriers below, because every carrier available to promote one of them is also available to the other, so the pair stays tied and the viewer reads a tie as no order at all. A frame can carry a second entry point when it is large enough that the two never compete in one glance, which a feed graphic never is. *Checked by the focal-point test.* Honest exception: a piece whose job is a field rather than a subject, such as a grid of equal members, where ranking the cells would lie about the content. In that case say so explicitly rather than inventing a primary.

2. **Build as many levels as survive the thumbnail, usually three and often two.** **(thin)** The mechanism is that each level must be distinguishable from its neighbours *at viewing size*, and the number of distinguishable steps available is set by the frame's area, not by how many ranks the content has. The arithmetic is in the Applied section: on a square canvas the ladder closes at two levels and on 4:5 it closes at three, computed from the content height and the spacing steps the levels need between them. Content with four ranks in it still gets the number of levels the frame supports, with the surplus ranks merged into the lowest level. *Checked by the level-naming test.*

3. **Give every level two carriers of difference, not one.** The mechanism is redundancy rather than richness. One carrier fails silently under four ordinary transformations: recolouring, printing in one ink, shrinking to thumbnail, and landing on a background you did not choose. Silently is the operative word, since the piece still looks finished, it has simply stopped having a hierarchy. Size plus one non-size property survives all four. Two carriers that break under the *same* transformation count as one, which is why colour plus size is not two carriers for anything appearing in both dark and light mode. The strongest version stacks three on the primary: colour, shape and texture at once, for instance an angular field against a curved subject in a saturated hue on a grainy ground. *Checked by the two-carrier test.*

4. **Write down the final ratio and viewing size before choosing a flow, and let them pick it.** **(thin)** The mechanism is that a reading path is a journey across a specific shape, so the shape decides which journeys are available: a tall narrow frame can carry a long vertical or diagonal journey because it has the distance for one, and a square cannot, because a vertical path in a square covers the same ground as a horizontal one and so reads as neither. The mapping from ratio to flow is looser than it is usually taught; a tall narrow frame can resolve into a diagonal rather than a vertical, and no reliable pairing attaches a radial flow to a square. Treat the ratio as ruling journeys out rather than selecting one. *Checked by the viewing-size test.*

5. **Put most of the piece on the grid and let exactly one element break it.** **(thin)** The mechanism is contrast against compliance: a break reads as deliberate only when the surrounding elements visibly obey a system, so the break's effect is borrowed entirely from the regularity around it. The first break is a focal point. The second removes the evidence that a system exists, at which point both read as inability rather than intent. The budget of one is shared across all three kinds of irregularity, grid break, pattern break and stylistic collision, because a viewer does not sort them into categories, they count anomalies. *Checked by the irregularity count.*

6. **Subtract as a build step, not as a tidy-up, and record what came out.** **(thin)** The mechanism is ordering: subtraction performed before the hierarchy exists removes elements at random, because nothing yet distinguishes a load-bearing element from a decorative one, whereas subtraction performed after the ladder is built has a criterion, which is that anything not carrying a level or the path between levels is removable. Keep removing past the point where it feels finished, since the feeling arrives while the frame is still at the density you are used to. *Checked by the subtraction accounting.*

## How to work

### Mode A: making something

1. Write down the aspect ratio and the final viewing size, in pixels or points, before opening the file.

2. Answer two questions in words: what the message is, and what the piece is for, meaning to inform, to sell, to shock or to be remembered. Each purpose implies a different structure. A selling piece needs a path that terminates at an action, so the last level is the action and the path must reach it. A shocking piece needs one element and no path, because a path gives the eye somewhere to go after the shock and dissipates it. A piece built to be remembered needs one irregularity, since the anomaly is the thing recall attaches to. **The register has to match the message.** A chaotic subject in a minimal clean arrangement reads as a mismatch, and a quiet subject needs no visual journey at all, which makes a sparse arrangement the right answer there rather than a lazy one.

3. Pick the one focal point and write the sentence that names it (1).

4. Build the ladder: two or three named levels, chosen by what the frame supports rather than by what the content has (2).

5. Give each level two carriers that survive this piece's real transformations. List the transformations first, then pick carriers against them (3).

6. Set the grid, closing the arithmetic so margins, columns and gutters sum to the canvas width, then decide *in advance* which single element breaks it (5). Deciding the break in advance is what prevents the second one, because a break chosen while drawing is always chosen on the grounds that it looks good, and so is the next.

7. Place the path with the cheapest available cue, working down the cue list in the path section. Cheapest means adding no element.

8. Subtract, and write down what came out (6).

9. Verify the furniture: every recurring element at the same size and position on every piece in the set, whatever that piece contains. The mechanism is that a viewer reads a constant element as the set's identity, and an element that changes size between pieces is read as a different element. A name set at one size across a large piece and a small piece makes the small piece read as the same brand; a name scaled proportionally to each piece makes it read as two.

10. Run the Tests table in order, then the ultimate test.

### Mode B: judging something that exists

Review in this order and stop at the first failure, because a failure early in the list makes everything after it unanswerable.

1. **Relevance.** Is the piece relevant to something the reader needs? Irrelevance is the first fault, ahead of superficiality and pretension, because a relevant piece badly made can be fixed and an irrelevant piece perfectly made cannot.

2. **Semantics.** Is the biggest element the most important claim, or merely the most available asset? These diverge whenever an image arrived before the message did.

3. **Honesty.** Audit every element that looks like a measured quantity: a small number made to look large, a before and after sized to flatter, a crop missing the inconvenient row, a chart with a truncated axis. Scale is the usual instrument, since two identical sets of figures read as "up" and as "stable" depending only on the vertical scale chosen. **One visible lie discredits everything near it**, so this gate is pass or fail rather than a matter of degree.

4. **Syntax.** Measure margins, gutters, furniture positions and level assignment. The common cause of a layout that does not work is that it is not internally consistent, meaning its own rules are applied in some places and not others, and this is the step that finds it because it is the only step that measures.

5. **Understandability.** Does an unaided reader get it, with no caption, no context and no explanation from the maker?

6. **Mechanics.** Run the Tests table in its order.

7. **Report** what passes, what fails, and the smallest fix for each failure, ordered by impact.

## Grid and negative space

- **The grid assigns hierarchy directly, so use span as a carrier.** An element spanning two columns of six outranks one sitting in a single column, before any difference in size or weight. Subdivide finer than you need, because the subdivisions are what put the small spaces on system too: a three-column layout split into six gives you half-column shifts that still land on a rule.

- **Make every type size a whole multiple of the baseline grid interval.** If every leading value is a whole multiple of one interval, then every baseline in every column lands on a line shared by all the other columns, so cross-column alignment survives a change of type size: alter a heading from three intervals to four and the body text below it moves by exactly one interval and stays aligned with the column beside it. The interval itself is arbitrary and the whole-number relationship is not.

- **Treat negative space as an element with a stated job, either legibility or sequence.** Passive space is not optional. Active space is the only hierarchy tool that costs nothing, because it imposes order without adding an element to rank. Large empty areas also carry an association with minimalism and luxury, which is an association rather than a mechanism **(thin)**, and emptiness deployed for the association alone produces the thin version of the look: empty but not organised, since the gaps were not placed to group anything.

- **Use the rule of thirds as a forcing function against dead centre, not as a law.** **(thin)** A thirds grid divides the frame into three equal parts on each axis, giving two lines and four intersections per axis pair. The usual justification, that the four intersections are where eyes land naturally, is asserted and not derived, and it should be dropped. What survives is purely structural: a thirds grid has no line at the midpoint of either axis, so placing an element on the grid makes dead-centre placement unavailable, and off-centre placement is the thing that creates both lead room and asymmetric weight. So use it as a constraint that rules out centring, and then move the element off the intersection by eye if the frame wants it elsewhere, because the intersection carries no authority of its own. The same reading applies to the golden ratio, roughly 1.618: the number is ordinary mathematics and the design claim attached to it is a starting point to adjust rather than a constraint to satisfy **(thin)**.

- **Apply the level ladder to colour: one dominant, one supporting, one accent.** Keep the structure and drop the percentage split sometimes attached to it, since the split is loose enough that a worked example of it typically misses its own accent share **(thin)**. The accent's job is to mark one thing rather than to occupy a quota.

- **Treat a perception claim as unusable unless you can state its mechanism.** The test is whether the claim predicts something you could observe in this frame, and a statistic about humans in general predicts nothing about it. Claims of the form "a fixed percentage of people are visual learners" or "recognition takes a fixed number of milliseconds" fail it, and belong in neither a deck nor a rationale for a layout.

## Path, balance and friction

Cues for the reading path, cheapest first. Cheapest means fewest added elements, and the order matters because each step down the list adds something that itself has to be composed.

1. **Weight alone. Prefer this.** Once the levels differ by enough, the path exists with no connector, because the eye moves from the heaviest mass to the next heaviest without instruction. It is the only cue that adds no element.
2. **Active negative space**, chunking elements into groups to control the order they are taken in.
3. **Gaze and limb direction**: an eyeline, a pointing hand, a figure's direction of travel. Works because an implied line of sight is followed without the viewer noticing they followed it. Pair it with lead room so the space the subject looks into is empty.
4. **A literal connector**: an arrow, a rule, a band, anything acting as a bridge. Last because it is an element that must then be ranked itself, and it is the cue most likely to end up carrying the hierarchy that the levels should have carried.

- **Use no more than two cue types on one path.** **(thin)** Each cue is itself a visible element or gap, so cues compound into clutter at the same time as they compound into direction, and past two the piece reads as instructed rather than composed. The related failure to watch for is multiple competing paths rather than multiple cues on one path, which reads as chaos directly.

- **Resolve asymmetric weight or the frame reads as falling.** A frame with its mass on one side and nothing answering it reads as mid-collapse, and the resolution is not symmetry. A much smaller element of much higher contrast is usually the right counterweight, because weight here is the product of size and contrast rather than size alone, so a small dark mark answers a large pale field.

- **Use repetition as the binding agent and one break in it as a focal point.** Repeated elements read as a system, and the single interruption in a repeating field becomes the focal point by default, with no promotion needed. Budget that break against principle 5, since it spends the piece's one irregularity. Keep one stylistic family throughout, with members that are cousins rather than siblings: visibly related, not identical. A register collision can be the idea of the piece, but then it is the piece's one deliberate collision and nothing else breaks.

- **Demote a pattern that competes.** **(thin)** A pattern is a ground, and a ground that reads before the subject has taken over the piece. *Test:* name what the pattern is behind. If the answer is the pattern, it has become the subject and must be demoted by reducing its tonal contrast until it reads as a field.

- **Prefer odd groups, because odd groups rank themselves and even groups do not.** An even number of equal subjects creates a tie the eye cannot break, so the group reads as a single field rather than as members. An odd number leaves one unpaired element that becomes the focal point by default. The commonly given reason for preferring odd numbers, that it reduces clutter, does not survive its own examples, which generally place the middle subject dead centre and so are symmetry moves rather than decluttering ones **(thin)**. Three or five members, and five only if the ladder can still tell them apart at viewing size.

- **Treat direction claims as structural, not emotional.** The defensible part is narrow: a diagonal is the only axis not parallel to a frame edge, so it reads as unresolved against the frame, which is what makes it feel active. The emotional vocabulary usually attached to horizontal, vertical and diagonal is asserted with no mechanism **(thin)**. Left-to-right reading order is real but cultural, and a piece whose structure depends on it does not transfer to a right-to-left audience.

- **Put friction only where nothing is being read.** **(thin)** Good friction arrests the eye, bad friction loses the message, so friction is admissible only in zones carrying nothing the reader needs, with clean reading zones maintained beside the rough ones. Tight leading on a decorative slab is texture. Tight leading on the claim is damage. In client work this is close to a prohibition, because almost every zone in a post graphic carries something.

## Anti-patterns

Broad approaches with predictable failure:

- **Starting from the format's existing examples.** This produces category-shaped work by construction, because the starting point contains the category's conventions and the work from there is refinement within them. The repair is a different starting point, usually the message or the subject, rather than more skill applied to the same start.

- **Running a technique catalogue as a generator.** Thirds, the golden triangle, framing and the horizon line are diagnostics: they tell you whether a composition landed on an attention point, and they cannot tell you what it should say. Run as a generator the catalogue produces well-composed pieces with nothing to communicate, and they pass every mechanical test in this file.

- **Clever layout on anything long-lived.** A compositional trick is a dating mechanism, because its legibility depends on the conventions current when it was made, so price it against the piece's lifespan. Ephemeral pieces can carry it; anything reused as a template should not. Do not average the two positions, since a half-clever system dates without earning the attention that would have paid for the dating.

- **Wide permitted variables in anything operated repeatedly.** A system's quality equals its weakest executor, so a template someone else fills needs one grid, a small fixed set of sizes and named archetypes. When every permutation is equally valid, no variant can mean anything, and the operator reuses whichever one is nearest to hand.

Specific failures and their fixes:

- **Flat field, everything at the same weight.** *Fix:* **demote** levels two and three until the gap shows at thumbnail size, rather than promoting the primary. Demoting preserves the density you already have, while promoting runs the primary into the frame edge and forces every other size up behind it.

- **Shouting match, three primaries at maximum contrast.** *Fix:* rank them in words first, then enforce the ranking with position and emptiness rather than size. Size is already spent, since all three are at maximum, so isolation is the only tool remaining.

- **Decorative path, a connector doing the hierarchy's job.** *Fix:* delete the connector and widen the weight gap until the path returns on its own. If it does not return, the fault is level assignment rather than the path, and the connector was concealing it.

- **Broken grid read as no grid.** *Fix:* snap everything on system, verify the arithmetic closes, then release exactly one element.

- **Friction on the message.** *Fix:* move the friction to a zone carrying nothing the reader needs, and restore clean spacing on the claim.

- **Works at build size only.** *Fix:* set type at the size it will be read at and let the artboard be large. The error is reading a 48px element as small because it is small on screen at 100 percent, when at viewing size it is the floor.

- **Balanced but falling**, where mirroring the frame sinks one side. *Fix:* a small high-contrast counterweight rather than a large low-contrast one, which would answer the weight by adding a second mass and produce a tie.

- **Ransom note, mixed stylistic families.** *Fix:* one family, varied within it. If two are genuinely needed, make the collision the piece's one irregularity and remove the others.

- **Furniture that scales with the piece.** *Fix:* fix its absolute size and position across the set.

## Applied to a post visual or carousel

Canvas sizes, the 3x nominal downscale and the 4x stress test come from `reference/canvas-assumptions.md` at the plugin root, so they stay consistent across skills. Verify platform render dimensions against a real post before locking a template, since specifications drift and the canvas file is a reasoned assumption rather than a measurement.

### The shared derivations

**Type floor.** The smallest reliably readable rendered size is about 12pt, which gives two floors rather than one. At the 3x nominal downscale the floor is 12 x 3 = **36px**. At the 4x stress test it is 12 x 4 = **48px**. Both are correct about different things, so a floor figure always travels with its case. This skill works to the **48px stress-case floor** throughout, because a composition decided at build size is the failure it exists to catch, so a piece that passes here also passes the nominal case. Where a number below is called "the floor" it means 48px, and 48px is a pass rather than a near-miss: it is exactly the size that delivers 12pt under the stress case.

**Type scale.** A step must still be visible after division by 3 or it is one level wearing two names. A 1.125 ratio puts 48px next to 54px, which renders as 16pt next to 18pt, two points apart, so it fails. A 1.5 ratio from the floor gives **48, 72, 108, 162**, rendering nominally as 16, 24, 36 and 54pt: gaps of 8, 12 and 18 points, all unambiguous. Round 108 to **120** where a heavier primary is wanted, which keeps it a whole multiple of the baseline interval below.

**Baseline grid: 24px.** Every leading value is a whole multiple of 24. L1 at 120px takes leading 144px, which is 6 x 24, a ratio of 1.2. L2 at 72px takes leading 96px, which is 4 x 24. L3 at 48px takes leading 72px, which is 3 x 24.

**Spacing scale.** Multiples of the baseline interval: **24, 48, 72, 96, 120, 144, 192, 240**. The rule for a gap *between* levels is that it must exceed the leading *inside* the block above it, otherwise the two blocks read as one. L1's internal leading is 144, so the gap after L1 is the next step up, **192**. L2's internal leading is 96, so the gap after L2 is **120**.

**Grid: six columns.** Margin 96px on all four sides, so the content width is 1080 - (2 x 96) = 888px. The 96px margin is a choice made in this file and not a shared constant: `reference/canvas-assumptions.md` fixes the canvas sizes and the downscale factors and fixes nothing about margins, so every number in this section depends on 96 and on the 24px gutter below. `dsn-grid`, which owns grid derivation, starts from a 72px margin and arrives at 936px of content width and 136px columns; both close, and a piece takes one triple or the other rather than mixing them. Six columns with five gutters at 24px: 888 - (5 x 24) = 888 - 120 = 768, and 768 / 6 = **128px per column**. The arithmetic closes: 96 + 768 + 120 + 96 = 1080. Six is the finest grid that still works here, because twelve columns on the same margin and gutter give 888 - (11 x 24) = 624, and 624 / 12 = 52px, which is narrower than the 48px type floor plus any padding, so a single column could not hold a readable unit. Six also divides cleanly into the spans actually used: full width is 6, half is 3, two-thirds is 4, one-third is 2. Four columns cannot give thirds at all.

**Span widths.** A four-column span is (4 x 128) + (3 x 24) = 512 + 72 = **584px**. A three-column span is (3 x 128) + (2 x 24) = 384 + 48 = **432px**. A two-column span is (2 x 128) + 24 = **280px**.

**Why a square takes two levels and 4:5 takes three.** Content height on portrait is 1350 - 192 = 1158px. On square it is 1080 - 192 = 888px. A three-level ladder costs: L1 at 120px over three lines of 144 leading = 432px, plus the 192 gap, plus L2 at 72px on one line of 96 leading = 96px, plus the 120 gap, plus L3 at 48px on one line of 72 leading = 72px. Total **912px**. On portrait that leaves 1158 - 912 = 246px, which is more than one 192 step, so a single deliberate empty region fits. On square the same ladder is 912 against 888, overrunning the frame by 24px before any empty region exists. Drop L3 and its gap and the square ladder costs 432 + 192 + 96 = 720px, leaving 168px, still under one 192 step, so cap L1 at two lines: 288 + 192 + 96 = 576px, leaving **312px** for one empty region. So: **portrait carries three levels with L1 up to three lines; square carries two with L1 capped at two.**

**Contrast thresholds.** 18pt rendered is the boundary above which the lower large-text ratio applies. At the 4x stress that is 18 x 4 = 72px in the working file. So type at **72px or above** needs 3:1 against its background and type **below 72px** needs 4.5:1. L1 at 120px renders 40pt nominal and 30pt under stress, so 3:1. L3 at 48px renders 16pt nominal and 12pt under stress, so 4.5:1. Measuring the ratios and fixing failures belongs to the skill that owns contrast ratios, not here.

### Single-frame post graphic

- **Frame:** 4:5 portrait, 1080 x 1350.

- **Levels: two, not three.** The third level would sit one scale step below L2, and L2 on a single frame is 72px, so L3 would be 72 / 1.5 = 48px, which sits exactly on the stress-case floor with no headroom above it. That is legal but it leaves nothing in hand on a frame whose only real test is the thumbnail, where a single rounding or a font substitution takes it under. So: **L1 is the claim**, one line to three, at 96px to 120px, where 96 is permitted because it is a baseline multiple and still 1.33x above L2 at 72px, which renders as 32pt against 24pt and so stays one distinguishable step. **L2 is the attribution or the single proof element**, 72px, high contrast, bottom anchored.

- **Word count for L1, computed.** For a bold sans-serif the average character advance, meaning the horizontal space one character occupies including its side bearings, is roughly half the type size. At 120px that is 60px per character, so a 584px four-column span holds 584 / 60 = 9.7 characters per line, and at an average English word plus space of about 6 characters that is 1.6 words per line, giving **three to four words over two lines**. At 96px the advance is 48px, so the full 768px content width holds 768 / 48 = 16 characters, or 2.7 words per line, giving **about eight words over three lines**. So the usable band is **four to nine words**, and the way to hit the top of it is to drop to 96px and run full width rather than to add a line at 120px.

- **Carriers:** size plus one **non-colour** property, because the piece appears on both dark and light app backgrounds, which is one transformation that breaks colour. Weight plus size is safe. Colour plus size is one carrier wearing two names here.

- **Grid:** six columns, 96px margin, L1 spanning four of six at 584px, zero or one break.

- **Space:** one empty region of at least 192px adjacent to L1, which the arithmetic above leaves room for. It does more for the hierarchy than any element you could add there. No friction anywhere on a single frame, because there is no zone carrying nothing.

### Carousel (document post)

A carousel is operated repeatedly, so narrow grammar governs. Build the template once, then fill it.

- **Frame:** portrait 4:5 on every slide. Mixed ratios break the page-turn rhythm and read as error rather than as variety, because the frame edge moving between slides is read as the page itself changing.

- **Six named archetypes, assigned rather than freeform.** An archetype is one permitted slide shape: a fixed arrangement a filler picks from rather than designs. The count is a closed set chosen for this skill; what matters is that it is closed, since an open set is the wide-permitted-variables failure. **Cover:** L1 claim large, no body copy, and also the feed thumbnail, so it faces the single-frame test above rather than the carousel one. **Claim:** one idea, one line, maximum space. **Proof:** a number or quote plus its source, the source mandatory and consistently sized. **List:** three to five items, computed below. **Breaker:** the only slide permitted friction, disruption, full bleed or a collision, and it spends the whole carousel's irregularity budget. **Close:** the action plus furniture at standard size. Content fitting none of the six is information about the content, not a reason to invent a seventh.

- **List length, computed.** Content height is 1158px. A slide heading at 72px over two lines of 96 leading is 192px, plus the 120 gap below it, so 312px is spent and 846px remains. A single-line item at 48px with 72px leading is 72px tall, and items are separated by one 72px gap. Five single-line items cost (5 x 72) + (4 x 72) = 360 + 288 = 648px, which fits in 846. Six cost (6 x 72) + (5 x 72) = 432 + 360 = 792px, which also fits, so the cap is not spatial for one-line items and comes instead from the odd-group rule: six equal members tie, five leave an unpaired one. If any item runs to two lines it is 144px tall, and then four items cost (4 x 144) + (3 x 72) = 576 + 216 = 792px and fit, while five cost (5 x 144) + (4 x 72) = 720 + 288 = 1008px and overrun 846. So: **three or five single-line items, four maximum once any item wraps.**

- **Furniture fixed:** name, handle and slide number at identical size and position on every slide. Set them at 48px, the floor, so they are present and never compete, and verify by measuring rather than by eye, since a 48px and a 42px handle look identical at build size and differ by a point and a half rendered.

- **Pacing is literal in a paged document**, where the swipe is the pause: a fast cover, a slow proof slide, a hard stop on the breaker, a release on the close. This is the one place a temporal reading of composition is verifiable, because the reader's progress through the frames is an actual sequence rather than an inferred one.

- **Direction follows the swipe.** Any subject, arrow or eyeline on a non-final slide points forward, and the lead room sits ahead of it. A subject looking backward on slide three tells the reader the sequence has ended.

- **One irregularity per carousel, total:** the breaker. Not one per slide.

- **Run the longest-real-content test on every archetype before the template ships**, because a template is only ever tested with convenient copy during its build, and the archetype that fails is usually Proof, where a five-digit number with a currency symbol and a four-line quote arrive together.

## Tests

Run in this order. Each verdict is decidable from this file alone, with the working file and a phone.

| Test | Catches | Verdict |
|---|---|---|
| **1. Focal point** | Competing primaries | Say the one focal point out loud in one sentence. Fail if it takes two sentences, or if the sentence contains "and" joining two elements. Two candidates is what the viewer experiences as no hierarchy. |
| **2. Level naming at viewing size** | Levels that exist only at build size | Render at the real viewing size and name the first, second and third elements in order. Fail if you cannot name a level you intended, since a level you cannot name does not exist for the viewer either. |
| **3. Two-carrier audit** | Hierarchy resting on one property, or on two that break together | List the properties separating each level from the one below. Fail on fewer than two. Fail also if the two are colour and size and the piece appears on both dark and light grounds, or if both break under the same one of recolour, one-ink print, shrink, or changed background. |
| **4. Viewing size written down** | A composition decided at build size | Ask for the final viewing size in pixels or points, recorded before the file was opened. Fail if it is absent, or if it equals the canvas width. |
| **5. Stress render** | A piece that survives only the nominal downscale | Render at 1/4 of canvas width. Fail if any type falls below 12pt equivalent, meaning below 48px in the working file. |
| **6. Blob count** | A flat field, and groups nobody planned | Blur until type is unreadable and count the distinct masses. Fail if the count exceeds the number of levels you intended. More blobs than levels means elements have merged into groups you did not assign. |
| **7. Greyscale** | Carriers that were colour wearing two names | Convert to greyscale. Fail if two levels now share a tonal value closely enough to merge, since that proves colour was doing the separating alone. |
| **8. Destructive edit** | Elements only assumed to be load-bearing | **(thin)** Degrade the live file on purpose: shrink the primary one scale step, enlarge the smallest level one step, delete the largest empty region, one at a time. Fail for that element if the hierarchy does not visibly worsen, because it was not carrying anything. |
| **9. Flip** | Unresolved asymmetric weight, which familiarity hides in the original orientation | Mirror the frame horizontally. Fail if one side now reads as sinking. It detects imbalance only, not whether the imbalance you have reads as energy or as error. |
| **10. Grid closure** | A grid that was placed by eye | Add margin, columns and gutters. Fail if the sum is not exactly the canvas width, and fail separately if any element sits off the grid other than the one planned break. |
| **11. Irregularity count** | A system that cannot be proved to exist | Count deliberate breaks across grid, pattern and style. Fail above one total. One passes; two reads as absence of a system. |
| **12. Cover the mark** | A composition carrying no identity of its own | Mask the logo and the handle. Fail if nothing in the arrangement, the grid, the type sizes or the spacing would identify the source, since recognition then lived entirely in the mark. |
| **13. Furniture sweep** | Recurring elements drifting across a set | Measure the size and position of every recurring element on every piece. Fail on any variation at all, including one point. |
| **14. Contrast floor** | Type below threshold | For each level, compute rendered size as working size divided by 4. Fail if a level at or above 72px working size is under 3:1 against its background, or a level below 72px is under 4.5:1. |
| **15. Subtraction accounting** | A pass that did not happen | Name what came out between draft and final. Fail on "nothing". |
| **16. Longest real content** | A template only ever seen with convenient copy | Rebuild each archetype with the longest real client name, a nine-word headline, a four-line quote, and a five-digit number with a currency symbol. Fail if any fix required smaller type, since that is a failure of the template rather than of the copy. |

## The ultimate test

**Shrink it to the thumbnail.** **(thin)** Render the piece at a third of its canvas width, which is the nominal case, so a 1080px asset is seen at about 360px, read it on a phone, and place it on a dark ground and on a light ground. This is the softer of the two renders: test 5 below runs the same piece at a quarter width, 270px, which is the stress case, and a piece that reads at 360px and not at 270px has passed here and failed there. Two questions, on both grounds: is the primary still identifiable as primary, and can the type still be read. Fail on either, on either ground. With no render available the cheap proxy is to step back from the screen until the detail is gone.

A fail diagnoses in order. Too many levels for the frame, which is principle 2 and is checked by the height arithmetic in the Applied section. A level resting on one carrier that the shrink destroyed, which is principle 3. Or a piece built at artboard size and hoped for, which is principle 1's failure arriving late, because a frame with two candidate primaries loses both at thumbnail size while looking fine at 100 percent.

This test rests on one account and still carries more weight than any other here for feed work, because it is the only one that reproduces the actual viewing condition rather than modelling it.

## What an agent can run, and what it cannot

**Can run, mechanically:** every test in the table above, plus margin, gutter and furniture sweeps against the stated arithmetic; contrast as a measured ratio; minimum rendered type size at a stated viewing size on both a dark and a light ground; a draft-to-final element diff for the subtraction accounting; a grid-closure sum; a blur-and-count pass; a greyscale conversion; and flagging anything that looks like a measured quantity for human verification.

**Cannot:**

- **Scale as a relationship.** Whether an element is the right size *for this frame* is a human call. The arithmetic gives a ladder that is internally consistent, and it cannot say whether 120px is the right primary for this particular subject.
- **Whether the focal point is the right one.** Enforcing a rank is mechanical once the rank is stated. Choosing which element is rank one is editorial, and it is the decision the whole file depends on.
- **How far to push friction, a break or a collision.** Too little is dull and too much destroys the message, and the boundary is specific to the piece.
- **Whether a subtraction removed the right thing**, as against merely emptying the frame. The accounting test proves something came out, not that it should have.
- **Whether unresolved asymmetry reads as energy or as error.** The flip test detects imbalance and not which of the two you have.
- **Load-bearing versus thin simplicity.** A plain frame letting the claim land is load-bearing. A plain frame because nothing was decided is thin. The two are identical to every mechanical test here, and the right composition will often look unimpressive at build size, which is when to ship it anyway.

## Where this skill should lose

This skill owns the arrangement that enforces a reading order: where each element sits, how large it is relative to its neighbours, and which regions are left empty to make the eye travel. Adjacent ground belongs elsewhere, and the arithmetic above is a working ladder rather than a specification, so close this file when the question is one of these.

**When the question is which element should be rank one, and what the full rank list is.** Use the skill that produces a written rank list and a computed type and spacing ladder, `dsn-hierarchy`. This file assumes the rank is decided and spends its effort on enforcing it in the frame.

Three files touch placement and they divide by the question being asked, so name the question before opening any of them. `dsn-hierarchy` decides which element is first and how much separation each rank needs. This file decides where each element sits and what path the eye takes between them. `dsn-balance` decides whether the resulting arrangement tips and what counterweight it needs. Practical version: if the fix is to make a different element the loud one, you are in the first. If the fix is to move something, you are here. If the fix is to add weight on the opposite side without changing what is loudest, you are in the third.

**When the grid itself is the deliverable: choosing a column count, computing spans, or auditing alignment across a campaign.** Use `dsn-grid`. The six-column derivation here is one worked instance for a 1080px canvas, not a grid method.

**When the question is symmetry versus tension, or a layout that tips.** Use `dsn-balance`. This file gives one rule, resolve asymmetric weight, and one test, the flip; weighing elements against each other and choosing a stability strategy is a larger job than that.

**When the question is how much air, or the spacing scale itself.** Use `dsn-spacing`. The scale above is derived from one baseline interval for one canvas, and grouping by proximity is decided there. Empty space is split between the two files: that one sets how large an empty region is and holds the decision that it carries nothing, and this one decides which region it is and what the emptiness points the eye at.

**When the question is type size, leading, tracking or measure as values to set.** Use `dsn-typeset`. This file uses type sizes as carriers of difference and takes the scale as an input.

**When the question is whether text is readable against its background.** Use `dsn-contrast`. The contrast-floor test here states the thresholds and does not measure them, and nothing in this file sets a ratio.

**When the carousel's order of ideas is the question rather than each slide's arrangement.** Use `dsn-sequence`. The six archetypes above are slide shapes, and which shape goes where, and where the turns fall, is sequencing.

**When the piece is one frame carrying one idea and the question is what to cut.** Use `dsn-poster`. There the composition and the editorial decision are the same decision, and this file separates them.

**When a photograph is the subject, or type has to sit over a picture.** Use `dsn-image`. This file treats an image as a mass with a tonal value and says nothing about choosing or rescuing one. Focal points are split: a photograph has one of its own inside the picture, and choosing and cropping for it happens there, while the frame's focal point, meaning which element the eye lands on first and where in the canvas it sits, is set here.

Outside the scope of any of this: measuring a composition against an outcome, characters-per-line as a readability range, type pairing and optical sizing, right-to-left and non-Latin reading order, motion and timing, chart and data composition beyond the honesty gate in Mode B, and composition at architectural or environmental scale. Everything here is screen and print at page size.

One thing that looks like a gap here is not one. Moving a set of numbers from one canvas to another has an owner: `dsn-grid` and `dsn-spacing` each carry a procedure for deciding whether a borrowed figure transfers to a new format, and `dsn-identity` carries the method of measuring every value in units of something already in the system, which is what keeps a billboard and a 1080 pixel square in character. What genuinely has no owner is automatic reflow between live breakpoints, where the layout is recomputed by a rendering engine rather than by a person.

## Writing the output

Plain words, full sentences. Name the actual element and the actual measurement rather than an abstraction: "the handle is 14pt on slide 3 and 12pt on slide 5" beats "inconsistent furniture." Give the principle first, then offer specific changes as options, because the principle is what lets someone reject your specific change and still fix the piece.

Say which tier a finding comes from. A failed margin sweep or a contrast ratio under threshold is mechanical and not arguable. A note that the focal point is the wrong one is editorial and belongs as a reading rather than as a verdict. Report the passes as well as the failures, since a passed test and a skipped test look identical in a summary that lists only failures.

Where a rule you are leaning on is marked thin in this file, say so at the point you use it, in one clause. Thirds and the golden ratio are the two that come up most. A report that presents every rule at the same confidence has to be re-checked from scratch by whoever receives it.

Sources, corroboration, where the material disagrees, discarded claims and folklore are in `references/provenance.md`.
