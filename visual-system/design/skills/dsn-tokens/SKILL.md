---
name: dsn-tokens
description: Turning brand decisions into named values an agent or build step can resolve, when a folder lists hex codes and calls itself a system, or auditing someone else's names.
---

# Tokens

This skill gives a brand's already-decided values names that resolve: names a build step can look up and an agent can extend without guessing. The single idea underneath it is that a file recording only outputs keeps the rule a secret. A spec that says `16 / 24 / 32 / 40` hands a reader four numbers and no way to produce a fifth, so when a fifth is needed it gets invented, and the invention is plausible and wrong. A spec that says *base 8, linear, steps named caption / body / deck / headline* lets anyone derive the next step, and lets you change the base once and have everything follow. Write the rule, not the results. Everything below is downstream of that sentence.

## What this skill is for

- turning a brand's values, sizes and spacings into names that mean something
- writing a spec an agent can extend correctly instead of guessing at
- auditing a brand folder that lists hex codes and calls itself a system
- deciding how many layers a system actually needs, which is usually fewer than published systems suggest
- fixing a name that was true when it was written and is false now

The output is one machine-readable file, a stated segment order, each scale written as a base plus a progression, and a verdict per test in the table below.

## Confidence

The rules here are practitioner conventions and reasoning from them, not measured findings. Nothing in this file rests on a controlled comparison, and no part of it has been run end to end on live client work. Rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than craft. The segment order rule is the single most likely thing in this file to be wrong, and it is also the hardest thing to change later, so it carries that marker and this warning.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Token.** A name bound to a value, where the name describes a decision and the lookup returns the value. `color.text.primary` is a token. A hex code written directly into a template is not.

**Value.** The literal thing a lookup returns: `#2B2B2B`, `90`, `1.4`, `Söhne Bold`.

**Raw value, also called a primitive.** A value stated once, with no decision attached to it, held for other tokens to point at. `colors.ink.900: #2B2B2B`. This is the only layer where a name is allowed to describe what the value is rather than what it is for.

**Alias.** A token whose value is another token's name rather than a literal. `color.text.primary: colors.ink.900`. Resolving an alias means following it until a literal is reached.

**Layer.** One rank in the system. This skill uses three: the raw layer (values), the job layer (what each value is for), the place layer (where a specific repeated part gets its values). Published systems call the middle layer "semantic", which means the same thing.

**Job, also called a role.** The function a value performs in a piece: the page surface, the surface sitting above it, the text on each, the accent, the hairline rule, the kicker (the small line of label text above a headline), the headline, the caption. A job persists when the format changes; a size does not.

**Segment.** One dot-separated part of a name. `color.surface.raised` has three segments: category, role, variant.

**Namespace.** The leading segment that groups a family of names. `color`, `type`, `space`.

**Mode.** A context the consumer of the system selects, under which the same job token resolves to a different value. Light and dark are modes. Platform, meaning LinkedIn against print against a deck, is also a mode.

**Base unit.** The number a linear scale multiplies. With base 18, step 5 returns 90.

**Linear scale.** A progression by addition or by whole multiples of a base: 18, 36, 54, 72. Values sit at even distances apart.

**Modular scale.** A progression by multiplication against a fixed ratio: 75, then 75 x 1.25, then 75 x 1.25 squared. Values spread wider as they climb.

**Ratio.** The multiplier a modular scale uses. 1.25 is the major third; 1.125 is the major second.

**Ramp.** A numbered series within one family, usually colour: `colors.ink.100` through `colors.ink.900`.

**T-shirt sizing.** Naming steps `xs / s / m / l / xl` instead of by proportion or by job. The name carries no value and no order beyond the convention.

**Composite value.** A value that is not a single scalar: a gradient, a multi-layer shadow, a multi-fill. Composites resolve differently from scalars in every tool, so some brand decisions will live as composites that cannot be aliased cleanly.

**Leading.** The vertical distance from one baseline of text to the next, usually stated as a multiple of the font size. 1.4 leading on 42px type is 58.8px between baselines.

**Tracking.** Uniform letter spacing added to or removed from a whole run of text.

**Measure.** The width of a column of text, counted in characters.

