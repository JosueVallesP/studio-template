# dsn-typeset provenance

Where the knowledge in `SKILL.md` came from, what each source uniquely supplied, where they contradict each other and how those contradictions were resolved, which figures survived and which were discarded, and what none of them cover.

This is the most number-dense skill in the plugin, so the discard list below is longer than the keep list. That is the correct ratio. Auto-captions mangle numbers more reliably than they mangle sentences, and a figure with no mechanism behind it cannot be checked against anything.

## Sources

**Hoonie XP, "Typography - Ultimate Design System Breakdown"**
`9w-BwzcuxYM`, 12m52s, 81k views, 2022-06-14. **The only source in the set that measures anything.** Tim extracted 127 text styles from 44 Figma design systems found through designsystems.com and designsystemsforfigma.com, put them in an Airtable, and sorted for patterns. Uniquely supplies: the four-level taxonomy of display, heading, body and label with average style counts per level (4 / 6 / 3 / 3) [00:03:21]; the whole naming taxonomy, four base types (typographic level, HTML tag, token, t-shirt size) and eight modifier types, with level + t-shirt + weight as the most common combination [00:03:21, 00:04:12, 00:05:08]; the type-scale ratio distribution, 75 percent major second, 16 percent minor third, 4.5 percent each major and minor second [00:06:48]; base body sizes clustering at 13, 14 and 16 [00:06:06]; the line-height gradient per level [00:08:37]; the letter-spacing gradient per level [00:09:37]; three named responsive methods with the systems that use each [00:10:26 onward]; the observation that systems do not use every step of their own scale [00:06:48]; and the note that systems setting absolute line heights use multiples of four to match a baseline or their spacing scale [00:07:36].

Its unique risk is being mistaken for evidence. It is a census of convention. It records what 44 teams shipped, not that any of it reads better.

**Kiran, "Complete Typography Guide for UI/UX Designers"**
`spyPKRE9Ers`, 135m59s, **634 views**, 2025-09-06. The longest source and the lowest viewed, which is the usual relationship in this corpus. A UI course worked live in Figma. Uniquely supplies: typographic anatomy with a stated *purpose* for each term rather than a definition, which is the thing that makes it usable, so x-height governs legibility at small sizes because of the white space inside each letter [00:08:31], aperture prevents a c reading as an o on a small screen [00:44:51], and stroke weight that is too light fails on low-resolution screens [00:13:43]; the empirical discovery of the leading floor, by watching a descender leave its text box at 90 percent and noticing the gap below it then looked like no gap at all [00:25:34]; the 50 to 75 character measure [00:48:43]; the mobile headline ceiling of 30 to 40 pixels, derived by dropping a 72 pixel headline onto a 428 wide iPhone frame and working down [00:59:00, 01:12:57]; the 12 pixel body floor and its single exception, 10 pixel bold in a five-icon bottom navigation [01:13:48]; jump sizes, two points noticeable at small sizes and four to six needed above body [01:12:01]; the classification of scale ratios into low, medium and high contrast with the argument that low-contrast ratios cannot build hierarchy on a phone [01:00:51]; the rejection of baseline grids [01:26:11]; the all-caps mechanism, that readers recognise word outlines through ascenders and descenders so caps force letter-by-letter reading, plus the screen-reader consequence [01:44:43, 01:45:35]; the weight-skip rule with the diagnosis "it looks like a mistake" [01:42:23]; the WCAG paragraph-spacing ratio [01:33:45]; alignment rules [01:37:13, 01:38:02]; the typeface history check, with Fraktur as the example [00:53:06]; and the icon-stroke-to-text-stroke match [02:03:49].

Also the most hedged and self-correcting source, which is a mark in its favour on mechanism and against it on every number.

**4 The Creatives, "Typography for Beginners: Fonts, Spacing and Layout Basics"**
`YYhaZop92Fg`, 113m39s, 10.7k views, 2026-03-11. A print and InDesign course, and the only source working outside a browser. Uniquely supplies: the leading default stated as a rule, leading at size plus 20 percent [00:30:23]; the tracking scope rule, that tracking belongs to caps and small caps and makes lowercase illegible, with the engraved-in-stone note on tracked caps [00:32:32]; the 2:1 headline to subhead ratio, worked [00:25:24, 00:26:10]; weight-skip corroboration including skipping three for stronger contrast [00:22:23]; width contrast, condensed against normal, as a contrast axis nobody else names [00:24:37]; rivers in justified type and the hyphenation tradeoff [00:36:53]; balance-ragged-lines and the staircase rag [00:37:37]; orphans, widows and runts [00:39:00]; never stretch or condense type [00:39:00]; small caps only when drawn into the typeface [00:14:17]; drop caps and ligatures [00:12:11, 00:16:23]; the overshoot of rounded letters being already drawn in by the type designer [00:11:26]; and the reliable and avoid typeface lists [00:40:38].

