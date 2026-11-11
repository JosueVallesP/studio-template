# Audit: dsn-balance

Independent check of `SKILL.md` against the six transcripts, not against `references/provenance.md`. The provenance file was written by the same agent that wrote the skill, so it is treated here as a claim to test rather than a record to trust. Every verdict below rests on the transcript text.

Sources checked: `balance__TNO44XTiz_w`, `balance__xozcVrEPAHQ`, `balance__Ano6XUcIblc`, `principles__FpwZTl3dCZE`, `principles__HmgzcaH-uv8`, `principles__9EPTM91TBDU`.

**Counts.** 6 mislabelled, 1 unsourced number, 9 derived and unlabelled, 2 unsupported, 13 citations clean. Of 23 inline citations, 6 resolve to the wrong place.

---

## Mislabelled: attributed to a source that does not support the claim as stated

### 1. Near-symmetry, where the source says the opposite

`SKILL.md` wrote: "Near-symmetry is the worst position on the axis: a mirror that is almost a mirror reads as a production error [xozcVrEPAHQ 00:05:56, the only source that states this]."

What the source says at that timestamp is the reverse. Describing a template whose mirror is inexact: "the Symmetry is almost perfect so this gives us a strong feeling of order of structure on this design neither side of the design feels heavier than the other one so we could say that this design is pretty much perfectly balanced" [xozcVrEPAHQ 00:05:56]. The next example is weaker still, with mismatched font weights across the axis, and he calls it "almost perfectly balanced horizontally" [xozcVrEPAHQ 00:06:35].

No passage in any of the six sources ranks near-symmetry below either pole. The parenthesis "the only source that states this" is therefore false twice over: the cited source does not state it, and no other source does either. **This is the most damaging finding in the skill**, because the rule is used as a stopping condition in Mode B ("if near-symmetry, stop, that is the finding") and in the brand-asset call.

Fixed: citation removed, rule kept, inference boundary marked inline with the contrary source reading.

### 2. Register break cited to the wrong Satori video

`SKILL.md` wrote: "a circle in an all-angular field ... [HmgzcaH-uv8 00:04:32 ...]".

`HmgzcaH-uv8` has no timestamp 00:04:32. Its chunk boundaries run 00:03:41, 00:04:35, 00:05:16. The passage actually described sits in the other Satori video: "the style is very angular and very straight ... but the area where the designer wanted you to hover your mouse over is circular ... breaking the repetition can act as a kind of focal point or a tension grabbing location" [FpwZTl3dCZE 00:04:32].

This is exactly the failure mode the channel-name-to-video-id conversion was expected to produce, and these two sources are the pair that share a channel. Note also that `HmgzcaH-uv8`'s nearest analogue is not a circle but a shoe: "very straight angled pointy lines ... contrasted with the smooth curvature of the actual shoe" [HmgzcaH-uv8 00:03:41].

Fixed: citation corrected to `FpwZTl3dCZE 00:04:32`.

### 3. A proximity break counted as a register break

`SKILL.md` wrote: "Register break. One element outside the family ... Four sources in three domains state this independently [... TNO44XTiz_w 00:03:12 ...], making it the best-corroborated mechanism in the set."

At that timestamp Aziev is breaking the proximity rule, not the register: "if you want to create the tension in your design this is one of the techniques to basically break the proximity rule to add a bit more of the spacing" [TNO44XTiz_w 00:03:12]. That is a spatial violation of a stated rule, which the skill already lists separately as "broken proximity". Counting it here inflates the corroboration count that makes this "the best-corroborated mechanism in the set".

Fixed: Aziev's citation moved out of the register-break list with a one-clause note, and the count corrected from four sources to three.

### 4. Broken proximity cited to the statement of the rule, not its break

`SKILL.md` wrote: "Broken proximity. Gaps pushed past the inner-smaller-than-outer rule, so the gap becomes the feature [TNO44XTiz_w 00:00:48]."

00:00:48 is where the inner-outer rule is established and obeyed: "so that we still keep that logic of inner and outer rule so the inner is less than the outer" [TNO44XTiz_w 00:00:48]. The gap becoming the feature is two and a half minutes later, at 00:03:12.

Fixed: timestamp corrected to 00:03:12.

### 5. Saturation cited to a passage about attention, not weight

`SKILL.md` wrote: "**Saturation** buys weight out of proportion to area: 2% of the frame in saturated colour balances 40% in neutral [xozcVrEPAHQ 00:20:11]."

