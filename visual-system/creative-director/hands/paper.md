# Paper

**Use it for:** layouts and simple vector art built as HTML that the studio owner wants to adjust by hand on his own computer; brand tokens applied as CSS variables.

**Don't use it for:** dense generated art like a full plate sky (see the size limit below), or anything in a run where the owner's computer may be off.

## Feature map

| Feature | Use it for (job number in `jobs.md`) | Status |
| --- | --- | --- |
| `write_html` artboards | Light layouts the owner tweaks by hand (8, 9) | Tested |
| `create_tokens` | Holding the system as CSS variables (3) | Tested |
| `paper-gen://` image generation (Nano Banana 2.1 at 1 usage unit; QuiverAI Arrow at 3 to 4 units, which returns editable SVG) | A quick image or simple vector art inside a layout | Untested. Arrow is the one to try for simple brand vectors |
| `export` to PNG, JPG, WebP, AVIF, SVG, PDF, MP4 or WebM (1 to 300 seconds) | Export (15); motion from an animated artboard (13) | Untested |
| `export_combined_pdf` | A multi-page PDF (11) | Needs Paper Desktop. Untested |
| `get_jsx` | Handing a layout to a developer | Untested |
| Duplicate a file | A template the owner reruns (17) | Untested |
| Comments | Read and resolve, but the agent can't post (16) | Untested |

## How a brand lives here

One Paper file per brand (`paper.file`), tokens created with `create_tokens` as CSS variables (`--color-ink` and so on).

## Working with the connector

1. `get_guide` with `paper-mcp-instructions` once per session, then override its design opinions with the brand's.
2. `get_font_family_info` before the first text.
3. Art: put generated SVG files in a connected folder on the Mac and reference them with `paper-asset://`. Paste inline only for small art.
4. `get_screenshot` per artboard; call `finish_working_on_nodes` at the end.

## Cost

None beyond the session, but large inline art costs a lot of conversation tokens.

## Gotchas

- Not for non-interactive runs.
- No `margin`, `display: grid` or tables in Paper's HTML; flex and absolute positioning only.

## Test log (Oct 30, 2026, Engraved Swirl brand, 1500 × 1800 framework card)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

- Reachable through the device bridge while the Mac and Paper were running. `create_file`, `create_tokens`, `create_artboard` all worked first time.
- `get_font_family_info` found EB Garamond (all weights, variable axis) and IBM Plex Mono, so brand fonts from Google Fonts just work.
- **Size limit is the real constraint.** Paper only takes art inline in the `write_html` call, or as a `paper-asset://` file already on the owner's Mac. The full plate is 182 KB of SVG, too big to paste. A thinned version (34 KB, about a third of the sky strokes) went in and rendered faithfully, but the sky looked sparser and less painterly than the brand calls for. Putting a file on the Mac needs a connected folder; the request for one was declined during the test.
- Every SVG element became its own layer (about 70 layers for one plate). Editable, but heavy.
- Paper's own built-in guide pushes its own taste: pick a "mood word," prefer playful accents, never mention Figma in placeholder copy. For a brand with tokens, ignore that guide's palette and mood advice and use the brand's tokens only.
- The `feTurbulence` grain filter was left out of the test, so whether Paper renders it is still unknown.
- Draft: `examples/engraved-swirl-test/brands/josue-valles/pieces/2026-10-30-body-of-work/drafts/paper-card.jpg`.
