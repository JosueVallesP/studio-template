# Choosing the tool

Start with `<plugin>/hands/jobs.md`, which maps each job (signature art, frameworks, photos, motion, fixes, exports, review, templates) to a tool and the feature to use. The table below is the short version for the most common pieces. Prefer features marked tested; an untested feature gets tried on a draft first and noted in `piece.md`.

Pick by what the piece needs most. Each tool's notes in `<plugin>/hands/` say what it actually did on a real brand; read the chosen tool's notes before using it. Choose only from the tools listed in the workspace config.

| The piece needs | Start with | Why (from the October 2026 test) |
| --- | --- | --- |
| A plate, illustration or diagram the brand draws by rule (exact palette, exact layout) | Figma, with generator code sent inside `use_figma` | Full-density art generated in the file, brand variables bound, live text. Matched the reference almost exactly |
| A layout of type and placed images (posts, carousels, one-sheets, headers, landing pages) to tweak and share by link | Claude Design, on the brand's Design System | Live editable type; art goes in as an uploaded image |
| A scene or spot illustration where exact composition matters less | Recraft with the brand's trained raster style | Holds the look well for 2 credits; ignores layout instructions and drifts on small brand details |
| A fix to an image someone already likes (swap a detail for the brand's version, restyle, upscale) | Flora image-to-image | Fixed a figure cleanly for $0.08; weak at clearing exact areas |
| A framework that really is boxes and arrows, or a chart of real numbers | Code diagrams (D2, Observable Plot), then finish in Figma | Exact structure from text; only boxes, so wrong for brands that forbid them |
| Motion: an animated plate or a short intro | Figma keyframes and `export_video` | Built the card up layer by layer into a 4-second MP4 in one call; check the headline animation in frames |
| A crop, pad or color treatment for export | Flora free actions | Padded a plate to a square in the brand's paper color for $0 |
| A light layout the studio owner wants to adjust by hand on his own computer | Paper | Faithful rendering, but art over about 30 KB can't be pasted in |

## Combining

The tests point to one strong pattern for illustrated brands: draw the scene in Recraft, calm the headline area with Recraft's `erase_region`, fix brand details in Flora, then place it in Figma or Claude Design and set all type there. Image models carry a look but not a layout, and they can change what a shape means, so every image-model draft goes through `cd-review` before anyone sees it. For brands whose art follows strict rules, skip the image models and generate the art in Figma.

## When the obvious tool can't do it

Say so, pick the next best, and note it in `piece.md`. If no listed tool fits, describe what's missing to the studio owner instead of forcing it. A new tool gets a `hands/` file, not a change to this skill.

## Keep mode

Prefer the tool the existing brand was made in. If canon pieces came from Figma, finish in Figma.
