# Keep mode: extract and lock

In keep mode the brand already exists and the job is to protect it. Write down what the brand is, so nothing made later drifts from it.

## 1. Gather the evidence

- The existing site: run the `site-teardown` skill when it's available, or read the pages and their CSS, to get exact colors, fonts, sizes and spacing.
- Existing pieces the person called "right" during intake. Ask them to put the best ones in `canon/` now; you can't put them there yourself.
- Any brand guide, logo files or Figma files they shared.

## 2. Write what you find, exactly

Fill `direction.md`:

- **Target association:** from the brief. In keep mode it describes what the brand already does.
- **The contradiction:** write "Keep mode protects the existing brand, so this direction sets no contradiction." If the existing brand clearly carries one, describe it in one line as something you observed.
- **Visual codes:** what the brand actually does on each lever, with exact values (hex codes, font names and weights, sizes). Use one column, headed "Existing."
- **Recurring shapes:** the ones the brand already uses.
- **Never:** things the existing brand clearly avoids, plus anything the person said they never want.
- **Locked and flexible:** list every element under Locked by default. Move something to Flexible only when the person says it can vary.

Values you can't confirm from a source (a color you only saw in a compressed image) go under "Waiting on a person" in the brand's `context.md`, not into the direction.

## 3. Note gaps without filling them

List the formats and situations the brand doesn't cover yet (a carousel, a chart, a dark background). Don't design for them. Add them to `context.md` under "Waiting on a person." `cd-make` will pick the most conservative option in each case and flag it, as `keep-mode.md` says.

## 4. Propose and approve

Show the person the Locked list and the gaps. Approval follows the main skill's Step 5.
