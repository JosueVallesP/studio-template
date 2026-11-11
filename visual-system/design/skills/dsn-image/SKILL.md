---
name: dsn-image
description: Choosing or judging photography in a layout, rescuing a poor supplied photo, setting a claim over a picture, or briefing a shoot. Gives the image's job and a type spec.
---

# Image

This skill decides which picture a piece uses, what that picture is doing, and what the picture gives up so the claim on top of it can be read. The single idea underneath it is that a photograph in a layout is not a background: it is the largest element on the canvas and it has a focal point of its own, so it either carries the piece's first look or it competes with whatever does. Grading cannot settle that competition, because recolouring an image moves every tonal value in it and leaves the focal point exactly where it was. An image can be composed correctly and still be the wrong picture, and that gap is what this file covers.

## What this skill is for

Use it when someone wants to:

- decide whether a photograph is working in a layout, or say why it is not
- choose between candidate images for one slot
- rescue a mediocre supplied photo that has to carry a piece with no reshoot available
- set a claim over a picture without wrecking either
- build a moodboard that constrains the work instead of decorating a pitch
- brief a photographer when you are not the photographer

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings: nothing in this file rests on a controlled study, a tested comparison, or any measurement of an image against an outcome. Rules marked **(thin)** rest on a single account, or on a convention chosen rather than derived, and should be treated as one person's house style rather than craft consensus.

The markers are dense in this file, so read a marked rule as an experiment worth running on a real post rather than as a law. Most of them are cheap to test that way. Where a value is a working default chosen for this skill rather than a derivation, it says so at the point of use and can be replaced with anything measured.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Claim.** The one line of type the piece exists to land. Everything else on the canvas, including the photograph, is measured against whether the claim can be read and believed.

**Subject.** The person, object or product the photograph is of. Distinct from the focal point: a picture of a person holding a kettle has one subject and may have its focal point on the kettle, and that split is the usual reason an image argues with the copy.

**Aspect ratio.** Width to height expressed as a ratio, with the pixel count stripped out. 1080 x 1080 is 1:1, written square here. 1080 x 1350 is 4:5, written portrait. Two canvases can share a ratio at different pixel counts and need the same crop.

**Full bleed.** An image running to all four canvas edges with no margin around it, so the image area equals the canvas area.

**Crop.** Choosing a rectangle inside the photograph and discarding everything outside it. A crop changes the apparent camera angle, the subject's position in frame and the aspect ratio, and it spends pixels it cannot get back.

**Margin, live area, column, gutter, span.** The margin is the band of empty canvas at each edge. The live area is what the margins enclose, which is where every element sits. Columns are equal vertical divisions of the live width; a gutter is the gap between two adjacent columns; a span is a run of columns plus the gutters between them, used as the width of one element. All five are computed for both canvases in Applied.

**Safe area.** The part of the canvas you can rely on surviving a platform's own re-cropping. Treated here as the live area, and treated as extrapolation rather than specification, because crop behaviour differs by surface and changes over time.

**Level one, level two, texture.** Three jobs an image can hold. Level one means the image is the first thing seen and carries the idea. Level two means the image is evidence under a claim that is carried by type. Texture means the image supplies surface and tone under type and has no focal point the reader is meant to find. These are three different pictures, not three crops of one.

**Focal point.** The single place in an image a viewer's eye lands first, findable by blurring the image until detail is gone and seeing what is left.

**Spanning edge.** The edge of the image that has to cover the full width or height of the canvas. If an image runs full bleed across a 1080px canvas, its spanning edge is the one that must supply 1080px.

**Dimensions versus resolution.** Dimensions are the pixel count of the file, 820 x 1230 for instance. Resolution, as this file uses it, is how much real detail those pixels carry. The two come apart as soon as a file has been enlarged: an image can have the dimensions a canvas needs and none of the detail, which is why every check below measures the edge of the original rather than the edge of the placed image.

**Upscaling.** Enlarging an image past its own pixel dimensions, where the software invents the pixels it adds by averaging neighbours. It raises dimensions and cannot raise resolution.

**Quiet region.** A continuous area of the image holding close to a single tonal value, so type set across it does not cross a light-to-dark boundary.

**Tonal value.** How light or dark an area is, independent of its hue. A navy field and a mid-grey field can hold the same tonal value.

**Greyscale.** An image with hue discarded and tonal value kept, so every pixel is a shade of grey.

**Relative luminance.** A number from 0 for black to 1 for white measuring how much light a colour emits, weighted for human sensitivity. Compute it by taking each of the red, green and blue channels as a fraction of 255, linearising each with `c / 12.92` when `c` is at or below 0.03928 and `((c + 0.055) / 1.055)` raised to the power 2.4 otherwise, then summing `0.2126 x R + 0.7152 x G + 0.0722 x B`.

