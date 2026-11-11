---
name: dsn-color
description: Use when colours exist and the frame reads wrong, a colour was picked by one slider, or a colour is justified by what it means. Gives each colour a job and a verdict.
---

# Colour

This skill decides and judges what a colour does once it exists: the three numbers that describe it, the job it is doing in this frame, and how it behaves against its neighbours, its background and its delivery size. The single idea underneath it is that the number almost everybody adjusts is the one that matters least. Lightness carries the readability, the ranking and the grouping. Saturation carries most of what people call the feeling. Hue carries identity and learned association and, on its own, carries no contrast at all. So a colour problem is nearly always a lightness problem wearing a hue costume, and the fix is a number, not a different hue.

## What this skill is for

Use it when someone wants to:

- set all three numbers of a colour on purpose instead of picking a hue and stopping
- choose a hue relationship and know what it leaves unsettled
- decide what colour is for in this piece: ranking attention, grouping, depth, weight, state
- work out why a frame reads flat, muddy or noisy when the colours look fine individually
- make a graphic hold up against a surrounding background nobody controls
- test whether a claimed feeling comes from hue or from saturation and lightness
- audit colour on a draft and report findings somebody can act on

The output is three numbers and a stated job per colour, a verdict per test, and the smallest change that fixes each failure.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file rests on a controlled study, so read it as a method that works for people rather than as a result. Rules marked **(thin)** rest on a single source and should be treated as one person's house style you may replace.

Two limits are specific to this topic. Colour meaning is the weakest-evidenced claim in the area and also the most confidently taught, so the section on it below is mostly an argument for not believing it, and it is the one place where this file contradicts the common teaching outright rather than qualifying it. And the feed settings in the applied section, the ground lightness bands and the separation figures, are extrapolation: they were derived from the delivery condition rather than observed, and have not been checked against a real platform render. Test them against one and correct the numbers here rather than treating them as findings.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Hue.** Which colour it is, as a position in degrees on a circle: 0 red, 60 yellow, 120 green, 180 cyan, 240 blue, 300 magenta, back to 360 as red. Hue distance is the shorter way round the circle, so 20 and 340 are 40 degrees apart, not 320.

**Saturation.** How much hue is present as against grey, written here as a percentage, where 0 is neutral grey and 100 is as colourful as the model allows.

**Lightness.** How light or dark the colour is, written here as a percentage, where 0 is black, 100 is white, and 50 is the mid point. This is the number everything load-bearing in this file is measured in.

**Value.** The traditional painting word for perceived lightness. It names the same axis as lightness, and it is defined here only so that a reader arriving from painting instruction can map it across. This file says lightness everywhere, and does not use both words for one axis.

**HSL.** The model this file uses: hue in degrees, saturation and lightness in percent. Every figure below is HSL. Writing a colour out means writing all three, in that order, for example H210 S12 L32.

**HSB, also called HSV.** A different model whose third number is brightness, not lightness. They are not the same quantity: a fully saturated pure hue sits at B100 in HSB and at L50 in HSL. If a picker is in HSB, convert before using any lightness figure here, or the numbers will be wrong by roughly a factor of two at the saturated end. This file does not mix the two.

**Chroma.** The colourfulness axis in perceptually uniform models such as LCH. It is not HSL saturation and the two do not convert by eye. Nothing here computes chroma, and the word appears only to say that a chroma figure from elsewhere cannot be dropped into an HSL slot.

**Tint, shade, tone.** Pigment words. A tint is a hue with white added, a shade is a hue with black added, a tone is a hue with grey added. In HSL those three operations are: raise lightness, lower lightness, lower saturation. Use the HSL description when you need a number and the pigment word only when talking to someone who thinks in paint.

**Greyscale.** The frame with every saturation set to 0 and every lightness untouched. Not a stylistic conversion filter, which may also adjust lightness: set saturation to zero and change nothing else, or the test below measures the wrong thing.

**Relative luminance.** A weighted measure of the light a colour emits, which is what a measured contrast ratio is computed from. It is not HSL lightness and the two disagree, most visibly on yellow, which sits far higher in luminance than its hue neighbours at the same HSL lightness. This file uses lightness and does not compute luminance or ratios; the skill that does is named at the end.

**Additive and subtractive, and the colour spaces they name.** Screen colour is additive: red, green and blue light added together, so more light moves toward white. The standard space a screen and a design file sit in is sRGB, which the HSL numbers here rest on top of. Print colour is subtractive: inks that absorb light, named CMYK, so more ink moves toward dark and neutral. The red, yellow, blue primary set taught with paint, RYB, is a convenience of pigment mixing and is not how either system works.

