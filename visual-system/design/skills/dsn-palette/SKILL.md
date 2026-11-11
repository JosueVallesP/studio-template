---
name: dsn-palette
description: Building a palette, picking a brand colour, judging a colour set, or fixing colours that fail at small size or on a feed. Produces the palette structure and its tests.
---

# Colour and Palette

This skill builds a palette for a body of work, judges one someone else assembled, and repairs one that works in the design file and fails at delivery. The single idea underneath it is that a colour has no fixed appearance. What a viewer sees is produced by the colour and everything around it together, so the hex code in the file is not the thing being approved. Every rule, test and repair below follows from that: a palette decision is a comparison made in a render at the size and on the background the piece will actually ship on, not a selection made in a picker.

## What this skill is for

Use it when someone wants to:

- build a palette for a brand that will run across many posts
- choose a brand colour or an accent and have a reason rather than a preference
- judge a colour set someone else assembled, including one a generator produced
- fix a palette that works in the file and fails at delivery size or on a feed
- decide what a content crew or an agent may be handed

The output is a role structure with named colours, a usage rule per role, and a measured verdict per text pair.

## Confidence

The rules here are practitioner accounts and careful reasoning from them, not measured findings. Nothing in this file rests on a controlled study. Rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than as established craft.

One further limit, and it is specific to this topic rather than general modesty. Palette building is the weakest-evidenced area in this whole domain. Most of the available teaching is tool instruction: which panel to open, which slider to drag, which plugin generates a ramp. Very little of it is craft, meaning an account of why one colour is right for a brief and another is not. So the mechanics in this file are thinner than the mechanics in the neighbouring skills, and the thinness is concentrated in one place: the step where you go from a written brief to an actual hue. This file marks that gap where it occurs and does not fill it. If a rule here is unmarked and sounds confident, it is because several independent practitioners teach it; if it carries **(thin)**, treat it as a default you may replace.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

These are the only terms this skill needs. The rest of the file assumes them.

**Hue.** The colour's name: the answer a child would give. Red, blue, orange. Measured as an angle from 0 to 360 degrees around a colour wheel.

**Saturation.** How much of the hue is present, from grey at zero to the most intense version of that hue at one hundred. A saturated red is a fire-engine red; a desaturated one is a dusty pink or a warm grey.

**Value, also called brightness.** How light or dark the colour is, from black at zero to the lightest version of that hue at one hundred. Value is how much light reaches the eye, which means it depends on where the eye is, so two people at different angles to the same screen can legitimately disagree about it.

**HSB.** A picker mode with one slider per channel: hue, saturation, brightness. Working in HSB is what lets you change exactly one property of a colour and say which one you changed. The alternative, dragging a point around a two-dimensional field, moves two or three at once without telling you.

**Surround.** Everything immediately around a colour in the finished piece: the field it sits on, the elements touching it, and on a social platform the app background behind the whole frame. The surround is part of what the viewer sees, so it is part of what you are approving.

**Interval.** The distance between two colours, stated per channel: so many degrees of hue, so many points of saturation, so many points of value. An interval is three numbers, never one.

**Tint, shade, tone.** A tint is a hue mixed toward white, a shade is a hue mixed toward black, and "tone" is used by different people to mean either, or both, or a position on a lightness ramp. The word is unusable. Say hue, saturation or value, and say which one you moved.

**Neutral.** A colour with very low saturation, used for fields and for text. A **near-light** is the almost-white neutral a piece reads on; a **near-dark** is the almost-black one. Both are properly near rather than true, which is explained in the structure section.

**Accent.** A colour that appears on very little of the canvas and is there to be noticed. The moment it appears on many elements it stops being an accent, whatever it is called in the file.

**Semantic colour.** A colour whose job is to carry a meaning rather than an identity: an error state, a warning, a success. It has to work for a viewer who cannot distinguish its hue, so meaning never rests on hue alone.

**Ramp.** A series of steps of one hue from light to dark, numbered, so that an element can be assigned "step 40" rather than a hex. A **token** is the named slot a step fills, for example a slot called "text on primary". Ramps and tokens are a convenience for large systems and are not required by anything in this file.

