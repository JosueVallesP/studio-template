# dsn-contrast: provenance

Everything about where the knowledge in `SKILL.md` came from. The skill itself
carries the uncertainty flags that change what you do; this file holds the
source list, the authority argument, the disagreement with its decision rule,
the convention-versus-derivation labels, the unreliable claims, and what these
sources do not cover.

## The source situation, stated plainly

**This skill rests on a specification, not on practitioners.** That is the
honest description and it is also the correct design.

The area was searched twice, including a name-driven pass over the channels that
cover UI and typography, and it stayed thin. Two usable videos came out of it,
both short, one of them a machine-translated auto-caption with no correct
threshold in it. For every other skill in this plugin that would be a curation
failure. Here it is not, for a specific reason: **contrast for legibility is
governed by a published normative document.** WCAG is a W3C Recommendation, it
is referenced in accessibility law in several jurisdictions, and the numbers in
it are not a practitioner's method that other practitioners might reasonably
contradict. A tutorial on contrast ratios can only restate the spec, correctly
or incorrectly. So the sensible move is to read the spec, use the videos for the
working mechanics and the traps, and say that is what happened.

The cost is real and is flagged throughout `SKILL.md`: these sources carry
**no craft tradition about what good contrast looks like**, as opposed to what
conforming contrast measures. And they carry nothing at all about the condition
Josué's work ships into. Everything in the skill's imagery and feed sections is
derived here.

## Authority tier: the specification

**WCAG 2.2**, W3C Recommendation, 12 December 2024.
`https://www.w3.org/TR/WCAG22/`. Fetched and read 2026-11-06. Supplies every
threshold in the skill, the definitions of contrast ratio, relative luminance
and large scale, the exception lists, and the conformance note on AAA.

- SC 1.4.1 Use of Color, Level A. Colour is not the only visual means of
  conveying information, indicating an action, prompting a response or
  distinguishing a visual element.
- SC 1.4.3 Contrast (Minimum), Level AA. 4.5:1 for text and images of text;
  3:1 for large-scale text and images of large-scale text. Exceptions:
  incidental text (part of an inactive UI component, pure decoration, not
  visible to anyone, or part of a picture that contains significant other visual
  content) and logotypes.
- SC 1.4.6 Contrast (Enhanced), Level AAA. 7:1 for text; 4.5:1 for large-scale
  text. Same exceptions.
- SC 1.4.11 Non-text Contrast, Level AA. 3:1 against adjacent colours for
  visual information required to identify UI components and states (except
  inactive components, or where the appearance is determined by the user agent
  and not modified by the author), and for parts of graphics required to
  understand the content (except where a particular presentation is essential).
- SC 2.4.13 Focus Appearance, Level AAA, new in 2.2. Includes a 3:1 ratio
  between the focused and unfocused states of the same pixels.
- Definition, contrast ratio: `(L1 + 0.05) / (L2 + 0.05)`, L1 the lighter.
  Range 1:1 to 21:1. Notes carry the single-sided-specification failure, the
  anti-aliasing allowance, and the narrow-border-counts-as-letter versus
  wide-border-acts-as-halo rule.
- Definition, relative luminance: `L = 0.2126 R + 0.7152 G + 0.0722 B` on
  linearised sRGB, with the 0.04045 threshold and the 2.4 exponent. sRGB only.
- Definition, large scale: at least 18 point, or 14 point bold, or the CJK
  equivalent. Notes: thin or unfamiliar letterforms are harder to read
  especially at lower contrast; size is as delivered; 14 and 18 point are
  roughly 1.2em and 1.5em for many body fonts but must be checked per font.
- Conformance 5.2.1 Note 2: Level AAA is not recommended as a general policy
  for entire sites, because some content cannot satisfy all of it.

**WCAG 2.1**, W3C Recommendation. Carries 1.4.1, 1.4.3, 1.4.6 and 1.4.11 with
**identical wording and identical figures**, verified by reading both. A piece
checked against 2.2 is checked against 2.1 for contrast purposes. 2.2 is the
current Recommendation and is the one to cite.

