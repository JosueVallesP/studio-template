---
name: dsn-contrast
description: Use when text may be unreadable, before setting type over a photograph, or when checking a design against WCAG. Gives the ratios, the tests and the fixes.
---

# Contrast and legibility

This skill decides whether a reader can physically resolve the text in a piece, and reports that as a number with a verdict attached. The single idea underneath it: **contrast is a floor you clear, not a quality you tune.** A pair of colours either separates enough for a reader with reduced vision to tell the letterforms from the background, or it does not, and the measurement that answers this is not a matter of taste. Clearing the floor says nothing about whether the piece is good; it says only that the words arrive. So this file is arithmetic, plus the small number of judgements the arithmetic cannot make.

## What this skill is for

Use it to:

- pick a text and background pair a reader with reduced vision can still read
- set type over a photograph or a background you do not control
- check a graphic or an interface against a named standard and report a verdict
- fix a failing pair with the cheapest change that fixes it
- answer "does this pass" without misquoting the figures

## Confidence

**This is the only skill in this plugin that rests on a published standard rather than on practitioner accounts.** Its sibling skills describe house styles and have to hedge; contrast has a defined measurement and defined thresholds, so a verdict here can be computed from two colour values and checked by anyone. Treat every threshold in the table below as firm, and quote it as a requirement.

Firm covers only what the standard covers, and that leaves a lot out: text over photography, feed rendering, recompression, platform dark mode, and how far above a floor you should sit. Figures for those were chosen here, and are marked **(thin)**, meaning they rest on a single account or on reasoning done here and are one house style rather than a requirement. Two limits apply even to the firm figures. The ratio is a crude model of perception and the body maintaining it is replacing the algorithm, which is worked out below. And no reading test of a real reader against these thresholds is reported anywhere, so a passing number says the letterforms are resolvable in principle, not that anyone read them.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**sRGB.** The standard colour space for screens, and the only space in which the figures below are defined. A hex code like `#8A8A8A` is an sRGB value. Nothing here governs ink on paper, CMYK, or wide-gamut displays such as P3.

**Relative luminance (L).** How much light a colour emits, on a scale where 0 is the darkest black and 1 is the lightest white. For sRGB it is `L = 0.2126 R + 0.7152 G + 0.0722 B`, where R, G and B are the channel values after linearising: divide the 8-bit value by 255, then if the result is at or below 0.04045 divide it by 12.92, otherwise compute `((value + 0.055) / 1.055) ^ 2.4`. The exponent exists because screens encode brightness non-linearly, and the formula undoes that encoding before weighting the channels.

**Linearising.** Converting a stored colour value back to the amount of light it represents. Skipping it is the commonest way a hand-rolled contrast calculation comes out wrong.

**Perceived lightness.** How light a colour looks to a viewer. This is a different quantity from relative luminance and it is not what the ratio reads, so the two disagree and the disagreement is where eyeballed verdicts come from. Perceived lightness runs roughly as the cube root of luminance, so the mid grey that looks halfway between black and white, `#777777`, has relative luminance 0.1845, about a fifth of the light rather than half of it. The two diverge hardest on saturated hues, most visibly on yellow. A pure yellow `#FFFF00` looks like a vivid colour rather than a near-white, yet its relative luminance is 0.2126 + 0.7152 = 0.9278, within a hair of white's 1.0, so yellow text on white measures (1.05) / (0.9278 + 0.05) = **1.07:1** and cannot be read. A pure blue `#0000FF` looks comparably vivid and has luminance 0.0722, giving (1.05) / (0.1222) = **8.59:1** on white. Same apparent intensity, opposite verdicts.

**Contrast ratio.** `(L1 + 0.05) / (L2 + 0.05)`, where L1 is the relative luminance of the lighter colour and L2 of the darker. Range 1:1 to 21:1. Written lighter side first, so `21:1`, never `1:21`. The two are the same pair written two ways but only one is the convention, and an agent that writes them interchangeably will eventually invert a verdict.

**Non-text contrast.** The floor that applies to things that are not letters, in two cases: the visual information needed to identify a control or the state it is in, such as a button's boundary or a checkbox's checked indicator, and the parts of a graphic needed to understand the content, such as a meaningful arrow or a plotted line in a chart. It is one criterion at one level with one figure, and shapes that are purely decorative fall outside it.

**Hue, saturation, luminance.** Hue is which colour it is, red against green. Saturation is how pure it is. Luminance is how much light it emits. Only the third enters the ratio.

**Success criterion (SC).** One numbered, testable requirement in the specification, such as SC 1.4.3. Quote the number with the verdict.

**Level A, AA, AAA.** Three conformance tiers. A is the most basic, AA is the working standard almost everyone means by "accessible", AAA is the enhanced tier. The specification's own conformance section says AAA is not recommended as a general policy for an entire site, because some content cannot satisfy all of it.

