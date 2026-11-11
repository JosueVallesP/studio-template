# Audit: dsn-typeface

Independent check of `SKILL.md` against the four transcripts in
`~/research/design-plugin/transcripts/`: `typeface__WTUM2Y11oJo` (Flux),
`typeface__yAuUDyUC-GM` (Envato), `typeface__a4Pj9MAPtuo` (Satori),
`typeface__WrWot89KMoE` (LiteGraphix). All four read in full. Pixel values
checked against `reference/canvas-assumptions.md` at the plugin root.
`references/provenance.md` was read to find the claims under test and was
treated as a suspect, never as evidence.

Counts: 9 mislabelled, 8 unsupported, 9 derived and unlabelled, 27 sourced and
confirmed. Six inline citations, all six resolve to the right source and the
right timestamp. Fixes applied where confident are marked **fixed**.

## The two specific checks requested

**Accused source error 1, the Caslon sans-serif attribution. Real, and the
provenance describes it accurately.** Envato says "the first sans-serif
printing type was developed by william caslen in the 18th century"
[yAuUDyUC-GM 00:10:53]. The usual attribution is William Caslon IV around
1816, so the century is wrong. Two corrections to how the task framed it:
nothing in Envato misclassifies a named typeface as a sans-serif, so "a
sans-serif attribution for a typeface that is not one" is not what is in the
transcript; and the provenance's secondary charge, that dating informal
sans-serif letterforms to "the 5th century bc" [00:10:53] is "garbled", is
weak, since that is a conventional claim about early Greek inscriptional
letterforms and appears in the transcript as a clean sentence.

**Accused source error 2, families and widths. The sentence is real, the
accusation is not.** Envato says font families "don't usually come in
different widths but there are a few famous ones that include a huge variety"
[yAuUDyUC-GM 00:18:47]. That is a defensible generalisation, not an error:
most shipped families carry one width, and Flux treats a width range as a
bonus rather than an expectation, "do you have a range of widths within the
typeface even better" [WTUM2Y11oJo 00:26:48]. The provenance's own gloss
concedes it, "True of many families", while still filing it under "Factual
errors in the sources". Two further problems: the provenance cites it as
[00:19:00], and no such timestamp block exists in the transcript, the sentence
sits in the [00:18:47] block; and the headline claim that the highest-view
source "carries the two clearest factual errors" rests on one real error plus
this one, so it should read as one.

**The five folklore pairing rules. Four of five are fairly characterised, one
is partly strawmanned.**

- "Opposites attract" is asserted with a saying, "They do say opposites
  attract after all" [a4Pj9MAPtuo 00:02:51], and the supporting reason is
  circular, "that works simply because they contrast each other". Fair.
- Same designer is asserted with a style claim and nothing else, "designers
  have a particular style and vision" [yAuUDyUC-GM 00:35:55], immediately
  beside a plug for the vendor's own designers. Fair.
- Font duos are a bare recommendation of the vendor's own product, "try font
  duos at envato elements" [yAuUDyUC-GM 00:36:47]. Fair.
- "Trust your gut" is asserted and then undercut by the same source, "there's
  no exact science as to what form pairings will perfectly work together"
  [yAuUDyUC-GM 00:36:47]. Fair.
- **Same era is partly strawmanned.** It is Flux's rule, not a non-procedural
  source's, and he gives it a mechanism: a monospace with a calligraphic face
  fails because "they just have a completely different mood they're like from a
  different era" [WTUM2Y11oJo 00:37:10], then "maybe fonts that were designed
  in the same time period or have the aesthetic of a certain type period"
  [00:37:58]. Shared mood is a mechanism, and he supports it with a worked
  counterexample. The skill's blanket "Each is a proxy rather than a mechanism"
  does not hold for this one, and the list does not say whose rule it is.

## Mislabelled attributions, most damaging first

1. **"**One decorative or display face per layout, maximum.** Two sources say
   it."** Only Flux states the cap of one: "only one decorative typeface per
   layout" [WTUM2Y11oJo 00:35:35]. LiteGraphix states a different, weaker
   thing: "ensure that you don't use too many display font ... using too many
   display fonts make your work look messy" [WrWot89KMoE 00:09:42], and
   separately "avoid overusing decorative font" [00:16:16]. Neither sentence
   gives a number. Envato and Satori do not state a display-face cap at all.
   The skill promotes a single-source house rule to a corroborated one, which
   matters because its own header tells the reader to treat uncorroborated
   pairing rules with suspicion. **fixed**

