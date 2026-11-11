---
name: dsn-identity
description: What a brand's identity is beyond its logo, a billboard and a post not reading as one brand, or auditing an identity you did not build. Gives an inventory and rules.
---

# The identity system

This skill decides what a visual identity is made of, what unit each of its measurements is expressed in, and how those decisions get written down so a stranger or an agent can apply them without you in the room. An identity is the full set of visual elements a brand uses, of which the logo is one. The single idea underneath everything here is that coherence comes from measuring every element in units of something already in the system, rather than from a list of approved assets. Clear space stated in logo widths survives a billboard and a 1080 pixel square; clear space stated as 40 pixels survives neither. A system built from absolute numbers looks consistent in the file it was designed in and falls apart at the second output size, which is why the audit in this skill is mostly a hunt for numbers that were typed in rather than derived.

## What this skill is for

Use it when someone wants to:

- decide what an identity consists of, beyond the mark
- make elements cohere so a billboard and a feed post read as one brand
- write a guidelines document someone else can actually apply
- audit an existing identity, including one they did not build
- judge whether a system will survive being handed to other people or to agents

The output is an element inventory scoped to one brand, a set of rules whose every number traces back to a declared unit, and a one line verdict: usable system, system with named gaps, or assets without a system.

## Confidence

The rules here are practitioner accounts of how working designers build and document identities, not measured findings. No controlled study stands behind any of it, and you should read it as a method that has worked for people rather than as a result. Rules marked **(thin)** rest on a single source and should be treated as one person's house style: adopt them because they are cheap and sensible, not because they are established.

Two limits worth stating before you use any of this. The claim that consistency causes commercial success is asserted everywhere in this field and evidenced nowhere, so every consistency rule below is worth following only for a reason you can name locally: recognition, reproduction, or the cost of arguing twice about the same decision. And colour psychology, typeface psychology, and values read out of a shape's geometry are refused here. A rounded corner does not mean approachable, and attributing a meaning to a form after the fact is not evidence the form carries it.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Mark.** The graphic part of a logo, drawn rather than typed. A **wordmark** is the brand's name set as the logo. A **monogram** is a wordmark reduced to initials. A **variant suite** is the full set of approved forms of the logo: horizontal, stacked, mark alone, one colour, reversed out of a dark background, each with a stated use case.

**Element inventory.** The list of what this identity actually contains: palette, typefaces with roles, imagery direction, illustration, pattern, iconography, motion, and the rules attached to each. Built per brand, not filled in from a template.

**Clear space.** The empty zone around the logo that no other element enters, stated as a fraction or multiple of the logo's own width so it scales with the logo.

**Co-branding space.** The gap between your logo and someone else's when both appear. Conventionally larger than clear space, because two marks that merely clear each other read as one compound mark.

**Minimum size.** The smallest the logo may be reproduced, established by shrinking it until it fails, then adding a safety margin. Stated separately for screen in pixels and for print in millimetres, because the two fail for different reasons.

**Counter.** The enclosed or partly enclosed empty space inside a letter or a shape: the hole in a lowercase e, the gap inside a ring. Counters are what close first as something is scaled down, and a closed counter is what minimum size is protecting against.

**Distinctive asset.** A non logo element that identifies the brand on its own: a particular slanted bar, a specific speech bubble shape, one colour used at one proportion. The thing that makes a layout recognisable after the logo is removed.

**Measure.** The length of a line of text, counted in characters. A measure that runs long makes the eye lose its place returning to the next line.

**Leading.** The vertical distance from one text baseline to the next, usually stated as a multiple of the type size. Type at 48 pixels with 1.35 leading sits on a 64.8 pixel rhythm.

**Tracking.** Uniform letter spacing applied across a run of text, tightened on large display type and opened on small type or on all capitals.

**Cap height and x-height.** Cap height is the height of a capital letter; x-height is the height of a lowercase x, so the height of the lowercase body without ascenders. Two typefaces set at the same nominal size can differ by a third in x-height, which is why a type ratio has to name the metric it is measuring.

**Type ratio.** The fixed multiplier between one level of a type hierarchy and the next, so the relationship rather than the absolute size is what is specified.

**Tonal value.** How light or dark something reads once colour is discarded, as if photographed in greyscale. Two colours can differ strongly in hue and have nearly identical tonal value, in which case type in one over the other will not read.

**Contrast ratio.** A number from 1 to 21 describing the luminance difference between two colours, computed as (L1 + 0.05) divided by (L2 + 0.05), where L is each colour's relative luminance on a 0 to 1 scale and L1 is the lighter. 4.5:1 is the accepted floor for body text and 3:1 for large text and graphical objects.

