# dsn-icon: sources and corroboration

## Sources

Twelve videos, twelve channels, roughly 25,000 words. All verified reachable with English captions at build time. Full findings in `~/research/design-plugin/extracts/icon_findings.md`.

### Icon-system half (7)

| ID | Channel | Min | Note |
|---|---|---|---|
| `EN-B481nG84` | Dewsign | 7 | Rules-first framing. Self-contradicts on decimals |
| `XqQ0ROz73bo` | Design with Mitch | 8 | Substantially a read-aloud of Material's docs. Clearest record of the keyline figures |
| `TXvlOwzwAQg` | Design With Kellie | 21 | Illustrator-based, but the best live diagnosis in the set |
| `iMPiXY_2pd4` | Couple of Designs | 17 | Illustrator workflow. Includes diagonals in its keyline grid |
| `9At1yFg901Y` | nikitisza | 5 | Dense, several arbitrary numbers |
| `eobqYu7wliE` | Christopher Deane | 9 | Only source addressing multiple canvas sizes. Figma-specific |
| `dY5rFtpZuec` | Voger Design | 8 | Only source citing a real study, and also a textbook unnamed-authority claim |

### Shape and silhouette half (5), different disciplines

| ID | Channel | Min | Discipline |
|---|---|---|---|
| `Zhz44T5pwtA` | Visign (Mathias Osland) | 26 | Character design |
| `jSun2GZzelU` | Faf Jr | 21 | Character silhouette. 36 views; content is substantive |
| `v6n9OYtaWZs` | Winged Canvas | 14 | Character design. Teaches and then retracts shape psychology |
| `l4OreGhpb-4` | Ufot Ubon | 36 | Brand illustration systems. Published the day before build |
| `pg1NpMmPv48` | TED-Ed (Eric Broug) | 5 | Islamic geometric pattern. Not about icons |

Twelve channels for twelve videos, so no channel concentration, the best diversity of any block in this plugin. The real risk here is not one voice but **one tradition**: four of the seven icon sources derive their figures from Google's Material guidance, so apparent agreement on keyline dimensions is one specification reported four times, not four independent findings.

### One source may be synthetic, and the skill's optical principle rests on it

**`EN-B481nG84` carries a provenance warning that was not in the original curation.** Uniform pitch, no stumbles, a channel publishing English voiceover under a non-English name, and a tell a working practitioner would be unlikely to produce: it forbids decimal stroke values as blurry and then recommends 1.5px fifty seconds later.

It is also **the densest mechanics source in the corpus and the only one that states the optical-weight principle at all.** So it was kept rather than dropped, and the consequence has to be stated plainly: the skill's equal-mass principle has a possibly-scripted single source behind it, and the derived equal-area rule exists partly to give that principle a footing that does not depend on it. **Verify every figure from this source against the primary published systems before citing any of them anywhere public.**

Two smaller provenance notes. `jSun2GZzelU` is genuine but padded, roughly four usable minutes out of twenty-one. `l4OreGhpb-4` contains **zero numbers** and still supplies the best consistency formulation in the corpus, which is itself a finding about where the useful material lives.

### Tool-default risk

Several house-style rules may be tool idiom rather than craft, flagged because an agent cannot tell the difference. High risk: the `icon/name/size` naming convention and flatten-to-one-semantic-colour-variable, both Figma features [`eobqYu7wliE`]; the outline-view shortcut sweep, an Illustrator mechanic whose underlying idea does generalise [`TXvlOwzwAQg`]. Medium: round caps and joins stated as a click rather than a decision; draw-with-strokes-expand-last.

## Corroboration

**CRAFT: three or more independent sources**

| Rule | n |
|---|---|
| Every member on one shared grid at one size | 6, plus the pattern tradition independently |
| One stroke weight across the set | 5 |
| An untouched trim ring no element enters | 4 |
| One corner radius across the set | 4 |
| Judge the set as a row, not icon by icon | 4, both disciplines |
| Readability beats cohesion where they conflict | 4, both disciplines |
| Reduce detail to the minimum that still identifies | 4, both disciplines |
| A set is defined by shared repeatable rules, not member count | 4 |
| Decide fill-or-line for the family before drawing | 3 |
| A shared shape vocabulary reused across members | 3 |

**Reported honestly as below the bar:** the silhouette test *as a procedure you run* has two sources, both character designers, so one discipline. It is the most useful procedure in the corpus and it is less corroborated than it feels. Stated as such in the skill.