**Hue relationship.** A named set of positions on the hue circle: complementary is two hues roughly 180 degrees apart, analogous is two to four hues within roughly 30 degrees of each other, triadic is three hues roughly 120 degrees apart, split complementary is one hue plus the two neighbours of its opposite, tetradic or square is four hues roughly 90 degrees apart, monochromatic is one hue at several saturations and lightnesses.

**Dominant, supporting, accent.** The three jobs a colour can hold in a frame. The dominant occupies the largest area and sets the overall read. The supporting occupies the second largest and separates regions inside the dominant. The accent occupies a small area and is the only genuinely saturated colour, present to be found.

**Area share.** The fraction of the frame's pixel area a colour covers. Computed, not estimated: pixel area of the shapes in that colour divided by the total pixel area of the canvas.

**Simultaneous contrast, also called colour relativity.** The effect by which the same colour reads differently depending on what surrounds it. This file asserts that the surround changes the appearance and prescribes a test, and deliberately does not predict the direction of the change, because the direction depends on the specific pair and the available accounts of it disagree.

**Edge vibration.** The shimmer at a boundary between two saturated hues far apart on the circle at similar lightness. Defined operationally in test 5 so it can be found rather than felt.

**Temperature.** Warm covers roughly H0 to H60, the reds, oranges and yellows. Cool covers roughly H120 to H270, the greens, blues and purples. H60 to H120 and H270 to H360 are the ambiguous bands and are better described by their actual numbers than by a temperature word.

**Alpha channel.** The transparency channel of an exported image. A graphic with alpha lets whatever is behind it become part of the composition, which in a feed means the app's background becomes your background.

## The principles

1. **Settle the lightness structure before any hue exists.** A frame whose regions are already distinguishable in greyscale accepts many hue schemes; a frame that is flat in greyscale is not rescued by any of them, because hue difference alone creates no contrast. Build in greyscale, then add hue last. Checked by the greyscale check.

2. **Write all three numbers for every colour, with a reason for each.** A deep burgundy at H350 S60 L22 and a bright cherry at H350 S90 L55 share a hue and behave nothing alike in a layout: one recedes and holds weight, the other grabs. A colour described only by its hue has had one of its three decisions made. Checked by the slider audit.

3. **Treat no colour as having a fixed appearance.** What a viewer sees is produced by the colour and its surround together, so a colour approved against the canvas you designed on has not been approved against the background it ships on. This is the rule that governs anything placed inside a surface you do not control. Checked by the three-ground test.

4. **Choose the hue relationship, then expect it to settle nothing else.** A relationship is a shortlist of hue positions. Whether the set is usable depends entirely on the saturation and lightness given to each member: a saturated red beside a saturated green at the same lightness is unusable, and the same two hues become workable once the red is lightened and desaturated toward pink and the green is darkened and desaturated. Identical relationship, opposite outcome. Checked by the pair-tune check.

5. **Give one colour the dominant role, one the supporting role, and at most one or two the accent role, and set the numbers per role.** Dominant at low saturation, because a saturated dominant leaves no headroom for an accent to be found against. Supporting near the dominant in hue and saturation and separated from it in lightness. Accent the only member above moderate saturation. **(thin)** on the specific split of area, which is a convention rather than a derivation: the taught figures of 60, 30 and 10 percent, or 60, 20, 10 and 10 for four colours, are an ordering dressed up as arithmetic, and the ordering is the part to keep. Checked by role and isolation.

6. **Let lightness carry everything load-bearing, and let hue carry only identity and mood.** Hue reproduction varies with display, colour profile and the platform's dark-mode treatment, and hue distinctions collapse first when a piece is scaled down; lightness relationships survive both. If the first thing read must be found, make it the lightest or the darkest thing in frame rather than the most colourful. Checked by the thumbnail check and the greyscale check.

7. **Never let colour be the only carrier of a state, a group or a rank.** If removing hue removes the message, the message was not in the design, and the reader who cannot distinguish those hues never had it. Add shape, position, label or a lightness difference alongside. Checked by redundant coding.

8. **Treat every fixed hue meaning as unproven, and look for a category convention instead.** Associations between a hue and a feeling are learned, vary across cultures to the point of inverting, and are supported mainly by lists of brands that used the colour. What does operate is category precedent, which is a positioning decision rather than a colour decision. Checked by the category swap.