Its three worked builds are the most valuable part and nobody narrates what they show: in all three, **type size is chosen by fitting a word to the column width,** not by stepping a scale. "Sunset" lands at 108 because that is where it reaches the margin [00:46:48]. That is the central mechanism of this skill being used without being named.

**Tonic, "How to set up your typography sizing and line height for web design"**
`eW2-ghXuYC8`, 16m11s, 41k views, 2023-01-23. A studio workflow in Figma with typescale.com, inheriting its scale from Finsweet's Client First. Uniquely supplies: the reverse derivation in practice, where he rejects 48 as too small, decides by eye that "something more like 72 might be pretty good", and then hunts for the ratio that lands near it [00:02:25, 00:05:05]; line height as a percentage rather than an absolute, because it survives a later size change, demonstrated by undoing the failure [00:06:57, 00:07:39]; rounding 75.76 to 76 because a developer should not be handed 75.76 [00:06:17]; and the explicit admission that his five body sizes are off-scale and "isn't really based on anything" [00:10:59].

Also supplies, without noticing, the fact the skill builds its floor argument on: his scale generates 13, 10 and 7 below base and he discards all three, "these in my opinion are too small... we ignore them" [00:11:37].

**Satori Graphics, "Typography Skills to Instantly Improve Your Graphic Designs"**
`Dptb5xojbJM`, 10m16s, 59k views, 2024-12-11. The craft source, and the only one on optical work. Uniquely supplies: optical enlargement of rounded letters in logos and titles [00:00:41]; never auto-kern a logo or heading [00:01:24]; tracking as expression [00:02:11]; typeface psychology [00:05:15 onward]; and the eye-training method, which is the most practical thing in it, study type in the wild, redesign an existing logo in a different category, and practise on Kern Type and Type Connection [00:03:46, 00:08:29].

Contains a Framer advertisement at [00:03:46] to [00:05:15], roughly 15 percent of its runtime.

## Corroboration

**Taught by two or more independent channels, so settled enough to act on:**

| Move | Channels |
|---|---|
| Four-level structure (display / heading / body / label) | Hoonie (measured), Kiran, Tonic |
| Tracking runs opposite to size | Hoonie (measured), Kiran (tested), Satori (register), 4TC (caps) |
| Leading runs opposite to size | Hoonie (measured), Kiran (bands), 4TC (1.2 on display) |
| Skip at least one weight to pair weights | Kiran, 4TC, independently and for the same reason |
| Two typefaces maximum | Kiran, 4TC |
| Pair on matching x-height | Kiran, 4TC |
| Caps need tracking and fail in long strings | Kiran, 4TC |
| x-height and aperture govern small-size legibility | Kiran, 4TC |
| Kerning is optical; auto-kerning fails on large type | Satori, 4TC (both send you to Kern Type) |
| Round generated decimals to whole or even numbers | Hoonie (measured), Tonic, Kiran |
| The two responsive strategies | Hoonie's method 1 is Kiran's "keep the scale, rebase"; Hoonie's 2 and 3 are Kiran's "keep the base, adjust the top" |

**Single-channel, so house style worth using but not consensus:**

- The naming taxonomy (Hoonie only). Weigh it differently from the rest of this list: it is one channel reporting a count across 44 systems, not one practitioner's preference.
- Leading bands of 80 to 120 percent for headings, 120 to 160 for body (Kiran).
- The 12 pixel body floor and the 10 pixel bold exception (Kiran).
- The 30 to 40 pixel mobile headline ceiling (Kiran).
- Low / medium / high contrast scale classification (Kiran).
- The baseline-grid rejection (Kiran), and it is an unargued dismissal.
- The 2:1 headline to subhead ratio (4TC).
- Leading at size plus 20 percent (4TC), which is the InDesign auto default restated as a rule.
- Rivers, rag balancing, orphan and widow repair (4TC, and print-shaped).
- Width contrast as an axis (4TC).
- Small caps, drop caps, ligatures (4TC).
- Optical enlargement of rounded letters (Satori, and contradicted below).
- Tracking as register, and typeface psychology (Satori, assertion with nothing offered).
- Reverse derivation from a chosen ceiling (Tonic), though it is the practice this skill adopts, because 4TC's builds do the same thing silently.
- The WCAG 1.5x paragraph-spacing ratio (Kiran), where the authority is the external standard rather than the channel.