**Relative luminance.** Perceived brightness of a colour as a single number. Take each of the red, green and blue channels as a 0 to 1 value, linearise it with c divided by 12.92 when c is at or below 0.03928 and ((c + 0.055) divided by 1.055) raised to the power 2.4 otherwise, then weight the three results 0.2126, 0.7152 and 0.0722 and add them.

**The mix.** The proportion of a finished canvas each colour occupies. Governing the mix means specifying those proportions rather than shortening the palette.

**Downscale factor.** The ratio between the pixel dimensions of a working file and the size it is actually rendered at. A 1080 pixel wide graphic in a phone feed column of roughly 360 points has a downscale factor of 3, so a 48 pixel element is seen at about 16 points.

**Dark mode.** A rendering context where the surrounding background is near black rather than near white. Not a second palette but a second set of pairings, since a colour that carries type on white often cannot carry it on black.

**Regime.** Which of two incompatible optimisation targets a project is on: a mark meant to last decades, or a project meant to be approved and delivered. The two have contradicting tests, which is why the first step is naming yours.

## Name the regime before you take advice from anyone

Two coherent positions exist on what a mark is for, and they are rarely stated side by side, so advice from one gets applied on a project running the other.

**The long-horizon regime.** A mark must be appropriate, distinctive and simple, and pointedly not expressive. It cannot say anything much; it needs to feel right. Meaning is not designed into the form, it is poured in by use. A yellow rectangle encountered cold is nothing, and only consistent use over years makes it the vessel for a set of associations. A national flag works the same way: it says nothing about its country, it is simply strong and distinctive, and it accrues meaning by being flown. The operational consequence is that the client does not have to like it on delivery, and a system built this way accepts six months of refusal as a normal cost.

**The throughput regime.** Here the meaning is installed in the form deliberately: list the words the brand owns, turn one into geometry, build the mark out of that geometry, and present it with the derivation visible. The presentation stage exists to build trust, reduce pushback and cut revision rounds. The mark is supposed to read as meaningful on the day it is shown.

Both are coherent and they optimise different things: a mark intended to run fifty years on an engagement where the firm can afford to be fired, against a delivered project on a mid five figure fee where another revision round is the actual cost. Their tests contradict, because under the long-horizon regime a client's dislike is not evidence of a problem and under the throughput regime it is the problem. Name your regime in writing before you take either side's advice.

One of the two is checkable and the other is not. The long-horizon claim makes a prediction that could fail: a mark carrying no legible meaning will still accrue meaning given consistent use. The throughput claim is close to unfalsifiable as practised, because the meaning is read back out of the form by the person who put it there. Prefer the checkable version when they collide, and treat a derivation story as a presentation device rather than as evidence the form works.

## The principles

**1. The identity is not the logo.** The logo is one asset inside a system and often not the one doing the recognition work, because at feed sizes it is tiny or cropped out entirely. *Checked by the logo-removed test.*

**2. Recognition comes from repeated consistent use, not from the mark's cleverness.** A distinctive form is necessary and nowhere near sufficient; the thing that makes it retrievable is having been seen in the same configuration many times. *No test exists at design time, which is the honest problem with this principle: it predicts something you cannot measure until after you have committed.*

**3. Simplicity is a scalability requirement, not a taste.** The mechanism is reproduction: detail that reads at poster size turns to mush at avatar size and fills in on uncoated paper, because the counters close. *Checked by the minimum-size test, run to the point of failure.*

**4. Every measurement is expressed in units of something already in the system.** Clear space in logo widths. Co-branding space in multiples of clear space. Margin as a fraction of the canvas. Type sizes as ratios to each other. Gaps as multiples of one spacing unit. Any absolute number that is not derived from something else is a loose end, and loose ends are where a system diverges between output sizes. This is the actual answer to how elements cohere. *Checked by the unit audit.*

**5. Consistency is enforced by governing the mix, not by restricting the palette.** **(thin)** Specify what proportion of a canvas each colour occupies, so the whole palette stays available and the recipe is what is fixed. The failure this prevents is an inverted hierarchy, where every colour used is technically approved and the result is unrecognisable because the accent is now the field. *Checked by the proportion audit.*

**6. Written rules exist to end arguments, not to constrain designers.** The payoff is that nobody relitigates whether a transition is too fast or whether a panel should enter from the left, because it is already decided and appealable to a document. This is also the correct framing for a system an agent must apply: a rule nobody can appeal to is not documentation. *Checked by the stranger test.*

## How to work

### Mode A: building a system

1. **Run intake that produces design inputs, not adjectives.** Who the ideal customer is and what characterises them; what the products solve; competitor URLs; what the brand should make someone feel; five words for the brand; brands that inspire and why; and any non negotiables such as an existing mark, colour or typeface that cannot change.