**CONTESTED**

| Question | Positions |
|---|---|
| Stroke weight at 24px | 2px (2 sources) vs 1.5px (2 sources). As ratios of canvas, 8.33% vs 6.25% |
| Are decimal stroke values legitimate? | Forbidden as blurry vs shipped as house standard. And the source forbidding them recommends 1.5px fifty seconds later |
| **Must members match in visual mass?** | Yes, that is the purpose of keylines, vs explicitly no, that is "definitely okay". **The core optical question.** Resolved in the skill by the dissenting source's own demonstration, where she catches and fixes an unequal member |
| Corner radius | 2px vs 3-or-5px-and-odd vs "max" |
| One stroke weight, or one per size? | Constant (3 sources) vs scaled across 16/24/32/64 (1 source, the only one addressing multiple sizes). Reconcilable as constant-within-size and scaled-across-sizes, but **no source says so** |
| Mixing fill and outline in one set | Forbidden vs allowed to express state vs ship both as parallel sets |
| Rotating a narrow icon to fill the container | Recommended vs cautioned against in the underlying Material guidance |
| Does shape carry personality? | Asserted by 2, retracted by 1 of those 2 |

**Derived, not sourced**, flagged because the skill uses it. Treating the four Material keylines as an equal-area system reproduces the published figures to within about 3%; the equal-area circle for an 18px square computes to ⌀20.31 against Google's 20. This converts a four-row lookup table into a rule extensible to shapes Material does not cover. **No source states, derives or even explains the four numbers.** Check by eye before trusting it on a new shape.

## The shape-meaning assessment

The skill's boundary was set before mining and the mining was asked to test it in both directions. Result:

**Against inherent shape personality.** Three claims in twelve sources. Support offered: assertion plus post-hoc readings of finished work by someone who already knew both shape and personality. Zero studies, zero mechanisms, zero predictions, zero naive-viewer tests. One asserting source downgrades it to a jumping-off point and names a counter-example from its own discipline. The other names feeling as the mechanism. A third mentions colour psychology in a single clause with no content.

**The one real citation.** Wertheimer, 1923, on perceptual grouping, correctly named and dated, the only named study in the corpus. It supports grouping by proximity and similarity, which genuinely underwrites set consistency. It supports nothing about affect. The same source then asserts that consistency builds trust with no name, study or date.

**What survived.** Geometric difference, which supports differentiation and is testable. Resemblance to a referent, which is iconographic rather than psychological, is filed under shape psychology by its source, does not belong there, and is the most important mechanism in the skill.

## Gaps: what no source covers

Listed because they bound the skill's authority.

- **Diagonal stroke-weight compensation is absent.** It was briefed as a target and does not exist in the corpus; only angle snapping. **Not inherited.** Source it elsewhere or leave it out.
- No general rule for optical size equalisation, and no way to extend Material's four keylines to a hexagon, diamond, triangle or rounded square. The derived rule above fills this and is marked derived.
- No terminal taxonomy. Butt, round and square caps are never compared. Never noted that a round cap extends a stroke by half its weight past the path end, changing both apparent length and weight.
- No rule relating corner radius to stroke weight or canvas size, despite three sources specifying both.
- Nothing on apparent weight of a filled shape versus a stroked outline of the same silhouette, which matters for the two sources recommending both.
- **Nothing on dark mode** beyond a colour-token swap. Light-on-dark stroke bloom is not mentioned by anyone.
- **No size-down test anywhere.** Assembled in the skill from four fragments and labelled as assembled.
- No legibility floor stated as a gate. No icon tested on a user; both silhouette tests are self-administered.
- **No accessibility content at all.** No stroke-contrast minimum, nothing for low vision, nothing on whether an icon can stand without a label.
- **How to distinguish semantically adjacent icons is never raised by any icon source.** The character sources solve the identical problem and nobody connects them. The adjacent-pair test is that transfer, labelled as such.
- Nothing on how to choose a canvas size beyond naming what the big systems chose; nothing on multiple keyline families for different contexts; nothing on RTL mirroring or culturally variable metaphors; nothing on naming beyond one convention; nothing on duotone systems.
- Nobody builds icons constructively from a divided circle and its construction lines, the one source that works that way is about geometric pattern, not icons. Every icon source fits drawings into bounding boxes instead.