**Large-scale text.** A size, not an impression: at least 18 point, or 14 point bold, measured as delivered to the reader rather than as drawn in your file.

**Normal text.** Any text that is not large-scale. Captions, secondary text and small print are normal text and owe the normal-text floor.

**Floor and margin.** The floor is the ratio a pair must clear for its role and level. The margin is measured ratio minus floor. Report both; a bare measured figure hides whether a pair is comfortable or scraping through.

**Greyscale.** Discarding hue and saturation so a pair is compared on lightness alone. It is a screen, not a measurement: tools convert to grey by several different weightings, none of them the ratio's formula, and what you then judge is perceived lightness rather than relative luminance. So **a greyscale eyeball check is not a ratio check.** It tells you a pair may be carrying its difference in hue; it never tells you whether that pair conforms.

**Colour vision deficiency (CVD).** Reduced ability to distinguish certain hues, most commonly red from green, affecting a few percent of readers. CVD leaves luminance differences intact, which is why luminance is the safe carrier and hue is not.

**Polarity.** Whether text is dark on light or light on dark. The ratio returns the same number either way, which is a known gap in the model rather than a property of perception.

**Scrim.** A semi-transparent flat or gradient fill laid between a photograph and the text on top of it, to pull the background away from the text's luminance. Dark scrim under light text, light scrim under dark text.

**Worst patch.** The single pixel pair under a run of text with the smallest contrast ratio. Over a photograph this is the number that decides the verdict.

**Counter.** The enclosed or partly enclosed white space inside a letter, the hole in an `o` or `e`. A letter outline wide enough to fill its counters stops reading as part of the letter.

**Ghost button.** A control drawn as an outline in the text colour with no filled background, used when a filled control cannot be made to separate from the page.

**Device-independent pixel and the downscale factor.** A post graphic is drawn at 1080 pixels wide and displayed in a feed column of roughly 360 device-independent pixels on a phone, so it is seen at about one third of its drawn size. That ratio, **3x nominal with 4x as a stress test**, comes from `reference/canvas-assumptions.md` and converts a drawn pixel size into a delivered point size: delivered points equals canvas pixels divided by the downscale factor. **(thin)**

**Recompression.** The lossy re-encoding a platform applies to an uploaded image. It erodes thin strokes and hairline borders without changing the colour values you measured, so a pair can pass on the artboard and fail in the feed.

### Computing a ratio from two hex values

Worked end to end for `#8A8A8A` on `#FFFFFF`, so the formulas above can be run without a tool.

1. **Split and scale each channel.** `8A` is 138 in decimal. 138 / 255 = 0.541176. All three channels are `8A`, so all three scale to 0.541176.
2. **Linearise each channel.** 0.541176 is above 0.04045, so use the exponent branch: ((0.541176 + 0.055) / 1.055) ^ 2.4 = (0.565096) ^ 2.4 = **0.254269**.
3. **Weight and sum.** L = 0.2126(0.254269) + 0.7152(0.254269) + 0.0722(0.254269) = **0.254269**. The weights sum to 1, so a neutral grey's luminance is just its linearised channel value; a non-neutral colour needs all three terms computed separately.
4. **Do the same for the other colour.** Every `#FFFFFF` channel scales to 1.0 and linearises to 1.0, so L = **1.0**.
5. **Order the pair and divide.** The lighter luminance goes on top: (1.0 + 0.05) / (0.254269 + 0.05) = 1.05 / 0.304269 = **3.45:1**.

For a non-neutral colour the only change is step 3. `#E8491D` scales to 0.909804, 0.286275, 0.113725, which linearise to 0.806928, 0.066604, 0.012280, so L = 0.2126(0.806928) + 0.7152(0.066604) + 0.0722(0.012280) = 0.171553 + 0.047635 + 0.000887 = **0.220075**, and on white that is 1.05 / 0.270075 = **3.89:1**. Note how little the blue term contributes: 0.000887 out of 0.220, which is the weighting that makes hue difference worthless and luminance difference everything.

## The principles

1. **Compute the ratio from luminance and never from how different the colours look.** Two colours of similar luminance fail however unlike they appear, because the formula reads only the light they emit, and green contributes about ten times what blue does and three times what red does. A saturated red at `#E8491D` has relative luminance 0.2201 and a mid grey at `#8A8A8A` has 0.2542, so the pair measures `(0.2542 + 0.05) / (0.2201 + 0.05)`, which is 1.13:1, barely above the 1:1 floor, despite being a loud clash on screen. **Hue difference alone creates no contrast.** *Checked by the greyscale test.*

2. **Name what the pair carries before quoting any figure.** The specification sets different floors for normal text, large-scale text and non-text information, and no floor at all for two cases, so a figure quoted without a named role is a figure quoted at random. This is the single commonest error in the area: one remembered number applied to headlines, icons and borders alike. *Checked by the role test.*

