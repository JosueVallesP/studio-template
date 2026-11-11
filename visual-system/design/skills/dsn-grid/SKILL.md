---
name: dsn-grid
description: Choosing a grid, computing its margin, columns, gutters and spans, sharing one grid across a carousel, or auditing a layout placed by eye. Gives the grid and its maths.
---

# Grid

This skill decides which grid a piece needs, computes its numbers so the arithmetic closes on the real canvas, and audits a finished draft for alignment. The single idea underneath it is that a grid is not a style, it is a retired decision. Placement gets solved once and then stops being a thing anyone can do inconsistently, including future you and including an agent. That is why a grid earns more on a set of pieces someone will operate repeatedly than on one piece finished today, and why the payoff shows up as cost avoided rather than as beauty added.

## What this skill is for

Use it when someone wants to:

- choose a grid and set its numbers: margin, columns, gutter, rows, spans, all expressed as multiples of a base unit taken from `dsn-spacing`
- build one grid a set of pieces will share, so a campaign or carousel reads as one thing
- audit a draft for alignment and report what is off, with a verdict per check
- turn a layout placed by eye into a system someone can operate repeatedly

## Confidence

The mechanics here are practitioner teaching rather than measured findings, but they are unusually well agreed: most of what follows is taught the same way by several people working independently, and one of those accounts connects back to the discipline's printed literature. That is more agreement than this subject usually gets, so you can lean on the mechanics harder than you would on a single designer's house rules. Rules marked **(thin)** rest on a single source and should be treated as one person's house style; there are few of them, and they cluster in two places, which are the selection procedure and the numbers borrowed from print.

One limit to hold throughout: every pixel figure in the applied section is computed from the canvas rather than inherited, so it is checkable but untested against a real export.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

These are the only terms this skill needs. Everything after this section assumes them.

**Margin.** The outside boundary for *information*, not for ink. Content stops at the margin; an image or a flat field of colour may cross it as a declared exception.

**Column.** One vertical division of the usable width. Columns are not where content goes, they are the units a span is measured in.

**Gutter.** The fixed gap between two adjacent columns or rows. One value, reused.

**Row.** One horizontal division of the usable height, same logic as a column.

**Module.** The rectangle formed where one column crosses one row. In a square grid the module is a square.

**Span.** How many columns wide an element is. A headline at span 4 is four columns plus the three gutters between them.

**Pitch.** Column width plus one gutter. The distance from the left edge of one column to the left edge of the next. Pitch is what makes arithmetic close.

**Measure.** The length of a line of text, counted in characters. Too narrow and the eye zigzags back too often; too wide and it loses its place returning to the left.

**Leading.** The vertical distance from one baseline of type to the next.

**Baseline.** The invisible line the bodies of letters sit on, ignoring descenders.

**Baseline grid.** Evenly spaced horizontal lines on which type sits, so baselines align across columns and across different point sizes. It is a typographic grid, separate from the column grid, and on a post graphic it is close to pointless. Its useful descendant is a single spacing unit. Beware the term in the wild: a stack of rectangular bands subdivided into rows is a band grid or zone grid, not a baseline grid, and it is often mislabelled.

**Spacing unit.** One vertical distance every gap is a whole multiple of. Replaces a baseline grid on short-copy work.

**Geometric centre.** The arithmetic middle of the frame. **Optical centre** is where the eye reads the middle to be, which is slightly above geometric centre, because a block centred by arithmetic reads as sitting low.

**Full bleed.** An image or colour field run to the physical edge of the canvas, crossing the margin on purpose.

**Chrome.** The platform's own interface drawn over or under a posted image: username, caption, action icons. It is not in your file and it eats the bottom of the frame.

**Crop-safe.** Inside the region that survives the platform re-cropping your canvas to a different ratio.

**Kicker** or **eyebrow.** The short line of type above a headline that labels or categorises it.

**Grid types**, named once here so the selection step can be short. A **column grid** divides the width only, giving one consistent measure for flowed text. A **modular grid** divides width and height, giving equal areas nothing is accidentally ranked within. A **hierarchical grid** has deliberately unequal modules, built so one zone dominates. **Axial** places content along one spine, **diagonal** tilts that spine, **radial** arranges it around a centre; all three raise contrast and lead the eye unconventionally, and standard layout software will not generate them, so you build them by hand.

## The principles

Each names the test that checks it. The tests are in the table below.