9. **Keep saturation consistent across the members of a set, and let the accent be the single exception.** A set whose members sit at scattered saturations reads as assembled rather than designed, and the outlier reads as a mistake even when each member is fine alone. Checked by the saturation sweep.

## Tests

In this order when auditing. Every verdict is decidable with a colour picker, an area measurement and this file.

| Test | Catches | Verdict |
|---|---|---|
| **1. Greyscale check** | Hierarchy resting on hue instead of lightness | Set every saturation to 0, change no lightness. Pass only if you can name the first, second and third thing you read, and every text block differs from the shape directly behind it by at least 25 points of lightness. Fail naming each merged pair and its lightness gap |
| **2. Slider audit** | A colour decided by dragging one slider | Write H, S and L for every distinct colour with one clause of reason per number. Fail if any colour has fewer than three numbers. Fail separately on any two colours whose S and L are each within 5 points and which differ only in H, because that pair is one decision wearing two names |
| **3. Three-ground test** | A colour approved only against the canvas it was built on | Export the frame and place it on an L100 ground, an L50 ground and an L7 ground. Fail if the frame edge becomes invisible on any of the three, or if any element inside changes which neighbour it reads as closest to |
| **4. Pair-tune check** | A relationship treated as a finished decision | Set both hues to S100 L50 and look at the boundary. Then tune each to its role band from principle 5 and look again. Fail only if no combination inside the role bands works, which means the relationship itself is wrong for this brief |
| **5. Vibration check** | Saturated near-opposites at similar lightness, which shimmer at the boundary | List every adjacency where the two hues are 120 to 180 degrees apart, both sit above S60, and their lightness differs by fewer than 12 points. Fail on any that touches type. Pass an adjacency away from type only if instability is stated as the intent |
| **6. Category swap** | A meaning claim that is really category precedent | Name three products in the same category as this one. If two or more use the hue, record it as convention and state which the brief wants, compliance or contrast. Fail if a colour's only stated reason is what the hue means and no swap was run |
| **7. Redundant coding** | A state, group or rank carried by hue alone | Set every saturation to 0, keeping lightness. Fail if any state, group or rank becomes unnameable |
| **8. Saturation sweep** | A set whose members sit at scattered intensities | List S for every member. Ignore the accent. Fail if the spread between the highest and lowest of the rest exceeds 25 points. **(thin)** on the 25-point figure, which is a working default |
| **9. Role and isolation** | Two colours doing the same job, or an accent that is not isolated | Compute area share per colour. Fail if two colours each exceed 25 percent of frame area and their lightness differs by fewer than 15 points. Fail separately if more than one element sits above S60, unless one of them repeats three or more times at even intervals, which is the rhythm case |
| **10. Thumbnail check** | Decisions that exist only at full size | Render at one third and at one quarter of the delivered pixel size. Fail if the first thing read changes between the three sizes, or if two groups that were separate merge at either reduction |
| **11. Floor check** | A coloured mark too small to be found at delivery size | Measure the shortest dimension in working-file pixels of every coloured element that carries meaning. Fail below 36px at the nominal reduction. Fail below 48px for anything that must still be findable at the stress reduction |

## How to work

### Mode A: putting colour on a design

1. **Build the frame in greyscale and pass test 1 before any hue exists.** Regions at their final lightnesses, text separated from its panels by at least 25 points, reading order nameable. Do not continue past a failure here, because every later decision rests on this one and none of them can repair it.

2. **Write down what colour has to do in this piece,** choosing from: rank attention, group items that are not adjacent, separate foreground from background, carry weight against a size imbalance, push something forward or back, encode a state, signal a category, set a mood. These are different jobs and several of them conflict. Two colours assigned the same job is the commonest structural fault, and it is what test 9 looks for.

3. **Assign the three roles before choosing any hue:** one dominant, one supporting, one or at most two accents. Order by area share, largest first. Compute the shares on the real canvas rather than estimating them; the arithmetic is in the applied section.

4. **Pick the hue relationship from the job list in step 2,** using the table below, then pick the base hue. The base hue is where brand and context decide and this file cannot.

5. **Set saturation and lightness per role.** Working bands: dominant S8 to S20, supporting S15 to S30, accent S70 to S90. Supporting at least 12 points of lightness from the dominant, so the regions separate, and at least 20 points from the primary type, so it does not compete with it. Run test 4 here rather than at the end, because a relationship that cannot be tuned has to be replaced before anything else is built on it.