3. **Work to AA, then aim above it for body text.** **(thin)** AA is the standard anyone will audit you against. The AAA figure is the margin to aim at for running text where the design allows, because the AA floor was set so that most readers are covered rather than all of them, and because the measurement method itself is being replaced. A pair at 4.6:1 conforms and is still unreadable at thumbnail size on a bright street. Conformance is a number; legibility is whether you read it without leaning in. *Checked by the margin check and the delivery-size read.*

4. **Treat a pair within a tenth or two of its floor as failing.** **(thin)** The ratio is a crude model of perception, the body maintaining it has said so in its own drafts, and a pair sitting on the floor has no room to absorb either a measurement revision or a rendering difference. `#767676` on white measures 4.54:1 against a 4.5:1 floor, which is a pass with 0.04 of margin, which is not a pass worth shipping. `#717171` on white measures 4.88:1 and is. *Checked by the margin check.*

5. **Give every distinction that colour makes a second, non-colour carrier.** Colour may reinforce a distinction. It may not be the sole means of making it. Red for error and green for success with no icon, no label and no position difference fails for a reader with red-green CVD and in any monochrome reproduction, and it fails silently, which is why it survives review. The second carrier can be a shape, an icon, a word, a position, a weight or an underline. *Checked by the two-carrier audit on colour.*

6. **Specify both sides of every pair.** A text colour named without its background, or a background without its text, cannot be evaluated at all, and the specification treats that as a failure in itself rather than as an omission, because the unspecified side falls back to a user default nobody can predict.

7. **Measure, do not eyeball, and measure at the delivered size.** A contrast checker, your design tool's contrast panel and browser developer tools all compute the same formula, so the measurement is free and there is no reason to estimate it. What they cannot tell you is the delivered size, which decides which floor applies. Compute that from the downscale factor before you read a floor off the table. *Checked by the delivery-size read and the thumbnail check.*

8. **Over a photograph, measure the worst patch and never an average.** The ratio is computed per pixel pair, so a photograph has as many ratios as it has pixels under the text. An average conforms on paper and loses the word that fell on the highlight. *Checked by the worst-patch sample.*

9. **Look the threshold up rather than recalling it.** These are exactly the figures that drift in retelling, because 4.5:1 appears twice in the specification meaning two different things and because the non-text criterion has no enhanced tier for people to remember. Confirm any figure against the current specification text before quoting it, and say which version you checked and when. *Checked by the spec check.*

## The thresholds

From WCAG 2.2, the current W3C Recommendation of 12 December 2024. WCAG 2.1 carries these four criteria with identical wording and identical figures, so a piece checked against one is checked against both. 2.2 is the one to cite.

| What the pair carries | Criterion | AA | AAA |
| --- | --- | --- | --- |
| Normal text, and images of text | 1.4.3 / 1.4.6 | **4.5:1** | **7:1** |
| Large-scale text, and images of it | 1.4.3 / 1.4.6 | **3:1** | **4.5:1** |
| Visual information required to identify a UI component or its state | 1.4.11 | **3:1** | no criterion exists |
| Parts of a graphic required to understand the content | 1.4.11 | **3:1** | no criterion exists |
| Incidental text: part of an inactive component, pure decoration, not visible to anyone, or part of a picture containing significant other visual content | 1.4.3 / 1.4.6 | none | none |
| Text that is part of a logo or brand name | 1.4.3 / 1.4.6 | none | none |

Colour as the sole carrier of information is SC 1.4.1, Level A, and carries no ratio at all. It is a yes-or-no requirement, and being Level A it sits in the most basic tier.

Four things in this table get misquoted, and each has a mechanism behind the error.

**Large-scale is stated in points, and the conversion is arithmetic you should do rather than remember.** At the conventional 96 dots per inch, one point is 96/72 pixels, so 18 point is 18 x 96 / 72 = 24 pixels, and 14 point bold is 14 x 96 / 72 = 18.67 pixels, which is usually rounded up to 19 for safety. **(thin)** The specification adds that 14 and 18 point land near 1.2em and 1.5em for many body faces but must be checked per face, and it notes separately that unusually thin strokes or unfamiliar letterforms are harder to read especially at lower contrast, so a face can satisfy the size rule and still fail a reader.

**4.5:1 appears twice and means two different things:** the AA floor for normal text, and the AAA floor for large-scale text. "4.5 is AA" stated without the text size is how a headline that owed only 3:1 gets reported as failing, and how body text that owed 7:1 gets reported as passing AAA.

**There is no AAA non-text criterion.** Non-text contrast is SC 1.4.11 at Level AA with no enhanced counterpart. Asked for "AAA for icons", say the criterion does not exist and give 3:1. One related criterion does sit at AAA: SC 2.4.13 Focus Appearance, new in 2.2, which requires a focus indicator at least as large as a 2-pixel perimeter of the component and a 3:1 ratio between the focused and unfocused states of the same pixels. So a question about focus indicators at AAA has an answer, and the figure is 3:1 either way.

