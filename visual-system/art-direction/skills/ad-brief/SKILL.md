---
name: ad-brief
description: Specifying an image before it exists for a photographer, illustrator or image model, and checking what comes back. Gives a shot list and acceptance criteria.
---

# Specifying an image before it exists

This skill writes the document a maker works from, and the checks you accept or reject the result against. The single idea underneath it: a brief is a specification only when a second person can hold the returned image beside the text and answer yes or no without asking you what you meant. Anything you cannot write that way is a wish, and a wish is accepted by default, because there is nothing in it to fail.

## What this skill is for

Use it when someone wants to:

- write a specification complete enough that what comes back is usable
- brief an image model, where nothing can be clarified while the job runs
- decide what to fix in advance and what is better left open
- check a returned image against what was asked for, and say pass or fail
- audit someone else's brief and name what it leaves unspecified

The output is a brief with its fields stated, a shot list, a written acceptance criterion, and one reshoot trigger.

## Confidence

The rules here are practitioner accounts and reasoning from them, not measured findings. Nothing in this file has been tested against an outcome, so nothing establishes that one specification produces a better image than another. Rules marked **(thin)** rest on a single source and should be treated as one person's house style; a figure is also marked thin when it was inherited rather than derived, and the derivation is shown wherever one exists.

Three limits. Everything behind this file describes makers who are people in a room on a clock, so the section on briefing an image model is argued rather than observed. It covers no moving image beyond the one adjacency test. It covers no licensing or rights clearance, which are legal rather than specification questions.

## Terms, defined before they are used

Terms that several skills share have one meaning each, in `reference/glossary.md` at the plugin root. Where this section differs from that file, that file wins.

**Art direction.** Deciding what the image is of and whether it is right. **Design** is making the page it sits on. This file specifies and judges; it does not lay out.

**The ask.** The one sentence stating what the image has to do for the piece. Everything else is derived from it or is decoration.

**Specification.** A brief whose every line is checkable against a returned image by someone who was not in the conversation.

**Direction.** The standing rules a body of work is held to, outliving any one image. **Style** is the surface appearance those rules produce: a direction can be argued with, a style only recognised.

**Reference board.** A reduced, annotated set of existing images carrying a direction, each present for a named attribute. A **moodboard** is the unreduced, unannotated version: it conveys a feeling and specifies nothing.

**Reference role.** The one attribute a reference is supplied for: this one for light, this one for wardrobe. A reference with no role is an instruction to average.

**Shot list.** The document naming every image the job has to produce, one row per image or category.

**Look.** One complete combination of wardrobe, hair and makeup.

**Apparatus.** Everything making the image that is not the subject: light, camera, lens, background, and for an image model the model itself, the style block and the seed policy.

**Lighting plot.** A diagram made before the shoot showing where each light stands.

**Treatment.** What is done to a picture after it exists: retouching, compositing, the processing choice. **Grade** is the narrower case of a deliberate colour and tonal pass, as distinct from choosing the colours of things in front of the lens.

**Crop.** Cutting the frame down after capture, which changes composition. **Aspect ratio** is the width-to-height proportion of the delivered file: a specification field, not a crop.

**Downscale factor.** How much smaller a frame is seen than built. A 1080px asset in a phone feed column of roughly 360 points is seen at a third of built size, so the factor is 3.

**In-frame check.** A binary question about a property of the image itself, answerable from the file with no access to the set. "The collar is seated" is one. "The photographer was prepared" is not.

**Acceptance criterion.** The in-frame checks, written before the image is made, that a return has to pass.

**Reshoot trigger.** The written condition under which work is made again rather than fixed in post or accepted. A **withhold** is the different act of declining to ship work that satisfies the brief because it fails your own standard: a self-check, not a criterion.

**Approval gate.** A point at which someone other than the maker says go or stop before work continues.

**Exploration** is generating options with the target not yet fixed; **refinement** is converging on one already chosen. The brief says which the maker is in, because the same note means opposite things in each. The **note ladder** is the ordered form a correction then takes: naming the attribute, naming the fix, making the fix yourself.

