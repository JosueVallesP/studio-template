# Essay judge

Input: the draft (with its PARTS MAP and source map if it came from the draft stage) and the piece's `brief.md`. If there is no brief, build the minimum one first: the one idea the draft carries, which structure, which title move, subtitle job and opening move, which close. State those assumptions at the top of the verdict.

Library files:
- `../library/hook-moves.md`
- `../library/body-moves.md`
- `../../fmt-linkedin-post/library/body-moves.md` (inside moves M1 to M9, closes C1 to C6)

Read the cards for the structure, the title move, the subtitle job and the opening move before judging. Grades come from the gates table in `skills/role-editor`: the title and opening checks (sections A and B) are "Format: opening craft", checks 10 and 11a are "Format: wrong shape or different idea", the rest of section C is "Format: body", and the rest are "Format: other checks" unless a gate there owns them. Judge against the cards, not against taste. Leave the draft's `## Argument check` unread until your own premise verdicts at check 31 are written; then note where the writer's verdicts differ.

## How to judge

Each check gets PASS or FAIL. A FAIL names the line or the section and says what's wrong in one sentence, using the card's language. Don't soften a fail. Don't rewrite the essay; give the fix for the one line or section, and only when the fix is obvious.

The judge is a different pass from the draft on purpose. If you wrote the draft, you're not the judge.

## Checks

### A. The title and subtitle earn the open

1. **Mechanism.** Does the title do its move's job? (T1: does the exact proof earn the payoff? T2: does the body's method really work under the bracket's condition? T4: is the cause one the reader wouldn't find alone? T7: can a stranger tell what the term means, from the title or the subtitle?)
2. **Works alone in an inbox.** Read only the title and subtitle. A stranger can say what they'd get. If not, FAIL.
3. **The subtitle does a job.** It explains, makes the payoff concrete, names the reader, raises the stakes, tells the story, says what it is or adds a deadline. A subtitle that repeats the title or adds nothing ("My thoughts on this") is a FAIL. No subtitle is a FAIL when the title is a riddle, a coined term or a bare quote.
4. **How it fails.** Go down the title move's "how it fails" list. Name any item the draft trips.
5. **Material is real.** Every number, name and claim in the title and subtitle comes from MATERIAL in the brief.

### B. The opening earns the scroll

6. **The move's job.** The opening does what its card says, with real material.
7. **Reaches the reader's problem fast.** Within the first 150 words or so, the reader can see what this has to do with them. If the opening runs on the writer's story or a big claim past that with no link to the reader, FAIL.
8. **The promise is there.** By the end of the opening, one sentence says what the reader will have by the end. Plain, not announced ("In this essay I will...").
9. **Stands alone.** It doesn't start mid-thought or lean on an earlier essay.
9b. **It does its job for its reader.** Read the brief's one real reader and Outcome, then the essay as that person. Would they come away thinking, feeling or doing what the Outcome says? FAIL when the essay speaks to someone else (examples, objection or level of detail that fit a different reader) or stops short of the Outcome; quote the line where it turns away. Written for a different reader is a redo; stopping short is a revise. A brief with no named reader (older pieces) skips this check.

### C. The body keeps the promise