## Claims refused

- Shapes carry inherent personality. Covered above.
- "Psychologists tell us that consistency is what builds trust... if we see them, we relax." No name, study or date.
- Consistency makes a product read as professional, trustworthy and expensive. Asserted.
- Odd-numbered corner radii, 3 or 5px. No reason offered for odd.
- A five-colour ceiling for icons. Arbitrary.
- "part of becoming a great designer is... knowing when to break the rules... trust me on this." The warrant is the phrase.
- A 2px stroke "delivers your brand's voice in the most stable and reliable way." Meaningless.
- 15° increments to minimise half-pixels. The 45° case is mechanically sound; 15° does not generally minimise half-pixel positions and no reason is given.
- An unsourced count of plugin launches per quarter, load-bearing for nothing.
- Colour psychology, asserted in one clause with no content or referent.
- "if you trust the process and maintain a good quality throughout the final outcome will be consistent." Process faith.

One honest non-rule worth preserving as a model: one source narrates picking a stroke weight as taste rather than law, one is too light, two too heavy, try 1.5 [`TXvlOwzwAQg` 00:07:30]. That is the right way to narrate taste. It should not be cited as independent confirmation of another source's 1.5px, though it does land on the same number, which is weak convergence.

## Material moved out of SKILL.md in the legibility pass

Recorded here so nothing is lost. The skill body now carries the mechanism and omits the attribution.

**Keyline figures as reported.** On a 24px canvas with a 20px live area and a 2px padding ring [`XqQ0ROz73bo` 00:00:40]: square 18 x 18, circle ⌀20, "vertical rectangle" 20 x 16, "horizontal rectangle" 16 x 20 [`XqQ0ROz73bo` 00:01:24], restated at 00:03:57 and 00:05:09. The labels are transposed or quoted height-first, since "vertical 20 by 16" read as width x height is wider than tall; the magnitude pair {16, 20} is not in doubt. The skill states orientation in its own terms rather than inheriting the ambiguity. A second source uses the identical grid and names the same four shapes without stating a single dimension [`TXvlOwzwAQg` 00:03:44]. A "dense live area and dense padding" variant is mentioned once with no figures [`XqQ0ROz73bo` 00:00:40].

**Stroke-weight positions.** 2px as standard [`EN-B481nG84` 00:04:12], [`9At1yFg901Y` 00:01:19]; 1.5px at 24px [`eobqYu7wliE` 00:01:21], [`TXvlOwzwAQg` 00:07:30]; whole pixels only, decimals "creating a half-pixel blur effect" [`EN-B481nG84` 00:04:55], contradicted fifty seconds later by a 1.5px recommendation at 00:05:44. Per-size table 1 / 1.5 / 2 / 3 px at 16 / 24 / 32 / 64 [`eobqYu7wliE` 00:00:40]-[00:01:21], whose encoded rule is a constant 6.25% of canvas to 32px then thinner, never stated by its author. The 2px standard is 8.33% of 24px.

**Trim ring.** 2px on 24px [`XqQ0ROz73bo` 00:00:40], [`TXvlOwzwAQg` 00:03:44]; per-size 1 / 2 / 2 / 4 px [`eobqYu7wliE` 00:00:40]; the mechanical reason given once, that edges "can get slightly cut off on real devices" [`EN-B481nG84` 00:03:22]. The same source publishing 2px works to roughly 4px in practice and still calls it tight [`eobqYu7wliE` 00:06:35].

**Corner radius.** 2px reused across a set [`TXvlOwzwAQg` 00:06:19]; odd numbers, 3 or 5px, no reason given [`9At1yFg901Y` 00:01:19]; "corner radius to max", 20px and 35px on a 200px grid [`iMPiXY_2pd4` 00:10:34, 00:14:23, 00:16:27], normalising to roughly 2.4 and 4.2px at 24px.

**Equal-mass conflict, and its resolution.** Keylines exist so shapes "share the exact same visual weight" [`EN-B481nG84` 00:02:30]-[00:03:22] against unequal mass being "definitely okay in an icon set" [`TXvlOwzwAQg` 00:11:35]. The dissenting source then lays her set in a row, spots a paintbrush reading small because its corner "is not going to that two pixel line", and fixes it [`TXvlOwzwAQg` 00:11:35]-[00:12:11]. The skill follows the demonstration and keeps the dissent as the limit in principle 7.