1. **Task before type.** The grid follows from what the reader has to do with the content, never from a list of grid types. **(thin)** This is the move most grid teaching skips, and skipping it is the failure mode of the whole subject: a designer who can name six grids and holds no selection rule picks the interesting one. Test: write down who views this, where they encounter it, and what they must understand or do. If you cannot answer, the brief is missing, not the grid. Checked by the brief-answerable test.

2. **Columns from spans, not spans from columns.** Ask what the widest and the narrowest things in the content need, then pick a count that produces both. **(thin)** If you set the count first and then fitted content to it, you did it backwards, and every span after that is arbitrary. Prefer a count with many factors, because factors are how one structure yields several divisions: 6 gives halves, thirds and a 4 plus 2 asymmetry, which is most of what a layout asks for. It does not give quarters, since 6 does not divide by 4. Checked by the span-naming test and the column-width-versus-display-type test.

3. **Margins bound information, not ink, and a break must be legible as a decision.** Only an image, a field of colour, or one declared exception may cross the margin. One break reads as intent. Two read as no grid, because a reader cannot tell a system with two exceptions from an absence of system. Checked by the edge-on-line test.

4. **Spans are assigned, not available.** **(thin)** Every span in use names a role: headline, kicker, body, attribution. Write the assignment down. A 6 by 6 grid offers hundreds of valid span and position combinations, and that is not freedom, it is a decision you will make badly at speed. The precedent is an identity system that generated tens of thousands of valid permutations and failed in use, because when every permutation is equally valid none of them can *mean* anything, so no variant can be assigned to anything. Unassigned flexibility also moves the work from design to approval, since somebody still has to decide which variant goes on which thing. Checked by the span-assignment test.

5. **Change the span, not the type size.** When content does not fit, move it to a wider span. Shrinking type or moving the margin to make copy fit destroys the one thing the grid was for, which is that these numbers hold across pieces. If no wider span exists, cut copy. Checked by the content-fits test.

6. **One spacing unit, and a clear step between within-group and between-group gaps.** Set one vertical unit and make every vertical distance a whole multiple of it. Then make the gap between two groups at least four times the gap inside a group **(thin)**, so grouping is legible before anything is read. Checked by the gutter-and-unit sweep and the squint-grouping test.

7. **Invention belongs in what you place, not in the structure you place it on.** A novel grid dates a piece faster than anything on it and fails the teachability test, because nobody else can operate it. Checked by nothing mechanical; it is a constraint on what you attempt.

8. **A shared grid is what makes a set a set.** Two pieces with different images and different titles read as one series when the structure underneath is identical and only the spans vary. Checked by the guides-overlay test.

9. **Audit syntax before beauty.** Run the mechanical checks before forming any opinion about whether the piece looks good. Most layout review runs that order in reverse, and the reason it is wrong is that a layout which does not work is usually not internally consistent, and internal consistency is exactly what is countable. For a grid, syntax is the whole test. Checked by running Mode B in its given order.

## Tests

Each returns a verdict decidable from this file alone. Numbers below are for the applied canvases; substitute your own where a test names one.

| Test | Catches | Verdict |
|---|---|---|
| **1. Brief-answerable** | A grid chosen before the task was known | Read the three written answers: who views this, where, what they must understand or do. Fail if any is missing, blank or a restatement of the format. Fail means the brief is incomplete, not that the grid is wrong |
| **2. Span naming** | A column count picked before the content was looked at | Read the written list of roles and the span each needs. Fail if the list was produced after the count was set, or if any role has no span |
| **3. Span assignment** | Spans no role was ever given | Pass if every span appearing in the file is in the written assignment table. Fail naming the element that is not, which is drift |
| **4. Content fits** | A grid that works only at the copy length you drafted | Add six words to the headline and re-render. Pass if existing spans absorbed it. Fail if the fix was shrinking type, changing leading, or moving the margin |
| **5. Column width versus display type** | Too many columns for the canvas, so every span is arbitrary | Compute one column width. Estimate a word of display type at the intended size as five characters at half the type size each, so 48px type gives 120px. Fail if the column is narrower than that, and halve the count |
| **6. Minimum rendered size** | Type that is legible in the working file and gone in the feed | Divide the smallest type size in the file by the downscale factor. Fail below 12pt. On a 1080 canvas that is a floor of 36px at the 3x nominal case and 48px at the 4x stress case, so state which case the piece is held to before reading a verdict. Fail separately if no case was stated |
| **7. Crop safety** | Load-bearing content a centre crop or platform chrome eats | Mark the crop-safe band on the frame, then check at thumbnail scale with guides off. Pass if the headline and the call to action both sit inside it. **(thin)** |
| **8. Distinct-edge count** | A grid abandoned halfway down the piece | Count distinct left edges on one frame, do not eyeball them. Fail above three |
| **9. Edge on line** | Elements placed by eye among elements placed on the grid | Check every element edge. Fail on any edge that is neither on a grid line nor a declared written exception. Fail separately at two or more exceptions, which reads as no grid |
| **10. Gutter and unit sweep** | Gaps that are nearly right | Measure every horizontal gap and every vertical gap. Fail on any horizontal gap that is not the gutter or a stated multiple of it, and any vertical gap that does not divide by the spacing unit |
| **11. Squint grouping** | Spacing not carrying the structure | Squint, or blur the render, until type is unreadable. Count the groups that stay separate. Fail if two groups you inventoried merge into one, and widen the between-group gap |
| **12. Longest real content** | A template seen only with placeholder copy | Re-render with the longest real client name, real headline and real quote you have. Fail on any overflow, reflow onto an unplanned line count, or element that moved off its line |
| **13. Guides overlay** | A set that is a set only by styling | Overlay the guide definitions from every piece in the set. Pass only if they are identical and only spans differ |
| **14. Arithmetic closes** | A grid whose numbers do not add up to the canvas | Sum margin, columns and gutters on each axis. Fail on any axis where the total is not exactly the canvas dimension, and on any non-integer column width or row height |