**WCAG 3.0**, W3C **Working Draft**, 10 September 2026.
`https://www.w3.org/TR/wcag-3.0/`. Read 2026-11-06. Supplies the
unsettled-model section. Restructures contrast as outcomes named "Text contrast
sufficient (minimum)", "Text contrast sufficient (enhanced)", "Graphical object
contrast sufficient", "Interactive element contrast sufficient" and several
focus and pointer contrast outcomes. All are at section status **Developing**.
The requirement text is literally `@@[contrast measure to be determined]`.

The editor's note attached to the text contrast requirements is the most useful
sentence in this whole source set, and it is W3C naming the current model's
limitations inside its own pipeline: the contrast algorithm used in WCAG 3 is
yet to be determined; the draft assumes the algorithm will include a size and
weight factor; and a separate requirement may be needed if red/green colour
vision deficiency is not accounted for within the algorithm.

**APCA is not mentioned anywhere in the published Working Draft.** Searched the
full document; zero occurrences. That is worth knowing, because secondary
sources commonly describe APCA as though it were in WCAG 3.

## Candidate-method tier: APCA

Not normative. Included in `SKILL.md` only to describe the live state of the
area, with instructions not to treat it as conformance.

- **APCA**, Accessible Perceptual Contrast Algorithm, Andrew Somers, Myndex
  Research, developed within the Visual Contrast subgroup of Silver/WCAG 3.
  `https://github.com/Myndex/apca-w3` and `https://git.apcacontrast.com`.
  Library version 0.1.9, base algorithm 0.0.98G-4g-base-W3, **beta**.
- Its own integration-compliance document states that "WCAG 3 Compliant" does
  not exist yet, and that the only suitable language is that APCA is the
  candidate contrast method for WCAG 3, currently in public beta and subject to
  change prior to adoption.
- Polarity sensitive: reports different values when text and background swap,
  negative for light-on-dark. WCAG 2.x is polarity blind. This is the concrete
  dark-mode gap in the ratio model.
- Published Lc orientation, from the Myndex introduction: Lc 45, Lc 60 and
  Lc 75 roughly correspond to 3:1, 4.5:1 and 7:1, functionally but **not
  backwards compatibly**; the backwards-compatible levels are given as Lc 58,
  Lc 72 and Lc 85. A separate Bronze-level list runs Lc 15, 30, 45, 60, 75, 90.
  **Two different sets of numbers for the same purpose, in the same
  documentation.** That is why `SKILL.md` says not to encode Lc values and to
  verify at the source.
- **W3C's Visual Contrast of Text subgroup wiki**
  (`https://www.w3.org/WAI/GL/task-forces/silver/wiki/Visual_Contrast_of_Text_Subgroup`)
  states that the subgroup is not active, that none of the material on the page
  has been approved by the working group to move forward into WCAG 3 at this
  time, and that the content is not normative. The scoring-level work lives
  there. Treat the whole APCA scoring apparatus as unapproved.

Secondary corroboration that the status is as described, not just as Myndex
describes it: GitHub's Primer accessibility guidance states that APCA is a
proposal and is not normative, and that contrast is valid for compliance only
if it meets WCAG 2.2.

## Explainer tier: the two transcripts

**Pimp my Type (Oliver Schöndorfer), *Fix Color Contrast in Web and UI
Design*** (`contrast__gdohlUn7fVQ`, 10m). **The one genuinely useful video, and
the only source here that is accurate on the figures.** Uniquely supplies: the
whole non-text contrast argument, which is the thing most designers do not know
and which the video is explicitly built around discovering [00:00:00]; the
point-versus-pixel trap, that the spec says points and web work happens in
pixels [00:02:35]; the pixel conversions, 24px and 19px bold; the ranked fixes
for a failing control, border in the text colour as a ghost button first, then
fill, then added signifiers [00:04:58]; the observation that an icon alone
leaves the clickable boundary unclear so a visible boundary is better
[00:05:48]; the 1.4.11 "only visual information that is absolutely required to
identify the component" exception, via Eric Eggert, with the position-and-context
reading [00:06:32–00:07:21]; the confirmation that **text contrast never
relaxes** even where the component's own contrast does [00:07:21]; the legal
framing, national policies plus the European Accessibility Act from 2025
[00:01:41]; and the closing summary that is correct on all four figures
[00:08:43–00:09:37]. Also the framing this skill's principle 3 rests on, that
these are minimum requirements and "you should strive to do this better"
[00:08:03]. Two named specialists appear: **Eric Eggert**, who worked for the
Web Accessibility Initiative, and a second reviewer the transcript renders as
"Mike my foreign" and never recovers.