**Contrast ratio.** `(L_lighter + 0.05) / (L_darker + 0.05)`, where each `L` is a relative luminance. Runs from 1:1 for two identical colours to 21:1 for black on white.

**Large type and body type, as the thresholds here use them.** Large means 18pt or more at the size the reader actually sees, and needs a 3:1 contrast ratio. Body type is anything smaller and needs 4.5:1. Both ratios are taken from the published accessibility standard rather than derived in this file, and both are stated as rendered sizes, so convert a working-file pixel size with the downscale factor before deciding which applies.

**Opacity.** The share of a covering layer's own colour that reaches the eye, from 0 for invisible to 1 for solid. A black layer at 0.6 opacity leaves each pixel beneath it at 40 percent of its original luminance, which is the arithmetic every scrim calculation below uses.

**Plate.** A solid block of one colour placed behind type, sized to the type block plus padding.

**Scrim.** A flat darkening or lightening applied across the whole image to drop its luminance uniformly, so type can clear a contrast threshold anywhere on it.

**Band.** A strip of flat colour outside the image, usually at an edge of the canvas, with the type sitting in it rather than on the picture.

**Comping.** Assembling one final image from parts of several photographs: a prop, an object, a hand or a background dropped in from another frame.

**Duotone.** An image mapped to two colours, typically one dark and one light, so all hue information in the original is discarded.

**Downscale factor.** The ratio between a working-file pixel and what a viewer actually sees. `reference/canvas-assumptions.md` sets the nominal at 3x and the stress test at 4x, so a 36px element in the working file renders at about 12pt on a phone, and at 9pt under the stress case.

**Feed size.** The size the piece is actually seen at, which is the canvas divided by the downscale factor. Every legibility decision in this file is made at feed size and not at build size.

**Application background.** The surface the piece is shown against inside an app, near-black in dark mode and near-white in light mode. A piece has to hold on both, because the reader picks which one and you do not.

**Leading.** The vertical distance from one line of type to the next, stated here as a multiple of the type size. Type at 108px with leading of 1.15 puts 124px between lines.

**Measure.** The length of a line of type, counted in characters rather than pixels, because characters are what determines whether a claim breaks where you want it to.

**White sweep.** A seamless white backdrop curving from the wall down to the floor, so a product photographed on it has no visible horizon line and no shadow edge to place it anywhere.

**Moodboard, internal and client-facing.** Two documents with different jobs. The internal board is a working surface for finding the direction. The client-facing board is an argument that the direction is right, made to someone who will approve or kill it.

## The principles

1. **Choose one deliberate difference per image and name it in a sentence before anything is shot or cropped.** **(thin)** The mechanism is attention in a scrolling column: a viewer passing a run of conventional images stops on the one that is not conventional, so the difference has to be a decision rather than something noticed afterwards. The sentence must name an object, an action, an angle or a light condition. "A nice photo of the product" names nothing. "The product on a chair carried halfway up a hill" names one. Checked by the one-thing test.

2. **State what the subject is doing as a verb, and if there is no verb, supply the activity and the prop.** **(thin)** The mechanism is a cost argument: an activity is free and composition is a skill, so when the camera is not in professional hands the activity carries more of the image than the framing does. The practical form is the hands problem. Empty hands pose; hands holding a book, a tool or a bag do something. A prop that does not function still works in frame. Checked by the verb test.

3. **Treat the image as a level in the hierarchy and assign that level in writing before choosing the picture.** A full-bleed image on a 1080 x 1350 canvas occupies 1,458,000 pixels, and no element of type on that canvas comes close, so by area the image is the largest thing present whatever job you intended for it. That is why an unassigned image defaults to level one and competes with the claim: nothing demoted it. Checked by the blur-the-type test.

4. **Keep a reference only if you can name the one quality you are taking from it.** **(thin)** The mechanism is that a board constrains work by telling people what to do, and an image nobody can account for tells them to do all of it. The quality has to be one of colour, composition, treatment, material, lighting or cultural reference, named specifically. Saving what you like and calling it direction is collecting, not referencing. Checked by the caption test.

5. **Decide whether a used format is acceptable by locating the audience, not by consulting your own fatigue.** **(thin)** A format practitioners consider finished still lands with an audience that has seen it once or twice, because the people who are sick of it are the people who make the work. The inverse holds for an audience that follows the category closely, where the same format reads as late. Name where this audience sits before calling a reference tired. Checked by the audience-position test.

## How to work

### Mode A: art-directing imagery for a piece

1. **Write the claim in one line.** The image serves that line. Everything after this step is subordinate to it.

2. **Assign the image's job: level one, level two as proof, or texture under type.** Write it down. An image with no written job will arrive as level one by area, per principle 3.

3. **Pick the one deliberate difference, cheapest column first: action, then angle, then location, then light.** **(thin)** Action and angle cost nothing: a prop and a stool reach both. Location costs travel. Light costs a photographer. Working down that order means you exhaust the free generators before you commit money, and most pieces never need to leave the first two.