**Contrast ratio.** A measured number comparing the relative luminance of two colours, written as 7.9:1. It runs from 1:1, meaning identical, to 21:1, meaning black against white. It is computed, not judged. The accessibility floor used throughout this file is **4.5:1 for normal-size body text**, which is the WCAG 2.1 AA requirement, and it is the one number in this skill that comes from an external published standard rather than from anyone's taste.

**Optical mixing.** What happens when a coloured element is too small or too thin for the eye to resolve it separately from its background: the two blend, and the element reads as neither its own colour nor the background's. A fine mesh of red on grey reads as a dull pink field, not as red.

**Soft edge and hard edge.** A soft edge is a boundary where element and background are close enough that the element nearly disappears into it. A hard edge is one where they are far enough apart to stay separate. This file makes the distinction decidable with a measured threshold rather than leaving it to judgement.

**Delivery size.** The pixel size the piece is actually seen at, which on a phone feed is roughly a third of the working-file size. The working-file numbers and the downscale factor used here come from `reference/canvas-assumptions.md`: square posts are 1080 x 1080, portrait posts and carousel slides are 1080 x 1350, the nominal downscale is 3x, and 4x is the stress case.

**Greyscale, and desaturating.** Setting saturation to zero across the whole frame, which leaves only value. Any structure that survives desaturation is carried by value; anything that collapses was being carried by hue, which is not safe to depend on.

## The mechanism: appearance is produced by the surround

The same colour on two different backgrounds is two colours to the eye, and nothing in the design file records the difference. You can demonstrate it with cut paper in ten minutes: place one colour on two fields, and it will read as two distinct colours even after you know they are identical. Knowing the trick does not undo it. The useful way to hold this is as two separate facts about one colour: the factual fact, which is the hex, and the actual fact, which is what a viewer sees. The file stores the first. The brief is about the second.

Three consequences follow, and all three are load-bearing.

**A swatch panel is not evidence.** A colour has no appearance until it has a surround. Six hexes in a row tell you about six hexes in a row, and the arrangement you are about to approve is not that.

**The instrument is a render, not a formula.** There is no number anywhere for how far a given colour moves on a given background. The honest position is that you have to look, which also means there is nothing to compute here and no shortcut around putting the candidate in the frame.

**Two people can disagree about a value and both be right,** because value is light arriving at an eye and their eyes are in different places. This is not a reason to abandon the argument. It is the reason to settle it by naming the channel and the interval rather than by trading impressions.

A second mechanism matters just as much for feed work and is easy to miss, because it only appears at small sizes. Below a certain size a colour stops behaving like a colour. Instead of drifting toward or away from its surround, it optically mixes with it, and the result is that the element can simply disappear into its ground rather than merely shift. This failure is invisible at working size and total at delivery size, which is why every test in this file that matters is run twice: once in the frame and once at the pixel size the piece ships at.

## The principles

Six. Each names the test that checks it. The tests are in the table below.

1. **Approve no colour in isolation.** Approve every colour in the frame, on its real surround, at delivery size. This is a condition on every other rule rather than one rule among them: a verdict reached from a swatch grid is void, whatever it says. Checked by the surround swap.

2. **Move one channel at a time, and say which one you moved.** Work in HSB and change hue, or saturation, or value, not two together. Most palette arguments are two people moving different channels and each calling it one change, which cannot be resolved because the two sides are not discussing the same edit. Checked by the interval statement.

3. **Put identity on a saturated colour, not a muted one. (thin)** A strongly saturated colour holds its own appearance on a background you did not choose, and a muted one gets pushed around by whatever it lands on. The colours that move most are the low-saturation ones: muddy browns, weak blues, anything without much of its hue present. So the colour carrying recognition has to be one that still looks like itself in a surround you do not control, which in practice means high saturation. Checked by the personality test.

4. **Expect a shared hue between element and surround to eat the element's hue, and use distance to preserve it. (thin)** A blue on a pale blue field washes out to a flat neutral grey, while the same blue on red stays recognisably blue. The closer element and background are in hue, the more the element surrenders its own. This is the mechanism behind the soft edge, and it is also the first repair to try when a colour reads wrong: change what is around it before you change it.