**Contrast ratio.** The relative luminance of the lighter of two colours plus 0.05, divided by that of the darker plus 0.05. It runs from 1:1, meaning identical, to 21:1, meaning black on white. The accessibility floor for normal-size text is 4.5:1.

**Downscale factor.** The number a working-file pixel is divided by to get the size a phone actually shows. On the canvases this plugin assumes it is 3 nominally and 4 as a stress test, which puts the smallest reliable rendered size at 12pt and so gives two working-file floors: **36px at the nominal case** and **48px at the stress case**. Name the case whenever you quote the floor, because the two figures are the same 12pt rendered and differ only in which viewing condition they survive.

## The mechanism: why a list of values cannot produce the next value

A list of values is a function defined only at the points someone happened to write down. Anything asked of it outside those points has no answer, so the consumer supplies one. A build step supplies a crash or a fallback. A person supplies whatever looks close. An agent supplies the most common value in its training distribution, which for spacing is 8 or 16 and for body type is 16, all of which are device-independent pixels from screen interface work and all of which are wrong by a factor of 3 on a 1080px canvas. Sixteen pixels of body type on a 1080px slide renders at about 5pt. Nothing errors. The piece is simply unreadable.

A rule is defined everywhere. State base 18 and linear, and step 7 returns 126 without anyone having written 126 down. State base 75 and ratio 1.25, and the fourth display step returns 146. The spec stops being an inventory and starts being a function, and the gap between those two is the whole value of the exercise.

The second half of the mechanism is where the rule lives. If the base is written in the file, changing it changes every derived value at once. If the base lives only in the head of whoever generated the list, then the list is the system, and changing the base means finding and editing every number, which is the point at which people stop changing it and the system calcifies at whatever was convenient the first week.

The list form has a tell: a page giving `#FF5F1F` beside the words "Brand Orange" has tokenised nothing, because name and value carry the same information and there is therefore no lookup. Ask what that colour is *for* and the file is silent, so every use of it is a fresh judgement call by whoever is working that day.

## The principles

**1. A token names a decision, not a value.** The test is which direction the name points. Raw values are the only tokens whose names may describe what they return; every layer above must describe what the value is used for, because a decision can change while staying the same decision and a description of appearance cannot survive that. *Test:* cold-read.

**2. Three layers: value, job, place.** **(thin)** A raw value, then what it is for, then where one specific repeated part gets its values. The raw layer is reference only, and nothing above the job layer may point past it to a raw value directly. The marker is on the count rather than the idea: the split into exactly three is a convention with a traceable single origin, and surveys of real systems find many competing names and counts, so treat three as a sensible default and not as a converged finding. *Test:* private-value audit, alias-resolution.

**3. Mark the raw layer in the name itself, with a plural.** **(thin)** A plural namespace marks a raw value and a singular one marks a decision, so `colors.ink.900` is unmistakably a primitive and `color.text.primary` is unmistakably a job token. One character encodes the tier, there is nothing to memorise, and it survives being read by someone who has never seen the system. *Test:* private-value audit.

**4. Name by job, not by size.** `caption / body / deck / headline`, not `xs / s / m / l`. A piece has stable named roles, kicker, headline, deck, body, caption, source, page number, and those roles persist across formats while the pixel values do not. A 1080 x 1350 slide and a 1200 x 627 link card share every role and share no sizes. Size names force a rename on every format change; job names do not. *Test:* format-move.

**5. Two jobs means two scales, each stated separately.** Display sizes and body sizes have no arithmetic relationship to each other, and forcing them onto one ratio is the most common error in brand type systems. Use a modular scale for display, which has to span a real range, and a linear one for body, which sits in a narrow band. Write each one's base and progression as its own line. If you cannot state two rules, you have one scale being asked to do two jobs. *Test:* two-scale.

**6. A modular ratio has to survive the downscale.** A step that is not visibly distinct once divided by the downscale factor is one level wearing two names. At 1.125, 48 sits beside 54, which is 16pt beside 18pt rendered, and nothing in the hierarchy reads as a level change. Require at least 4pt of rendered separation between adjacent display steps, which at a downscale of 3 means at least 12 working pixels, and derive the minimum ratio from the smallest display size you actually use. *Test:* step-distinctness.

