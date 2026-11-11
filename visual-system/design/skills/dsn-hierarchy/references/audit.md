# Audit: dsn-hierarchy

Independent check of `SKILL.md` against the transcripts in
`~/research/design-plugin/transcripts/` only. The source set used:
`hierarchy__5yjYe9aDSBM`, `hierarchy__4QNEDhrsRLo`, `hierarchy__kK1TOpI948o`,
`principles__HmgzcaH-uv8` and `principles__WLI5ckPofrk`.

`references/provenance.md` was not used as evidence. It was written by the same
agent that wrote the skill, so it is self-attestation.

Counts: 4 mislabelled, 2 citations pointing at the wrong place, 6 unsupported,
7 derived but unlabelled. Fixes applied inline where the correction is grounded
in a transcript; everything left alone is marked "reported only".

The skill's own promise, "single sources and derived figures are flagged at the
point of use," did not hold for thirteen of these nineteen findings. The fixes
below bring most of them inside it.

---

## Mislabelled attributions

### 1. "4 / 8 / 16 / 32, or 8 / 16 / 32 / 64 [5yjYe9aDSBM 00:14:52]"

The source states one scale, not two: "what actually works really well on a
design is using a spatial scale. It's a consistent system of values, so maybe 4
8 16 32" [5yjYe9aDSBM 00:14:52]. A search of all five transcripts returns no
occurrence of 64 at all. The second scale is attributed to a source that does
not state it.

The same source's own worked example also fails the doubling the skill builds
on it: "four-point micro space between your body text lines, but then eight
points between the heading and that body text. And then also 32 from the entire
text group" [5yjYe9aDSBM 00:15:38]. That is 4, 8, 32, skipping 16.

**Fixed:** second scale relabelled as an extension made here, the gap in the
source's own example noted.

### 2. "Every pixel value below is derived from it" (Applied to a post visual or carousel)

This is the most damaging finding in the file, because it launders a source
claim into a shared-file claim and the shared file says the opposite.

`reference/canvas-assumptions.md` contains the canvas sizes, the 3x factor, the
4x stress test, a 36px floor and a note about type-scale steps. It does not
contain 8, 16, 32 or 64. Those values trace to a video source
[5yjYe9aDSBM 00:14:52], not to the shared file.

And `canvas-assumptions.md` explicitly rules the convention out for canvas
work: "Absolute values borrowed from UI and web work (16px body, 12px minimum,
4 and 8px spacing units) are device-independent pixels. Multiply by the
downscale factor before using them on a canvas, which is also why the 4 and 8
unit convention does not transfer: its reason is whole-pixel rendering, and a
non-integer downscale voids that."

So "Spacing: 8 / 16 / 32 / 64" in the post-graphic section is presented as
deriving from a file that forbids it.

The thresholds attached to it, "within-group at or below 16, between-group at or
above 32", are in neither the shared file nor any transcript.

**Fixed:** the header claim corrected, the spacing values attributed to the
source they come from, the shared file's objection carried into the line that
uses them, and the 16 and 32 thresholds marked as constructions.

### 3. "WCAG 2.1 AA wants 4.5:1 ... which the 4.5 figure matches for text [kK1TOpI948o 00:05:37]"

The citation resolves to the figure, but not to that framing. The source cites
WebAIM, not WCAG, and states the figure for general prominence rather than for
text: "WebAIM ... They say we want to aim for a contrast ratio of 4.5 or higher
if you want one element to pop against the background or to be visually distinct
from other elements" [kK1TOpI948o 00:05:37]. It then adds that this is
"especially useful for text legibility".

3:1 for large text and UI components is in no source in the set. It is correct
against WCAG 2.1 AA as external knowledge, and the skill does attribute it to
WCAG, so this is a small correction rather than a false claim.

**Fixed:** WebAIM named as the source's own citation.

### 4. "Built from three visual-hierarchy tutorials ... Roughly 60 to 65 percent of it rests on one channel"

The source set is five transcripts, four of them Satori Graphics. Two Satori
supporting guides, `principles__HmgzcaH-uv8` and `principles__WLI5ckPofrk`,
carry load-bearing material in the skill (the flow-from-rank claim behind the
arrow-removal test, and the deck pacing), and the opening does not count them.

The 60 to 65 percent figure has nothing behind it. It is not a measurement of
anything, and no method for arriving at it is stated or available.

**Fixed:** the count corrected, the percentage relabelled as an estimate.

---

## Citations pointing at the wrong place

### 5. "a landing page puts the headline above the video even when the video is the point [kK1TOpI948o 00:13:09]"

The landing-page case is at 00:12:38: "most landing pages which feature a video
will have a headline up top and the video underneath. Even though we might think
as designers that the video is more important than the headline, visitors need
the headline to understand the context of the video."

