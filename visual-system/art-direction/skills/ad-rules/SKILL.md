---
name: ad-rules
description: Writing a visual direction as rules a maker can be held to, auditing one that reads well and governs nothing, or deciding if you have a rule or a preference.
---

# The direction as rules

This skill turns an approved look into written clauses a maker can comply with or fail, and audits a direction someone else wrote. The single idea underneath it is that a direction is only a direction if an artefact can violate it. A line reading "the work should feel premium and intentional" cannot be violated, so nobody can be held to it, nobody can be shown to have missed it, and the person executing decides everything it appears to govern. A line reading "no type below 48px" can be violated by a ruler. Everything below is the work of converting the first kind of line into the second, naming what you are leaving undecided, and building the two artefacts that let the rules survive a change of maker.

## What this skill is for

- turning an approved look into rules someone else can comply with or fail
- writing a direction an agent or an image model can be held to
- auditing a direction that reads well and governs nothing
- deciding whether what you are holding is a rule or a preference
- finding out which dimensions of a piece you are silently delegating to whoever executes

The output is a numbered clause set, two handoff artefacts, a stated gate with its consequence, and one verdict per test in the table below.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file rests on a controlled comparison, and none of it has been run end to end on live client work. Rules marked **(thin)** rest on a single source and should be treated as one person's house style rather than craft. The clause grammar below, meaning the six forms and the clause count, was constructed from well-formed examples rather than taken from anyone who teaches it, which makes it the most likely thing here to be wrong. One rule also survives whose trigger I could not make testable: principle 2 starts from an artefact you approve of, and approving is taste. What it produces, a written list of named attributes, is fully testable; what you point it at is not.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Direction.** The written set of decisions constraining how a piece or a set gets made: what is in the world, what the values are, where contrast peaks, what is forbidden. Prescriptive, and can be failed.

**Style.** The observable properties of finished work: heavy serif type, desaturated greens, hard side light. Descriptive, and cannot be failed, because it reads what exists rather than instructing what should. A direction may be derived from a style, which is principle 2, but handing someone a style description and calling it a direction is the commonest failure here.

**Art direction against design.** Art direction specifies what a piece must do and judges whether it did. Design makes the page: grid, type sizes, spacing, palette structure. This skill writes the specification and the judgement; the craft belongs to the design skills named at the end.

**Rule.** A clause an artefact can violate, where you can name the violating artefact before you see it.

**Preference.** A clause you cannot trace to anything and cannot imagine violating. "Softer corners feel better": legitimate taste, illegitimate instruction.

**Testable.** A clause is testable when a reader holding the clause and the artefact, with no access to you, returns the same verdict you would. That takes three parts: the quantity or relationship constrained, the threshold or forbidden state, and the instrument that reads it. "Enough contrast" has the first only. "Subject and ground at least 51 points apart on a 0 to 255 greyscale, read in any editor's luma channel" has all three.

**Clause.** One numbered line of a direction, constraining one thing, in one of the six forms below.

**Threshold.** A number or range with its unit and viewing condition both named. A bare number is incomplete: 36px is a floor under one downscale assumption and not another.

**Prohibition.** A clause stating what must not appear or happen. A direction satisfiable only by adding is the easiest kind to fake, since adding is always available and removal is the only move that costs something.

**Gate.** The named moment the direction is applied to an artefact, with a stated consequence for failing. A gate with no consequence is a reminder.

**Dimension.** One axis a direction can govern: palette, type, light, shape language, texture, composition, **crop** (what the frame excludes and where the subject sits in it), motion, material. Dimensions you do not name are not undecided; they are decided by the maker.

**Shape language.** The system governing silhouettes and corner treatments across a set: all rounded rectangles and circles, or all hard angles. The dimension most often left unstated.

**Treatment.** One operation applied identically to every asset so the set reads as one thing: a single grain pass, a single halftone, a single **grade**, meaning a deliberate post-hoc shift of an image's colour and tonal values. A treatment on four of five assets breaks the set.