**AAA is not a blanket target.** AA is the standard you work to and will be audited against; AAA is the figure you aim body text at, element by element, where the design allows.

**Non-text contrast has one exception worth knowing and not relying on.** **(thin)** SC 1.4.11 covers only visual information *required* to identify a component, so where position and context already identify something, two buttons in an obvious save-and-cancel arrangement for instance, the fill arguably need not clear 3:1 against the page. This reading is interpretive by construction and competent auditors land on opposite sides of it, so the decision rule is to design above the floor and never meet the question. **Text contrast never relaxes**, whatever happens to the component's own fill. The failure to recognise is a button whose fill nearly matches the page: the label passes, and readers see only text, so they do not know there is a control there. Fixes, cheapest first: a border in the text colour, making it a ghost button; a darker or lighter fill; an added signifier such as an underline. An icon with no visible boundary leaves the tappable area unclear, so a boundary beats an icon.

## How to work

### Mode A: making something

1. **List every colour pair in the piece and name the role of each** before picking a number: body text, large text, control boundary, meaningful graphic part, decoration, logo.
2. **Compute the delivered size of every text pair** from the downscale factor, because that decides whether a pair owes the normal-text floor or the large-scale one.
3. **Read the floor off the table and measure the pair.** Work to AA.
4. **Clear the floor with a margin,** aiming at the AAA figure for body text. Anything within a tenth or two of the floor is a fail.
5. **For text over imagery, use the imagery section** and sample the worst patch. Never measure against an average of the photograph.
6. **Give every colour-carried distinction a second carrier,** and measure any inverted variant separately, because the ratio cannot see polarity and a palette tuned for light mode is unmeasured in dark mode.
7. **Export at delivery specification and run the ultimate test.**

### Mode B: judging something that exists

1. Build the pair list: every text and background combination, every control boundary, every meaningful graphic part. Name each role and compute each delivered size.
2. Measure each. Report ratio, role, criterion, level, floor, verdict and margin.
3. Run greyscale, the two-carrier audit on colour, and the worst-patch sample on anything over imagery.
4. Run the delivery-size read and the thumbnail check, then the ultimate test, then walk the anti-patterns.
5. Report what passes, what fails, and the cheapest fix for each. **The cheapest fix is almost always moving one colour's luminance, not reworking the palette**, because luminance is the only axis the ratio reads and a hue-preserving darkening usually leaves the design intact.

## Text over imagery

Nothing in the specification addresses a caption set over a photograph, so the reasoning below is derived from the definition of the ratio rather than quoted from a requirement.

Because the ratio is a per-pixel-pair computation, the requirement is that the **worst local pair under the text clears the floor.** An average does not conform. The "part of a picture that contains significant other visual content" exception does not rescue you either: that covers text inside the photograph, a street sign in the scene, not a caption laid over it.

Treatments, cheapest and most reliable first. **(thin)**

1. **Put the text on its own field:** a solid block, bar or panel behind it. This converts the problem back to a two-colour pair you measure once, and it is the only option that survives a platform crop, because a crop can move the text onto different pixels but cannot move it off its own panel.
2. **Scrim the photograph under the text,** flat or gradient, dark under light text. Set the opacity by measuring rather than by taste: sample the lightest pixel under the text, composite the scrim over it, and raise the opacity until that worst pixel clears the floor. The arithmetic is worked below.
3. **Blur the region as well as darkening it.** Blur averages neighbouring pixels, so it narrows the spread between the best and worst pair without raising either reliably. A help after a scrim, never a substitute for one.
4. **Last resort, an outline or shadow on the letters.** A narrow border around a letter counts as part of the letter and does add contrast. A wide border that fills the counters acts as a halo and counts as background instead, which means the fix has a width at which it stops working. Hard to measure and it degrades under recompression.

Then check at delivered size, because recompression erodes thin strokes and fine borders, and downscaling lowers the delivered point size, which can push text out of the large-scale category it was relying on for its 3:1 floor.

## Where the measurement model is unsettled

The ratio is widely understood to be a crude model of perception, and **the body maintaining it is replacing the algorithm rather than the thresholds.** The WCAG 3.0 Working Draft of 10 September 2026 states its text contrast requirement as a contrast measure still to be determined, with an editor's note saying the algorithm is yet to be chosen, that the draft assumes it will include a size and weight factor, and that a separate requirement may be needed if red-green colour vision deficiency turns out not to be accounted for within it. That is the specification's own maintainers naming two limitations of the current model inside their own pipeline: it ignores size and weight, and it may not handle the commonest form of CVD. A third limitation is that it is polarity blind, returning an identical number for light-on-dark as for dark-on-light.