**Seed.** The number making an image model's output reproducible. **Style reference** is an image supplied to be matched rather than interpreted. **Negative prompt** is what the model is told to exclude.

**Key frame.** The image in a set approved first, that every later image is made consistent with.

**Adjacency.** Whether two images seen next to each other sit together, as distinct from whether each is good alone.

## The specification inventory

Fix the first group before any image is made, because each is a choice the maker will otherwise make for you, differently each time.

**Fix first.**

- **The ask.** One paragraph before any visual choice. It is also the resolution rule for every later gap: when you cannot decide the light, the pose or the wardrobe, the answer is whichever serves the ask.
- **Light: quality, direction, placement.** Hard or soft, from where, how high. Everything else in the frame is modified by it, so leaving it open leaves the image open. Its most complete form is a lighting plot.
- **Framing and shot size,** from the enumerated set: wide, mid, chest-up, close, extreme close, macro.
- **Wardrobe and styling,** per look: top, bottom, accessories, the area of the body in play, plus hair and makeup. **(thin)** Check feasibility against what the subject has worn before, so you know the garment exists.
- **Colour and palette.** Name it, then filter your reference search by it, so references outside the palette never enter the board.

**Fix too.** Pose and action, handed to the subject early enough to practise. Shot order. The reference board, every image roled. Location, scouted in person rather than on a map, two or three options carried, with parking, a changing space, bathrooms, restrictions and opening hours checked on site. **(thin)** Props and set dressing. Lens or focal length. Post-processing intent, declared before capture, because you light differently for an edit you have already decided on.

**Fix if relevant.** Casting criteria. Time of day, which for a photographer constrains the light and for a model is a renderable attribute, so promote it. Camera movement. Call times. Number of looks.

**Six fields a maker at a distance cannot infer.** Each costs a line, and together they are the difference between a brief and a conversation you are not having.

1. **Deliverable count,** how many finished images the job commits to.
2. **Aspect ratio.** For post graphics the two canvases are 1080 x 1080 and 1080 x 1350, per the design plugin's `reference/canvas-assumptions.md`, the shared source for every pixel figure here.
3. **Resolution, file format and colour space.**
4. **Usage: which surface, at what size, under what crop.**
5. **Budget, as a written constraint.**
6. **The acceptance criterion.** Without it, every return is accepted by default.

## A spec line names the mechanism, not the feeling

Nearly every unobservable standard has a checkable mechanism sitting next to it, and the mechanism is what belongs in the brief. *A sense of closed intimacy* is untestable; *put up a black background* is the move that produces it, and it is testable. *Dramatic lighting* is untestable; *hard light from camera left, low* is testable. *A better photograph* is untestable; *a foreground, a subject and a background* is testable.

So the working definition: **a spec line is testable when a second person can hold the return beside it and answer yes or no without asking you what you meant.**

Phrases of this shape circulate as standards and are not tests: as close to the soul as possible; angles that are not typically shot at, since typical to whom; the model representing the brand, which needs a judgment rather than an observation; posing appropriately, which is only a test if the pose was specified. Each is rescued by asking what visible thing would make you say it. That answer is the spec line.

## The principles

Each names the test that checks it. The tests are in the table below.

**1. Fix the apparatus so the content can vary.** Keep light, camera, lens and background identical across a body of work, and the only thing changing between images is what you are saying. Planning and responsiveness are not in tension: settling the apparatus in advance buys room to respond on the day, because a maker who knows where the lights are can explore, and one who does not is still solving the setup. Fixing the apparatus early is also compatible with judging the result late, which is the resolution of the two positions you will meet on where the look belongs in the order: one treats the look as the spine to settle first, the other withholds it until after the ask and the message. The first is about the apparatus, the second about the result. *Test:* fixed versus open.