5. **Treat anything small or thin as a candidate for optical mixing. (thin)** Hairlines, one-pixel rules, small caps, sparse texture and fine mesh all stop reading as their own colour at delivery size and blend with the ground instead. The failure mode is worse than a shift: one element can vanish while its twin on another background survives. This is the most load-bearing principle for post graphics, because a feed delivers everything small. Checked by the small-size mix test.

6. **Let colour carry part of a brief and never the whole of it.** Using yellow does not make a thing optimistic and purple does not make it regal. Colour contributes to a brief alongside type and imagery, and the check is whether all three carry the same handful of adjectives. Checked by the strip test.

## Tests

Each returns a verdict decidable from this file alone. Run them in this order on a build; for a review, the order in Mode B below is faster.

| Test | Catches | Verdict |
|---|---|---|
| **1. Surround swap** | A colour judged in a panel rather than in the piece | Place the candidate on every background it will appear on, in one view, at delivery size. Pass only if the colour reads as the same colour on all of them. Fail if any surround needs a different variant, and record which. |
| **2. Two-field** | How far a colour moves, and in which direction | Put the same colour on two of your real backgrounds, side by side. Fix your eye on the midpoint between them and read both at the edge of vision rather than looking straight at either, which prevents the eye adapting to one. Verdict is a named shift in one channel, or "stable". |
| **3. Interval statement** | A palette that varies on one channel while claiming several colours | For every pair in the set, write the hue distance in degrees, the saturation distance in points and the value distance in points. Fail if every pair differs only in value, because that set is one colour and a ramp wearing several names. |
| **4. Greyscale** | Structure resting on hue alone | Set the whole frame to zero saturation. Fail if the order in which you notice things changes, or if two elements that carried different meanings now sit within 1.2:1 of each other. |
| **5. Small-size mix** | Optical mixing | Render at delivery pixel size, then again at the 4x stress size, and look at the thinnest and smallest coloured elements. Fail any element that no longer reads as its own colour. The fix is mass, a value gap, or deletion, in that order. |
| **6. Soft-edge count** | Elements nearly disappearing into their ground | Count every boundary where element and background are within 30 degrees of hue and measure below 1.5:1 in contrast ratio. **(thin)** Pass only if each one is deliberate and you can say what it is for. Every other one gets a value gap. |
| **7. Personality** | A load-bearing role on a colour that will not stay put | For each colour, read its saturation. Fail if the colour carrying brand recognition sits below roughly 50 saturation while an atmospheric colour sits above it. **(thin)** The fix is to swap the roles, not the hues. |
| **8. Contrast ratio** | Illegible pairs the eye forgives at full zoom | Measure every text-on-field pair. Fail any body-text pair below 4.5:1. Report the number, never an impression. For a failing pair, also report the nearest shade at the same hue and saturation that passes. |
| **9. Wardrobe** | Taste arriving as a decision | Ask whether these are the colours you reach for by default, or literally the colours you are wearing. Verdict is "chosen" or "defaulted". Defaulting is allowed once it is named out loud; what is not allowed is defaulting while calling it a decision. |
| **10. Feed render** | A palette that dissolves into the platform around it | Place the real frame on the platform's light background and on its dark background, with real neighbouring posts above and below. Fail if the frame's outer field measures below 1.5:1 against either app background, because at that distance the frame has no visible edge. The fix is a boundary inside the frame, not a change to the palette. |
| **11. Strip** | Colour being asked to carry the whole brief | Remove all colour, leaving only the type and the imagery. Fail if the piece no longer says the thing it is supposed to say, because that means colour was the only thing saying it. |

## How to work

### Mode A: building a palette

1. **Write the brief in words before opening a picker.** Either the four questions, meaning what constraints exist, what guidance already exists, what the viewer should do, and what the viewer should feel; or five or six adjectives that must then be visible in colour, type and imagery alike. **(thin)** on the adjective form specifically. Either way the output is text, and the point of it is that the hue can later be argued against something.

