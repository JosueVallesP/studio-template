# dsn-grid: independent audit

Checked against the five transcripts in `~/research/design-plugin/transcripts/`
(`grid__BQEVqWiD304`, `grid__MNMTjffhRcU`, `grid__QcT9a8gcG74`,
`grid__oPrDgIuxdYQ`, `grid__wIabVp0Hh8U`) and against
`reference/canvas-assumptions.md`. The provenance file was read for context only
and was not treated as evidence, since it was written by the same agent that
wrote the skill.

Counts: 9 mislabelled, 5 broken or misplaced citations, 10 unsupported,
7 derived and unlabelled, 4 arithmetic errors. Fixes applied where the brief
allowed. Nothing was restructured or deleted.

## Arithmetic errors

**A1. "twelve on 1080 gives 68 pixel columns" is wrong by 12 pixels per column.**
Inside the margins this section itself sets (72 each side, gutter 24) the figure
is 56: (1080 - 144 - 11 x 24) / 12 = 672 / 12 = 56. The value 68 is what you get
if you drop the margins entirely, (1080 - 264) / 12, which contradicts the grid
stated three lines above. **Fixed to 56 with the working shown.** The argument
(six, not twelve) survives and is strengthened, since 56 is further below a word
of display type than 68.

**A2. Six columns cannot give quarters.** Principle 2 reads "6 gives halves,
thirds and quarters from one structure". Six does not divide by four. The source
says "Six columns gives us halves, thirds, and smaller divisions within one
structure" [QcT9a8gcG74 00:02:02]. The applied section gets this right ("halves,
thirds and a 4+2 asymmetric split"), so the skill contradicts itself.
**Fixed to the source's wording.**

**A3. "The 182 bottom margin is 2.5x the top" is 2.53x.** 182 / 72 = 2.528;
2.5x of 72 is 180. **Fixed to "about 2.53x" with the division shown.** See M7 for
the larger problem with the sentence around it.

**A4. "Keep the headline inside rows 2 to 5 so it survives a centre crop" is
stricter than the stated reason.** On this grid (margin 72 top, row pitch 160)
row 7 ends at y=1168 and a centred square crop of a 1080x1350 frame keeps
y=135 to y=1215, so rows 2 to 7 all survive. Only row 1 is cut. The restriction
to rows 2 to 5 is a conservative default with no arithmetic behind it.
**Noted inline; the number was left alone because the section already labels the
crop-safe rows as extrapolation.**

## Mislabelled

Most damaging category: attributed to a source that does not support it as
stated.

**M1. "Every pixel value below is derived from `reference/canvas-assumptions.md`"
is false.** That file contains the two canvas sizes, the 3x downscale, the 4x
stress test, a 36px type floor and the 12pt rendered minimum. It contains no
margin, no gutter, no column width, no row height and no spacing unit. None of
72, 24, 136, 182 or 96 appears in it, and none follows from it. These are
constructions computed in the skill. **Fixed: the sentence now says which values
come from the shared file and which are constructed here.** This is the same
defect the `dsn-image` audit found, and the identical sentence appears in
`dsn-spacing`.

**M2. "6 gives halves, thirds and quarters."** See A2. Presented as the factor
argument, which in the sources is Flux on twelve ("12 has lots of factors"
[wIabVp0Hh8U 00:04:49]) and Satori on six with "smaller divisions", not quarters
[QcT9a8gcG74 00:02:02].

**M3. "the source that uses twelve is working on a wide landscape banner."**
Two sources in the set use twelve. Satori's is the landscape banner, "let's go
ahead and adapt the campaign to the landscape banner... I'm using 12 columns
here" [QcT9a8gcG74 00:08:03]. Flux's is a desktop frame, "let's type in 12
columns" on "a desktop size frame" [wIabVp0Hh8U 00:04:09, 00:02:38]. The
singular attribution hides the second case, which is the one that actually makes
twelve a web convention. **Fixed to name both.**

**M4. "No software generates the alternative grids; you build them by hand."**
Gareth's claim is weaker: axial, diagonal and radial grids "are not easily
generated in software such as Photoshop InDesign or illustrator"
[BQEVqWiD304 00:08:48]. A source in the same set contradicts the hardened
version outright: "when you long press on the line segment tool, you'll find a
polar grid tool. You can choose that" [oPrDgIuxdYQ 00:04:06].
**Fixed to the sourced strength, with the exception named.**

**M5. "8 or 10 pixel base units. Convention. Figma's default."** Only 10 is
Figma's default in this source set: "this is a simple modular Grid it's like a
baseline grid of 10 pixels" [wIabVp0Hh8U 00:02:38]. No grid source mentions 8 at
all. The 8 unit is UI practice from outside the set. **Fixed.**

**M6. "The oldest well-grounded figure in the discipline [MNMTjffhRcU 00:07:45]."**
The cited passage supports only the mechanism: "if the column is too tight...
your eyes zigging zagging back from the end to the beginning but if it's too
long... you lose your place" [MNMTjffhRcU 00:07:45]. The reviewer says nothing
about the measure's age or its standing in the discipline. A ranking claim is
riding inside a citation that does not carry it. **Relabelled as the skill's own
assessment.**