**2. Strip the brief to what is necessary.** If an element is necessary it is in there, and if it is not, it is not. The harder version: delete the line and ask whether the specified image is still the same image. If it is, the line was not doing work. *Test:* the necessity pass.

**3. Cast the maker to the brief before you instruct them.** Match the maker to the reference board: a soft board does not go to a maker whose work is hard and high contrast. This is the only control exercised before any instruction is given, and the cheapest, because a maker whose work already contains the quality you want needs less brief than one who has to be argued into it. For an image model the analogue is the model and the style reference, both chosen before the prompt. *Test:* the maker-match test.

**4. Ship the reference board to everyone, not just the maker.** Attach it to every outbound message: the maker, hair and makeup, the subject's representation, the call sheet. Otherwise the image exists only in your head and everyone else is working from a different one. People should also have a clear view of the end result before they see the end result. *Test:* the restatement test.

**5. Specify conduct where harm is possible, as a condition of the image.** If a person is in the frame, the brief says how they are treated: how many at once, what the pace is, who speaks. Where subjects are minors, privacy and a changing space are requirements rather than courtesies. **(thin)** *Test:* the conduct line.

**6. Reject on the two grounds visible in the frame.** First, the composition is one already made before, recognised because you have seen the shape too many times. Second, performance is visible, where the pass condition is that nobody looks like they are performing. Both are checkable by a second person holding the frame, which is why both survive an absent maker. *Test:* the two-ground selection pass.

**7. Bound every description.** Ten to twenty words per shot. **(thin)** A long description stops being a specification and becomes a mood, because the reader cannot tell which clause is binding. If the line will not fit, you are specifying two images.

**8. Give every reference a role.** Name the one attribute each is supplying. An unroled pile is an instruction to average, survivable with a person who treats a reference as an indication and ruinous with a model that treats it as a target. *Test:* reference roles.

**9. Write the acceptance criterion before the image exists.** In-frame checks, each binary, each a property of the file. Written afterwards it is a rationalisation of what arrived. *Test:* the acceptance criterion exists.

## How to work

### Mode A: writing a brief

1. **Write the ask in one paragraph,** before opening any reference.
2. **Fill the fix-first group,** then the second group where relevant, then all six distance fields. A field left open is written down as open, with the reason.
3. **Build or receive the reference board** and check every image has a role. Building one belongs to the sibling skill named at the end of this file.
4. **Cast the maker,** or choose the model and style reference, against the board.
5. **Write the shot list,** as a set or as a sequence, per the next section.
6. **Write the acceptance criterion:** one binary in-frame check per fixed element visible in the finished image.
7. **Write the reshoot trigger,** one line.
8. **Run the necessity pass, the noun sweep, then the restatement test.**
9. **Ship it to every participant** and require confirmation of receipt, twenty-four to forty-eight hours ahead, so a non-reply can still be replaced. **(thin)**

### Mode B: auditing a brief, or a return

Stop at the first failure when auditing a brief, because a missing ask invalidates everything specified under it. Do not stop when auditing a return: run every check and report all of them, since the maker needs the whole list in one pass.

Run the tests in table order, then write the output in the order set out at the end of this file, ending in one verdict: a specification, a specification with named gaps, or a wish.

## The shot list: a set checked by enumeration, a sequence checked by adjacency

Two documents wear the same name, and which you need is set by whether the deliverable is seen one image at a time.

**A set is checked by enumeration.** One row per shot category, a category being a shot size or a lens. Each row carries a title, a description bounded at ten to twenty words, and two to ten references that double as the pose list. Three to five categories. **(thin)** Used on the day as a literal checklist, open on a phone, which prevents omission under time pressure.

Where looks rather than shots are the unit, the ordering constraint is irreversibility, not preference: hair and makeup runs soft to bold, because you can add and cannot subtract.

**A sequence is checked by adjacency.** Its unit is a moment rather than a shot, its references are motion clips with stills second, and its test is whether frame A cuts to frame B.