**Saurabh Saini, *WCAG AA and AAA contrast ratio in UI/UX explained***
(`contrast__M80jKhvooyY`, 11m). **Supplies no usable threshold.** It is an
auto-captioned machine translation, and the figures in it are either absent or
garbled. What survives as correct and useful: ratios run from 1:1 to 21:1 and
21:1 is black and white [00:02:13]; 1:1 means no difference; raising or lowering
a hue's lightness is what moves the ratio, so darkening a yellow against white
walks it from fail to AA to AAA [00:05:04–00:06:12]; a demonstration of the
WebAIM contrast checker as the working tool, with foreground and background
inputs and pass/fail per text size [00:03:59]; the note that Figma now surfaces
contrast in the colour panel [00:06:12]; and the observation that increasing
size or weight improves legibility without fixing a bad ratio [00:08:29–00:08:59],
which is a correct intuition about the thing WCAG 3's editor's note says the
current algorithm lacks.

What is wrong or unusable in it, listed because the skill deliberately takes
nothing numeric from it:

- **It never states the AA or AAA figures.** Not 4.5:1, not 7:1, not 3:1.
- It writes ratios backwards while explaining them, as 1:21, 1:1.2, 1:4, 1:4.2,
  1:8 and 1:3 [00:02:13–00:03:23], and treats the two orders as interchangeable.
  The spec puts the lighter luminance first, so those are inverted. Not every
  ratio in the video: the same sentence at [00:02:13] offers "1:21 or 21:1", and
  the later demonstration quotes "1.1:1" [00:04:32], "5.9:1" [00:06:12], "10:1"
  [00:07:15] and "21:1" [00:06:45] in the spec's own order. The real defect is
  the claim that order does not matter, "Both things are the same thing"
  [00:06:45].
- "Sometimes you get Double A approved even in the ratio of 1:3 and sometimes
  you are not able to get it even in the ratio of 1:5:6" [00:03:23] conflates
  the text-size cases into apparent randomness. The actual explanation is that
  3:1 is the large-text floor and 4.5:1 the normal-text floor.
- "1:8 or 8.2" offered as the AAA boundary [00:03:23] is in the right region by
  accident; the figure is 7:1.
- Its one near-miss figure, a 5.9:1 pair failing AAA for normal text [00:06:12],
  is **consistent** with the spec's 7:1 and never names it.
- "1:21" and "21:1" called "the same thing" [00:06:45]. They are the same pair
  written two ways, but only one is the spec's convention.
- The equation of accessibility with "accessible to human eyes" [00:07:15] is a
  weaker definition than the one the Pimp my Type video gets from Eggert, which
  is about readers with impairments rather than readers in general.

## Corroboration

There is no corroboration analysis to do in the usual sense, because the two
videos are not independent authorities on the same question: they are both
restatements of one document, and one of them restates it inaccurately. The
corroboration that matters is **video against spec**, and it ran as follows.

- **Pimp my Type's four figures all verify** against WCAG 2.2: 4.5:1 normal
  text, 3:1 text above 24px, 3:1 bold text above 19px, 3:1 for icons, graphics
  and UI components. The pixel conversions are correct arithmetic at 96dpi for
  the spec's 18pt and 14pt bold.
- **Saurabh Saini's figures do not verify, because there are none to verify.**
- **The AAA figures come from the spec alone.** Neither video states 7:1 or the
  4.5:1 large-text AAA floor. `SKILL.md` attributes them to the specification
  for this reason.
- **The absence of an AAA non-text criterion comes from the spec alone**,
  confirmed by reading the full 2.2 criterion list rather than by a source
  saying so.