The cited stretch is not about balancing weight. It introduces a second route to asymmetry, explicitly distinguished from the contrast route, whose purpose is to pull the eye: "use a touch like a hint of bright color in some small area of the design that will create attention with the larger area of your design which is of more muted colours" [xozcVrEPAHQ 00:21:00]. The transcript's own wording oscillates between "a tension" and "attention" across these lines, so the one thing the passage cannot be read as is a weight equivalence.

Fixed: claim reworded to the mechanism the source states, with the attention framing noted inline.

### 6. A photographic element reported as a textured one

`SKILL.md` wrote: "**Texture** does the same at a finer grain, and a flat field makes one textured element land [HmgzcaH-uv8 00:04:35]."

The case at that timestamp is a photograph against flatness, and the source files it under style rather than texture: "we see a very minimal bald and flat design that is apart from the photographic element of the Cockroach this is a contrast of style" [HmgzcaH-uv8 00:04:35]. Texture as a weight input is real in this source, but it is the Nike background at [HmgzcaH-uv8 00:03:41] and the marker and balloon cases at [HmgzcaH-uv8 00:05:57].

Fixed: descriptor corrected to photographic, with the texture timestamps kept separately.

---

## Unsourced numbers

### 7. The 2 percent against 40 percent ratio

"2% of the frame in saturated colour balances 40% in neutral" appears nowhere in any of the six transcripts, in any form. No source in the set states a ratio, a threshold or a step scale for weight, which the skill itself asserts two paragraphs later ("No source says how much of one input buys how much of another"). The two figures are the skill's own construction presented inside a citation.

Fixed: marked inline as construction.

---

## Derived: reasonable, not stated by any source, not labelled as derived

### 8. The operator rule, which outruns its evidence by three steps

See the dedicated section below. The skill names its evidence honestly but stops one step short of naming what that evidence does not contain.

### 9. The caption stack that tips a photograph's frame

"A dense block of small type outweighs a larger plain shape, which is why a caption stack can tip a frame a photograph was supposed to hold [xozcVrEPAHQ 00:15:41]." The first half is sourced: contrast "in terms of small versus big light versus dark textured versus plain" [xozcVrEPAHQ 00:15:41], with complexity against simplicity worked through at [xozcVrEPAHQ 00:16:28]. The caption-stack consequence is the skill's, and the source's worked case runs the other way, with an empty rectangle balancing "the abundance of color in the rest of the design" [xozcVrEPAHQ 00:18:43].

Fixed: inference boundary marked inline.

### 10. Deleting rivals, where the source differentiates them

"You make an element heavy by deleting what shares its attribute, not by enlarging it [Ano6XUcIblc 00:10:28]." The source removes no rivals. It gives the rivals different attributes: "there's no other wood tone like it in the room so we deliberately the coffee table is a complete opposite ... it's in a natural wood it's not a dark mahogany" [Ano6XUcIblc 00:10:28]. The mechanism is sole possession of an attribute. Deletion is one route to it and the only one the skill offers, which is why the subtraction test asks for "a deletable rival, which you delete instead".

Not fixed, because correcting it would rewrite the principle and its test rather than mark a boundary. Flagged here as the largest unfixed gap: a reader following the subtraction test will delete where the source re-tuned.

### 11 to 16. Asserted mechanics with no source behind them

- "Symmetry ... survives any substitution, costs nothing to view, says nothing." No source discusses substitution at all.
- "Instability is a cost paid on every viewing."
- "Tension is a budget with one item in it ... Two energy sources read as noise."
- "a carousel's first slide is hand-tuned and the rest come from a stable template."
- "A grounding element ... anchors it and **licenses the instability above**." The source states the two coexisting, not one permitting the other: the capsule "helps create stability and that also grounds the poster but towards the middle of the poster there is movement" [9EPTM91TBDU 00:13:16].
- "tighter letter-spacing re-satisfies the broken relation at a smaller scale **while the placement is kept**." The source moves the element: "we can actually bring the second line closer but maybe we need to adjust the letter spacing" [TNO44XTiz_w 00:09:22], then "because we adjusted the letter spacing ... we can actually apply this rule" [TNO44XTiz_w 00:10:10]. Placement changes as well as tracking.

Fixed: the grounding-element and letter-spacing clauses corrected, since both are citation-level misreadings. The three unattributed assertions are left in place and listed here; they are plausible and marked nowhere, which is the defect.

### 17. Five of the eleven tests have no source

Sourced as observable checks: the falling test [9EPTM91TBDU 00:02:22], the four-fields check [xozcVrEPAHQ 00:01:38], the flip test as the mirroring technique [xozcVrEPAHQ 00:04:37], the dominance-order test from zero-sum dominance [Ano6XUcIblc 00:18:59], the device-and-counterforce test from the column power lines [TNO44XTiz_w 00:06:39], and the device inventory by implication.

