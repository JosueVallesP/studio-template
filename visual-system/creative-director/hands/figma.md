# Figma

**Use it for:** the finished, editable version of a piece; any plate or illustration drawn from code; the brand's variables. In the October 2026 test it was the most faithful tool by a wide margin.

**Don't use it for:** fast exploration of many layouts (Claude Design is quicker to iterate), or generating imagery from a prompt.

## Feature map

| Feature | Use it for (job number in `jobs.md`) | Status |
| --- | --- | --- |
| `use_figma` (Plugin API) with generator code | Plates, frameworks, marks drawn by rule (2, 5, 6) | Tested: the best match |
| Variables, text styles, components | Holding the system (3); templates on a page (17) | Variables tested |
| Motion: keyframes per layer, text stagger, `export_video` | Animated plates and short intros (13) | Tested: works |
| Shaders (35 built in: Hatching, Halftone, Dither, Duotone and more; custom WGSL) | A finishing treatment on art or photos (5, 10) | Untested |
| `generate_image` | Prompted images inside the file | Costs Figma AI credits. Untested; use Recraft or Flora with the brand's style instead |
| `generate_diagram` | Quick flow sketches in FigJam | Mermaid flow types only, no 2x2 or Venn. Don't use for brand frameworks |
| Generative plugins | A person runs them in the app | The library is empty; the agent can't run them |
| Weave tools | Model pipelines | Not linked (link at app.weavy.ai/settings). Untested |
| `get_screenshot`, image export | Review drafts and export (15) | Tested |

Not exposed to this connector: `html_to_figma`, `generate_deck`, `generate_figma_design`.

## How a brand lives here

One file per brand (`figma.file_key`), a variables collection named after the brand (`figma.variables_collection`), and text styles. Publishing as a library for a client needs a person's yes.

## Working with the connector

1. `create_session` with the file key before any other call; reuse its id.
2. Read the `figma-use` resource before the first `use_figma` call, and `figma-generate-design` before visible changes. Pass both in `skillNames` with the `resource:` prefix.
3. Draw plates and diagrams by sending generator code, not finished SVG strings.
4. `get_screenshot` returns a short-lived URL; download it with curl into `drafts/` for review.

## Cost

Included in the Figma plan. No per-call charge seen.

## Gotchas

- Text: always `loadFontAsync` first; style names are exact (`Regular`, not `Normal`).
- Colors are 0 to 1, not 0 to 255.
- Variable paints: `setBoundVariableForPaint` returns a new paint you must assign.
- Motion: check `motionAvailable` first; the styles are `TextStagger`, `Position`, `Scale`, `Rotation`, `Size`, `Opacity` and `Path`. Review motion by pulling frames with ffmpeg, never by trusting the export.
- The test file subscribes to three community kits it doesn't need. Unsubscribe in a brand's real file.

## Test log (Oct 30, 2026, Engraved Swirl brand, 1500 × 1800 framework card)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

- `create_new_file` worked on a Full seat. (Older notes in the Engraved Swirl guide say new files fail; that was a View seat, and it's no longer true.)
- 13 color tokens became a variables collection in one call, each with explicit scopes.
- The plate was drawn by sending the generator code itself (about 4 KB) inside `use_figma`, which built six SVG layers with `createNodeFromSvg` in about 0.2 seconds. Full sky density (about 170 KB of path data) never passed through the conversation. **This is the main reason to draw plates in Figma: the art is generated inside the file, not pasted.**
- EB Garamond loaded by name (`Regular`, `Italic`); the headline is live text with the italic phrase set by range, its fill bound to the `ink` variable.
- Grain: a white rectangle set to MULTIPLY with a NOISE effect. Putting `blendMode` inside the effect object throws `Unrecognized key(s) in object: 'blendMode'`. Leave it out.
- Result: matched the reference render almost exactly. Draft: `examples/engraved-swirl-test/brands/josue-valles/pieces/2026-10-30-body-of-work/drafts/figma-card.png`.

**Motion.** The same card became a 4-second intro. Keyframes on each layer (the sky fading in, then the rough pile, the wall rising, the figure) and a `TextStagger` style on the headline, timeline set to 4 seconds on the frame. `export_video` returned an MP4 link in one call (540 × 648, 10 fps, 2.3 MB). The link expires within hours; download it right away.

- The build-up read clearly in frames pulled at 0.3, 1.2, 2.4 and 3.9 seconds: empty paper, then sky and pile, then the wall and figure.
- **The headline didn't animate as planned.** It showed fully from the first frame and shifted down about 12 pixels near the end. Check the text stagger in frames before sending; set the headline's opacity keyframes by hand if the stagger misbehaves.
- Draft: `figma-motion.mp4`.