The candidate replacement is **APCA**, the Accessible Perceptual Contrast Algorithm. It is polarity sensitive, which is exactly the dark-mode gap the ratio cannot see, and it reports Lc values rather than ratios. Treat it as information about where the area is going, not as a standard: it is beta, it is not normative, its own documentation publishes two conflicting sets of Lc levels for the same purpose, and the published WCAG 3 draft names no algorithm at all. **Do not encode Lc numbers as thresholds, and never present an APCA result as conformance.**

Working position: **conform to WCAG 2.2 AA, aim above it, and expect the measurement method to change.** A design with real margin survives that change. A design sitting on 4.5:1 might not. That is the mechanism behind principles 3 and 4, and it is the whole reason the margin check exists.

## Tests

Each returns a verdict decidable from this file alone. Run them in this order.

| Test | Catches | Verdict |
|---|---|---|
| **1. Role** | The wrong threshold applied confidently | Name what each pair carries: body text, large text, control boundary, meaningful graphic part, decoration, logo. Fail any pair with no named role, and quote no figure for it, because there is no floor to quote. |
| **2. Delivered size** | A floor read off the drawn size instead of the seen size | Divide each text element's canvas pixel size by the downscale factor. Fail if any pair was assigned the 3:1 large-scale floor while its delivered size is under 18 point, or under 14 point when bold. |
| **3. Greyscale** | Contrast carried by hue alone | Desaturate the piece, then compute the ratio for every pair whose two greys show no visible edge between them. Fail the test if any pair in the piece was accepted on how unlike the colours looked rather than on a computed ratio. The greyscale view selects which pairs to compute; the number, never the view, returns the verdict. |
| **4. Margin check** | A pass with no room in it | Measured ratio minus floor. Fail at 0.2 or less, and treat the pair as failing in practice even though it conforms. **(thin)** |
| **5. Two-carrier audit on colour** | SC 1.4.1 failures and CVD failures | For every distinction colour makes, name the second carrier in words. Fail any distinction where you cannot name one. |
| **6. Worst-patch sample** | An average hiding a highlight | Over imagery, sample the lightest and the darkest pixel under the text and compute both ratios. The worse number is the number. Fail if that number is below the floor. |
| **7. Boundary** | SC 1.4.11 failures on containers | Cover the label inside a button, chip or card and ask whether you can still see where the thing is. Fail if the shape vanishes; it needs a border or a stronger fill. |
| **8. Delivery-size read** | Numbers that pass and text that does not read | Export at delivery specification, open it on the target device, hold it at arm's length and read the smallest text aloud. Fail on any word you had to lean in for or guess. |
| **9. Thumbnail check** | Thin type and hairlines that survive the artboard and not the pipeline | View at feed thumbnail scale, after recompression if you can get it. Fail if a stroke, border or hairline has thinned or broken up. |
| **10. Polarity check** | A dark-mode variant nobody measured | If the piece has an inverted variant, measure every pair in it separately. Fail if any pair was assumed to carry over from the light variant on the strength of its ratio. |
| **11. Spec check** | A figure that drifted in retelling | Before quoting any threshold, confirm it against the current specification text. Fail if a figure in your report came from memory rather than from a lookup, and state which version you checked and when. |

## Anti-patterns

- **One number for everything.** "We use 4.5:1", applied to headlines, icons and borders alike. *Fix:* role test, then the table.
- **Hue instead of luminance.** Two mid-tone accents chosen because they look different. *Fix:* greyscale, then move one colour's luminance rather than its hue.
- **Greyscale read as the verdict.** A pair cleared because the two greys looked different enough after desaturating. *Fix:* greyscale only selects which pairs to compute; compute the ratio and report that.
- **Averaging over a photograph.** Measured at the mid-tone while two words sit on a highlight. *Fix:* worst-patch sample, then a field or a measured scrim.
- **Treating the pass as the goal.** A palette tuned to land just over the floor everywhere. *Fix:* margin check, and aim body text at the AAA figure.
- **Colour as the only carrier.** Red for error and green for success, with no icon or label. *Fix:* add the second carrier.
- **Invisible control.** A button or chip whose fill does not separate from the page, so it reads as plain text. *Fix:* boundary test, then a border in the text colour or a stronger fill.
- **Light grey on white for secondary text.** The commonest real failure, because it looks refined on a calibrated monitor in a dark room. *Fix:* measure and darken. Secondary text is normal text and owes 4.5:1.
- **Thin type carrying the ratio.** A hairline that measures fine and vanishes after recompression. *Fix:* add weight or raise the ratio, then run the thumbnail check.
- **Claiming AAA for icons,** a figure for a criterion that does not exist. *Fix:* say the criterion does not exist, and give 3:1.
- **Checking only at artboard size.** Legible at 1080 pixels wide, illegible at 360. *Fix:* delivery-size read before shipping.
- **Measuring against the feed.** Treating the app's own background as one side of a pair. *Fix:* put the piece's own background inside the frame, because dark mode flips the app's and you do not control it.
- **An unmeasured dark variant.** Light-mode pairs inverted and shipped on the assumption the ratio carried over. *Fix:* polarity check.