4. **Write the verb.** With no verb available, invent the activity and supply the object, per principle 2.

5. **Add one out-of-place element if the image still reads as conventional.** **(thin)** The mechanism is that an element the viewer cannot immediately account for holds them a beat longer than one they can. A chair carried up a hill, a garment rack dragged into the street, a model on a treadmill in heels.

6. **Choose the angle.** **(thin)** A high angle flatters almost any face; a low angle makes a subject look deliberately unflattering, which is usable when that is the point. Shooting downward needs about two steps of height above the subject, which a stool supplies. No mechanism is offered for any of these three, and they are cheap to check against a real face in ten minutes.

7. **Decide where the type sits before the shoot or before the crop, and keep that region quiet.** Compute the region first, using the arithmetic in the Applied section, then frame or crop to produce it. The other order is how a good photograph and a good headline ruin each other: both are finished, neither can move, and the only remaining tool is a scrim.

8. **Brief a photographer with references in four groups, angle, action, location and light, and let them name the technique.** **(thin)** The unit you hand a collaborator is a reference, not an instruction, because a reference carries the result you want and leaves the method with the person who owns it.

9. **For a brand rather than a one-off, fix a sandbox first and select from it afterwards.** **(thin)** Four things go in the sandbox: iconography the concept itself produces rather than carries, which means the brand's marks appear because of what is being photographed rather than being applied on top; one narrow lifestyle adjacency; one portrait philosophy; and two or three recurring signatures. The count of signatures is read off a single brand, not offered as a target. Selecting from a fixed sandbox is what makes a run of pieces read as one brand rather than as a set of individually defensible decisions.

10. **Run the tests table in order, then the ultimate test.**

### Mode B: judging an image or a layout that already exists

Work in this order and stop at the first failure. The order is derived rather than reported: it runs cheap, decisive checks before expensive, arguable ones, so a piece that fails on job assignment never consumes a grading review.

1. **Job.** Is the image level one, proof, or texture? An image with no stated job is decoration, and every finding after this point is about the wrong picture.

2. **One thing, then the verb.** Principles 1 and 2. An image whose difference cannot be named is the failure that gets described as "looks like stock", and it is the failure that grading and colour never rescue.

3. **Argument with the copy.** Blur the type until it is unreadable, name the image's focal point, and say whether that focal point is the claim's subject. A focal point unrelated to the claim is a second headline.

4. **Claim legibility at viewing size**, on both dark and light application backgrounds. Measure the claim, not the photograph. The arithmetic is in Applied.

5. **Craft.** Spanning-edge resolution, horizon level, what the crop destroyed, skin and product colour, compression blocking, sharpening halos.

6. **Report the smallest fix per failure, ordered by impact, with the tier of each finding named.** Tiers are in "Writing the output".

## Choosing between candidate images

Judging one image is a yes or no against principles 1 to 3. Choosing among several is a different operation, and running it as a beauty contest produces the wrong answer because the criterion a client can judge in isolation is the last one that matters. Rank by what each image gives the layout, in this order:

1. **Does it leave a quiet region where the claim goes, at the size the claim needs?** A worse photograph with a usable sky beats a better one with detail across the whole frame, because the better one costs you the claim, a plate, or the photograph itself.
2. **Does its focal point agree with the claim?**
3. **Is the deliberate difference nameable?**
4. **Does the spanning edge meet the canvas, per the resolution arithmetic below?**
5. **Only then: is it the better picture?**

An image that wins on 5 and loses on 1 costs you either the claim or the photograph, since the only remaining tools are a plate over the picture or a smaller claim. Treat the ranking as the instruction.

When the subject sits on a plain background and there is no location to work with, two generators are cheap. **Scale ambiguity** **(thin)**: frame so the viewer cannot tell whether the bag is huge or the table tiny, which holds attention while they resolve it. **Partial reveal** **(thin)**: show less than the whole object, so the frame implies a shoot the viewer cannot see all of.

## When the supplied photo is poor

This is the normal case, not the exception. Work down the ladder in order and stop at the rung where the piece works. Every rung is derived rather than reported, and each one's cost is stated so you can tell what you are spending.

1. **Crop to manufacture the one deliberate difference.** A crop creates an angle the camera did not have, cuts the office out of a headshot, isolates a hand, and opens a quiet region where there was none. Free, and usually sufficient. Check the spanning edge against the resolution floor first, because cropping spends resolution and cannot get it back.

2. **Demote the image to level two.** Small, bottom-anchored, high contrast, with the claim set in type on a flat ground above it. The mechanism is area: at a two-column inset the image occupies a small fraction of the canvas, so its flaws fall below the size at which they can be read, while the same flaws at full bleed are the piece. A small mediocre photograph reads as a credential. A large one reads as the work.

