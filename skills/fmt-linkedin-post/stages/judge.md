
# Content judge

Input: the draft (with its SKELETON, PARTS MAP and source map if it came from the draft stage) and the piece's `brief.md`. If there is no brief, build the minimum one first: the one idea the draft is carrying, which hook move it's attempting, which shape, which close. State those assumptions at the top of the verdict.

Library files:
- `../library/hook-moves.md`
- `../library/body-moves.md`

Read the cards for the hook move and the shape before judging. Judge against the card, not against your taste. If the format plan names a TYPE, read `../types/<type>.md` and run its "Checks the judge adds" as extra checks after section A. Each takes its grade from the gates table in `skills/role-editor` ("Format: type checks"): a check that names a gate there takes that gate's grade (a borrowed fact with no source and no hedge is "Outside example unverified"; a proof post with no real result is "Invented material, new"), and the rest are revise. Leave the draft's `## Argument check` unread until your own premise verdicts at check 20 are written; then note where the writer's verdicts differ.

## How to judge

Each check gets PASS or FAIL. A FAIL names the line and says what is wrong in one sentence, using the card's language. Do not soften a fail. Do not rewrite the post; give the fix for the one line, and only when the fix is obvious.

The judge is a different pass from the draft on purpose. If you wrote the draft, you are not the judge.

## Checks

### A. The hook does the move's job

1. **Mechanism.** Read the move's mechanism sentence. Does this hook do that? (Proof-then-payoff: does the proof earn the payoff? The line someone said: is it verbatim and is the response unexpected? The common advice is wrong: is it advice the audience follows? The reframe: does the new lens explain more than the old one?)
2. **Material is real.** Every number, name, client, quote, result, story and date about the person in the hook comes from MATERIAL in the brief or the material files it cites. Anything about the person not in those is invented. FAIL and name it. A line the source map marks `writer` or `borrowed: verify` (kinds: `CLAUDE.md` rule 1) is not invented; check it under 19 and 20 instead. A stretch (a claim beyond what its entry records) fails 18, not this check.
3. **How it fails.** Go down the move's "how it fails" list. Each item is a check. Name any the draft trips.
4. **Works before "see more".** The first one to three lines make the promise on their own.

### B. The body keeps the promise