00:13:09 holds the general decoupling statement that follows it, "hierarchy is
not the decision of what's essential in the design, but simply what visitors
should see first," which supports the principle's first sentence but not the
example cited to it.

**Fixed:** both timestamps given.

### 6. "same-type elements share identical size, weight, colour, padding, radius and height [kK1TOpI948o 00:10:13]"

00:10:13 holds the principle: "You can make an element look exactly how you want,
so long as the other elements of the same type share the same values." The
enumeration the skill quotes is at 00:10:47: "Each image should be the same
size. Each card title should use the same font with the same font size and the
same font weight. Each paragraph should be exactly the same, even taking up the
same height. Even the card should have the exact same border color and corner
radius."

**Fixed:** range extended to 00:10:13 to 00:10:47.

Every other inline citation resolves. Verified: `kK1TOpI948o` 00:02:50 (the
task-relevance claim, exactly as the skill flags it), 00:05:37; `5yjYe9aDSBM`
00:14:52, 00:08:48, 00:17:14 to 00:18:43; `4QNEDhrsRLo` 00:08:49 (the hedge,
"it's actually a streamlined Avenue that most viewers will be able to use").

`Cairo Low28hx4wyk 00:24:24` in principle 7 is not a video in this skill's
source set and is not present in `~/research/design-plugin/transcripts/`, so
the election-map case and its 80/20 and 50/50 figures could not be checked
either way here. Reported, not changed.

---

## Unsupported

### 7. "Two channels for rank 1, one for rank 2, none for rank 3" (principle 5, and the channel-count test)

No source in the set states any channel allocation, any count of channels, or
the claim that "one usually loses, four is shouting". The nearest source
statements are qualitative: "save your strongest contrast for the most
important thing" [5yjYe9aDSBM 00:08:48] and "You don't need to make everything
bold or use every trick at once" [5yjYe9aDSBM 00:02:41].

The exception the principle names is sourced: weight "guides the eye down our
paragraph" and "is not insanely attention-grabbing like motion"
[kK1TOpI948o 00:07:17].

**Fixed:** the 2 / 1 / 0 allocation marked as a construction, the sourced
exception left as is.

### 8. "Three type sizes, two weights, one accent element"

No source caps any of these. The one-accent part has partial cover as a tactic
rather than a cap: "one common tactic is to have a dull even grayscale design
with one single element in color" [4QNEDhrsRLo 00:02:06].

**Fixed:** marked as constructions where the figures first appear.

### 9. "every gap within a group is smaller than every gap between groups, by at least one step on the scale. Arithmetic, not feel"

The grouping relation is sourced: "Give each group of assets enough room to be
seen clearly, then use a larger gap to signal a new idea or aspect of your
design" [5yjYe9aDSBM 00:04:36], with proximity named as the mechanism,
"Elements that are close together are seen as a group" [00:12:37].

"By at least one step on the scale" is the skill's quantification. Calling it
arithmetic rather than feel overstates what the source gives, which is larger
versus smaller.

**Fixed:** quantification marked derived.

### 10. "By slide 5 someone is reading on purpose"

Slide 5 is in no source. The tasked-reader idea is sourced [kK1TOpI948o
00:02:50]; the slide number is not. **Fixed:** marked as a construction.

### 11. "Stray boxing is the commonest amateur tell in a carousel"

A frequency claim. Nothing in any of the five transcripts says it, ranks
amateur tells, or mentions carousels at all. The surrounding mechanism, that a
box promotes what is inside it, has partial cover from the extra-elements
channel, "adding an extra element like a border or a tag can be a great way"
[kK1TOpI948o 00:08:28].

**Fixed:** the frequency claim marked as not coming from these tutorials. The
claim itself is kept.

### 12. "A 340 percent at 200pt"

Illustrative figures with no source. Reported only: they are a worked
hypothetical inside a sourced principle, and marking them would add noise
without changing what a reader does.

---

## Derived but not labelled as derived

### 13. The squint test, repurposed

The skill uses it to count competing firsts: "Squint until type is unreadable
and count the shapes. Catches competing firsts. Verdict: one passes; two or
more, flatten and promote once."

The source's squint test is for grouping, and that is all it asks of it: "Squint
your eyes and look at your layout in a blurry way. You should still be able to
tell which elements belong together just by how the white space shapes the page.
That's the power of grouping or proximity" [5yjYe9aDSBM 00:13:20].

Counting shapes to find competing primaries is a different reading of the same
gesture. **Fixed:** labelled as an extension of the source's grouping test.

### 14. The greyscale test

No source states it. It is derived from the colour-vision caveat: "if you don't
change the luminance value at all, then it will be less accessible for people
with color vision deficiency" [kK1TOpI948o 00:06:11]. **Fixed:** labelled
derived.