3. **Convert it to texture.** Hard crop, then greyscale or a single-colour duotone. Greyscale discards the colour channels, so a wrong white balance and poor skin rendering cannot be read at all: there is no hue left to be wrong. This removes two specific failure modes and nothing else, so it does not fix a soft or badly framed image.

4. **Add the one deliberate difference in post.** Comping a prop, an object or a hand into the frame is standard practice at the top of the market rather than a patch. **(thin)**

5. **Add it physically.** **(thin)** One object placed in the subject's hands costs about thirty seconds and converts a pose into an action, per principle 2.

6. **Replace the image with type on a flat ground.** This is a decision and should be reported as one, not as a failure to deliver a visual.

**Do not upscale and sharpen.** The downscale to feed size averages neighbouring pixels, which hides softness and preserves high-contrast edges. Sharpening halos and compression blocks are high-contrast edges, so the downscale preserves exactly the artefacts upscaling introduces while forgiving the softness it was meant to fix. Soft is recoverable. Crunchy is not.

**Resolution, computed.** The canvas is 1080px on the spanning edge, so an image running full bleed needs 1080px on that edge in the working file. Below that you are upscaling. A 540px image upscaled 2x to fill the frame is soft at build size and can survive the phone view, because 1080 / 3 = 360 rendered pixels and the averaging hides the softness, but it has nothing left for a crop and it fails as soon as the asset is viewed larger than the feed column. Treat 1080 as the floor and anything below it as borrowed.

**For features inside the image that must be read, divide by three.** A feature needs 12pt rendered to be legible, and the nominal downscale is 3x, so it needs 12 x 3 = 36px in the working file. Under the 4x stress case the same 12pt requires 12 x 4 = 48px. Measure the feature, not the file: a face occupying 100px of a 296px-wide inset is 100px, and 100 is above 48, so it reads. A product label occupying 30px does not, under either factor.

## Type over a photograph

Everything in this section is derived from the canvas arithmetic and the contrast formula rather than reported, so each step is shown as a derivation and can be checked line by line.

**Choose the quiet region first, then crop to it.** When the claim is level one, the photograph serves the type. Find the least varied region in the image, then crop so that region lands where the claim goes, per Mode A step 7.

**Blur the image heavily and look only at where the type will sit.** More than one tonal value in that area means the type crosses a boundary, and it will fight the picture at some sizes and on some screens even where it reads on yours.

**Compute the luminance ceiling the region has to meet.** Take 3:1 for large type and 4.5:1 for body type, per the thresholds defined above. For white type, solve `1.05 / (L + 0.05)` for the threshold: at 3:1 the lightest pixel under the type must sit at or below `1.05 / 3 - 0.05 = 0.30` relative luminance; at 4.5:1 it must sit at or below `1.05 / 4.5 - 0.05 = 0.183`. For black type on a light region, solve `(L + 0.05) / 0.05`: the darkest pixel must sit at or above `3 x 0.05 - 0.05 = 0.10` for 3:1, and at or above `4.5 x 0.05 - 0.05 = 0.175` for 4.5:1. Measure the extreme pixel in the region, not its average, because the average passes while the type crosses the part that fails.

**Three honest repairs when no quiet region exists**, in order of what each costs the photograph.

- **A plate.** A solid block behind the type, sized to the type block plus padding. Cheapest, and it reads as a deliberate element rather than as a fix. It costs the area it covers and nothing else.
- **A scrim.** Flat darkening across the whole image. Compute the opacity from the measured ceiling: to bring a lightest pixel at 0.75 relative luminance down to the 0.30 white-type threshold, a black overlay needs `1 - (0.30 / 0.75) = 0.60`, so 60 percent. The cost is arithmetic, not taste: every pixel in the image retains 40 percent of its luminance, so the photograph loses more than half its light to make one headline legible.
- **Move the type off the picture into a band.** Costs the photograph nothing, costs the canvas the band's height, and is the most underused of the three.

A gradient scrim at one edge is the common default and the worst of the three, because a gradient has no single luminance value: the type crosses a range, so part of it clears the threshold and part does not, and the visible ramp reads as a repair because it is one.

**Size, carriers and the floor.** The working-file floor is 36px, which renders at 12pt at the nominal downscale, and 48px if you want 12pt under the 4x stress case. A claim set over a photograph sits far above that floor and needs both size and a carrier that is not colour, meaning weight, a plate, or position, because the image supplies colour across the whole frame and the application background changes between dark and light mode.

## Moodboards that constrain

Two boards, with different jobs. Confusing them is the failure. Everything in this section rests on one source. **(thin)**

**The internal board** is looser and exploratory, and variants of one idea are fine on it. Every reference still earns its place by principle 4: if you cannot say what you take from it, it is noise. The trap is volume, and the mechanism is dilution. A board constrains by telling people what to do, so each reference that nobody can account for widens the range of work the board permits. More references do not mean more clarity, they mean less.

