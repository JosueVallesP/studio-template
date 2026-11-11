# Audit: dsn-sequence

Independent check of `SKILL.md` against the four transcripts, not against `references/provenance.md`. The provenance file was written by the same agent that wrote the skill, so it is treated here as a claim to test.

Sources checked: `sequence__BAbKX4US7jk`, `sequence__OGgvDBFx3-A`, `sequence__u5p_s63NwwU`, `sequence__JGeIMOpYDsY`.

**Counts.** 1 mislabelled, 2 unsourced numbers, 4 derived and unlabelled, 0 unsupported, 11 of 12 citations resolve to the right source with 3 of those pointing a chunk or two early. No claim attributed to the editorial transcripts turned out to be imported from the storytelling file.

**On the transfer declaration: it is honest.** The skill opens by saying the carousel material does not exist, that the mechanics come from editorial and magazine sequencing and the spine from the storytelling canon, and that the four video sources are all print. Every one of those statements checks out. The canon-derived principles carry their attribution at the point of use (principle 2 to McKee, principle 3 to Sanderson, position 6 to the conflict in the canon, the anti-patterns to rules 25 and pass D). The derivations are labelled: the position map, the one-rest-per-five figure, the pair-not-frame rules, the strip render and the recital test all say so inline. This is the better-provenanced of the three skills audited.

---

## Mislabelled

### 1. Both sources credited with the three-sketch minimum, where only one gives a number

`SKILL.md` wrote: "Both print sources insist on three minimum before the application opens [OGgvDBFx3-A 00:02:10], because sketching catches what you otherwise find with the file half built [u5p_s63NwwU 00:09:07]."

The first citation is exact: "it is usually minimum three thumbnails that i would start with before i actually start doing things in indesign" [OGgvDBFx3-A 00:02:10]. The second source gives no count. It argues for sketching on paper and for speed, and the reason is captions: "sometimes you get to a computer and you're looking at this blank page and you forget to leave room for captions and you just kind of throw them in where you can fit them and they look like an afterthought because they were an afterthought" [u5p_s63NwwU 00:09:07]. Three is one source's working practice, not a corroborated minimum.

Fixed: "both insist on three" corrected to one source supplying the number and the other the reason.

---

## Unsourced numbers

### 2. The tasked reader at frame five

"By frame five the reader is a tasked reader rather than a scrolling one." No number like this appears in any of the four transcripts, and none of them discusses a reader's state changing as a sequence proceeds. The claim is inherited from `dsn-hierarchy`, where the provenance file reports it as single-source and uncorroborated.

Fixed: marked inline as inherited and uncorroborated.

### 3. The 36px floor and the 25 percent strip

Both are declared as deriving from `reference/canvas-assumptions.md` rather than from a source, at the head of the applied section and again at test 9. Correctly handled, no fix needed. Recorded here only so the count of unmarked numbers is not mistaken for the count of constructed ones.

---

## Derived: reasonable, not stated by any source, not labelled as derived

### 4. Density pacing carried across frames, which is the skill's central extrapolation

`SKILL.md` presents the rest position as sourced: "**Rest.** One deliberately sparse frame immediately before the payoff. Sourced to the dense-beside-breathing mechanism [OGgvDBFx3-A 00:16:27]."

The source is pacing a reader's eye across two facing pages taken in at one glance. Read in place, the passage is a tour of a single spread: "you don't want to have too much busy things in one place you want to have some breeding space next to a very dense area so just after this big block of text we have that nice breathing space here and some visual interest and then we move on to a nice pleasing image and only after that we have some additional text" [OGgvDBFx3-A 00:16:27]. Everything he names is simultaneously visible. A carousel's rest frame is seen alone, seconds after the frame before it, with no possibility of seeing both at once.

The word the skill quotes as "breathing" is "breeding" in the transcript, an obvious caption garble, and normalising it is fair. Calling the extrapolation "sourced" is not. The same stretch is also where principle 4's citation sits, with the same gap. The provenance file knows this and says so plainly; `SKILL.md` does not.