10. **One idea.** State the essay's idea in one sentence. Every section serves it. A section that serves a different idea is a FAIL, named. An essay whose idea isn't the brief's one idea is a redo.
11a. **The shape fits the idea.** Do this before reading the plan's QUESTIONS or SECTIONS. Read the essay as a stranger and write down the questions it raises, in order, and where each gets answered. Then compare with the plan. Four ways to fail:
   - **A question left hanging.** The idea needs it answered and the essay doesn't answer it. FAIL, quote where it's raised.
   - **Padding.** A section or paragraph that answers no question the reader would have, or one the idea doesn't need. FAIL, quote it; the fix is the cut.
   - **The wrong shape.** The idea would be clearly easier to get in another structure (a list that's really one argument split into items; a protocol where the reader first needed to be argued out of something). FAIL only when you can name the other structure and say in one sentence why it reads more clearly for this reader. This fail is a redo. An essay that changed the plan's structure and says why in Brief defects is judged on whether the change was right.
   - **The questions on the page.** Questions as section headers, "Why? Because..." pairs, a run of questions it then answers. FAIL, quote the lines; this is a revise.
11. **Structure matches.** The body is the structure the brief chose, or the draft says why it changed.
12. **The parts the reader needs are there.** Held against the structure's parts in `draft.md` step 1 as a check: a part the essay skips fails only when the idea needed it and Brief defects gives no reason (diagnosis: the prescription follows from the cause; ladder: each level has signs; worked case: a rule pulled from each stage; protocol: steps a reader can follow without asking; annotated source: notes that add something; argument: two different cases and the real objection).
13. **Every section earns its place.** Its header says what it gives the reader, it does that, and it isn't there because the structure had a slot.
14. **The reader is carried.** For essays over about 1,500 words: bridges between sections (N4), and a map up front (N2) when there are more than three sections. A reader can tell where they are at any point.
15. **The turn is one line and the meaning line comes after.** Find them in the PARTS MAP. A turn announced ("Here's the twist") or a lesson stated before the material made it is a FAIL.
16. **Evidence is real and different.** Cases are not one case told twice; each has a number or a name.
17. **The other side is the real objection**, in the reader's words, where the structure calls for one.
18. **Promise kept.** Whatever the title, subtitle and promise line said, the body delivers it fully, and above the paywall if the post is paid and the promise is made to free readers.
19. **Length.** The plan's LENGTH is a guide, never a target: an essay shorter than the guide passes when every question is answered. Padding (a section restating the last one, a list stretched to a number) is a FAIL.
20. **Not a template.** The sections don't all have the same build (claim, example, landing line). The essay doesn't share its opening, closing line or section pattern with the person's last essays, if those are in the body of work index.
20a. **The chain holds.** Run the chain check in `skills/craft-copylosophy` ("The chain check") across the whole essay, one step per section move. Each fail it names (a shifted test or term, a group nobody defined, an example next to the claim, a claim taken back, a close that breaks the body) is one FAIL here, with both steps quoted.

### D. The close and the furniture

21. **Close is the one the brief chose**, or the draft says why not.
22. **The close is a close.** A resource list, a product plug or a paid-tier ask after the sign-off doesn't count as the close; something before it must end the essay.
23. **Paywall placement.** If paid: everything above `[PAYWALL]` is whole on its own, and the paywall doesn't sit at the turn or right before the list the title promised.
24. **Plugs follow the channel's selling rule.** None inside the body unless the channel file allows it, and none in place of the close.

### E. The writing rules

The house rules (`skills/craft-house-rules`) apply. Run `python3 scripts/check-prose.py <draft>` and `python3 scripts/voice-diff.py <draft>` first; fails go into the review, flags are evidence. On the piece's first judged draft, once `bank/voiceprint/profile.json` exists, also run `python3 scripts/voiceprint.py score <draft>` and put its VOICEPRINT block in the review (`skills/check-voiceprint`): a reading, never a fail by itself, and a revised draft isn't read again. When the draft holds Posts A, B and C, these scripts check each one on its own; the voiceprint reading runs once, on the draft you picked (`--draft A`, B or C). Read yourself for H1, H7, H8 and H24, and run the swap test: could another name go on this essay as it stands? If yes, FAIL as "not theirs".

When the piece was made from the person's own words (`--source`), voice-diff also flags two things. Under "sure where they weren't", a bound the person put on a claim ("usually", "in my experience", "might") that the draft dropped, a modal made stronger, a booster added or an "I" line turned general: each one is a line that states as settled what the person said with a bound, so the fix is to keep the bound or mark the line `inferred`. Under "their terms", a word of theirs swapped for another where the draft talks about the same thing: a FAIL under supplied copy and rule 3 when the term is theirs (quoted, coined, in the voice guide), and a flag to read when it's a name or a common compound.

When the draft holds three candidates, pick first, then judge, as the post judge's check 15b does: a quick pick on what decides it (the scripts' fails on each, the title's mechanism at check 1, the shape at check 11a, and which reads most like the person's own samples), one line on which and why, then every check in this file on the picked draft alone. Never merge them. If none of the three can pass, send all three back with what each needs.