**Enumeration never asks whether two images belong together, only whether each was captured.** For a set seen as a set, a carousel, a series, a plate sequence, enumeration is incomplete by exactly the number of pairs it never looks at, counted in Applied.

## Briefing a maker who is not in the room

An image model is a maker who cannot ask what you meant, cannot be supervised while it works, and can regenerate for nearly nothing. Each changes a different part of the brief.

**Two mechanisms transfer, because both are properties of the finished image.**

The **in-frame inspection list.** The practitioner version, for a styled shoot, is a handful of binary checks run while the shutter fires: the collar seated, the top not bunched at the waist, the accessories visible, the garment hanging correctly. **(thin)** None needs you on set. Write your equivalents before you generate and run them on every return. That is the acceptance criterion.

The **two-ground selection pass,** per principle 6. Of its two grounds, *this composition is one already made before* is load-bearing here, because sameness is the dominant failure of an image model, and the thing to check it against is the model's own house defaults rather than your archive. *Nobody is performing* is the direct test for the posed, dead-eyed portrait a model returns when nothing stops it.

**Everything live does not transfer, and the approval gate is the case worth understanding.** With a person, the maker tethers to a monitor and the approver gives a green light per look. Working with a model you hold both roles, so the gate collapses, and with it what the gate was for: once the approver has said go, a later complaint that a shot was missed is not the maker's fault. **You cannot transfer accountability to yourself.** The written criterion is the substitute, because it is the only artefact in the room that can disagree with you.

**Eight adaptations.**

- **Specify the outcome, not the method.** "Hard light from camera left, low" is an outcome; "a bare bulb in a small box" is a method the model cannot run.
- **State all six distance fields,** since ratio, count, resolution and usage are what a model decides for you by default.
- **Hold the apparatus constant across a series** by fixing the model, the seed policy and a constant style block, so content is the only variable.
- **Lock a key frame first, then generate the rest against it.** Shot order loses its original reason, since generation order is free and nothing is physically irreversible, and gains a better one: an approved first frame is what later frames are made consistent with. This is also what survives of the approval gate, as a batch gate on one locked frame rather than a live green light per look.
- **Reduce the reference count and role every one.** A loose pile averages into mush. Arithmetic in Applied.
- **Over-collect candidates, then cull.** How many more is computable from your criterion, in Applied.
- **Specify the visible signal, not the interior state.** Directing a person to think about something has no mechanism in a model. What transfers is the consequence: jaw set, eyes away from the lens, weight on the back foot.
- **Make the brief structured rather than designed.** Building it in a design tool for better fonts buys legibility for a human reader and nothing for a model. Keep the sectioning, drop the styling.

**Pre-commit the plan B:** which attribute you drop when the model cannot render the thing, which you compose in afterwards, and at what point you stop regenerating.

## The reshoot trigger, and the withhold that is not one

Write one line: **what has to be wrong for this to be made again rather than fixed in post or accepted.** Name the condition, not a feeling. Without it, every return is accepted by default, which is the standing failure of generated work, where another attempt is cheap enough that nobody ever decides one is owed.

The withhold is the other half and not a substitute: if the light is not right the image does not go out, regardless of whether it satisfies the brief. Keep both and keep them separate, because a second person can apply the reshoot trigger and cannot apply your withhold.

## Who specifies, who makes, who signs off

Creating the vision belongs to the creative director. Arranging what is physically in front of the lens belongs to the art director. Specifying the frame, light and lens belongs to the photographer. Checking that the return matches belongs to the approver, with the client holding final sign-off.

**A brief written for an image model collapses the art director and the photographer into the text itself,** because the same lines carry the things in the frame and the framing, light and lens. The vision holder and the approver stay human.

The contested point: one argument says the approver cannot also be the maker, on accountability rather than talent, because the green light transfers blame and that needs two people. The other says one person routinely wears all the hats, which low-budget work requires. Both hold, and the half nobody says is that collapsing the roles is normal **and** destroys the sign-off mechanism. Treat the separation as a claim about who signs off, not about who is capable.