2. **List every surround this palette must survive.** Both feed backgrounds, every field colour inside the piece, and any third-party context the work gets embedded in. This list is the test rig for everything after it, and a palette approved against a shorter list than the real one is simply untested.

3. **Shortlist two or three hues. (thin)** This is the weakest step in the skill and the file will not pretend otherwise. What is available is category convention, meaning look at what the field already uses so the work reads as its category, while not taking a competitor's exact colour; plus culture and locality as a veto, since a hue can carry political or sporting meaning in one city and none in another. Neither of those picks a hue. Both narrow the field. Shortlist, and settle at step 5 in a render.

4. **Pick the specific colour by hand in HSB, one slider at a time.** This is the best-supported procedure in the whole area: several independent practitioners teach exactly this and none of them teaches picking by dragging a point. Make the brand colour strongly saturated, because principle 3 says that is what makes it hold on a surround you do not control.

5. **Put each candidate against the real surrounds and the real type, and approve it there.** This is the step no generator can perform for you, because the thing being judged is not in its coordinate space.

6. **Build the role structure, not a harmony.** The structure section below.

7. **Write usage rules as prohibitions.** Which colour owns the field, which carries text, which is the accent, and what the brand colour may never be used for. Write "the brand colour is never used for body text", not "use the brand colour sparingly". An aspiration is unenforceable, and a palette without prohibitions becomes a yellow website: one colour on everything, because nothing said it could not be.

8. **Run tests 1 to 11, then the ultimate test.**

### Mode B: judging a palette that exists

1. **Ask what the piece is for and where it will be seen, before looking at the colours.** A palette review run before the piece's meaning is settled is running the review in the wrong order, and will produce notes that have to be thrown away.

2. **Ask how the set was produced.** A harmony rule, a generator or a theme plugin sends you straight to test 1, because that is where this class of failure lives.

3. **Run test 3 first.** A set varying only in value is the commonest defect and the fastest to name, and naming it changes the whole conversation.

4. **Run tests 4, 6 and 8.** The first two cost nothing. The third produces a number you can hand to someone who disagrees with you.

5. **Run tests 5 and 10 at delivery size,** then test 7 on whichever colour carries the brand.

6. **Report what passes, what fails, and the smallest change that fixes each failure, ordered by impact.** Name the channel in every recommendation. "Raise the brand blue's value by 35 points and keep hue and saturation" is actionable; "the blue feels muddy" is not.

## Palette structure

A brand running across many posts needs roles, not a harmony. A harmony is a statement about hue spacing and nothing else, which is why a set can be a textbook split complementary and still fail on value and saturation. Roles survive because they say what each colour is for.

**One brand colour, strongly saturated, carrying identity.** It appears on few elements and never on body text. Its saturation is what lets it stay itself in surrounds you do not control.

**A near-dark and a near-light, both tinted toward the brand hue, and neither true black nor true white.** This is the best-supported structural move in the area: practitioners coming from product interfaces, from visual design and from token systems all arrive at it independently. True black strains the eye, and both true endpoints read as generic. Give every neutral a trace of one hue and the whole piece gets a consistent atmosphere for nothing: the greys belong to the brand instead of being borrowed from the operating system.

**Two tuned variants of the brand colour, one per surface. (thin)** This is relativity turned into a deliverable. The same hex does not read the same on a light field and a dark one, so you ship two and name them so that nobody treats one as a correction of the other. Single-source, and kept anyway, because it is the direct operational consequence of the central mechanism rather than a separate claim. The arithmetic for deriving the second one is in the Applied section.

**One semantic colour, chosen when the palette is built. (thin)** Not defaulted to a stock red six months later when an error state first appears. It has to work without its hue, since roughly one viewer in twenty cannot reliably distinguish it, so pair it with an icon, a word or a weight. That population figure is inherited rather than measured here and is approximately right for a mixed population. **(thin)**

**A ramp per role, only if you actually need one.** Ramps are for systems large enough that elements get assigned slots rather than colours. The step numbers in general circulation are published tokens from one framework, read off its documentation rather than derived by anyone, and that framework's claim that its paired steps are accessible by construction is demonstrated by eye rather than measured. **(thin)** Use the ramp as a shortcut if it saves you time, and run test 8 anyway.