## Applied to a post visual or carousel

Canvases are square at 1080 x 1080 and portrait at 1080 x 1350, from `reference/canvas-assumptions.md`. The downscale factor is 3x nominal and 4x as a stress test, so **delivered points equals canvas pixels divided by the downscale factor.**

That single division decides which floor applies, so compute the large-scale boundary for this canvas before anything else:

- Large-scale needs 18 point delivered. At 3x that is 18 x 3 = **54 canvas pixels**. At the 4x stress test it is 18 x 4 = **72 canvas pixels**.
- Large-scale also admits 14 point bold. At 3x that is 14 x 3 = **42 canvas pixels bold**. At 4x, 14 x 4 = **56 canvas pixels bold**.
- The working-file floor for any text at all is **36 pixels at the 3x nominal case**, which is 36 / 3 = 12 point delivered, and **48 pixels at the 4x stress case**, which is 48 / 4 = 12 point delivered. Quote whichever case the piece is being held to; a bare floor figure does not say what it survives.

So on these canvases **only type at 72 pixels or above is reliably large-scale**, and everything between 36 and 71 pixels is normal text owing 4.5:1 once you honour the stress test.

### Worked example: single square frame

**Before.** A 1080 x 1080 graphic on a white field. Headline at 64 pixels in the brand accent `#E8491D`. Caption at 36 pixels in `#8A8A8A`. A small arrow icon in the accent over white. Logo wordmark in `#B8B8B8`.

**Diagnosis, computed.**

- *Caption, delivered size.* 36 / 3 = 12 point. Not bold. Normal text, so SC 1.4.3 Level AA, floor **4.5:1**.
- *Caption, measured.* `#8A8A8A` has relative luminance 0.2542, white has 1.0, so the ratio is (1.0 + 0.05) / (0.2542 + 0.05) = 1.05 / 0.3042 = **3.45:1**. Margin is 3.45 minus 4.5, so **minus 1.05. Fails.**
- *Headline, delivered size.* 64 / 3 = 21.3 point at nominal, which clears 18 point, so at nominal it is large-scale with a **3:1** floor. 64 / 4 = 16.0 point under the stress test, which does not clear 18 point, so under the stress test it is normal text with a **4.5:1** floor.
- *Headline, measured.* `#E8491D` on white is **3.89:1**. Margin against 3:1 is plus 0.89, a pass at nominal. Margin against 4.5:1 is minus 0.61, a **fail under the stress test**. This is the downscaling trap in one line: the headline passes only because of a size category it loses the moment the feed column narrows.
- *Icon.* The arrow carries meaning, so it is a part of a graphic required to understand the content: SC 1.4.11 Level AA, floor **3:1**. `#E8491D` on white at 3.89:1 passes with 0.89 of margin. There is no AAA figure to report, and if asked for one, say the criterion does not exist.
- *Logo.* Text that is part of a logo or brand name has no contrast requirement, which is permission to keep it quiet. Quiet is not invisible, and nothing else in the frame should be reading at the logo's weight.
- *Greyscale test.* The accent and the caption grey sit at luminance 0.2201 and 0.2542, so accent on caption grey would be (0.2542 + 0.05) / (0.2201 + 0.05) = **1.13:1**. Never set one on the other, and do not let the accent stand in for the caption grey anywhere.

**After.**

- *Caption.* Darkening along the same neutral axis: `#767676` on white is 4.54:1, a margin of plus 0.04, which test 4 fails at 0.2 or less. Go further to `#717171` on white at **4.88:1**, margin plus 0.38, passes. For the AAA body target of 7:1, `#595959` on white measures **7.00:1** exactly, which is the figure to use when the design can carry it.
- *Headline.* Two fixes, either sufficient. Raise the size to 96 pixels: 96 / 3 = 32 point and 96 / 4 = 24 point, so it is large-scale at both, and 3.89:1 against the 3:1 floor is a margin of plus 0.89. Or hold 64 pixels and darken the accent to `#C62A0B`, which measures **5.62:1** on white, a margin of plus 1.12 against the normal-text floor and therefore size-independent. Prefer the darkened accent when the piece has to survive an unknown crop, since it removes the dependence on a size category entirely.
- *Report line.* "Caption `#717171` on `#FFFFFF` at 4.88:1. Normal text at 12 point delivered, SC 1.4.3 AA, floor 4.5:1. Passes with 0.38 of margin. Checked against WCAG 2.2 on 2026-11-06."

### Worked example: portrait slide with text over a photograph

**Before.** A 1080 x 1350 slide. White caption at 42 pixels regular, set directly over a photograph.

**Diagnosis, computed.**

