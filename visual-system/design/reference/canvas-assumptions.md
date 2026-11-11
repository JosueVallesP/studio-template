# Canvas assumptions

Shared by all 17 skills, and by the art-direction and creative-director
plugins. This is the only file where the canvas sizes, the downscale factors,
the type floors and the default system are written. Any other file that needs
one of them points here and does not repeat the number.

**None of this comes from the video sources.** All of them are silent on
platform rendering. This file is an assumption with its reasoning shown, so it
can be checked and corrected in one place instead of drifting across ten files.

## Canvas sizes

| Use | Pixels | Ratio |
|---|---|---|
| Square post graphic | 1080 x 1080 | 1:1 |
| Portrait post graphic and carousel slide | 1080 x 1350 | 4:5 |

## The downscale factor

**Nominal: 3x.** A 1080px-wide asset lands in a feed column of roughly 360
device-independent pixels on a phone held at arm's length. So a 48px element in
the working file is seen at about 16pt.

Derivation: common phone viewports sit near 390pt wide, the feed column is
somewhat narrower after app chrome and padding, which puts the image column in
the region of 360pt. 1080 / 360 = 3.

**Stress test: 4x.** Check the piece at 25% as well. This covers a narrower
column, a smaller phone, a denser feed layout, and the case where a square
asset is cropped and shown smaller. A piece that survives 4x is safe; a piece
that only survives 3x is at the edge.

**Consequences that follow, and are used in the skills:**
- Smallest rendered size you can rely on is about 12pt, so there are **two
  working-file floors and a floor figure quoted without its case is
  incomplete**. At the nominal downscale the floor is 12 x 3 = **36px**. At the
  stress case it is 12 x 4 = **48px**. Both are correct about different things:
  36px is what a piece must clear to be readable in a normal feed column, 48px
  is what it must clear to stay readable when the column is narrower, the phone
  is smaller, or the asset is cropped and shown smaller. Nothing in a post
  graphic goes below 36px. Anything that must still be read under the stress
  case is set at 48px or above, and anything nobody has to read may sit at 36px
  provided the file says so.
- A step in a type scale must be visible after division by 3. A 1.125 ratio
  puts 48 next to 54, which is two pixels apart once rendered, so it is one
  level wearing two names.
- Absolute values borrowed from UI and web work (16px body, 12px minimum,
  4 and 8px spacing units) are device-independent pixels. Multiply by the
  downscale factor before using them on a canvas, which is also why the 4 and
  8 unit convention does not transfer: its reason is whole-pixel rendering, and
  a non-integer downscale voids that.

## What is not assumed here

- **Crop behaviour.** Platforms crop and re-render assets in ways that change
  over time and differ by surface. Treat any crop-safe margin as extrapolation,
  not as a specification. Verify against a real post before relying on it.
- **Desktop rendering.** The 3x figure is the phone case, which is the strict
  one. Desktop feeds show images larger, so a piece built for 3x is
  comfortable there.
- **Dark and light app backgrounds.** Handled in `dsn-color` and
  `dsn-contrast`, not here.

## The default system for a 1080 canvas

One set of numbers for both canvases. Every skill uses these wherever the brand
gives no value of its own, and no skill derives a different set. They are a
chosen default with the reasons shown, in the same spirit as the rest of this
file. A brand's own tokens replace any of them.

| What | Value | Why |
|---|---|---|
| Spacing unit | 24px | Divides 1080 into 45 whole units. Renders as 8pt at 3x and 6pt at 4x, still a visible gap |
| Margin, all four sides | 72px | Three units. Renders as 24pt at 3x and 18pt at 4x |
| Gutter | 24px | One unit |
| Columns | 6, each 136px | (1080 - 2 x 72 - 5 x 24) / 6 = 136 |
| Gap ladder | 24, 48, 96, 144, 216 | Each step is at least 1.5 times the one before, so two neighbouring steps never read as the same gap |
| Type ladder | 36, 48, 72, 96, 144 | See below |

**The type ladder.** 36px is the nominal floor and 48px is the stress-case floor,
both from the section above. 48 is the default size for body text, because body
text must survive the stress case. 36 is only for text nobody has to read under
the stress case, such as a source line. Above the body size: 72 is 1.5 times 48,
96 is 2 times 48, and 144 is 2 times 72. The smallest difference between two
neighbouring sizes is 12px, which is 4pt at 3x, so every step stays visible after
the downscale. Every size is a multiple of 12, so type and spacing share one unit.

**Which sizes a frame uses.** A frame does not use all five. It uses the sizes
its ranks need, and the skill that owns hierarchy says how many ranks a frame
can hold.

**Where a skill's worked example shows other numbers.** Some skills still carry
a worked example built on a 90px, 96px or 128px margin, or on another spacing
unit. Those are illustrations of a method. The table above is the system to
build with.

## A canvas that is not 1080 wide

The floors scale with the canvas width, because the feed column stays the same.

- Nominal downscale = canvas width / 360. Stress downscale = canvas width / 270.
- Nominal floor = 12 x canvas width / 360. Stress floor = 12 x canvas width / 270.
- Worked for a 1500px-wide canvas: 1500 / 360 = 4.17, so the nominal floor is
  12 x 4.17 = 50px. 1500 / 270 = 5.56, so the stress floor is 12 x 5.56 = 67px.
- Scale the default system by the same factor (canvas width / 1080) and round
  each value to a whole pixel.

## How to correct this file

Post one real graphic containing a ruler of known pixel widths, screenshot it
on the target device, and measure. That single test replaces every estimate
above. Until someone does it, these are reasoned assumptions and the skills say
so.