## Where the sources disagree, and the decision rule

**1. How much contrast a scale ratio needs.** Hoonie's census puts 75 percent of 44 systems on a major second of 1.125 [9w-BwzcuxYM 00:06:48]. Kiran calls the low-contrast ratios useless, "these two are actually useless", because a 24 beside a 22 cannot build hierarchy, and prefers minor and major third for mobile [spyPKRE9Ers 01:00:51].
*Rule: both are right for their canvas, and the variable is ramp length against the smallest visible rendered difference.* A product system needs many closely spaced sizes to cover dense application screens, and 1.125 supplies them. A five-step scale on a canvas downscaled threefold cannot spend a step nobody can see. The 1.125 majority is an artifact of ramp length, not of perception. This is the most consequential disagreement in the set and `SKILL.md` resolves it toward Kiran for Josué's canvas while keeping Hoonie's distribution as the reason why.

**2. Line height in percentages or absolutes.** Tonic: always percentage, because a percentage survives a later size change and an absolute silently does not, and he demonstrates the rework [eW2-ghXuYC8 00:07:39]. Kiran: pixels, because "the numbers give us more control" and percentages "often result into odd numbers" [spyPKRE9Ers 00:29:40].
*Rule: Tonic has a mechanism and Kiran has a rounding complaint.* Set the ratio and let the tool compute the absolute. Kiran's own objection is answered by rounding the computed value, which he does anyway.

**3. Whether to optically adjust rounded letters.** Satori: rounded letters appear smaller than straight-sided ones at the same size, so enlarge the O and the C slightly in logos and titles [Dptb5xojbJM 00:00:41]. 4TC: the overshoot is already drawn into the typeface by its designer, "you don't need to adjust them yourself" [YYhaZop92Fg 00:11:26].
*Rule: 4TC is right about well-drawn typefaces and Satori is right about the failure case, and Satori concedes the scope himself,* "if the typeface doesn't already account for this which many do". Check the real render at display size and adjust only when the overshoot is visibly absent. Never in body text, which both agree on.

**4. Widow, orphan and runt.** Kiran: a widow is a single word ending a paragraph on its own line, an orphan is a first line alone at the bottom of a column [spyPKRE9Ers 00:30:40]. 4TC: an orphan is a first line left in a previous column, a widow is a last line pushed to the next, and a runt is the single word at the end of a paragraph [YYhaZop92Fg 00:39:00]. The first two terms are swapped between them and the third exists in only one.
*Rule: name the artifact, never the term.* "A one-word last line" and "a heading alone at the bottom" cannot be misread. The same lesson as the baseline-grid terminology problem recorded in `dsn-grid`: in this corpus a term is less reliable than a description.

**5. Baseline grids.** Kiran rejects them outright and says a bad design will not be fixed by aligning type to lines [spyPKRE9Ers 01:27:59]. Hoonie observes, without endorsing, that systems setting absolute line heights use multiples of four "so that it matches the baseline or works well with their spacing standards" [9w-BwzcuxYM 00:07:36].
*Rule: they do not contradict each other, and neither applies here.* Hoonie records that the multiple-of-four habit is downstream of a baseline grid. A fixed canvas has no second column and no flowed text, so there is nothing for a baseline to align across, and after a non-integer downscale the whole-pixel argument is void too. Kiran's conclusion is right; his reasoning for it is not given.

**6. How many typefaces.** Kiran offers 60 percent one, 30 percent two, 10 percent three [spyPKRE9Ers 00:49:39], then says twenty minutes later that one is enough "in 70% cases" [00:54:47]. The two sets are incompatible and neither is sourced. 4TC is firm: never more than two [YYhaZop92Fg 00:17:39].
*Rule: two is the ceiling, and Kiran's percentages are not data.* They are a verbal hedge formatted as a statistic, which is the most common way a number in this corpus turns out to mean nothing.

**7. Centred text.** Kiran: never centre more than three lines, and centring is right maybe 10 to 15 percent of the time [spyPKRE9Ers 01:37:13]. 4TC centres all three of its practice builds end to end and says so approvingly, "it's all aligned in the center because there's not a lot of type to read" [YYhaZop92Fg 01:52:35].
*Rule: they are describing different canvases, and 4TC's reason is the real rule.* Centring costs the left edge a reader returns to, which only matters once there is enough text to return. A post graphic is a poster, so a centred display lockup is normal; the three-line limit is the constraint that transfers.