The writing rules in `CLAUDE.md` apply. Each of these is a FAIL with the line quoted:

25. A line that breaks one of the house rules (`skills/craft-house-rules`), including a term used before it's explained. Name the rule. The bar test is applied as `skills/craft-human` ("How to apply the bar test") says.
26. Supplied copy changed (CLAUDE.md rule 3).
27. The writer is absent: the essay is facts about a subject with no first-person presence (what they did, found, think).
28. Anything the voice guide rules out, including its rules for essays.

### F. Honesty

These checks are graded as the gates table in `skills/role-editor` says, not by this section.

29. **No invented material anywhere.** Every number, name, quote, story and case about the person traces to an ID or a file in the source map; every case from outside their material is `borrowed: verify` with a source named. Lines marked `writer` are not invented (kinds: `CLAUDE.md` rule 1); check them for truth at 30. An essay with no `writer` rows at all is the person's entries restated; FAIL here.
29a. **Said fresh, not stitched (H34).** Run `python3 scripts/check-stitch.py <draft> --cap 4`; each line it names is a FAIL with the fix it gives. Then read for a teaching example of the person's presented as something they did or refuse, and for a section stretched from a fragment that doesn't carry it; the fix for the second is the cut. An essay stitched in three or more places is a redo, rewritten from the idea and the facts with the sources closed.
30. **Borrowed cases are checked against their source, and writer lines are true.** Every `borrowed: verify` item is checked as "Checking an outside case" in `skills/role-editor` says: open the source, compare each detail the essay uses, record what was checked where. Never mark a case checked from memory. A source quoted in an annotated-source essay is quoted exactly and credited. A `writer` row that states something false, or that the material and premises don't support, is a FAIL here.
31. **The argument holds.** Run the judge pass defined in `skills/craft-copylosophy` ("In the studio") on the finished essay. A `false` premise is a FAIL here. A `weak` premise is a FAIL in section C unless the essay states the condition.

### G. Reads like a person

32. **check-human passes.** Run `skills/check-human` (and `scripts/check-human.py` without `--detector` when a shell is available) on the picked essay. A `fix` verdict is a FAIL here ("Machine patterns" in the gates table), with the patterns and the quoted lines carried into this review. Whoever judges records the detector reading, from the "Detector" row of the gates table in `skills/role-editor`, which makes the one call (on the picked draft, `--detector --draft B`, first judged draft only); this check doesn't call it again. The label is recorded, never graded.

## Output

Before anything else: THE ONE THING, the deepest failing lever with the quoted line and the fix, as `skills/craft-refine` orders them (idea, legibility, concreteness, examples, analogy, frame, craft). On a pass, "none". The writer revises from this line, not from the full list.

```
VERDICT        pass / revise / redo
                Read the ladder top down; the first line that matches is the verdict.
                redo: any fail the gates table in `skills/role-editor` grades redo (a different idea at check 10, a wrong shape at check 11a, two or more body fails in C, an essay stitched in three or more places, and the gates it lists)
                revise: any other fail, title and opening craft and "promise kept" included
                pass: no fails. Notes that aren't fails never change the verdict
FAILS          numbered list: check number, the line or section quoted, what's wrong, the fix if obvious
ARGUMENT CHAIN the numbered steps from check 20a, with each fail marked on its step
OUTSIDE CASES  each borrowed case: checked against <link>, or not checked, with the details to confirm
PASSES WORTH NOTING   at most two, only when the draft does something the library's best essays do
```

Save it as `review-vN.md` in the piece's folder (save from `templates/piece/review.md`, or `review-direct.md` when the brief has `path: direct`), or give it in the reply if there's no piece folder. Return the verdict to the person, or to the draft stage for a second pass with the FAILS attached. On the second pass, judge again from the start; don't assume the fixes landed.