**Gaps, centring, output.** Internal gaps equal to stroke weight, measured with a 1.5px spacer rectangle in hot pink [`TXvlOwzwAQg` 00:08:47]-[00:09:21]; internal spacing held constant "for example 3 pixel" [`9At1yFg901Y` 00:02:36]; optical centring of nested elements, with a logo mark whose triangle "is not exactly in the center" as the example [`9At1yFg901Y` 00:02:36]; stroke set inside the path [`iMPiXY_2pd4` 00:09:10], and the fill-to-outline trim breach [`TXvlOwzwAQg` 00:16:13]; live strokes that "may or may not scale" [`TXvlOwzwAQg` 00:12:48]; outline-view sweep for "little baby shapes" [`TXvlOwzwAQg` 00:15:01].

**Cross-discipline rules and their origin.** Silhouette test [`jSun2GZzelU` 00:00:00, 00:03:23, 00:18:34], [`Zhz44T5pwtA` 00:05:13]; negative space between parts [`jSun2GZzelU` 00:13:16]-[00:14:40]; blob collapse, "it won't read if we fill this up, it's gone" [`jSun2GZzelU` 00:15:36]-[00:16:37]; differentiation by dominant geometry across a cast [`v6n9OYtaWZs` 00:01:13]-[00:02:33]; two-tier size control [`Zhz44T5pwtA` 00:13:05, 00:15:08]; parent-shape reuse [`Zhz44T5pwtA` 00:19:57]; shape-ingredient decomposition [`Zhz44T5pwtA` 00:09:41]; detail-density matching [`Zhz44T5pwtA` 00:23:15]; redraw from memory [`Zhz44T5pwtA` 00:13:05]. Detail budgeted to display size, "for an icon set illustration, you need to take out a lot of the details" [`l4OreGhpb-4` 00:22:54]-[00:23:33], with the constraint that the reduced version still reads as the same family.

**Spec and consistency material.** Named features with named treatments [`l4OreGhpb-4` 00:12:44]; visual drift and "every brief starts from zero" as production failures [`l4OreGhpb-4` 00:19:41]; good versus good-for-the-brand [`l4OreGhpb-4` 00:19:41]; a set defined by "shared, repeatable logic" rather than member count [`l4OreGhpb-4` 00:11:55]; recognition over cohesiveness, "never sacrifice on clarity" [`9At1yFg901Y` 00:03:16]; grouping by proximity and similarity, correctly attributed to Wertheimer 1923 [`dY5rFtpZuec` 00:00:00], immediately followed by the unsourced "psychologists tell us that consistency is what builds trust" [`dY5rFtpZuec` 00:01:03].

**Angles.** The 45° case is mechanically sound; the 15°-increment claim [`EN-B481nG84` 00:04:55] does not generally minimise half-pixel positions and no reason is given. The skill keeps the first and drops the second.

**Corroboration counts stripped from the body.** They are already tabulated above. The body now carries a single plain-language confidence paragraph plus **(thin)** markers instead. Marked thin in the body: the trim ring figure, the stroke and radius figures, the optical-mass principle, the adjacent-pair transfer, the size-down test, the harvest step, the two-tier rule, the gap-equals-stroke rule, and the record-the-offset half of optical centring.

**Derivations the body now carries.** All three are checkable arithmetic rather than inherited figures, and all three are labelled in the body as derivations rather than conventions: the equal-area keyline system and its extension formulas (§2.1 above, generalised to circle, rectangle, triangle, hexagon and diamond); cap overshoot, where a round or square cap extends a line by half the stroke weight past its path end; and stroke-alignment overrun, where inside, centre and outside alignment consume none, half and all of the trim ring respectively. No source states any of the three. The cap and alignment arithmetic fill the "no terminal taxonomy" gap listed below.

## Known weaknesses

- **One tradition, not twelve.** Four icon sources trace their figures to Material. Agreement on keylines is one spec reported four times.
- **Five of twelve sources are from other disciplines.** Every transfer is assessed item by item in the findings file, and the two tests that come from the character half are labelled. But the skill's readability spine is borrowed, and the icon literature's silence on silhouette testing is itself a finding.
- **The most valuable consistency formulation comes from the newest and least-viewed source**, published a day before the build, from brand illustration rather than iconography.
- **No numbers here are principles.** Most are contested and several are arbitrary. The skill states this rather than picking a winner.
- Not run on live client work.
