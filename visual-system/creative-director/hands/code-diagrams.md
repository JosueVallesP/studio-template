# Code diagrams (D2, Observable Plot)

**Use it for:** frameworks whose shape really is boxes and arrows (a sequence, a hierarchy, a flow), and charts of real numbers. Fast to revise: change the text, render again.

**Don't use it for:** brands whose style rules out boxes, or illustrated frameworks. In the Engraved Swirl test, D2 could only draw containers and rectangles, which that brand's "hairlines, not boxes" rule forbids.

## How a brand lives here

A theme generated from `tokens.json` (`code_diagrams.d2_theme` in `bindings.yaml`), plus the brand's font files.

## Gotchas

- These tools draw whatever shape you give them. The shape still comes from `taste/rules/diagram-form.md`.
- Observable Plot: not tested yet.

## Test log (Oct 30, 2026, Engraved Swirl brand)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

- The D2 install script (`curl … | sh`) was blocked in the cloud workspace. The npm package works: `npm install @terrastruct/d2@0.1.33` (D2 compiled to WebAssembly, run from Node).
- Brand colors went in through `theme-overrides` and per-class styles without trouble; `border-radius: 0` honored.
- **Fonts are the trap.** Pass the font files as plain arrays (`Array.from(fs.readFileSync(f))`). Passing a `Uint8Array` fails with `invalid JSON input`. Pass all four (`fontRegular`, `fontItalic`, `fontBold`, `fontSemibold`), or any label using a missing weight falls back to Source Sans Pro. Node labels are bold by default; set `bold: false` in their style.
- EB Garamond came from the Google Fonts repo on GitHub as a variable TTF and worked.
- Render took about 5 seconds; convert the SVG to PNG with the preinstalled Playwright for review.
- The ELK layout put the two containers at uneven heights. Fine for a draft, needs finishing in Figma.
- Drafts: `d2-structure.png` (correct fonts) and `d2-structure-fontbug.png` (the fallback-font failure), with the `.d2` source.
