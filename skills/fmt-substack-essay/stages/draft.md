# Essay draft

Input: the piece's `brief.md`, with its material, purpose and format plan (IDEA, READER NOW, QUESTIONS, STRUCTURE, TITLE MOVE, SUBTITLE JOB, OPENING MOVE, SECTIONS, INSIDE MOVES, CLOSE, LENGTH, ACCESS, EXAMPLES, WATCH FOR, and OPENING when the person picked one). If there is no brief, or its format plan is empty, run the moves stage first. Do not draft from a topic.

What the writer reads at this stage, and nothing else: `pieces/<id>/packet.md` (built by `python3 scripts/packet.py pieces/<id>` after the moves stage: the writer's sheet, the brief, the cards the plan picked, the voice) and this file. The libraries, the full house rules, `craft-human` and `craft-copylosophy` stay closed at the moment of writing; the judge reads them. The plan's EXAMPLES line holds each pulled essay's title, and that is all the writer reads of them.

Voice: follow the voice order in `skills/craft-house-rules` ("The voice order"): the rewrite pairs, the voice guide when it exists (including anything it says about essays: how to open, which kinds of examples to use, how to sign off), five to eight of the person's own pieces from `material/`, and plain writing only when none of those exists.

Two standards sit under the voice and apply to every person:

- `skills/craft-house-rules/SKILL.md`: the house rules and the method under "How the sentences get written". In short: read the person's own writing first (the voice order); when they've already said the thing (a memo, a transcript line, a rough draft), keep their sentences and add only the connecting tissue; write three distinct drafts of the whole piece, different in what leads and how it moves, and hand all three to the judge; then run `python3 scripts/self-check.py <draft> [--source <their raw words>]` (check-mechanical, check-human without the detector, check-prose, voice-diff and check-stitch with `--cap 4`, each of Posts A, B and C on its own) and fix what fails. `skills/craft-human/SKILL.md` explains the six patterns the scripts measure.
- `skills/craft-copylosophy/SKILL.md`: every essay argues something, even a story essay. Run the writer pass as defined in its "In the studio" section on the IDEA before writing, and build the sections on premises that hold. Its output goes in the draft, never in the brief.

## Why this order

The body comes first, then the title, the subtitle and the opening. The title and opening promise what the body delivers, so they're written once the body exists, against it. When the person already picked a title and opening (the plan's OPENING line, from `/essay` stage 2), that pick leads: the body is written to keep its promise, and the title and opening are sharpened against the body, never replaced.

## Before writing

1. Read the packet top to bottom once: the sheet, the brief, the cards, the voice. Then read the IDEA and the QUESTIONS in the format plan again. Keep the idea sentence in front of you the whole time.
2. The cards for the structure, the title move, the subtitle job, the opening move and each inside move the plan lists are in the packet. Keep each mechanism sentence in front of you; they're the tests.
3. The plan's EXAMPLES line holds each pulled essay's title; that is all the writer reads of them. If the examples don't match the plan's structure, say so under Brief defects and draft from the cards.