2. **"Sources disagree on what categories signal. **Three** map serif to
   traditional and sans to modern and call it type psychology."** One source
   does all of that: Envato maps serifs to "traditional formal practical and
   serious" and sans to "clean minimalistic contemporary and sleek", and frames
   it as "just like there's color psychology there is also psychology for
   typography" [yAuUDyUC-GM 00:31:52, 00:32:42]. LiteGraphix gives half of it,
   serif for "formal, traditional or trustworthy designs" [WrWot89KMoE
   00:05:46], and never maps sans to modern. Satori maps nothing by category;
   it says "Understand how each type face has a personality" [a4Pj9MAPtuo
   00:00:42], which is the general claim, not the serif-to-sans mapping. Count
   of three is wrong, and the decision rule that follows is built on the
   disagreement being three against one. **fixed**

3. **"**The sources** give 45 to 70 characters per line as the print
   convention."** One source gives it: "aim for a number of characters between
   45 and 70" [yAuUDyUC-GM 00:27:12]. No other source in this set states a
   measure in characters at all. **fixed**

4. **"the other three corroborate the constraints and the caps but teach no
   process."** The caps are corroborated by all four, and the italic
   distinction and the legibility traits by Envato. The rest of the constraint
   sheet is Flux alone: licence [WTUM2Y11oJo 00:16:29], glyph and language
   coverage [00:25:10], weight range and width range [00:26:48]. No other
   source mentions licensing, language coverage or glyph sets. Saying the other
   three corroborate "the constraints" overstates the support under the part of
   the skill the header tells the reader to lean hardest on. **fixed**

5. **"Two or three typefaces is the cap all four channels give ... **every
   source** gives the reason as confusion or mess."** The cap is genuinely in
   all four: Flux "never use more than two or three distinct typefaces"
   [WTUM2Y11oJo 00:33:56], Envato "combine only two to three fonts"
   [yAuUDyUC-GM 00:35:08], Satori "keeping fonts down to two, three max"
   [a4Pj9MAPtuo 00:01:25], LiteGraphix "limit font to two or three per design"
   [WrWot89KMoE 00:11:54]. But Satori gives no reason whatsoever, the cap
   arrives as a parenthetical. Three sources give the confusion or mess reason,
   not four. **fixed**

6. **"**Flux names the apparent contradiction himself** ... It resolves on two
   axes: structure wants distance, proportion wants agreement."** The first
   half is exact, Flux says "so it appears there's maybe a contradiction here"
   [WTUM2Y11oJo 00:37:10]. The resolution is the skill's own and is not his.
   Flux resolves it on mood, era and shared anatomy: "think about the overall
   mood maybe fonts that were designed in the same time period" [00:37:58], and
   "you start picking up things like similar x heights or similar features"
   [00:39:27]. Only the x-height half of the skill's "proportion" axis is his.
   Presented as the resolution of a contradiction he named, the sentence reads
   as reporting him, and the skill then files his actual resolution under
   folklore. **fixed** by labelling the resolution derived.

7. **"**Flux adds** that weights sit at least two steps apart ... because one
   step reads as inconsistency rather than difference."** The rule is his, "i
   recommend you go up at least two ways so we've gone from regular to medium
   to semi bold" [WTUM2Y11oJo 00:32:29]. The reason he gives is bare proximity,
   "a medium and a regular a light and irregular can be a little bit too
   close". "Reads as inconsistency" is the skill's mechanism borrowed from its
   own near-match argument and attributed to him in the same sentence.

8. **"The serif-versus-sans legibility question is unsettled, and one source
   says so."** The quoted hedge is real at the cited timestamp but the full
   phrase is "serifs or lack of serifs are generally believed to enhance
   legibility" [yAuUDyUC-GM 00:23:50], which hedges in both directions rather
   than hedging about serifs. The same source asserts the unhedged version
   twice elsewhere, "serifs help the reader follow the letter forms easily
   making them highly legible" [00:08:00] and "serif fonts are great as body
   copy because they are extremely legible" [00:31:52]. Envato's position is
   the assertion; the hedge is one sentence inside it.