5. **The shape fits the idea.** Do this before reading the plan's QUESTIONS or the draft's SKELETON. Read the post as a stranger and write down the questions it raises, in order, and where each gets answered. Then compare with the plan and the skeleton. Three ways to fail:
   - **A question left hanging.** The idea needs it answered and the post doesn't answer it. FAIL, quote where it's raised.
   - **Padding.** A paragraph that answers no question the reader would have, or answers one the idea doesn't need. FAIL, quote it; the fix is the cut.
   - **The wrong shape.** The idea would be clearly easier to get in another shape (a list that's really one argument split into items; a story where the reader needed to be argued out of something; three paragraphs where one sentence would do). FAIL only when you can name the other shape and say in one sentence why it reads more clearly for this reader. This fail is a redo ("Format: wrong shape or different idea" in the gates table). A post that changed the plan's shape and says why in Brief defects is judged on whether the change was right, not on the change itself.
   - **The questions on the page.** The post sets out the reader's questions and answers them in turn (questions as headers, "Why? Because..." pairs, a run of questions it then answers). The questions shape the post; the reader shouldn't see them. FAIL, quote the lines; this is a revise.
   The idea sentence the reader would repeat should match the brief's one idea. If the post carries a different idea, that's a redo too.
5b. **It does its job for its reader.** Read the brief's one real reader and Outcome, then the post as that person. Would they come away thinking, feeling or doing what the Outcome says? FAIL when the post speaks to someone else (examples, objection or level of detail that fit a different reader) or stops short of the Outcome; quote the line where it turns away. A post written for a different reader is a redo; one that stops short is a revise. A brief with no named reader (older pieces) skips this check.
6. **Each beat is there.** Every beat in the skeleton shows up in the post, and the parts the shape's card names are present where the beats need them (an argument the reader would push back on needs the other side; a story needs a complication before the turn; a breakdown needs the context its parts use). A card part the beats left out with a reason in Brief defects passes.
7. **The turn is one line.** Find it (PARTS MAP). If it is announced ("Here's the twist:") or spread over a paragraph, FAIL.
8. **The meaning line comes after, and is no bigger than the story.** If the lesson is stated before the material has made it, or claims more than the material shows, FAIL.
9. **Evidence is two different things,** when the post argues. Not one case told twice. Each has a number or a name.
10. **The other side is the real objection,** when the post takes one on: the strongest version of it, in the reader's words.
11. **Promise kept.** Whatever the hook promised (a formula, 7 steps, the exact test, what happened), the body delivers it, fully.
11a. **One idea, carried whole.** State the post's idea in one sentence with no "and". Every line serves it, and the post gives that idea every step it needs. A post that holds the conclusions of several ideas without the steps that join them is a shrunk essay or a shrunk talk: FAIL, and name the idea the post could carry alone. When the brief has `adapted_from:`, compare with the source: the post should hold one of its ideas, not a summary of all of them (`skills/job-adapt`, "One idea per piece").
11b. **The chain holds.** Run the chain check in `skills/craft-copylosophy` ("The chain check"). Each fail it names (a shifted test or term, a group nobody defined, an example next to the claim, a claim taken back, a close that breaks the body) is one FAIL here, with both steps quoted.

### C. The close

12. **Close is the one the brief chose**, or the draft says why not.
13. **Not the restated principle by default.** If it is the restated principle, the brief gave a reason.
14. **Nothing after the end.** No second close, no stacked asks (follow, repost, link), no P.S. that is a pitch.

### D. The writing rules

The house rules (`skills/craft-house-rules`) apply. Run `python3 scripts/check-prose.py <draft>`, `python3 scripts/voice-diff.py <draft>` and `python3 scripts/check-stitch.py <draft>` first; the script's fails go straight into the review, its flags are evidence to read. On the piece's first judged draft, once `bank/voiceprint/profile.json` exists, also run `python3 scripts/voiceprint.py score <draft>` and put its VOICEPRINT block in the review (`skills/check-voiceprint`): a reading, never a fail by itself, and a revised draft isn't read again. When the draft holds Posts A, B and C, these scripts check each one on its own; the voiceprint reading runs once, on the draft you picked (`--draft A`, B or C). When the piece was made from the person's own words (`--source`), voice-diff also flags two things. Under "sure where they weren't", a bound the person put on a claim ("usually", "in my experience", "might") that the draft dropped, a modal made stronger, a booster added or an "I" line turned general: each one is a line that states as settled what the person said with a bound, so the fix is to keep the bound or mark the line `inferred`. Under "their terms", a word of theirs swapped for another where the draft talks about the same thing: a FAIL under supplied copy and rule 3 when the term is theirs (quoted, coined, in the voice guide), and a flag to read when it's a name or a common compound. Each of these is a FAIL with the line quoted:

15. A line that breaks a house rule. Name the rule (H-number). The bar test is applied as `skills/craft-human` ("How to apply the bar test") says. Four the scripts can't see, read for them yourself: H1 (an image or analogy that performs where the point was already clear), H7 (a verdict with no why), H8 (the central idea never stated in one plain sentence), H24 (a reaction, feeling or habit of the person's that no source gives).
15a. **The swap test.** Could another name go on this post as it stands? If yes, it was generated, whatever else it passes. FAIL as "not theirs".
15b. **Three drafts.** When the draft file holds `## Post A`, `## Post B` and `## Post C`, pick first, then judge. The pick is quick and reads each draft only for what decides it: the scripts' fails on each (they already run draft by draft), the hook's mechanism (check 1), the shape and the questions (check 5), and which reads most like the person's own samples (`material/`, their side of `bank/rewrites/`). Say which and why in one line. Then run every check in this file on the picked draft alone; the verdict, the fails and THE ONE THING are about that draft. If the pick shows that none of the three can pass (each fails check 5, or each carries invented material), send all three back with what each needs; never merge them yourself.
15c. **Not a template.** Read the `final.md` of the person's last six shipped posts (`pieces/index.md`, newest first; fewer if they have fewer). FAIL when the draft repeats one of them in a way a regular reader would notice: the same opening words or the same opening build (a question, a one-word line, "I used to think"), the same closing line or sign-off, or the same hook move and structure as two of the last three. Quote the draft line and the earlier one. A repeated move is fine when it's carried by new material and opens and closes differently; what fails is the reader recognizing the pattern before the content. The person's own signature lines, quoted from their material or voice guide, are theirs and don't fail here. When Posts A, B and C are in the file, also FAIL 15b if two of them share their opening build or their close: three drafts are only worth judging when they differ.
16. Supplied copy changed (CLAUDE.md rule 3).
17. The writer is absent: facts about the subject with no first-person presence (what they did, found, think).