- **The relative luminance formula and the per-channel coefficients come from
  the spec alone.** Neither video gives the formula. Saurabh Saini gestures at a
  "colour scale" and promises a luminance video that is not in this source set.
- **The two-carriers connection is not in either video.** It comes from SC
  1.4.1 plus the existing rule in `dsn-composition`.

## Where the sources disagree

One disagreement, and it is inside the Pimp my Type video, between two named
practitioners on camera.

**Do YouTube's filter chips satisfy 1.4.11?** The chips have a fill that does
not clear 3:1 against the page. **Mike** (surname unrecoverable from the
transcript) says not good enough: wherever there is an interactive control you
have to clearly show its boundary, or people will not know it is a control
rather than plain text [00:04:11]. **Eric Eggert** says he would pass it in an
audit: the definition of user interface component is flexible, you can read the
whole chip group as one component with one state highlighted, that highlighted
state does have enough contrast, and there is nothing else in the same space it
could be confused with [00:07:21].

**Decision rule: design above the floor and the disagreement does not arise.**
The criterion's own wording, "visual information required to identify user
interface components and states", is interpretive by construction, so the audit
outcome depends on the auditor. Both men agree on the thing that resolves it in
practice, which the video states directly: WCAG is a minimum requirement and you
should do better than it. `SKILL.md` records the exception because an agent will
meet it, and then tells you not to rely on it.

## Convention versus derivation

- **All six threshold figures are specification**, verified by reading WCAG 2.2
  on 2026-11-06. Not convention, not derivation, not one practitioner's method.
  This is the only skill in the plugin that can say that about its numbers.
- **24px and 19px** are Pimp my Type's conversion of the spec's 18pt and 14pt
  bold [00:02:35]. The arithmetic is right at 96dpi. The spec's own note that
  you must check per font is the reason `SKILL.md` gives both forms.
- **"Aim at the AAA figure for body text"** is derived here, from the spec's
  conformance note that AAA is not a sensible blanket policy combined with the
  video's minimum-not-target framing. No source states it as a rule.
- **The margin check**, treating a pair close to its floor as failing, is
  derived here from the WCAG 3 editor's note about the algorithm being replaced.
  No source states it. The cutoff is **0.2 of ratio, a default chosen for this
  skill on 2026-11-06** so that the test is decidable from `SKILL.md` alone,
  which the standard requires. An earlier version left it as "a tenth or two" on
  the grounds that inventing a number was the error the skill warns about; an
  undecidable test is the larger error, so the number now exists and is marked
  **(thin)** at the point of use. A different cutoff near it would be equally
  defensible. It is not a specification figure and must never be reported as one.
- **The greyscale test** is shared with `dsn-hierarchy`, where it was derived
  from DesignSpo's colour-vision caveat. Here it has a firmer basis, in the
  luminance coefficients: it is a direct consequence of the formula.
- **Greyscale demoted from verdict to screen, 2026-11-06.** No source makes this
  distinction; it is derived from the formulas. A grey conversion in a design
  tool uses one of several luma weightings, none of them the WCAG relative
  luminance formula, and what the eye then judges is perceived lightness, which
  runs roughly as the cube root of luminance. So the greyscale view cannot return
  a conformance verdict. The earlier verdict wording, "fail if the two greys are
  hard to tell apart", was also undecidable, which the standard forbids. The test
  now selects pairs to compute and the ratio decides.
- **The perceived-lightness arithmetic is derived here.** Computed 2026-11-06
  from the sRGB linearisation and the luminance coefficients. `#777777` has
  relative luminance 0.1845. `#FFFF00` has 0.2126 + 0.7152 = 0.9278, giving
  1.07:1 on white; `#0000FF` has 0.0722, giving 8.59:1 on white. The cube-root
  relation between perceived lightness and luminance is standard colorimetry, not
  a WCAG claim. No source in this set makes the yellow point.
- **The worked hex-to-ratio computation is derived here**, 2026-11-06, by
  applying the specification's own formulas step by step to `#8A8A8A` and
  `#E8491D`. The specification gives the formulas; it does not work an example.
  Added so a reader can compute a ratio from this file alone, as the standard's
  one-read test requires.
