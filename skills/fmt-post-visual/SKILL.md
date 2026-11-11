---
name: fmt-post-visual
description: >-
  Decide and build the visual for a post (single image, carousel, field guide, plate or word card). The idea comes first: visual philosophy finds its shape, then a grammar of marks, relations, plays and 22 proven moves (with nineteen variants) turns the shape into a picture, built from the person's visual kit in neutral and then styled. Use when a post needs a visual, or someone asks "what should the picture be?" or for a carousel, field guide, infographic or framework visual. Not for writing the post or essay itself (use fmt-linkedin-post or fmt-substack-essay).
---

# Post visual

Decide what the picture for a post should be, build it in neutral, then hand it to a style. Reads `library/visual-moves.md` (marks, relations, plays, moves, formats, the kit). For real examples of a post and its picture together, 174 posts in `../fmt-linkedin-post/library/posts/` carry a `visual_url` and a `media` type (carousel, infographic, image); filter the index CSV by its `Media` column to find them. The idea leads: `skills/craft-visual-philosophy` runs first on every visual, and the moves are the vocabulary it reaches for, never a menu to pick from before the idea has a shape. Hands off to the person's style at the end (step 5 has the one order to find it). The person's design system, when there is one, lives in the canon (`canon/visual/design-system.md`) and `config/tools.md` names their Figma visual kit and any style skill they use.

Rule for everything here: the picture must make sense to someone who never reads the post. Concrete headline, labels in familiar words, no concept jargon.

## Two doors

**Door 1. "Here's the post. What should the visual be?"** The usual case. Start with the piece's `brief.md` (its material and format plan) and the draft's PARTS MAP if they exist, or with the post itself. The chain below decides the format.

**Door 2. "I want a carousel" (or a field guide, a plate, a word card, a single image).** The format is fixed. Skip the format choice in step 3 and pick the move inside the container.

The format menu, for door 2 and for step 3:

| Format | Use it when | Not when |
|---|---|---|
| Single image | One idea with one shape. Most posts. | The idea has three parts that each need a picture |
| Carousel | The post has a sequence of beats worth a frame each (a story arc, an explained list, a breakdown) and the opener can carry a headline plus one line | The post is one claim; it becomes a single image padded to seven frames |
| Field guide | Two or three parts of one idea, each with its own shape (a tree and a process; a curve and a table) | One part. Then it's a single image with a subhead for no reason |
| Plate | The idea is a feeling or a metaphor that one scene carries, with two or three short paragraphs under it | The idea needs labels to be understood |
| Word card | The claim stands alone in one to eight words. Usually "the body is the hook" posts, and carousel middles | The line needs explaining |

"Infographic" and "illustration" are not formats. An infographic is a single image or a field guide using a diagram move. An illustration is the scene move (V15) drawn in a style that can illustrate.

## The chain

Before step 1, run `skills/craft-visual-philosophy` steps 0 to 4 on the brief's one idea: state the idea, find its logic, name the purpose and reader, list the things, name the relationship, find the visual mechanic. When `visual-brief.md` already exists with an option picked (from `/visual-philosophy` or an earlier run), read it instead and don't run the method again: steps 1 and 2 below are already answered there, so check them in a line and go to step 3, or straight to step 4 with the picked option. When the brief holds no shape, visual philosophy says so and the piece has no visual.