**7. Derive every step from the base, never from the rounded step before it.** Rounding compounds. Base 75 at ratio 1.25 gives 93.75, 117.19, 146.48, which round to 94, 117, 146. Chain the rounded values instead and you get 94, 118, 148, which drifts two pixels by the fourth step and more after that, and the drift is invisible until someone regenerates the scale and gets different numbers from the same stated rule. *Test:* derivation.

**8. Derive the base from the canvas, not from interface convention.** **(thin)** The 4 and 8 pixel spacing convention exists because whole-pixel rendering on a screen rewards it, and a non-integer downscale voids that reason, so it does not transfer to a fixed canvas. Choose a base that divides the canvas cleanly instead, so that margins, gutters and column widths come out as integers. On 1080 that means a divisor of 1080: 18 gives 60 units across the canvas, 20 gives 54, 24 gives 45. The marker is on the specific base: the method is derived, the choice among the candidate divisors is house style. *Test:* base-change.

**9. Proportional names beat t-shirt names wherever a machine reads the spec.** `space.5` against a stated base of 18 tells any reader the value is 90. `space.large` tells them to go and look it up, and a consumer that cannot look it up will guess. The exception is a short ramp of three to five steps that will never be extended, where role names read better and there is no next step to derive. *Test:* value-recall.

**10. A name must survive the decision changing.** The move to make is from what a thing looks like to what rank it holds: `tier.2` rather than `outlined`, because the appearance was negotiable and the rank was not. Brand systems are full of the first kind, `big-blue-header`, `dark-slide`, `quote-card-v2`, and each one becomes a lie the first time the decision it describes is revisited, which leaves the system holding names that actively mislead. *Test:* rename.

**11. A colour pair that carries a guarantee must record the guarantee.** A job-layer pair such as text on a raised surface is the only place in a token system where a legibility promise can actually be held, because a raw hex knows nothing about what sits on it. Record the computed contrast ratio on the pair, and recompute it whenever either side moves. This is the one thing the job layer can enforce that the raw layer cannot. *Test:* contrast-guarantee.

**12. Add modes only for contexts a consumer genuinely selects.** Light and dark qualify. Platform qualifies, and it sits *above* the brand layer rather than inside it, because platform is a context the consumer picks rather than a property of the brand: concretely, the surface token resolves differently per platform and the template never needs to know which platform it is on. **(thin)** A campaign is not a mode, and neither is a format; those are places, and they belong to the place layer if they belong anywhere. *Test:* theme-swap.

**13. Build the place layer only when the map comes back a grid.** Write the repeated parts down one axis, slide, cover, kicker block, chart plate, pull quote, and the jobs down the other, and mark which part consumes which job at which value. If every job resolves to one value everywhere, the result is a column and the layer would hold nothing, so skip it. Build it only when two parts consume the same job at genuinely different values, which in practice means one template serving several brands or several formats. **(thin)** Most single-client systems come back a column. *Test:* map-shape.

**14. Make the file machine-readable even if nothing compiles it.** One file, names, values and aliases, dots as separators so grouping is available later, and never `$`, `{` or `}` in a name. This costs nothing now and it is the only thing that makes the private-value audit possible at all. *Test:* spec-legality, private-value audit.

## Choosing the segment order, and capping the depth

**Order segments by how you will search, broadest filter first. (thin)** For brand work that is category, then role, then variant: `color.surface.raised`, `type.body.lead`, `space.gap.tight`. The mechanism is retrieval rather than taxonomy. You type the category first because that is how you narrow, and once the broadest filter leads, alphabetical grouping does useful work for free: every colour token sorts together, every type token sorts together, and a reader scanning the file finds a family instead of a scatter.

This rule carries a warning that none of the others do. It is reasoned from one person's retrieval rationale rather than argued anywhere, published schemes that commit to an order commit to different orders without defending them, and the order is close to a one-way door: changing it after templates consume the names means a rename of every token at once. Choose it once, write the chosen order at the top of the file as a sentence, and do not revisit it casually.

**Cap names at three segments. (thin)** Eight and nine segment taxonomies exist to disambiguate thousands of tokens across several products, brands and platforms. A single-client brand system has tens. Apply eight segments to forty tokens and you get names where two segments carry the same information, which is the segment-count test's second clause and a reliable sign that depth was copied rather than needed. Keep a longer taxonomy as a checklist of what a name *could* encode, consult it once while deciding your order, then put it away.