## Anti-patterns

**No written acceptance criterion.** The one that matters most when the maker is absent. *Fix:* one binary in-frame check per fixed element.

**Hoping rather than specifying.** Arriving with a few shots written down and hoping they cut together and the light lines up. *Fix:* the shot list, in the form the deliverable needs.

**Enumerating a set without checking adjacency.** *Fix:* count the pairs, in Applied.

**A description that runs long.** *Fix:* ten to twenty words, or split it into two shots.

**Specifying the content and leaving the apparatus to chance.** The inverse of principle 1, and it produces a body of work where every image was decided twice and nothing is consistent.

**Varying your tools to differentiate.** Shooting at angles not typically shot at is unfalsifiable. Fixing the apparatus and varying the message is checkable.

**Casting on convenience.** Choosing whoever is easiest after having listed the subject as a thing to specify.

**An unroled pile of references.** *Fix:* one attribute per reference, or cut the reference.

**Leaving ratio, count and usage unstated.** *Fix:* the six distance fields.

**Accepting a return because nothing said it was wrong.** *Fix:* the reshoot trigger.

## Applied

Every pixel figure below is taken from the design plugin's `reference/canvas-assumptions.md`: canvases are 1080 x 1080 and 1080 x 1350, the nominal downscale factor is 3 and the stress case is 4, and the rendered type floor of about 12pt therefore has two working-file cases, 36px at the nominal downscale and 48px at the stress case. A floor quoted without naming its case is incomplete. The arithmetic below is this file's; the figures it starts from are not.

### The ratio field, computed

A brief that omits aspect ratio is not saved by a crop afterwards, and the cost is countable.

**Square generated for a portrait placement.** A 1080 x 1080 return in a 1080 x 1350 frame leaves 1350 minus 1080 = **270px with no picture in it**, which is 270 / 1350 = **20 percent of the frame height**, now a design problem: it has to become a type block, a ground, or a reason.

**Portrait generated for a square placement.** Cropping 1080 x 1350 to 1080 x 1080 discards the same 270px, so **20 percent of the picture is gone**, and which 20 percent is a composition decision the brief did not make.

**A return at the wrong resolution.** 1024 x 1024 against a 1080 x 1080 deliverable is short by a factor of 1080 / 1024 = **1.055**, a resize costing nothing visible. The same return against 1080 x 1350 is short 326px of height: 326 / 1350 = **24 percent of the image never generated**. Resolution and ratio are two fields, and the second cannot be fixed in post.

**Type inside the generated frame.** If the brief asks a model to render words, the smallest size that must be read is held to 48px in a 1080 file to survive the stress case, or 36px if only the nominal case. Models have no reliable letterform rendering, so the default spec line is **no type in the generated frame, type set afterwards**, and the brief states the clear area the type will occupy in pixels, so the picture is composed around it rather than cropped into it.

### The reference count, computed

Take five attribute roles: light, wardrobe, palette, framing, pose. **Roled, that is 5 images**, each answerable: you can say what it is for, and a second person can check whether the return got that one thing. **Unroled**, at the photographer's habit of three to ten references per shot category across five categories, it is **15 to 50 images** with no stated job **(thin)**, and a model asked to match 15 to 50 images returns their average, which is a house default wearing your palette.

### How many candidates to generate, computed

Let the criterion hold *n* independent binary in-frame checks, and *p* be the share of returns passing any one. A return passes all with probability *p* to the power *n*, so candidates per accepted image is 1 divided by that.

- **Five checks at p = 0.75.** 0.75 to the fifth is 0.237, so 1 / 0.237 = 4.2: **generate 5**.
- **A six-frame carousel, same checks.** 6 x 4.2 = 25.3: **generate 26**.
- **One weak check.** If identity across the set passes half the time while the other four hold at 0.75, the rate is 0.316 x 0.5 = 0.158, so 1 / 0.158 = 6.3: **generate 7**, or 38 for the carousel.

