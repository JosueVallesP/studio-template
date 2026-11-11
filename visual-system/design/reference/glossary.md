# Glossary

One meaning for every term that more than one skill uses. Where a skill's own
terms section says something different, this file wins until that skill is
corrected. A term that only one skill uses stays in that skill.

Two rules for adding to this file: one meaning per word, and one word per thing.
The "Do not use" lines name the second words that were in use for the same thing.

## The canvas and how it is seen

**Canvas.** The pixel dimensions of the working file: 1080 x 1080 or 1080 x 1350.
The sizes are fixed in `reference/canvas-assumptions.md`. The small square an icon
is drawn in is called the **icon box**, never the canvas.

**Frame.** One canvas in a piece, edge to edge, margins included. A carousel slide
is a frame. A poster is a piece with one frame.

**Downscale factor.** The working-file width divided by the width the frame is seen
at. The two cases, nominal and stress, and their values are in
`reference/canvas-assumptions.md`.

**Delivery size.** The size the reader sees: a working-file size divided by the
downscale factor. Do not use "delivered size", "viewing size" or "rendered size"
for this.

**Type floor.** The smallest working-file size for text someone must read. It has
two cases, and a floor quoted without its case is incomplete. The values are in
`reference/canvas-assumptions.md`.

## Structure and space

**Margin.** The band between the canvas edge and the live area. Text and anything
else that carries information stops at the margin. A picture or a flat field of
colour may cross it when the layout says so.

**Live area.** The canvas minus its margins.

**Column, gutter, span.** Columns are equal vertical divisions of the live area. A
gutter is the gap between two neighbouring columns. A span is a run of columns
plus the gutters between them.

**Spacing unit.** The one number every gap, margin and gutter is a multiple of.
Its default value is in `reference/canvas-assumptions.md`.

**Gap.** The empty distance between two separate elements, measured edge to edge.

**Negative space.** A region of the frame left empty on purpose.

## Type

**Measure.** The length of one line of text, counted in characters including
spaces. Never in pixels: when a width in pixels is meant, say "column width".

**Leading.** The distance from one baseline to the next, written as a ratio of the
type size (1.40, not 67px).

**Tracking.** Letter spacing applied evenly across a run of text.

**x-height.** The height of a lowercase x in a typeface.

**Counter.** The enclosed or partly enclosed space inside a letter or shape.

**Weight.** A named cut of a typeface at one stroke thickness: light, regular,
medium, semibold, bold. For how heavy an element looks in a layout, say "visual
weight".

## Order

**Rank.** A position in the order a reader notices things. Rank 1 is noticed
first. A rank is held by content (the headline, the figure), not by a style. Do
not use "level", "level one" or "L1" for this.

**Focal point.** The place in the frame where the rank 1 element sits. A
photograph has its own focal point inside its crop; call that "the picture's focal
point".

**Channel.** One visual property used to mark a rank: size, weight, colour,
position, surrounding space, or an added element such as a rule or a tag. For the
separate idea of something that carries meaning (words, a picture, colour), say
"carrier".

**Register.** The tone a frame arrives in, named in one word: urgent, warm,
clinical. For a set of elements that share a visual character (all angular, all
photographic), say "family".

## Colour

**Hue, saturation, lightness.** The three numbers that describe a colour. Hue is
its position on the colour circle, saturation is how far it is from grey, and
lightness is how light or dark it is.

**Value.** What a token returns when it is looked up: `#2B2B2B`, `90`, `1.4`. Do
not use "value" for lightness.

**Tonal value.** How light or dark something looks with its colour removed. When a
number is needed, it is the relative luminance.

**Relative luminance.** The brightness of a colour as one number from 0 to 1,
computed as the accessibility specification defines it. The skill that measures
contrast holds the formula.

**Contrast ratio.** (L1 + 0.05) / (L2 + 0.05), where L1 is the relative luminance
of the lighter colour and L2 of the darker. It runs from 1 to 21. The thresholds
belong to the skill that measures contrast.

**Greyscale check.** Looking at a frame with its colour removed to see whether the
structure still holds. It is a quick screen. It is never a measurement and never
reported as a contrast ratio.

**Tint and shade.** A tint is a hue made lighter. A shade is a hue made darker. Do
not use "tone": people use it for three different things.

**Dominant, supporting, accent.** The three jobs a colour can hold in a frame. The
dominant covers the largest area. The supporting covers the second largest. The
accent covers a small area, is the most saturated colour in the frame, and is
there to be noticed. A colour used on many elements is not an accent, whatever
its name.

## Brand

**Mark.** The fixed graphic that stands for the brand. It can be a wordmark (the
name drawn as the mark), a monogram (initials), a pictorial mark or an abstract
mark. For only the drawn, non-letter part of a logo, say "symbol".

**Token.** A name bound to a value, where the name states the job (`color.text.primary`,
`space.margin`) and the lookup returns the value. A name that states a size (`md`,
`large`) or a hue (`sky-blue`) is not a token name.

**Moodboard.** A set of images that share a feeling, with no note on what each is
there for. A set where every image carries a note naming the one quality taken
from it is a **reference board**, and the art-direction plugin owns building one.

## Marks used in the skills

**(thin).** The rule or number rests on a single source, or was inherited without
a reason. Treat it as a default you may change, and say so when a finding rests
on it.