2. **Cap values at three.** **(thin)** More brand values make it harder to tie any individual decision back to one, and a value no decision rests on is decoration. Three values, three tone characteristics, three audience personas. If no brief exists, generate one from a call rather than waiting for paperwork.

3. **Extract the words from the client's own language.** Read the brief or call transcript and lift the recurring nouns; those become the design inputs. A lifted word does not have to be expressed in one place: it can live in the mark, or the palette, or the typeface, and spreading it is usually better than making the mark carry everything.

4. **Make two or three mood boards, each leaning on one value.** Cap the count deliberately. More boards make the stories harder to tell apart, and the point of the exercise is a decision between distinguishable directions.

5. **Resolve the approved board into a written checklist before designing anything.** Restate the direction as a specification: a wide palette, one clean sans with a second face for display, a structure flexible enough to carry contrasting colours, subtle hand drawn illustration. From here the identity is checkable against a document rather than against taste, and this is the single most load bearing step in the mode. *Checked by the stranger test and, later, the self-application test.*

6. **Build the element inventory, scoped to this brand.** Palette, typography with roles assigned, and imagery direction are in nearly every system. A guidelines document and illustration are close behind. Then pattern, iconography, clear space, approved colour pairings, minimum size, misuse rules, a logo variant suite, and mock-ups. Co-branding rules and logo placement rules **(thin)**. Motion **(thin)**. A guidelines document is sized by the number of touchpoints the brand actually has, so dropping packaging and photography for a software client is correct, not lazy. Do not fill a template.

7. **Constrain to two or three typefaces, with roles assigned.** Select by elimination: set every candidate in the brand's own name in one file at one size, then remove them one at a time, saying why each goes, until one is left. The role assignment matters as much as the choice, because an unassigned second face becomes a free variable downstream.

8. **Fix type by ratio and name the metric you are measuring.** A workable starting chain is subhead at roughly a third of the headline and body at roughly half the subhead, but the ratio is the specification and the sizes are not. Say whether the ratio applies to nominal type size, cap height or x-height, because two faces at the same nominal size can differ by a third in x-height and the ratio will not hold across a substitution. Start from what looks right at one size, lock the ratio, then verify it holds at every real output size before writing it down. *Checked by the format-invariance test.*

9. **Derive secondary elements from the primary ones.** Pattern from a repeated element of the mark. The shape language of the mark propagated into type treatment, container shapes, image crops, and physical fixtures if there are any. The strongest version of this move: a mark whose idea is a slanted bar sets its type on the same slant, so the identity survives translation into a script with no shared letterforms at all, because what is recognised is the angle rather than the word.

10. **Pre-test colour pairings and ship the pass list.** Step through the palette two colours at a time, compute the contrast ratio for each pair, and record pass or fail against 4.5:1 for body text and 3:1 for large text. Ship the list. Without it, downstream users will pick combinations that fail and it will read as your error. Name the colours after the brand rather than by hue, which also forces you to notice when the brand black is not actually black.

11. **Establish minimum size by breaking it.** Scale the mark down until a counter closes or a stroke merges with its neighbour, record that number, add a safety margin, then print it and measure the physical floor with a ruler. Screen and print floors are different numbers and both belong in the document.

12. **Write the don'ts as plausible mistakes, and declare the list non-exhaustive.** Stretch the logo by a believable 8 percent rather than an absurd 60, because the point is to catch the error someone might actually make, not to demonstrate that you know distortion is bad. State explicitly that the list illustrates a principle rather than bounding it, otherwise anything unlisted reads as permitted.

13. **Split the artefact in two.** **(thin)** The presentation carries the why behind each decision and is read once; the guidelines carry the how and are read repeatedly by people who were not in the room. This resolves the real question of whether rationale belongs in guidelines: it belongs, in the other document.

14. **Make it findable.** **(thin)** A contents page with page numbers, numbered sections, and a separate one page quick reference carrying the hex codes, the type sizes and the clear space rule. Nobody opens a forty page packet to get a hex code, and what they do instead is guess.

15. **Name the audience explicitly.** Designers, developers, marketers, social managers, the founder. The reason to write guidelines at all is usually concrete: someone is about to hire editors or social help, and whatever is handed downstream is what gets built with.

16. **Make the document obey its own rules.** A guidelines document that breaks its own margin, its own type scale or its own palette has falsified those rules on its own first page. *Checked by the self-application test.*

17. **Deliver assets somewhere the client controls.** **(thin)** A system whose files live on your personal cloud drive, which you clear annually, is not documented. Hand over a structured folder the client owns, with the source files, the export set, and the font licence scope stated.

### Mode B: auditing a system

