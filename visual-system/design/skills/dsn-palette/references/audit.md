# dsn-palette: independent audit

Audited 2026-11-06 by an agent that did not write `SKILL.md` or
`references/provenance.md`. Every claim was checked against the transcripts,
never against the provenance file. Sources consulted: `palette__fdZlIwyZSHo`
(Albers), `palette__R2sCpXbE8R4` (Oatley), `palette__Co75kmQtbaA` (Flux),
`palette__met6BVkv0Ec` (UTF), `palette__Eel2E7uVklE` (Maddy),
`palette__h3vI39h4tuw` (Kennedy), plus `balance__xozcVrEPAHQ` (Canva) for the
one cross-skill citation.

**Citation integrity is high.** All 44 citation instances in `SKILL.md` resolve
to a real timestamp block in the mapped transcript, checked mechanically. Of the
twenty-two checked word by word, nineteen support the claim they carry exactly.
The defects are concentrated in one place: a single sentence that turns a
qualitative observation from a borrowed source into two percentages and cites a
block that does not contain either.

## Mislabelled

Most damaging first.

### 1. Two invented percentages presented as a source-backed finding

`SKILL.md`, the 60/30/10 section: **"The real constraint is weight, not area,
and saturation buys weight far out of proportion to area, with a couple of
percent of saturated colour balancing forty percent of neutral [dsn-balance,
Canva 00:20:11]."**

Three things are wrong and they compound.

- **The percentages are in no source.** The string "percent" and the character
  "%" do not occur anywhere in `balance__xozcVrEPAHQ`. Neither "a couple of
  percent" nor "forty percent" comes from any transcript in this plugin.
- **The cited block is the wrong one and carries nothing about colour.**
  [xozcVrEPAHQ 00:20:11] is a recap of kinds of contrast that make asymmetry:
  "complexity versus Simplicity ... dark versus light colors ... small versus
  large elements." The colour-weight observation is at 00:21:00: "a hint of
  bright color in some small area of the design that will create attention with
  the larger area of your design which is of more muted colors ... so a hint of
  color in a sea of big neutral tones."
- **`dsn-balance`, the skill being cited, says the opposite about quantifying
  it.** Its own line reads: "**Saturation** buys weight out of proportion to
  area: 'a hint of color in a sea of big neutral tones' [xozcVrEPAHQ 00:21:00],
  where the source states the mechanism as attention rather than as weight. Any
  ratio is construction; no source in the set ..." So `dsn-balance` cites the
  right block, flags that the source frames it as attention and not weight, and
  rules out exactly the kind of ratio `dsn-palette` then prints. The numbers were
  manufactured in transit between two skills in the same plugin.

This is the defect class the `dsn-image` audit found: a construction wearing a
citation. It is worse here than a bare guess would be, because the bracket makes
it look checked, and the next reader has no reason to doubt it.

**Fixed.** The sentence now carries the source's own words, the right timestamp,
the note that the source means attention, and the percentages marked as
construction rather than finding.

### 2. The net demonstration is reported as "did not shift" when the source says the halves looked quite different

`SKILL.md` principle 5: **"a red fruit net, halved onto two backgrounds, did not
shift, because the mesh was fine enough that red and background were 'in a sort
of a pointillist way visually mixing' [Albers 00:48:15]."**

The quote is verbatim and the timestamp is right. The setup is right: "we cut it
in half it's the same color red fruit net" [fdZlIwyZSHo 00:47:22]. What the
source reports is not that nothing happened. It is: "they do in fact feel quite a
bit different here it does look like one of them disappeared I agree"
[fdZlIwyZSHo 00:47:22]. One half vanished into its ground. His conclusion the
next block is narrower than the skill's: "so we're not really seeing the color
shift that we had seen in the previous examples" [fdZlIwyZSHo 00:48:15].

So the net did change appearance, dramatically in one case. What it did not do is
shift hue the way the earlier flat swatches did, because optical mixing replaced
the effect. "Did not shift" inverts the observation that makes the principle
useful for feed work, which is that a small element can disappear into its
surround rather than merely drift.

**Fixed.** The principle now states what the source observed.

