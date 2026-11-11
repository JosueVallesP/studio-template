# Audit: dsn-typeset

Independent check of `SKILL.md` against the five transcripts in
`~/research/design-plugin/transcripts/`: `typeset__9w-BwzcuxYM` (the 44-system
census), `typeset__spyPKRE9Ers` (the UI course), `typeset__YYhaZop92Fg` (the
InDesign course), `typeset__eW2-ghXuYC8` (the studio workflow),
`typeset__Dptb5xojbJM` (the craft video). All five read in full. Pixel values
checked against `reference/canvas-assumptions.md`, and the cross-skill figures
against `dsn-spacing` and `dsn-grid`. `references/provenance.md` was read to
find the claims under test and was treated as a suspect, never as evidence.

Counts: 5 mislabelled, 6 unsupported, 7 derived and unlabelled, 34 sourced and
confirmed. Five inline citations, all five resolve to the right source, four to
the exact right timestamp and one off by one block. Fixes applied where
confident are marked **fixed**.

## The arithmetic check

**Every calculation in the derivation and the table is correct.** Recomputed
independently:

| Claim | Check | Verdict |
|---|---|---|
| 12 effective px floor x 3 = 36 | 36 | correct |
| 16 effective px x 3 = 48 body | 48 | correct |
| 20 chars at 0.5 em on an 860 column needs 86 | 860 / 20 = 43 per char, / 0.5 = 86 | correct |
| 15 chars needs 115 | 860 / 15 = 57.33, / 0.5 = 114.7 | correct |
| 96 / 48 = 2.0 over three steps, cube root 1.26 | 1.2599, and 48 x 1.26^3 = 96.0 | correct |
| One step below 48 at 1.25 is 38 | 38.4 | correct |
| 1.125 puts 48 beside 54, two rendered px at 3x | 54, and 18 - 16 = 2 | correct |
| Mobile headline 40 px on a 428 viewport scales to 101 | 40 x 1080 / 428 = 100.9 | correct |
| Line boxes 106 / 87 / 72 / 67 / 55 | 105.6, 87.4, 72.0, 67.2, 55.1 | correct |
| Chars at 860 of 18 / 23 / 29 / 36 / 45 | 1720 / size = 17.9, 22.6, 28.7, 35.8, 45.3 | correct |
| Rendered 12.7 / 16 / 20 / 25.3 / 32 at 3x | 38, 48, 60, 76, 96 divided by 3 | correct |
| Label clears the 12 floor "by less than a pixel" | 12.67 - 12 = 0.67 | correct |
| "A product system carries sixteen text styles" | census averages 4 + 6 + 3 + 3 = 16 | correct |
| Census 75 percent on 1.125 | "seventy-five percent of these systems were using major second" [9w-BwzcuxYM 00:06:48], major second is 1.125 | correct |

Three presentation and consistency problems inside otherwise correct working:

- **The rendered-pixel list runs against the table.** "Rendered at 3x that is
  12.7 / 16 / 20 / 25.3 / 32" ascends while the table descends from `display`
  to `label`, so it reads as if the display line renders at 12.7. **fixed** by
  reversing it to the table's order.
- **The table's label row inverts the census it claims to follow.** The skill
  says "The leading column follows the census gradient but diverges at the top",
  yet it also diverges at the bottom and in the other direction: measured body
  is 147 percent and measured label 141.76 [9w-BwzcuxYM 00:08:37], so the
  census has label tighter than body, while the table has label 1.45 against
  body 1.40. The census narrator's own summary ignores his label figure too,
  "once it reaches the smaller sizes the line height tends to be higher". The
  table's values are defensible from the character count, which is the skill's
  own argument; the claim to be following the measured gradient is not. **fixed**
- **The 4x stress test is cited and never run.** The applied section says the
  "4x stress test come from `reference/canvas-assumptions.md`", and the
  reference says "Check the piece at 25% as well ... a piece that only survives
  3x is at the edge." At 4x the label renders at 9.5 effective pixels and the
  body at 12.0, so the scale fails the stress test it cites and the whole lower
  half of the ramp is at the edge by the reference's own wording. Not fixed,
  because fixing it means changing the scale rather than a label.