Run in this order. The early tests are the ones that can produce a real negative, and running them after the reassuring ones lets the reassuring result colour the reading.

1. **Logo-removed test** on three real layouts, with a viewer who has not been primed.
2. **Palette-only test**: show the palette alone and ask which brand it is.
3. **Doodle test** on the mark: show it twice, then ask for it back from memory.
4. **Unit audit**: list every measurement in the system and name the unit each derives from. Flag every absolute number.
5. **Proportion audit**: measure what share of a real layout each colour actually occupies, against the stated mix.
6. **Contrast and dark-mode check**: compute every palette pair and check that at least one pair works on a near black background.
7. **Minimum-size check** against the stated floor, on screen and on paper.
8. **Format-invariance check**: apply the layout rules at every real output size and look for the one that needs manual rescue.
9. **Self-application check** on the guidelines document itself.
10. **Stranger test**, which is the ultimate test below and the only one that interrogates the whole system.

Report which findings rest on rules this file marks **(thin)**, because those are the ones a client may reasonably overrule.

## What no method covers: inventing a distinctive asset

**There is no procedure anywhere for generating a distinctive asset from scratch.**

The concept is well established and the evidence for it is strong: a single non logo element frequently carries the recognition, and a layout can be instantly identifiable with the logo removed. The theory of why it works is the vessel argument from the long-horizon regime, that a form meaning nothing becomes retrievable through repetition and then works whether or not the logo is present.

What is missing is the step between. The nearest available method is deriving a pattern from the logo, which is the opposite of what is needed, because the entire point of a distinctive asset is that it survives the logo's removal. An element derived from the mark goes with the mark.

So treat any asset you derive from the mark as a coherence device and nothing more. It will make a set of layouts feel related. It will not pass the logo-removed test with a naive viewer, because what the viewer is retrieving is the mark you derived it from. Say that in the deliverable rather than claiming the pattern is the asset.

## Treat every constant as notation, not derivation

The most complete layout systems in this field were built the other way round from how they are presented: figure out what looks good, then reverse engineer the arithmetic behind it. That is honest and it reclassifies the whole genre of brand guideline mathematics.

Concretely: a margin rule that divides the canvas by 25 has no stated reason for 25, and no reason has ever been offered beyond the number having been seen somewhere and stuck **(thin)**. A type scale stepping by 1.618 is justified by the name of the number, and it routinely contradicts the stated type ratios sitting a page away in the same document **(thin)**. Headline leading is specified as 90 percent in one place, 100 in another and 110 in a third, which means it is taste wearing a specification's clothes.

**Reverse-engineered notation is still worth having.** It takes a private judgement and makes it transferable and repeatable, which is exactly what you need in order to hand work to another person or to an agent. What it is not is a principle: it will not generalise to a brand with different proportions, and the constant inside it is arbitrary.

So keep the move and discard the constant. Derive the margin proportionally from the canvas, choose your own proportion by eye at the real output size, and write down which number you chose and which input it came from. A number labelled as taste is usable; a number presented as a derivation that it is not blocks the next person from changing it.

## Consistency without sameness

Six mechanisms that hold a system together without making every piece look identical:

- **Proportional rules rather than absolute values**, so a billboard and a phone post differ in size and agree in character.
- **Ranges rather than fixed values**, narrowed once tested. "Accent occupies 4 to 8 percent of the canvas" survives more real layouts than "accent occupies 5 percent".
- **Proportion of canvas rather than prohibition**: the palette stays fully available and the mix is what is governed.
- **Named recipes per output type** **(thin)**, so a social graphic has one specified combination of background, text and supporting graphic, and a carousel cover has another.
- **A declared variant suite with selection rules**, each variant carrying the use case it exists for, so nobody picks the stacked lockup because it was first in the folder.
- **A written exception clause** **(thin)**. A brand whose character is slow and deliberate documents the cases where it is allowed to move fast, rather than leaving that to argument at the moment it matters.

And the test of whether a system is finished: **force it through a hard case it appears to forbid.** A slow, luxurious brand cannot do a Halloween jump scare. The wrong answer is to skip Halloween. The right answer is the compliant version of the brief, a slower and more mysterious piece that still frightens, and producing it proves the system can say something other than no. A system that can only refuse is incomplete, and it is the refusals that get it ignored.

## Motion rules **(thin)**

Everything in this section rests on a single account and is provisional. Most identity systems omit motion entirely, which is itself the argument for including it: the gap is real.

Motion decisions derive from the same inputs as every other element. Position the brand on sliders between opposites, fast against slow, mechanical against organic, abrupt against eased, and commit in writing. The best drill is **one action, three readings**: animate something trivial, a button press or a logo reveal, three ways, plain and serious and playful, then pick by the brief rather than by preference. Then assign rules for how often anything animates, how long an interaction takes as a function of how often a user hits it, what happens when one moving thing meets another, button states including the fact that hover does not exist on touch, how type arrives, and what the mark's animation sounds like if anything.