The 0.75 is an assumption, not a measurement **(thin)**. Replace it by counting your last fifty returns: the share passing each check is that check's *p*. The structural point survives any value: **candidates needed rise with the number of checks, so a longer criterion costs generation volume, and a criterion you cannot afford to enforce is not one.**

### The adjacency load, computed

**A fixed-order set of six.** Neighbouring pairs are 6 minus 1 = **5**. Enumeration runs 6 row checks and leaves those 5 pairs unexamined, so a carousel checked by enumeration alone has **five of its eleven checks skipped**.

**An unordered set of nine,** a profile grid where any image can end up beside any other. Every pair is potentially adjacent: 9 x 8 / 2 = **36 pairs** against 9 enumeration checks, which is why a grid drifts visibly while every individual image passes.

The cheap partial check: generate the two frames you expect to be hardest to reconcile, put them side by side, and commit to the rest only if that pair holds.

### Worked example: a brief that was a wish, rewritten

**Before.** "Hero image for the launch post. Editorial, confident, a bit moody. Think high-end skincare. Attached: 12 reference images."

**Diagnosis.**

- *The ask.* Absent. "Editorial, confident, a bit moody" names three feelings and no mechanism, so nothing downstream is decidable.
- *Mechanism check.* Three lines, zero mechanisms.
- *Reference roles.* 12 images, 0 roles. Against five attribute roles the roled count is 5, so this is **7 references with no job** plus an instruction to average all 12.
- *The six distance fields.* **0 of 6 present.**
- *Acceptance criterion.* Absent, so *n* = 0 and the arithmetic above returns 1 candidate per accepted image. **Whatever comes back is accepted.**
- *Reshoot trigger.* Absent.
- *Verdict:* a wish.

**After.**

*Ask.* "The product is the only warm thing in a cold frame. The reader should want to pick it up."

*Apparatus, fixed.* Hard light from camera left, 45 degrees above, single source, no fill. Grey seamless ground. Long lens, compressed. Cool grey palette, one warm note on the product and nowhere else.

*Open, deliberately.* The angle of the bottle, and whether a second object enters the frame.

*Distance fields.* Count 3. Ratios 1080 x 1080 for the square post, 1080 x 1350 for the portrait post and carousel opener. Resolution 1080 minimum per side, PNG, sRGB. Usage: feed, seen at a third of built size. Budget: one generation session.

*Clear area.* The top 300px of the portrait frame carries the headline afterwards, so nothing load-bearing sits above y 300, leaving 1350 minus 300 = **1050px of picture** the product has to read inside.

*References.* 5, roled: light, ground, palette, framing, product angle. Seven cut.

*Shot list.* Three rows inside the twenty-word bound: square hero; portrait hero with clear area; portrait detail, macro.

*Criterion, five binary in-frame checks.* One warm element only, and it is the product. Single hard light direction, one consistent shadow edge. Ground unbroken grey, no banding. Nothing crosses above y 300 in the portrait frame. Product silhouette unaltered: no invented cap, no extra seam, no changed label geometry.

*Candidates.* Five checks at an assumed 0.75 each is 4.2 per accepted image, times three deliverables: **13 generations budgeted**.

*Adjacency.* Three images in fixed order is 2 pairs. Check both before accepting any.

*Reshoot trigger.* "The product silhouette is altered, or a second warm element appears. Either one is made again, not retouched."

*Verdict:* a specification.

## Tests

Run in this order. Each returns a verdict decidable from this file alone.

