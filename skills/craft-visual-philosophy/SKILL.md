---
name: craft-visual-philosophy
description: Turns an idea into a clear visual by testing it through philosophy's branches (purpose, the things, how they relate, the visual mechanic, how sure we are, how it will be read, which signs carry it), then makes several options and cuts. The designer runs it before picking a visual move. Use for any diagram, framework, field guide or request to show an idea visually.
---

# Visual Philosophy

Method by Josué Valles, the studio's author.

## In the studio

The method is kept whole here. In the studio it is the designer's first step, before `fmt-post-visual` picks a move from the library:

- **Inputs come from the piece and the canon.** The idea in one or two sentences is the brief's "one idea" (`pieces/<id>/brief.md`); the parts and the relationship come from the brief's fractal shape and the canon entries it links; the reader and purpose come from the brief's reader section and the channel file (`canon/strategy/channels/<channel>.md`). Ask the person only for what those don't hold.
- **Output goes into the piece folder** as `visual-brief.md` (where it goes, always, is the one rule in `skills/fmt-post-visual`, "Where `visual-brief.md` goes"): the shared part, three options with their sketches, and what was cut. `fmt-post-visual` then takes the chosen option and builds it with the move library, neutral first, then in the person's style.
- **Every headline and label** passes the house rules (`skills/craft-house-rules`) and the stand-alone test: understandable by someone who never reads the post, in the reader's own words, no concept names.
- **Styling** comes from the person's design system (`canon/visual/`, written by `setup-visual-identity`) when one exists, and from the TRAIN principles below when it doesn't.

Facts about the person never live in this file. It names the canon and piece files to read.

## Run on its own (`/visual-philosophy`)

The whole method, from Step 0 to the sketches, with nothing built yet. The person hands over an idea in a sentence or two, a post or essay (pasted, or a piece in `pieces/`), or a framework they've been drawing on paper. They get back the output below: what all options share, three options with a sketch each, and what was cut.