## How to work

### Mode A: building a grid

Steps 1 to 5 are the spine. They run off what the reader has to do with the content and end with a column count derived from the spans the content actually needs. Everything after step 5 is construction. Do not reorder the spine, and in particular do not start at the grid-type table, which is a consequence of step 2 rather than a menu.

1. **Inventory the content as groups, not as elements.** Two headline groups, one portrait, a block of supporting information, a footer with a title and a call to action. The group count is what drives the column count, and elements counted individually give you the wrong number. Do this before you draw a single guide. It is free and it changes the answer.

2. **Answer three questions in writing.** Who views this. Where do they encounter it. What must they understand or do because of it. These three answers, and nothing else, select the structure in step 3. Written down, not held in mind: the point of writing them is that step 3 has to be checkable against them later. Checked by test 1.

3. **Read the structure off the reader's task.**

   | Reader has to | Structure | Why this one |
   |---|---|---|
   | Compare or scan parallel items | Modular | Equal areas, one item per module, nothing accidentally ranked |
   | Read continuous text at length | Column | One consistent measure across flowed type |
   | Notice one thing, then act | Hierarchical | Built for a single focal point; modules deliberately unequal |
   | Be made to look around, where the job is tone rather than transfer | Axial, diagonal or radial | High contrast, leads the eye unconventionally |
   | Get one line or one number and leave | No grid | Margins and optical centring only |

   The last row has a real floor: below roughly three information groups a grid adds overhead and imposes no constraint, because there is nothing for it to hold in relation to anything else **(thin)**. A grid is not always necessary, and that is settled by format and content volume rather than by principle.

   **The escape hatch.** If the task analysis returns "the reader's task is to feel something", that is a legitimate answer, and the idea picks the structure instead of the task. That is the route that produces axial, diagonal and radial grids, which no amount of task analysis will ever select. What is not legitimate is skipping the analysis because you already like a grid. The test for which you did is test 1: an escape hatch declared in writing is a decision, an empty brief is an evasion.

4. **Name the span each role needs, in words, before any number exists.** The widest thing in the content and the narrowest thing in the content, and for each role in the inventory, roughly how much of the width it has to occupy. "The headline wants the full width, the kicker about two thirds, the body a bit over half, the attribution a narrow strip." Checked by test 2.

5. **Set the column count to the smallest count that produces every span on that list, then take the largest such count that still passes test 5.** Compute candidate column widths with the formula below, reject any count that gives a non-integer width or a column narrower than a word of display type, and among what survives prefer a count with many factors, because factors are extra divisions for free. Worked arithmetic for the two standard canvases is in the applied section.

   ```
   column width = (canvas - 2 x margin - (n - 1) x gutter) / n
   pitch        = column width + gutter
   span of n    = n x column width + (n - 1) x gutter
   ```

6. **Set the margin, which is the outside boundary for information.** On an unbound surface derive it from format and viewing conditions rather than from print ratios, and make it a whole multiple of the spacing unit so element edges land on the unit at the frame edge as well as inside it. Which print ratios survive the move to screen, and which do not, is in the section on numbers below.