The duration figures circulating in this area, commonly 600 milliseconds for a reveal and 250 for an interaction, are stated by nobody in particular. They sit near ordinary interface motion conventions, so keep them as defaults to test and label them as defaults in the document. The eight second attention span statistic is circulating folklore and is refused here.

Motion is also why the format question has an answer: motion rules cannot live in a PDF, so a system with motion in its inventory needs a hosted document. That is a decision about delivery, not a preference about tooling.

## Anti-patterns

- **Logo-as-brand.** Treating the mark as the identity, so the system is a folder containing one file and a colour.
- **Strategy skipped, visuals delivered.** After which no decision can be justified and every revision is a matter of opinion.
- **The interchangeable mark.** The form is competent and somebody in the same category already has three near copies of it.
- **Colour-only differentiation.** The palette is the whole distinction, which the palette-only test exists to break.
- **Inverted colour hierarchy.** Every colour used is approved, the mix is wrong, and the result is unrecognisable.
- **Decoration added because the brand feels empty.** Pattern, texture and gradient arriving to fill space rather than to carry an idea.
- **Trend adoption mid-system.** A new element in this season's manner, which dates the whole system to this season.
- **Two things competing for the same memory slot.** A mark and a wordmark so unrelated that there is nothing to remember the brand by.
- **The obvious literal icon.** The product drawn as a picture of itself, which is usually both crowded and already taken.
- **Designing for launch rather than for scale.** The system works beautifully across the six pieces that were made to present it.
- **Template contamination.** The previous client's name, or their margin, surviving into the next document.
- **Treating any number in this file as derived.** They are notation. Re-derive them for your canvas.

## Tests

In this order. Every verdict below is decidable by someone holding only this file, the artwork and a ruler.

| Test | Catches | Verdict |
|---|---|---|
| **1. Logo-removed** | A system that is only a logo | Remove the logo from three finished layouts and show them to three people who have not seen the brand. Ask which brand it is. Fail if none of the three names it from any of the layouts, and name what was supposed to carry the recognition. |
| **2. Palette-only** | Colour doing all the differentiation | Show the palette alone, no mark, type or layout, and ask which brand it is. Fail if the answer is a different brand or more than one brand. This test is designed to produce a negative: there are millions of registered trademarks and a handful of nameable colours, so colour alone almost never retrieves one brand. |
| **3. Doodle** | A mark too complex to be remembered | Show the mark twice, remove it, then ask the viewer to draw it or describe it to someone else. Fail if the reproduction loses a feature the mark's idea depends on. |
| **4. Minimum-size** | Detail that destroys reproduction | Scale the mark down in steps until a counter closes or two strokes merge. Record that pixel width, multiply by 1.5 for the stated floor, then print at the floor and inspect with the naked eye. Fail if the computed floor is larger than the smallest slot the mark must occupy, and issue a reduced variant. |
| **5. Unit audit** | Numbers that will diverge across formats | List every measurement in the system and write the unit each derives from beside it. Fail on any number with no named input. A number labelled "chosen by eye" passes; a number with nothing beside it fails. |
| **6. Proportion audit** | An inverted colour hierarchy | Take one real layout, compute each colour's area as a percentage of total canvas pixels, and compare against the stated mix. Fail on any colour more than 2 percentage points outside its stated band. |
| **7. Pairwise pairing** | Pairings nobody checked | Compute the contrast ratio for all n(n-1)/2 pairs in an n colour palette. Fail if any pair documented for body text is under 4.5:1, or any pair documented for large text or graphics is under 3:1. |
| **8. Dark-mode** | A palette with no dark context | Compute every palette colour's ratio against near black. Fail if no colour reaches 4.5:1, since the brand then cannot set body text in dark mode at all. |
| **9. Format-invariance** | Rules that only work at one size | Apply the layout rules at every real output size. Fail on any size that needs a manual override, and name the two rules that collided. |
| **10. Self-application** | Rules the author does not believe | Check the guidelines document against its own margin, type scale and palette. Fail on any violation, including on the cover. |
| **11. Plausible-mistake** | Don't pages that catch nothing | Read each don't and ask whether a competent person under time pressure would plausibly make that error. Fail on any don't that only an incompetent person would trigger, such as a logo stretched to 300 percent. |
| **12. Trademark clearance** | A mark that cannot be used | **(thin)** Search the registry for the relevant classes and the relevant territories before the mark is presented. Fail on any hit in a class the brand trades in. Near identical marks in unrelated categories are usually not a problem. |
| **13. Stranger** | A system that only works with its author present | See the ultimate test below. Fail if the returned piece needs fixing to belong. |

