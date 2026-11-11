---
name: dsn-typeface
description: Picking a typeface, auditing a font choice already made, deciding whether one family is enough, or pairing two faces. Gives a constraint sheet and a rejected shortlist.
---

# Choosing and pairing typefaces

This skill decides which typefaces a project uses. It covers the work that happens before a size is set: listing what the type has to survive, rejecting faces that cannot survive it, pairing what is left or deciding one family is enough, and auditing a choice someone else made. The single idea underneath it is that choosing a typeface is a constraint-satisfaction problem rather than a taste problem. Write down what the type has to survive, use that list to reject, then spend taste on the handful that remain. Done the other way round the constraints still arrive, just later and as a redesign: the headline face cannot set a caption, the licence does not cover a client, the language set has no accents, the thin weight disappears when the platform compresses the image.

## What this skill is for

Use it to:

- pick the typefaces for a brand, a deck, a site or a body of posts
- say why a font choice fails, in terms someone can act on
- pair two faces, or decide one family is enough
- set the role list and the weights a project needs before anyone opens a font menu
- audit a type choice you did not make, including one a model produced

## Confidence

The rules here are practitioner accounts of how working designers select type, not measured findings. No reader was tested for any claim in this file, and where a rule sounds like a fact about legibility it is usually a fact about a letterform plus a plausible inference about reading. Rules marked **(thin)** rest on a single source and should be treated as one person's house style: use them, and check them against the actual piece rather than citing them.

Every pixel figure in the applied section is computed here from the canvas assumptions rather than taken from anywhere, so it is reproducible but not evidence, and the arithmetic is shown so you can redo it with different assumptions.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

Design vocabulary is the main thing that makes type advice unreadable. These are the only terms this file needs.

**Slot.** One role type plays in a design, with its own smallest size and its own longest run: display, heading, subheading, body, caption, label, numerals, interface. A project has slots before it has fonts.

**Typeface and font.** The typeface is the design, the font is the file. "Two typefaces, six fonts" means two designs shipped as six weight and width files.

**Em and point size.** Type size is the height of an invisible box, the em, not the height of any letter in it. Two faces set at the same size can look wildly different in size, which is the root of most pairing trouble.

**Cap height.** Height of a capital letter, measured from the baseline, the invisible line letters sit on.

**x-height.** Height of a lowercase `x`, from the baseline. Stated as a fraction of the em, it runs from roughly 0.44 on an old-style serif to roughly 0.55 on a modern humanist sans. At small sizes a taller x-height puts more of each letter above the baseline and so leaves more of the letter visible, which is why x-height matters more than point size for whether small text reads. **(thin)** The mechanism is the whole of the argument here; nothing measures it.

**Aperture.** The size of the gap where a letter's curve stops short of closing, in `c`, `e`, `s`, `a`. Open apertures keep those letters distinct from `o`; closed apertures turn them into variations on a circle at small size.

**Counter.** The enclosed or partly enclosed white space inside a letter: the hole in `o`, the bowl of `b`, the two in `g`. Small counters fill in when an image is compressed or printed at size.

**Stroke contrast.** The difference in thickness between a letter's thick and thin strokes. A grotesque sans has almost none; a modern serif has extreme contrast, with hairline thins that vanish first at small size and under compression.

**Character width.** How wide a letter is relative to its height. Narrow faces fit more characters per line and lose distinction between letters sooner.

**Measure.** The length of a line of text, counted in characters rather than in pixels, because what tires a reader is how far the eye travels before it has to find the next line.

**Leading.** The vertical distance from one baseline to the next. Set in this skill's sibling, not here.

**Tracking.** Uniform extra space added between every letter in a run.

**Glyph.** One drawn character in a font file. A font with no `ñ` has no glyph for it, and the application silently substitutes the character from some other face, mid-word.

**Tabular numerals.** Digits all drawn to the same width so columns of numbers line up. The alternative, proportional numerals, makes a price table ragged.

**Drawn italic versus slant.** A drawn italic is a separately designed set of letterforms, often with different skeletons: a single-storey `a`, an entry stroke on `n`. A slant, also called a faked or algorithmic oblique, is the roman letters tipped over by the application. On a sans the difference is often tolerable. On a serif a slant shears the serifs and the stress of the curves, and it reads as broken.

