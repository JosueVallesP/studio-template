# dsn-tokens: sources, transfer assessment and corroboration

Six videos, roughly 174 minutes. Full findings in `~/research/design-plugin/extracts/tokens_findings.md`.

## Sources

| ID | Who | Min | What it is |
|---|---|---|---|
| `irsPXBHjPXs` | Into Design Systems conference, several speakers | 84 | Multi-speaker. The only source where practitioners disagree with each other on camera, which is its main value |
| `kCgoc19VrXw` | Kevin Muldoon, Medium Day | 28 | Naming taxonomy. Best test instrument, worst evidence for it |
| `UmAqcGw9trc` | Kevin Zolkiewicz, 8th Light | 26 | Layer architecture. Poses the corpus's unanswered question |
| `9w-BwzcuxYM` | Hoonie XP | 13 | The only empirical dataset. Serious method problems |
| `JyCmacSyDY4` | Figma | 13 | **Vendor source.** Tool capabilities presented as architecture |
| `Uv-BAqUWt3A` | Systematically | 9 | Parametric scales. Shortest source, highest density, most transferable |

**Not a graphic-design corpus.** Five of six are about shipping software UI; the sixth is web typography. Nothing here was imported without assessment.

**One vendor source.** Figma's video is a map of one tool's current capabilities presented as token architecture, and it will be wrong on a timetable set by that tool's release notes. Its one durable contribution is a real constraint: composite values such as gradients, multi-fill and multi-shadow resolve differently from scalar ones in every tool, so some brand decisions will live as composites that cannot be aliased cleanly.

## Transfer assessment

### Transfers intact

- **The three-layer split as value → job → place.** The only medium-independent idea in the corpus, and the naming-direction test transfers word for word.
- **Primitives are reference-only.** A template reaching for a raw hex has the same disease a button does.
- **Write the rule, not the results.** The single most important transfer, specifically because of the agent handoff.
- **Jobs as step names rather than t-shirt sizes.** Transfers *better* than it works in code, because brand roles are stable across formats where pixel values are not.
- **Two jobs, two scales.** Display and body have no arithmetic relationship. Linear for body, modular for display.
- **Proportional naming where machines read the spec.**
- **The plural trick, which encodes the tier in one character.** A plural namespace marks a raw value and a singular one marks a decision, so `colors.blue.500` is unmistakably a primitive and `color.text.default` is unmistakably a job-layer token. One character, nothing to memorise, and it survives being read by someone who has never seen the system.
- **The rename and cold-read tests.** The cold-read test is sharper for client work than for internal systems: an internal team acclimatises to a misleading name, a client's team reads the folder once and never asks.
- **Conway's law, inverted.** A system encodes its organisation's vocabulary, so a client system will not port to the next client. One method per client, not one scheme across the roster.
- **The name/value redundancy failure.** A brand page listing a hex beside a colour name has tokenised nothing, and this is the most common state of brand books in the wild.

### Transfers with modification

- **The place layer.** Run the map-shape test honestly and most single-client systems come back a column, meaning skip it. The vendor source's own caveat confines it to large enterprise systems.
- **Modes.** Light and dark unchanged. Platform works as a mode, and the conference audience's correction to the speaker is the right shape: platform is a context the consumer selects, so it sits above the brand layer, not inside it.
- **Numeric ramps.** The direction rule and the insertion mechanic transfer. But brand systems rarely need nine steps; three to five is typical, which is the case where one source himself says role names are fine.
- **The typographic counts.** Four levels with roughly 4 / 6 / 3 / 3 styles each is a usable starting shape, and the count discipline is the useful part, six heading styles, not sixteen. The line-height bands and letter-spacing ranges are reasonable first guesses **with the source's own caveat applied harder than he applies it**: they are means across 127 *web* styles at screen reading distance, and a 1080px carousel read at thumb distance is a different optical problem. His closing note is the operative one, that fonts render differently even on identical specs and need adjusting by eye.

### Does not transfer