Rejected as tests, although all four are commonly used: is it cohesive, does it feel right, does it look premium, does it resonate. None has a failure condition, so none can return a negative.

## Applied to a 1080 x 1080 and 1080 x 1350 post system

The canvases are a square 1080 x 1080 post graphic and a 4:5 portrait 1080 x 1350 carousel slide, with a nominal downscale factor of 3 and a stress case of 4, per `reference/canvas-assumptions.md`. Every number below is computed from two declared inputs: a 12 point rendered floor for legible type, and the downscale factor.

**Body type, from the floor up.** 12 points rendered at a downscale factor of 3 gives a working size of 36 pixels, which is the floor at the nominal case and the lowest size permitted anywhere on the canvas. At the 4x stress case, 36 pixels renders at 9 points and fails, so the stress-case floor is 12 x 4 = 48 pixels. Both floors deliver the same 12 points and differ only in the viewing case they survive, so every mention of the floor below names which one. Set body at 48 pixels: 48 / 3 = 16 points nominal, 48 / 4 = 12 points at stress, exactly on the stress-case floor. Body is 48 pixels.

**The type chain, and where it breaks.** The starting ratio is subhead at a third of headline and body at half of subhead, which inverted from a 48 pixel body gives subhead 96 and headline 288. Check the headline against measure. With a margin of 128 pixels on each side, derived below from this file's own spacing unit rather than taken from the canvas file, which fixes nothing about margins, the text column is 1080 - 256 = 824 pixels. Every measure figure in this section rests on that 128, and `dsn-grid`, which owns grid derivation, closes a different column on a 72px margin. A sans at 288 pixels averages roughly 0.5 em per character, so 144 pixels, giving 824 / 144 = 5.7 characters per line. A headline of five characters is a single short word.

Run it the other way. For a headline of about 12 characters on one line, the size is 824 / (12 x 0.5) = 137 pixels, round to 136. Carrying the ratio down from there gives subhead 45 and body 23, and 23 pixels is below the 36 pixel floor, so the three level chain cannot run on this canvas at all.

The resolution is two levels, not three. Body stays at 48 pixels, on the stress-case floor. Headline is 120 pixels: 120 / 3 = 40 points rendered, and 824 / (120 x 0.5) = 13.7 characters per line, so a three to five word headline fits. The ratio between them is 120 / 48 = 2.5, which is the number that goes in the document. Where a third level is genuinely needed, it is 48 pixels in a different weight or colour rather than a different size, because a size step must survive division by 3: a 1.125 ratio would put 48 next to 54, which is 16 points next to 18 points rendered, one level wearing two names.

**The spacing unit, from the body type.** Body 48 pixels at 1.35 leading is 64.8, round to 64. Spacing unit is 64 pixels, and the scale is 64, 128, 192, 256, 320. Every gap, pad and margin in the system is one of those.

**Margin, derived rather than inherited.** Margin is two spacing units, 128 pixels, which is 128 / 1080 = 11.9 percent of the edge. Compare the inherited canvas-divided-by-25 constant: 1080 / 25 = 43.2 pixels, or 4 percent, which at a downscale factor of 3 leaves a 14 point gap between content and the edge of the frame. The derived margin is used and the inherited constant is refused, and the reason is now on the page rather than in someone's memory of a document.

**Clear space, and a collision worth documenting.** The logo sits at 160 pixels wide in a post graphic. The rule is clear space equal to half the logo width, so 80 pixels. But 80 is not on the spacing scale, so round up to the next step, 128 pixels. The rule in the document is therefore: clear space is half the logo width, rounded up to the next spacing step. Co-branding space is double clear space, 256 pixels, which is also exactly one scale step up and one quarter of the canvas width. When a logo width rule and a spacing scale disagree, the spacing scale wins, because it is the unit everything else is already measured in.

**Minimum size, computed to a real failure.** The mark's smallest counter closes at 88 pixels wide in the working file. Stated floor is 88 x 1.5 = 132 pixels. A feed avatar renders at roughly 40 points, which at a downscale factor of 3 is 120 pixels of source. 132 > 120, so **the primary mark fails as an avatar** and a reduced variant with opened counters and no enclosed detail is required, with its own floor measured the same way. This is the normal outcome and it is why the variant suite exists.

**Colour pairings, computed.** Brand dark green at #1B4332 has a relative luminance of 0.0448. Against black it is (0.0448 + 0.05) / 0.05 = 1.9:1, which fails 4.5:1 by a wide margin, so this brand cannot set body text in its primary colour in dark mode. Against white it is 1.05 / 0.0948 = 11.1:1 and passes. Add a light green at #B7E4C7, relative luminance 0.697: against black it is 0.747 / 0.05 = 14.9:1 and against the dark green it is 0.747 / 0.0948 = 7.9:1, both passing. With those three plus white, n = 4, so n(n-1)/2 = 6 pairs to compute, and the pass list ships with all six.