**Where `visual-brief.md` goes.** This is the one rule, and `craft-visual-philosophy` and `/visual` follow it. Always write it to a piece folder and show it in the chat too: `pieces/<id>/visual-brief.md` when the idea came from a piece, otherwise a new folder `pieces/<yyyy-mm-dd>-<slug>/visual-brief.md` that holds only that file until a piece is made from it (with no `brief.md`, `/status` doesn't count it as a piece). Say where it went in one line.

### 1. The idea and its shape

Write the idea in one or two plain sentences. If it can't be said in two sentences, it isn't ready to draw; go back to the writing.

Then find its logic, from the one list of what gives an idea a shape (`skills/craft-visual-philosophy`, step 0). If it has none, say so: this one is words, or the idea needs sharpening before it has a shape. Do not draw a diagram about the idea.

When the brief exists, the hook move narrows this fast: then-and-now hooks carry a curve or a side by side; proof hooks carry a ladder, a sequence or a table; contrarian hooks carry a side by side or a flip; scene hooks carry a scene; the finding carries a distribution, a branching or a count.

### 2. What it is for

Three questions, answered from the brief or asked:
- Who sees it, and what do they already know?
- Where does it live: the feed next to the post, a slide, standalone?
- Is the job to make them feel a problem they recognize, or to show them the fix? These give different pictures (a problem is often a scene or a side by side; a fix is often a sequence, a ladder or a table).

### 3. Three options

Read `library/visual-moves.md`. For the idea's shape, pick the relation (Layer 2), then two or three moves that carry it (Layer 4), and the plays that fit (Layer 3). If no move fits the shape, go back to the visual brief's mechanic (`skills/craft-visual-philosophy` step 4) and build one from marks and a relation, and treat the result as a candidate move.

Offer three options that use different mechanics, not three layouts of one idea; fewer only when the idea allows only one honest shape, and then say so: for example one comparison (side by side), one repeated mark (scale, field, bars), one scene or borrowed symbol. Lead with the strongest. For each:

```
MOVE        name, or "new: <one line>"
RELATION    what the arrangement claims
PLAYS       which, and what each adds
FORMAT      from the menu (skip if door 2)
LAYOUT      what is drawn, where it sits, what the viewer sees first, what size and position mean
HEADLINE    the one concrete line
LABELS      every label, written out, as few as the picture needs
WEAK SPOT   what it carries and what it doesn't ("carries the feeling, not the fix")
LABEL TEST  delete the labels in your head: what is still visible?
```

Then: what was cut, in a line, so the person can add it back.

The person picks one. If they're not there, take the first and say so.

### 3a. Carousels only: the slide plan

Before drafting, map the post to frames:
- Frames 1 and 2 show together: headline on 1, the supporting line on 2. Design them as a pair.
- One complete thought per frame. Big type. A small diagram beats a big one.
- Map the body's parts to frames using the PARTS MAP: the setup, each piece of evidence or each list item, the turn (its own frame), the meaning line (the close).
- Alternate: a word or scene frame, then a text frame. Diagram moves go in the middle frames at small size.
- Last frame: the restated claim or one ask. Never both.
- Five to ten frames. If it's under five, it's a single image.

### 4. Draft in neutral

Build the picked option from the visual kit (see "The visual kit in Figma" in `library/visual-moves.md`): the person's copy when `config/tools.md` names one, otherwise the master. Work on a page called "Pieces", in a starter frame from the Kit page, in the Neutral mode. Place the marks the idea needs as instances from the Kit, sized, placed and named for what they stand for. The example for the move on the Moves page is a reference for how the parts go together, not a form: when the example's layout already fits the idea, you can start from a copy of it, but change it until it carries this idea and no other (the number of cells, steps, rings or bars comes from the idea, never from the example). Apply the plays from step 3. No Figma at all? Build it as SVG with the same marks and the same rules; that's the default without Figma, saved as `visual-neutral.svg` in the piece folder and shown in the chat. No style. Black hairlines on white with one accent is the point: the idea gets judged before the skin can flatter it.

Then run the six tests in `library/visual-moves.md`, "Tests for any picture" (the one copy of them). Fix what fails. Then subtract: remove one element at a time until removing one more would break the idea.

### 5. Style

The style comes from the first of these that exists, and this is the one fallback order (the designer and `/visual` point here):

1. `canon/visual/design-system.md` (written by `setup-visual-identity`): its type, color, texture, composition and mark, the clash points the contradiction brief names, and any style skill it or `config/tools.md` names.
2. `config/tools.md` says Figma `brand applied: yes`: switch the frame to the Brand mode and stop there.
3. The person's brand assets from the intake (`canon/visual/brand-assets.md`): their colors and fonts on the neutral build.
4. Nothing: stay in neutral, with the TRAIN principles in `craft-visual-philosophy` ("When styling comes later"), and say in one line that the full look waits on `setup-visual-identity`.

The move, the relation, the marks and the labels do not change. The style changes type, color, texture, line, and draws the illustration where the move is a scene. If a style skill the person uses has rules of its own (how many versions of a visual it makes, say), those apply here; this skill doesn't hold them.

### 6. Judge at feed size

Look at the styled version at the size it will be seen, with the post text hidden. Check: stand-alone, stranger, legibility of every label, the headline readable in the first second. One fix pass, then stop.

## Output

```
IDEA         one or two sentences
SHAPE        the logic found in step 1
PURPOSE      who, where, feel the problem or show the fix
OPTIONS      three briefs, strongest first; which was picked
SLIDE PLAN   carousels only
NEUTRAL      node id of the draft in Figma, or the SVG file; test results
STYLED       node id or file after the style pass
```

## Rules

- Neutral before style, always.
- Three options, with different mechanics, even when one is obvious; fewer only when the idea allows only one honest shape, and say so.
- The format is a decision made from the idea's shape (door 1) or given (door 2). It is never a reason to stretch or pad an idea.
- When a new move works, never edit the library (it's the studio's, and an update replaces it). Write it to `studio-notes.md` as a candidate move for the studio's author, with the full card filled in the library's format.
- Every label and headline follows the house rules (`skills/craft-house-rules`).