One rule governs the interaction between a ramp and a brand: **key colours override generated tokens for the brand roles.** If a brand already has a colour and the ramp says the primary slot takes a particular step, taking the step silently changes the brand. Put the brand colour in the slot and let the ramp fill everything else.

## Enumerate with a tool, approve in a render

There is a real method conflict here, not a difference in emphasis, and every colour tool you will be handed sits on one side of it. One position is that a colour cannot be judged out of context at all, so you cut many candidates, rotate many backgrounds under them, and look; cheap iteration is the whole technique, paper rather than paint, so that thirty combinations cost an hour instead of a week. The other is embodied in every wheel, picker and plugin: apply a rule, read off a set, judge the result as rectangles in a panel.

**The decision rule is that a generator enumerates and a render decides.** This is not a split between an old way and a new way and better tooling will not resolve it. A generator operates on coordinates; appearance is a relationship between a colour and its surround, and the generator cannot see the surround. It is structurally incapable of judging its own output, regardless of what year it was built. Use it freely to produce candidates and never to approve one. Even the practitioners who teach picker-first methods follow this in practice while their stated method does not, because they keep rejecting candidates against the real wordmark.

Operationally there is a one-line version. **If the window where you chose the colour is the window where you approved it, you used a generator as a judge.**

## The 60/30/10 ratio

**This is a convention, not a derivation. (thin)** It is asserted as something established elsewhere and then fitted retroactively to work already considered good. Nobody derives it, measures it, or offers a range around it.

What it is a crude proxy for is the usable part: **exactly one colour owns the field, exactly one carries the reading surface, and the chromatic accent takes so little area that it stays an accent.** The real constraint is visual weight rather than area, and saturation buys weight far out of proportion to area. The honest statement of the mechanism is a hint of colour in a sea of big neutral tones, which is a direction and not a ratio. No number for it exists anywhere, so do not quote one.

The arithmetic shows why the literal figure misleads. A square canvas is 1080 x 1080, so 1,166,400 pixels. Ten percent of that is 116,640 pixels, and the square root of 116,640 is 342, so a literal ten percent accent is a 342 x 342 block: roughly a third of the canvas width, in a fully saturated colour. On a 4:5 slide, 1080 x 1350 is 1,458,000 pixels, ten percent is 145,800, and the square root is 382, so a 382 x 382 block, which is 35 percent of the width. Neither of those is an accent. By comparison, a 180-pixel saturated disc covers pi times 90 squared, which is 25,447 pixels, or 2.2 percent of the square canvas. That reads as an accent.

So: treat the ratio as a reminder to ration, budget the accent in low single-digit percentages of area rather than at ten, run it through the weight check in the skill that owns visual weight, `dsn-balance`, and do not quote the three numbers as a rule.

## Anti-patterns

Broad approaches worth naming:

**Palette by generator.** A harmony rule produced the set and nobody rendered it on a real surround. Fix: enumerate with the tool, approve in the frame.

**Harmony-name thinking.** "It is a split complementary, so it works." Fix: state the three intervals per pair. The harmony name covers hue only and says nothing about the two channels the set is most likely failing on.

**Colour psychology as a decision.** Association lists are asserted everywhere in this genre and tested nowhere, and even the material that supplies them says plainly that association alone does not produce the effect. Fix: shortlist with it if you like, settle on the surrounds.

Specific failures:

**Monochrome wearing three names.** Primary, secondary and tertiary all one hue at different values. Fix: separate the hues, or admit it is one colour and a ramp, and stop charging for three.

**Taste by default.** Fix: the wardrobe check, then choose again on purpose.

**"They look good together."** The fastest way to lose an argument about colour, because the only available reply is "tell me how". Fix: name the channel and the interval.

**Identity on a muted colour.** It will be a different colour on every surround you do not control, which means recognition never accumulates. Fix: the personality test, then move identity onto the saturated colour.

**True black and true white.** Straining and generic. Fix: tint both toward the brand hue.

**One brand hex for both surfaces.** Fix: two tuned variants, derived and measured.

