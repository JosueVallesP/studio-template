# Editor notes on the role-editor run

Piece: `pieces/2026-10-22-two-clients-same-quarter`, draft v1. Verdict redo, no score. These notes are for the author of the skill, not for the writer.

## Files read

About 26 files or file sections. In order: CLAUDE.md, role-editor SKILL.md, brief, draft, channel file (linkedin.md), brand-strategy.md, voice-guide.md, stories.md, proof.md, povs.md, thesis.md, branches.md, stop-list.md, audience.md, vehicle.md and content-plan.md (grep only, to find C1), scoring.md, review template, log template, the piece log, the format judge stage, craft-human, craft-copylosophy (long, about 480 lines, most of it the writing-rules half the editor does not need), check-human SKILL.md, hook-moves.md (card header plus moves 4 and 11), body-moves.md (header, S3, M2, M9, C3, C4), the CSV rows for L104 and L142, and the check-human script's output. The read list in the skill is right but it is long for a 258-word post; craft-copylosophy alone is a quarter of the reading, and the editor needs maybe sixty lines of it (the engine steps 1 to 6 and the lens reference).

## Where the skill was unclear or contradictory

1. **The invented-material gate has one grade.** Every number, name, quote, story and claim must be in the source map and match its entry, or REDO. There is no grade between "matches" and "redo". This draft had one sentence that states a fact about the two S1 clients that S1 does not record ("Nothing in the monthly P&L had warned either of them"), and the writer's own source map flagged it as a general claim dressed as a fact. By the table that is a REDO of the whole piece with no score, for a line the writer could fix in a minute. I followed the table. Either the author means that (then say so, because it feels wrong in the moment and a softer editor will fudge it), or the gate needs a FIX grade for "a claim stretches a confirmed entry without adding a new fact", the way the format gate has A: REDO, B: FIX.

2. **No rule for a fact the approved brief asserts but the canon does not hold.** The brief's Outcome says the reader "understands why the monthly P&L showed nothing wrong" and the Fractal shape says "the monthly P&L shows it a quarter late (P1)". P1 says neither. The producer approved that brief. The skill says to ask the producer when "the brief itself is the problem", but it does not say what the verdict is meanwhile, whether the draft is penalised for following an approved brief, or whether the review should stop at the brief and not judge the draft at all. I failed the gate and sent the question up. Say which is wanted.

3. **The hook gate depends on a field the brief can get wrong, and this one did.** The format judge's check 1 judges the hook against "the move's mechanism sentence". The brief's plan said "HOOK MOVE 4, the finding that contradicts the dashboard": 4 is "put the reader in the room", "the finding" is move 11. The writer's log says they read it as 4; the hook they wrote is a move 11 shape. Against card 4 it fails check 1, which is REDO. Against card 11 it is a near pass with a weak-sample note. The whole A gate turned on which number I believed. The skill should say what the editor does when the brief's move label and gloss disagree (judge against the label, judge against the gloss, or stop and ask before running the gates). I judged against the label and flagged it.

4. **check-human has two homes.** `skills/check-human/SKILL.md` says to write `check-human.md` next to the draft. role-editor's output block has a CHECK-HUMAN section in the review and never mentions the file. The writer's log also says it ran check-human.py. I wrote it into the review only. Pick one, and say whether the editor's check-human run replaces the writer's or sits beside it.

5. **check-human's own pass rule is tighter than the editor's.** check-human: pass is "two patterns or fewer, each in one place". The editor's gate: fix is "check-human verdict fix", and craft-human says "three or more patterns is a fix". A draft with two patterns, one of them in two places, is a pass by craft-human and by the fix line, but not by check-human's pass line. That is this draft (pattern 6 in two places, pattern 4 once). I passed it. The three sentences should agree.

6. **Check numbers.** role-editor says "run check-human and copylosophy as the stage's checks 28 and 29 say". In judge.md, 28 is copylosophy and 29 is check-human. Right pair, reversed order. Trivial, but a reader who trusts the skill will look for copylosophy at 29.

7. **"Set the piece's status to reviewed" names no file.** The status lives in brief.md's frontmatter (the only place it appears). The writer put the draft's status nowhere either (draft-v1.md has no status field). Say "in brief.md".

8. **The review template's reviewer field asks for a version** ("role-editor <version>") and the skills carry none. The writer hit the same thing. Either version the skills or drop the field and point at CHANGELOG.

9. **The score section when a gate fails.** The template's Score table has four rows that must be filled or left blank. The skill says never score after a REDO gate. I left the scores as "not scored" and filled the weights and the "what it measures" column, so the writer has a bearing. Say whether the table should be removed or filled with weights only when there is no score.

10. **Review weights.** scoring.md says the channel file "may override them under Review weights". The channel file written by strategy-brand has no such section. Either strategy-brand should write one or scoring.md should not promise it. Defaults applied; I had to grep the channel file to be sure it was absent.

11. **The brief's EXAMPLES field pointed at the wrong posts** (L104 is a prediction-plus-argument, L142 a then-and-now list; neither is a story arc). The skill says "the library cards the brief names", which I read as the cards, so I did not judge against L104 or L142. If EXAMPLES are meant to be part of what the editor compares against, the skill should say so and the strategist should pick ones that match the structure.

12. **Severity vocabulary.** The template uses gate / should / could and the format judge uses PUBLISH / FIX / REDO, and the editor's verdict is pass / revise / redo. Three scales for one review. They map, but nobody wrote the mapping down (a FIX in the format judge is a "gate" row in the issues table with a "revise" verdict, I assumed).

13. **Order of the gates versus the format judge.** The skill lists nine gates, then says to run the format judge "in full" whose checks 2 and 26 are the invented-material gate again and whose 28 and 29 are two more of the gates. So the editor runs the same checks twice and has to decide which block owns the finding. I put each finding in the gates table once and repeated the quoted line in the format block, which is what the template's shape forces. A cleaner split: gates table owns fidelity, premise, permission, anti-association; format block owns A to D; check-human owns F.

## What I had to guess

- Whether an inference from a POV ("hiring ahead isn't the problem by itself", inferred from P4's "two quarters before" condition, against P4's rejects line) is an invented belief (gate) or a fidelity "should". I called it a should. The skill's rule 1 ("never invent... a belief") argues for the gate; the source map's reasoning argues for a should.
- Whether "cash months" with no canon definition is a gap to fill (the writer's reading) or a fact about her method the draft invented. I called it a gate fail because the definition the writer supplied is a real claim about how she measures, and it may not match R1. Rule 1 does not say what to do with a term the person uses that the canon never defines.
- Whether the C1 selling rule ("once or twice a month") is checkable. It is not from the piece files; it needs the other pieces of the month. I passed it and did not look.
- Whether the editor can read vehicle.md and content-plan.md to find C1. The read list does not include them; the source map cites C1 with no file. I grepped for it. The source map should carry the file for IDs outside the listed canon files, or the read list should include the vehicle.

## What worked

The read order was right: brief, then draft, then canon, then standards, then the cards. Reading the cards before judging made check 1 and check 8 decidable rather than taste. The source map made the fidelity pass fast and is where both gate fails surfaced; a draft without one would have taken twice as long. The "never rewrite" rule held well; the one-line fixes column kept me from drifting into drafting.