## How to work

### Mode A: building the system

1. **Audit what exists before naming anything.** List every value actually in use across real finished pieces, not the values the brand book claims. You are looking for two specific shapes: one decision expressed as three slightly different values, which means the decision was never recorded, and one value doing three unrelated jobs, which means the system will break the first time one of those jobs changes.
2. **Write the raw layer as reference only, with plural namespaces.** Hex codes, the base unit, the typefaces. Put it somewhere the templates do not read from, so that the palette page in the brand folder is a derivation of the system rather than the system itself.
3. **Name the jobs.** For each thing a piece actually needs, the surface, the surface above it, the text on each, the accent, the hairline rule, each type role, give it a name that says what it is for. This layer is the system. If it is thin, the system is thin, and the symptom is templates reaching past it for raw values.
4. **State each scale as a rule: base, progression, named steps.** Linear for body, modular for display, each on its own line. Compute every step from the base. Then divide each value by the downscale factor and check the result against the 12pt floor and the 4pt separation requirement before you name anything.
5. **Record the contrast ratio on every text-and-surface pair** you intend people to use together, computed rather than assumed.
6. **Run the map-shape test and decide whether you need a place layer at all.** A column means skip it.
7. **Add modes only for real contexts**, with platform above the brand layer.
8. **Write the whole thing into one machine-readable file**, dot-separated, legal characters, aliases pointing at raw values and nothing pointing past the job layer.
9. **Run the tests below**, and specifically the base-change test and the derivation test before you hand anything over.

### Mode B: auditing a brand folder

1. For each name, decide whether it describes the value or the use, and count how many describe the value. Report the count against the total.
2. For each scale, find whether the rule is written anywhere. If only the outputs are listed, record that the scale cannot be extended.
3. Run the cold-read test on the colour names.
4. Run the rename test on anything named after an appearance, a campaign or a platform.
5. Change the base and count the edits.
6. Find every raw value appearing outside the raw layer, or record that the audit was not runnable because the system is not a searchable file.
7. Compute the contrast ratio of every stated text-and-surface pair and compare it against whatever the folder claims.
8. Report what a consumer would have to guess, named specifically.

## Tests

Each returns a verdict decidable from this file alone. An auditor with the spec file and a calculator can run all but two of them.

| Test | Catches | Verdict |
|---|---|---|
| **1. Cold-read** | A name that restates its value, or carries nothing | Show a name to someone who has not seen the system. Ask what value it returns, then which values it is definitely not. Fail if they state the exact value from the name alone. Fail separately if they cannot name one value it is definitely not. |
| **2. Rename** | Names describing appearance rather than rank | Change the design decision the token encodes: make the dark slide light. Fail if the name is now false. |
| **3. Format-move** | Sizes and positions wearing job names | Apply the spec to 1080 x 1080 having written it for 1080 x 1350. Fail every name that no longer applies. |
| **4. Base-change** | Results shipped in place of a rule | Change the stated base unit. Count the places you edit. Pass at exactly one. Fail at two or more. |
| **5. Value-recall** | Names a machine cannot resolve | Give a reader only the base line, then ask what `space.5` returns. Pass only if they compute it. Fail if they need the table. |
| **6. Map-shape** | A place layer built because published systems have one | Repeated parts on one axis, jobs on the other, marked with the value each part consumes. Fail, meaning build the layer, only if two parts consume one job at different values. Otherwise skip the layer. |
| **7. Theme-swap** | Mode values stranded outside the job layer | Switch light to dark. Count tokens edited by hand. Fail on any hand edit. |
| **8. Private-value audit** | Missing job tokens | Search the spec and every template for `#`, for `px`, and for any bare digit outside the raw layer. Fail on every hit; each one is a job you did not name. Runnable only if the system is a searchable text file. |
| **9. Spec-legality** | Names that break a parser | Search for `$`, `{`, `}` and spaces in any name. Then sort the names and look for two differing only by case or by separator. Fail on any hit. |
| **10. Alias-resolution** | Chains that terminate nowhere | Resolve each alias by following it. Fail any name that does not reach a literal value within three hops, and fail any name that revisits a name already visited. |
| **11. Derivation** | A spec that is an inventory | Ask for a step the spec does not list: the sixth spacing step, a display size above the largest named one. Fail if the answer is not computable from the stated base and progression. |
| **12. Floor** | Values that vanish in a feed | Divide every type size and every spacing value by the downscale factor of 3. Fail any type value landing below 12pt. Repeat at 4 and record which values fail only there. |
| **13. Step-distinctness** | One level wearing two names | Divide two adjacent display steps by 3. Fail if the results land within 4pt of each other. |
| **14. Contrast-guarantee** | A promise the pair no longer keeps | Compute the ratio for each stated text-and-surface pair. Fail if the pair carries no recorded ratio. Fail separately if the computed ratio is below the recorded one, or below 4.5:1 for normal-size text. |
| **15. Segment-count** | Depth copied rather than needed | Count segments in every name. Fail any name above three. Fail separately if two segments in one name carry the same information, such as `color.text.text-primary`. |
| **16. Two-scale** | One ratio doing display and body | Read the scale rules. Fail if there is one base and one progression covering both display and body sizes, or if either rule is absent. |