6. **Run tests 1, 3 and 5, in that order.** Fix every lightness failure before touching a hue. A hue change does not repair a lightness failure, and a lightness change often repairs an apparent hue failure.

7. **Run tests 10 and 11 at the delivered size,** not on the editor canvas at the zoom level you have been working at.

8. **Run Mode B on your own file,** mechanically, before forming any view about whether the colours are nice.

### Mode B: judging colour on something that exists

Run the tests in this order, before any opinion about taste.

1. **Test 1,** then **test 2**. Everything else is downstream of the first, and any colour with fewer than three stated numbers is already a finding whatever it looks like. Name each merged pair with its lightness gap in points, because that number is the fix.
2. **Test 9,** then **test 5** on every adjacency test 9 turned up, then **test 7** on every state, group and rank in the piece.
3. **Test 3** if the piece ships inside a surface nobody controls, then **test 10**, then **test 11**, all at the delivered pixel size.
4. **Test 8** across the whole set at once, including every slide of a carousel, since an outlier is only visible in company. Then **test 6** on every colour whose stated reason is a meaning.
5. **Report** each pass and each fail, the smallest change that fixes each fail, and which findings are mechanical as against which are judgement. Order by impact: lightness failures first, isolation second, the rest after.

## The lightness ladder

Running one hue through several lightnesses gives a monochromatic set with real separation, and it is how a one-hue design keeps a hierarchy. The arithmetic, which every later section reuses: pick the base hue, hold saturation inside one role band, then step lightness by at least 12 points between any two regions that must read as separate and by at least 25 points between text and the shape directly behind it. Two colours at identical saturation and lightness have no contrast between them however far apart their hues sit on the circle, so a ladder built on hue steps alone is not a ladder.

## Working on a screen rather than in pigment

Much of the available colour teaching is pigment practice. The division is physical rather than stylistic: pigment mixing drags toward dark and neutral and a black pigment carries its own hue bias, while an HSL lightness slider moves lightness without that drift.

| Rule as taught for pigment | Transfers? |
|---|---|
| Lightness matters more than hue | **Yes.** It is the strongest rule in this file and the one with the cleanest test |
| A colour's appearance changes with what sits beside it and the light on it | **Yes.** The load-bearing crossover, and what the whole applied section rests on |
| A mid-lightness ground lets you place elements both lighter and darker in one frame; on a near-white ground you can only go darker, and on a near-black one only lighter | **Yes.** **(thin)**, and it is the reason a feed graphic wants a mid ground |
| A restrained set with a few moments of high intensity beats abundant intense colour | **Yes.** It is the same instruction as accent isolation, arrived at from the other side |
| Darkening a warm colour toward a warm dark beats darkening it toward neutral | **Partly.** On screen, dropping lightness alone reads lifeless, and nudging hue a few degrees warmer while dropping lightness reads better. Same instruction, different cause: in pigment the drift is unavoidable, on screen you are adding it deliberately |
| Do not rely on black to darken, because black is itself a colour and darkening yellow with it produces green | **No.** A property of specific pigments: lowering HSL lightness on yellow does not shift its hue toward green. The surviving part of the caution is the previous row |
| Red, yellow and blue are primaries nothing else can mix; white cools a colour; and every question about tubes, mediums and mixing order | **No.** RYB is true of pigment and false of a screen, which mixes from red, green and blue light, and the claim is usually taught in the same breath as RGB without reconciling the two. For the rest there is simply no HSL operation that corresponds |

Two cautions on the move across. The mixing arithmetic drawn on a colour wheel is pigment arithmetic, while the hue positions on it, the temperature split and the relational rule all survive. And do not carry "muddiness" across: that is what pigment does when complementaries combine physically, whereas on screen the equivalent is a saturation figure you chose, so calling it muddy hides the fact that it is a number you can change.

## Choosing a hue relationship, and what it leaves unsettled

| What the piece needs | Relationship | What it costs, and the number that fixes it |
|---|---|---|
| Maximum separation, an accent that cannot be missed | Complementary | Unusable at full saturation. Use the two hues plus a tint of each, so four colours rather than two, and separate the pair by at least 20 points of lightness. **(thin)** on this caution |
| Separation with less shouting | Split complementary | The hardest to balance, because the two near-opposites also relate to each other. Expect several passes. **(thin)** |
| Three-way separation, charts, infographics | Triadic | Overpowering at equal saturation, and type placed on any of the three gets lost. Give one hue the dominant role and drop the other two to supporting saturation. **(thin)** |
| Calm, unified, soft | Analogous | Almost no hue contrast exists, so every bit of contrast has to come from lightness. The lightness ladder is not optional here, it is the whole structure |
| Cohesion with a real hierarchy | Monochromatic | Nothing stands out by hue, so this is wrong for anything that must grab attention from outside the frame. Separation is entirely the lightness steps |
| Four-colour richness | Tetradic or square | Noise unless one is dominant and the rest are held at supporting saturation with the accent role given to exactly one |

