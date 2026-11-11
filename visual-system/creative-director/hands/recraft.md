# Recraft

**Use it for:** illustration in a brand's trained style when exact composition doesn't matter much (a scene, a spot illustration, a texture, a first pass to refine elsewhere); calming an area of an image with a mask; removing a photo's background; upscaling for print.

**Don't use it for:** anything that needs precise layout (where the headline goes, exact proportions), exact brand colors, clean editable vectors of complex art, or keeping a layout while changing its style. Never ask it for text.

## Feature map

| Feature | Use it for (job number in `jobs.md`) | Status |
| --- | --- | --- |
| `generate_image` with a custom style | Scenes and spot art in the brand's look (5) | Tested: right look, wrong layout |
| `create_style` | Teaching the look from canon (4). Free | Existing styles used; creation untested |
| `erase_region` with a mask | Calming an area, like the space behind a headline (14). 1 credit | Tested: works |
| `image_to_image` | Restyling while keeping the layout | Tested: don't. Composition was lost even at strength 0.2 |
| `inpaint_image`, `replace_background`, `generate_background` | Area edits | Only work with v2 or v3 styles, so not with a v4 trained style |
| `image_edit` | Prompt edits with outside models | Raster only, no custom styles. Untested |
| `remove_background` | Cutting out a person's photo (10) | Untested |
| `vectorize_image` | A clean raster mark into a vector (2) | Untested. Simple marks only |
| `crisp_upscale`, `creative_upscale` | Print sizes (15). Crisp keeps detail; creative invents it, so avoid it on art that follows rules | Untested |
| `variate_image` | Variations of a draft someone liked | Untested |
| `image_to_video` | Motion | Likely not on the Free plan. Untested |
| `call_agent` (Design Agent) | Leaning toward app and marketing kits, and always runs in the personal account | Don't, for brand work |

## How a brand lives here

A trained style per brand (`recraft.style_id`), trained only from canon. List with `list_styles`. There's no update: retraining means a new style, a new id in `bindings.yaml`, and deleting the old one once nothing uses it.

**Check privacy.** Both Engraved Swirl styles are set to public. A client's style should be private. Creating a style is free, so recreating one as private costs nothing; update the id in `bindings.yaml` afterwards.

## A workflow that works

Generate the scene in Recraft, calm the headline area with `erase_region`, fix brand details in Flora, then place it in Figma or Claude Design and set all type there.

## Cost

Free plan: 30 credits a day. Raster with a custom style: 2 credits. Vector with a custom style: 4. `erase_region`: 1. `image_to_image`: 2. The tests spent 11 credits. Check with `get_user` before a batch.

## Gotchas

- Workspace: the personal account is active unless one was selected. Don't switch without asking.
- Make each mask the same size as the image, white where the change goes.
- Image URLs are public links; download outputs into `drafts/` right away.

## Test log (Oct 30, 2026, Engraved Swirl brand)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

The studio owner already had two trained styles, "Engraved Swirl" (raster) and "Engraved Swirl (vector)". Same scene prompt for both: rough blocks tumbling off a plinth, a dressed wall rising, a tiny figure carrying a block, and "leave the upper third of the sky empty for a headline."

- **Raster style: the look held.** Dashed swirling sky in blue and warm grey, grey stone, hatching, grain, a believable plate. 2 credits, 896 × 1152, delivered as WEBP even though the URL suggests PNG.
- **It ignored layout instructions.** Both runs filled the whole sky with swirls. Composition requests are suggestions to Recraft, not rules.
- **It drifted on brand details.** The figure came out as a realistic little man, not the brand's chunky silhouette.
- **Vector style: not production-ready.** 4 credits. A 3.6 MB SVG with 6,227 paths and 461 distinct greys, none matching the brand tokens exactly.
- **`erase_region` fixed the layout fault.** A mask covering the top third (white where to erase) turned the swirls there into a calm grey fade, 1 credit. A headline can sit on it. Draft: `recraft-erase-top.webp`.
- **`image_to_image` didn't.** At strength 0.45 and 0.2 (2 credits each) the output kept the look and threw away the composition. Drafts: `recraft-i2i-045.webp`, `recraft-i2i-020.webp`.
- Drafts: `recraft-raster.webp`, `recraft-vector.svg` in the test piece's `drafts/`.
