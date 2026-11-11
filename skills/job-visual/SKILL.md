---
name: job-visual
description: >-
  The visual for a post, an essay or a bare idea, from one command: finds the idea's shape (visual philosophy), picks the move and the format (single image, carousel, field guide, plate, word card), builds it in neutral from the person's Figma visual kit, then applies their style. Works with no canon. Use for /visual, "make the visual", "what should the picture be", "make a carousel of this", "a framework for this idea".
---

# /visual

One picture, from one command. The idea comes first and the picture follows from it; the studio never fills a template. This skill runs `skills/fmt-post-visual` directly and skips the designer role's pipeline steps (the reviewed-piece precondition and the producer's decision).

## What it takes

One of these, in order of preference:

1. **A piece in `pieces/`** (the last one `/post` or `/essay` made, or one the person names): its `brief.md`, the draft's PARTS MAP and the post itself. Door 1 in `fmt-post-visual`.
2. **A post or essay pasted in the chat.** Same door; the chain builds the minimum brief first (the one idea, the material it uses).
3. **A bare idea** ("a framework for how I think about pricing"): run visual philosophy on it and say what shape it has, if any, from the one list in `skills/craft-visual-philosophy` step 0. An idea with none of those has no picture, and the honest answer is to say so and ask what the idea rests on.
4. **A format asked for by name** ("make a carousel of this"): door 2; the format is fixed and the move is picked inside it.

## Before it runs

- `config/tools.md`: whether Figma is connected and which file is the person's visual kit.
- `canon/visual/design-system.md` when it exists: the style to apply at the end.
- `visual/brands/<their-name>/system/package/` when it exists: the person's own visual package from `/visual-system`. Read its README first.

## Procedure

Run `skills/fmt-post-visual` as written. What differs on the direct path:

- **No piece needed.** For a pasted post or a bare idea, `visual-brief.md` still goes to a folder of its own and into the chat, by the one rule in `skills/fmt-post-visual`, "Where `visual-brief.md` goes".
- **The person picks.** Show the three options in words, two lines each, say which you'd take, and let them pick (or take yours when the pick is obvious). This is the one place they decide before anything is drawn.
- **Without Figma**, build the picked option as SVG, neutral, as `fmt-post-visual` step 4 says (the default without Figma), save it in the folder and show it, and say in one line that the full kit arrives with the Figma quick win (`setup-figma`).
- **The style** follows the one fallback order in `skills/fmt-post-visual` step 5.
- **With a visual package**, build the picked option with the package's script and one of its formats, as the package's README says, in place of the Figma kit or the neutral SVG, and run the script's check on the result. A format the package doesn't have is built as `fmt-post-visual` step 4 says and styled from the package's values. The package's rules and its never list win over the style fallback.
- **Never invent** a number or a label the post doesn't carry.

## Two more kinds of visual, through the same philosophy

**Art direction.** For a visual the kit can't build (an illustration, a painted or engraved scene, a photo concept), the output is a brief someone or something else executes (an illustrator, a photographer, an image tool). Visual philosophy runs first as for any visual; the brief says what the image has to show and why, what it must not show, the composition, how it fits the person's design system, and how it sits with the text. Same standard: legible on its own to someone who never reads the post. Never a copy of a living artist's style or a known work.

**Data visuals.** Numbers are one more kind of idea that visual philosophy gives a shape to, not a chart skill. A plain chart is right when the numbers themselves are the point; otherwise look for a shape that makes the point at a glance. Shape first: what do the numbers say (a change, a comparison, a share of a whole, a gap)? Find a mechanic that makes that point at a glance, often a picture or a diagram rather than a bar or a line. The plain chart is the fallback, used only when nothing better carries the point. Honest proportions: the shape can be creative, but the sizes match the numbers (Edward Tufte's lie factor; something drawn twice as big means twice as much). Real, sourced numbers only: a number about the person comes from their material or canon (`CLAUDE.md` rule 1); an outside number is `borrowed: verify`, with its source on or under the visual.

## Output

The picture exported at the channel's size (1500 × 1800 or square for a LinkedIn image; the carousel sizes in the kit), saved next to the piece or shown as a Figma link, and two lines on what the picture does and why that shape.

## Handoff

None. The piece keeps its status; the person decides what to do with the picture.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