## What colour does in a frame

- **Ranking attention.** Colour assigns a reading order, stacking with size and position rather than replacing them, so a small accent-coloured element and a large dominant-coloured one can both claim first look and produce a tie. Test 10 surfaces the tie.
- **Grouping.** A shared colour groups items that are not next to each other, strongly enough that removing it collapses a grouped set into an undifferentiated list. **(thin)**, and the most reliable job colour does that lightness does not already do better.
- **Entry point.** One isolated element above S60 draws the eye regardless of its size or position. The power is the isolation, so a second one does not double the effect, it halves the first. **(thin)**
- **Depth.** Warm hues appear to advance and cool hues to recede. **(thin)**, and weaker than it is usually taught, because the warm element in a demonstration of it is almost always also the lighter and more saturated one, so temperature is never isolated from the other two numbers. Warm plus light plus saturated advancing is safe to rely on; warm alone is not. Test it by matching lightness and saturation across the pair and seeing whether the effect survives.
- **Weight.** A dark element reads as denser than a light one of the same size, so a small dark shape holds its own against a much larger light one and balances a frame with no size changing. **(thin)**, and it is a lightness effect: the same shape in a light version of the same hue does not do it.
- **Rhythm.** A small saturated accent repeated at even intervals creates a beat and moves the eye through a sequence without repeating any shape. **(thin)**, and the single case where more than one saturated element in a set is correct, which is why test 9 carves it out.
- **Encoding state.** Green for approved, amber for warning, red for problem, grey for unavailable. A learned interface convention, specific to some cultures, which fails outright for a reader who cannot distinguish those hues. Ship the icon or label as well, then run test 7.

**Temperature** is a lever for mood and for the depth effect above, not a rule. It is the most durable associative claim here, because the link between warm hues and sun or fire and between cool hues and water, ice or night points at shared physical experience rather than at a brand category. Even so it describes a tendency that can be pushed, blended or deliberately inverted.

## Colour meaning: convention, not property

Fixed meanings per hue are asserted constantly in colour teaching and almost never with evidence. The pattern to recognise is that the support offered is a list of brands and posters that used the colour, and the same list would support any hue with enough famous users. **Treat every fixed hue meaning as unproven.** A meaning that reverses between two countries, as several of them do, is a convention, which is a useful thing and a different thing.

Two claims here are better supported, and they are what to use instead.

**The feeling comes from saturation and contrast far more than from hue.** Low saturation with soft lightness contrast reads calm, and high saturation with strong lightness contrast reads active and hard. The same hue does both, which is why pastels read gentle and neon reads loud with no appeal to hue meaning at all, and it moves with two sliders. Concretely: to calm a frame without changing a single hue, drop every saturation by 15 to 25 points and close the largest lightness gap by 10. To harden it, do the reverse.

**Where hue meaning does appear to operate, it is category precedent.** A deep desaturated forest green reads as expensive not through anything inherent in that hue, but because luxury branding has used it long enough to train the association with heritage and restraint. That effect is real and learnable, so it can be complied with to belong in a category or broken to stand out in it, and which of those the piece wants is a positioning question that belongs in the brief.

So when someone justifies a colour by what it means, run test 6, report the convention as a convention, then ask the brief which side of it to be on. Do not simply override the claim: the convention is often real, and the person may be right about the move for the wrong reason.

## Failure patterns

Four structural ones, which are approaches rather than mistakes.

**Hue-first design.** Colours chosen before any lightness structure exists, then the missing hierarchy patched with more hue. The signature is a frame that collapses entirely under test 1 while every individual colour is defensible. Fix: rebuild in greyscale, add hue last.

**Harmony as the whole answer.** A relationship selected, the hues left at whatever saturation and lightness the picker offered. Fix: test 4, then set saturation and lightness per role.

**Meaning as justification.** "Blue for trust." Fix: test 6, then state the real reason, which is nearly always one of three things: compliance with a category convention, deliberate contrast against it, or an existing brand colour you do not get to change.