## Citations pointing at the wrong place

Three, two of them minor. All corrected.

1. **`[dsn-balance, Canva 00:20:11]`** should be 00:21:00. Covered above.
2. **`[Albers 00:39:22]`** carries both halves of principle 4, but the block
   carries only the first: "isn't interesting how this has basically been
   completely washed at any hue it is in fact a blue but when it sits on top of
   this light blue napkin it becomes this neutral flat gray"
   [fdZlIwyZSHo 00:39:22]. The second half, the blue holding on red, is a block
   later: "whereas when it sits on top of the red it retains its blue quality"
   [fdZlIwyZSHo 00:40:27]. **Corrected to a span.**
3. **`[Maddy 00:01:20]`** is cited in the palette-structure section for the
   near-dark and near-light "both tinted toward the brand hue". The block it
   points at establishes the light and dark neutrals and ends mid-sentence on
   "my first tip here is to never use true". The prohibition and the tint are
   the next block: "never use true white or true black especially true black
   because these are a little bit straining on the eye ... it's actually even
   more interesting to add maybe a little bit of color into your blacks and
   whites" [Eel2E7uVklE 00:02:00]. **Corrected to a span.**

## Derived but not labelled as derived

The skill labels its biggest inferences well. Test 10 carries "No source covers
this; it is inferred". The 60/30/10 numbers are called convention in bold. The
generator decision rule is marked as operational. Four smaller items are not
marked.

1. **"Four of the six sources jump from brief to hue by intuition and none tests
   the jump."** The skill's own tally across the corpus, not anyone's claim. It
   survives inspection: Flux reasons from psychology and locality
   [Co75kmQtbaA 00:02:11, 00:03:04], Kennedy from adjectives to "I immediately
   have an idea about what sorts of colors I'm gonna have" [h3vI39h4tuw
   00:21:50], Maddy from category research [Eel2E7uVklE 00:02:39], UTF from
   competitor inspection [met6BVkv0Ec 00:08:13], and none of the four tests
   whether the hue chosen did what the brief asked.
2. **"Make the brand colour richly saturated, because that is what makes it
   hold."** Uncited in the procedure. It follows from Albers' personality
   principle [fdZlIwyZSHo 00:52:08] and is independently asserted by UTF, who
   says "the primary color is a color that should have a lot of saturation"
   [met6BVkv0Ec, perceived-brightness passage]. Sound, and worth a citation.
3. **"Dusty blues" in principle 3.** The claim is that "the colours that shifted
   most in his demonstration were muddy browns and dusty blues, not the bright
   orange" [Albers 00:51:11]. "Muddy brown" is his word: "this brown which is
   sort of a muddy brown without a whole lot of strong identity was able to move
   fairly well" [fdZlIwyZSHo 00:51:11]. "Dusty" is not. He characterises the
   blues as weak rather than dusty: "they're great blues but they're not ... they
   don't really have a lot of oomph to them" [fdZlIwyZSHo 00:52:08]. Worth
   flagging because the provenance file says not to cite a colour name from this
   transcript. Note also that the cited block is self-contradictory about the
   orange, saying both "I was excited to see this orange change so much ... it's
   still doing it" and "this orange which is quite strong isn't moving so
   easily". The skill reports the second, which is the one he draws the lesson
   from, so this is a reasonable reading of an unreliable block rather than a
   misreading.
4. **The five-step ladder for an unusable client brand colour.** The provenance
   says plainly that no source poses the problem. `SKILL.md` presents the ladder
   with one citation at the last rung and no inline mark that the ladder itself
   is assembled here. Only step 5's tool is sourced [h3vI39h4tuw 00:28:26].

## Unsupported

None beyond the two percentages in mislabelled item 1, which are now marked as
construction.

No hex value is asserted anywhere in `SKILL.md`. The skill's own warning about
this is verified: UTF reads codes aloud that arrive as "0005 AFF"
[met6BVkv0Ec 00:10:13] and "0058F" [met6BVkv0Ec 00:11:37], exactly as quoted.

## The claim about the 200-minute source, checked

