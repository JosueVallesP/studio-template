# dsn-spacing: independent audit

Checked against the four transcripts in `~/research/design-plugin/transcripts/`
(`spacing__1cZBMrdSZUA`, `spacing__3QJKOWTRuE4`, `spacing__FDFD2-poyGw`,
`spacing__zyHjG6Szt5g`) and against `reference/canvas-assumptions.md`. The
provenance file was read for context only and was not treated as evidence, since
it was written by the same agent that wrote the skill.

Counts: 5 mislabelled, 1 misplaced citation, 11 unsupported, 7 derived and
unlabelled, 4 arithmetic errors. Fixes applied where the brief allowed. Nothing
was restructured or deleted.

Overall this skill is more honest than `dsn-grid` about its own sourcing. Its
six inline citations nearly all resolve exactly, it says outright that the one
idea is unsourced, and the applied section announces itself as construction. The
damage here is concentrated in the arithmetic and in the sentence claiming the
pixel values come from the shared canvas file.

## Arithmetic errors

**A1. "a 4px gap is a quarter of a rendered pixel" is off by a factor of five.**
At the 3x downscale in `reference/canvas-assumptions.md`, 4px renders at about
1.33px, not 0.25px. A quarter of a pixel would need a 16x downscale. The
conclusion (raise the base) survives, but the figure presented as the proof does
not. **Fixed to about 1.3px.**

**A2. "shown roughly 400px wide in a feed" contradicts the file it cites.**
`canvas-assumptions.md` puts the feed column "in the region of 360pt" and sets
the nominal downscale at 3x on that basis. 400 would make the factor 2.7x.
**Fixed to 360.**

**A3. "Text column capped at 860" does not follow from the reading margin above
it.** The same block sets the reading margin at 108 per edge, which leaves
1080 - (2 x 108) = 864. 860 matches nothing in the skill, the sources or the
shared file. **Fixed to 864, which is the value its own reading margin implies.**

**A4. "Base step 16, doubling" describes only the first four steps.**
16, 32, 64, 128 doubles. 128 to 192 is 1.5x and 192 to 256 is 1.33x. Worse, the
1.33x step sits below the 1.5x floor the skill sets two sections earlier in
principle 5, so the ladder fails the skill's own test at its top end.
**Fixed: the label now states the real ratios, and the `field` row notes that
256 is 1.33x and that 288 or more restores the floor.** The token values were
left alone, since changing one would be a design change rather than a
correction.

## Mislabelled

**M1. "Every pixel value below is derived from
`reference/canvas-assumptions.md`" is false, and the skill contradicts it three
lines later.** That file holds the two canvas sizes, the 3x downscale, the 4x
stress test, a 36px floor and a 12pt rendered minimum. It contains no base step,
no dead band, no reading margin, no chrome zone and no emptiness fraction. None
of 16, 64, 108, 860, 180, 80 or 30% appears in it. The next paragraph says the
opposite and is correct: "These numbers are a construction, not a platform
spec." **Fixed: the first sentence now says which values come from the shared
file.** The identical false sentence appears in `dsn-grid`.

**M2. "so the numbers stay consistent across skills" is not true of this pair.**
`dsn-grid` builds the same 1080 square on a margin of 72 and a spacing unit of
24. Neither is a step on this skill's ladder, and 72 falls between this skill's
64 dead band and its 108 reading margin. The two skills also set the
within-group to between-group boundary differently: about 2x here, a 4x minimum
in `dsn-grid`. **Fixed as part of M1.**

**M3. "the one consequence chain more than one source corroborates."** One source
states the chain, across two blocks: "that clutter generates confusion like we
don't really know where to look at" [zyHjG6Szt5g 00:06:19], then "they failed to
be memorable and therefore functional because if we don't remember them... we
will not take any action" [zyHjG6Szt5g 00:07:02]. A second source corroborates
only that clutter is a functional failure, "it does look cluttered and it's
pretty busy" [3QJKOWTRuE4 00:11:49] and "A design with poor hierarchy forces the
user to work extra effort" [FDFD2-poyGw 00:03:07]. Neither Satori video runs the
chain to action. **Fixed to state what each source supports.**

**M4. "screens render whole pixels at 2x and 3x densities, so multiples of 4
survive scaling without half-pixel rounding."** The reason does not work as
stated. At an integer density of 2x or 3x, *any* whole-pixel value stays whole;
4 has no privilege. Half-pixel rounding comes from non-integer scaling, which is
what the shared file says: "a non-integer downscale voids that". No source gives
any reason at all. The only source using the convention just declares it, "I'm
going to use 8 pixel grid system in this case" [1cZBMrdSZUA 00:00:00].
**Fixed to the mechanism that actually holds, and marked as unsourced.**