**On what was kept against what was discarded: the split is sound.** Every
figure the provenance says it kept is in a transcript where it says it is, and
every figure it says it discarded as garbled is genuinely garbled or genuinely
self-contradictory. Verified individually: the measure band "there is a
character limit of 50 to 75 in one line" [spyPKRE9Ers 00:48:43]; the ratio
distribution [9w-BwzcuxYM 00:06:48], which sums to 100; the leading and
tracking gradients [00:08:37, 00:09:37]; rounding to whole or even numbers
[00:06:48]; the weight skip [YYhaZop92Fg 00:22:23]; the 1.5x paragraph spacing
[spyPKRE9Ers 01:33:45]; the three-line centring limit [01:37:13]. And on the
discard side: the letter-spacing band "the safe limit we have is the minus2 to
+2" [spyPKRE9Ers 01:28:49] is indeed stated in pixels across sizes from 12 to
96, which makes it unusable as given; "0.1 means 010% and sorry 0.1 actually"
[01:28:49] is unrecoverable; the paragraph arithmetic "let's try making it at
least 12 is 20" [01:33:45] breaks mid-sentence; the heading ladder "here we
could use 20 and then here we could go 30 and then here we could go 38"
[01:13:48] does contradict the four-to-six rule stated at [01:12:01]; the
typeface percentages are two incompatible sets, 60 / 30 / 10 at [00:49:39]
against "in 70% cases" at [00:54:47]; "70% of type on the web is using sand
serif" [YYhaZop92Fg 00:04:33] is unsourced and load-bearing on nothing; and the
census display list "36 42 48 60 72 78 and 96" [9w-BwzcuxYM 00:07:36] does
break its own series at 78.

## Mislabelled attributions, most damaging first

1. **"The smallest reliably readable UI text is about 12 effective pixels,
   **the one figure both long-form sources insist on**."** One long-form source
   insists on it: "your body text should never be smaller than 12 pixel"
   and "no need to go below 12 pixel people won't be able to read that"
   [spyPKRE9Ers 01:13:48], with one stated exception at 10 bold. The other
   long-form source states no floor anywhere. It works in InDesign at point
   sizes and the nearest thing to a floor is a passing adjustment on a URL
   line, "I'm going to bring this type to 12. It's a little small there. 14."
   [YYhaZop92Fg 01:21:12], which is a judgement about one string, not a
   minimum. Worse for the claim, the census records shipped label sizes of "10
   12 13 and 14" [9w-BwzcuxYM 00:07:36], so the measured source contradicts a
   12 floor. This is the most damaging finding in the skill because the floor
   is the first input to the derivation: 12 x 3 = 36 sets the bottom of the
   scale, and a doubled attribution makes a single practitioner's rule look
   like a convergence. **fixed**

2. **"The census found the same gradient **across all 44 systems**, negative at
   display and positive at label."** The census reports one average range per
   level, not per system: "for display level the average range is between
   negative two point five percent and negative one percent ... for label the
   average range was between zero and three percent" [9w-BwzcuxYM 00:09:37]. An
   average range across four levels says nothing about how many of the 44
   systems individually show the gradient, and the source never claims it does.
   The same overstatement would let a reader treat the gradient as near
   universal rather than as a mean. **fixed**

3. **"**x-height and aperture for small text**" listed among nine moves that
   "come from two or more independent channels".** Both halves are one channel.
   x-height for small sizes: "Type faces with tall X heights have better
   legibility at small font sizes as the white space within each letter makes
   it more legible" [spyPKRE9Ers 00:08:31], restated at [00:44:03]. Aperture:
   only [spyPKRE9Ers 00:44:51], "it is also like this open part of A and this
   open part of C ... do not prefer them over the ones which have the wider
   aperture". The InDesign course mentions x-height twice, once as an anatomy
   definition [YYhaZop92Fg 00:11:26] and once as a pairing criterion, "having
   them with the same x can help make the design look better" [00:23:14],
   neither about small-size legibility, and never mentions aperture at all. The
   craft video does not mention either. **fixed**

4. **"the four-level structure" in the same list of nine.** Display, heading,
   body, label as a named four-level taxonomy is the census alone
   [9w-BwzcuxYM 00:01:46 to 00:02:35]. The UI course uses headings, body,
   captions, labels and buttons and never a display level [spyPKRE9Ers
   01:04:02]; the studio workflow uses H1 to H6 plus five body sizes
   [eW2-ghXuYC8 00:00:40], which is a different structure with a different
   count. The levels are real as a convergence of roles, not as a shared
   four-level structure.

5. **Citation off by one block: "one source demonstrates the rework
   [eW2-ghXuYC8 00:07:39]".** The rework is demonstrated in the preceding
   block: "if we now change this later on say we've designed a whole website
   and the client says Hey the headings are way too big ... then you're going
   to have to go through and calculate that all again" [eW2-ghXuYC8 00:06:57].
   The cited block holds the resolution, "we can see our line height has stayed
   relative to the font size" [00:07:39]. **fixed**