## Failure patterns

**The name restating the value.** `brand-orange: #FF5F1F`. There is no lookup, because the name and the value carry the same information. Nothing has been tokenised.

**Shipping results without the rule.** Four numbers and no base. The spec answers only at the four points someone wrote down.

**One scale doing two jobs.** Display and body forced onto one ratio, which produces display steps too close to read as levels and body steps too far apart to sit in a paragraph.

**A ratio that dies in the feed.** 1.125 on display type, giving adjacent steps two rendered points apart.

**Chained rounding.** Each step computed from the rounded step before it, so the stated rule and the shipped numbers disagree by the fourth step.

**Interface defaults on a canvas.** 8 and 16 pixel spacing, 16 pixel body type, carried over from screen interface work without multiplying by the downscale factor.

**Names describing appearance.** `dark-slide` dies the day the slide is light.

**Names describing a platform or a campaign.** `instagram-carousel-background` breaks the moment the format moves, and it was never a job in the first place.

**A place layer built because published systems describe one.** Run the map-shape test first; most single-client maps come back a column.

**Eight segments on forty tokens**, with two segments repeating the same information.

**T-shirt sizes anywhere a machine reads the spec**, unless the ramp is short and will never be extended.

**A ramp's step count taken as given.** Nine steps of anything is rare in brand work; three to five is typical, and that is exactly the case where role names beat numbers.

**A contrast pair whose values drifted.** Both names still read correctly and the promise underneath them is gone.

**Citing efficiency gains as the reason to build a system.** That claim has no measurement behind it anywhere. Argue from derivability and from handoff, which are demonstrable, and leave speed alone.

## The audit you cannot run on a design file

The sharpest instrument available for finding a system's missing vocabulary is mechanical: mark raw values so they are distinguishable in text, then search every consumer for the marker. Every hit is a place someone reached past the job layer, and each one names a job token you failed to define. It finds the gaps empirically rather than by introspection, which matters because introspection finds the jobs you already thought of.

**There is no search over a Figma file, a PDF brand book or a client's Canva account.** This is a missing capability rather than a translation problem, and a naming convention does not substitute for a search: you can mark the primitives perfectly and still have no way to ask where they were used.

The partial substitute is the reason step 8 of Mode A exists. If the brand system lives as a text file that people and agents read, the audit runs on that file, and test 8 above is its concrete form. That is the argument for a machine-readable brand folder even when nothing compiles it: not build tooling, which is irrelevant unless the system feeds a website, but auditability.

## One method per client, not one scheme across clients

A token system encodes the vocabulary of the organisation that made it, which is why published systems are named so differently from one another despite sharing a structure. For an agency that has a direct consequence: a client's system should use that client's words, which means **it will not port to the next client.** Do not build one naming scheme across a roster. Build one method and run it per client. What you reuse is this procedure, the tests, and your segment order. What you do not reuse is the names.

## Applied to a carousel system

Canvases are 1080 x 1080 and 1080 x 1350, with a downscale factor of 3 nominal and 4 as a stress test, per `reference/canvas-assumptions.md`.

