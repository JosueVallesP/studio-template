# Craft routing

This plugin decides what a brand should look like and whether a piece is on brand.
It does not hold the craft mechanics underneath that. Those live in the **design**
plugin, `github.com/JosueVallesP/design`, as 17 `dsn-*` skills.

**The dependency runs one way.** This plugin may point at design. Design never
points back at a skill here, and nothing in design needs to change for this file to
work. `ROUTING.md` holds the order of what wins: the brand beats a craft default, and a
measured floor beats the brand. Record in `piece.md` any case where you followed
one over the other.

Open the design skill when the question is craft rather than brand. Route by the
question, not by the format:

| The question in front of you | Open |
| --- | --- |
| What reads first, second, third, and nothing does | `dsn-hierarchy` |
| Where things sit in the frame, and the frame reads flat | `dsn-composition` |
| Margins, columns, gutters, spans, or a layout placed by eye | `dsn-grid` |
| Gaps, padding, whether there is enough air, safe zones | `dsn-spacing` |
| Whether the frame should feel stable or should tip | `dsn-balance` |
| Picking or pairing a typeface | `dsn-typeface` |
| Size, leading, tracking, measure, or a type scale | `dsn-typeset` |
| Which colours should exist, or judging a set | `dsn-palette` |
| What a colour is doing, or why a frame reads muddy | `dsn-color` |
| Whether text is readable by a measured standard | `dsn-contrast` |
| Choosing, cropping or treating a photograph | `dsn-image` |
| How a carousel argues across slides | `dsn-sequence` |
| One frame carrying an idea with no next slide | `dsn-poster` |
| Designing or judging a logo, wordmark or monogram | `dsn-mark` |
| What a brand's identity consists of beyond its logo | `dsn-identity` |
| Turning brand decisions into named, resolvable values | `dsn-tokens` |
| A set of icons that must read small and look like a family | `dsn-icon` |

## Two shared facts to read before you draw

Read both in design's `reference/canvas-assumptions.md` before drawing. That file
is the only place the numbers are written, so this file does not repeat them.

- **The type floor.** The smallest working-file size for text someone must read,
  with its two cases, and the rule for a canvas that is not 1080 wide.
- **The default system.** One margin, gutter, spacing unit and type ladder for a
  1080 canvas. Use it wherever the brand's `tokens.json` gives no value.

## Where critique lives

Judgment about whether a direction holds and whether a piece is finished belongs to
the **art-direction** plugin, `github.com/JosueVallesP/art-direction`: `ad-board`
for reference boards that work as directions, `ad-rules` for writing a direction as
testable rules, `ad-brief` for specifying an image before it exists, and
`ad-critique` for judging someone else's work.

That is a different question from `/cd-review`, which judges a draft against one
brand's own tokens, direction and canon. Use the review here for brand fidelity.
Reach for art direction when the question is whether the direction itself is any
good, or whether the work is done.
