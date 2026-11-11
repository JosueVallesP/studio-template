# dsn-spacing: provenance

Where the knowledge in `SKILL.md` came from, what each source uniquely supplied, where they contradict each other and how those contradictions were resolved, which figures are unreliable, and what none of them cover.

The independent audit of this skill, including the arithmetic corrections, the mislabelled claims and the list of derived-but-unlabelled passages, is in `audit.md` beside this file.

## Moved out of SKILL.md by the legibility pass

- **The discipline framing.** The body previously carried the scale split as a split between system work and composition work, which tracked the one interface-side source against the three graphic-design sources. The graphic sources already carry the distinction in their own vocabulary as micro against macro space, so the body now frames it as a scale split and defines both ends. The interface-versus-graphic reading was an artefact of which source supplied which half.
- **Named canon.** The Mode B review order (semantics, then syntax, then understandability, then the rest), the degraded-state anecdote about dinnerware designed to stack with debris inside it, and the reliability argument that one caught inconsistency discredits the parts a viewer cannot check are all canon from outside the four transcripts, unverifiable here, and now appear in the body as mechanism without attribution. The degraded-state test is marked thin because that anecdote was its only stated warrant.
- **The register examples.** The body no longer names the premium-brand or punk-flyer examples as warrants, since both are examples quoted inside sources rather than evidence. The claim that generous space reads premium and tight space reads urgent is now in the confidence line as a convention.
- **The 15 percent thumbnail figure.** Replaced in the body by 270px, which is the 4x stress case in `reference/canvas-assumptions.md`, with 162px noted as stricter than anything the plugin assumes. This resolves the conflict the audit recorded at U4, where 15 percent was stricter than the plugin's own worst case and `dsn-grid` used 25 percent for the same check.
- **The `field` token value.** Changed from 256 to 288 in the body, because 256 is 1.33x on 192 and fails the 1.5x step floor the same file sets. 288 is 192 x 1.5. The audit recorded this contradiction at A4 and left the value alone as a design change; the legibility pass required the arithmetic to close, so the value moved.
- **Corroboration counts.** Every inline note of the form "two sources", "one source states the chain", "flagged inline" and "the one consequence chain more than one source corroborates" is removed from the body. The corroboration record is in the Corroboration section above and the per-claim record is in `audit.md`.
- **The unrecoverable artefact.** The body no longer discusses the on-screen table that exists only as video frames. It is recorded in "The unrecoverable artefact" below, and the consequence, that the register guidance is thinner than what was shown, is carried in the body as a thin marker on the register claims.

## Sources

**02ui: Idea to Product, "Master Spacing in UI Design with One Simple System"**
`1cZBMrdSZUA`, 40m53s, 7.1k views, 2025-12-02. A real-time Figma build, not a lecture. Uniquely supplies: the three-leg split of radius / size / space [00:01:00, 00:07:37]; scoping each token group to its legal properties so illegal values cannot be picked [00:06:31]; two-tier tokens with semantic aliases over primitives [00:17:23, 00:19:02]; single-point propagation [00:11:25]; the named nightmare of "random numbers with so many integers" [00:20:08]; and, unintentionally, the honest demonstration that a token system constrains the vocabulary while the actual gap choices stay by-eye and iterative [00:33:30]. The only UI-side source, and the only one concerned with consistency at scale.

**Satori Graphics, "The ONLY Graphic Design Video On Space You Need To See!"**
`3QJKOWTRuE4`, 15m19s, 32k views, 2024-04-05. The most conceptually dense. Uniquely supplies: the macro / micro distinction with the content-first rule that decides which job you have [00:00:00, 00:00:40]; passive versus active whitespace with the three-state paragraph demo [00:02:08, 00:02:53]; the register rule of thumb [00:01:21]; the viewing-condition (subway poster) argument [00:01:21]; the proximity repair worked in both directions [00:13:05]; the claustrophobic two-line logotype and its small-increment fix [00:13:49]; and the explicit insistence that negative space and whitespace are different things [00:14:27], which contradicts the Canva source head-on.