Fixed: inference boundary marked inline at both the principle and the position.

### 5. Magnitude variety applied inside one deck

"**The magnitude of the turn varies on purpose.** Uniform intensity cancels itself, and three equal turns running read as boring even though things are technically happening." No source states this. The two design citations attached supply density alternation and colour alternation, which are different claims. The magnitude rule is the canon's, and per the provenance file the canon states it at feed level and explicitly says it has little to say inside a single short piece, which makes the application here an extension of an extension.

Fixed: attribution added inline.

### 6. The affordance judgement

"The affordance is situational; the open loop is not." The source removes an arrow when position supplies the cue: "if they were on a spread i'd probably remove that arrow and they would just automatically get that there's something going on" [BAbKX4US7jk 00:10:07]. He says nothing about open loops being non-negotiable. The ranking of the two is the skill's.

Not fixed. It is a one-clause judgement adjacent to a correctly cited passage and marking it would cost more than it returns. Recorded for completeness.

### 7. The contents page as the publication's *one* exploratory treatment

"the contents page gets the publication's one exploratory treatment because it never repeats [JGeIMOpYDsY 00:11:49]". The source says this section is a good place to get creative because "this section doesn't really repeat after throughout the magazine" [JGeIMOpYDsY 00:11:49]. It does not say it is the only such place. The exclusivity is the skill's, and it matters because the skill uses it to licence exactly one break in a deck.

Fixed: "one" softened to what the source supports, with the exclusivity marked as the skill's.

---

## Citations checked, with three pointing slightly early

- "where's the continuity I need some continuity" [BAbKX4US7jk 00:14:59]. Exact. Clean.
- "I only want enough to get people's interest and then lead them with that arrow over to the next page" [BAbKX4US7jk 00:09:27]. Exact. The second half of the claim, removing the arrow on a spread, is at 00:10:07, not 00:09:27. Fixed by adding the second timestamp.
- The 48pt headline style [BAbKX4US7jk 00:04:04]. Exact, including "if i want to be consistent it's going to stay that 48". Clean, and the only source-supplied number in the skill.
- "every time there is a circle then there is a quote" [JGeIMOpYDsY 00:35:03]. Exact. Clean.
- "make sure your design is driven from that content and that it's not the other way around" [u5p_s63NwwU 00:10:58]. Exact. The golf counter-example is one chunk earlier at 00:10:21 and supports the claim as the skill states it. Clean.
- The spread as the unit with an element crossing the gutter [u5p_s63NwwU 00:01:14]. The spread-as-unit half is there: "we always want to design spreads cohesively so they look like one cohesive unit and not two separate pages". The crossing element is at 00:01:52: "you should have some sort of element that crosses over the middle that brings the two sides together". Fixed by adding the second timestamp.
- Three thumbnails [OGgvDBFx3-A 00:02:10]. Exact. See finding 1 for the companion citation.
- Rhythm by alternation [OGgvDBFx3-A 00:29:03]. Supported: "it is also helping to establish a bit of rhythm where we have these colors alternating" [OGgvDBFx3-A 00:29:03]. The gloss "rather than by making every frame loud" is the skill's framing of a within-spread colour decision. Left as is.
- "three of the four sources say some version of this" for the spread as unit. Conservative and defensible: explicit in `u5p_s63NwwU` and `OGgvDBFx3-A`, present in `JGeIMOpYDsY` at 00:37:30, glancing in `BAbKX4US7jk`. Clean.

---

## Checked and fine

- Nothing attributed to the editorial transcripts turned out to come from `storytelling.md`. The two bodies of material are kept separate throughout, and where the design sources are thin the skill says so rather than borrowing authority ("The editorial version is a complaint rather than a theory").
- Test 11 declares that no source runs a reader test. True of all four.
- The six-position map is declared a derivation at the point of use.
- The hand-tuned against templated split is declared as inherited from `dsn-balance`'s operator rule. See that skill's audit: the rule is sound reasoning resting on one observation that does not cover substitution, and this skill now carries a pointer to that boundary.