- **The underscore-and-search audit.** The best instrument in the corpus, and there is no search over a Figma file, a PDF brand book or a Canva account. **A real missing capability, not a translation problem**, and named as such in the skill. Partial substitute: if the system lives as a JSON file an agent reads, the audit is runnable on that file, which is the argument for machine-readable brand folders even when nothing compiles them.
- **Build toolchains, multi-platform transforms, package versioning.** Irrelevant unless the system feeds a website. The *shape* (one file, names, values, aliases) is worth copying; the toolchain is not.
- **Breakpoints and responsive text scaling.** Carousels are fixed-canvas. The analogous problem, one design across several fixed aspect ratios, is structurally different and **no source addresses it.** Responsive patterns solve reflow; a carousel does not reflow, it gets recomposed.
- **The eight- and nine-segment taxonomies at full size.** Built to disambiguate thousands of tokens across products, brands and platforms. Useful only as a checklist of what a name could encode.
- **Spec-compliance and separator politics**, except two parts that cost nothing: no `$`, `{` or `}` in a name, and use dots.

## Quotations and locators moved out of SKILL.md

The legibility pass stripped bracketed IDs and attributed quotations from the body. They are recorded here in full.

| Claim as it appears in the skill | Source quotation and locator |
|---|---|
| Write the rule, not the results | A file recording only outputs "stores the results and keeps the rule a secret" [`Uv-BAqUWt3A` 00:00:02] |
| A name restating its value has tokenised nothing | If the name carries the exact value, "these are not design tokens" [`irsPXBHjPXs` 00:35:52] |
| Raw values are the only layer whose names describe what they return | Primitives are "the only tokens where the name describes the value they return rather than describing how they are used" [`UmAqcGw9trc` 00:03:44] |
| Two jobs means two scales | "font sizes, 16 and 32, but those were never two steps of one range. They're two different jobs" [`Uv-BAqUWt3A` 00:05:48] |
| Name by job, not by size | [`Uv-BAqUWt3A` 00:06:40] |
| A name must survive the decision changing | `outlined` renamed to `tier 2` because the appearance was negotiable and the rank was not [`irsPXBHjPXs` 00:12:55] |
| Proportional names beat t-shirt names where a machine reads the spec | `space.4` against a stated base of 8 [`UmAqcGw9trc` 00:16:48] |
| Order segments broadest filter first | "if I frontload the token with that information I can easily find what I'm looking for" [`irsPXBHjPXs` 00:54:03] |
| Segment order named as the hard problem, then not answered | [`UmAqcGw9trc` 00:06:43] |
| The underscore-and-search audit | [`UmAqcGw9trc` 00:12:42-00:14:02] |
| A system encodes its organisation's vocabulary, so it will not port | [`kCgoc19VrXw` 00:12:07] |

## Numbers the skill supplies itself

None of these is inherited. They are derived in the skill's Applied section from `reference/canvas-assumptions.md` or chosen as defaults for this plugin, and each is marked **(thin)** or shown as arithmetic in the body.

- **Base 18 for spacing.** Method derived: pick a divisor of 1080 so margins, gutters and columns come out as integers. The choice of 18 over 20 or 24 is house style.
- **Ratio 1.25 for display type.** Chosen because the minimum ratio is derived from the 4pt rendered-separation requirement and 1.25 clears it at every display size in use; 1.125 is shown failing.
- **4pt minimum rendered separation between adjacent display steps.** A default for this skill. `canvas-assumptions.md` observes that 1.125 produces steps two rendered points apart and calls that one level wearing two names; the 4pt figure turns that observation into a threshold and is not from any source.
- **Three-segment cap.** A default for brand-scale systems. The published taxonomies run to eight and nine segments and both authors concede most tokens use three or four, which is the only support for the cap.
- **Three to five ramp steps as typical.** Inherited as an impression, not a measurement.

## Rules the skill marks (thin)

Principle 2 (exactly three layers), principle 3 (the plural trick), principle 8 (base 18 specifically), principle 12 (platform as a mode above the brand layer), principle 13 (most single-client maps come back a column), the segment order rule and the three-segment cap.