**Specification.** The written instruction for one piece that does not exist yet. A direction constrains many pieces; a specification describes one. Writing one is a different skill, named at the end.

**The ask.** What the piece has to accomplish, stated before any visual judgement.

**Exploration against refinement.** Exploration generates options under loose constraint; refinement improves one chosen option under tight constraint. A direction written during exploration is too loose to gate with, so write it at the transition, once one option is approved.

**Paired exemplar.** Two images together: the real thing, and the same thing in the intended treatment. It carries the transformation rather than the destination.

**Reference board against moodboard.** A moodboard communicates atmosphere and can afford to be loose. A reference board is annotated to the attribute: each image carries a note naming the property wanted from it and the properties to disregard. The annotation is the rule; the image is evidence of it.

**Depth band.** A layer of a composition at one distance: foreground, midground, background. Contrast is budgeted per band.

## The mechanism: why a direction that cannot be failed governs nothing

Every clause in a direction is a function from an artefact to a verdict. A testable clause returns pass or fail for anyone holding it. An untestable clause returns nothing, so the verdict gets supplied by whoever is in the room, which means the clause did no work and its appearance of doing work is the damage. The direction looks four pages long and governs two lines of it.

The second half of the failure is worse. A clause that cannot be failed cannot be used to correct a maker either, so correction arrives as taste after the fact: this is not quite it, try again. That is the exact condition the direction was written to prevent, reproduced while absorbing the effort of having been written.

The third consequence is the one that makes this worth doing. Unreasoned decisions are invisible while they are being made, because nothing in the room forces a reason out of anybody. A clause set forces one: a decision contradicting a clause means either arguing against the clause or changing the decision, and both leave a record. The characteristic signatures of no clause set are a material included because the category always includes it, with the reason replaced by a rhetorical question; a placement left open because the criterion could not be articulated; and a palette changed mid-build with no criterion stated and no record of what it replaced. The value of a written clause set is not better decisions. It is that unreasoned ones become visible while they are still cheap to change.

## The principles

**1. Every clause must name an artefact that would violate it.** Write the violating artefact beside the clause while you draft it. If you cannot imagine one, the clause is a mood: delete it or rewrite it until a violation is imaginable. *Test:* falsifiability.

**2. Derive the clause set from one artefact you already approve, not from theory.** Take the reference or existing asset you most want the work to resemble and write down what you like about it property by property: the corner radius, the two colours doing the work, the way the light falls. Then convert each entry into a clause. The list answers the question when your eye cannot: where you cannot tell whether an asset is right, you check the sheet instead of deliberating. Clauses derived from theory have nothing behind them and are the first to be argued away. *Test:* derivation.

**3. Every value must have a named source.** Sample each colour and measurement off a named artefact and record where it came from. Two reasons converge: a sampled value ties the palette to something real, and colour perception is unreliable enough that a value chosen by eye is often not the value you think you chose. *Test:* value provenance.

**4. At least one clause must forbid something. (thin)** The strongest prohibitions are flat: never hide the mark, never set type below the stated floor, never use pure black as a shadow. The marker is on the requirement rather than the idea, since treating one prohibition as mandatory is house style. *Test:* prohibition count.

**5. State the gate and its consequence. (thin)** Name the moment the direction gets applied, the question asked, and what happens on a fail. A usable form: before this ships, does it still solve the stated problem, and would you put your name on it; if either answer is no it does not go in. *Test:* rejection.

**6. A reference is only direction once annotated to the attribute, including what to ignore.** One note per image naming the property wanted, one naming what to disregard. An unannotated board hands over atmosphere where the maker needed attributes, and the maker then extracts whichever property they happened to notice. *Test:* blind handoff.

**7. Start from a stated problem, not from a look.** Write the ask first, including the failure it has to avoid. Without it the process is decorating: a colour chosen because you saw it somewhere, a typeface because it looks nice, nothing holding the two together. *Test:* problem presence.

**8. Specify the world separately from the rendering style. (thin)** The world is where the thing takes place and what is in it; the rendering style is the medium depicting it. Merging them skips the step that makes two assets belong to the same place, and the symptom is a direction that dies on a change of medium because every clause in it is about the medium. *Test:* world separation.