A smaller unit works better than one board per project: a master board per category, then boards of three to eight images per concept **(thin)**, each with a title, a note on what would make it different, and a note on what that would cost and how long it would take. The reason for keeping a concept board that small is that it has to communicate one idea at a glance, which a board large enough to need scanning cannot do.

**The client-facing board** is a different document. Fewer images, harmonised so the page reads as one object rather than as a set of good pictures. Three rules carry it.

- **Size is editorial, not aesthetic.** Viewers weight larger images more heavily, so the references most central to the direction get the most space on the page.
- **Harmonise the reference that jars.** Recolour a strong but discordant reference until it sits with the others. If it stands out to you it will stand out to the client, and a client reads standing out as not belonging. Never put a pixelated or badly cropped reference on a client board.
- **Caption every reference with the one quality you are taking**, naming colour, photographic treatment, material, texture or typographic mood. Without a caption a client reacts to the part of the image you were not referencing, and once an idea is dead in someone's head you are arguing from behind.

**Put the cost beside the concept.** Premium materials, named photographers, specific locations and effects all commit someone to spending. A board that references them without saying so makes the direction look aspirational rather than intentional, which is how a direction gets approved and then unbuildable.

**Hold the right altitude.** A board at art-direction level is the whole world of the piece: photography, colour territories, typographic mood, materials, tone. A board at design level zooms into one element and exists as evidence supporting an argument that has already been made and approved. A board at the wrong altitude either reopens a settled decision or fails to support an unsettled one.

**Where references come from is a real variable.** A board assembled from one week of one algorithmic feed produces category-shaped work by construction, because the feed is serving the same results to everyone searching the same terms. Which platform fixes that is unsettled, and nothing in this skill's basis demonstrates it. Vary the source; do not trust a claim that one particular source is higher quality.

## Tests

Run in this order. Each returns a verdict decidable from this file alone.

| Test | Catches | Verdict |
|---|---|---|
| **1. Job** | An image with no assigned role | Read the written job: level one, proof, or texture. Fail if it is not written down, and stop the review there. |
| **2. One-thing** | Images with no idea in them | Say the deliberate difference in one sentence naming an object, action, angle or light condition. Fail if the sentence names no concrete noun or verb. |
| **3. Verb** | Posed subjects | State what the subject is doing. "Standing", "smiling", "posing" and "looking at camera" fail, because they describe a photograph being taken rather than an event. |
| **4. Blur-the-type** | An image arguing with the copy | Blur until the type is unreadable, then name the image's focal point. Fail if that focal point is not the claim's subject. |
| **5. Quiet-region blur** | Type that reads on your screen and fails elsewhere | Blur the image heavily; look only at the area the type will occupy. Fail on more than one tonal value in that area. |
| **6. Luminance ceiling** | Type relying on the photograph for contrast | Measure the relative luminance of the lightest pixel under white type, or the darkest under black type. Fail if white type sits over anything above 0.30, or black type over anything below 0.10. Use 0.183 and 0.175 when the type renders below 18pt. |
| **7. Spanning-edge** | Resolution shortfalls, before a layout is built on them | Measure the image edge that must span the canvas. Fail below 1080px. Mechanical: below the floor, use the image smaller, never upscale. |
| **8. Divide by three** | Detail that exists only at build size | Measure each feature that must be read, in working-file pixels. Fail below 36px, or below 48px if the piece must survive the stress case. |
| **9. Dark and light grounds at 25 percent** | Claims that hold on one application background only | Render the piece at 25 percent over both a near-black and a near-white ground. Fail if the claim weakens on either. |
| **10. Caption** | Referencing by attraction | For each reference, name the one quality taken, as a specific noun phrase: "cyan-to-grey palette", "hard flash on matte fabric". Fail on a paragraph, on "it looks good", and on any image with no caption at all. |
| **11. Board volume** | A board diluting its own direction | Count the references, then count the ones that pass test 10. Fail on any gap; the gap is the cut list. No reference count threshold is given here because none is supported, so the caption, not a number, is the limit. |
| **12. Swap** | An image doing no work | Replace the image with a flat grey rectangle. Fail if the piece says the same thing, and then either make the image carry something or ship the rectangle. |
| **13. Competitor swap** | Brand iconography applied as decoration | Ask whether a competitor could run this concept by swapping its logo in. Fail on yes: the iconography is sitting on the concept rather than being produced by it. |
| **14. Audience-position** | Fatigue deciding a format | Name where this audience sits relative to the category: do they follow it closely, or encounter it occasionally? Fail if the answer is unknown, or if the only evidence that a format is tired is that you are tired of it. **(thin)** |
| **15. Treatment consistency** | A treatment reading as a cover-up | List the treatment applied to every image in the set. Fail if any image is untreated, including the good ones, and fail if two images carry different treatments with no stated rule. |

## Anti-patterns

Broad approaches that fail predictably:

- **Reference by attraction.** Saving what you like and calling it direction. *Fix:* run test 10 over the board and rebuild from the survivors.
- **Treating the photograph as the piece.** The claim gets whatever space is left over. *Fix:* set the claim first at its computed size, then find the image that fits around it.
- **Shooting the product rather than the situation.** *Fix:* principle 2, and supply the activity.
- **Chasing production value.** Waiting on a location, a budget or gear that is not coming. *Fix:* the deliberate difference is reachable with a prop and a stool, per Mode A step 3.
- **Letting your own fatigue decide what is tired.** *Fix:* test 14.

Specific failures and their fixes:

- **Unnameable image.** Fails test 2. *Fix:* crop hard into one detail, or add a prop. Colour never rescues an image with no idea in it.
- **Posed subject.** Fails test 3. *Fix:* put an object in their hands, including an object that does not function.
- **Image fighting the headline.** Fails test 4. *Fix:* crop so the focal point is the claim's subject, or demote the image to level two.
- **Claim set in the busiest part of the picture and rescued with a gradient scrim.** Fails tests 5 and 6. *Fix:* reposition the crop so the quiet region lands under the claim; add a plate only if no quiet region exists anywhere in the frame.
- **Board nobody can caption.** Fails tests 10 and 11. *Fix:* cut to the references that pass the caption test, then decide whether what is left still makes the argument.
- **Uncaptioned client board.** *Fix:* captions, or a clean page followed by an annotated one.
- **Different treatment on every post.** Each image defensible, the set unrecognisable. Fails test 15. *Fix:* one treatment across the set, applied to the good photographs too.
- **Upscaled and sharpened supplied photo.** *Fix:* use it at its real size as level two, per rung 2 of the ladder.

## Applied to a post graphic or carousel

Canvas sizes and both downscale factors come from `reference/canvas-assumptions.md`. Everything else below is computed from them here, and each figure is either shown as arithmetic or labelled as a derived default.

### The grid this section uses, computed

**Canvases.** Square 1080 x 1080. Portrait and carousel slide 1080 x 1350.

**Margin: 72px.** Derived from the stress case. A margin has to read as deliberate air rather than as a trimming error, which means it must stay visibly larger than the smallest type at the worst downscale. The floor type renders at 12pt, so a margin rendering at 12pt reads as the same interval as a line gap. At the 4x stress factor, 48px renders at 12pt and fails that; 72px renders at 72 / 4 = 18pt, which is one and a half times the floor and still reads as a margin. Take 72px.

**Live width: 1080 - (2 x 72) = 936px.**

**Columns: six, gutters 24px.** The gutter is one third of the margin, so the page edge stays the larger interval and a reader can tell an outer boundary from an internal separation. Five gutters at 24px is 120px. Column area is 936 - 120 = 816px, so each column is 816 / 6 = 136px. Check the arithmetic closes: `(6 x 136) + (5 x 24) + (2 x 72) = 816 + 120 + 144 = 1080`.

**Useful spans.** Two columns: `(2 x 136) + 24 = 296px`. Three columns: `(3 x 136) + (2 x 24) = 456px`. Four columns: `(4 x 136) + (3 x 24) = 616px`. Six columns: 936px.

**Live height.** Square: `1080 - 144 = 936px`. Portrait: `1350 - 144 = 1206px`.

**Type ladder.** Start at the 4x-safe floor of 48px and step by 1.5, because a 1.5 ratio keeps adjacent steps distinguishable after division by 3 or 4, where a 1.125 ratio would put 48 next to 54 and render them two points apart. That gives 48, 72, 108, 162, 243px, rendering at the nominal factor as 16, 24, 36, 54 and 81pt.

**Measure check for a claim.** A sans-serif at a given size averages roughly half that size per character, so at 108px each character takes about 54px. Across the full 936px live width that is `936 / 54 = 17` characters per line. A claim of three to seven words fits on two or three lines at 108px. The same claim at 162px would take `936 / 81 = 11` characters per line, which breaks a short claim into four lines and is why 108px is the working level-one size on this canvas and 162px is reserved for one or two words.

### The common case: one mediocre supplied photo carrying a post

A 4:5 frame at 1080 x 1350. One office headshot, or one product photograph on a white sweep. No reshoot available.

**Before.** The photograph is dropped in full bleed, the claim is set over the subject's shirt in white, and the gradient scrim at the bottom is doing the legibility work. The photograph is 820px on its long edge.

**Diagnosis, computed.**

- **Test 1 fails.** No job was written, so the image arrived at level one by area: at full bleed it covers 1080 x 1350 = 1,458,000 pixels, and the claim's type block covers at most 936 x 372 = 348,192, which is 24 percent of it.
- **Test 7 fails.** The spanning edge is 820px against a 1080px canvas, so filling the frame means upscaling by `1080 / 820 = 1.32x`. The softness that introduces is forgiven by the downscale, but the crop budget is already spent.
- **Test 5 fails.** A heavy blur over the claim's area leaves three tonal values: shirt, collar shadow, and background.
- **Test 6 fails.** The lightest pixel under the white claim measures 0.58 relative luminance. `1.05 / (0.58 + 0.05) = 1.67:1`, against the 3:1 the type needs at 36pt rendered.
- **Test 8.** The subject's face spans 430px in the working file, well above the 48px stress floor, so the face reads. Nothing else in the image has to be read.