## Corroboration

**CRAFT, with a serious caveat**: the three-layer architecture is agreed across four sources, though they disagree on what to call the middle layer and on whether anyone may ever apply a primitive directly.

**That agreement is probably one article read several times, and the evidence is explicit rather than inferred.** One source openly credits his three tiers to a named blog post and his nine naming segments to a different named blog post. Two others present the same structure with no attribution at all. So what reads as multi-source corroboration on the corpus's most load-bearing claim is one lineage restated, and the same source's own survey of systems in the wild found eight or nine *competing* tier names, which is what genuine independent arrival actually looks like. **Treat the three layers as a convention with a traceable origin, not as a converged finding.**

**CONTESTED, and the skill takes a position:**

| Question | State |
|---|---|
| **Segment order** | **Unanswered by every source.** One names it as the hard problem and warns it is a one-way door, then does not answer. Another says play with it. A third says modify the template. The two schemas that commit, commit to different orders without arguing for either. The skill supplies a rule (broadest filter first, ordered by how you search) derived from one speaker's frontloading rationale |
| Does the namespace belong in the name? | Split |
| May anyone apply a primitive directly? | Split, and the reasons are more interesting than the positions. The vendor source says absolutely not and ships a product feature to enforce it. Another source actively *encourages* reaching past the job layer, **so that the shortcut leaves a searchable mark**, which is the mechanism the underscore-and-search audit depends on. Prohibition and permission are both instrumental, to opposite ends |
| Is the middle layer "semantic"? | Split on terminology, agreed on function |
| Is t-shirt sizing bad practice or standard? | Split, and reconcilable: fine for short ramps, bad where a machine reads the spec |
| One schema for all tokens, or one per layer? | Split |
| When are two layers enough? | No decision rule anywhere. One threshold is offered with no derivation |

**A pattern worth naming: four of the six sources close on some version of "there's no one right way"**, deployed precisely where a reader most needs an answer. That is why this skill takes a position on segment order rather than reproducing the hedge.

## Claims refused

- **"Companies that use design tokens are much faster."** No source, no comparison, no measure. This is the load-bearing business case for the corpus's longest talk and it is one unsupported sentence. **Never cite efficiency gains as the reason to build a token system.**
- **A fabricated survey result.** One source invents both a sample size and an outcome, guaranteeing 99-plus percent of 5,000 respondents would pick correctly, and uses the invented result as proof his fix works. No survey was run. **Keep his test, discard the number**; the instrument is genuinely the best in the corpus.
- **A team-count threshold for collapsing layers.** No mechanism. A threshold with no derivation is a convention.
- **A two-to-four-letter prefix rule.** Why that range is never said; the author's own examples span it.
- **"75% of systems use a major second ratio."** The most-cited empirical number in the corpus, and it is **an artifact of the fitting procedure**: matching observed sizes to the *nearest* named ratio clusters on the narrowest ratio by construction, because narrower ratios produce more closely-spaced steps that sit nearer any arbitrary set of sizes. The author also concedes the systems did not use all steps of their scales, which loosens the fit further. He names four ratios and **gives no numeric value for any of them**, so nothing in the section is reproducible. Unreproducible and probably wrong.
- **"The most common font."** 7 of 44, reached by collapsing three distinct typefaces into one bar, against a runner-up of 5 of 44. That is a flat distribution reported as a ranking.
- **The sample itself.** Drawn from systems that publish libraries to two directories, which is a sample of marketing behaviour. Credit to the author for naming the assumption; every downstream number inherits it.
- **Line-height means reported to two decimal places** and discarded in the next sentence in favour of round numbers. The precision is theatre. Four approximate bands are the usable content.
- **A monotone line-height trend that the author's own data contradicts.** He states that line height falls as size rises and explains it by legibility at small sizes. His smallest level has a *lower* line height than the level above it, which is the opposite of what his explanation predicts. He does not notice.
- **The most common naming convention may be a tool artifact.** The author flags this himself as an assumption: the convention is popular because it suits one tool's folder-grouping UI. If true, that is a significant finding stated as a throwaway, and **the convention should not be treated as craft.**
- **A self-contradiction inside two sentences** about the field being less than a decade old, immediately followed by examples from the 1970s.