If the format plan has no QUESTIONS line (a brief written before the moves stage worked out the reader's questions), run the moves stage's step 1a on the brief first, add the lines, and note it under Brief defects. Don't change anything else in the brief.

## Step 1. Body, section by section

Build the sections the plan lists, in order. Each one answers its question from the plan. For each section:

- A header that says what the section gives the reader, in plain words. Not a pun, not a label only the writer understands.
- The section's job, done with the material the plan names. One idea per section, and every section serves the essay's one IDEA.
- The inside moves the plan assigns to it.
- A bridge in its last line (N4) when the next section answers something this one raised.

The reader's questions decide what the essay covers and in what order; they don't appear on the page as questions and answers (no questions as headers, no "Why? Because..." pairs).

When the body is written, check it against the structure's parts below. They're what each structure usually needs, a check after the body exists and never a form to fill: when a part listed here isn't in the sections, either a question was missed (add the section) or the idea doesn't need it (say so in one line under Brief defects). The card has the rest.

**E1 The argument**: the claim plainly; reason one with its own case; reason two with a different case; the real objection in the reader's words and the answer; what changes if the reader accepts it; the claim again, stronger.

**E2 The diagnosis**: the problem in the reader's terms; what's happening (how it got this way); what it means (consequences); what to do (a rule, then how to apply it). The prescription follows from the cause.

**E3 The named idea as a lens**: the puzzle; the name and its one-sentence definition, with where it came from; the idea in at least three places, ideally far apart; the idea turned on the reader's own situation; the catch it creates.

**E4 The ladder**: the model (describe the diagram if there will be one); each level with its signs, its trap and the way up; why the top level wins; where the reader probably is.

**E5 The story essay**: the story to the turn; the idea named once, plainly; a second case so the first isn't a one-off; how the writer uses the idea now; the reader's version.

**E6 Changing my mind**: the old belief; why it was right then; the evidence, in the order it arrived; the new position with its limits; what the reader can do with it.

**E7 The worked case**: the result and why it's shared; the starting point; stage by stage, each with the general rule it shows; the result in numbers; what to take from it.

**E8 The protocol**: why the usual approach fails; the ideas that build the case; the protocol, step by step, specific enough to follow without asking; a recap line per step.

**E9 The explained list**: why these matter; each item with its reasoning and a real example; a section that turns the list into use (questions, a checklist, a habit).

**E10 The annotated source**: why this source; each part opened with the source's exact words, credited, then notes that add something; each part ending on what the next answers; the writer's own answer at the end.

**E11 The resolved paradox**: both sides as opposites; why each matters; why one alone fails; how they fit; how to live it.

**E12 The objections answered**: the situation; the objections in the reader's words; each answered with a reason.

**E13 The book**: a table of contents with one claim per chapter; an introduction that sets the reading contract; chapters that each end with a bridge; the one idea coming back in each.

Whatever the structure: the turn is one line, the meaning line comes after the material has made the point, and nothing in the essay is there because the structure has a slot for it. A section that doesn't serve the IDEA comes out, however good it is.

The person's facts are written fresh, from what they mean and in their register, and cited to where they came from; their sentences are kept only when they wrote them about this thing (a memo, a journal entry, a draft on this idea), or when the exact words are the point, marked `verbatim` and inside the cap of four (H34 in `skills/craft-house-rules`; `scripts/check-stitch.py --cap 4`). An example they used to teach stays an example of how they teach, never something they did. Examples come from the material. When a section needs an example the material doesn't hold, use a real, checkable case (a known story, campaign, company or moment from history or the news) and mark it in the source map as `borrowed: verify` (see rule 1 in `CLAUDE.md`), with the source named. Never invent a client, a story, a number or a scene and present it as real. Follow the voice guide if it rules out hypotheticals altogether.

## Step 2. Titles, subtitle and opening, written against the body

**Titles.** Write three titles. All three use the plan's title move. They differ in which piece of the material leads. When the plan has an OPENING line, the person already picked a title and opening: all three titles start from it, keeping its move and meaning and sharpening only the wording. Words the person wrote themselves are supplied copy and stay as written.

For each, check it against the mechanism in one line. T1: is the number exact and does the payoff come from it? T2: does the method really work under the condition the bracket states? T4: is the cause one the reader wouldn't find by looking at the problem? T7: can a stranger guess what the term means, or does the subtitle tell them? T9: would the reader use these words about themselves? Then the promise: does the body you just wrote deliver what the title says? If either check fails, the title isn't done.

Use the person's numbers and words as they gave them. Don't round, inflate or reorder them. A title must work alone in an inbox, next to dozens of others, with no picture.

**Subtitle.** One subtitle for the chosen title, doing the plan's job. One sentence, two at most. Check: does the title plus the subtitle tell a stranger what they'll get? If the title is a riddle, a coined term or a quote and the subtitle doesn't explain it, rewrite the subtitle.

**Opening.** Write the opening with the plan's opening move, from the first line to the promise line, or sharpen the one the person picked. It should reach the reader's own problem within the first 150 words, whatever the move. It ends on one sentence that says what the reader will have by the end, and the body already delivers it; write it plainly, not as an announcement ("In this essay I will..."). If the body can't keep the promise of an opening the person picked, say so under Brief defects rather than changing the opening.

The opening never starts mid-thought or assumes the reader read an earlier essay.

## Step 3. Close and furniture

Write the close the plan chose. Offer one alternative. Then the sign-off the voice guide sets, if any; never a closing sentence that could end any essay.

If ACCESS is paid, mark the paywall in the draft as `[PAYWALL]` at the place the plan names, and check that everything above it is whole on its own.

Plugs and asks only as the channel's selling rule allows, and never in place of the close.

## Step 4. Assemble and strip

Read it once as a reader in an inbox: title, subtitle, the first screen. Then the whole thing. Then apply the house rules (`skills/craft-house-rules`) as cuts. Three more for an essay:

- Every term used before it's explained.
- Copywriter habits stretched over an essay: one-line paragraphs stacked for effect, rhetorical questions in a row, a landing line closing every paragraph, every section built the same way.
- Any section, paragraph or example that doesn't serve the one IDEA.

Supplied copy and source quotes: CLAUDE.md rule 3. The plan's LENGTH is a guide: the essay is as long as its sections need. If it runs well past the guide, cut the sections that serve the idea least before trimming sentences; never pad to reach it.

## Three drafts

The house rules ask for three distinct drafts, and the judge picks. All three answer the plan's questions and carry the same IDEA; they differ in what leads and how the sections move, never in the idea. When the person picked an opening, all three keep it and differ in the wording around it. Write each body fresh; don't make B and C by editing A.

## Output

```
TITLE OPTIONS   three, each with a one-line mechanism check and promise check
SUBTITLE        for the chosen title, with its job
ESSAYS          three distinct full drafts (A, B, C), each with its title, subtitle, opening, sections with headers, close, sign-off, [PAYWALL] if paid; say in one line what each one bets on
ESSAY           the one you would pick, and why in one line (the judge may pick another)
CLOSE ALT       one alternative close
PARTS MAP       the promise line, the thesis line, each section's job in a few words, the turn(s), the bridges, the meaning line
BRIEF DEFECTS   anything in the plan or brief that didn't hold (a card number and description that disagree, examples that don't fit), what you did, and why
ARGUMENT CHECK  the writer pass of craft-copylosophy: the premises and the refined thesis
```

Save it as `draft-vN.md` in the piece's folder (from `templates/piece/draft.md`). Each of the three drafts (title, subtitle and essay) goes in its own section, `## Post A`, `## Post B` and `## Post C`, and nothing else does; a revision of the one draft the judge picked goes under a single `## Post`. Write the essay's section headers as `###`, because the check scripts measure each `## Post` section and stop at the next `##`. TITLE OPTIONS, SUBTITLE, CLOSE ALT and PARTS MAP go under `## Format stage blocks`, BRIEF DEFECTS under `## Brief defects`, then the source map in the five kinds of `CLAUDE.md` rule 1, then ARGUMENT CHECK under `## Argument check`. If no piece folder exists, give it in the reply.

Hand the output and the brief to the judge stage. Do not revise from your own reading; that's the judge's job.
