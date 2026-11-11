# Flora

**Use it for:** fixing or adjusting an image someone already likes, in a second step (swap a detail for the brand's version, upscale); a quick sample in a brand's look from reference images; free finishing transforms (crop, pad, color grade, tint); and pipelines a team reruns, saved on a Flora canvas.

**Don't use it for:** precise layout changes (clearing a defined area, moving things to exact positions), anything with text, or redrawing a person's face.

## Feature map

| Feature | What it is | Use it for (job number in `jobs.md`) | Status |
| --- | --- | --- | --- |
| Generations | 192 image, 227 video, 31 image-to-text, 22 3D and 9 audio models | Image-to-image fixes (14); multi-reference samples (1, 5); mockups (12) | Fixes and multi-reference tested |
| Actions | 42 prebuilt transforms that cost nothing: crop, pad to aspect, resize, color grade, tint, filter, duotone and halftone shaders, magic eraser, add text, Ken Burns video, stitch video | Export sizes (15); a consistent photo treatment (10); cheap motion from a still (13) | Pad tested; the plan includes actions |
| Custom actions | Your own transform written in JavaScript or Python, saved to the workspace | A brand-specific step, like snapping colors to the brand's tokens | Untested |
| Techniques | A saved canvas pipeline anyone can run with new inputs | Templates the team reruns (17) | None in the account. The connector can run them but not create them; build them in the Flora app |
| LoRA trainers | Train a model on a brand's look (Flux 2, Krea 2, Recraft V4 style and vector style) | Teaching the look (4), once canon has enough pieces | Untested. Cost unknown; the connector can't delete one |
| Image-to-text models | Cheap vision models (from about $0.001 a call) | A second pair of eyes on a draft, alongside `cd-review` | Untested |
| Comments | Threads the agent can post, read and reply to | Client review (16) | Untested |
| Library (assets) | Files uploaded to the workspace, fetched from a public URL | Keeping canon and inputs next to the pipelines | Tested |
| Flora skills | 18 ready workflows (batch generate, mockup deck, refine loop) | Check `flora_discover_skills` before building a pipeline by hand | `flora-brand` needs tools this connector doesn't have |

Decks made in Flora can't be exported through the connector.

## How a brand lives here

A Flora project per brand (`flora.project_id`). Each generation leaves a node on the canvas, so a working sequence (Recraft scene, then a Flora brand-detail fix) can be turned into a technique in the Flora app (`flora.techniques`) and rerun by the connector. A trained LoRA, if any, goes in `flora.lora_id`.

## Working with the connector

1. `flora_list_workspaces`, then `flora_create_project` (or reuse the brand's).
2. `flora_list_models` with a `model_id` to get its parameter names (`image_url`, `image_urls`, `aspect_ratio`, `resolution`).
3. Always run once with `quote: true`, tell the studio owner the dollar cost, then run for real.
4. Actions: read the declared params with `flora_get_action` first; undeclared keys are rejected. `flora_run_action` doesn't touch the canvas; read the output with `flora_list_generations`.
5. Poll no faster than every 15 seconds. Never retry a batch after a partial failure; check history first.

## Cost

Reported in US dollars. Image-to-image at 2K: $0.077. Multi-reference at 1K: $0.052. Actions: free. Nano Banana Pro runs about $0.18 an image; a Magnific upscale about $0.175. The account had $22.92 before the second round of tests and spent $0.13 across all of them.

## Gotchas

- Prompts that say "change only X" mostly hold for details, less for areas.
- Image outputs come back as public `media.flora.ai` links; download them into `drafts/` right away.
- The test canvas nodes aren't wired together, so the canvas doesn't yet show the pipeline. Wire them (`reference_node_ids`) when building something to turn into a technique.

## Test log (Oct 30, 2026, Engraved Swirl brand)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

**Fix (image-to-image).** The test took Recraft's raster plate, which had two faults (sky swirls filling the headline area, and a realistic figure instead of the brand's chunky silhouette), and asked Flora to fix only those two things.

- Upload: `flora_create_asset` fetched the public Recraft URL server-side into the project. No download or re-upload needed.
- Nano Banana 2.1 image-to-image (`i2i-elote-gateway`) at 2K quoted $0.077 and charged exactly that. Done in about 30 seconds.
- **The figure fix worked.** The realistic man became a solid black chunky silhouette carrying a block, and everything else held: stone, sky, palette, grain.
- **The layout fix half worked.** It cleared a hard-edged horizontal band in the sky instead of a calm upper third. The band reads as an edit. Draft: `flora-fix.png`.

**New scene from references (multi-reference).** Two brand plates as style references and a new scene in the prompt (a figure on a road with milestones growing taller), `is2i-elote-gateway` at 1K, 4:5. Quoted and charged $0.052.

- **The look carried very well**: the dashed swirling sky with blue strokes, hatched ground, warm grey paper, small dark figure.
- **It ignored layout again.** The sky filled the whole top half; "keep the top third empty" was dropped.
- **A shape changed meaning.** The rounded milestones read as gravestones, so a picture meant to say "progress" says "death." Draft: `flora-multiref-newscene.png`.

**Free action.** `change-image-ar-browser` padded the 1856 × 2304 fix to a 2304 × 2304 square in the brand's paper color (#E6E4DF). Charged $0, done in 10 seconds. Draft: `flora-action-pad-1x1.png`.