**Satori Graphics, "Graphic Design Principles Master-Class! (Ep 1 White Space)"**
`FDFD2-poyGw`, 10m14s, 104k views, 2025-07-15. Six staged levels, and the only source that gets past "leave more space". Uniquely supplies: the proximity statement and the seating metaphor [00:01:32]; the squint test and "it should work even before you read a single word" [00:02:19]; whitespace that need not be empty [00:02:19]; micro space deciding what gets noticed first [00:03:07]; the spatial-scale argument for "rhythm, trust, and cohesion" [00:03:51]; the micro / macro job split [00:04:38]; the punk-flyer register example [00:06:13]; dynamic counterbalance with the anchor requirement and the cover test [00:07:48, 00:08:40]; spatial pacing as tempo [00:09:18]; and the beginner panic, "the urge to fill it with something or anything" [00:00:43]. Highest-value source for the composition half.

**Design with Canva, "White Space | Basic Principles of Graphic Design [Ep. 04]"**
`zyHjG6Szt5g`, 26m8s, 29k views, 2023-01-05. Tool-led, most beginner-facing, most worked repairs. Uniquely supplies: the clutter → confusion → unscannable → unmemorable → not-acted-on consequence chain [00:06:19, 00:07:02]; the less-is-more deletion pass as an explicit procedure with a worked edit [00:10:08, 00:10:56]; the fill-the-canvas reflex named as the central beginner error, "I have this canvas I need to fill it up with things... I cannot waste any of that free space" [00:15:20]; the half-committed empty region that "kind of hints at creating that space" [00:05:41]; the Apple pattern of importance made "by creating emptiness around the important elements" [00:08:34]; choosing a background image for the empty region it already has [00:12:28, 00:16:08]; the internal-padding defect and its centre-align fix [00:21:54, 00:23:17]; equal gaps across an icon row [00:24:05]; and the oversized bleeding element [00:24:44]. Also the source of the negative-space-equals-whitespace claim this skill rejects.

**Design canon (consistency and judgement).** Vignelli for the review order (semantics, syntax, understandability, then the rest), for "scale, you have it or you don't", and for designing the degraded state (dinnerware that stacks with the debris inside). The Central Park reliability rule for why one caught inconsistency discredits the rest. Bierut for the resolution whose only defect is that nobody will think you were clever. "Scale, you have it or you don't" is unfalsifiable as a standard and functions in a review to end discussion, so `SKILL.md` keeps only the load-bearing half: because scale is a relationship, it cannot be briefed numerically.

## Corroboration

**Taught by more than one independent channel, so treat as settled enough to act on:**
- Proximity as grouping: both Satori videos, one from the statement side and one from the repair side.
- Isolation as emphasis: Satori and Canva, both via the Apple pattern.
- Clutter as a functional failure rather than an aesthetic one: Satori and Canva.
- The fill-the-canvas reflex as the beginner error: Satori and Canva, independently named.
- A short list of permitted values beating hand-dragged numbers: 02ui from the system side, Satori from the "rhythm, trust, cohesion" side.

**Single-channel, so treat as house style worth using but not as consensus:**
- Macro / micro as the organising vocabulary (Satori only).
- Passive versus active whitespace (Satori only, and internally inconsistent, see below).
- Dynamic counterbalance and the anchor requirement (Satori only).
- Spatial pacing as musical tempo (Satori only).
- Token scoping, aliasing and propagation (02ui only).
- The deletion pass as a formal step (Canva only).

## Where the sources disagree, and the decision rule

