# dsn-contrast: independent audit

Audited 2026-11-06 by an agent that did not write `SKILL.md` or
`references/provenance.md`. Every claim was checked against the primary source,
not against the provenance file. Thresholds were checked against the published
specification text, fetched on 2026-11-06 from the W3C WCAG repository
(`raw.githubusercontent.com/w3c/wcag/main/guidelines/`) and from
`https://www.w3.org/TR/WCAG22/` and `https://www.w3.org/TR/wcag-3.0/`.
Transcripts read in full: `contrast__gdohlUn7fVQ`, `contrast__M80jKhvooyY`.

## Headline: every accessibility threshold in this skill is correct

This is the finding that mattered most and it is clean. All six threshold
figures, both exception lists, the formula, the coefficients, the size
definition, the ratio range and the conformance note verify word for word
against WCAG 2.2. Nothing was changed. The verification, item by item:

| Claim in `SKILL.md` | Spec source | Verdict |
| --- | --- | --- |
| Normal text, AA, 4.5:1 | SC 1.4.3, Level AA | **Correct** |
| Normal text, AAA, 7:1 | SC 1.4.6, Level AAA | **Correct** |
| Large text, AA, 3:1 | SC 1.4.3, Large Text exception | **Correct** |
| Large text, AAA, 4.5:1 | SC 1.4.6, Large Text exception | **Correct** |
| UI component information, 3:1 | SC 1.4.11, Level AA | **Correct** |
| Parts of graphics needed to understand content, 3:1 | SC 1.4.11, Level AA | **Correct** |
| Incidental text has no requirement: inactive component, pure decoration, invisible, part of a picture with significant other visual content | SC 1.4.3 Incidental | **Correct**, and the skill's list matches the spec's four items exactly |
| Logo or brand name has no requirement | SC 1.4.3 Logotypes | **Correct** |
| Large scale is 18pt, or 14pt bold | definition, large scale | **Correct** |
| 14pt and 18pt land near 1.2em and 1.5em, check per font | definition, large scale, note 3 | **Correct**, including the per-font caveat |
| Ratio is `(L1 + 0.05) / (L2 + 0.05)`, L1 the lighter | definition, contrast ratio | **Correct** |
| `L = 0.2126 R + 0.7152 G + 0.0722 B` on linearised sRGB | definition, relative luminance | **Correct** |
| Range 1:1 to 21:1, lighter first | definition, contrast ratio, note 1 | **Correct**, the spec says "commonly written 1:1 to 21:1" |
| Specifying one side of a pair without the other is itself a failure | definition, contrast ratio, note | **Correct**, the spec calls it a failure in both directions |
| Narrow border counts as the letter, wide border acts as a halo and counts as background | definition, contrast ratio, final note | **Correct** |
| SC 1.4.1 Use of Color is the only Level A criterion here | SC 1.4.1 | **Correct** |
| Level AAA not recommended as a general policy for entire sites | Conformance, note | **Correct**, near verbatim |
| WCAG 2.2 is the current Recommendation, 12 December 2024 | masthead of `/TR/WCAG22/` | **Correct** |
| WCAG 2.1 carries identical contrast criteria | 1.4.3 and 1.4.6 are 2.0 criteria, 1.4.11 is a 2.1 criterion, all unchanged in 2.2 | **Correct** |
| WCAG 3.0 Working Draft of 10 September 2026 | masthead of `/TR/wcag-3.0/` | **Correct** |
| The requirement reads as a "contrast measure to be determined" | WCAG 3.0, Text contrast sufficient (minimum) | **Correct**, the draft text is `@@[contrast measure to be determined]` |
| Editor's note: algorithm yet to be determined, draft assumes a size and weight factor, a separate requirement may be needed for red/green CVD | WCAG 3.0, editor's note on text contrast | **Correct** on all three points |
| APCA is named nowhere in the published draft | searched the rendered draft, zero occurrences of "APCA" | **Correct** |

## Mislabelled

Most damaging first. These are attributions a source does not support as stated.

### 1. "Both explainers say it" is true of one explainer

`SKILL.md` principle 3: **"Both explainers say it: the standard covers most
readers at a minimum and you should beat it."**

Only `gdohlUn7fVQ` says it. It says both halves plainly: the minimums are there
"so that most of your visitors are covered by the standard" [gdohlUn7fVQ
00:08:43], and both of its reviewers "agree that where cake is only a minimum
requirement and you should strive to do this better" [gdohlUn7fVQ 00:08:03].

`M80jKhvooyY` says neither half. Its nearest statement is about climbing from AA
to AAA on one pair: "Will be of double A grade but will not pass triple A. Which
means still there are improvements that can be done" [M80jKhvooyY 00:05:36].
That is a remark about a slider, not about what the standard covers or about
designing above it. The video never says the standard covers most readers.

This also sits badly against the skill's own line 10, which says the second
video "supplies no usable figure at all". A source described as supplying
nothing cannot then be cited as half of a consensus.

**Fixed.** The sentence now attributes the claim to the one video that makes it
and records the second video's weaker version.

### 2. "Two specialists" promotes a reviewer the transcript never qualifies

`SKILL.md`: **"This is the one point the video's two specialists disagree on"**
and, under what needs a human, **"a judgement two specialists disagreed about on
camera."**