**Hue carrying meaning alone,** such as a red-only error state. Fix: add an icon, a word or a weight.

**Accent inflation.** Every element gets a colour, so nothing is an accent. The clearest contrast is an interface that repeats every colour from its product packaging until the screen is noise, against a retailer whose interface is black, white and one red precisely so the products can be the colour. Fix: the field around a vivid subject stays quiet.

**A hex copied from a transcript or a caption.** Automatic transcription mangles colour names and hex values without exception, and colour vocabulary specifically: hue, tone, shade and tint get swapped at random, and codes arrive as word fragments. Fix: never state a hex as fact from a transcript. Sample it from the artefact.

**Approving a palette for print.** Everything in this file is screen-only. A palette that passes every test here can still be unprintable, because ink, paper and a limited gamut impose constraints nothing above accounts for. Fix: treat print as out of scope and get a proof.

**Applying this skill to a chart.** Sequential, diverging and categorical data palettes have requirements that cut directly against several rules here, including the tinted neutral. Fix: do not.

## Applied to a post visual or carousel

**The palette is fixed for the body of work, not chosen per post.** Recognition accumulates only on a structure that repeats, so the colour set must not vary. Variation comes from the content inside it.

**Build it against both feed backgrounds first, and measure.** Square and 4:5 frames sit inside app chrome you do not control, which makes the feed itself the surround and principle 1 decisive.

Start with a brand blue at hue 220, saturation 85, value 60. Converting HSB to 8-bit RGB gives 23, 66, 153, so `#174299`, with a relative luminance of 0.064.

Derive the two neutrals by keeping hue 220 and collapsing saturation. The near-light at saturation 6 and value 97 gives 233, 237, 247, so `#E9EDF7`, luminance 0.846. The near-dark at saturation 30 and value 13 gives 23, 27, 33, so `#171B21`, luminance 0.011.

Now measure the pairs. Contrast ratio is the lighter luminance plus 0.05, divided by the darker luminance plus 0.05.

- Brand on near-light: (0.846 + 0.05) / (0.064 + 0.05) = 0.896 / 0.114 = **7.87:1**. Passes 4.5:1 comfortably, so the brand colour is usable as text on the light surface.
- Brand on near-dark: (0.064 + 0.05) / (0.011 + 0.05) = 0.114 / 0.061 = **1.87:1**. Fails badly. The brand colour is not a text colour on the dark surface, and no amount of looking at it will change that.

So derive the dark-surface variant. Keep hue 220, drop saturation slightly to 70 so the lighter value stays believable, and raise value. At value 92 the colour is 70, 125, 235, `#467DEB`, luminance 0.220, giving (0.220 + 0.05) / 0.061 = **4.44:1**, which still fails. At value 95 it is 73, 129, 242, `#4981F2`, luminance 0.235, giving 0.285 / 0.061 = **4.70:1**, which passes. That is the dark-surface variant, and the two-step derivation is the point: the first plausible lift was not enough, and only the measurement said so.

Add one semantic colour the same way. Red at hue 0, saturation 80, value 80 is 204, 41, 41, `#CC2929`, luminance 0.146. On the near-light that is 0.896 / 0.196 = **4.58:1**, which just clears the body floor. It is paired with an icon and a word regardless, because test 4 is about meaning and not about legibility.

**Then measure the frame against the feed, which is where most palettes actually fail.** A light app background is effectively white, luminance 1.0. The near-light field against it is (1.0 + 0.05) / (0.846 + 0.05) = 1.05 / 0.896 = **1.17:1**. A typical dark app background is around `#16181C`, luminance 0.009. The near-dark field against it is (0.011 + 0.05) / (0.009 + 0.05) = 0.061 / 0.059 = **1.03:1**. Both are below the 1.5:1 soft-edge threshold in test 6, which means that on its matching feed each field has no visible boundary at all: the post dissolves and the viewer sees floating type. Either the frame carries its own boundary, meaning a full-bleed tinted field or a visible edge, or the palette holds on only one of the two feeds.