**M5. "Roughly 1.5x to 2x between steps is the part doing the work," presented as
a principle.** No source states any ratio between steps. The one spatial scale a
source gives arrives garbled as "4 8632" [FDFD2-poyGw 00:03:51], and the skill
itself says so later. Presenting a number range as the load-bearing part of a
principle, with no label, reads as sourced. **Labelled derived.**

## Citations that do not resolve

**C1. [zyHjG6Szt5g 00:06:19] covers only the first link of the chain it is cited
for.** The recall test attributes "clutter produces confusion, confusion makes a
piece unscannable, unscannable makes it unmemorable, and unmemorable means it is
never acted on" to that one timestamp. Confusion is there; unscannable,
unmemorable and not-acted-on are at 00:07:02. **Fixed to cite both.**

The other five inline citations resolve exactly:
- [FDFD2-poyGw 00:01:32] "Elements that are close together are seen as a group."
- [zyHjG6Szt5g 00:08:34] "create importance by removing by creating emptiness
  around the important elements on the page."
- [1cZBMrdSZUA 00:06:31] "I want them only to be appeared on the radius and
  nothing else... uncheck these and just check corner radius."
- [FDFD2-poyGw 00:02:19] "squint your eyes and look at your layout in a blurry
  way... It should work even before you read a single word."
- [1cZBMrdSZUA 00:33:30] "something like base 16. Too tight... Even too tight.
  40."

## Unsupported

**U1. The ratio check's "about 2x", and "about 2x again" between sections.**
No source states a figure. The mechanism is sourced, the number is not. The
nearest thing is a loose passage, "four point micro space between your body text
lines... eight points between the heading and that body text and then also 32"
[FDFD2-poyGw 00:04:38], which is roughly 1:2:8 and which the skill elsewhere
says to read as ratios only. **Labelled derived in both places.**

**U2. The five-value ceiling.** "Five values are learnable in a sitting",
"A sixth value means you are improvising", "Five distinct values per frame is
the ceiling". No source names a count. The one system-building source runs 36
variables with spacing tokens "from zero to 72" [1cZBMrdSZUA 00:02:53].
**Labelled construction.**

**U3. "at least 30% of the canvas empty."** No source quantifies emptiness, and
the figure is not in the shared canvas file. **Labelled construction.** The
measurement procedure around it (black out every bounding box, read the white
fraction) is a good one and is the skill's own invention.

**U4. "the thumbnail test at roughly 15%."** Not in any source and not derivable
from `canvas-assumptions.md`, which gives 3x nominal (about 33%) and 4x as the
stress test (25%). 15% is stricter than the plugin's own worst case, and
`dsn-grid` uses 25% for the same check. **Labelled construction with the
conflict named.**

**U5. The edge values 64, 108, 180 and 80.** Constructions, and the section says
so, which is why these are not counted as mislabels. Worth noting that 108, 180
and 80 are not steps on this skill's own ladder, so a strict reading of the gap
audit ("every value is a scale step") fails on the skill's own edge spec. Left
alone: zones are not gaps, and forcing them onto the ladder would be a design
change.

**U6. Frequency claims, four of them, none sourced.** "the commonest 4:5 mistake
is treating the extra 270px as one more line"; "this is the commonest way a
carousel loses its CTA"; "the one spacing error this format makes unmissable";
"which is why most reviews feel productive and change nothing". No source
discusses carousels, feed formats or review practice at all. **Left in place and
listed here; each would need an argument rewritten to relabel.**

**U7. The canon material, uncited.** "The order is Vignelli's: semantics, then
syntax, then understandability, then the rest" and "Vignelli designed dinnerware
to stack with the debris still inside it" come from outside the four
transcripts, with no id or timestamp. Unlike `dsn-grid`, this skill does not
attach a fake-looking citation to them, which is better, but they are still
unverifiable here. **Marked as outside the transcript set.** Note that the
degraded-state check is a good test whose only stated warrant is this
unverifiable anecdote.

**U8. "one caught inconsistency costs trust in the parts the viewer cannot
check."** Canon, outside the corpus, uncited.

**U9. "Exactly one" isolated element.** The sources support isolation as
emphasis [zyHjG6Szt5g 00:08:34]. The count of one, and "Isolate two and you have
isolated nothing", are the skill's. Not labelled.

**U10. "A seven-word headline wrapping to three lines"** and "the twentieth use
of a template is the one that fails" in the degraded-state check. Illustrative
numbers presented as if typical.

**U11. "Keep the anchor small enough not to rebalance the layout."** The anchor
requirement is sourced, "Even the most off-balance layout needs a visual
counterpoint" [FDFD2-poyGw 00:08:40]. The size constraint is not.

## Derived but not labelled