| Test | Catches | Verdict |
|---|---|---|
| **1. The ask exists** | A brief with no governing sentence | Point at the one sentence saying what the image has to do. Fails if you must assemble it from several lines |
| **2. Necessity pass** | Lines present because they were available | Delete each line and ask whether the specified image is still the same. Fails on any line where the answer is yes |
| **3. Mechanism check** | Feelings standing in for specifications | Per line, ask whether a second person could answer yes or no about the return without asking you anything. Fails on any line where they could not |
| **4. Answerable from the ask** | Unmotivated or inconsistent choices | Ask why this, per line. Fails if the only answer is that it looks good, unless the line is marked arbitrary, and fails if an ordering is stated twice with two reasons |
| **5. Noun sweep** | Content you did not intend | Underline every concrete noun. Fails if any one is not something you want in the frame, because the maker will try to include all of them |
| **6. Restatement test** | A brief only its author can read | Someone absent from the conversation describes the target image from the brief alone. Fails if their description differs from yours on any fixed element |
| **7. Reference roles** | An instruction to average | Count references, count stated roles. Fails if the numbers differ |
| **8. Fixed versus open** | Guessing, or pointless hiring | List what is fixed and what is deliberately open. Fails at nothing fixed, because the maker is guessing, and at nothing open, because you removed the reason to use a maker |
| **9. Maker-match test** | Control not exercised before instruction | Look at the maker's existing work, or the model's untouched defaults. Fails if the quality you are asking for appears nowhere in it |
| **10. Conduct line** | Harm left unspecified | If a person is in the frame, point at the line saying how they are treated. Fails if there is none |
| **11. The six distance fields** | A maker deciding for you | Count how many of count, ratio, resolution and format, usage, budget and criterion are stated. Fails below 6 unless an omission is written down as deliberate |
| **12. Criterion exists** | Returns accepted by default | Count the binary in-frame checks written before generation. Fails at 0, and fails if any check needs the set rather than the file |
| **13. Candidate budget** | A criterion nobody can afford to enforce | Raise the per-check pass rate to the power of the check count, invert, multiply by the deliverable count. Fails if the result exceeds the generations you will run **(thin)** |
| **14. Enumeration** | A missing deliverable | One returned image per shot list row, and per row the framing, light direction and hardness, lens, palette, wardrobe, time of day, pose geometry, ratio and resolution each match what was named. Fails on any unmatched row or attribute |
| **15. Specified props present, unspecified absent** | Invented content | Two passes. Fails if anything named is missing, and fails if anything unnamed is present. The second half catches generated output |
| **16. Two-ground selection pass** | Repetition and performance | Ask whether this composition is one already made before, and whether anyone looks like they are performing. Fails on either |
| **17. Adjacency check** | A set whose members do not sit together | For a fixed order of n images check n minus 1 pairs; unordered, n times n minus 1, divided by 2. Fails if any pair differs visibly in palette, light direction, lens compression or subject identity |
| **18. Invariants held** | A drifting series | Name what you fixed, confirm it is identical in every return. Fails on any variation in a fixed element |
| **19. Reshoot trigger** | Acceptance by exhaustion | Point at the written line. Fails if absent, or if it names a feeling rather than a condition. Then ask the separate withhold question, whether the image is wrong by your own standard, which fails the ship decision regardless of compliance |
| **20. Receipt confirmed** | A participant working from nothing | Every participant has confirmed receipt. Fails on any silence **(thin)** |

## Checklist

The fields, since the tests table already carries the verdicts.

- [ ] The ask written before any visual choice
- [ ] Light, framing and shot size, palette or grade specified
- [ ] Wardrobe, props, location and post-processing intent specified where relevant
- [ ] Conduct specified if a person is in the frame
- [ ] Maker or model cast to the board, not just instructed
- [ ] Key frame locked first if the deliverable is a set
- [ ] Clear area stated in pixels if type is set afterwards
- [ ] Candidate budget computed from the criterion

## The ultimate test

Hand the brief to someone who was not in the conversation, have them produce the image, and then decide whether to accept it using only what you wrote down.

If you can accept or reject it against the text, the brief was a specification. If you have to look at it and feel, you wrote a wish, and with a maker who is not in the room a wish is accepted by default.

## What an agent can run, and what it cannot