**Colour doing a job that structure should do.** Colour added to rescue a layout that is flat in its arrangement. Fix: fix the arrangement. Colour multiplies an existing hierarchy and cannot create one.

Eight specific ones, each with the number that fixes it.

- **Text and background at the same lightness.** Readable on the monitor it was built on, gone on a phone outdoors. Fix: open the lightness gap to at least 25 points. A hue change does nothing here.
- **Two dominants.** Two colours each above 25 percent of frame area within 15 points of lightness, so neither leads. Fix: demote one by dropping its saturation into the supporting band, or cut its area below 25 percent.
- **Accent inflation.** Three or more elements above S60, so none of them is an accent. Fix: keep one, drop the rest below S30, unless the repetition is the rhythm case and is evenly spaced.
- **A vibrating edge behind type.** Fix, in order of preference: separate the pair by more than 12 points of lightness, drop one below S60, or insert a neutral band between them.
- **Hue-only status coding.** Fix: add shape, icon or label, then run test 7 to confirm the state is still nameable at S0.
- **Mixed intensity across a set.** One member more than 25 points of saturation from the rest. Fix: move the outlier to the family's band rather than moving the family.
- **A transparent background on a feed graphic.** Alpha exported, so the app's background becomes the composition. Fix: ship an opaque ground.
- **Design-mode colour.** Judged at full size, at the working zoom level, on the editor's own neutral canvas. Fix: tests 3, 10 and 11, every time.

## Applied to a post graphic and a carousel

The canvas sizes and the reduction factors come from `reference/canvas-assumptions.md`: a square post graphic is 1080 by 1080, a portrait graphic or carousel slide is 1080 by 1350, the nominal reduction at delivery is 3x and the stress case is 4x. Every number below is computed from those.

### The ground, computed

**Declare your own ground.** Export opaque, never with alpha. The frame edge then becomes the only relational boundary you do not control, which reduces an unknown surround to one known problem you can test with test 3.

**Put the ground in a middle lightness band,** not near-white and not near-black. A near-white graphic dissolves into a light feed and becomes a hard bright rectangle on a dark one; a near-black graphic does the reverse. A mid ground reads as a deliberate graphic against both, and it is the only choice that lets you place elements both lighter and darker than the ground inside one frame. Working bands, both **(thin)** because they are extrapolated from the delivery condition rather than observed: **L25 to L40**, or **L60 to L75**, at S8 to S20.

**A worked dark-ground frame on the 1080 square.** Base hue H210. Ground H210 S12 L32.

- Primary type: at least 55 points of lightness from the ground, so L87 or above. Take H210 S6 L87. Check: 87 minus 32 is 55. **(thin)** on the 55-point figure, which is extrapolation. Verify in greyscale with test 1, not by eye.
- Supporting panel: at least 12 points from the ground, so L44 or above, and at least 20 points below the type, so L67 or below. That gives a window of L44 to L67. Take L52, S18. Check: 52 minus 32 is 20, clear of the 12 minimum; 87 minus 52 is 35, clear of the 20 minimum.
- Secondary type on that panel: at least 25 points from L52, so L27 or below, or L77 or above. Take L88 to match the primary family. Check: 88 minus 52 is 36.
- Accent: H28 S82 L58. Check it against test 5. Hue distance from the ground's H210 is 182 degrees, inside the 120 to 180 band once you account for the shorter way round, which would flag it, but the ground sits at S12, below the S60 threshold, so no vibration. The pair passes. Lightness distance from the ground is 26 points, so the accent also reads as a distinct shape in greyscale, which test 7 requires.

**The same frame on a light ground, for symmetry.** Ground L68. Primary type at 68 minus 55, so L13. Supporting panel at least 12 below 68, so L56 or below, and at least 20 above 13, so L33 or above: window L33 to L56, take L46.

### Area shares, computed

The square canvas is 1080 by 1080, so 1,166,400 square pixels. The portrait canvas is 1080 by 1350, so 1,458,000 square pixels. Applying the conventional ordering from principle 5:

| Role | Share | Square, in px | Portrait, in px |
|---|---|---|---|
| Dominant | 60 percent | 699,840 | 874,800 |
| Supporting | 30 percent | 349,920 | 437,400 |
| Accent | 10 percent | 116,640 | 145,800 |