**9. Rule where the references come from, on the input side. (thin)** State which categories you will look at and which you will not. The strong move is to leave the category: to make an instant coffee read as genuinely luxurious, look at what that level of luxury looks like elsewhere rather than at coffee. It prevents category mimicry, where researching the category faithfully reproduces its tells and you arrive at beans and a steam curl. *Test:* category tell.

**10. Decide where contrast peaks, then budget the rest against it. (thin)** Highest contrast where the focus is meant to be, an allowance per depth band, and a cap inside each band so a near object does not take more highlight than it needs. This outranks uniformity: a set where every asset matches every other and no subject separates from its ground has failed at what consistency was serving. *Test:* desaturation, value band.

**11. Name the light and the shadow colour as decisions, neither pure. (thin)** Pure black and pure white muddy everything they touch, and they are what you get by default, so a direction that ends up with them without saying so has delegated the decision. *Test:* light and shadow naming.

**12. Give every asset a job no other asset does. (thin)** One sentence per asset naming what it does visually that the others do not. Two matching sentences means one asset too many. This is what stops a nine-slide carousel saying one thing nine times. *Test:* job uniqueness.

**13. Specify every dimension you care about, and list the ones you are delegating.** Walk the dimensions from the terms section and mark each specified or delegated. The delegated list is the useful half: it tells you, before the work comes back, which decisions you handed over. Shape language is the one most often missing. *Test:* dimension coverage.

**14. Build the handoff artefacts.** The clause set alone does not survive a change of maker. The paired exemplar and the annotated board do, and both are specified below. *Test:* blind handoff.

**15. Carry a figure only with its unit and its viewing condition.** A bare threshold is incomplete, because one rendered size corresponds to two working-file numbers under two viewing assumptions. For post graphics this plugin takes canvas sizes and downscale factors from `reference/canvas-assumptions.md` in the design plugin, which fixes both type floors and the stress case rather than letting each file invent its own. *Test:* threshold completeness.

## The six clause forms, and how many clauses

A clause works when it takes one of these shapes. If an entry from your derived list will not go into any of them, that entry was a feeling and belongs in a different document.

- **A measurable threshold.** A camera distance, a height and a tilt. A type floor with its viewing case. A proportion held as a ratio: noticing that a figure's torso equals one head and its legs about three, then holding that ratio across the set. A fixed canvas and a fixed asset count.
- **A required relationship between elements.** Two palettes at opposed temperatures, so the product stays cold and clean while the world around it runs warm. Subject and ground desaturated by different amounts. A ceiling on internal contrast within a depth band.
- **A named source for a value.** Principle 3. The clause is not the value, it is the requirement that the value be traceable.
- **A job assignment.** Every asset in the set must do something visually that the others are not doing. Checkable by writing one sentence per asset.
- **A prohibition.** Principle 4. Flat, with no exception clause.
- **A gate with a stated consequence.** Principle 5.

**Count: roughly four to eight clauses. (thin)** Below about four you have a mood with headings; above about eight nobody gates against it, because gating means reading every clause against every asset. Both ends were inherited from a single instance of six clauses rather than derived, hence the marker. The shape of the constraint is not house style: the lower bound exists because one dimension cannot constrain a piece, the upper because the gate has to stay cheap enough to run.

## How to work

### Mode A: writing a direction