- **Inputs.** For a piece in `pieces/`, read its `brief.md` and latest draft as above. For pasted text or a bare idea, work out the answers from what they gave and show them for a quick check; ask only what's missing, one question at a time. For the reader, read `canon/strategy/audience.md` when it exists, or ask who will see it. A fact about the person on a label (a number, a client, a result) comes only from what they gave, `material/` or the canon (`CLAUDE.md` rule 1).
- **Saved to** a piece folder and shown in the chat, by the rule in `skills/fmt-post-visual`, "Where `visual-brief.md` goes".
- **No canon change without their yes.** A framework they name while you work is new, so it goes in as a `draft` branch entry in `canon/person/branches.md` (name, parts and `visual` in their words, `sources: said in /visual-philosophy, <date>`, a log line), after one question ("want me to keep this framework in your files?"), as `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes", says. A shape that connects entries already in their files (the same structure under three branches, say) is a connection, so it goes to `proposals.md` as `seen`, with their words quoted and one question, after checking the open proposals and the cap in `templates/proposals.md` (rules 6 and 8).
- **Next.** When they pick an option, `/visual` builds it from their Figma kit, neutral first, then in their style. This command stops at the brief and the sketches.


A method for articulating an idea visually. Each branch of philosophy asks one question about the visual, and a set of visual mechanics, many drawn from Jack Butcher's Visualize Value method, turns the answers into a shape. Answer the questions in order and the form follows from the idea instead of from a template.

Two beliefs sit under the method:

1. A visual is an argument. Its shapes make claims about what exists, how things relate, how sure we are, and what the reader should take away. A good visual makes true claims and makes them easy to read.
2. The meaning should live in the shape, not in the words. In a strong visual, you could delete every label and still see the idea. Words name what the reader has already understood. If the labels are doing all the work, you've made a diagram about the idea, not a picture of it.

Why this matters: people recognize visual patterns faster than they parse sentences, and they remember the idea rather than the wording. A visual also doesn't depend on the reader sharing your vocabulary. A good one carries an idea across fields and languages.

## How to run it

Work with the person in conversation. Ask one question at a time, and only ask what you can't work out from what they already gave you. If they hand you a full idea, a draft, a post or a document, extract the answers yourself and show them for a quick check instead of interviewing.

### Step 0. State the idea and find its logic

Ask the person to say the idea in one or two plain sentences. If they can't, help them find it before drawing anything. A visual can't fix an unclear thought; it only exposes it. Offer back your best version and ask if it's right.

Then look for the logic underneath the sentence. Not every true sentence has a shape, and the ones that do usually contain one of these. This is the one list of what gives an idea a shape; `fmt-post-visual` and `/visual` point here:
- a contrast between two states (with and without, theory and practice, what you said and what they remember)
- a transformation, or a change over time (where someone starts and where they end up, and the shape in between)
- a difference in size or amount
- parts of a whole that relate in space
- an order (steps, levels)
- an intersection (two things, and a thing that only exists where they meet)
- a relationship that holds every time (more of A means less of B)

If the idea has none of these, say so. It may be better as words, or it may need sharpening first. Butcher's own test when choosing what to draw was whether the idea has some underlying logic or contrast that jumps out.

For a long post or essay, there may be several visual ideas inside it. Find the one that carries the core claim, and note the others as possible options.

### Step 1. Teleology: what is this visual for?

Find the purpose and the reader.
- Who will look at it, and what do they already know?
- What should they be able to do, decide, remember or believe after seeing it?
- Where will it live (a post, a slide, a page, a whiteboard)? Will it sit next to text, or have to stand alone?
- Is the goal to make them feel a problem they recognize, or to show them how to fix it? These lead to different visuals.

The purpose decides what stays and what goes. Harry Beck's London Tube map works because its purpose was narrow: get a rider from one station to another. Everything that didn't serve that, including real geography, went.

### Step 2. Ontology: what are the things?

List the parts of the idea: the things, people, stages, forces or categories it involves. Then check the list.
- Is each item really a separate thing, or are two of them the same thing named twice?
- Are they at the same level, or is one a kind of, or a part of, another?
- Is anything missing that the idea depends on?
- Which parts are the core claim, and which are setup? Setup usually doesn't belong in the visual.

When you put boxes inside boxes or branches off a trunk, you claim how the world divides. The Porphyrian tree (3rd century) split "substance" step by step down to "human" and made every split a claim. A chart that nests every stage of change inside the next one claims each stage contains all the earlier ones. Make sure your categories and your nesting are ones you'd defend.

### Step 3. Logic: how do the things relate?

Name the relationship the idea rests on. Most ideas rest on one, sometimes two. Each common visual device carries a meaning readers already know, so match the device to the relationship: the table of relationships, their devices and what the reader understands without being told is `skills/fmt-post-visual/library/visual-moves.md`, Layer 2 (the one copy of it; a bigger idea is bigger, left came first, the overlap is both).

Treat these as options that fit, not a menu to start from. Sometimes the best form is a scene, a borrowed object, or a single comparison. Maslow's hierarchy works as a pyramid because the shape itself makes the claim that lower needs hold up higher ones.

Then check that the argument holds. If the visual implies "A leads to B leads to C," is that true in every case, or only some? Euler drew circles to show that if every A sits inside B and every B inside C, every A sits inside C. A good diagram makes the conclusion visible; a broken argument often looks wrong on the page.

### Step 4. Find the visual mechanic

This is the step that turns a relationship into a picture. Try these in order, and use the first one that carries the idea without leaning on labels.

**a. One repeated mark that changes in one way.** Pick a single unit (a circle, a bar, a line, a square, a dot) and vary one property: size, length, number, smoothness, position, darkness. The eye compares instead of reads. Examples: circles that grow when you avoid a problem and shrink when you face it; fifteen bars for "what you said" next to one bar for "what they remember"; steady rising bars for product-market fit next to one spike for hype; Minard's map of Napoleon's march, where the width of the line is the size of the army.

**b. Comparison: the same marks, two states.** Show the idea as two sides of a story, with and without, before and after. Use identical elements on both sides and change only what the idea is about, so the difference is the only thing left to notice. Every comparison needs a baseline; without contrast the reader can't see the point. Butcher's examples: "Examine what is said, not who speaks" as two chat threads with the emphasis swapped between the message and the speaker; Yogi Berra's "In theory there is no difference between theory and practice. In practice, there is" as a smooth textbook curve next to a jagged real chart.

**c. Scale.** When the idea is about size, let size do the talking. Butcher drew Confucius's "The man who moves a mountain begins by carrying away small stones" as a mountain with an almost invisible corner trimmed off.

**d. A borrowed symbol.** Use something the reader already knows and let its meaning carry over: an eye for vision, a speech bubble, a chat window, a dialog box whose only button that works is "change," a calendar day crossed out, a bouncing ball for "fail better," a compounding curve, a target for a narrow view. Familiar symbols bring decades of shared meaning for free; people recognize a toy airplane as an airplane even though it couldn't fly. Avoid the worn-out version (a lightbulb for "idea") unless you twist it into something new.

**e. A metaphor you build.** When no symbol exists, reverse engineer one from the concept. Butcher drew "reality" as a complex geometric pattern from nature and "your perspective" as a small target placed over it. Build the metaphor from a property the idea actually has, not just a resemblance.

Three rules apply to every mechanic:

- **Two states read as a switch; three or more read as growth.** If the idea is gradual change, show several in-between steps. "Consistency creates competence" works as a row of wobbly shapes slowly becoming a perfect circle, not as one bad circle and one good one.
- **Draw how it feels when the idea is about experience.** The Yerkes-Dodson curve and hand-drawn "creative process" charts put an experience on a line, and people recognize their own life in the shape. If the idea is a feeling (a sting, dread, momentum), drawing it as a process of boxes and arrows loses it.
- **Let the structure be the argument.** Manu Cornet's org charts of tech companies work because each drawing is the claim: one is a clean hierarchy, one is a mesh, one is everything pointing at one person. No caption needed.

Only fall back to labeled boxes and arrows when the idea really is a procedure the reader needs to follow step by step.

### Step 5. Epistemology: how sure are we?

Visuals look more certain than words. A clean framework reads like settled fact even when it's a model or a guess.
- Which parts are evidence, which are the person's model, which are open questions?
- Do clean lines and hard boundaries suggest more precision than exists? If categories blur in reality, the visual can show that.
- Does any number, size, proportion or count imply a measurement nobody made? Labels like "one" vs "many" or bars of exact lengths can claim more than the person knows. Keep proportions loose enough to read as illustration unless there's real data.
- Does the shape promise more than the idea does? A visual of a method shouldn't imply it always works.

Show only as much certainty as the person has. When it helps, frame the visual honestly as a way of seeing the problem rather than a law.

### Step 6. Hermeneutics: how will it be read?

Readers interpret with habits they bring with them. Design for the reading they'll most likely make.
- Arrows can mean causes, leads to, becomes or flows into. Make sure only one reading fits. Arcs and connecting lines need a clear meaning too; a web of arcs that never says what an arc means looks deep but tells the reader nothing.
- Size reads as importance. Up reads as better or more. Left to right reads as time for left-to-right readers. Center reads as core. Dark and light read as without and with (vision, knowledge, clarity).
- Map the order of the statement to the order on the page. If the sentence says "what is said, not who speaks," the left side shows what is said.
- Keep a meaning consistent once you assign it. If left means before, it means before everywhere.
- Give the eye one place to start and a clear path through, using size, contrast and placement.

### Step 7. Semiotics: which signs carry the meaning?

Charles Peirce sorted signs into three kinds: icons look like what they mean, indexes point to it, and symbols mean something only by agreement. Choose signs the reader already understands.
- Prefer familiar shapes and borrowed symbols over private symbols or invented icons.
- Treat words as training wheels. Use as few labels as the visual needs to be understood on its own, and put them on what the reader can't infer. Writing each clause of the statement on its matching part of the picture works, but a visual that gets the idea across with fewer words is stronger and easier to remember. Butcher's aim: once someone has read the idea and seen the image, the image alone should bring the idea back, like hearing the instrumental of a song you know.
- The visual still has to make sense to someone who never reads the post. So keep a plain, concrete headline that states the idea rather than teasing it, and write any labels in the reader's own words, with concrete nouns and verbs, not concept names that need an explanation.

### Step 8. Make many, then cut

- Make several versions before choosing. Keep them all side by side rather than overwriting, because the best result is often parts of two or three versions combined. This is the same as writing a paragraph three ways and keeping the best sentence from each.
- Use helper elements (guide lines, extra labels, measurement marks) while working out proportions, then remove them.
- Edit like writing: what can you take away and still make the point clearly? Butcher describes the sequence as finding the edges of the idea, chipping away what's extra, then compressing until only the essential outline is left.
- Remove every element that doesn't serve the purpose from Step 1. Stop when removing one more thing would break the idea.

### Step 9. Test

Run the tests in `skills/fmt-post-visual/library/visual-moves.md`, "Tests for any picture" (the one copy: delete the labels, stand alone, stranger, wall, certainty, one meaning). If nothing is left but a row of rectangles once the labels go, go back to Step 4. For the stranger test, show it to someone if you can; otherwise describe what a first-time reader would most likely conclude, and fix any gap between that and the intended idea.

## Output

Start with what all options share, written once: the idea in one or two sentences, the purpose and reader, the parts and how they're grouped, the main relationship, and how certain the visual should look.

Then give three options; fewer only when the idea allows only one honest shape, and then say so. Make them use different mechanics from Step 4 (for example one repeated-mark visual, one comparison, one borrowed symbol), so the person chooses between real alternatives rather than variations of one layout. Lead with the strongest.

For each option, give a short brief:

1. The mechanic, and one line on why the shape fits the claim
2. Layout: what's drawn, where it sits, what the reader sees first, what size, position and repetition mean
3. Headline and every label, written out (as few labels as the visual needs)
4. What it emphasizes, and its weak spot (for example, "carries the feeling but not the fix")
5. The result of the delete-the-labels test, in a line

End with what was cut, in a line, so the person can add it back if they disagree.

### Sketches (required for every option)

Always produce one sketch per option, placed right after that option's brief. The sketch shows the idea, not a design. Its only job is to let the person see the structure and judge whether the shape carries the claim.

Keep every sketch neutral:
- Grayscale only: black or dark gray lines and shapes on a white or transparent background. One light gray fill at most, used only to group or contrast things.
- Plain shapes: circles, bars, lines, curves, squares, simple outline symbols or stick figures. Draw the mark the mechanic calls for (the growing circles, the jagged line, the trimmed mountain), not boxes describing it.
- One plain sans-serif typeface, at two or three sizes at most (headline, labels, small notes).
- No brand colors, textures, illustration styles, shadows, gradients or decoration.
- Use the real headline and labels from the brief, so the person can test whether the words and the shape work together.
- Make the layout match the brief: same positions, same reading path, same meaning for size and space.

How to draw it: draw the sketch inline in the conversation as SVG or simple HTML when the session can render visuals. If it can't, give a plain-text sketch in a code block that shows the same layout. Never skip the sketch because the brief already describes the layout.

A styled version, in any visual style the person uses, comes only after they pick an option and ask for it.

## When styling comes later

When the person picks an option and asks for a finished version, apply their own visual style if they have one. If they don't, these principles from Butcher's content-system lesson (TRAIN) keep it clear:
- **Typography:** pick one or two typefaces and use size and weight to set the reading order, like a newspaper front page.
- **Restraint:** decide the palette and tools once (Butcher kept to black and white vector shapes) so the effort goes into the idea instead of endless tweaking. Black and white also carry ready-made meaning: dark and light, without and with.
- **Alignment:** line elements up on a grid; invisible relationships make a piece feel finished.
- **Image treatment:** if photos appear, give them one consistent treatment.
- **Negative space:** space frames the idea. Resist filling it.

## Common failures to catch

- The labels carry the meaning and the shapes are just containers (a flowchart where a picture was needed).
- Two states drawn with different elements, so the reader has to read to find the difference.
- A process drawn where the idea is really a feeling.
- Decorative arcs, orbits or webs whose lines never say what they mean.
- Nesting or layering that makes a claim the person wouldn't defend.
- So many labels and layers that the main relationship gets lost.
- Proportions or counts that imply a measurement nobody made.

## Writing rules for every word in the visual and the brief

The house rules (`skills/craft-house-rules`) apply, and supplied wording follows `CLAUDE.md` rule 3. Two more for this method:

- Use real examples (a known map, campaign, brand, historical case) or plain logic. Don't invent hypothetical cases and present them as real.
- Stay nuanced: give principles, and treat specific devices, mechanics and moves as possibilities rather than rules that fit every case.