**8. Why not to justify.** Kiran's objection is reflow: word spacing changes as the viewport narrows, so the control you wanted is lost [spyPKRE9Ers 01:38:47]. 4TC's objection is rivers of white opening inside the block [YYhaZop92Fg 00:36:53].
*Rule: different scopes, and only one survives here.* A fixed canvas does not reflow, so Kiran's objection does not apply; rivers still open, so 4TC's does. Worth noting because the two sources look like they agree and do not.

## Convention versus derivation

- **Scale ratio names (minor second, major third, perfect fourth): convention,** borrowed from musical intervals with no perceptual claim attached. The ratio does the work; the name is a label on a dropdown.
- **16 pixel web body and a 12 pixel minimum: convention with a partial reason.** They encode a typical viewing distance and device pixel ratio. Real at UI size on a UI screen, and they transfer to a 1080 canvas only after multiplying by the downscale factor.
- **Multiples of four: convention with a partial reason.** Whole-pixel rendering at 2x and 3x avoids half-pixel rounding. Scoped to UI at UI size, and void after a non-integer downscale.
- **Leading at 1.2: convention.** It is InDesign's auto value, presented by 4TC as "a good rule". Nothing wrong with it as a default for display type on a short measure, which is what his builds use it for. It is wrong as a general rule, and that is exactly the error the central mechanism catches.
- **The 50 to 75 character measure: derivation,** from return-sweep difficulty. Single-channel but mechanistic, so it survives.
- **Leading set from characters per line: derivation, and the central synthesis.** No source states it. Hoonie measured the size correlation and attributed it to size; the cause is measure, and the divergence between his 1.21 display average and this skill's 1.10 display value is the proof, since his display rows sit in a wide browser column and a post graphic's display line holds eighteen characters.
- **The tracking mechanism: derivation.** Kiran states it loosely, that more space between letters increases "the contrast between each letter shape" [spyPKRE9Ers 00:20:38], and then apologises for the sentence. The mechanism is right and is what makes the gradient predictable rather than a convention to memorise.
- **The weight-skip rule: derivation,** from the requirement that a level be visibly a level. Both channels give the same diagnosis of the failure.
- **0.5 em average character width: not from any source.** It is a working approximation for a grotesque at mixed case, used in `SKILL.md` to convert a column width into a character count. Check it by setting the real string and counting, which takes less time than arguing about it.
- **Every number in the applied section: construction.** The sources' ratios and floors raised to post-graphic scale.
- **The three leading bands by character count, 1.05 to 1.20 under 25 characters, 1.30 to 1.45 at 25 to 50, 1.40 to 1.55 at 50 to 75: construction.** No source states leading against a count. The nearest sourced bands are by role: 80 to 120 percent for headings and 120 to 160 for body [spyPKRE9Ers 00:28:48]. `SKILL.md` labels them derived at the point of use.
- **The 25 to 50 character band for a short body block: construction, and forced rather than chosen.** On an 860 column the legal size range runs from the 36 floor to the 48 body, which gives 1720 / 36 = 47.8 and 1720 / 48 = 35.8 characters. So every legal body size on this canvas produces 36 to 48 characters per line, below the sourced 50 to 75 band. That band is scoped by its source to continuous body text [spyPKRE9Ers 00:48:43], and a three-line block never accumulates enough return sweeps for it to bind, so the apparent conflict is a scope difference, not a failure.
- **The label level scoped to losable strings: construction, and it resolves the 4x failure recorded in `audit.md`.** At the 4x stress factor from `reference/canvas-assumptions.md` the 38 label renders at 9.5 effective pixels and the 48 body at 12.0. Raising the scale is not available, because the ceiling is fixed by the 18-character display line. `SKILL.md` therefore scopes the levels: nothing that must be read sits below the 60 subhead, which renders at 15 under the stress factor, and the label level carries a handle, a date or a source line only. This is the fix the audit left open.
- **The thumbnail arithmetic in the carousel section: construction, and unverified.** At a thumbnail one third of feed width the effective downscale is 9x, so a 96 display line renders at 10.7 effective pixels, below the floor. The thumbnail width is not in `reference/canvas-assumptions.md` and no source discusses a thumbnail, so `SKILL.md` instructs measuring it rather than trusting the figure.
- **The centre-crop boundary on 4:5: arithmetic on an unverified assumption.** A centre square crop of 1080 x 1350 loses 135 top and bottom, so readable content sits between y = 135 and y = 1215. Crop behaviour is explicitly not assumed in `reference/canvas-assumptions.md`.
- **The CSS half-leading offset: derivation.** A block at line height 1.4 sits ((1.4 - 1.0) / 2) x size below its frame top, about 10px at a 48 size, because the difference between font height and line box is split above and below every line including the first. No source states it; it follows from how the line box is defined, and it is the reason `SKILL.md` tells the reader to align the first baseline rather than the text frame.
- **The 3x downscale factor: construction, and inconsistent across this plugin.** `dsn-grid` says a 1080 canvas displays at "roughly a third" and tests at 25 percent; `dsn-spacing` assumes roughly 400 pixels rendered, which is 2.7x, and tests at 15 percent. This skill takes 3x as the stricter of the two working figures. Measure a real export on a real phone and the three siblings should be reconciled to whatever that gives.