### 15. "Demote, don't promote" (principle 6)

No source states it. The nearest support is DesignSpo's relativity point, "it's
not about making some elements huge if you want them to get noticed, but about
using their contrasting sizes to create hierarchy" [kK1TOpI948o 00:06:44], and
Satori's "keep the supporting details quieter" [5yjYe9aDSBM 00:02:41].

Satori elsewhere teaches the promotion move directly: "just think of the most
important information on your design and then give that prominence"
[4QNEDhrsRLo 00:04:18].

So the skill's strongest instruction to an agent is a derivation that one source
contradicts. **Fixed:** labelled derived, with the contradiction noted.

### 16. "read as related across as much empty space as you like"

The source says "across a gap": "use alignment to connect things across a gap.
So, two elements sharing an edge or an axis can feel like part of the same
system without needing a box or divider between them" [5yjYe9aDSBM 00:08:48].
"As much as you like" is an amplification. Reported only; one clause inside an
otherwise sourced rule.

### 17. "Pace the deck: impact, linger, pause"

The source's triad is "Impact, linger, release" [WLI5ckPofrk 00:08:33], which
it also renders as "punch, slow, pull, release" [00:09:26]. "Pause" is the word
it uses for the white-space beat in the preceding sentence, not the third term
of the triad. **Fixed:** corrected to the source's wording, with the citation.

### 18. The hand example under silhouette spacing

The principle is at the cited timestamp [5yjYe9aDSBM 00:08:48]: "judge space
from the visible shapes, not just the boxes around them. A broad image may need
more breathing room than a thin line, even when the measurements are technically
equal."

The outstretched-arm example is at 00:01:19: "that space follows the visible
outline of the hand and the chalk, rather than the edge of the rectangular image
file." **Fixed:** second timestamp added.

### 19. "rank 1 top-left or at the optical centre"

No source says optical centre. Satori says "a focal point in the very center"
[4QNEDhrsRLo 00:10:03]. Reported only: the term is standard outside these
sources and the placement advice is unaffected.

---

## Claims checked and found sound

Noted so the audit is not read as a verdict on the whole file.

- The task-relevance flag, which the skill calls its strongest and most
  counterintuitive claim, is exactly what the source says and exactly as
  single-source as the skill states: "people often don't look at the big,
  obvious, bold thing in a design, they look for what's important to them"
  [kK1TOpI948o 00:02:50]. Nothing in the other four transcripts corroborates
  it, and Satori's model runs the other way, "The design is literally a visual
  trap" [4QNEDhrsRLo 00:01:19].
- The ten-channel ordering is as the skill reports it, motion then
  task-relevant information above every designer-controlled channel
  [kK1TOpI948o 00:02:14 to 00:09:37], and the skill is right to refuse to quote
  it as a ranking.
- "A headline only has to be a little bit bigger to be read visually as a
  headline" [kK1TOpI948o 00:06:44]. Quoted accurately.
- "No source here supplies a type scale at all." Confirmed across all five.
  The 2x and 1.3 to 1.5x steps are already labelled derived in the skill, as is
  the pair in the post-graphic section.
- F and Z as conventions with differing mechanisms. Confirmed: Satori has the F
  starting top-left and extending right [4QNEDhrsRLo 00:08:49]; DesignSpo has
  the F as top to bottom then left to right [kK1TOpI948o 00:14:16]. Neither
  cites eye-tracking. The hedge the skill quotes is real.
- Placement choices by medium are sourced: "On a poster or a billboard or more
  minimalist designs, the Z pattern might be more effective. In a letter or a
  card ... top to bottom ... on the web, generally, the F pattern"
  [kK1TOpI948o 00:14:50].
- Counterbalance and the cover test, single-source and correctly cited
  [5yjYe9aDSBM 00:17:14 to 00:18:43], including the anchor requirement, "you
  have to anchor everything".
- Flow from correctly expressed rank, behind the arrow-removal test: the arrow
  "has been completely banished" and the eye still stops in the middle because
  "Larger bolder elements are seen first, then medium elements, and then the
  smaller ones" [WLI5ckPofrk 00:01:28].
- Three ranks as a convention, and two or three per region on a multi-area
  layout: "each section has at least two or three levels of hierarchy"
  [4QNEDhrsRLo 00:14:59].
- Tight spacing as a legitimate energetic choice: "A punk band flyer might use
  tight, chaotic spacing because it says energy" [5yjYe9aDSBM 00:16:23].
- Brand-first ranking, demonstrated by the broken package: "The Crocs mark,
  product name, and specifications all compete for attention now"
  [5yjYe9aDSBM 00:01:59].