**Variable font.** One file carrying a continuous range along an axis, usually weight or width, in place of several static files. Relevant to shipping weight on the web, irrelevant to an exported image.

**Subsetting.** Shipping only the glyphs a page actually uses, which cuts file weight. Breaks if content later introduces a character that was cut.

**Structure, or skeleton.** The underlying construction of a letter, independent of its details: where the stress falls, whether the `o` is a circle or an oval, whether the terminals are straight cuts or angled. Structure is what a reader perceives as "a different kind of letter". Two faces with the same skeleton and different details read as the same face drawn twice.

**The categories, as behaviour rather than as history.** A category name is useful because it predicts how a face behaves at size, which is mechanical, and much less useful as a prediction about what a reader feels.

- **Old style** serif, such as Garamond: low stroke contrast, small x-height, angled stress. Holds together small, looks dated large if nothing else is modern.
- **Transitional** serif, such as Baskerville or Caslon: moderate contrast, vertical stress. The default text serif.
- **Modern** serif, such as Bodoni: extreme contrast with hairline thins. Dies at small size and under compression.
- **Slab** serif: serifs as thick as the strokes. Short runs only.
- **Grotesque and neo-grotesque** sans, such as Helvetica: near-uniform stroke, closed apertures, tight spacing. Bought its neutrality with those closed apertures, so it loses letter distinction small.
- **Humanist** sans: open apertures, some calligraphic stress, usually a tall x-height. The category that survives smallest.
- **Geometric** sans, such as Futura: circular bowls, uniform stroke. Reads clean large, and small its `c`, `e`, `o` and `a` converge on the same circle.
- **Mono**, such as Courier or JetBrains Mono: every character the same width. For code, data and deliberate effect.
- **Script and display**: drawn for a few words at size. No body text, ever.

## The principles

Each rule names the test that checks it. The tests are in the table below.

1. **Fill the constraint sheet before you think about mood.** Mood narrows thousands of faces to hundreds and cannot narrow further, because it has no reject condition in it. The survival list narrows hundreds to about a dozen mechanically, since each item on it is a fact that is either true of a face or false. Checked by the **constraint sheet** test.

2. **Specify slots, not fonts.** Each slot carries its own smallest size and its own longest run, and those two numbers are what reject faces. A font list longer than the slot list is shopping rather than selection. Checked by the **slot count** test.

3. **The smallest size in the project decides more than the brief does.** A face that fails at caption size is rejected however well it answers the mood, because the caption still has to be read and the headline can be solved a dozen other ways. Long runs need ordinary proportions and ordinary stroke weight, which is the mechanical reason display faces cannot carry them: their distinguishing features are exactly the ones that stop working when repeated for thirty words. Checked by the **small-size render** test.

4. **Reject mechanically, choose by taste, in that order.** Taste is real and it is the last step, applied only to survivors. If nothing was ruled out by a rule, you produced a preference list wearing the costume of a process, and the rejections are where the information is. Checked by the **rejection list** test.

5. **Pairing is one problem on two axes: maximise structural distance, minimise proportional distance.** Differ in skeleton by enough that no reader could read the difference as an accident, agree in x-height and character width by enough that the two sit on a line without one looking oversized. Checked by the **mistake** test, then the **x-height match** test.

6. **One family until a second earns its place.** Weight and width inside one well-drawn family cover most hierarchy, and a second family adds a distinction the reader has to decode on top of the ones you meant. Checked by the **second-family justification** test.

7. **Keep a curated go-to list and work from it, not from the library. (thin)** Twenty to sixty faces you already know how to set, grouped by category, so a brief keyword resolves to a shelf rather than to a search. Treat the count as a working range and the mechanism as the rule: selecting from a set you have already set type in is faster and produces fewer surprises than selecting from one you have not. Checked by the **rejection list** test.

8. **Evaluate a candidate by comparison, not in isolation. (thin)** Set the candidate beside the acknowledged classic of its own category, same size, same words. A face seen alone looks like itself; seen next to its category's reference, its actual divergence becomes visible and you can say what you are buying.

9. **Never state a typeface name you cannot verify in the available library.** A confident wrong font name costs more than an admitted gap, because it gets specified, propagated, and discovered at build time.

## How to work

### Mode A: choosing type for a project