Now compute what the accent figure actually means, which is where the convention breaks. On the square canvas, 116,640 square pixels as a disc gives a radius of the square root of 116,640 divided by pi, which is the square root of 37,128, so about 193px, a disc about 385px across. A 385px disc on a 1080px canvas is not an accent. It is a third major element, and test 9 would correctly fail it.

So **read the 10 percent as a ceiling and not a target.** The usable accent band is far below it, and it has a floor as well as a ceiling:

- Floor, from test 11: a coloured mark that must be findable at the 4x stress reduction needs 48px in its shortest dimension, since 48 divided by 4 is 12pt. A 48px disc covers about 1,810 square pixels, which is 0.16 percent of the square canvas.
- A sensible working ceiling: 3 percent of the square canvas is 34,992 square pixels, a disc about 211px across, which renders at 70pt at 3x and 53pt at 4x.
- So target the accent between roughly 0.2 and 3 percent of frame area, which is a disc between 48 and 211px on the square. Everything the convention assigns to the accent above that figure should be going to the supporting colour instead.

One exact shape worth keeping in mind, because a bar is the easiest accent to place: a full-width bar 108px tall on the square canvas covers 1080 times 108, which is 116,640 square pixels, exactly 10 percent, and on the portrait canvas a full-width bar 135px tall covers 145,800, also exactly 10 percent. The 108px bar renders 36pt tall at 3x and 27pt at 4x, so it clears the floor by a wide margin in both cases, which is why a thin full-width bar is a safer accent than a disc of the same area.

### Reduction, computed

The square canvas at 3x delivers 360 by 360pt and at 4x delivers 270 by 270pt. The portrait canvas delivers 360 by 450pt and 270 by 338pt.

- A 122px accent disc, about 1 percent of the square, renders at about 41pt at 3x and 30pt at 4x. Both clear the 12pt floor comfortably, which makes 1 percent a good default accent size.
- A 36px element renders at 12pt at 3x and 9pt at 4x, so it clears the nominal case and fails the stress case. That is why test 11 carries two floors rather than one.

### Carousel, computed

A six-slide carousel at 1080 by 1350.

**Hold the hue family constant across all six slides** so the set reads as one object in a feed. Hold the ground at H210 S12 L32 on every slide.

**Separate the slides with lightness rather than hue.** Vary the supporting panel inside the window computed above, L44 to L67: slides at L46, L52, L58, L52, L46, L58. Every value sits in the window, so every slide passes the same separation checks as the single frame, and no two adjacent slides repeat.

**Place the accent only on slides that carry a turn or an action, and place them at an even interval.** Test 9 allows more than one saturated element only when it repeats at even intervals, and on six slides the even options are every second slide, so 1, 3 and 5, or every third, so 1 and 4. Slides 1, 4 and 6 give gaps of three and two, which is not a beat and fails the stricter reading of test 9, so either move the accent onto an even interval or declare the irregularity as intentional. Slides 1, 2 and 6 is not rhythm at all, it is accent inflation.

**Cap each accent at 3 percent of the portrait canvas,** which is 43,740 square pixels, and hold every accent at the same size across the slides that carry one, since an accent that changes size between slides reads as an error rather than a beat.

**Run test 8 across the whole set at once** rather than slide by slide. A saturation outlier is invisible on its own slide and obvious in company, which is the only reason the test exists.

## Checklist

Structure
- [ ] Lightness structure settled before any hue, and test 1 passes with every text block 25 or more points from its backing
- [ ] Every colour has H, S and L written down with a reason for each
- [ ] One dominant, one supporting, at most two accents, with area shares computed rather than estimated
- [ ] No two colours each above 25 percent of area within 15 points of lightness

Behaviour
- [ ] Each job colour is doing is named, and no two colours are assigned the same job
- [ ] At most one element above S60, unless the repetition is evenly spaced rhythm
- [ ] No adjacency of two hues 120 to 180 degrees apart, both above S60, within 12 points of lightness, touching type
- [ ] Nothing load-bearing carried by hue alone, confirmed at S0

Delivery
- [ ] Opaque ground, no alpha, ground lightness inside L25 to L40 or L60 to L75
- [ ] Tests 3, 10 and 11 run at the delivered pixel size, with the 36px nominal-case floor applied to every coloured element carrying meaning and the 48px stress-case floor applied to anything that must be found
- [ ] Any colour justified by a meaning has had test 6 run and is reported as convention
- [ ] Test 8 run across the whole set, not per slide

## The ultimate test