1. **Write the ask**, naming the problem and the failure to avoid. One paragraph. Everything downstream, including the gate, gets checked against it.
2. **Specify the world, then the rendering style, in two passes.** No medium word in the world.
3. **State where references may come from and where they may not.** Name the categories you borrow codes from and the one whose tells you refuse.
4. **Write down what you like about the one artefact you approve of most,** property by property. Keep "two colours, one warm and one cold, nothing in between"; drop "restraint is why it reads as expensive".
5. **Convert each entry into a clause in one of the six forms.** Entries that resist conversion go on a separate page headed preferences, which is honest and claims nothing.
6. **Sample every value, record its source, and name colours after the brand's world rather than the hue: (thin)** not red but brake light, not a deeper red but engine bay, with paddock grey and tarmac alongside. A named colour survives handoff; a hex code gets approximated.
7. **Name the light colour and the shadow colour.** Neither pure.
8. **Locate the contrast peak and budget each depth band against it.**
9. **Add at least one prohibition.**
10. **Mark every dimension specified or delegated,** and put the delegated list where the maker will see it.
11. **Build the paired exemplar and the annotated reference board.**
12. **State the gate and its consequence.**
13. **Run the tests,** falsifiability and format change first, before anyone else sees the file.

### Mode B: auditing a direction

1. Count the clauses against the four to eight range.
2. Name a violating artefact for each. List the clauses where you cannot.
3. Name each value's source. List the untraceable ones.
4. Count the prohibitions.
5. Ask what has been rejected under this direction. Nothing means the gate is undemonstrated.
6. Check dimension coverage and name what is delegated by default rather than by decision.
7. Run the transplant and format-change tests.
8. Report in the order given at the end of this file.

## The handoff artefacts

These carry more of the direction than the prose does, and they are what survives a change of maker.

**The paired exemplar. (thin)** The real thing beside the same thing in the intended treatment. It can be handed to a maker who was not in the room, and they will know what transformation is being asked for, which no adjective conveys. Build the stylised half by subtraction with a stop condition: remove detail and enlarge the controls until a hand could plausibly use them, and stop when the interaction reads. The stop condition matters more than the method, because subtraction without one runs until the thing is unrecognisable.

**The annotated reference board.** Each image carries a note naming the single property wanted from it and a note naming what to disregard: here it is the tiles and that everything is stacked neatly, there it is that the shop owner chooses quirky art, and in both, do not look at the coffee machine. Style references split the same way: this one for the perspective, this one for the line art, this one for the colours. `ad-board` owns sourcing and annotating the board. This skill takes the annotated board as an input and builds nothing on it that `ad-board` has not already written.

## Desaturate the artefact, and what it cannot tell you

Convert to greyscale and read it. Two questions: does the subject separate from the ground, and is peak contrast where the direction said the focus would be. One keystroke, works on any raster output, and it can come back negative, which is more than any other instrument here manages. **(thin)** For a generated image it is the best post-generation gate available, because it runs on the output and needs nothing recorded at the time.

To make it a test rather than a look, the direction has to state a separation floor. There is no published floor to borrow, so whatever number you pick is house style and gets marked as such wherever it is written. Workable form: read the luma channel, which weights the channels 0.2126 red, 0.7152 green, 0.0722 blue on a 0 to 255 scale, and require a stated minimum gap between the subject's mean value and the ground's. The arithmetic is in the worked examples.

Two limits.

**It is diagnostic, not generative.** It says something is wrong, not what to change. A failure sends you back to principle 10, where the decision lives.

**Its anchor does not transfer.** In game work, where the test is routine, clarity has a functional arbiter: can the player find the character, can they tell what is walkable and what does damage. A brand image has no equivalent, so the honest analogue is weaker: does the subject separate, does the product read, does the type survive at feed size. Import the test, not the certainty that came with it.

## Telling a toolkit from a direction

A toolkit is a document of devices you might use: change the scale drastically, put the object somewhere it does not belong, borrow the status of a setting by placing the brand beside something that already has it. You take a reference, go through the toolkit, and apply what makes the result different. That is a generator, and a useful one.

**The diagnostic is one sentence: nothing on a toolkit can be failed.** A device is an option and an option has no violating artefact. Its closest approach to a standard is a count, make one intentional decision and you have moved from a photo to a photo with one idea, which is countable and also trivially passed and self-certified.

So keep a toolkit for generating options during exploration, on a separate page from the direction. Run the diagnostic first on anything handed to you as a direction: if no line has a violating artefact, the audit verdict is toolkit rather than direction with gaps. A toolkit also has no mechanism for retiring a device, so exhausted ones stay in circulation, which is what the category-tell test catches and why one test runs against competitors' work rather than the direction.