## Gaps: what no source covers

1. **Segment order.** Covered above. The corpus's central void.
2. **Deprecation and migration.** A status field in one spreadsheet is the entire treatment of token lifecycle in 174 minutes. Nobody covers finding every consumer before deleting a token, how long to keep an alias alive, or how to version a breaking rename. **One source names the one-way-door trap and nobody offers the escape.** The nearest thing to a tool is a reverse-dependency lookup in one speaker's spreadsheet, which is exactly the primitive a deprecation process needs, and nobody connects it.
3. **How many primitives.** Everyone says not too many; nobody gives a number, a range or a derivation.
4. **Linting and validation.** Named by the corpus as the missing chapter, explicitly skipped for time. The only validation anywhere is a character scan.
5. **What a machine needs in order to *choose* a token** rather than merely parse one. **The largest gap relative to this plugin's purpose.** The one treatment of machines reading tokens is a formatter that tidies strings. Component tokens are justified partly on machine-legibility grounds and the mechanism is never spelled out.
6. **Encoding a contrast guarantee in a token pair.** One source built a contrast tool and never mentions contrast again in 28 minutes on naming. This is the one thing a job-layer colour token could actually enforce and a raw value cannot.
7. **When two layers are correct.** No decision rule. One instrument exists and it only answers the place-layer question.
8. **Anything that is not a CSS property.** Every category list in the corpus is a list of CSS property families. Nothing on tokenising image treatment, colour grading, illustration style, grid or compositional structure.
9. **Motion.** Appears twice as a list item and once as a spreadsheet column. Never developed, and actively excluded from the aliasing discussion by the vendor source.
10. **What a bad token system costs.** Many failure modes named, zero measured. Nobody compares a bad system to no system, which is the comparison that decides whether a small team should build one at all.
11. **One design at several fixed aspect ratios.** The dominant case in this plugin's work, and nobody addresses it.

## Known weaknesses

- **No source is about graphic design.** Every transfer is an argument, and the arguments are above rather than hidden.
- **The best test does not survive the move to design files**, and the second-best is stated in passing by a vendor.
- **The only empirical dataset is unreliable** and its headline figure is a method artifact.
- **The skill takes a position on segment order that no source would take.** It is reasoned from one speaker's search rationale, and it is the most likely thing in this file to be wrong. If it proves wrong, the cost is high, because that source is right that the order is hard to change later.
- The three-layer architecture, while agreed, is essentially one lineage restated, the sources share vocabulary and conference circuit, so agreement may reflect a common origin rather than independent arrival.
- Not run on live client work.

## Changed by the cross-skill numeric reconciliation

The shared floor is two figures, not one: 36px at the nominal 3x downscale and 48px at the 4x stress case, both delivering about 12pt rendered. A floor quoted without its case is incomplete. The framing is established in `reference/canvas-assumptions.md`, which also records that nothing shared fixes margins, columns or gutters.

- **The downscale-factor term.** Previously ended at a working-file floor of 36px, naming no case even though it had just named both factors. It now gives both floors and says to name the case whenever the floor is quoted. The body-type derivation lower down already carried both bands, 36 / 42 / 48 at the nominal case and 48 / 54 / 60 at the stress case, and is unchanged.
- **The spacing derivation.** Now says margin 90, gutter 36 and column 120 are consequences of base 18 rather than shared constants, and names `dsn-grid`'s 72, 24 and 136 as the triple a project takes when it needs one grid. This sits with the existing note that the arithmetic demonstrates naming rather than judging whether 90px of margin is right.
- **Values unchanged.** (900 - 5 x 36) / 6 = 120 still closes, as does the base-change test at base 20 giving 113.33 on six columns and 144 on five.