7. **Set the gutter from how separate adjacent things must read**, then hold it. The gutter is one number reused, not a value tuned per pair of elements, because a gutter tuned per pair is just placement by eye with extra steps.

8. **Assign spans to roles in writing, in the order of what must be understood first.** The widest element is not automatically seen first, so priority and width are two decisions and the table records both. For a card or panel, settle where the panel sits on the grid before you decide how its contents sit inside it; doing it the other way produces a panel that fits its contents and nothing else. Checked by test 3.

9. **Set one vertical spacing unit** and make every vertical distance a whole multiple of it, with at least a four times step between within-group and between-group gaps **(thin)**. A unit of 24 gives related distances of 24, 48, 72 and 96, and the four times step is what makes the squint test pass.

10. **Sketch at the exact finished ratio, on paper, before software.** **(thin)** For 16:9, draw 16 squares by 9 on gridded paper; for 4:5, 4 by 5. A layout that is good at the wrong ratio collapses on the real canvas, because every span relationship changes when the frame does. Pencil, several options, five minutes. This is the step that makes the rest fast.

11. **Lay out, then stress the content.** Widen spans, adjust line breaks, re-crop the image. The rule while doing it: outside margin fixed, internal arrangement adapts. Run tests 4 and 12 here, not later.

12. **Finish with Mode B,** then show it to someone unfamiliar and ask what they noticed first. The answer is informative mainly when it names something you had treated as secondary.

### Mode B: auditing a draft

Run these in order, mechanically, before forming any opinion about whether the piece looks good.

1. **Distinct-edge count** (test 8). Count them; do not eyeball them.
2. **Edge-on-line check** (test 9). More than one exception, see principle 3.
3. **Gutter and unit sweep** (test 10), then **span assignment** (test 3).
4. **Squint grouping** (test 11). Blur or squint until type is unreadable and count the groups that stay separate.
5. **Content fits** (test 4), then **longest real content** (test 12).
6. **Minimum rendered size** (test 6) and **crop safety** (test 7), guides off, at intended size, with the graphic also viewed at roughly 25 percent to simulate a thumbnail. Is the message clear, can they find the action, is the character right.
7. **Arithmetic closes** (test 14), if you have the grid definition and not only the render.
8. **Report** passes, fails, and the smallest fix for each, ordered by impact.

## Deciding whether a number transfers to this format

Importing a print ratio without its reason is the standard way to be confidently wrong. Every number in the discipline is one of three things, and the decision you make at the point of use is which: a **derived** number has a reason you can restate, so it transfers wherever the reason holds and nowhere else; a **convention** has no reason attached, so it transfers only as a default to test; a **teaching example** is a demonstration fitted to one format and transfers nowhere.

The rule: before reusing any number, say the reason out loud. If you cannot, it is a convention, label it as one, and the person you hand the work to can override it without thinking they broke a rule.

| Number | Status and the reason, where there is one |
|---|---|
| Measure set by reading comfort | **Derived.** Legibility. Too narrow and the eye zigzags back too often, too wide and it loses its place returning. Transfers to any flowed text |
| Leading grows as type size grows | **Derived.** Legibility. Transfers |
| Column count with many factors | **Derived.** More divisions from one structure. Transfers |
| Gutter sized for separation | **Derived.** Proximity grouping: things closer together read as belonging together. Transfers |
| Bottom margin slightly larger than geometrically equal | **Derived.** Optical centre sits above geometric centre, so a block centred by arithmetic reads low. Transfers to any held or viewed surface |
| Inner margin larger than outer | **Derived, bound work only.** The reason is the binding swallowing inner space. No binding, no reason, no transfer |
| Generous lower and outer margins | **Derived, held work only.** The reason is thumbs covering what you are reading |
| Bottom margin twice the top, inner 1.5 times the top | **Convention. (thin)** Inherited ratios, disclaimed even where they are taught. The perceptual effect behind them is real; the specific multiples are not derived |
| 12 columns | **Convention. (thin)** A web default. The factor argument justifies *a composite number*, not twelve, and twelve is only workable where a twelfth of the canvas still holds a word, which is a wide landscape frame or a desktop viewport |
| A 10 pixel or 8 pixel base unit | **Convention. (thin)** One is a default in design software, the other is interface practice. Nobody derives either, and the 8 unit's usual justification is whole-pixel rendering, which a non-integer downscale voids |
| 8, 20 and 32 field grids | **Teaching examples. (thin)** Demonstrations fitted to A4, not universal counts |
| A 65 to 75 character measure | **Convention from print.** Derived for a page held at reading distance. It does not survive a feed, for the arithmetic reason computed in the applied section |
| Three distinct left edges as a ceiling | **Convention, set here. (thin)** A working threshold for test 8, not a measured limit |