One of the two is a specialist and the transcript says so: "Eric is a specialist
who worked for the web accessibility initiative" [gdohlUn7fVQ 00:01:41]. The
other is introduced only as someone who sent a tweet, rendered by the captions
as "Mike my foreign" [gdohlUn7fVQ 00:03:20], and the video says nothing about
his credentials. Calling both specialists borrows Eggert's standing for a person
the source does not describe.

**Fixed.** Both sentences now say one specialist and one reviewer.

## Incomplete rather than wrong

### 3. "No AAA criterion exists" for component state is true of 1.4.11 and not of the whole spec

`SKILL.md` table: **"Visual information needed to identify a UI component or its
state | 3:1 | no criterion exists"**, and the bullet: **"Asked for 'AAA for
icons', say the criterion does not exist and give 3:1."**

Correct about 1.4.11, which has no enhanced counterpart. But WCAG 2.2 added SC
2.4.13 Focus Appearance at Level AAA, and it requires "a contrast ratio of at
least 3:1 between the same pixels in the focused and unfocused states". That is
a Level AAA contrast requirement about a component's state. An agent told
flatly that no AAA criterion touches component state would give a wrong answer
about focus indicators.

The figure is 3:1 either way, so no threshold changed. **Fixed** by naming the
one exception in the bullet. The provenance file already recorded 2.4.13; the
skill did not.

## Derived but not labelled as derived

The skill labels its large derivations honestly: the imagery section, the feed
section, the margin check and the 60 percent scrim all carry an explicit mark.
Three smaller ones do not.

1. **"Green contributes about ten times what blue does and three times what red
   does."** Not in either video and not stated by the spec. It is arithmetic on
   the published coefficients, and it is right: 0.7152 / 0.0722 is 9.9, and
   0.7152 / 0.2126 is 3.4. Sound, derived, worth marking only if the skill is
   ever audited for what is quotable from the spec itself.
2. **"W3C naming two limitations of the current model."** The editor's note does
   not describe the current model as deficient. It says the WCAG 3 algorithm is
   undetermined, that this draft assumes a size and weight factor, and that a
   separate requirement may be needed if red/green CVD is not handled. Reading
   those as two gaps in WCAG 2.x is a fair inference and is the skill's
   inference, not the draft's statement.
3. **"A third is that the ratio is polarity blind."** Stated as fact with no
   source. True, and it follows from the formula being symmetric in L1 and L2,
   so it is derived rather than unsupported.

## Unsupported

None found. No figure, threshold or mechanism in `SKILL.md` lacks a basis in
either the specification or a transcript.

## Citations

Three inline citations, all resolving and all supporting what they are attached
to.

- **`gdohlUn7fVQ` 00:02:35.** "three to one for text larger than 24 pixels and
  three to one for bold text larger than 19 pixels", and the point-versus-pixel
  trap, "when you look it up there it says points but you'll have to calculate
  this in pixels". **Resolves, supports.** The conversions are also right:
  18pt at 96dpi is 24px and 14pt is 18.67px.
- **`gdohlUn7fVQ` 00:04:11.** "people won't see the background of the button they
  just see the text". **Resolves, verbatim.**
- **`gdohlUn7fVQ` 00:07:21.** The context exception and the save-and-cancel
  reading: "this last example where I did not change anything about the buttons
  I just arranged them in the row would pass because of context", and in the
  same block, "basically you still always have to conform to the text contrast".
  **Resolves, supports both the exception and the text-never-relaxes claim.**

## The accusation against `M80jKhvooyY`, checked

The provenance file says of that transcript: **"It writes every ratio backwards,
as 1:21, 1:4, 1:8 [00:02:13 to 00:03:23]."**

**The accusation is overstated and does not hold as written.** The transcript
writes ratios in the inverted order through the opening explanation, and it does
assert that the order does not matter. It also writes four ratios in the spec's
own order later in the same video.

Inverted, as charged: "for example 1:21", "if you make this ratio 1:1",
"1:1.2", "it could be 1:4", "1:4.2", "1:8 or 8.2", "the ratio of 1:3"
[M80jKhvooyY 00:02:13 to 00:03:23].

Not inverted, in the same video: "I think the ratio is 1:21 or 21:1"
[00:02:13], which offers both orders in the sentence the charge rests on;
"Of 1.1:1" [00:04:32]; "if you are at a ratio of 5.9:1" [00:06:12]; "here it is
a difference of 10:1" [00:07:15]; "what is the maximum ratio going to be? 21:1
of black and white" [00:06:45].

The defensible version, and the one now in the provenance file: it writes ratios
backwards while explaining them, and it treats the two orders as interchangeable,
saying of 21:1 and 1:21 "Both things are the same thing" [00:06:45]. That is the
real defect, because the spec fixes the order by putting the lighter luminance
first. **Fixed in `references/provenance.md`.** No claim in `SKILL.md` depended
on it.

The related claim in `SKILL.md` line 10, that this video "supplies no usable
figure at all", survives as written if read as thresholds: the video states no
AA or AAA figure anywhere, and says so itself, "it is not necessary that you do
not remember the number" [00:06:12]. It does state ratios as examples, so the
sentence is loose rather than false.

## Counts

| Category | Count |
| --- | --- |
| Sourced, verified against spec or transcript | 32 |
| Mislabelled | 2 |
| Incomplete rather than wrong | 1 |
| Derived, not labelled as derived | 3 |
| Unsupported | 0 |
| Citations that fail to resolve or do not support | 0 |
| Accessibility thresholds wrong | **0** |

Fixes applied: 4 in `SKILL.md`, 1 in `references/provenance.md`.