**After, computed.** Demote to level two, rung 2 of the ladder.

- **Inset size: 296px on the long edge**, a two-column span. That renders at `296 / 3 = 99pt` nominal and `296 / 4 = 74pt` under stress. The face, which was 430px of an 820px long edge, scales to `296 x (430 / 820) = 155px`, which clears the 48px stress floor by a factor of three, so it still reads as a face. Flaws below 48px in the inset cannot be read at all, which is the point of the demotion. This 296px figure is a derived default from the column grid, not a sourced finding: any span that holds the face above 48px works.
- **Place it bottom-anchored inside the margin**, so its lower edge sits on the 72px margin line at y = 1278.
- **Claim at 108px across four columns, 616px.** At 54px per character that is `616 / 54 = 11` characters per line, so a five-word claim lands on three lines. Leading at 1.15 gives `108 x 1.15 = 124px` per line, so the block is `3 x 124 = 372px` tall. Set it on a flat ground, not on the photograph.
- **Space between claim block and inset: 72px**, one step down the ladder from the 108px type, which keeps the gap smaller than the margin so the two elements group as one unit against the page edge.
- **Vertical check.** `72 margin + 372 claim + 72 gap + 296 inset + 72 margin = 884px`, inside the 1350px canvas with 466px left for a label, a logo, or air. The arithmetic closes.
- **Treat the inset** in greyscale or a single-colour duotone, applied to every image in the set per test 15, so it reads as a signature rather than as a cover-up for this one photograph.
- **Then add the one deliberate difference if it is reachable:** one comped object, or thirty seconds with something in the subject's hands.
- **Stress it** at 25 percent on both near-black and near-white grounds, checking the claim and not the photograph. If the claim still weakens, ship type on a flat ground and report that as the decision.

### If the image must be level one

Because the product is the claim, and only then.

1. **Check the spanning edge against 1080px before cropping**, since a crop spends resolution and cannot recover it. An 820px source has no crop budget at all on a 1080px canvas.
2. **Crop hard into one detail** to manufacture both an angle the camera did not have and a quiet region that did not exist.
3. **Compute the quiet region the claim needs**, then crop to produce it. For a bottom-anchored claim on a 4:5 canvas: 372px of type block plus 72px of clearance below it is 444px tall, across the 936px live width. That is the area that must hold one tonal value, and it is 444 / 1206 = 37 percent of the live height. Knowing the fraction before you crop is the difference between finding a quiet region and hoping for one.
4. **Measure the luminance ceiling in that region** per test 6. If the lightest pixel under white type exceeds 0.30, compute the scrim: at 0.62 measured, a black overlay at `1 - (0.30 / 0.62) = 0.52`, so 52 percent, brings it to threshold and leaves the photograph at 48 percent of its luminance. Decide whether the picture is worth that; a plate costs 936 x 516px of area and nothing else, where 516 is the 372px type block plus 72px of padding on each side.

### Carousel

- **Fix the image treatment once and apply it to every slide**, including slides where the photograph is good. Test 15.
- **One image role per slide archetype.** The cover takes the strongest image. Proof slides take the 296px two-column inset. The breaker is the only slide where an image may run full bleed. Never mix full-bleed and inset without a stated rule, because a reader reads an unexplained inconsistency as an error.
- **Check every supplied image against the 1080px spanning-edge floor before building the template.** Finding a 600px photograph on slide seven after the template locks is the usual way a carousel gets rebuilt from the start.
- **Keep the claim inside the 72px margin on every slide.** Crop behaviour across surfaces is not assumed in `reference/canvas-assumptions.md`, so treat anything closer to the edge than the margin as unverified rather than as safe.

## The ultimate test

**The ten-second read at feed size.** Put the finished piece at its real viewing size in front of someone who has not seen the brief, for ten seconds, take it away, and ask two questions: what was the subject doing, and what was the piece about.

Pass means the image and the claim are doing one job. Fail diagnoses in order. No answer to the first question means no deliberate difference was chosen, per principle 1, or the subject was posing, per principle 2. Two unrelated answers mean the image is arguing with the copy, per principle 3. An answer about the photograph and nothing about the claim means the photograph was made the piece when it should have been level two.

The ten seconds is a short fixed interval chosen for this skill, with no measurement behind it. **(thin)** Any interval short enough to prevent the viewer studying the piece does the same work.

## What an agent can run, and what it cannot