- *Delivered size.* 42 / 3 = 14.0 point. 14 point qualifies as large-scale **only when bold**, and this is regular, so it is normal text: floor **4.5:1**.
- *Worst-patch sample.* Sampling under the caption run gives a lightest pixel of `#D8D4CE` and a darkest of `#3B3A38`. White on the darkest is 11.36:1, comfortable. White on the lightest is (1.0 + 0.05) / (0.6614 + 0.05) = 1.05 / 0.7114 = **1.48:1**. The worse number is the number: **1.48:1, failing by 3.02.** An average of the two would have reported something near 6:1 and shipped.

**After, deriving the scrim opacity rather than guessing it.** Compositing black at opacity a over a pixel multiplies each channel by (1 minus a), so `#D8D4CE` under a 45 percent black scrim becomes (216, 212, 206) x 0.55, which rounds to `#777571`, and white on that measures **4.60:1**. That clears the 4.5:1 floor by 0.10, which test 4 fails. Raise it: at 59 percent the lightest pixel becomes `#595754` and white on it measures **7.20:1**, clearing the 7:1 AAA figure for normal text. So **60 percent black is the working starting point, and it is the opacity at which the worst pixel reaches the AAA body figure rather than scraping the AA floor.** At 60 percent the darkest pixel becomes `#181716` at 17.9:1, so nothing in the range has gone too dark for white text. Re-measure after any change to the photograph, because the number depends entirely on that lightest pixel.

**The cheaper alternative, for comparison.** Put the caption on a solid bar at `#1A1A1A` and white on it measures **17.4:1**, one measurement that holds for every slide and every crop. Choose the scrim only when the photograph has to stay visible behind the words.

### Carousel

- **Measure once per template, then hold it.** Body slides built from one template share one pair, so one measurement covers the deck. Then measure **every slide that breaks the template**, because that is the one that fails: a quote over a photograph, a final call to action in the accent, a slide that inverts to a dark field.
- **A call to action drawn on a slide is a graphic, not a control.** SC 1.4.11 does not apply to it, because there is nothing to click. Its text still owes the text floor at its delivered size, and the boundary test still earns its place, because a call to action that does not read as one does not get acted on.
- **Progress dots and slide numbers.** If a reader needs them to know where they are in the deck, they are parts of a graphic required to understand the content and owe 3:1. If they are decoration, they have no floor and should look like decoration, which means they should not be competing with anything.
- **Never rely on the app's background as one side of a pair.** Put the slide's own background inside the 1080 x 1350 frame. The surrounding field may be light or dark on the same day on the same device, and a pair measured against one of them is unmeasured against the other.

## Checklist

Measurement
- [ ] Every pair measured, with its role named
- [ ] Delivered size computed for every text pair, by dividing canvas pixels by the downscale factor
- [ ] Normal text at 4.5:1 or better, body text aiming at 7:1
- [ ] Large-scale text, 18 point or 14 point bold as delivered, at 3:1 or better
- [ ] Control boundaries and meaningful graphic parts at 3:1 or better
- [ ] No pair within 0.2 of its floor
- [ ] Both sides of every pair specified

Robustness
- [ ] Distinctions survive the greyscale test
- [ ] Every colour-carried distinction has a named second carrier
- [ ] Text over imagery on a field or on a measured scrim, verified at the worst patch
- [ ] Type weight heavy enough to survive recompression
- [ ] Nothing depends on the app's own background colour
- [ ] Inverted variant measured separately, pair by pair

Delivery
- [ ] Read at delivery size on the target device, and at thumbnail scale
- [ ] Every figure confirmed against the current specification before being quoted
- [ ] Criterion number, level, floor, measured ratio and margin in the report

## The ultimate test

Export at the real delivery specification, open it on a phone, hold it at arm's length in ordinary daylight, and read the smallest piece of text out loud. Then measure the worst pair in the file. **A piece passes only if both hold.**

- **Reads fine, number fails.** Usually large text relying on a size the export downscaled it out of, or a pair measured against the wrong background. Fix the number: your own eyes, on your own screen, in your own light, are not the reader you are designing for.
- **Number passes, does not read.** The model's known gaps are showing, through thin strokes, light text on dark, or a pair sitting on its floor. Raise the margin and add weight.
- **Both fail.** Hue was doing the work. Move luminance.
- **Both pass.** Say so with the numbers, and name the criterion, the level and the margin.

Where you can, hand the piece to someone wearing glasses they have not updated, in a room you did not choose, and watch where they stop.

## Where this skill should lose

**When contrast is expressing rank rather than clearing a floor.** Use `dsn-hierarchy`, which decides what reads first, second and third and how much separation each level needs. This skill will tell you a pair conforms and say nothing about whether the right thing is loudest. A frame can pass every test here and still have two elements fighting for first look.

**When the question is which colours exist at all.** Use `dsn-palette`, which builds the set: how many colours there are, which hues, and what each slot is for. This skill never adds or removes a colour. It evaluates a pair you already have, and its one move is to shift one colour's luminance. If the fix keeps coming out as "darken it" and the brand will not allow that, the problem is upstream in the set.

