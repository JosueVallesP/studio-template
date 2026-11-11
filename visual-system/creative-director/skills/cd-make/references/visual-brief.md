# The visual brief contract

The visual brief is the handoff into `cd-make`. A content system (like the studio owner's content studio), a person or `cd-make` itself can write it. Whoever writes it owns the idea. `cd-make` owns how it looks.

## Where it lives

`<brand>/pieces/<YYYY-MM-DD>-<slug>/visual-brief.md`, using the template in `_piece-template/`. A content system writes the file there directly; that's the whole integration.

## Two kinds of piece

- **Idea pieces** carry one claim: a framework, a diagram, a post visual, a carousel, an essay header.
- **Composed pieces** gather existing material into a layout: a one-sheet, a speaker page, a bio card, a book cover, an event slide.

The gates below say which kind each one applies to.

## What a complete brief has

| Field | Required for | What makes it complete |
| --- | --- | --- |
| The claim | Idea pieces | One or two sentences the visual must make true, in the person's words |
| Where it comes from | Idea pieces | A specific belief, method, story or result from the person's work, ideally one in `brief.md` |
| What the visual must show | All | For idea pieces, the relationship or contrast the reader should see. For composed pieces, what the reader should come away knowing about the person |
| Content to include | Composed pieces | The material to place, pointing to files in `<brand>/assets/` (headshot, bio, talk description, testimonials, logo) or pasted in |
| Words that must appear | Optional | Exact wording, kept as given. Empty means `cd-make` proposes words and marks them as proposed |
| Platform and format | All | A platform and a file in `formats/`, or "custom" with a size |
| Constraints | Optional | Size, deadline, tool, anything the studio owner asked for |

If content a composed piece needs isn't in `assets/` or the brief, ask the studio owner for it. Never write a bio, a quote or a testimonial yourself.

## The idea gate

The content side runs these before writing the brief. `cd-make` checks them again and sends the brief back if one fails:

1. **Source** (idea pieces): the claim traces back to the person's own work.
2. **Swap** (idea pieces): with another name on it, it wouldn't fit just as well.
3. **Shape** (diagrams, frameworks and charts only): the idea has a relationship or contrast a visual can show (see `<plugin>/taste/rules/diagram-form.md`). If not, it may be better as words.
4. **Concrete words** (all): the brief's words are ones the reader already knows.

## Sending a brief back

End the run on `Brief returned: <reason>`, and write the reason at the top of the visual brief under a heading "Returned," with the date. Name the failed gate and, where you can, what would fix it. Don't rewrite the claim yourself.

## Review can also send it back

If `cd-review`'s caliber, legibility or form reviewer finds the idea thinner than the brief promised, the piece goes back to the brief's author, not to another round of drafts.
