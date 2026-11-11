# Jobs and which tool does each

`cd-make` reads this before `choose-hand.md`. Each tool's own file in `hands/` has the details and the gotchas.

The jobs a creative director does for a personal brand, and which tool and which feature of that tool does each one. **Tested** means it ran on a real brand (the Engraved Swirl brand, October 30, 2026) and the result is in the test piece's `drafts/`. **Untested** means the feature exists and looks right for the job, but nobody has run it yet. Try it on a draft before promising it to a client.

## Setting the brand up

| Job | Use | Feature | Status |
| --- | --- | --- | --- |
| 1. Explore directions before one is approved | Claude Design | A Design canvas with one artboard per direction, side by side, shared by link | Tested (single card) |
| | Flora | Multi-reference image (`is2i-elote-gateway`, about $0.05): feed the person's reference images, get a sample in that look | Tested: carried the look well, ignored layout |
| | Recraft | A basic style, or the person's own references turned into a quick style with `create_style` (free) | Untested for exploration |
| 2. Make or clean up the mark | Figma | Draw it as vectors, by hand or from code | Untested for marks |
| | Recraft | `vectorize_image` to turn a clean raster mark into a vector | Untested. Only for simple marks; a plate came out as 6,000 paths |
| 3. Hold the system | The repo | `system/tokens.json` is the source; `cd-system` copies it out | Tested |
| | Claude Design | A Design System artifact (needs the list-shaped token format) | Tested |
| | Figma | A variables collection, text styles, components on a page | Tested (variables) |
| | Paper | `create_tokens` as CSS variables | Tested |
| 4. Teach image tools the look | Recraft | `create_style` from canon images. Free. Set it private | Tested (styles already existed) |
| | Flora | LoRA trainers (Flux 2, Krea 2, Recraft V4 style) | Untested. Cost unknown; the connector can't delete a trained LoRA |
| | Code | For rule-drawn brands, the generator code is the trained look (`plate-generator.mjs` in the test). Keep it in `<brand>/system/` | Tested |

## Making pieces

| Job | Use | Feature | Status |
| --- | --- | --- | --- |
| 5. Signature art (plates, scenes) | Figma | Generator code sent inside `use_figma`; the art is drawn in the file | Tested: the best match |
| | Recraft | The brand's trained raster style, 2 credits | Tested: right look, wrong layout |
| | Flora | Multi-reference with canon as the style source | Tested: right look, wrong layout, one shape read wrong |
| | Figma | Built-in shaders (Hatching, Halftone, Dither, Duotone) as a finishing treatment on art | Untested |
| 6. Frameworks (2x2, Venn, field guide, flow) | Figma | Hairlines and shapes from code, so the shape follows `diagram-form.md` | Tested (the card) |
| | D2 | Boxes and arrows from text, then finished in Figma | Tested: boxes only |
| | Figma | `generate_diagram` | Don't use: Mermaid flow types only, into FigJam, no 2x2 or Venn |
| 7. Charts of real numbers | Code | Observable Plot or D3 with the brand's tokens, then placed in Figma or Claude Design | Untested |
| 8. Social posts (card, post art, carousel) | Claude Design | One artboard per card or slide, live type on the Design System, art uploaded as an image | Tested (card) |
| | Figma | The finished, editable version | Tested (card) |
| 9. Substack (headers, inline diagrams) | Claude Design or Figma | Same as social, at the format's size | Untested at Substack sizes |
| 10. Photos of the person | Recraft | `remove_background`; `crisp_upscale` | Untested |
| | Flora | Free actions for a consistent treatment: color grade, color tint, duotone shader, crop or pad | Pad tested; the rest untested |
| | Any image model | Restyling a face | Don't: models change faces. Treat the photo, never redraw the person |
| 11. Composed pieces (one-sheet, speaker page, deck) | Claude Design | A Design canvas with print size and "All artboards .pdf"; "Make from this" turns it into a deck; the Slides type exports .pptx and PDF | Untested |
| 12. Mockups (book cover, booth, stage slide) | Flora | Image-to-image placing brand art into a scene; the `flora-mockup-deck` skill | Untested |
| 13. Motion (animated plate, short intro) | Figma | Keyframes on each layer, text stagger on the headline, `export_video` to MP4 | Tested: works |
| | Flora | The free `ken-burns-video` action on a still | Untested |
| | Paper | Export to MP4 or WebM (1 to 300 seconds) | Untested |
| | Claude Design | No motion type | Don't |

## Fixing and finishing

| Job | Use | Feature | Status |
| --- | --- | --- | --- |
| 14. Fix an image | Flora | Image-to-image for a detail (swap a figure for the brand's version), about $0.08 | Tested: clean |
| | Recraft | `erase_region` with a mask image, 1 credit, to calm an area | Tested: gave a calm grey fade, usable behind a headline |
| | Flora | Free `magic-eraser` and `pixel-remover` actions | Untested |
| | Figma | Anything with an exact area or position | Tested |
| | Recraft | `image_to_image` to keep a layout while changing style | Don't: composition was lost even at strength 0.2 |
| | Recraft | `inpaint_image`, `replace_background`, `generate_background` | Only with v2 or v3 styles, so not with the brand's v4 trained style |
| 15. Export | Figma | Image export; `export_video` for motion | Tested |
| | Flora | Free pad or crop to an aspect ratio (a 5:6 plate to a 1:1 square, padded in the brand's paper color) | Tested |
| | Recraft | `crisp_upscale` for print sizes | Untested |
| | Claude Design | Print PDF, "Send to Canva" | Untested |

## Working with people

| Job | Use | Feature | Status |
| --- | --- | --- | --- |
| 16. Client review | Claude Design | A share link; comments pinned to the artboard | Untested. Claude only sees threads sent to it |
| | Flora | Comment threads the agent can post and read | Untested |
| | Paper | Comments the agent can read and resolve, but not post | Untested |
| | The repo | `log.md` records every decision a person makes, whatever tool the comment came from | Tested |
| 17. Templates the team reruns | Flora | Techniques: a saved pipeline anyone can run. Built in the Flora app; the connector can only run them | Untested |
| | Flora | Custom actions (code) for a repeatable transform | Untested |
| | Figma | Components on a page of the brand file (the Editorial Print System file already has plate components on page 07) | Untested |
| | Paper | Duplicate a file as a template | Untested |
| | Claude Design | The Design System plus a canvas used as the starting point | Tested |

## Patterns that held across tests

- **Image models carry a look, not a layout.** Recraft and Flora both kept the brand's sky, palette and grain, and both ignored "keep the top third empty." Plan a second step for layout, or draw rule-bound art in Figma.
- **Image models can change what a shape means.** Flora's milestones came out as gravestones. A row of rounded stones on a road says death, not progress. The `form` and `fidelity` reviewers must check what each shape reads as, not only how it looks.
- **Set type outside image tools.** Every tool that set live type (Figma, Claude Design, Paper) did it well; no image model is asked for words.