**When the question is how a colour behaves next to another one.** Use `dsn-color`, which owns the relational and appearance decisions: what each colour is doing in the piece, and simultaneous contrast, the effect where one colour looks lighter against a dark surround than it does against a light one, so the same grey can read as two different greys in one frame. The ratio is blind to all of that, because it reads two values in isolation and returns the same number whatever surrounds them. This file owns measurable conformance only: a pair either clears its floor or it does not. A piece can clear every floor here and still be full of colours that misbehave against their neighbours.

**When the text is too small or too tightly set rather than too pale.** Use the skill that sets size, leading and measure, `dsn-typeset`. A pair at 9:1 is still unreadable at six words to the line, and this file will report a pass.

**When the choice is which photograph to use, or how to treat one.** Use `dsn-image`. This skill tells you a photograph's highlight is eating a caption and offers a field or a scrim. It does not tell you the photograph is wrong for the piece.

**When the audit is about accessibility beyond contrast.** Focus order, semantic headings, alternative text, keyboard navigation, screen reader behaviour, minimum touch target size and a reader's ability to override your type sizes and spacing are all out of scope here by design, and a contrast pass reported as an accessibility pass is a misleading result. They are also out of scope everywhere else in this plugin, so when a neighbour says accessibility belongs here, it means the measured contrast floor and nothing more. Use a wider accessibility review, from a source outside these files.

**One rule that governs every boundary above.** This is the file every other skill sends a pair of values to, and it sends nothing back except a number and a verdict. It never chooses a colour, a size, a rank, a position or a picture. Hand it two values and the rendered size of the text, and it returns the ratio, the threshold that applies and a pass or fail, and the only repair it offers is to move one of the two values' luminance. So when the only fix that clears the floor is one the brand or the layout will not permit, stop here: the decision belongs to whichever file owns the value you are not allowed to move, which is `dsn-palette` for a brand colour, `dsn-typeset` for a size, and `dsn-image` for what sits behind the text.

That rule settles a handful of pairs this file is sent from and says nothing about on its own, so take them all the same way. A frame weighted for stability sends a tonal value here and gets a legibility verdict back, and that verdict wins over the weight effect, because a frame nobody can read is not balanced, it is unread. A mark checked on a light and a dark ground, an icon stroke against its background, a seam element rendered small on a carousel frame, and a pair of tokens recorded with a ratio are all the same operation: two values in, one verdict out. In every one of those cases this file confirms or refuses the pair and never touches the drawing, the stroke spec, the frame order or the name. One case is genuinely unaddressed here rather than delegated: the minimum contrast a thin icon stroke needs against a dark ground is a figure no file in this plugin carries, so measure the pair and treat the published non-text floor as the best available answer.

**When the subject is a data graphic.** SC 1.4.11 sets a floor for parts of a graphic required to understand the content and says nothing about encoding: which hues to assign to which series, how many stay distinguishable, or whether a sequential scale reads in order. Use dedicated data visualisation guidance for the encoding and come back here for the floor.

## What an agent can run, and what it cannot

**Can run mechanically:** every ratio from hex values, using the formula in the terms section; the delivered-size division; the role table lookup; greyscale conversion; worst-patch sampling given the image and the text bounds; scrim opacity derivation given the lightest pixel and the target floor; every checklist item that is a number; and fetching the current specification to confirm a figure.

**Needs a human:** the delivery-size read and the recital, because both ask what a person perceived rather than what a value computes to; whether a control is already identified by its position and context under SC 1.4.11, which competent auditors decide differently; and whether an element is decoration or information, which depends on the brief rather than on the file.

**Agent defaults to override explicitly.** A model asked about contrast recites remembered figures confidently, and these are exactly the figures that drift, so the standing instruction is **look the threshold up, do not recall it.** A model also reports a technical pass as a success, so require it to report ratio, floor and margin together, which makes 4.6:1 read as the marginal result it is rather than as a pass. And a model will write a ratio in whichever order it was given; require the lighter luminance first every time.

## Writing the output

Plain words and full sentences. Report in this order: the pair, what it carries, the delivered size, the measured ratio, the criterion and level, the floor, the verdict, the margin. "The caption is `#8A8A8A` on `#FFFFFF` at 3.45:1. It is normal text at 12 point delivered, so SC 1.4.3 AA sets the floor at 4.5:1. It fails by 1.05, and `#717171` clears it at 4.88:1." Not "the caption feels light."

Name the criterion and the level with every verdict, because the bare figure is the thing that gets misquoted, and say which version of the specification you checked and when. Where a recommendation is derived rather than drawn from the specification, say so in the same sentence; that covers everything in the imagery and carousel sections, and the margin check. An APCA value is neither normative nor conformance, so say so whenever you quote one.

Sources, verification dates, the recorded disagreement and its decision rule, and what these sources do not cover are in `references/provenance.md`.