- **The three-way boundary with `dsn-palette` and `dsn-color` is a routing
  decision made here**, 2026-11-06, not a sourced claim: palette owns the set,
  colour owns relational and appearance behaviour including simultaneous
  contrast, this skill owns measurable conformance. Simultaneous contrast is a
  named concept, invariant to the ratio because the ratio reads two values in
  isolation.
- **Everything in "Text over imagery" is derived here.** The worst-patch rule
  follows from the ratio being a per-pixel-pair computation, which is sound. The
  ranked treatments, field then scrim then blur then shadow, are reasoning from
  the mechanism, not instruction from a source. **No source in this set mentions
  text over a photograph at all.**
- **The 60 percent scrim starting point is now derived arithmetically rather
  than offered as a placeholder.** Computed 2026-11-06. Standard alpha
  compositing of black at opacity a over an 8-bit sRGB pixel multiplies each
  channel by (1 minus a). For the worked lightest pixel `#D8D4CE`, white text
  reaches 4.60:1 at 45 percent (clearing the 4.5:1 AA floor by 0.10, which the
  margin check fails) and 7.20:1 at 59 percent, which clears the 7:1 AAA
  normal-text figure. 60 percent is therefore the opacity at which the worst
  pixel reaches the AAA body figure rather than scraping the AA floor, and that
  is the derivation `SKILL.md` now shows. The figure is specific to that
  lightest pixel; the measured ratio after the scrim remains the only number
  that counts. The compositing model assumes the design tool blends in
  gamma-encoded sRGB, which is the common case and is not a specification claim.

- **The large-scale boundary in canvas pixels is derived here.** Computed
  2026-11-06 from the spec's 18 point and 14 point bold, delivered size, and the
  3x nominal / 4x stress downscale factor in `reference/canvas-assumptions.md`:
  18 x 3 = 54px and 18 x 4 = 72px; 14 x 3 = 42px bold and 14 x 4 = 56px bold.
  The consequence, that only type at 72px or above on a 1080px canvas is
  reliably large-scale, follows from the assumption file and inherits its
  uncertainty, which is why it is marked **(thin)** in `SKILL.md`. No source
  states it.

- **The point-to-pixel conversion is now shown as arithmetic** (18 x 96 / 72 =
  24px; 14 x 96 / 72 = 18.67px, rounded up to 19 for safety) rather than quoted
  from the video. The 96dpi basis is a convention and the round-up from 18.67 to
  19 is inherited rather than derived, so the rule carries **(thin)**.
- **The whole "Applied to a post visual or carousel" section is derived.**
  Neither video discusses feeds, thumbnails, recompression, downscaling or
  platform dark mode.
- **The Lc correspondences are Myndex's published beta figures**, reported as
  orientation and explicitly not as thresholds. Two conflicting sets exist in
  that documentation, which is recorded above.

## Caption-level and unreliable claims

- The Saurabh Saini transcript is a **machine translation of auto-captions** and
  every number in it should be treated as corrupt. The specific failures are
  listed above. Nothing numeric from it reaches `SKILL.md`.
- "WCAG" is rendered throughout both transcripts as "W CAG", "where cake",
  "work egg" and "cake". "A11y" appears as "A1Y". "Figma" appears as "Sigma".
- The second reviewer in the Pimp my Type video is rendered "Mike my foreign"
  [00:03:20] and his surname is not recoverable from the transcript. Do not
  attribute his position to a named person without checking the video
  description.
- "From 2025 on for many European companies this will become required with the
  European accessibility act" [00:01:41] is a correct direction of travel but a
  legal claim from a typography channel. Do not repeat it as legal advice; the
  implementation dates and the scope vary by member state.
- Pimp my Type's reading of the 1.4.11 exception comes through a paraphrase of a
  conversation with Eggert rather than from the spec text. The spec wording is
  in the authority section above and is what to cite.

## Moved out of SKILL.md by the legibility pass