A boundary has to survive the downscale to be a boundary. At the nominal 3x, a 1-pixel rule in the working file renders at a third of a device pixel and simply is not there; a 2-pixel rule renders at two thirds. The minimum stroke that occupies a whole device pixel is **3 pixels at 3x and 4 pixels at the 4x stress case**, so draw frame edges at 4 pixels or more and treat anything under that as decoration.

**Thin elements lose their colour first, and here is the floor.** The reliable smallest rendered size is about 12pt, which at 3x is a working-file floor of 36 pixels. So body type at 42 pixels renders at 14pt and a 36-pixel caption renders at 12pt, right on the floor; at the 4x stress the same caption renders at 9pt, which is below it. A coloured element needs more area than a neutral one to hold its hue, so set the floor for coloured type higher: **48 pixels in the working file**, which renders at 16pt at 3x and 12pt at 4x. Below that, carry the text on a neutral at full contrast and let the brand colour live on fields and marks.

**Carousels: one palette, one role assignment, every slide.** The brand colour appears on the same kind of element throughout. At most one slide inverts the light and dark roles, and that slide carries the turn in the argument. If you are re-picking colours on slide seven, the structure is wrong and no individual slide fix will repair it.

**When a client's brand colour is unusable at small size or against the feed, change its role and not the colour.** In order, and the ladder is assembled here rather than taken from anywhere, so treat the ordering as reasoned rather than established. **(thin)**

1. **Keep the hue, move the value.** The recognisable part of a brand colour is its hue. Build a lighter or darker sibling at the same hue and saturation, as derived above, and reserve the exact brand value for the one element large enough to carry it.
2. **Give it mass instead of scatter.** A colour that fails as 2pt text is fine as a 400-pixel field. The failure was never the colour, it was the area.
3. **Change its surround rather than the colour.** A brand colour that reads muddy on the near-light can read correct on the tinted near-dark, because a shared hue was eating it. Try this before touching the hex.
4. **If it still fails test 8 as text, it is not a text colour.** Demote it to fields and marks and carry text on the tinted neutrals. Say it in exactly those terms: the brand colour has not been changed, its role has. That is defensible to a client. "We lightened your blue" is not.
5. **Never silently alter the brand hex.** Record each sibling as a derived value with its measured ratio and its permitted role, the way the two variants above are recorded. A contrast tool that returns the nearest passing shade at the same hue makes this a one-minute job rather than an afternoon.

## Checklist

- [ ] Brief written in words, and every surround listed, before any picker was opened
- [ ] Brand colour strongly saturated, with identity not resting on a muted colour
- [ ] Near-dark and near-light tinted toward the brand hue, no true black or white
- [ ] Two tuned variants of the brand colour, one per surface, each with its measured ratio recorded
- [ ] Three intervals named per pair, so the set is not a value ramp wearing several names
- [ ] Every text pair measured against the 4.5:1 body floor, as a number
- [ ] Hierarchy survives desaturation, and no meaning rests on hue alone
- [ ] Rendered at delivery size and at the 4x stress, with thin elements checked for mixing
- [ ] Frame measured against both app backgrounds, with a boundary of at least 4 pixels where either fails
- [ ] Usage rules written as prohibitions: dominant, text, accent, and what the brand colour may never do
- [ ] Across a sequence: one palette, one role assignment, at most one inverting slide

## The ultimate test

**Tests 1 and 5 together, run by the person who will actually refill the template, on the real feed at real size.** Every colour still reads as the colour you chose, on every surround on your list, at the size it ships: the palette is sound. A colour reads correctly on one background only: it is a one-off needing a tuned sibling, not a palette entry. It reads correctly at full zoom only: it is not in the piece at all, whatever the file says. Report which of those three you have, by name.

## What an agent can run, and what it cannot

Can run from this file, with no judgement required:

- **Contrast ratios for every pair,** pass or fail against the stated floor, plus the nearest passing shade at the same hue and saturation.
- **Interval reporting.** Hue, saturation and value distance per pair, which exposes a value-only palette immediately.
- **Soft-edge detection.** Every element and background pair within 30 degrees of hue and below 1.5:1 in contrast.
- **Thin-element inventory.** Every coloured element below the stated stroke and type thresholds, which is the mixing risk list.
- **Greyscale and colour-blindness simulations,** plus renders at delivery size and at the 4x stress on both app backgrounds, so that a human has to look once at one sheet rather than ten times at ten files.
- **Consistency across a sequence,** and a check that nothing in the file uses an off-palette value.