## Tests

Each verdict is decidable by a reader holding only this file, the direction and the artefact. The three that need a person or a history are marked.

| Test | Catches | Verdict |
|---|---|---|
| **1. Falsifiability** | Clauses nobody can fail | Write one violating artefact beside each clause. Fail any clause where you cannot, and fail the direction if more than one clause in four fails. |
| **2. Clause count** | A mood, or a set too long to gate with | Count the numbered clauses. Fail below 4, fail above 8. |
| **3. Prohibition count** | A direction satisfiable by adding | Count clauses stating what must not appear or happen. Fail at zero. |
| **4. Derivation** | Clauses invented from theory | Point at the artefact each clause came from. Fail any clause with no artefact behind it. |
| **5. Problem presence** | Decorating | Read the opening. Fail if it does not name a problem and a failure to avoid, and fail if the problem is a look. |
| **6. World separation** | A technique posing as a world | Find the world section. Fail if it contains a medium word (photographic, illustrated, 3D, risograph), or if there is no separate world section. |
| **7. Value provenance** | Guessed values | For each colour and measurement, name the artefact it was sampled from. Fail every value with no named source. |
| **8. Threshold completeness** | A number that means two things | Check every figure for its unit and its viewing condition. Fail any bare number. |
| **9. Light and shadow naming** | A default mistaken for a decision | Find both colours. Fail if either is absent, or is pure black or pure white without the direction saying so deliberately. |
| **10. Desaturation** | A subject that does not separate | Convert to greyscale. Compute the subject's mean luma and the ground's. Fail if the gap is below the direction's stated floor, and fail the direction if it states no floor. Then fail if peak contrast is not on the nominated element. |
| **11. Value band** | Background taking foreground's contrast | In greyscale, compare internal contrast per depth band. Fail if any background element carries more than a foreground one. |
| **12. Job uniqueness** | A set repeating itself | One sentence per asset naming what it does that others do not. Fail on any two that match. |
| **13. Treatment presence** | A broken set | Name the universal treatment, check every asset. Fail on the first asset without it. |
| **14. Dimension coverage** | Silent delegation | List the dimensions from the terms section, mark each specified or delegated. Fail if the direction does not itself carry the delegated list. |
| **15. Transplant** | A generic direction | Strip the brand name and every proper noun. Fail if the remaining clauses would serve a competitor in another category unchanged. |
| **16. Category tell** | Mimicry | List every element in the artefact that would appear in any competitor's work. Fail if no clause excludes any of them. Each listed element is a deletion candidate. |
| **17. Format change** | Clauses that hold in one frame only | Apply the direction to a format it was not written for: square to vertical, still to motion, screen to print. Fail if more than one clause breaks, or if the direction states no behaviour for the second format. |
| **18. Rejection** | An undemonstrated gate | Name one artefact declined under this direction and the clause used to decline it. Fail at zero. Needs a history, so it cannot run on a direction written today. |
| **19. Blind handoff** | Missing clauses | Give the clauses, the exemplar and the board to someone who was not in the room; ask for one asset. Every correction no clause covers is a missing clause. Fail above one. Needs a person. |
| **20. Shape affordance** | Shape language left undecided | Ask an unbriefed person what each element is for. Fail on any element they cannot name. Needs a person. |

## Failure patterns

**The unfalsifiable clause.** Premium, elevated, sculptural, artful, intentional, aesthetic. The type specimen is "inherently sculptural", where *inherently* carries the whole argument.

**Decorating.** A colour chosen because it was good somewhere else, a typeface because it looks nice, no stated problem connecting them.

**Category mimicry.** Researching the category thoroughly and reproducing its tells faithfully.

**Consistency policed over clarity.** Outline weights audited across a set in which no subject separates from its ground.

**Guessed values.** A colour picked by eye and never traced, where the chosen value is often not the perceived one.

**The moodboard used as a reference board.** Atmosphere handed over where attributes were needed, so the maker extracts whichever property they noticed.