**Spacing, derived.** 1080 factorises as 2 cubed times 3 cubed times 5, so its divisors include 18, 20 and 24. Take base 18: the canvas is 60 units wide and, at 1350, 75 units tall. Steps are whole multiples, named by proportion: `space.1` 18, `space.2` 36, `space.3` 54, `space.4` 72, `space.5` 90, `space.6` 108. Margin is `space.5`, so 90, leaving a live width of 1080 minus 180, which is 900. Gutter is `space.2`, so 36. At six columns the column width is (900 minus 5 x 36) / 6, which is (900 minus 180) / 6, which is 720 / 6, so 120. Every number is an integer, and `space.5` is resolvable by anyone who has read the base line. Margin, gutter and column width here are consequences of base 18 and not shared constants, since the canvas file fixes sizes and downscale factors and fixes nothing about grids: `dsn-grid`, which owns grid derivation, starts from a 72px margin with a 24px gutter and closes on 136px columns. This section demonstrates naming, so where a project needs one grid it takes that triple and this base changes to suit.

**The base-change test, computed.** Change the base from 18 to 20 and nothing else. Margin `space.5` becomes 100, live width becomes 880, gutter `space.2` becomes 40. Six columns now gives (880 minus 200) / 6, which is 680 / 6, so 113.33. Non-integer. Five columns gives (880 minus 160) / 5, which is 720 / 5, so 144. The test passes on its own terms, one edit, and it surfaces something worth knowing: the column count was never a token, it was a consequence of the base, and a spec that lists "6 columns" alongside the base has recorded a derived value as a decision. Record the rule instead: as many columns as divide the live width into integers at the stated gutter.

**Body type, derived from the floor.** The reliable rendered minimum is 12pt, so at a downscale of 3 the working floor is 36px. Linear in steps of 6: `type.caption` 36, `type.body` 42, `type.lead` 48, rendering at 12pt, 14pt and 16pt. At the 4x stress test those become 9pt, 10.5pt and 12pt, so the caption fails test 12 at 4x. If the piece has to survive 4x, the floor moves to 12 x 4, which is 48, and the band becomes `type.caption` 48, `type.body` 54, `type.lead` 60.

**Display type, derived from the body ceiling and the separation requirement.** The display base has to clear the body ceiling by a visible step. At the 4x-safe ceiling of 60, a base of 60 x 1.25 gives 75. Ratio 1.25, every step computed from the base: 75, then 75 x 1.25 is 93.75 which rounds to 94, then 75 x 1.5625 is 117.19 which rounds to 117, then 75 x 1.953 is 146.48 which rounds to 146. Named by job: `type.deck` 75, `type.headline` 94, `type.hero` 117, `type.cover` 146. Step-distinctness at a downscale of 3: 25pt, 31.3pt, 39pt, 48.7pt, so the smallest gap is 6.3pt, comfortably above the 4pt requirement. Check what 1.125 would have done instead: 75, 84, 95, 107, rendering at 25pt and 28pt for the first two, a 3pt gap, which fails test 13. That is the arithmetic behind principle 6.

**Why the two scales cannot be one.** The 4x-safe body band runs 48 to 60, a span of 1.25 across three steps. The display band runs 75 to 146, a span of 1.95 across four. One ratio producing both would have to be 1.08 or so at the bottom and 1.25 at the top, which is not a ratio. State two rules.

**Surfaces, not colours.** `color.surface.canvas`, `color.surface.raised`, `color.text.primary`, `color.text.on-accent`. This is the layer that makes dark mode and platform modes work at all, and the layer where a contrast promise can live.

**A contrast guarantee, computed.** Take `color.text.primary` as `#F2F2F2` and `color.surface.raised` as `#2B2B2B`. Relative luminance of `#F2F2F2` is 0.888; of `#2B2B2B` it is 0.024. The ratio is (0.888 plus 0.05) / (0.024 plus 0.05), which is 0.938 / 0.074, so 12.65:1. Record 12.65 on the pair. Now suppose someone lightens the raised surface to `#757575` because a slide looked heavy. Its luminance is 0.178, so the ratio becomes 0.938 / 0.228, which is 4.12:1. That is below the 4.5:1 floor for normal-size text. Both token names still read correctly, no build step complains, and the guarantee the pair was created to hold is gone. That is test 14's whole purpose, and it is the clearest case in this skill of a value drifting away from what its name promises.