## Unsupported, including figures absent from canvas-assumptions.md

1. **"The ascender-to-descender span is roughly 1.0 to 1.1 em, so a ratio under
   about 1.05 drives descenders into the next line's ascenders."** Neither
   figure is in any source, and the sentence that follows cites a source for
   the principle, so both read as sourced. Worse, the cited source contradicts
   the 1.05 threshold: having found the failure at 90 percent for one font, he
   gives a safe band well below 1.05, "the safe range for the headings is 80%
   to 120%" [spyPKRE9Ers 00:27:57], and repeats it at [01:25:28]. The
   descender test as a test is sound and his observation is exact; the em span
   and the numeric floor are this skill's construction and one of them cuts
   against the source it leans on. **fixed**

2. **The three leading bands by character count: "Under 25 characters wants
   roughly 1.05 to 1.20; thirty-five to fifty wants 1.35 to 1.45; above
   seventy-five, narrow the column rather than add leading."** No source states
   leading against a character count, which is the skill's own stated
   contribution, "No source states this, and it is the one thing to take from
   the set." The bands themselves are nonetheless set out immediately after a
   sourced citation in the same principle, with no label, so the numbers
   inherit the citation. The nearest sourced bands are by role, not by count:
   80 to 120 percent for headings and "a range of 120 to 160 is an ideal range"
   for body [spyPKRE9Ers 00:28:48]. **fixed**

3. **"0.5 em average character width"** as the conversion from column width to
   character count. In no source. It carries the entire ceiling derivation and
   the whole last column of the table. The provenance admits it; the skill
   presents it as a conversion rule. Low risk because it is checkable in a
   minute, which the skill should say.

4. **"**Tracking on the wrong level.** ... *Fix:* 4 to 8 percent on caps at
   small sizes."** No source states a caps tracking percentage. The census
   measures label tracking at 0 to 3 percent [9w-BwzcuxYM 00:09:37], which is
   lower than the whole band. The UI course works in pixels: +1 px on 12 px
   all-caps, "for 12 I am trying to have all caps now it is not readable so we
   might want to introduce some positive spacing so let's make plus one"
   [spyPKRE9Ers 01:30:33], which is 8.3 percent, and +0.25 to +0.5 px at 12 px
   in sentence case [00:22:38], which is 2 to 4 percent. So the band is a
   conversion of one practitioner's two pixel values, not a figure anyone
   states. **fixed**

5. **"caps over four words fail regardless."** The source says two or three:
   "any text longer than two three words written in the all cap section will
   look like that you are yelling at them" [spyPKRE9Ers 01:43:55], with the
   mechanism at [01:44:43]. Four is looser than the only stated threshold.
   **fixed** to the source's number.

6. **"A display line should hold 15 to 25 characters"** and the test verdict
   "under 25 for display". No source gives a display measure. The 50 to 75 band
   is explicitly scoped to body text by the source, "Understand I'm talking
   about body text" [spyPKRE9Ers 00:48:43]. The display band is a construction,
   and it sets the ceiling. The skill does say the display character count is a
   tone decision an agent cannot make, which is the right instinct, but the
   numbers are not labelled where they are used.

## Derived but not labelled as derived

1. Leading set from characters per line, the central synthesis. The skill does
   say "No source states this", so this one is correctly flagged and is listed
   here only for completeness.
2. "most post graphics need four" styles, and "A seventh means improvising".
   The 16-style product figure is sourced; four to six and the seventh are not.
3. The browser-artifact split itself. No source distinguishes what survives a
   fixed canvas, because none of them works on one.
4. "a feed graphic cannot use the bottom of any scale." The observation it
   rests on is sourced, the three discarded steps [eW2-ghXuYC8 00:10:59]; the
   conclusion for a downscaled canvas is derived.
5. Mode B's stop-at-first-failure ordering, and the reason given for it.
6. Every carousel rule: frozen style set and first baseline, one display step
   per slide, cover slide sized against the thumbnail, CTA lifted off label
   size. None of the five sources discusses a carousel, a feed or a thumbnail.
   The applied section's blanket "Every pixel value below is derived" covers
   the numbers but not these rules.
7. "Two display lines at 18 characters is 36 characters of headline", and that
   this is a copy constraint. Correct arithmetic on a derived character count.

## Sourced and confirmed

Spot list, each checked at the stated place.

- The measure band, exact and in the right scope [spyPKRE9Ers 00:48:43].
- The descender discovery at 90 percent, "this Y tail is now outside that blue
  box ... it feels like there is no spacing" [spyPKRE9Ers 00:25:34 to 00:26:23].
  The skill's paraphrase is accurate.