**The toolkit substituted for the direction.** A menu of devices handed over as a constraint.

**Borrowed status with nothing owned.** The brand placed beside a stronger one and taking the reading. The tell: nothing survives removing the borrowed object.

**The untested gate.** Declared binding, never once used to reject anything.

**Silent rule change.** A clause altered mid-build with no criterion and no record of what it replaced, so earlier work can no longer be audited.

**Deferral by feel.** A decision left open because the criterion could not be articulated, usually after reasoned options were on the table.

**Rules that only govern the hero asset.** The tell is a note about a detail being probably invisible at full scale but nice that it is there.

**Post-hoc rules reverse-engineered from a campaign you had no part in.** Reading observable properties off an artefact and converting them to a spec is legitimate and is what principle 2 does. Inventing the brand's reasoning, or inferring intent from an ad library that shows what ran and never why, is not.

**A floor quoted without its case.** "Nothing below 36px" read as universal, when 36px and 48px are the same rendered size under two viewing assumptions.

## Applied

### A client brand set, with the arithmetic

**Before.** The direction reads: "Bold, premium automotive energy. Rich reds, industrial greys. Type should feel confident. Captions small and understated. Keep it clean."

**Diagnosis.** Five lines, zero clauses. Falsifiability: name an artefact violating "bold, premium automotive energy". There is none, so test 1 fails on all five. "Rich reds" names no artefact, so test 7 fails on every value. "Captions small" is not a number, let alone one with a case, so test 8 fails. Prohibitions: zero. No stated problem, no world section, no light or shadow colour, no delegated list. Verdict: toolkit, and a short one.

**After, derived.** The approved artefact is one photograph of a car in a pit lane at dusk, written down property by property: one saturated red object against desaturated grey surroundings, light from one low side source, no second accent, subject occupying a little over half the frame height.

Clause 1, palette with sources: brake light `#C8102E` (the tail light), engine bay `#7A0C1E` (the shadow inside the bonnet), paddock grey `#B4B4B4` (the wall), tarmac `#4A4A4A` (the ground). Test 7 passes.

Clause 2, prohibition: no fifth colour, neither light nor shadow pure. Shadow is engine bay, light is paddock grey. Tests 3 and 9 pass.

Clause 3, separation threshold, with the arithmetic. Luma weights the channels 0.2126 red, 0.7152 green, 0.0722 blue on a 0 to 255 scale. Brake light is R200 G16 B46: 0.2126 x 200 = 42.5, plus 0.7152 x 16 = 11.4, plus 0.0722 x 46 = 3.3, giving 57. Tarmac is R74 G74 B74, so 74. The gap is 17 points of 255, under 7 percent, so in greyscale the red subject and the tarmac ground are nearly the same tone and the subject does not separate. Paddock grey resolves to 180, and 180 minus 57 is 123 points, about 48 percent. The clause therefore reads: subject against paddock grey, never against tarmac, floor of 51 points of luma separation, which is 20 percent of the range. **The 51 is house style (thin)**, written into the direction as such so the next person argues with the number instead of guessing. The arithmetic is not house style and anyone can rerun it.

Clause 4, type floor with its case. The canvas is 1080 x 1350 and the downscale assumptions are 3x nominal and 4x stress, per the design plugin's `reference/canvas-assumptions.md`, which puts the two working-file floors at 36px and 48px for the same 12pt rendered result. These assets get republished cropped, which is the stress case, so the floor is 48px and the clause states the case. A 36px caption renders 12pt nominal and 9pt under stress, which is why the bare number was never enough.

Clause 5, ratio across the set: the subject occupies 55 percent of frame height, 0.55 x 1350 = 742px, held within plus or minus 20px, measurable with a ruler on a contact sheet.

Clause 6, job uniqueness: one sentence per asset, no two matching. Clause 7, the gate: desaturate before anything ships and run tests 10 and 11; a fail goes back, a second fail on the same asset cuts it.

Seven clauses, inside the range, each with a violating artefact available, every value traceable, every figure carrying its case.