**Can run:** the six distance fields, the necessity pass, the noun sweep, reference roles as a count against a count, fixed versus open, the candidate budget arithmetic, the adjacency pair count, enumeration against the shot list, specified props present and unspecified absent from a described frame, and the in-frame checks if written as frame properties. Flagging every inventory element the brief leaves unspecified is the highest-value automatable check here.

**Cannot:** the maker-match test, which needs the maker's existing work. Whether a composition is one *you* have made before, which needs your archive. Whether the ask is the right ask. The withhold question, which is a judgment.

**If the agent is the maker,** give it the criterion with the brief so it rejects its own output before returning it. That works only because the criterion is written in frame properties, and it is the one case where the absent maker is better supervised than the present one.

## Where this skill should lose

**When you are still assembling the references.** Use `ad-board`, the sibling owning how a reference board becomes a direction rather than a collection: sourcing, annotating each image to the single attribute it carries, reduction, and avoiding a board that looks like everyone else's. This file assumes the board arrives roled and reduced. If yours is a pile, close this file: an unroled board fails test 7 and no amount of brief writing repairs it.

**When the rules outlive this one image.** Use `ad-rules`, which owns writing a visual direction as clauses a maker can be held to, with thresholds and prohibitions. A standing threshold applying to every image a brand makes belongs there; a line applying to this job only belongs here. If you are writing a rule you would want enforced on the next twenty pieces, you are in the wrong file.

**When the image already exists and needs notes.** Use `ad-critique`, which owns the form a note takes, the order findings are given in, and when to call the end of exploration. This file produces pass or fail against a written criterion; that one produces a note a maker can act on, which is a different artefact.

**When the picture is chosen rather than commissioned.** Use the design plugin's `dsn-image`, which owns choosing a photograph, cropping it, treating it, rescuing a poor supplied one, and how a picture and type share a frame. It also carries a short reference-group brief to a photographer, grouped by angle, action, location and light, for the narrower case of a picture that has to sit in a layout. Close this file when the question moves from what the image is of to what is done to it. The two meet at the clear area: this file states the pixels type will occupy, that one decides how picture and type behave inside them.

**When the deliverable is one frame carrying an idea alone.** Use the design plugin's `dsn-poster`, which owns a single canvas with no next slide: the element ceiling, what gets cut, the type sizes against the floor, and whether the frame is finished. A brief can specify a picture perfectly and still specify the wrong thing, because a frame carrying an idea by itself often cannot afford a picture at all. If the arithmetic there argues the picture out of the frame, that finding outranks this file's shot list.

**When the question is the order of a set, or whether a number clears a measured floor.** Both live in the design plugin: the skill owning ordering across frames decides what frame three does given frame two and how many frames a piece needs, while the skills owning type scale, colour and measured contrast own every floor and step. This file counts adjacency pairs and quotes canvas figures to write a spec line. Quoting is the limit: deriving a type scale inside a brief means you have crossed into design.

The dependency runs one way. This file points at design skills; nothing in the design plugin needs to point back here.

## Writing the output

When auditing a brief or a return, report in this order:

1. Inventory elements left unspecified, listed.
2. Which of the six distance fields are missing.
3. Whether an acceptance criterion exists, and whether every check in it is observable in the finished frame.
4. Whether a reshoot trigger exists, and whether it names a condition rather than a feeling.
5. What is fixed and what is open, and whether that split is deliberate.
6. For a set, every neighbouring pair that will not sit together, by pair.
7. One verdict: a specification, a specification with named gaps, or a wish.

Name the field and give the number: "12 references carry 0 stated roles against 5 attribute roles", not "the references are unfocused". Show the arithmetic whenever a number decides something, because "a 1024px square return is 24 percent short of a 1080 x 1350 deliverable in height, which is not a resize" settles the question and "the resolution is too low" starts an argument.

Say which tests you ran and what each returned, including the passes, because a pass and a skipped test look identical in a summary listing only failures. Separate the mechanical from the reading: a missing ratio field is not arguable, whether the ask is the right ask is.

Sources, corroboration, contested questions, refused claims and what the material does not reach are in `references/provenance.md`.