Set the finished piece to S0, change no lightness, and hand it to someone who has not seen it. Ask them to name the first, second and third thing they read, and which items belong together. If they can, colour is doing work the structure supports and hue is free to carry identity and mood. If the piece falls apart, no hue decision in it was ever the problem and none will be the fix. Report the greyscale version beside the colour one, so whoever approves it sees what the structure rests on.

## What an agent can run, and what it cannot

**Can run,** given the file or a render: every test in the table; lightness, saturation and hue distance between any two colours; area share per colour; counts of elements above a saturation threshold; detection of saturated near-opposite adjacencies; alpha channel detection; the shortest dimension of every coloured element against both floors; and a list of every state, group or rank that becomes unnameable at S0.

**Cannot run.** Deciding what colour is for in this piece, which is Mode A step 2 and governs every decision after it. Choosing the base hue, which rests on brand and context rather than on anything in this file. Judging whether a vibrating edge is apt tension or a mistake, because counting an adjacency cannot tell you whether the discomfort is wanted. Deciding whether to comply with a category convention or break it, which is positioning. And setting the brief that resolves a conflict between two jobs colour has been given.

## Where this skill should lose

Three skills here touch colour and they divide cleanly. **If the question is which colours should exist, you are in the wrong file. If the question is whether a specific pair is readable by a measured standard, you are also in the wrong file. If the question is why this frame is not working in colour, or what a colour you already have is doing, stay here.**

**When there are no colours yet, or the set itself is in question.** Use `dsn-palette`. It owns building the set: the role structure with named colours, picking a brand colour or accent with a reason, judging a set somebody else assembled including one a generator produced, and repairing a set that fails at delivery. Palette decides *which* colours a body of work gets and hands you a named set; this file decides what each one *does* in one frame. If you find yourself inventing a colour while reading this file, stop and open that one, because a colour invented inside a single frame will not survive the next twenty.

**When anyone asks whether a pair passes.** Use `dsn-contrast`. It owns measured legibility against the published accessibility specification: the contrast ratio arithmetic, computed from relative luminance rather than from HSL lightness, the separate thresholds for normal text, large text and non-text elements, and the conformance verdict. The split matters because the two measures disagree in a dangerous direction: test 1 here can pass on lightness points while the pair still fails a measured ratio, most often on yellows and saturated colours, because luminance weights green roughly ten times as heavily as blue and HSL lightness weights nothing at all. The lightness figures in this file are a structural tool for hierarchy and grouping and are not a legibility claim, so **never report a greyscale result as a conformance result.**

**When two elements compete for first look and the ranking itself is the problem.** Use `dsn-hierarchy`. It owns the written rank list and the computed type and spacing ladder that produce a rank. Colour multiplies an existing hierarchy rather than creating one, so a failure of test 1 is fixed in that file and not in this one.

**When a small dark element is being used to balance a larger light one.** Use `dsn-balance`. The weight effect is listed here because it is a lightness property, but deciding whether the frame tips and what counterforce it needs is composition, and this file has no account of it.

**When type is going over a photograph.** Use `dsn-image` for judging and rescuing the photograph, then `dsn-contrast` for the pair. A photograph is a surround you did not choose and it varies within the frame rather than around it, so test 3 is not sufficient.

**When these decisions have to be handed to someone else or to an agent.** Use `dsn-tokens`. It owns turning values into named, derivable tokens and the tests that catch a rename. Do not invent a naming scheme here: this file produces numbers and jobs, that file produces the names they ship under.

Nothing in this file covers colour management, profiles or gamut mapping; print reproduction; spot colour; colour in motion or video grading; data visualisation scales, including sequential and diverging ramps; theming and dark-mode token systems; gradients and blend modes as a subject; or colour-blind simulation beyond the greyscale and redundancy tests.

## Writing the output

Name a colour by its role and its three numbers, never by a mood. "The supporting panel sits at L52 against a ground at L32, so it separates by 20 points and survives greyscale" beats "the palette feels muddy": the first is a finding somebody can act on, the second is a reaction. Say which test produced each finding, including the passes, since a pass on test 6 and a missing test 6 look identical in a summary that lists only failures. Give the change as an option with the number attached: not "lighten the type" but "raise the type from L74 to L87, which takes the gap from 42 to 55 points". Label a convention as a convention at the point you use it, especially anything about what a hue means, so the person can override it without feeling they broke a rule, and say when a figure here was extrapolated rather than derived.

Sources, corroboration, disagreements, discarded claims and the full accounting of the colour-meaning evidence are in `references/provenance.md`.