1. **Write the slot list:** display, heading, subheading, body, caption, label, numerals, interface. Delete the slots this project does not have. For each surviving slot note two numbers, the smallest size it renders at and the longest continuous run it carries. Do this before any font menu opens, on paper if that helps **(thin)**, since the point is that the numbers exist before the candidates do.

2. **Write the constraint sheet**, one line per item per slot. The items are in the section below.

3. **Reject against the sheet.** Start from the go-to list. Delete anything that fails a hard constraint: licence class, language and glyph coverage, weight range, smallest-size legibility, file weight. Most of the list should go, and every deletion should have a nameable reason. A sheet that rejects nothing is a sheet that was filled in after the choice.

4. **Only now bring in mood.** Pull keywords off the brief: playful or serious, restrained or expressive, familiar or strange. Use them to rank survivors. Never use them to find new candidates, because a candidate found by mood has not been through step 3.

5. **Look for one upgrade.** Ask what your default choice cannot do, then look for exactly that with a search filter rather than by scrolling. Rank sources by signal: an independent foundry whose faces you have shipped, then a paid library, then a filtered free library, then a recommendation list. Discard any list where a third of the picks look wrong to you, because that tells you the list's selection criteria are not yours.

6. **Set the pair, or decide one family is enough.** The section below. Choose one face first and find its partner, rather than hunting for a pair as a unit. **(thin)** Hunting for pairs is how you end up with a vendor's duo instead of a decision.

7. **Assign faces to slots and fix the weight per slot.** This is where selection ends: every slot names its face, its weight and its case. The sizes, the scale ratio, the leading, the tracking and the final measure are a separate job and belong to the skill that sets type. Hand over a slot table, not a mood board.

8. **Test at the real size in the real medium.** Real copy, never lorem ipsum, since placeholder Latin has no `ñ`, no numerals, no awkward ascender collisions and no long words. Set a paragraph, a caption and a headline, export at the delivery size, open it on a phone, print it if it prints.

9. Run the checklist and the ultimate test.

### Mode B: judging a font choice that exists

1. Ask for the constraint sheet and the slot list. If neither exists, reconstruct them from the artefact and say in the report that they are reconstructed, because a reconstructed sheet can show what fails but cannot show what was rejected, and a process with no rejections is the finding.
2. Run the small-size render on every slot, smallest first.
3. Check the hard constraints as facts rather than as impressions: licence class against actual use, glyph table against every language that ships, available weights and widths against the scale in the file, file weight against the medium.
4. Run the mistake test and the x-height match on every pairing.
5. Count typefaces, display faces, weights and slots, then run the anti-pattern list.
6. Report what passes, what fails, and the smallest change that fixes each failure, ordered by impact. A failed hard constraint outranks every aesthetic finding, because a licence failure or a missing glyph is a defect and a mood mismatch is a preference.

## The constraint sheet

One per slot. A blank line is a decision deferred, not a decision absent, so blanks are tracked rather than tolerated.

- **Size range.** The smallest and largest size this slot renders at, in the units of the medium. Not "small". The number.
- **Medium.** Print, screen, feed, projection, signage. A face that works in a PDF at arm's length can die at feed thumbnail size, and the two are the same file.
- **Length.** The longest continuous run. A face can carry three words and fail at thirty, because the features that make it distinctive accumulate.
- **Language and glyphs.** Every language that ships, plus accented characters, currency symbols, maths, fractions and tabular numerals. One missing glyph is a rejection, not a note, since the application substitutes a character from another face mid-word and nobody catches it in review.
- **Weights and widths needed.** Two weights is a working minimum. One weight is a constraint you fight for the life of the project, because every hierarchy decision then has to be made with size, case and space alone.
- **Italics.** Whether this slot needs drawn italics or can live with a slant, and on a serif the answer is drawn.
- **Licence.** Desktop, web, app, broadcast, logo, client transfer, seat counts, pageview tiers. **(thin)** Kept as a hard gate anyway, because it is a legal fact rather than a taste claim, and it is the constraint discovered after launch more often than any other.
- **Performance.** For web only: file weight per shipped weight, whether subsetting is safe given the content, whether one variable font replaces four static files. Decisive for a site, irrelevant to an exported post graphic.
- **Who else touches the file.** A client setting type in a slide tool or a browser-based editor will not have your licensed foundry face installed, so plan the fallback now and name it on the sheet. An unplanned fallback is a different face chosen by the operating system.