**The gap between slides and the margin inside them are two different jobs**, even when they currently share the number 90. `space.gap.slide` and `space.margin.outer` both resolving to `space.5` today is correct; collapsing them into one token means the day you want wider outer margins you also change the rhythm between slides.

**One design at several fixed aspect ratios has no inherited solution.** Responsive patterns do not apply: they solve reflow, and a carousel does not reflow, it gets recomposed. Treat each format as its own resolution of the same roles, with the roles tokenised once and the per-format sizes computed from each canvas's own floor.

## Checklist

- [ ] Existing values audited from finished pieces before naming
- [ ] Raw layer exists, is reference only, and is marked by plural namespaces
- [ ] Every job named by what it is for
- [ ] Each scale written as a base plus a progression, with named steps
- [ ] Display and body scales stated separately
- [ ] Every step computed from the base, not from the rounded previous step
- [ ] Base chosen as a divisor of the canvas
- [ ] Every type value checked against the 12pt floor at 3x and at 4x
- [ ] Adjacent display steps at least 4pt apart once rendered
- [ ] Contrast ratio computed and recorded on every text-and-surface pair
- [ ] Segment order chosen, broadest filter first, written at the top of the file
- [ ] No name above three segments, no segment repeating another
- [ ] Place layer built only if the map-shape test returned a grid
- [ ] Modes limited to contexts a consumer selects, platform above brand
- [ ] File is machine-readable, dot-separated, legal characters, aliases resolving to literals
- [ ] Base-change test run
- [ ] Derivation test run on a step the spec does not list

## The ultimate test

Give the spec and no examples to an agent, ask for a piece in a format the spec has never covered, and see whether it derives the values or invents them.

If it derives them, you wrote rules. If it invents them, you wrote a list, and the list will be wrong in exactly the places you left implicit.

## What an agent can run, and what it cannot

**Runs fully, with no judgement required.** The spec-legality scan, which is a character search and a sort. The alias-resolution test, which is a traversal. The private-value audit, which is a search for `#`, `px` and bare digits outside the raw layer, and which is runnable precisely because the spec is a text file. The base-change test, by substituting the base and recomputing every derived value. The derivation test, by being asked for a step the spec does not list. The value-recall test, by being given only the base line. The floor test and the step-distinctness test, which are division. The contrast-guarantee test, which is the luminance formula and a comparison. The segment-count test. The two-scale test. Listing every name that describes a value rather than a use.

**Runs partially.** The cold-read test, by stating what it expects a name to return before being shown the value, which is a genuine cold read for a name it has not seen but tells you nothing about how a client's team will read it. The rename test, by checking whether a name contains an appearance word, which catches `dark-slide` and misses a name that is misleading for reasons no word in it reveals. The format-move test, by recomputing for the second canvas, which catches names that encode sizes and not names that encode a position only a person can see is wrong.

**Cannot run.** The private-value audit over design files, because no search exists over a Figma file, a PDF brand book or a Canva account. Whether a job name matches how the client's team actually talks, which is the one input the whole naming scheme rests on and the one an agent has no access to. Whether a composite value such as a gradient or a multi-layer shadow survives being aliased in a given tool, which changes with that tool's release notes.

**What breaks when a name is wrong.** A name that describes its value leaves nothing to reach for. Ask an agent for a darker surface in a system whose only colour token is `brand-orange: #FF5F1F` and there is no token that answers, so it writes a hex directly into the piece. The piece now carries a colour outside the palette, no step failed, and the drift is invisible until someone audits the output rather than the spec. A name that cannot be resolved produces a plausible default instead: `space.large` with no base stated gets 24, because 24 is common in interface work, and 24 on a 1080 canvas renders as 8pt of gap, which reads as a rendering fault rather than a design decision. A name above three segments or duplicated under two separators, `color.textPrimary` beside `color.text-primary`, resolves by whichever the consumer sees last, so the same spec produces different pieces depending on file order. An illegal character is worse than a crash: `$` and braces are interpolation syntax in most token formats, so a name carrying them often resolves to an empty string rather than erroring, and an empty colour renders as transparent or as a tool default while the build reports success. An alias cycle, `color.text.primary` pointing at `color.text.body` pointing back, either recurses or returns the alias name as a literal string, which a renderer treats as an unknown colour keyword and silently ignores.