**The mix, computed on both canvases.** Stated mix is background 70 percent, ink 25 percent, accent 5 percent. The square canvas is 1080 x 1080 = 1,166,400 pixels, so the accent budget is 58,320 pixels. One 240 x 240 accent block is 57,600 pixels, or 4.94 percent, which fits. A second identical block takes it to 115,200 pixels, or 9.9 percent, which is double the budget and breaks the recipe, so the rule says one accent block per square. The portrait canvas is 1080 x 1350 = 1,458,000 pixels, so the accent budget is 72,900 pixels, and a 270 x 270 block is 72,900 pixels, exactly 5 percent. The portrait slide gets one larger accent block rather than two small ones.

**The unit audit on the system just built.** 48 comes from the 12 point floor times the downscale factor. 120 comes from 48 times 2.5. 64 comes from 48 times 1.35 leading. 128, 192 and 256 come from 64. Margin comes from the spacing scale. Clear space comes from the logo width, rounded onto the spacing scale. Minimum size comes from a measured counter failure times 1.5. The loose ends, which are declared as chosen rather than computed, are exactly four: the 12 point rendered floor, the downscale factor of 3, the 1.35 leading multiplier, and the 2.5 headline ratio. Four declared inputs, and every other number in the system traces to them. That is what passing the unit audit looks like.

**For a personal brand or a content operation specifically.** The recognition surface is a feed rather than a brand world: post graphics, a 1:1 avatar, carousel covers, a newsletter header. Three consequences follow from that. Test 1 outranks everything, because at feed size the mark is tiny or cropped out and something else has to do the identifying. The mix rules have to exist before the palette grows, since publishing daily brings the inverted hierarchy failure on in weeks rather than years. And if agents will produce the work, the written checklist from Mode A step 5 and the unit audit are the load bearing deliverables, because an agent cannot infer a mix from examples and will produce approved-but-wrong output exactly where a rule was left implicit.

## Checklist

- [ ] Regime named in writing: long-horizon or throughput
- [ ] Three values, three tone characteristics, three personas
- [ ] Words extracted from the client's own language
- [ ] Mood board resolved into a written checklist before designing
- [ ] Element inventory scoped to this brand, not to a template
- [ ] Two or three typefaces, roles assigned, chosen by elimination
- [ ] Type fixed by ratio, with the vertical metric named
- [ ] Every measurement expressed in a unit derived from the system
- [ ] Every chosen constant labelled as chosen
- [ ] Colour pairings computed, pass list shipped
- [ ] Colour mix governed by proportion, with bands not points
- [ ] Minimum size established by breaking it, on screen and in print
- [ ] Reduced variant issued wherever the floor exceeds a real slot
- [ ] Don'ts plausible, list declared non-exhaustive
- [ ] Presentation and guidelines separated
- [ ] Contents, numbering and a one page reference
- [ ] Audience named
- [ ] Document obeys its own rules
- [ ] Assets delivered somewhere the client controls
- [ ] Logo-removed and palette-only tests run with unprimed viewers

## The ultimate test

Hand the guidelines and no other help to someone who did not build the system, ask them to make a piece the system has never covered, and look at what comes back.

If it belongs, the system is real. If it belongs only after you fix it, you have a folder of assets and a document about consistency. This is also the exact test for whether an agent can run the brand, which is why the written checklist matters more than the mood board that produced it: the checklist is the part that transfers.

## What an agent can run, and what it cannot

**Can run, fully:** the unit audit, listing every measurement and flagging every number with no named input. The proportion audit, by counting pixels per colour against a stated mix. Contrast ratios for every palette pair and against a dark mode background. Minimum-size checks by scaling and inspecting for closed counters. The format-invariance check across a declared list of output sizes. The self-application check on the guidelines document. Checking any new piece against a written checklist. Describing a mark cold, which is a usable doodle-test proxy as long as it has not seen the labelled original.

**Cannot run:** the logo-removed and palette-only tests, which need viewers who have not been primed, and an agent that has read the brand file is primed by definition. Trademark clearance. Physical print measurement. Whether the regime is the right one for this client.

**Worth delegating deliberately:** the stranger test, which is delegation by definition. And the logo-removed test, because whoever built the system cannot unsee the mark.

## Where this skill should lose

Three skills sit directly next to this one and the boundaries are worth stating precisely, because the overlap is real and picking wrong wastes a session.