## Building the shortlist

**Work from the go-to list, grouped by the categories in the terms section**, because a shelf can be rejected as a unit: "nothing in this piece goes below 36 pixels and the smallest slot is a caption" removes modern serif, geometric sans and every display face in one move, before any individual face is considered.

**Choose on traits that have a mechanism under them, not on category reputation.** The serif-versus-sans legibility question has no agreed evidence behind it, and the honest form of the claim is that serifs are generally believed to help, which is a statement about belief. So decide on the traits instead, each of which you can see in a specimen: x-height relative to cap height, aperture openness, stroke contrast, character width, and whether `l`, `I` and `1` are distinguishable from each other, along with `0` and `O`, and `r` followed by `n` against `m`.

**Category predicts behaviour, not personality.** Advice that maps serif to traditional and sans to contemporary is a shortlist filter and not a prediction about a reader: it is easy to falsify with any current consumer-electronics brand setting its headlines in a short serif precisely to read as new. Use the mapping to order a shortlist if it helps you decide quickly. Do not use it to justify a choice, and never present it as a fact about how the type will be received. The mechanical half of the category, how the face behaves as it gets smaller, is the half that survives scrutiny.

## Pairing

Pairing is the smaller half of the job, and most published advice about it is convention rather than mechanism. Exactly one pairing claim has a mechanism under it, and the rule here follows from that claim alone: a near-match reads as an error. Two faces from the same category, close enough that the difference is small, present the reader with a difference that has no meaning, and a meaningless difference is read as a mistake rather than as emphasis.

**The rule.** Either one family, or two faces far apart in structure and close in proportion.

- **Far apart in structure** means a different skeleton: serif against sans, roman against script, proportional against mono. Not another face in the same category.
- **Close in proportion** means similar x-height relative to cap height, similar character width, and similar stroke weight when both are set at the same size. Where x-heights differ, you must set one slot larger to make the two look equal, which is fine as a deliberate compensation and a bug when it happens by itself.

**The apparent contradiction, resolved.** Advice says faces should be distinct and also complementary, which sounds like one requirement cancelling the other. It is two requirements on two different axes. Structure wants distance so the difference is legible as intentional. Proportion wants agreement so neither face looks mis-sized next to the other. Both can be satisfied at once, so there is nothing to trade off. Resolving it on shared mood or shared period instead, which is the common move, replaces a checkable requirement with a proxy and leaves the proportion axis unmeasured except for x-height.

**The safe default is one family**: two weights, or a width and a weight. **(thin)** Keep the two weights at least two steps apart on the family's own weight ladder, regular to semibold rather than regular to medium, on the reasoning that one step reads as inconsistency rather than as difference. Verify the step at the smallest size the pair appears at: a step visible at heading size can disappear at caption size, and then you have two weights doing one job.

**One decorative or display face per layout, maximum. (thin)** Use it for headlines, a large numeral, or a graphic element, and nowhere else. The commonly stated alternative is a vague "not too many", which gives you nothing to check, so the cap here is one.

**Two or three typefaces per layout is the cap.** This is the most widely repeated claim in the field and the one with the least mechanism attached, since the reason usually given is that more looks confusing or messy. The defensible restatement: every additional typeface is another distinction the reader has to decode, so the real cap is on meaningful distinctions and therefore on slots, not on files. Four weights of one family can break this rule while two typefaces do not.

### Pairing rules that do not work

Each is a proxy standing in for a mechanism, and each fails often enough to be unusable as a rule.

- **"Opposites attract."** Contrast is necessary and not sufficient. A monospace and a formal script are about as opposite as two faces get and they do not work together. Replace it with structural distance plus an explicit proportion check.
- **Pair faces by the same designer.** The reasoning is that a designer has a consistent style. Sometimes true, and silent on the only thing you needed to know, whether the two agree in x-height and width.
- **Pair faces from the same era.** The strongest of the four, because it does carry a mechanism underneath it, shared mood. Still a proxy: faces drawn in one period often share a width and a contrast model, and that sharing is the reason they work, not the date. A 1920s geometric sans and a 1920s art-deco display face are contemporaries and share nothing a line needs. Check the proportions directly and the era stops mattering.
- **Buy a font duo, or follow a vendor's pairing list.** The vendors recommending duos sell them, so the recommendation is a commercial interest rather than evidence. A duo is a shortcut past a check that takes one minute.
- **Trust your gut.** Not a rule. It is the name for having already internalised the checks, which means it works for the person who no longer needs it.