Two claims were put under audit. **Both hold.**

### It is Material Design 3, read off the documentation

The source runs to 03:19:40, so 200 minutes is right. "Material design 3"
appears nine times and "material design" sixty-one times. He works by opening
the Material Design pages and reading the token values out: "tonal value of 40
and that's why you can see primary 40 over here. Now that primary 40 in this case
for material design has this as it code" [met6BVkv0Ec 01:43:16]; "if I come here
in material design there are also other levels of contrast ... We have the medium
contrast and we have the high contrast as we can see here" [met6BVkv0Ec
02:29:23]; "material design is letting me know that if I'm to have an accessible
color combination, I should use colors that are ... from the tonal palette with
these particular tonal values" [met6BVkv0Ec 02:11:21 region]. The step numbers
in `SKILL.md` are therefore Google's published tokens read aloud, which is what
the skill says they are.

### The accessibility of the tone pairs is never measured

Verified mechanically and by reading every contrast passage. In 200 minutes:

- **"4.5" occurs zero times.** No threshold figure of any kind.
- **"WCAG" occurs zero times.** The standard is never named.
- **No contrast checker, plugin or tool appears.** Zero mentions of a checker,
  of Stark, or of any measuring instrument.
- **The word "ratio" occurs forty times and every one of them is inside
  "saturation".** Not once as a contrast ratio.

Every accessibility verdict in the source is delivered by eye. The clearest
instance: "you can see that we have a very good looking button with an accessible
combination. Right? We don't have any issues with contrast. You can see that this
can easily be read" [met6BVkv0Ec 02:11:21]. And when he flips pairs, the test he
hands the viewer is a feeling: "you should ... have the ability to tell if what
you are getting ... is actually accessible or has a good enough contrast"
[met6BVkv0Ec 02:16:03].

So the skill is right twice over: the ramp numbers are published tokens rather
than anyone's derivation, and the system's justifying claim that its pairs are
accessible by construction is asserted and never measured in this source. The
instruction to run test 8 anyway is the correct response to that.

One small correction to the provenance's wording, not to the skill: it quotes
the source as saying "you can see there's no issue with contrast". The actual
words are "We don't have any issues with contrast. You can see that this can
easily be read." Same meaning, not a verbatim quote.

## Accessibility figures in this skill

One appears, and it is correct. Test 8 and the checklist both state **4.5:1 as
the floor for body text**, sourced to [Eel2E7uVklE 00:03:22], where the source
says "provide a contrast ratio of at least 4.5 to 1. that's a good rule of thumb".
That matches WCAG 2.2 SC 1.4.3 Contrast (Minimum) at Level AA for normal text.
No other threshold is quoted here, and none needed correcting.

## Citations checked word by word and confirmed