9. **"Flux's last step is this and nothing else, and it is the only one
   producing evidence."** Step five is broader than the stated test: he also
   says "throw it you know onto some posters", "print it out", "try it in
   different sorts of digital layouts" [WTUM2Y11oJo 00:43:58]. The phone
   export is one item in his list, not the whole step. Minor, and the direction
   of the claim is right.

## Unsupported, including figures absent from canvas-assumptions.md

1. **"On a 1080 by 1350 canvas a phone feed renders near 400 to 500 pixels
   wide, so authored type shows at roughly 40 percent."** No source discusses
   platform rendering at all, which the skill says. The problem is the plugin's
   own reference: `reference/canvas-assumptions.md` fixes the feed column at
   "roughly 360" device-independent pixels and the downscale at 3x, that is 33
   percent, with a 4x stress test. 400 to 500 and 40 percent appear in no other
   file in the plugin, and the reference exists specifically so these numbers
   do not drift. Every floor below inherits the discrepancy. **fixed**

2. **"captions and sources no smaller than 30."** At the shared 3x this renders
   at 10 effective pixels, under the 12 the reference relies on, and under the
   36 working-file floor the reference states as absolute: "Nothing in a post
   graphic goes below it." `dsn-typeset` reaches the opposite conclusion from
   the same assumption, "there is no caption level on this canvas". **fixed**

3. **"headings 90 to 140."** Not derivable from the stated ratio, not in any
   source, not in the reference. Presented inside a sentence that labels the
   figures derived from the 40 percent ratio, but the ratio yields no ceiling.
   **fixed** by relabelling it a construction.

4. **"**Weight floor.** Nothing below regular at body size, nothing below
   medium at caption size."** No source names a weight floor. Envato comes
   nearest with a legibility trait, "very light or heavy weights are extremely
   hard to read" [yAuUDyUC-GM 00:23:00], which is not a floor by slot. The
   provenance concedes the derivation; the skill states it flat. **fixed**

5. **"The outer 135 pixels top and bottom are decoration only."** The
   arithmetic is right, 1350 minus 1080 is 270 and half is 135. The premise is
   not available: the reference explicitly refuses to assume crop behaviour,
   "Treat any crop-safe margin as extrapolation, not as a specification." The
   skill states the crop as a fact, "because the grid thumbnail crops top and
   bottom". **fixed** by marking it extrapolation.

6. **"**Performance.** For web: file weight per shipped weight, subsetting,
   whether one variable font replaces four static files."** No source mentions
   file weight, subsetting or loading. Flux mentions variable fonts only as
   more options [WTUM2Y11oJo 00:26:48], Envato only as a file format
   [yAuUDyUC-GM 00:21:19].

7. **"[Licence] is the constraint found after launch most often."** A frequency
   claim with no source and no way to check it. Flux gives licensing weight as
   legal and ethical, "it's a legal issue it's also an ethical issue"
   [WTUM2Y11oJo 00:16:29], and says nothing about when it is discovered.

8. **"A client setting type in Canva or Slides will break a licensed foundry
   face."** No source discusses handoff, Canva or Slides.

## Derived but not labelled as derived

Reasonable inferences, none stated by any source, none currently marked. Listed
because the skill's own writing rule is to say so in the same sentence.

1. The constraint sheet as a per-slot artefact. Flux supplies the items as
   questions in prose [WTUM2Y11oJo 00:25:10 to 00:26:48]; the sheet, the
   per-slot structure and the stop-on-blank verdict are assembled here.
2. The ambiguity set. Flux gives `l`, `I` and `1` as an objective fact,
   "the lowercase l and the uppercase i and the one numeral are different
   characters instead of just lines" [WTUM2Y11oJo 00:24:20]. `0O` and `rn` are
   added here.
3. The compression test. No source mentions platform recompression.
4. "aim for 35 to 50" characters at feed size. A scaling of Envato's print
   band, and the scaling factor is the disputed 40 percent. **fixed** to read
   as derived.
5. The failure ordering in "Pick for the floor": which category loses letter
   distinction first and that a modern serif loses its thins "first of all".
   The category behaviours are Envato's [yAuUDyUC-GM 00:11:53, 00:12:53,
   00:16:25]; the ranking is not.
6. "One typeface, two weights, is the right default for a body of posts"
   and its recognition-across-forty-posts reason. The single-family default is
   in all four sources; the reason is this skill's.
7. The crop test diagnoses in "The ultimate test", which map four failure modes
   to four fixes. No source branches a diagnosis.