**M7. "which looks like the inherited print ratio and is not."** There is no
2.5x print ratio in this source set to be mistaken for. Flux's convention is
bottom double the top and inner 1.5x: "we're going to change the bottom margin
to 20 or double what the top margin is" [wIabVp0Hh8U 00:09:49]. So the sentence
warns against inheriting a ratio none of its sources states. **Fixed to name the
actual convention.**

**M8. Margin 72 "clears chrome, survives a centre crop."** Neither half holds on
the plugin's own numbers. `dsn-spacing` puts the chrome zone at 180px, and a
centred square crop of a 4:5 frame costs 135px top and bottom; a 4:5 crop of a
square asset costs 108px each side. 72 is smaller than all three.
**Relabelled as construction with the conflict named.**

**M9. "Two sources and the print literature agree a baseline grid is evenly
spaced horizontal lines on which type sits, so baselines align across columns
and across point sizes."** Only Flux states the whole definition: "a baseline
grid consists of evenly spaced horizontal lines on which the type sits this
allows the designer to align bass lines across columns and differing Point
sizes" [wIabVp0Hh8U 00:01:21]. Gareth supports the lines-for-type half and
vertical rhythm, not the cross-point-size clause: "a series of horizontal
lines... more so to manage type and Define lines where type can set"
[BQEVqWiD304 00:06:39]. **Fixed to split the attribution.**

Related precision point, not fixed: the skill says a third source "uses
'baseline grid' for stacked rectangular bands". That source in fact states the
standard definition first, "Baseline grid is made of horizontal lines that
guides text placements. Every line of text sits perfectly on these guides"
[oPrDgIuxdYQ 00:07:30], and then builds bands. The terminology warning holds for
what it builds, not for what it says.

## Citations that do not resolve

**C1 to C3. Three citations point to video ids that are not in the corpus.**
`N4Dz28mgHpo` (cited at 00:08:58 and 00:02:14) and `7NuKb9mk0ac` (cited at
00:10:56) match no file in `~/research/design-plugin/transcripts/`. They are the
only such ids in the whole plugin: every citation in the other twelve skills
resolves to a transcript. The skill's own header says "Built from five sources",
so three of its ten inline citations come from outside the set it claims. The
underlying claims may well be accurate as talks, but nothing here can check
them. **Marked inline as canon tier, outside the transcript set, unverified.**
These carry real weight in the skill: the reliability argument in the opening,
the Mode B review order, and the whole of principle 4.

**C4. [BQEVqWiD304 00:12:16] is one block late.** The quoted concession is in the
00:11:36 block: "it's not always necessary to use a grid much design is created
without one" [BQEVqWiD304 00:11:36]. The 00:12:16 block begins "so in
application when you're designing posters". **Fixed.** The provenance file
carries the same error.

**C5. [MNMTjffhRcU 00:07:45] for "builds the type area from the measure... before
any layout exists" is in the wrong place.** 00:07:45 is the column-width passage.
The type-area-then-grid order is stated at 00:11:44: "we're going through a lot
of different construction of the type area in this part once the type area is
constructed he's going to go through how to construct the grid"
[MNMTjffhRcU 00:11:44]. **Fixed.**

## Unsupported

**U1. "Four of the five sources spend their runtime enumerating grid types."**
Three do: Flux [wIabVp0Hh8U 00:00:39 to 00:02:38], Gareth
[BQEVqWiD304 00:02:11 onward] and GraphiqVibe, which names six in its opening
[oPrDgIuxdYQ 00:00:00]. Satori does not, which the skill says. The fifth is a
page-by-page review of one book, and its field-grid counts are examples inside a
single system, not a taxonomy. **Fixed to three.**

**U2. "Fail above three distinct left edges on one frame."** No source counts
edges or names a limit. **Labelled derived.**

**U3. "a 4x step minimum between within-group and between-group gaps."** No
source states any ratio. The nearest passage is a 12-pixel unit "giving us
related distances such as 12, 24, and 48" [QcT9a8gcG74 00:07:19], with the rule
stated only qualitatively: "keep related content close... Then leave a larger
gap before the next group". It also contradicts `dsn-spacing`, which sets the
same boundary at about 2x. **Labelled construction, with the conflict named.**

**U4. "Below roughly three information groups a grid adds overhead and no
constraint."** Gareth concedes a grid is not always necessary
[BQEVqWiD304 00:11:36] and then, as the provenance itself notes, says nothing
about when. The threshold is invented. **Labelled derived.**

**U5. "A print-derived 65 to 75 character measure renders unreadable."** No
character count appears in any of the five transcripts, nor in
`canvas-assumptions.md`. The book reviewer discusses measure only qualitatively
[MNMTjffhRcU 00:07:45]. **Labelled as outside the source set.**

**U6. The square and 4:5 grids.** 72, 24, 136, 182, 96 and the row and column
counts are constructions. Covered by M1. The arithmetic closes on both axes and
was checked: 72 + (6 x 136) + (5 x 24) + 72 = 1080, and
72 + (7 x 136) + (6 x 24) + 182 = 1350. Both correct.