**Can run, mechanically:** the spanning-edge measurement, the divide-by-three sweep over named features, rendering at 25 and 33 percent over near-black and near-white grounds, both blur passes, relative luminance of the extreme pixel in a region and the resulting contrast ratio, the scrim opacity arithmetic, counting references against captioned ones, flagging mixed treatments and full-bleed rule violations across slides, detecting sharpening halos and compression blocking, and generating crop candidates against a computed quiet-region target.

**Cannot run:**

- **Whether the deliberate difference is interesting.** Nameability is mechanical. Being worth naming is editorial.
- **Whether an action reads as natural or staged.** The two are identical in a written description and opposite in the frame, and nothing in this skill's basis gives a way to tell them apart. This is the gap directly under principle 2, which is the load-bearing rule.
- **Whether a treatment reads as a signature or as a cover-up.** The same duotone does both, and which one depends on whether the good photographs got it too, which is test 15 and not a judgment.
- **Where this audience sits relative to the category.** Test 14 needs someone who knows them.
- **Whether a reference is taken or copied.** Nothing here locates that line.

**Gaps in this skill's coverage:** no measurement of any image against any outcome, no colour management, no accurate product or skin colour reproduction, no licensing or model release, no retouching ethics, no video or motion, and no accessibility beyond the contrast arithmetic in test 6. Subject coverage is people, apparel and product made to sell something. Food, interiors, architecture, documentary and still life outside commerce are absent, and the rules above have not been checked against them.

## Where this skill should lose

**When the question is what reads first, second and third in the frame.** Use `dsn-composition`. This skill chooses the picture and states what it owes the type; that one arranges the elements and runs the thumbnail test. Focal points are split between the two files and the split is easy to get wrong: the picture has a focal point of its own inside the crop, and choosing the picture and cropping for it is this skill, while the frame's focal point, meaning which element the eye lands on first and where in the canvas it sits, is that one.

**When the question is which element wins and by how much.** Use `dsn-hierarchy`. Assigning the image a level here is a single binary decision; building the full rank order across every element, and the type and spacing ladder that expresses it, belongs there.

**When you need the grid rather than one worked example of one.** Use `dsn-grid`. The six columns, 72px margin and 24px gutter computed above exist to make this file's arithmetic concrete, and that skill owns margin, column, gutter and span derivation for the piece as a whole.

**When the type over the photograph has to be set properly.** Use the skill that sets size, leading, tracking and measure: `dsn-typeset`. The 108px and 124px leading computed here are enough to show whether a quiet region is big enough, and not enough to set a headline well.

**When the contrast question is the whole question.** Use `dsn-contrast`. Test 6 gives the thresholds and the arithmetic for one claim over one region. Auditing a whole piece against an accessibility standard, including text that is not over an image, belongs there.

**When the image is being graded or recoloured rather than chosen.** Use `dsn-color` for what a colour is doing in the frame, and `dsn-palette` for building the set the treatment draws from. This file decides that one treatment applies across the set, not which treatment. The reverse direction is a hole rather than a handoff, so do not look for it here or there: nothing in this plugin derives a colour set out of a photograph. If a project needs one, sample candidates off the image by eye and then test them with the build procedure in `dsn-palette`, because the sampling has no method and the testing does.

**When the frame tips because the picture is the heaviest thing in it.** Use `dsn-balance`, which owns the stability call and decides what counterweight an off-centre mass needs. This file supplies the two facts that skill needs before it can weigh a picture, its tonal value and where its own focal point sits inside the crop, and it is also the place to establish whether a different picture is the cheaper repair. Balance will rearrange around a bad photograph indefinitely; only this file can say the photograph is the problem.

**When the sequence across slides is the problem.** Use `dsn-sequence`. The carousel notes above assign one image role per archetype; the shape of the run, where it turns, and the per-frame budget belong there.

**When one frame has to carry an idea alone and the question is what comes out.** Use `dsn-poster`. This skill tells you which photograph and what it gives up. That one decides the element count for a single frame with no next slide.

## Writing the output

Plain words, full sentences. Name the actual image, the measurement and the region rather than an abstraction: "the claim on slide 2 sits over the subject's shirt, which holds three tonal values after a heavy blur and a lightest pixel at 0.58, giving 1.67:1 against the 3:1 it needs", not "legibility issue".

Name the tier each finding comes from. A spanning-edge shortfall or a failed luminance ceiling is mechanical and settles the matter. A derived default, such as the 296px inset or the 72px margin, is labelled as a default at the point you use it, with the arithmetic that produced it. "The deliberate difference is weak" is a reading, offered as one, with the fix as an option. Say explicitly when a recommendation rests on a rule marked **(thin)**, and say where a move is cheap to test on a real post, because one test on a live feed outweighs everything in this file on anything about what stops a scroll.

Do not repeat a brand, photographer or tool name sourced from this skill's basis without verifying the spelling first.

Sources, corroboration, the disagreements between them, the claims that do not trace to a transcript, and the full caption-level warnings are in `references/provenance.md`.