## Tests

Each returns a verdict decidable from this file alone, by someone holding the specimen, the font file and one exported render.

| Test | Catches | Verdict |
|---|---|---|
| **1. Constraint sheet** | A mood choice a hard constraint will overturn | Read the sheet before any font opens. Fail on any blank. Stop work, rather than proceeding provisionally, if the blank is licence or glyph coverage. |
| **2. Slot count** | Shopping dressed as selection | Count slots, then count typefaces. Fail if typefaces exceed slots. Fail if any typeface cannot be assigned a slot it alone serves. |
| **3. Small-size render** | Faces chosen at 200pt in a font menu | Set real copy at the slot's smallest size, export at delivery size and compression, open it on the target device at arm's length, read the smallest line aloud. Fail if you lean in, squint, or re-read any word. |
| **4. Rejection list** | A process that only ever added candidates | Ask which faces were ruled out and by which sheet line. Fail if the list is empty. Fail if any entry names a preference rather than a sheet line. |
| **5. Mistake** | The near-match pairing | Show the two faces in the piece to someone who did not make it and ask whether two fonts were used by accident. Fail on any yes, and fix it by changing one face's category, never by changing its weight. |
| **6. X-height match** | A pair that needs size compensation nobody applied | Set both faces at the same size on the same line with the same words. Fail if one lowercase run is visibly taller than the other and no compensation is recorded in the slot table. |
| **7. Second-family justification** | A second typeface doing a job one family already does | Name what the second face does that no weight, width or case of the first can. Fail on no answer, and collapse to one family. |
| **8. Ambiguity** | Lost character distinction, worst in data | Set `Il1`, `0O` and `rn` at the smallest slot size, rendered. Fail if any pair is hard to separate, and reject the face for prices, codes, URLs and captions. |
| **9. Glyph table** | A silent mid-word substitution | Open the font's full character set, not the marketing specimen, and check it against every language and symbol the project ships. Fail on one missing glyph. |
| **10. Compression** | Thin strokes and tight counters destroyed in delivery | Export at the platform's real compression and inspect the thinnest stroke and the smallest counter at rendered size. Fail if a stroke breaks up or a counter fills in, and fix with a heavier weight or a lower-contrast face. |
| **11. Stretch** | Type distorted by the application | Compare the set text against the family's own condensed or extended cut. Fail if vertical and horizontal stroke weights differ from each other in a way the real cut does not show. Reset to 100 percent and use a drawn width. |
| **12. Weight-step** | Two weights reading as one | Render the two chosen weights side by side at the smallest size either appears at. Fail if you cannot tell them apart at that size. |
| **13. Crop** | Type lost to a platform crop, and the branching diagnosis | The ultimate test, below. |

## Anti-patterns

- **Font chosen first, constraints discovered later.** The broad failure every other one descends from, and usually the result of scrolling a font menu until patience ran out. Fix: write the sheet, filter by category and weight count, and accept that the face you liked may not survive it.
- **Display face in a body slot.** Tight counters, high stroke contrast or strong personality asked to carry a paragraph. Fix: keep it for the headline and put a neutral face underneath. That is the only pairing most pieces need.
- **One weight available.** A regular-only face fighting a four-step hierarchy. Fix: reject it at the sheet stage, or drop weight as a channel entirely and rank by size, case and space.
- **Print figures applied to a screen.** A body-copy range of 8 to 11 points, with 12 called slightly too big, is sound print-book convention, wrong on a phone and badly wrong in a feed. Fix: treat every size figure as belonging to a medium, and re-derive it with the small-size render in the medium you are actually shipping to.
- **Near-match pairing.** Two geometric sans faces, or two transitional serifs, close enough that the difference reads as inconsistency. Fix: change the category of one, not the weight.
- **Type distorted by the application.** Horizontally stretched text, plus faked slants and faked bolds. The mechanism: scaling multiplies one axis and leaves the other, so vertical strokes thicken while horizontals do not, whereas a drawn condensed cut redraws both and keeps them in proportion. The same applies to a faked bold, which grows the strokes into the counters instead of redrawing the letter. Fix: real widths, real cuts, or move the emphasis to case or colour.
- **Licence mismatch.** A personal-use face in client work, or a desktop licence on a shipped web font. Fix: swap before launch, not after, because the swap changes character widths and therefore every line break in the layout.
- **Hairline weights in a feed.** A thin or ultralight weight at small size, erased by compression. Fix: raise the weight until it survives test 10.
- **Four weights reading as four fonts.** Light, regular, semibold and black in one piece, so no step carries meaning. Fix: cut to two, and move the rest of the hierarchy into size and space.
- **Lorem ipsum as the test string.** Placeholder Latin has no accents, no numerals, no long compound words and no awkward ascender collisions, so it hides exactly the failures the sheet was written to catch. Fix: test with the real copy, or with the worst real copy you can find.