### Directing an image model

Nothing this skill draws on addresses directing a generative model, so this is construction from the transferable parts, labelled as such.

**Before.** The prompt is the direction's prose pasted in: bold premium automotive energy, rich reds, industrial greys, cinematic. It returns a plausible image every time, a different one every time, and nothing in the direction can reject any of them.

**Diagnosis.** The model is the maker, and test 14 says every unspecified dimension is decided by the maker: here that is shape language, crop, light direction, texture and the exact values, which is most of the piece. The model is art directing and you are selecting.

**After.** Three artefacts this skill already builds, repurposed, then two clauses.

The annotated board is already a prompt structure: this image for the perspective, this one for the line art, this one for the colour, disregard that element. The annotation that turns a board into a direction is the annotation that makes a prompt specific. The paired exemplar is a reference-image pair, carrying the transformation no adjective does. The derived list is the gate on output: approve one generation, write down what you like about it property by property, hold every later generation against that list. It works better here than on commissioned work because approved examples accumulate at almost no cost, so the list sharpens with every batch.

Then two clauses: desaturate every generation before accepting it, since the commonest failure of a generated image is a subject that does not separate from its ground; and specify shape language explicitly, because the model will otherwise supply whatever its training distribution favours, which will be plausible, consistent across your set, and nothing you chose.

### Auditing someone else's direction

**Before.** A six-page deck titled Visual Direction: boards, a palette page of twelve hex codes, and a closing page headed Principles with four lines, intentional, considered, human, premium.

**Diagnosis, run as the tests.** Clause count four, inside the range, but test 1 kills all four, so the effective count is zero. Twelve hex codes, no sources, twelve failures on test 7. Dimension coverage: palette specified; type, light, shape language and treatment absent, so four dimensions delegated and the deck says so nowhere. Prohibitions: zero. Transplant: strip the brand name and the four lines serve any brand in any category. Boards unannotated, so moodboard rather than reference board. Nothing declined, so no demonstrated gate.

**After, as the report.** Verdict: toolkit, not a direction with gaps, because nothing in it can be failed. Then the three conversions recovering the most, in order: annotate the existing boards to the attribute, which costs an afternoon and salvages material already paid for; cut twelve hex codes to four or five with named sources, since twelve unsourced values are worth what none are; add one prohibition, the cheapest clause to write and the hardest to fake compliance with.

## Checklist

- [ ] Ask written, naming the problem and the failure to avoid
- [ ] World stated separately, no medium word in it
- [ ] Reference sourcing ruled, refused category named
- [ ] Clauses derived from one approved artefact, property by property
- [ ] Every clause in one of the six forms, with a violating artefact beside it
- [ ] Clause count between four and eight
- [ ] At least one flat prohibition
- [ ] Every value sampled, source recorded, named for the brand's world
- [ ] Light and shadow colours named, neither pure
- [ ] Contrast peak located, depth bands budgeted
- [ ] Separation floor stated and marked as house style
- [ ] Every figure carries its unit and its viewing condition
- [ ] Dimensions marked specified or delegated, delegated list inside the direction
- [ ] Paired exemplar built, with its stop condition
- [ ] Board annotated to the attribute, including what to ignore
- [ ] Gate stated with its consequence
- [ ] Format-change test run, first clause to break recorded

## The ultimate test

Give the clauses and the paired exemplar to someone who was not in the room, ask for one asset, and then try to reject it using only the written clauses.

If you can reject it and point at the clause, the direction governs. If you have to say it just does not feel right, you wrote a moodboard with headings.

## What an agent can run, and what it cannot

**Runs fully.** Clause and prohibition counts. Threshold completeness, a scan for figures and a check that each has a unit and a case. Dimension coverage against the named list. The transplant test, by stripping proper nouns. Desaturation and the value-band check on raster output, which is a channel conversion and arithmetic. Treatment presence across a set. Job uniqueness, by generating one sentence per asset and comparing. Category-tell listing. World separation, a search for medium words inside the world section.