Cannot run:

- **Judging appearance.** It is produced by the surround and not by the file, and every practitioner in this area, including the most tool-driven, reaches a colour verdict by looking.
- **Choosing the hue.** An agent can shortlist from category convention. It cannot pick, and aptness is the specific capability to distrust here.
- **Whether a colour is apt for the brief,** since association lists are untested and a correct association does not produce the effect anyway.
- **How far is too far on an accent,** because no maximum exists, and **telling a deliberate soft edge from an accident,** because in the file they are identical and only intent separates them.

On generated work the order inverts. Generators return palettes that are internally consistent and contextually untested, so **harmony is what you get for free and context is what you must specify.** Give an agent the surround list and the delivery size as constraints up front, not as a review step afterwards. That inversion is reasoned here rather than taken from anywhere. **(thin)**

## Where this skill should lose

**When the question is how colour behaves rather than which colours to use.** Use `dsn-color`, the skill that owns colour behaviour. This file assumes the mechanism and spends its space on building and judging a set.

**When the question is whether a specific pair is legible enough.** Use `dsn-contrast`, the skill that owns contrast and legibility thresholds. Test 8 here measures text pairs against one floor and stops; it does not cover large-text thresholds, non-text contrast, or what to do when a client's standard differs from the published one.

**When the question is whether the piece is weighted correctly.** Use `dsn-balance`, the skill that owns visual weight. The accent-rationing argument above hands off to it deliberately, because how much saturated colour balances how much neutral is a weight question and this file has no number for it.

**When the palette has to become a system with named slots.** Use `dsn-tokens`, the skill that owns token structures and ramps. This file tells you to use a ramp only if you need one and says nothing about naming schemes, theming or handoff.

**When the question is what the brand is, not what colour it uses.** Use `dsn-identity`, the skill that owns identity systems. Colour is one component of a brief here and deliberately not the governing one.

**When the palette has to come out of a photograph.** No file does this, and that includes `dsn-image`, which chooses a picture, crops it and sets one treatment across a set, and nowhere produces a colour set out of one. Do not go looking for the method, and do not expect a neighbour to hold it. The hole is real, so here is the workable substitute: sample four to six candidate values off the image by eye, write down all three numbers of each rather than only the hex, then run them through this file's build procedure and every test in it exactly as if they had been chosen any other way. The sampling step is unmethodical and the testing step is not, and the tests are what decides whether the set holds. What this file does own is the reverse direction, choosing or briefing imagery to fit a palette already set.

**When the question is the order a viewer reads things in.** Use `dsn-hierarchy`, the skill that owns reading order. Test 4 here only checks that a hierarchy survives desaturation; it does not build one.

**When the question is how a carousel argues across slides.** Use `dsn-sequence`, the skill that owns sequence. The carousel rule above fixes the palette across slides and says nothing about what goes on them.

Two topics have no owner anywhere, so name them rather than improvise: **print, ink and gamut**, and **display calibration and colour management**, which is the modern form of the observation that two viewers see different values. If either is in play, this file cannot help and neither can its neighbours.

## Writing the output

Plain words, full sentences, and the actual colour role, pair and measurement rather than an abstraction. Never say a palette feels off: name the channel, the pair and the interval. Give the measured number rather than a characterisation, because "4.44:1 against the near-dark, which fails the 4.5 floor" settles an argument and "a bit low on the dark background" starts one. When a reviewer needs one handle, give the verdict in a single word, defined: **washed**, meaning the colour shares its surround's hue and has lost its own; **mixed**, meaning it is too small or thin to read as its colour at delivery size; or **holding**. State the principle first and the change as an option, so the person can choose a different fix for the same diagnosis. Label a default as a default at the point you use it. Where the mechanics are thin, say so rather than inventing a rule to cover the gap.

Sources, corroboration, disagreements, caption warnings and what was read and left out are in `references/provenance.md`.