## Applied to a post visual or carousel

The output is read on a phone, in a feed, usually at 4:5. Canvas sizes and the downscale factor are fixed in `reference/canvas-assumptions.md`: square posts are 1080 by 1080, portrait posts and carousel slides are 1080 by 1350, and a 1080-wide asset lands in a feed column of roughly 360 device-independent pixels, which is a 3x downscale, with 4x as the stress case. Everything below is computed from those numbers.

**The floor, computed.** The smallest size you can rely on being read on a phone is about 12 points rendered. At the nominal 3x downscale, the authored size that produces it is 12 x 3 = 36 pixels, so nothing in a post graphic is set below 36, captions included. At the 4x stress case, 36 authored renders at 36 / 4 = 9 points, which is under the floor, so a piece that must survive 4x needs 12 x 4 = 48 pixels as its smallest authored size. Use 36 as the floor and 48 as the floor for anything you cannot afford to lose.

**The heading band, computed rather than asserted.** A scale step has to be visible after division by 3, so adjacent named steps need enough separation to read as different sizes once rendered. Taking 4 points of rendered separation as the minimum visible difference gives 4 x 3 = 12 pixels of authored separation at the bottom of the scale. A 1.125 ratio from a 36-pixel body gives 40.5, which is 13.5 points against 12 rendered, a 1.5-point difference: one level wearing two names. A 1.333 ratio gives a usable ladder: 36, 48, 64, 85, 114, rendering at 12, 16, 21, 28 and 38 points. That puts headings in the 85 to 114 band for a body of 36, and the band moves if you change the body size or the ratio. The ratio itself is not this skill's decision; the skill that builds type scales owns it.

**Pick for the floor, not for the headline.** The caption slot rejects more faces than the headline slot, so run the shortlist against the caption first. At 36 pixels authored, rendered at 12 points, a humanist sans with an x-height near 0.52 of the em and open apertures puts roughly 6.2 points of lowercase on screen and keeps `c`, `e` and `o` distinct. A geometric sans with circular bowls at the same size puts the same height on screen with less distinction between those three letters, because the distinction was never in the height. A modern serif with hairline thins loses the thins first of all, before any letter-distinction question arises.

**Weight floor.** Nothing below regular at body size, nothing below medium at caption size, derived from compression behaviour rather than taken from anywhere: a hairline stroke on a 36-pixel letter is roughly one authored pixel wide, renders at a third of a device pixel, and is the first thing a compression algorithm discards. Hairlines belong to print and large format.

**X-height compensation, computed.** Suppose the chosen heading face has an x-height of 0.52 of the em and the body face has 0.46. At a shared 36 pixels the body face shows 36 x 0.46 = 16.6 pixels of lowercase against the heading face's 36 x 0.52 = 18.7, so the body looks smaller than it is. To match the apparent size, set the body face at 36 x 0.52 / 0.46 = 40.7, so 41 pixels. Record that 41 in the slot table as a compensation with its reason, or the next person will normalise it back to 36 and the pair will look wrong again.

**Measure, computed.** On a 1080-wide canvas with 80-pixel side margins the text column is 1080 - 160 = 920 pixels. Average character width for a humanist sans runs near 0.5 of the type size, so at 36-pixel body type a character occupies about 18 pixels and the column holds 920 / 18 = 51 characters. At 48-pixel type a character occupies about 24 pixels and the column holds 920 / 24 = 38 characters. So a feed column holds roughly 35 to 50 characters, against the 45 to 70 print convention **(thin)**, and it cannot reach the top of that convention at any usable size. Two consequences for selection: a wide-set face shortens the line further and should be rejected for the body slot on a narrow canvas, and headlines in this format are broken by hand rather than by the text engine. The final measure and leading are set by the type-setting skill; what this arithmetic is for here is rejecting faces whose character width will not fit the column.