**Runs partially.** Falsifiability: it can propose a violating artefact per clause and flag the clauses where it cannot, which catches adjective clauses reliably and misses a clause that is technically violable and never actually checked. Derivation: it can record which clauses name no artefact, not whether the named artefact holds the property claimed. Format change: it can recompute every figure for the second canvas, and will miss a clause that breaks for compositional reasons only a person sees.

**Cannot run.** Value provenance, unless the sampling was recorded at the time, because a hex code carries no history. The rejection test, which needs a history nobody wrote down. The shape-affordance read and the blind handoff, both needing an unbriefed person. And whether the problem the direction starts from is the right problem, which is the input everything else rests on.

**Worth delegating deliberately.** Falsifiability screening, because whoever wrote a clause is its worst judge: they can always imagine what they meant, which is exactly what the maker will not have.

## Where this skill should lose

**When the direction does not exist yet.** The sibling skill that builds and audits a reference board owns sourcing images, reducing a pile to a direction, and the anti-sameness moves that keep it off the category's defaults. It produces the approved artefact and the board that principles 2 and 6 consume. If you are still looking at images with no one artefact you would defend, close this file and open that one.

**When the job is one image rather than a set of constraints.** The sibling skill that writes an image specification owns shot lists, acceptance criteria and approval gates for a single picture: what is in frame, what the crop is, what counts as delivered. Handing a photographer a direction when they needed a specification leaves them inventing the piece.

**When work already exists and needs judging.** The sibling skill that gives art-direction notes owns note form, the order findings arrive in, and calling the end of exploration. If you are writing what the work must do you are here; if the work is on the table and you are deciding what to say about it you are there. That skill quotes the clause set when it writes a finding, which is the practical reason every clause has to be quotable.

**When the direction has to become named values an agent or a build step resolves.** Use the design skill that owns tokens: names bound to values, each scale written as a base plus a progression so the next value is derived rather than invented, and a contrast ratio recorded on each text-and-surface pair. That is the machine-readable end of this job. Concretely: this skill decides the shadow is engine bay and nothing drops below 48px under the stress case; that skill decides those are called `color.shadow.base` and `type.caption`, how they resolve, and what the next step up the scale is. Go there the moment the direction stops being read by people.

**When the question is what the identity consists of at all.** Use the design skill that owns identity: which elements exist beyond the mark, the unit each is measured in, and the coherence rules that make a billboard and a feed post read as one brand. That is upstream of everything here. This skill writes failable clauses about decided elements; it does not decide which elements the brand has. Asking whether the brand needs a secondary mark or a texture system means closing this file.

**When a clause needs craft underneath it.** The design plugin owns the mechanics a clause specifies: the skill computing margins, columns and gutters for a canvas; the one setting type sizes, leading, tracking and measure; the one structuring a palette and deciding which colours exist; the one measuring contrast ratios against the accessibility floor and owning the fixes; the one handling a picture's crop and focal point. A clause here saying peak contrast sits on the subject becomes, there, a computed ratio and a chosen value. Name the constraint; do not attempt the craft.

The dependency runs one way. Point at those files; do not expect them to point back.

Sources, corroboration, refused claims, the commercial interests behind each source, the construction history of the clause grammar, and the gaps no source covers are in `references/provenance.md`.

## Writing the output

When auditing, report in this order:

1. Clause count, and the count of clauses with no conceivable violation, each one listed.
2. Prohibition count.
3. Values with no traceable source, listed individually.
4. Figures carrying no unit or no viewing condition, listed.
5. Dimensions left unspecified, and therefore delegated, named rather than counted.
6. The transplant-test result, with the stripped clauses shown.
7. Which clause breaks first under format change.
8. What has been rejected under this direction, or an explicit statement that nothing has.
9. One verdict: a direction, a direction with named gaps, or a toolkit.

Give the arithmetic, not the conclusion. "Subject luma 57, ground luma 74, gap 17 of 255, floor 51, fails" beats "the contrast is weak." Name a default as a default at the point you use it, and mark a number as house style wherever you could not derive it.