| Citation | Carries | Verdict |
| --- | --- | --- |
| Albers 00:05:55 | "your intellect knows that this is one color but your perception of this is that it's two colors" | **Verbatim** |
| Albers 00:06:50 | factual fact against actual fact | **Supports**, phrase introduced at the close of 00:05:55 and defined here |
| Albers 00:22:46 | "place your eye right in the center ... look at both of these sort of out of the corner of your eye" | **Verbatim** |
| Albers 00:24:29 onward | hue as "simply the color name", then the three qualities of contrast | **Supports**, and the skill correctly marks it "onward" |
| Albers 00:32:03 | "my eyes are in a different place than your eyes" | **Supports** |
| Albers 00:35:36 | "in Albers terms he would call this a soft edge hard edge interaction" | **Verbatim** |
| Albers 00:39:22 | blue washed to "neutral flat gray" on light blue | **Supports first half only**, see citation defect 2 |
| Albers 00:43:56 | cut paper, rotating backgrounds, "you can go through things really quickly" | **Supports** |
| Albers 00:48:15 | "in a sort of a pointillist way visually mixing" | **Verbatim**, see mislabelled item 2 |
| Albers 00:51:11 | "the less intense colors the less saturated colors tend to be more easily shifted" | **Supports** |
| Albers 00:52:08 | "colors that have a strong personality ... may be hard to push around" | **Verbatim** |
| Albers 00:12:51 | several backgrounds and foregrounds to rotate through | **Supports** |
| Oatley 00:18:10 | "this idea of color intervals is Central to Albert's approach" | **Supports** |
| Oatley 00:25:44 | "someone will have chosen the exact same three colors that they are wearing" | **Supports** |
| Oatley 00:26:25 | "oh they look good together well tell me how" | **Verbatim** |
| Flux 00:00:44 | the four brief questions, constraints, guidance, action, feeling | **Supports**, all four present |
| Flux 00:03:04 | "just using yellow doesn't make something optimistic", plus locality as a veto | **Verbatim**, and the locality caution is in the same block |
| Flux 00:04:37 | "I like to use the hsb sliders ... hue saturation and brightness" | **Supports** |
| Flux 00:06:13 | candidate rejected against the real wordmark, "it doesn't jive with this word mark" | **Supports** |
| Flux 00:12:31, 00:13:13, 00:23:34 | Adobe Color harmony rules, one hue across a monochromatic set, output rejected on saturation | **Support** |
| Flux 00:27:27, 00:28:57 | skincare interface as noise, guitar retailer as "white black and then red being the only accent color" | **Support** |
| Flux 00:32:55, 00:33:37 | 60/30/10 cited to other videos, then fitted to sites already praised | **Support**, including "a lot of the sites we've looked at today" |
| Flux 00:34:21 | usage rules, "you don't want people making everything yellow ... yellow website" | **Supports** the yellow-website line exactly |
| Maddy 00:02:39 | "make sure not to choose the exact brand color of one of your competitors" | **Verbatim** |
| Maddy 00:03:22 | "a contrast ratio of at least 4.5 to 1", with one neutral required to pass | **Supports** |
| Maddy 00:03:56 | two versions of the brand colour, named "toothpaste am and toothpaste pm" | **Supports** |
| Maddy 00:04:32 | alert colour chosen up front "instead of just defaulting to one later" | **Supports** |
| Maddy 00:05:15 | HSB as the method | **Supports** |
| Maddy 00:06:36 | "about four and a half percent of the world's population" | **Supports** "roughly one viewer in twenty" |
| Kennedy 00:09:03 | the adjective list first | **Supports** |
| Kennedy 00:11:38 | "we need these adjectives to be reflected in three things the color the typography and the imagery" | **Verbatim** |
| Kennedy 00:21:50 | "I always work in the hsb color system" | **Supports** |
| Kennedy 00:28:26 | "my tool is coming up with the closest shade of pink that meets double a guidelines for small text" | **Supports** the nearest-passing-shade claim |
| Kennedy 00:41:36 | "if every gray has just the slightest bit of blue in it you'll have sort of this cool vibe across everything" | **Supports** |
| UTF 00:08:13 | competitor website inspection | **Supports** the category-convention route; the "without copying" half is Maddy's, correctly co-cited |
| UTF 00:10:13, 00:11:37 | "0005 AFF" and "0058F" | **Verbatim**, both manglings exactly as quoted |
| UTF 00:26:30 | "what we have over here looks like a monochromatic combination of colors ... they all have the same U value" | **Supports** the self-named defect |
| UTF 01:06:33 | neutral variant mixed with the tint of the primary | **Supports** |
| UTF 01:14:31 | the tonal-palette plugin | **Supports** |
| UTF 01:43:16 onward | Material's tonal value 40 for the primary role | **Supports** |

## Counts

| Category | Count |
| --- | --- |
| Citation instances in `SKILL.md` | 44 |
| Citation instances resolving to a real block | 44 of 44 |
| Citations checked word by word | 22 |
| Sourced, verified | 19 of those 22 |
| Mislabelled | 2 |
| Citations pointing at the wrong place | 3 |
| Unsourced numbers presented as sourced | 2, both in one sentence |
| Derived, not labelled as derived | 4 |
| Unsupported with no basis anywhere | 0 |
| Hex values asserted from a transcript | 0 |

Fixes applied: 4, all in `SKILL.md`. One sentence rewritten to separate source
from construction, one principle corrected to the observation, two citations
repointed.