**When the question is whether one drawing is right, use the skill that designs and corrects a single mark, `dsn-mark`.** It owns deriving a mark's idea, constructing it, correcting it optically so it looks right rather than measures right, and testing whether that one form is ownable and whether it reduces. Close this file and open that one the moment the question becomes "is this logo any good". This file never evaluates a drawing. It takes the mark as given and asks what the other elements are, what units they are measured in, and whether the set holds together with the mark removed.

**When the question is what to call the decisions and how a tool resolves them, use the skill that turns decisions into named values, `dsn-tokens`.** It owns naming structure, the derivation chain from a base value to its steps, layering a semantic name over a raw one, and the rename tests that catch a name doing two jobs. The division is clean: this file decides that margin is two spacing units and that the spacing unit is the body line height, and that file decides whether the name is `space-200` or `layout-margin-default`, and what happens when someone changes the base. If you have the numbers and need the names, you are in the wrong file. If you have names and no stated derivation behind them, come back here and run the unit audit first, because tokenising an underived number just gives the loose end a label.

**When the question is how to draw a set of small glyphs so they read small and look related, use the skill that builds icon sets, `dsn-icon`.** It owns the keyline grid that every glyph is built on, the shared stroke weight and corner treatment, optical weight compensation so a circle and a square look equally heavy, and silhouette readability at small size. This file says only that iconography belongs in the element inventory, that the set needs a stated minimum size, and that its shape language should follow the mark's. Everything about actually drawing the set, and everything about one glyph failing at 16 points while its neighbours survive, belongs in that file. The practical trigger: if you have more than one small glyph and they must look like siblings, leave.

**What this file owns that none of those three do:** which elements exist at all, before any of them is drawn; the unit each measurement is expressed in, so that a billboard and a 1080 pixel post agree in character; the proportion rules that govern the mix of an available palette rather than shortening it; the written artefact a stranger applies without you; and the audit of a system you did not build, including the verdict on whether it is a system or a folder.

Five more overlap partially, and in each case this file consumes their output rather than producing it. Choosing the brand colour and structuring the palette is `dsn-palette`; this file audits the mix and computes the pairings but does not pick the colours. Fixing a failing contrast ratio, and the full treatment of a measured legibility floor including type over photographs, is `dsn-contrast`; this file only computes ratios to produce a pass list. Choosing and pairing typefaces is `dsn-typeface` and setting size, leading, tracking and measure is `dsn-typeset`; this file fixes the ratio between levels and demands the metric be named, and the quality of the setting is theirs. Computing a grid and auditing alignment is `dsn-grid`, and designing the spacing scale and the base unit is `dsn-spacing`; this file consumes a spacing unit and insists everything derive from it.

**One boundary about scope rather than craft.** Coherence comes in two sizes and this file owns the larger one. Whether two separate posts read as the same brand is this file's question, and it is answered by the unit method and the element inventory. Whether the frames inside one post hold together, meaning what repeats across each seam and which frames are templated, is `dsn-sequence`. If the complaint is that a carousel's middle slides look different from its first, go there. If the complaint is that last month's carousel and this month's look like two companies, stay here.

**One subject this file holds by default rather than by strength:** motion. The motion rules here are thin and cover only consistency of duration and easing across a brand's pieces. No other file in this plugin says anything at all about motion, several of them say so explicitly, and they point here. So this is the only coverage that exists, it is the shallowest material in the file, and a project that depends on motion needs a source outside these files.

And a case where no design skill applies: the strategy is wrong rather than the visuals. Every method here treats a signed strategy as fixed, and nothing in this file tells you what to do when the client's self understanding is the obstacle. That is a conversation, not a system.

## Writing the output

When auditing, report in this order:

1. Whether the brand survives the logo-removed test, naming what carries the recognition or stating plainly that nothing does.
2. The palette-only result, with the brands the palette actually retrieved.
3. Every absolute number with no named input, listed individually.
4. Measured colour proportions against the stated mix, as percentages.
5. Every contrast pair that fails, with its computed ratio and the threshold it missed.
6. Whether a stranger could make an uncovered piece correctly from the document, and what the returned piece got wrong.
7. One verdict: usable system, system with named gaps, or assets without a system.

Give numbers with their units and their derivation, never a characterisation: "clear space is 128 pixels, which is half the 160 pixel logo width rounded up to the next spacing step" beats "clear space is generous". Label a chosen constant as chosen at the point you use it. Say which findings rest on rules this file marks **(thin)**, since those are the ones a client may reasonably overrule. And never justify a consistency rule by claiming that consistent brands succeed commercially; justify it by naming the local failure it prevents.

Sources, corroboration, disagreements, refused claims and the known gaps in the underlying material are in `references/provenance.md`.