**What breaks when a value drifts from its source.** This is the failure that produces no error anywhere. The contrast pair computed above goes from 12.65:1 to 4.12:1 because someone adjusted a surface by eye, both names still read correctly, and the guarantee is gone with no record that it was ever made. The same shape appears in scales: edit one shipped type size because a headline looked large on one slide, and the stated base and ratio no longer generate the numbers in the file, so the next agent to extend the scale produces values that disagree with the existing ones and has no way to tell which set is authoritative. Hence two habits: record the ratio on the pair, and treat any hand-edited derived value as a bug in the rule rather than a fix to the output. If a derived value is wrong, the base or the progression is wrong.

## Where this skill should lose

**When the question is what the identity consists of and what each element's value should be.** Use `dsn-identity`. That skill owns which elements exist, their inventory, and the coherence rules that bind them; this skill owns giving those decided values names that resolve, and nothing else. The boundary is the one readers get wrong, so state it as a question: a reader deciding *which* colour, which typeface, which element belongs in the system is upstream of this file and should close it. A reader who has a colour and needs it to have a name a build step or an agent can look up is in the right place. Put plainly, `dsn-identity` decides that the brand has a raised surface and that it is a particular dark grey. This skill decides that it is called `color.surface.raised`, that it resolves through an alias to a primitive, and that the pair it forms with the text on it records a contrast ratio of 12.65:1.

**When the question is which colours to choose, or how a palette should be structured.** Use `dsn-palette`. This skill will happily name a palette that does not work. If instead the question is what a colour you already have is doing in a frame, meaning the job it performs, its tonal value and how it behaves against its neighbours, that is `dsn-color`. Both of those decide values; this skill takes a decided value and gives it a name, and it decides no value of its own.

**When the question is where the margin and the columns are.** Use `dsn-grid`, which computes the margin, the column count, the gutter and which columns an element spans for a given canvas. This skill turns those figures into names a build step resolves and an agent can extend, which is useful only once the figures exist. Practical version: if you are asking how many columns, you are in that file. If you are asking whether the figure should be called `layout.gutter` or `space.300` and what produces the next value up, you are here.

**When the values belong to a drawn thing rather than to a layout.** The construction of one mark and its lockup is `dsn-mark`, and the keyline grid, stroke weight, corner treatment and minimum size of an icon set are `dsn-icon`. This skill names the numbers those files settle, which matters most for an icon set, since a stroke weight and a minimum size that live only in prose get retyped and drift. It decides none of them.

**When the question is what size, leading, tracking or measure to set.** Use `dsn-typeset`, which owns the scale's content and the legibility audit on it. This skill owns the scale's *form*: that it is stated as a base and a progression, that its steps are named by job, and that it is one of two scales rather than one. If you are deciding what the body size should be, that is theirs. If you are deciding what to call it and how the next step is derived, that is here.

**When the question is how much space a layout needs.** Use `dsn-spacing`. The arithmetic above derives a spacing scale as a demonstration of naming, not as a judgement about whether 90px of margin is right for a given piece.

**When the question is whether text is readable against its background.** Use `dsn-contrast`, which owns the ratios, the thresholds and the fixes. Principle 11 and test 14 here only insist that whatever ratio you were given gets recorded on the token pair and rechecked when a value moves.

**When the question is which parts repeat across a deck and in what order.** Use `dsn-sequence`. The map-shape test needs a list of repeated parts as an input and does not produce one.

Sources, transfer assessment, corroboration, refused claims and the gaps no source covers are in `references/provenance.md`.

## Writing the output

When auditing, report in this order:

1. How many names describe values rather than uses, as a count out of the total.
2. Which scales ship results with no rule, so cannot be extended.
3. Edits required by the base-change test.
4. Names failing the rename, format-move or segment-count tests, listed individually.
5. Raw values found outside the raw layer, or an explicit note that the audit was not runnable because the system is not a searchable file.
6. Contrast pairs whose computed ratio is below 4.5:1 or below what the folder claims, with both numbers shown.
7. What a consumer would have to guess, named specifically rather than characterised.
8. One verdict: a derivable system, a list with some rules in it, or a palette page.

Give the arithmetic, not the conclusion: "base 18, so `space.5` is 90, so the live width is 900" beats "the spacing is consistent." Name a default as a default at the point you use it.