## Caption-level and unreliable figures

Do not quote any figure below as a source's stated value.

- **Hoonie's line-height averages: 120.81, 132.36, 147, 141.76 percent** [9w-BwzcuxYM 00:08:37]. The gradient is real and measured. The two-decimal precision is meaningless and he says so himself, recommending increments of 5 or 10 and "140 percent instead of 141.76 percent". Keep 120 / 130 / 145 / 140 as the shape, and note that "147" is spoken without the word average while the other three carry it.
- **Hoonie's display size list, "36 42 48 60 72 78 and 96"** [00:07:36]. 78 breaks an otherwise regular series and is probably 80 or 84. Take the range, not the list.
- **Hoonie's ratio distribution, 75 / 16 / 4.5 / 4.5** [00:06:48]. Sums to 100, so internally consistent. Kept, and the one figure in the corpus that behaves like data.
- **Kiran's letter-spacing band, "minus 2 to plus 2"** [spyPKRE9Ers 01:28:49]. Units unstated and he is working in pixels across sizes from 12 to 96. At 96px, −2px is about −2 percent; at 16px it is −12.5 percent, which contradicts the gradient he states in the same breath. The band is unusable as given. The sign rule is kept, the absolutes discarded, and Hoonie's percentage ranges used instead because a percentage is unit-safe across sizes.
- **Kiran's "0.1 means 010% and sorry 0.1 actually"** [01:28:49]. Garbled beyond recovery.
- **Kiran's paragraph-spacing arithmetic, "so let's try making it at least 12 is 20 and see what happens"** [01:33:45]. Garbled mid-sentence. The WCAG ratio of 1.5 times line spacing is verifiable externally and is kept; his worked numbers are not.
- **Kiran's heading ladder, "here the jump is two point. Here we could use 20 and then here we could go 30 and then here we could go 38"** [01:13:48]. Inconsistent with the four-to-six rule he states a minute earlier. The rule is kept, the ladder discarded.
- **Kiran's icon-stroke comparison, "approximately 1.5 or maybe 1.3 points in width like the stroke but this particular font is only one pixel"** [02:03:49]. Points and pixels mixed in one sentence. The principle, match the icon stroke to the text stroke, is kept; the numbers are not.
- **Kiran's typeface-count percentages** [00:49:39, 00:54:47]. Invented and self-contradictory. See disagreement 6.
- **4TC's leading rule, "a good rule is to have your leading at 20% more than the size of your font. The default size for your leting is always going to be 20%"** [YYhaZop92Fg 00:30:23]. The second sentence misstates the first: 20 percent more is a ratio of 1.2, not a leading of 20 percent. 1.2 is kept as the InDesign default; the phrasing is not quotable.
- **4TC's "70% of type on the web is using sand serif"** [00:04:33]. Unsourced, unverifiable, and it changes no decision. Discarded.
- **Satori's "challenge yourself to score above 90%" on Kern Type** [Dptb5xojbJM 00:03:46]. An arbitrary practice target, not a standard. Kept as a practice note only.
- **Tonic's arithmetic is the one set that checks out.** 76 x 1.1 = 83.6 [eW2-ghXuYC8 00:06:57] and base 18 at a perfect fourth reaching 75.8 [00:05:05] are both correct. Kept.

### Transcript quality, by source