**Dead on screen entirely,** so do not carry them across at all: bleed allowance, page numbers, binding allowance, proofing at 1:1 for a printer, and flowing body text from one column into the next.

One terminology warning, because it is the reason to check a term before repeating it. "Baseline grid" is used in the wild for two different things: evenly spaced horizontal lines on which type sits, which is the correct meaning given in the terms above, and a stack of rectangular bands subdivided into rows, which is a band or zone grid. The second usage describes something real and useful under the wrong name. Check every term and every figure against a second source before you build on it.

## Anti-patterns

Broad approaches that are not always wrong but should be named when they appear:

- **Grid types picked off a list.** Six grids named, the interesting one chosen. Fix: the three questions, then the task table, then the spans.
- **Grid before content.** Guides drawn in the empty document, content imported after. This one is a genuine disagreement rather than a mistake: drawing the grid first optimises for getting unstuck, because a grid already on the canvas is something to react to. The decision rule is that inventory and the three questions always come first, since they cost nothing and they change the column count, and drawing the grid first only works when you already know what the content is.
- **Flexibility as a virtue.** Every permutation equally valid, which moves the work from design to approval. Fix: the assignment table.
Specific failures:

- **Grid as ornament.** Lines visible, content not aligned to them. Fix: place against a hidden grid, then decide separately whether a visible rule earns its place as a drawn element.
- **Default centring.** Equal margins all round plus everything centred reads as a software default. Fix: commit to symmetry as the idea, or set a deliberate asymmetry with a stated reason.
- **Two accidental grids.** Leftover guides sitting beside the real ones, so half the elements align to each. Fix: delete the old ones before placing anything. An overlaid type grid and image grid are allowed, but only as a stated decision.
- **An image that does not fit its module.** Fix in this order: re-crop to the module; rule or box it so the mismatch becomes a frame; lay a flat colour block over part of it for optical stability. **(thin)**
- **Static regular placement.** Equal items in equal modules, three and three, reads inert. Fix: break one symmetry decisively and compensate elsewhere, three one side and two the other with a bleeding image redistributing the weight, rather than softening several symmetries slightly. **(thin)**
- **Gutters tuned per pair.** Each gap nudged until it looks right. That is placement by eye wearing a grid's clothes, and test 10 catches it.

One permitted move that looks like a violation: a single extra guide inside one column, for instance a centre line used to rebalance one paragraph **(thin)**. It is legitimate when written down as the one declared exception, and it is drift when it is not.

## Applied to a post visual or carousel

Canvas sizes, the 3x nominal downscale and the 4x stress test come from the plugin's shared canvas assumptions. Everything else below is computed here, from those canvas sizes and the tests above. Nothing in this section is inherited from print, and none of it has been checked against a real export, so treat every figure as a working default and run tests 4, 6, 7 and 12 against a real post before standardising on it.

**The measure constraint inverts.** A page limits you by maximum comfortable line length. A phone limits you by minimum legible type size, because a 1080px-wide canvas is displayed in a feed column of roughly 360 device-independent pixels, a 3x downscale. Work the print measure through that: at the smallest type you can rely on, 12pt rendered, an average character is about half the type size, so 6pt wide, and 65 characters is about 390pt of line. The feed column is 360pt. The print measure does not merely read badly, it does not fit the frame at all. In working-file pixels the same computation is 36px type, roughly 18px per character, 65 characters is 1170px, against a usable width of 936px. So: one column of text on a post graphic, two at most, and the line length is whatever the span gives you rather than a number you target.

**Cropping replaces margins as the real constraint.** A 4:5 frame is centre-cropped to square on some surfaces, a square is cropped on others, and the bottom of the frame sits under caption and username chrome. This is the constraint that actually breaks post graphics, and the crop-safe rows are computed below from frame geometry rather than measured.

### Deriving the square, 1080 x 1080

Fix the spacing unit at 24 first, because the margin and the gutter both have to be multiples of it. At 3x, 24px renders as 8pt and the between-group gap of 96px renders as 32pt, which are plainly different distances; at the 4x stress scale they are 6pt and 24pt, still plainly different. The unit survives both.

Set the gutter to the unit, 24. Now test candidate margins against test 14, which requires an integer column width:

```
margin 64:  usable 1080 - 128 = 952;  952 - (5 x 24) = 832;  832 / 6 = 138.67   non-integer, reject
margin 72:  usable 1080 - 144 = 936;  936 - (5 x 24) = 816;  816 / 6 = 136      integer, accept
margin 96:  usable 1080 - 192 = 888;  888 - (5 x 24) = 768;  768 / 6 = 128      integer, accept
```

Take 72, which is 3 x 24 and one fifteenth of the canvas, because 96 spends a further 48px of usable width per side without buying anything.

The margin is a choice made here and not a constant inherited from `reference/canvas-assumptions.md`, which fixes the canvas sizes and the downscale factors and deliberately fixes nothing about margins. So 96 above is rejected rather than illegal, and a skill that starts from a different margin for a different reason closes on a different column width: 96 with a 24 gutter gives 128px columns, and 90 with a 36 gutter gives 120px. All three close. This file's numbers are 72, 24 and 136, and anything consuming the grid from here takes that triple whole rather than mixing it with another.

Now derive the column count rather than choosing it. Test 5 needs a word of display type: five characters at half the type size, and display type on a post graphic is around 48px, so 120px. Usable width 936, gutter 24:

```
n = 4:   (936 - 72)  / 4  = 216     integer, 216 > 120   passes
n = 5:   (936 - 96)  / 5  = 168     integer, 168 > 120   passes
n = 6:   (936 - 120) / 6  = 136     integer, 136 > 120   passes
n = 7:   (936 - 144) / 7  = 113.1   non-integer, and below 120   fails twice
n = 8:   (936 - 168) / 8  = 96      integer, 96 < 120    fails test 5
n = 12:  (936 - 264) / 12 = 56      integer, 56 < 120    fails test 5 badly
```

Six is the largest count that passes, and among 4, 5 and 6 it is the one with the most factors: 6 gives halves, thirds and a 4 plus 2 asymmetry, where 5 is prime and gives none of them and 4 gives halves but no thirds. So six is derived, not preferred. Twelve on this canvas gives 56px columns, which holds about two characters of display type, which is why copying a web convention onto a square makes every span arbitrary.

Rows: make the module square by setting the row pitch equal to the column pitch, 136 + 24 = 160. Then usable height 936 = 160n - 24, so n = 6.

```
margin        72 all four sides      (3 x unit; one fifteenth of 1080)
usable        936 x 936
columns       6, gutter 24           column width 136
rows          6, gutter 24           row height 136
pitch         160, both axes
module        136 x 136, square
spacing unit  24                     (within group 24, between groups 96)
```

Arithmetic closes on both axes: 72 + (6 x 136) + (5 x 24) + 72 = 72 + 816 + 120 + 72 = 1080.

Line and module positions, so an audit has something to measure against. Column or row k starts at 72 + (k - 1) x 160 and is 136 wide:

```
1:  72 to 208     2:  232 to 368    3:  392 to 528
4:  552 to 688    5:  712 to 848    6:  872 to 1008      (1008 + 72 = 1080)
```

Span widths, from the formula, 160n - 24:

```
span 1: 136    span 2: 296    span 3: 456
span 4: 616    span 5: 776    span 6: 936
```

### Deriving the 4:5, 1080 x 1350

Hold the horizontal grammar identical to the square, so a set reads as a set: margin 72 left and right, 6 columns, gutter 24, column width 136, pitch 160. Only the vertical changes.

Keep the pitch at 160 so modules stay square, and keep the top margin at 72. Then the row count is forced by what fits:

```
7 rows: (7 x 136) + (6 x 24) = 952 + 144 = 1096;  1350 - 72 - 1096 = 182 left at the bottom
8 rows: (8 x 136) + (7 x 24) = 1088 + 168 = 1256; 1350 - 72 - 1256 = 22  left, not a margin
```

So seven rows, with a bottom margin of 182.

```
margin        72 left, right and top; 182 bottom
columns       6, gutter 24           column width 136   (identical to the square)
rows          7, gutter 24           row height 136
pitch         160, both axes
spacing unit  24
```

Arithmetic closes: 72 + (7 x 136) + (6 x 24) + 182 = 72 + 952 + 144 + 182 = 1350.

Row positions: rows 1 to 6 are at the same coordinates as the square's rows, and row 7 runs 1032 to 1168, with 1168 + 182 = 1350.

Two things about that 182. It is about 2.53 times the top margin, which looks exactly like an inherited print ratio and is not: it is the remainder after seven square modules, and the print convention it resembles is bottom double the top, a different number for a different reason. Say which you are using. And 182 is not a multiple of the spacing unit, 182 / 24 = 7.58, which is acceptable only because nothing is placed against the bottom edge; if something has to be, move it up to the nearest unit multiple, 168 from the bottom, and leave the slack outside it.