**1. Is negative space the same as whitespace?** Canva says yes, the terms "are interchangeable they mean the same thing" [zyHjG6Szt5g 00:01:27]. Satori says no, equally explicitly: "negative space isn't white space they are not the same thing", negative space creates subject, form or meaning when two or more objects interact, as with the FedEx arrow [3QJKOWTRuE4 00:14:27].
*Rule: use Satori's distinction, because it separates two jobs that need different work.* Whitespace is breathing room, tuned by measurement. Negative space is a second figure readable in the gap, found by trial; Satori's own catalogue of it (ambigrams, dual interpretation, hidden meaning) is a set of concept problems, and his honest note is that it "does require a creative mind to think about the design concept in the first place" [00:06:58]. Canva's usage is ordinary speech and harmless in conversation; it will mislead you in a brief.

**2. Must whitespace be empty?** Canva's method treats it as absence [zyHjG6Szt5g 00:12:28, 00:16:08]. Satori says background textures, soft images and subtle colour blocks still function as whitespace if they preserve breathing room, because "the key is perception of separation and clarity, not just the absen[ce] of content" [FDFD2-poyGw 00:02:19].
*Rule: Satori is right about the mechanism, Canva is right about the default.* A quiet texture can qualify, but a texture that is slightly too busy fails silently: it still looks like a decision rather than an error, whereas genuine emptiness cannot fail that way. Use texture-as-whitespace only when you can run the squint test on the real export.

**3. Scale versus rhythm.** 02ui wants every value tokenised, propagated and consistent [1cZBMrdSZUA 00:11:25]. Satori wants intervals varied and expectations broken [FDFD2-poyGw 00:09:18]. Applied naively these are opposed, and a scale applied uniformly is exactly the even-and-dead failure.
*Rule: the scale governs the vocabulary, the composition governs the pattern.* Neither source states this. It is the central synthesis of the skill and the most important thing to take from the pair.

**4. Adapt to the content, or cut the content?** Satori's opening move is to ask what you were given and adapt [3QJKOWTRuE4 00:00:40]. Canva's is to delete whatever is not necessary [zyHjG6Szt5g 00:10:08].
*Rule: it turns on who owns the copy.* On your own posts, cut. On client-supplied or legally fixed text, adapt. The error is attempting a minimal composition on content that cannot be reduced, which produces either an illegible piece or a dishonest mockup.

**5. The two Satori videos contradict each other on micro space.** The longer one treats micro space as serving legibility and aesthetics "without guiding the viewer in terms of structure", that is what *passive* means [3QJKOWTRuE4 00:02:08]. The shorter one has micro space deciding what gets noticed first, by adjusting gaps between a heading, a paragraph and a button [FDFD2-poyGw 00:03:07]. Same author, incompatible claims about whether small gaps direct attention.
*Rule: the shorter video is right, and the passive/active split is about intent rather than size.* Small gaps do direct attention, that is the proximity mechanism. The usable part of passive/active is the question *is this gap there to make reading comfortable, or to make the eye go somewhere*, which is worth asking of every gap and is independent of magnitude.

## Convention versus derivation

- **4 and 8 as base units: convention with a partial reason.** Screens render whole pixels and common densities are 2x and 3x, so multiples of 4 survive scaling without half-pixel rounding. Real, but scoped to UI at UI sizes. It does not transfer to a 1080px post graphic.
- **Powers of two specifically: convention.** 1.5x modular ratios work for the same perceptual reason.
- **A named token ladder: convention,** and useful because a name cannot be mistyped into a near-miss value.
- **Roughly 1.5x to 2x between steps: derivation,** from the requirement that a viewer can see that two gaps differ. This is the part of the scale argument that is load-bearing.
- **The ~2x between-group to within-group ratio: derivation** from the proximity mechanism, expressed in a measurable form. No source states the figure.
- **Every number in the "Applied to a post visual or carousel" section, construction.** The sources' ratios raised to post-graphic scale. No source states them, and the platform behaviour behind the dead bands is mechanism rather than a verified current spec. Crops and chrome change; confirm against a live export before a launch that matters.

## Caption-level and unreliable figures

This topic is dense with numbers and the auto-captions handle them badly. Do not quote any figure below as a source's stated value.