Worth recording because it determines what can be quoted at all. Satori's captions render kerning as "curing" and "King" and typography as "topography" throughout, so nothing in that video is quotable verbatim and `SKILL.md` cites it for a paraphrased claim only. Kiran's render Roboto as "robboto" and "Voto", Helvetica as "halvatika", and WCAG as "VCAG" and "VCAC"; any typeface name taken from that transcript needs checking before it reaches a brief. Hoonie's and Tonic's are clean, which is unsurprising given both are scripted. 4TC's are clean except for "leting" for leading, consistently.

## Not covered by these sources

- **Any measurement of reading.** This is the gap that matters most, and the census is the reason it is easy to miss. Hoonie counts what 44 teams shipped; nobody tests comprehension, reading speed, or recall against any setting. The most data-shaped source in the set is the one most likely to be mistaken for evidence. On a feed where engagement is measurable, this is the gap to close with Josué's own numbers.
- **Optical margin alignment, hanging punctuation, optical centring.** Absent from all five, and this is where most of the remaining quality in a set text block lives. 4TC gets closest with optical kerning and explicitly defers to the eye.
- **Variable fonts.** No source mentions an axis. Kiran's requirement of five static weights is a pre-variable constraint.
- **OpenType features beyond ligatures and small caps.** Tabular against proportional figures, oldstyle figures, stylistic sets, alternates. Kiran runs into a numeral-alignment problem at [02:08:22], says "the styling and the numbering is something I don't like where this aligns the text in a different manners", and has no vocabulary for it. That is a tabular-figures problem with a one-setting fix.
- **Hinting and rendering differences between engines,** which is what actually decides whether a 12 pixel floor holds.
- **Non-Latin scripts, right-to-left, vertical setting.** Kiran's x-height, aperture and all-caps arguments are Latin-specific and none of them is flagged as such.
- **Print type properly.** Point size against pixel, ink spread, paper. 4TC works in InDesign at point sizes throughout and never addresses the conversion.
- **Accessibility beyond two items.** The paragraph-spacing criterion and the all-caps screen-reader note are the whole of it. Nothing on user text resizing, nothing on the full WCAG text-spacing criterion, nothing on minimum contrast, which is `dsn-contrast`'s territory.
- **What a scale costs when the content changes.** Every source builds a scale once against sample copy. Nobody re-runs it against a headline two words longer, which is the degraded-state problem `dsn-spacing` names and the commonest way a type scale fails on its twentieth use.
- **Licensing**, beyond Kiran's note that Google Fonts are free and a web licence can run to several thousand.

## Stripped from SKILL.md in the legibility pass

The legibility pass removed from `SKILL.md` its opening provenance paragraph, a "Craft and house style" section carrying the corroboration split, and 16 bracketed source IDs. Everything in them is recorded above: the five-source composition and the census's status in **Sources**; the two-or-more-channel list in **Corroboration**; the single-channel items including the four-level taxonomy, x-height and aperture, and the two register claims in the same section; the discarded sub-base steps in the Tonic entry; the unreliable figures in **Caption-level and unreliable figures**; and the absence of any measurement of reading in **Not covered by these sources**. No claim left the body without a home here.

## Changed by the cross-skill numeric reconciliation

The shared floor is two figures, not one: 36px at the nominal 3x downscale and 48px at the 4x stress case, both delivering about 12pt rendered. A floor quoted without its case is incomplete. The framing is established in `reference/canvas-assumptions.md`, which also records that nothing shared fixes margins, columns or gutters.

- **The floor.** Previously gave 36px alone. It now gives 48px at the stress case alongside it, says the two differ only in the viewing condition they survive, and notes that the 48px body step lands on the same value as the stress floor by coincidence rather than by derivation, since it comes from 16 effective pixels at 3x. The scale values 96 / 76 / 60 / 48 / 38, the line boxes, the character counts and the 3x and 4x columns are all unchanged, as is the scoping rule that nothing which must be read goes below the subhead at 60px.
- **The text column.** Previously said the skill that owns margins and columns caps the text column at 860 for this canvas. That is not true of `dsn-grid`, which derives a 72px margin and 936px of usable width and states no 860 figure. The passage now attributes 72 and 936 to that file and the 860 cap to this one, with the reason for the split, and says a piece on another margin recomputes the cap. 860, the 1720 / size character counts and the 86-to-115 display ceiling are unchanged.
- **The poster supersede note.** `dsn-poster` recorded that its computed sizes supersede imported values of 96, 48 and 38 and that this file wins any conflict over type settings. That statement existed only there. The matching half is now in the body here, after the scale table: for a single frame that file's three sizes supersede this ladder, and where a project needs both, this ladder wins and the floor check is re-run against it. No value changed.