**Crop-safe rows, computed.** A centred square crop of 1080 x 1350 removes 270px of height, 135 from the top and 135 from the bottom, leaving the band from y = 135 to y = 1215. Row 1 runs 72 to 208, so its top 63px is cut. Row 7 ends at 1168, inside 1215, so it survives the crop. Then chrome: assume the platform draws caption and username over roughly the bottom 180px, covering y above 1170. Row 7 ends at 1168, clearing that by 2px, which is no margin at all, so treat row 7 as lost. Rows 2 to 6 survive both the crop and the chrome. Put the headline in rows 2 to 5, one row more conservative than the computation allows, and put the call to action no lower than row 6. Both the 180px chrome band and the centred crop are assumptions about platform behaviour, so verify with one real post before you rely on them. **(thin)**

### Span assignment, both formats

This table is the generator. Everything placed on either canvas comes from a row in it, and test 3 fails on anything that does not.

| Role | Span | Width | Characters per line at the type size used |
|---|---|---|---|
| Hook or headline | 6, or 4 when an image shares the row | 936, or 616 | 39 at 48px type; 25 at 616 |
| Kicker or eyebrow | 4 | 616 | 34 at 36px type, usually one line |
| Body or explanation | 4 | 616 | 34 at 36px type |
| Attribution or handle | 3 | 456 | 25 at 36px type |
| Full-bleed image | crosses the margin | 1080 | the only element permitted to cross |

Character counts use the same estimate as test 5, half the type size per character: 936 / 24 = 39 at 48px type, 616 / 18 = 34 at 36px, 456 / 18 = 25. These are the measures the grid produces, and they are the numbers to check copy length against rather than a print figure. **The 36px rows in the table are the nominal case.** They render at 12pt at 3x and 9pt at 4x, so a piece held to the stress case raises those three rows to 48px, which recomputes their character counts as 616 / 24 = 25 for the kicker and the body and 456 / 24 = 19 for the attribution. Those are the two legal versions of the table and the rest of the grid is unchanged either way, since the spans and the widths come from the margin and the gutter rather than from the type size.

Type size floor, from test 6: 12pt rendered at the 3x nominal downscale is 36px in the file, and at the 4x stress scale 48px. Both are the same 12pt rendered; they differ only in which viewing case they survive. Use 36px and accept that it is at the edge, or 48px and be safe at both, and write down which one the piece was built to.

### Carousel

- **One grid across every slide, spans varying by slide.** A shared grid is precisely the answer to the carousel problem, which is that ten slides have to read as one object while saying ten different things.
- **Slide 1 hierarchical, middle slides modular.** Slide one is a poster and needs a single focal point, so take the 6 by 6 base and give one zone a deliberately oversized span, for instance a headline at span 6 occupying rows 2 to 4 with nothing competing. The last slide repeats slide one's spans so the set closes.
- **One permitted break, the same on every slide.** A full-bleed image crossing the margin is the usual choice. The same break on every slide reads as grammar; a different break per slide reads as no grid, by principle 3.
- **Sketch all slides at 4:5 on one sheet first,** ten small 4 by 5 boxes on gridded paper. This is the only way to see rhythm across the sequence, which is where the heavier and lighter slides fall in order. Decide that before any slide exists.
- **Run test 4 on the longest slide, not the first.** The first slide is the one you drafted to fit.

## Checklist

Decision
- [ ] Content inventoried as groups, and the three questions answered in writing, before any guide was drawn
- [ ] Structure read off the reader's task, or "the task is to feel something" declared explicitly
- [ ] Span each role needs named in words before any count was set

Numbers
- [ ] Arithmetic closes on both axes, and no column width or row height is fractional
- [ ] Column count derived against the display-type check, not chosen
- [ ] Every imported ratio either re-derived for this format or labelled a convention
- [ ] One spacing unit, with a four times step or more between within-group and between-group gaps
- [ ] Smallest type size clears the floor at the stress downscale

File
- [ ] Every test above run and its verdict recorded, passes included
- [ ] At most one break, declared in writing, and only an image or colour field crosses the margin
- [ ] One grid shared across the set, with only spans varying
- [ ] Headline and call to action inside the crop-safe band

## The ultimate test

Test 4 with the image swapped as well as the copy lengthened. If the layout absorbs both by changing spans alone, the grid is real and will carry the next twenty pieces. If either one required moving a margin or resizing type, you do not have a grid, you have an arrangement that happened to work once.