Constructed here, with no analogue in any transcript: the blur test, the subtraction test as a procedure, the level-one count as an integer, the grey-box and substitution render, and the delivery-size render. The word "blur" occurs twice in the six transcripts and both are "color blur texture" describing the Nike background. Nothing in the set squints at, blurs, grey-boxes, refills or downscales anything.

Fixed: one line added at the Tests heading separating the sourced instruments from the constructed ones.

---

## Unsupported

### 18. "Which is most failing frames"

The four-fields check "Catches: a frame balanced side to side and tipping top to bottom, which is most failing frames." No source counts failure modes, or counts anything. Nobody in the set measures anything.

Fixed: marked as asserted.

### 19. Corroboration count for optical weight

"three channels independently" for weight being optical rather than geometric is fair on the citations given, but the third leg is thinner than stated. `HmgzcaH-uv8 00:01:27` establishes relational dominance, that an object "sat next to similar objects is going to appear dominant", which supports relativity rather than opticality. Left as is; the claim survives on the other two legs, "every element on a page carries a visual weight and that can be through different scales shapes colors and even textures" [9EPTM91TBDU 00:00:43] and "the distribution of the visual weight of our objects colors textures and space" [xozcVrEPAHQ 00:00:46].

---

## Citations that resolve cleanly

`9EPTM91TBDU 00:00:43`, `xozcVrEPAHQ 00:00:46`, `HmgzcaH-uv8 00:01:27`, `FpwZTl3dCZE 00:14:43`, `Ano6XUcIblc 00:10:28`, `Ano6XUcIblc 00:18:59`, `Ano6XUcIblc 00:13:15`, `9EPTM91TBDU 00:02:22`, `xozcVrEPAHQ 00:01:38`, `xozcVrEPAHQ 00:15:41` (for density only), `TNO44XTiz_w 00:06:39`, `9EPTM91TBDU 00:18:02`, `Ano6XUcIblc 00:03:08`.

---

## How far the operator rule outruns its evidence

The rule: "Tension is tuned per instance and detunes silently when anything is substituted. So if anyone other than you will refill this layout, including you next week and including an agent, target balance. Balance survives substitution."

The whole of its evidence, quoted in full, is a counterfactual Aziev runs on a poster he is analysing: "here again we have typography close to the edges and if we were to make this composition to breathe to add a bit more space that wouldn't really work because now we lose that power and tension that was there before and you kind of don't understand now why is it aligned like this" [TNO44XTiz_w 00:09:22].

Four things that evidence is not.

1. **It is not a restoration of space he removed.** `SKILL.md` says "Aziev restores the space he removed". The composition is somebody else's, arrived at already tight, and he adds space to it hypothetically. Nothing was removed first.
2. **It removes the device, not the content.** Adding the space back is deleting the tension device itself. That the effect dies when you delete the thing producing it is near tautological. The rule needs the opposite case: device kept, content changed.
3. **No source in the set mentions substitution, refilling, templates as content containers, copy length or operators.** Not Aziev, not any of the other five. The step from "this gap is load bearing" to "a four-word headline replaced by an eight-word headline silently detunes it" is unevidenced in the corpus. It is a good inference. It is still an inference.
4. **"Balance survives substitution" has no evidence at all, in either direction.** It is the half of the rule that decides what a crew may be handed, and no source tests, claims or illustrates it.

So the chain is: one sourced observation, then three unsourced steps, then a general gate on templating and delegation. `SKILL.md` discloses step one accurately and labels the generalisation as the skill's inference in `provenance.md`, but in the skill itself the sentence "Its evidence is one demonstration" invites a reader to think the demonstration is of substitution. It is not.

Fixed: inference boundary marked inline at the rule, naming what the demonstration shows and what it does not. The rule itself is untouched, and should be, because it is the right call on the available reasoning. It is a reasoned default, not a finding.

---

## Checked and fine

- The cross-domain verdict on the interiors source holds up. Every claim kept from it is in the transcript, and "A room has no frame, no fixed viewpoint and no reading order" is a fair structural reading, with the lines-of-sight passage at [Ano6XUcIblc 00:17:38] supporting it.
- Every pixel figure in the applied section is declared as derived from `reference/canvas-assumptions.md`, and the platform-crop gap is declared unsourced. Correctly handled.
- The sequence inference at step 6 of Mode A is labelled inline as the skill's own. Correctly handled.
- The generated-work inversion is labelled an inference from the canon. Correctly handled.
- No designer or material name is quoted from `TNO44XTiz_w` or `Ano6XUcIblc`, which the caption garbling makes unrecoverable. Correctly handled.