- The weight skip and the three-weight version, "you should always skip at
  least one font ... Or for even more contrast, use light and bold by skipping
  over three fonts" [YYhaZop92Fg 00:22:23]. Citation resolves exactly, and the
  second channel is "always skip a weight when you're creating the hierarchy"
  with the diagnosis "It looks like a mistake actually" [spyPKRE9Ers 01:42:23].
- Kerning as optical and never automatic on display type, "you should never
  rely on automatic curing on logos or headings" [Dptb5xojbJM 00:01:24], with
  "it needs to look good to the eye" [YYhaZop92Fg 00:33:59] and the manual fix
  at [spyPKRE9Ers 00:19:44]. Citation resolves.
- The census leading averages and the trend it reads off them
  [9w-BwzcuxYM 00:08:37]. Citation resolves, both quoted values correct.
- Five weights as a requirement, "we are always supposed to choose a type uh
  with at least five weights" [spyPKRE9Ers 00:14:41], repeated at [01:38:47].
- Two typefaces as the ceiling, "you don't want to use more than two type faces
  per design" [YYhaZop92Fg 00:17:39], with the UI course agreeing in substance.
- Pair on matching x-height, both channels [YYhaZop92Fg 00:23:14] and
  [spyPKRE9Ers 00:55:34].
- Caps need tracking and lowercase does not, "it's best to use tracking only
  for all caps or small caps" [YYhaZop92Fg 00:32:32].
- Paragraph spacing at least 1.5 times line spacing, attributed by the source
  to the accessibility standard [spyPKRE9Ers 01:33:45]. Worth noting that the
  published criterion is phrased against font size rather than line spacing, so
  the skill inherits the source's phrasing; the direction and the floor are
  right.
- Left align over three lines, "don't align anything centered that is longer
  than three lines. Simple rule." [spyPKRE9Ers 01:37:13].
- The reflow objection to justification [spyPKRE9Ers 01:38:47] and the rivers
  objection [YYhaZop92Fg 00:36:53], correctly separated.
- One-word last lines and staircase rags, "a runt is when a single word appears
  at the bottom of a paragraph" [YYhaZop92Fg 00:39:00] and "you want to make
  sure it doesn't look like a staircase" [00:38:22].
- Never stretch or condense by scaling [YYhaZop92Fg 00:39:44].
- Icon stroke against text stroke, worked live [spyPKRE9Ers 02:03:49].
- Rounding generated decimals, in three channels [9w-BwzcuxYM 00:06:48],
  [eW2-ghXuYC8 00:06:17], [spyPKRE9Ers 01:14:34].
- Multiples of four scoped to absolute line heights [9w-BwzcuxYM 00:07:36] and
  the baseline-grid rejection, "if your design is bad it is not going to be
  fixed by aligning your text" [spyPKRE9Ers 01:27:59].
- Base plus up to two modifiers, with the level as the base
  [9w-BwzcuxYM 00:03:21].
- The two bare-assertion register claims, both real and both bare: "ht King
  works well when you want to convey strength urgency or modernity" and "loose
  King creates a sense of luxury calmness or openness" [Dptb5xojbJM 00:02:11,
  00:02:58], and sharp serifs that "evoke tradition Authority and elegance"
  [00:05:15]. The skill's characterisation of them is exact.
- The three discarded sub-base steps [eW2-ghXuYC8 00:10:59], and the mobile
  headline ceiling of 30 to 40 [spyPKRE9Ers 01:12:57] on the 428 wide frame
  [01:15:36].

Two small notes on that last one. The cross-check calls 96 and 101 "two
independent routes agreeing within rounding"; 5 percent is a fair agreement but
it is not rounding, and the first route produced a range of 86 to 115 from
which 96 was chosen, so the agreement is between a chosen value and a scaled
one. And the viewport matters: the same claim scaled from the 390 wide frame
used earlier in that video [00:59:00] gives 111, not 101.

## Cross-skill consistency

- `860` text column resolves: `dsn-spacing` line 134, "Text column capped at
  **860**". The `936` content width resolves: `dsn-grid` line 144, "usable
  936 x 936".
- The 3x downscale matches `reference/canvas-assumptions.md`. `dsn-typeface`
  is the outlier in the plugin, assuming a 400 to 500 pixel render and roughly
  40 percent, which puts its caption floor of 30 below this skill's conclusion
  that no caption level exists on this canvas. Recorded in that skill's audit.