**The 4:5 safe area, computed.** Author at 1080 by 1350 and keep every word inside a centred 1080 by 1080 square. The margin that leaves is (1350 - 1080) / 2 = 135 pixels top and bottom, which is decoration only: background, texture, a rule, never type. This is extrapolation and not a specification, since the canvas assumptions file declines to assume crop behaviour at all, so verify it against one real post before relying on it.

**Carousel cohesion is absolute.** One family across the deck, with identical heading face, size, weight and position on every body slide, and identical body size and measure. The mechanism is sequence: the reader sees the slides one after another in a few seconds, so a face or size that changes between them is read as an error rather than as emphasis, which is the opposite of what the change was for.

**Slide 1 is the only place a display face belongs**, and only if its structure survives the downscale. Check it at 1080 / 3 = 360 wide and again at 270 for the stress case. A display face that is hard to read at 270 is decoration pretending to be a hook.

**One typeface, two weights, is the right default for a body of posts.** The reason is recognition rather than taste: a reader scrolling past the fortieth post should identify the source from the type before reading any words, and that only happens if the type did not change between the first post and the fortieth.

**Worked example.** Before: a 4:5 carousel sets headings in a geometric sans at 96 pixels, body in the same geometric sans regular at 30 pixels, captions in a modern serif at 24 pixels, with a thin weight on slide 1's subtitle and the slide number set 40 pixels from the bottom edge. Diagnosis, computed: body at 30 renders at 30 / 3 = 10 points, below the 12-point floor, so it fails test 3. Captions at 24 render at 8 points, two-thirds of the floor, and the modern serif's hairlines fail test 10 on top of that. The caption face and the body face are both failures of the same kind, chosen at menu size. Headings at 96 and body at 30 are a ratio of 3.2, so hierarchy is not the problem. The thin weight on slide 1 fails the weight floor. The slide number sits 40 pixels from the bottom, inside the 135-pixel crop margin, so it fails test 13. After: one humanist sans for every slot, body at 36, captions at 36 since the reference puts nothing below the floor, headings at 85 to 114 off the 1.333 ladder, caption and subtitle weight raised to medium, the slide number moved to 160 pixels from the bottom edge, which clears the 135-pixel margin with 25 pixels to spare. Two typefaces became one, which also satisfies test 7 by deleting the question.

## Checklist

Constraints
- [ ] Sheet filled per slot, with numbers for size range and longest run
- [ ] Licence class matches the actual use, including client transfer and web
- [ ] Glyph table checked against every language and symbol that ships
- [ ] Weights and widths cover the hierarchy, two weights minimum, drawn italics where a serif needs them

Selection
- [ ] Rejections happened before preferences, each naming a sheet line
- [ ] Smallest slot passes the small-size render in the real medium
- [ ] `Il1`, `0O` and `rn` are separable at the smallest rendered size
- [ ] No display, script or high-contrast face in a body or caption slot

Pairing
- [ ] One family, or two faces far apart in structure and close in proportion
- [ ] Mistake test passes, and any x-height compensation is recorded with its reason
- [ ] One display face maximum, two or three typefaces maximum
- [ ] Every slot names its face, weight and case, and the scale is handed to the type-setting skill

Feed
- [ ] Every slot at or above 36 pixels on a 1080 canvas, captions included, which is the nominal-case floor; at or above 48 pixels if the piece is held to the 4x stress case
- [ ] Nothing below medium weight at caption size
- [ ] All type inside the centred 1080 square of a 4:5 frame
- [ ] Type settings identical across carousel body slides, and the piece survives the compression test

## The ultimate test

Export at the real output size, let the platform compress it, open it on a phone at arm's length, and read the smallest line of type out loud without leaning in. Then crop the frame to a centred square and check that nothing you just read has gone.

If you read it all and nothing was lost to the crop, the type choice holds. If something failed, the diagnosis branches by what failed, and each branch has a different fix:

- **Words you leaned in for**: the size floor is wrong for this face. Raise the size, or move to a face with a taller x-height and more open apertures.
- **Letters you worked out from context rather than read**: closed apertures or ambiguous characters. Change the face, not the size, because size was not the problem.
- **Strokes that broke up, or counters that filled in**: weight or stroke contrast. Raise the weight or drop to a lower-contrast face.
- **Type lost to the crop**: a layout fix, not a type fix. Move it inside the safe area.