- The spatial scale in [FDFD2-poyGw 00:03:51] renders as "4 8632". Almost certainly 4 / 8 / 16 / 32 with the 16 lost.
- 02ui's token names arrive as "Excel 7 80" for what is plainly XL7 = 80 [1cZBMrdSZUA 00:10:10].
- "four point micro space between your body text lines... eight points between the heading and that body text and then also 32" [FDFD2-poyGw 00:04:38] leaves points and pixels unresolved, and a 4-unit gap *between lines of body text* is not a gap at all, it is leading described loosely. Take the **ratios** from that passage, roughly 1 : 2 : 8 for line, block and group, and discard the absolutes.
- The trial sequence in [1cZBMrdSZUA 00:33:30] runs 16, "too tight", enlarged, "even too tight", landed at 40. All three figures are caption-level. The point of the passage survives regardless: the choice was made by eye.

## The unrecoverable artefact

[FDFD2-poyGw 00:07:04] presents an on-screen table mapping emotional goals to spacing choices and tells the viewer to bookmark it. Its contents are visual only and are not in the transcript. The register guidance in `SKILL.md` is reconstructed from the two examples the video narrates (Apple, and the punk-band flyer using tight chaotic spacing to signal energy and non-conformity) [FDFD2-poyGw 00:06:13], and is therefore thinner than what was actually shown. If the video can be watched again, that frame is the highest-value thing to recover.

## Not covered by these sources

- **Any evidence that more whitespace performs better.** All four argue it from authority (Apple is cited in two) and from critique of weak work. Zero measurement, zero comparison, no case where more space made something worse except by assertion. The register claims are plausible conventions, not findings. On a feed where engagement is measurable, this is the gap most worth closing with the user's own data.
- **Optical spacing.** Kerning is named once in passing [3QJKOWTRuE4 00:13:49] with no method. Optical margin alignment, hanging punctuation and optical centring are absent entirely, and they are where most of the remaining quality in a text block lives.
- **Line height and letter-spacing values.** 02ui files them under the space scale [1cZBMrdSZUA 00:07:37] and never gives a ratio or a method. Nothing on the relationship between measure, size and leading.
- **Baseline grids and vertical rhythm** as a typographic system. Not mentioned by any of the four.
- **Responsive and fluid spacing.** 02ui's tokens are fixed pixel values; it notes in passing that "in the mobile version I need them a little bit tighter" [1cZBMrdSZUA 00:38:57] and supplies no method. How a scale behaves across breakpoints is the obvious next question and is absent.
- **Print.** Bleed, trim, safe area, binding gutters, and the fact that a margin must survive a guillotine. Nothing.
- **Accessibility.** No source mentions minimum touch target size, the WCAG text-spacing criterion, or the reflow behaviour that user-set spacing overrides cause. A real gap for anything interactive.
- **Non-Latin scripts and vertical or RTL settings,** where micro-space conventions differ materially.

## Changed by the cross-skill numeric reconciliation

The shared canvas file fixes sizes and downscale factors and fixes nothing about margins, columns or gutters. The framing is recorded in `reference/canvas-assumptions.md`.

- **The reading margin.** This file hands margins to `dsn-grid` in its handoff section and then sets a 108px reading margin, which read as a competing margin. The bullet now says 108 is a content-exclusion zone measured from the canvas edge and not the grid margin, which that file sets at 72, and that a piece carries both: columns start at 72 and nothing that must be read sits before 108. No value changed and 1080 - (2 x 108) = 864 still closes.
- **Verified and left alone.** The `field` step at 288, recorded above as moved from 256 because 256 is only 1.33x on 192, is not contradicted anywhere in the set: no other skill states a field or macro step, and `dsn-grid` carries no spacing ladder. The 270px thumbnail figure agrees with `dsn-grid`, whose check runs at roughly 25 percent of 1080, which is the same 270px, so the conflict the audit recorded at U4 is now closed in both files and neither needed a further edit.