## What an agent can run, and what it cannot

**Can run:** every test in the table above; the column, pitch and span formulas for any canvas, margin, count and gutter, including the candidate sweep in the applied section, emitting guide definitions; the gutter and unit sweep; minimum rendered type size against a stated downscale; the crop-safe band from frame geometry; and the check that one grid and one break type hold across a carousel.

**Cannot run:** deciding what the reader has to do, which selects the structure and is what everything downstream rests on; selecting an axial, diagonal or radial grid, because that decision is that the piece's job is tone rather than transfer and no content inventory reveals it; judging whether a break reads as intent or as error, since counting breaks cannot say whether the one you kept is apt; scale, which is a relationship rather than a dimension and so cannot be briefed numerically; the residue between two or three valid span choices, where someone has to just decide; and whether an asymmetry has a reason, since only the person who set it knows.

Say so when reporting: nothing here covers responsive or fluid grids, CSS or auto-layout implementation, accessibility, non-Latin or right-to-left setting, grids for charts and tables, or motion.

## Where this skill should lose

**When the question is how far apart two things should sit.** Use `dsn-spacing`, which owns the spacing ladder, the base unit the ladder is built from, and the rule that a gap inside a group is smaller than the gap around it. The split is what the space is measured from. This file owns space measured from the canvas: the page margin, how many columns there are, the gutter between them, and which columns an element spans. That file owns space measured from the content: the gap between two elements, the padding inside one, and the size of a region left carrying nothing. Concretely, deciding that the margin is 72 and that the headline spans columns 1 to 4 is this file. Deciding that the gap under the eyebrow is 32 and the gap under the headline is 64 is that one. Where the two disagree, each wins on its own side: a margin, gutter or column width computed here is not overridden by a ladder value, because every element on the page was placed against these figures, and a gap between two content groups is not overridden by a grid figure, because a column grid does not set it. Take the base unit from that file rather than picking one here, and express this file's margin and gutter as multiples of it. One exception outranks both: a platform's crop-safe box or safe zone is a hard constraint, it is specified in that file, and it wins over this file's margin when they conflict.

**When the question is which element should be seen first.** Use `dsn-hierarchy`. This skill will tell you a headline is at span 6 and will not tell you whether it wins the first look, and principle 4's warning that the widest element is not automatically seen first is the boundary between the two.

**When the question is type size, leading or measure as values.** Use `dsn-typeset`. This skill derives the character counts a span produces and stops there; choosing the size and the leading that fill it is not its job.

**When there is one frame, no set, and no repeat.** Use `dsn-composition`, which owns placement and weight in a single frame. A grid's payoff is the second piece and the twentieth, so on a one-off it is overhead, and the "no grid" row of the task table exists for exactly that case.

**When the layout is on the grid and still feels wrong.** Use `dsn-balance`, which owns optical weight. A piece can pass every test in this file and still sit heavy on one side, because alignment and weight are different problems and nothing here measures weight.

**When the question is the shape of a sequence rather than the structure in it.** Use `dsn-sequence` for how a carousel's slides should be ordered and paced. This skill gives all ten slides one grid and says nothing about what each slide should do.

**When the numbers have to become a reusable set someone else can apply.** Use `dsn-tokens`. This file computes a grid for one format; turning margin, gutter, pitch and spans into named values that hold across a whole output is a separate job.

**When another file has already computed a grid and you want to know whether to keep it.** Several files quote one worked grid to make their own arithmetic concrete: a four column grid for a single frame, a six column grid under a photograph, a keyline grid for an icon, a construction grid for a mark. None of those is a grid method, and the last two are not page grids at all. If a project needs a grid that more than one piece will share, derive it here and let the quoted instances take their ratios from it. Where a figure in this file and a figure quoted in one of those disagrees, this file wins on the grid itself: margin, column count, gutter and span.

## Writing the output

Name the actual element and the actual measurement, never an abstraction: "the attribution sits 18 pixels below the row 6 line" beats "alignment issues in the lower zone". Give the principle first and the change as an option, since the right move depends on the piece. Say which tests you ran and what each returned, including the passes, because a pass on test 7 and a missing test 7 look identical in a summary that lists only failures. Show the arithmetic for any number you recommend, so the person can follow it to the same answer or disagree with a step. And when a number is a convention rather than a derivation, label it at the point of use, so it can be overridden without anyone thinking they broke a rule.

Sources, corroboration, where the accounts disagree, and what none of them reach are in `references/provenance.md`.