Hand the piece to a person and ask them to read the smallest line, if you can. Every other judgement in this file is the designer's own eye on their own work, which is the weakest instrument available for a legibility question. The cheapest substitute is to leave the design for an hour or two, return with fresh eyes, then ask a colleague **(thin)**. A real reader reading the smallest line out loud beats all of it.

## What an agent can run, and what it cannot

**Can run mechanically:** the glyph table check, the weight and width count, the licence class against a stated use, the ambiguity check, file weight, the typeface and display-face counts, the x-height comparison where it can measure a render, every checklist item that is a number, and the full arithmetic in the applied section. It can also export at target size and at the platform's compression, which collapses tests 3 and 10 into one render each.

**Needs a person:** whether the face answers the brief, whether a display face can carry an identity, and the mistake test, which asks what a viewer would assume rather than what a file measures. Taste is not an obstacle to route around. It goes last, and only on survivors.

**Agent defaults to override explicitly.** Asked to choose a typeface, a model returns a mood-matched name drawn from a popularity distribution, usually a free library's top twenty, having checked no constraint at all. The instruction has to be *fill the sheet and reject first, then rank survivors*. And never state a typeface name you cannot verify in the available library, since a confident wrong name gets specified and propagated before anyone discovers the file does not exist.

## Where this skill should lose

**When the face is already chosen and the question is a number.** Use `dsn-typeset`, the skill that sets type: size, scale ratio, leading, tracking and final measure. The boundary is the slot table. This skill ends when every slot names a face, a weight and a case; that skill begins there and owns everything numeric after it. The floors and measures computed above are rejection filters, used to delete faces that cannot survive the smallest slot, not a specification of how the chosen face gets set. Practical version: if the fix is to swap a face or change its category, you are in this file. If the fix is to change a size, a leading value or a tracking value on a face that stays, close this file and open that one.

**When the question is which element the reader should see first.** Use `dsn-hierarchy`. This skill will tell you two weights are too close to read as different; it will not tell you whether the heading or the image should win first look, and it takes the rank order as given.

**When the project needs the chosen faces written down as named values other people apply.** Use `dsn-tokens`. A slot table is the handoff; naming, scales and the rename tests are not this skill's job.

**When the question is what the brand's type should say about it, across every surface and not just this piece.** Use `dsn-identity`. This skill rejects faces on mechanical grounds and deliberately refuses to predict how a category will be received, which is exactly the judgement an identity decision needs.

**When the type is a logo.** Use `dsn-mark`. A wordmark is drawn and optically corrected for one fixed use at many sizes, which is a different problem from choosing a face that must set arbitrary copy it has never seen.

**What nothing here covers**, so you do not look for it in this file: optical sizing and why a text cut differs from the display cut of the same family, hinting and rasterisation differences across operating systems, non-Latin scripts beyond the instruction to check glyph coverage, variable font axes beyond weight and width, and web font loading strategy including fallback metric matching.

Three things look like gaps in this list and are not missing, they are simply owned elsewhere. Type scales and modular ratios are set in `dsn-typeset`, which also computes the smallest size that survives being viewed in a phone feed, so the floors used here as rejection filters have a fuller treatment there. Minimum readable contrast for a text pair is measured in `dsn-contrast`. The rest of accessibility for type, including user font scaling and a reader's ability to override your values, has no owner in this plugin, so if a project needs it, it needs a source outside these files.

## Writing the output

Plain words and full sentences. Name the face, the slot, the size and the test: "the caption face is set at 24 pixels on a 1080 canvas, which renders near 8 points against a 12-point floor, and it failed the small-size render" beats "the small text is hard to read". Give the constraint before the replacement, and give replacements as options, since the right face depends on brief and budget and you are usually not holding both. Put failed hard constraints above aesthetic findings. Show the arithmetic whenever you quote a pixel value, so the reader can redo it with different assumptions. And when a recommendation rests on a single source or on a number derived here rather than measured anywhere, say so in the same sentence as the recommendation, not in a footnote.

Sources, corroboration, disagreements, discarded advice and the full list of derived figures are in `references/provenance.md`.