8. Mode B as a procedure. No source judges existing type.
9. The agent-default warnings. Not a claim about typefaces, and out of the
   sources' scope entirely.

## Sourced and confirmed

Spot list, every one checked in the transcript at the stated place.

- Body copy needs ordinary proportions, "it's important to stick to typefaces
  with classic features and proportions" [WTUM2Y11oJo 00:05:55], with the
  failure modes named, "super wide typefaces or very thin or ones with weird
  features that don't reduce very well at small sizes". Citation in the skill
  resolves.
- The near-match clash, "it's like a clash it's like a color clash"
  [WTUM2Y11oJo 00:34:46], over Poppins, Century Gothic and Futura, which are
  geometric, so the skill's gloss is accurate. Citation resolves.
- Envato's matching claim, "avoid mixing fonts from the same category that look
  alike this can look like a mistake" [yAuUDyUC-GM 00:35:55].
- Print body sizes, "normal body copy text size should be set between 8 points
  to 11 points 12 points tend to be a little bit too big" [yAuUDyUC-GM
  00:25:34]. Citation resolves, quote exact.
- The go-to list of twenty to sixty, "you've got 20 40 60 maybe"
  [WTUM2Y11oJo 00:05:07], built on the Vignelli canon [00:03:34], and the time
  saving, "it just saves so much time" [00:05:55].
- Flux's worked case against category psychology: the current phone whose
  headline "that's actually a serif" with "quite tall x height"
  [WTUM2Y11oJo 00:10:59 to 00:11:40].
- Drawn italics against a slant, in both sources: "italics are separately
  designed uh characters" [WTUM2Y11oJo 00:25:57]; "true italics are angle type
  faces strongly influenced by calligraphy ... oblique fonts ... can look like
  they're a roman character with a slight slant" [yAuUDyUC-GM 00:17:54 to
  00:18:47].
- Two weights as the working minimum, "if you've just got one weight that's
  limiting if you have regular and bold it's better than one" [WTUM2Y11oJo
  00:25:57].
- Category behaviour: neo-grotesque neutrality bought with closed apertures
  [yAuUDyUC-GM 00:11:53]; humanist "wide aperture on letters like a and s to
  improve legibility" [00:11:53]; geometric and slab excepted from small-size
  legibility [00:16:25]; modern serif thins "challenging to read" [00:23:50].
- The legibility trait list: x-height, character width, weight, design traits,
  stroke contrast, counters [yAuUDyUC-GM 00:23:00 to 00:24:46].
- Source ranking by signal and the recommendation-list filter, "if they
  recommend 10 fonts and straight away you're looking you think three or four
  of them are pretty ugly then maybe don't take their recommendations"
  [WTUM2Y11oJo 00:28:15].
- Role-first opening, "where is the type face going to be on your design
  itself" [a4Pj9MAPtuo 00:00:00], and the paper brief before the computer
  [WTUM2Y11oJo 00:02:52].
- The fresh-eyes review, "leaving your design for 1 to 2 hours and then return
  with fresh eyes" [a4Pj9MAPtuo 00:06:54] and "ask a friend or a colleague"
  [00:07:34]. The skill's claim that no source tests on a reader holds; Flux
  also says "you can always ask a friend" [WTUM2Y11oJo 00:28:15].
- Stretching named without a mechanism, "don't stretch font. It kills
  professionality" [WrWot89KMoE 00:13:20], and the skill supplies the
  mechanism and labels that it does.
- Real-copy testing on the device, "set some paragraphs out make it small make
  it big look at it on your phone" [WTUM2Y11oJo 00:28:58] and "test it out on
  your phone you know do that figma prototype" [00:43:58].

## Typeface names

Rule in the skill is sound and is followed: it names almost no faces. Two name
problems worth recording, both in the provenance rather than the skill.

- The provenance lists "the ditto family" as a confident reading of Bodoni
  [yAuUDyUC-GM 00:02:58]. In context it is the Didot family, which is the
  phrase that fits "designed one of the first modern serifs", and Didot and
  Bodoni are different foundries. Not confident either way, so it should sit in
  the uncertain list.
- "Laura" in LiteGraphix's script-font list [WrWot89KMoE 00:07:18] is read as
  Lora in the provenance, and Lora is a serif, not a script, so either the
  reading or the source's category is wrong. Flagged, unresolved. The skill
  uses neither name.

Names the skill itself states: none that I cannot verify, because it states
none.