**U7. "A 6x6 grid offers hundreds of valid span combinations."** A magnitude
claim with no source and no working. **Labelled derived.**

**U8. The demitasse story.** Uncited in the skill, and the talk it comes from is
not in the corpus. **Marked unverified.**

**U9. "That is the strongest corroboration behind any skill in this plugin."**
A self-assessment, unverifiable from the sources, and in tension with C1 to C3:
the skill leans on two talks nobody can check. **Labelled as the skill's own
claim.**

**U10. "the numbers stay consistent across skills."** They do not. This skill's
square uses margin 72 and a 24 unit; `dsn-spacing` uses a 16 base step, a 64
dead band and a 108 reading margin. 72 and 24 are on neither ladder.
**Fixed as part of M1.**

## Derived but not labelled

Reasonable inferences, stated flatly. Not fixed except where a number was
involved, since relabelling each would mean rewriting arguments.

- **D1. The reader-task to grid table.** The sources say what each grid is for.
  "Compare or scan parallel items", "Notice one thing, then act" and the rest
  are the skill's mapping. Only the hierarchical row is close to a source
  statement: "the hierarchical grid is used for the sole purpose of establishing
  a very clear visual hierarchy" [BQEVqWiD304 00:05:51].
- **D2. "That table is the generator"** for the span assignment table.
- **D3. Mode B's order as a mechanical seven-step sequence.** The review order
  it rests on comes from the unverifiable canon citation.
- **D4. "Slide 1 hierarchical, middles modular"** and the last slide repeating
  slide one's spans.
- **D5. "One permitted break, the same on every slide."**
- **D6. "scale, a relationship rather than a dimension, so it cannot be briefed
  numerically"** in the agent section. Canon, outside the corpus.
- **D7. "A feed graphic is not a page... baseline grids are close to pointless."**
  Sound, but no source discusses feed graphics at all.

## Sourced and verified

Spot-checked and confirmed, with the passage found where claimed:

- Grid as retired decisions, "solve it once by creating a grid and it's done"
  [MNMTjffhRcU 00:42:08].
- Grid chosen from the audience's task, "before choosing your grid, you want to
  identify what the audience needs to accomplish" [QcT9a8gcG74 00:04:21].
- The three questions, asked at [QcT9a8gcG74 00:00:34] and again at 00:03:38.
- The column formula and its walkthrough [QcT9a8gcG74 00:02:52]. Satori's
  illustration is internally consistent: 1200 wide, 60 margins, 1080 usable,
  5 gutters of 24 occupying 120, 960 / 6 = 160.
- Margins bound information not ink, "the background and portrait can extend
  beyond these boundaries, but the important text sits inside it"
  [QcT9a8gcG74 00:01:19].
- Spans assigned by priority [QcT9a8gcG74 00:05:05], and the warning that "the
  widest elements won't automatically be seen first" [QcT9a8gcG74 00:05:46].
- The content-change stress test, four columns to five, outside margin fixed
  [QcT9a8gcG74 00:10:49].
- Guides off at intended size, and asking a stranger what they noticed first
  [QcT9a8gcG74 00:11:32].
- Container before contents [QcT9a8gcG74 00:10:08].
- Sketching at the exact finished ratio, 16 squares by 9 for 16:9
  [MNMTjffhRcU 00:19:37], and the reviewer's own note that the 1:1 comping rule
  aged out with typewriters and phototypesetting [MNMTjffhRcU 00:20:56].
- A shared grid making a series read as a series, "you know that this series
  goes together because of the grid" [MNMTjffhRcU 00:27:44].
- The later chapters stretching the concept, "what vegetable are we looking at
  right here that has to do with a grid" [MNMTjffhRcU 00:36:36].
- Leading growing with type size [MNMTjffhRcU 00:09:04]; inner margin for
  binding [MNMTjffhRcU 00:09:43]; outer margin for fingers
  [MNMTjffhRcU 00:10:24]; 8, 20 and 32 field grids as A4 examples
  [MNMTjffhRcU 00:14:12].
- The image-does-not-fit repairs, box it or lay a colour block over it for
  "greater Optical stability" [MNMTjffhRcU 00:23:13].
- Equal margins reading as default [wIabVp0Hh8U 00:09:49] with the author's own
  disclaimer "these aren't exact relationships that you have to use every time".
- Three and three reading static, repaired with three and two plus a bleeding
  image [wIabVp0Hh8U 00:22:09].
- Pencil before software [wIabVp0Hh8U 00:17:38].
- Biggest zone to the primary element [oPrDgIuxdYQ 00:02:58], and the declared
  sub-guide break, "it's okay to break the rules on these kind of situations"
  [oPrDgIuxdYQ 00:07:30].

Two sources, `wIabVp0Hh8U` and `oPrDgIuxdYQ`, are never cited inline anywhere in
`SKILL.md` despite carrying several of its claims. Not a defect on its own, but
it is why the mislabels above went unnoticed: an uncited claim is never checked.