Recorded 2026-11-06. `SKILL.md` previously carried the following, all of which
is audit rather than procedure and all of which is held above in this file.

- The opening authority argument, naming the specification and the two
  explainers and arguing why a specification is the right basis here. Held in
  "The source situation, stated plainly".
- Four bracketed timecode source IDs, in principle 3, the large-scale bullet,
  the non-text exception paragraph and the worked button failure.
- Two verbatim quotes supporting the minimum-not-target framing, plus the note
  that the second video does not state it. Held in the explainer tier.
- The named practitioners in the 1.4.11 disagreement, and the fact that it was
  recorded between two reviewers on camera. Held in "Where the sources
  disagree", with its decision rule. `SKILL.md` keeps the exception, the
  interpretive-by-construction reasoning and the decision rule, and now names
  nobody.
- The attribution of APCA to its author and research group. The named concept
  stays in `SKILL.md`; the attribution and the version numbers are held here.
- The attribution of the 24px and 19px conversions, and of the greyscale test's
  origin in another skill's colour-vision caveat.
- Three "no source covers this" / "derived here, not sourced" notes in the
  imagery and feed sections. `SKILL.md` now says the specification is silent on
  the case and shows the derivation instead, which is the same information
  stated as mechanism.
- The cross-reference to `dsn-composition` as the origin of the two-carrier
  rule. The rule stays; the reader is no longer asked to resolve where it came
  from.

## Not covered by these sources

- **Print, CMYK and non-sRGB colour.** The luminance formula is defined for sRGB
  and the spec says to evaluate in sRGB unless another space is known to be in
  use. Nothing here governs ink on paper, wide-gamut displays or P3.
- **Dark mode polarity as a design problem.** Neither video raises it. The gap
  is identified only through APCA's polarity sensitivity and the WCAG 3 editor's
  note.
- **Text over photography, video or any non-uniform background.** Absent from
  both videos. Derived in `SKILL.md`.
- **Platform conditions.** Compression, downscaling, feed background inversion,
  thumbnail rendering. Absent. This is the condition Josué's work actually ships
  into and no source in this set addresses it.
- **Colour vision deficiency beyond "do not rely on colour".** No palette
  construction for deuteranopia or protanopia, no simulation workflow, no
  guidance on how many categorical hues stay distinguishable. The WCAG 3
  editor's note says red/green CVD may not be handled by the current algorithm
  at all, which makes this a real gap rather than a nice-to-have.
- **Data graphics.** Series colours, sequential and diverging scales, encoding
  choices. 1.4.11's "parts of graphics required to understand the content"
  covers the floor and nothing about the encoding. Use the `dataviz` material.
- **Accessibility beyond contrast.** Focus order, semantic headings, alt text,
  keyboard navigation, screen readers, touch target size. Out of scope here by
  design; the `design` plugin's `accessibility-review` skill covers the wider
  audit.
- **Any measurement of real reader outcomes.** No source here, including the
  spec, reports a reading test against these thresholds. The spec's figures come
  from vision science the document cites rather than reproduces; the videos
  report the figures. The recital test in `SKILL.md` is the only thing touching a
  real reader and **no source runs it.**
- **Motion and animation.** Nothing on contrast in moving content, flashing
  thresholds aside.

## Changed by the cross-skill numeric reconciliation

The shared floor is two figures, not one: 36px at the nominal 3x downscale and 48px at the 4x stress case, both delivering about 12pt rendered. A floor quoted without its case is incomplete. The framing is established in `reference/canvas-assumptions.md`.

- **The applied floor line.** Previously stated 36 pixels alone, with the division by 3 shown but the case unnamed, which left the file silent on the stress case it applies everywhere else. It now gives both floors with both divisions and says to quote the case with the number. Nothing is downstream of it: the 54px and 72px large-scale boundaries, the 42px and 56px bold boundaries and the 36-to-71px normal-text band are unchanged and still close.
- **Verified and left alone.** The greyscale warning here agrees with the one in `dsn-color`; the 72px stress-safe large-text boundary agrees with `dsn-composition`, `dsn-sequence` and `dsn-hierarchy`.