- **D1. Mode A step 5's consolidation argument.** Grouping is sourced
  [zyHjG6Szt5g 00:18:59]. The cost argument (three boundaries become one, the
  difference released as a composable region, a gap taken from consolidation
  "is paid for by nothing") is the skill's own and is one of its best passages.
- **D2. Token aliasing raised to post-graphic work.** Sourced for UI
  [1cZBMrdSZUA 00:17:23, 00:19:02]; no source applies it to a 1080 canvas.
- **D3. "emphasis is comparative."**
- **D4. "Freeze the frame, vary the density inside it"** and the swipe-jitter
  reasoning.
- **D5. "One isolated element per slide, not per carousel."**
- **D6. The cover slide "is unmissable at thumbnail, the only size a cover is
  first seen at."** The oversized bleeding element is sourced
  [zyHjG6Szt5g 00:24:44]; the thumbnail reasoning is not.
- **D7. The whole Mode B ordering argument** (an inconsistency found after the
  polish invalidates the polish). Sound, and nowhere in the sources.

The skill labels its central synthesis correctly: "No source states this; it is
the resolution they leave open." That is the convention the items above should
have followed.

## Sourced and verified

- Proximity as grouping, and the seating metaphor [FDFD2-poyGw 00:01:32].
- The squint test and "It should work even before you read a single word"
  [FDFD2-poyGw 00:02:19].
- Whitespace need not be empty, "The key is perception of separation and clarity,
  not just the absent of content" [FDFD2-poyGw 00:02:19].
- Micro space deciding what is noticed first [FDFD2-poyGw 00:03:07], and the
  micro / macro job split [FDFD2-poyGw 00:03:51, 00:04:38].
- The contradiction in principle 3 is real. Passive micro space serves
  legibility "without guiding the viewer in terms of structure and viewing
  order" [3QJKOWTRuE4 00:02:08], against micro space deciding what gets noticed
  first [FDFD2-poyGw 00:03:07]. Same channel, incompatible.
- Micro and macro as the vocabulary, and content deciding which job you have,
  "rooms and rooms of text" [3QJKOWTRuE4 00:00:40].
- The register claims: more macro space suggests "minimalism modernity and
  luxury" [3QJKOWTRuE4 00:01:21], Apple reads "premium, modern, minimal" and a
  punk flyer uses "tight, chaotic spacing" [FDFD2-poyGw 00:06:13], tight spacing
  as "fast urgent beats" [FDFD2-poyGw 00:09:18].
- Isolation as emphasis [zyHjG6Szt5g 00:08:34].
- Cut before you space, the less-is-more pass with a worked edit
  [zyHjG6Szt5g 00:10:08, 00:10:56].
- The fill-the-canvas reflex, "I have this canvas I need to fill it up with
  things... I cannot waste any of that free space" [zyHjG6Szt5g 00:15:20].
- Timid whitespace, a region that "kind of hints at creating that space"
  [zyHjG6Szt5g 00:05:41].
- Padding drift inside objects and the centre-align fix
  [zyHjG6Szt5g 00:21:54, 00:23:17]; equal gaps across an icon row
  [zyHjG6Szt5g 00:24:05].
- The claustrophobic two-line logotype and its small-increment fix
  [3QJKOWTRuE4 00:13:49].
- The equidistant-orphan repair worked from the proximity side
  [3QJKOWTRuE4 00:13:05].
- Negative space is not whitespace, "negative space isn't white space they are
  not the same thing" [3QJKOWTRuE4 00:14:27], against "these two words are
  interchangeable they mean the same thing" [zyHjG6Szt5g 00:01:27]. The skill
  reports this disagreement accurately.
- Asymmetry needs an anchor, and the masking test
  [FDFD2-poyGw 00:07:48, 00:08:40].
- Vary the intervals [FDFD2-poyGw 00:09:18].
- Token scoping [1cZBMrdSZUA 00:06:31], aliasing to intent
  [1cZBMrdSZUA 00:17:23], single-point propagation [1cZBMrdSZUA 00:11:25], and
  "random numbers with so many integers" [1cZBMrdSZUA 00:20:08].
- The gaps still chosen by trial [1cZBMrdSZUA 00:33:30].
- The claim that no source offers evidence that more whitespace performs better.
  Verified across all four: every argument is from Apple or from critique of
  weak work. No measurement, no comparison.
- The unrecoverable on-screen table, "here's a table that I've crafted... so
  yeah, bookmark this" [FDFD2-poyGw 00:07:04], contents visual only.
- The list of absences (optical margin alignment, baseline grids, responsive
  spacing, print safe areas, accessibility minimums, non-Latin settings).
  Verified: none of the four mentions any of them.

One source, `3QJKOWTRuE4`, is never cited inline despite supplying principle 2
and half of principle 3.