### E. Honesty

These checks are graded as the gates table in `skills/role-editor` says, not by this section.

18. **No invented material anywhere in the post.** Same as check 2, for the body. Then look at the source map as a whole (kinds: `CLAUDE.md` rule 1): if every row is `verbatim` or `said again` and nothing is `writer`, the post is the person's entries restated, not a post. FAIL as "no reasoning of the writer's own".
18a. **Said fresh, not stitched (H34).** Run `python3 scripts/check-stitch.py <draft>`; each line it names (a run of the source's words not marked `verbatim`, or the cap over) is a FAIL with the fix it gives. Then read for the two it can't see. A teaching example presented as the person's own act: the material shows them using a case to explain a point (a workshop example, a figure they gave to illustrate, a client's situation) and the post has them doing or refusing that thing themselves; FAIL, quote both, and the fix is to say what it is or cut it. A stretched beat: a line whose cited source carries less than the line claims, or a beat that exists only because a fragment was lying around; FAIL, and the fix is the cut, never a bigger claim. A post stitched in three or more places (the collage reads: each paragraph in a different register, sourced lines with frames around them) is a redo: the writer rewrites from the idea and the facts, reading the sources closed.
19. **Borrowed stories and documents are checked against their source, and writer lines are true.** Every `borrowed: verify` row is checked as "Checking an outside case" in `skills/role-editor` says: open the source, compare each detail the post uses, record what was checked where. Never mark a case checked from memory. A `writer` row that states something false, or that the material and premises don't support, is a FAIL here.
20. **The argument holds.** Run the judge pass defined in `skills/craft-copylosophy` ("In the studio") on the finished post. A `false` premise is a FAIL here. A `weak` premise is a FAIL in section B unless the post states the condition.

### F. Reads like a person

21. **check-human passes.** Run `skills/check-human` (and `scripts/check-human.py` without `--detector` when a shell is available) on the picked post. A `fix` verdict is a FAIL here, with the patterns and the quoted lines carried into this review. Whoever judges records the detector reading, from the "Detector" row of the gates table in `skills/role-editor`, which makes the one call (on the picked draft, `--detector --draft B`, first judged draft only); this check doesn't call it again. The label is recorded, never graded.

## Output

Before anything else: THE ONE THING, the deepest failing lever with the quoted line and the fix, as `skills/craft-refine` orders them (idea, legibility, concreteness, examples, analogy, frame, craft). A wrong shape or a hanging question is a legibility fail. On a pass, "none". The writer revises from this line, not from the full list.

```
VERDICT        pass / revise / redo
                Read the ladder top down; the first line that matches is the verdict.
                redo: any fail the gates table in `skills/role-editor` grades redo (a wrong shape or a different idea under check 5, two or more body fails in B, a post stitched in three or more places, and the gates it lists)
                revise: any other fail, hook-craft fails in A included
                pass: no fails. Notes that aren't fails never change the verdict
FAILS          numbered list: check number, the line quoted, what is wrong, the fix if obvious
ARGUMENT CHAIN the numbered steps from check 11b, with each fail marked on its step
OUTSIDE CASES  each borrowed case: checked against <link>, or not checked, with the details to confirm
PASSES WORTH NOTING   at most two, only when the draft does something the library's best posts do
```

Save it as `review-vN.md` in the piece's folder (save from `templates/piece/review.md`, or `review-direct.md` when the brief has `path: direct`), or give it in the reply if there is no piece folder. Return the verdict to the person, or to the draft stage for a second pass with the FAILS attached. On the second pass, judge again from the start; do not assume the fixes landed.
