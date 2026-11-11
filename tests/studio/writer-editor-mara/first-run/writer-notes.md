# Writer notes, test run on 2026-10-22-two-clients-same-quarter

For the author of `role-writer`. Blunt by request.

## Files read

About 27: CLAUDE.md, role-writer SKILL.md, brief.md, log.md, channels/linkedin.md, voice-guide.md, stories.md, proof.md, povs.md, thesis.md, branches.md, audience.md, fmt-linkedin-post SKILL.md, stages/draft.md, hook-moves.md (the header, cards 4 and 11, the pilot notes), body-moves.md (header, S3, M2, M9, all six closes, the sort notes), content-moves-sorted.csv (rows L104, L142, then L008, S012, L105, L143, L189 on my own), craft-human SKILL.md, craft-copylosophy SKILL.md (all 395 lines, most of it the method's standalone chat flow), templates/piece/draft.md, log.md, brief.md, README.md, scripts/check-human.py, studio-notes.md. Plus two directory listings. The copylosophy file alone is about a third of the reading and most of it (entry points, interview questions, output format with belief-gate question to "the user") doesn't apply to a writer working from a brief.

## Where the skill or its inputs were unclear, wrong or missing

1. **The brief's hook move contradicted itself and the skill has no rule for that.** Format plan said `HOOK MOVE 4, the finding that contradicts the dashboard`. Card 4 is "Put the reader in the room". "The finding" is card 11. I went with the number, because the plan's STRUCTURE (story arc) pairs with 4 and card 11 pairs with the argument, and because S1 is a story, not a study. That's a guess the editor can't see unless they read the log. The skill should say which wins when a plan's number and name disagree, or tell the writer to block.

2. **The plan's EXAMPLES were useless and the skill says to read them.** L104 is a bet-on-the-future argument with a restated-principle close; L142 is a proof-then-payoff bare list. Neither is a story arc or move 4. I read them as told, got nothing, and pulled L008, S012, L105, L143 and L189 myself. The skill should let the writer swap examples when the plan's don't match the move and structure, and say so in the log.

3. **The draft stage promises "full text of the example posts, last column" of the CSV. The last column is a LinkedIn URL.** The only text is the `Hook` column, one or two lines. So "read the full text of the example posts" can't be done from the repo. Either the CSV needs the text or the stage needs to stop promising it.

4. **The channel file is `status: draft` and nothing says whether a writer may read a draft strategy file.** Rule 2 in CLAUDE.md covers canon *entries* (material). `channels/linkedin.md` is strategy, unconfirmed, and it decides the CTA and the word ban. I used it. The skill's precondition list should say whether a draft channel file blocks the piece or not. I'd say no, but it should be written down.

5. **Copylosophy trigger is ambiguous for a story post that carries OPINION lines.** The skill says run steps 1 to 10 "when the piece argues (an OPINION or PATTERN line carries it, or the structure is an argument)". This piece has two OPINION lines in its material but the story carries it. Steps 1 to 10 as written include research (step 4), a belief gate addressed to "the user" (step 9), and a chat output format with a question at the end. None of that fits a writer running alone from a brief. I ran the short version plus the hidden-premise and lens work and wrote it into the draft file. The skill should define a writer-sized copylosophy pass (claim, premises, lenses, refined thesis, trace to a POV) in ten lines and stop pointing at the whole method.

6. **Where the copylosophy output goes is contradictory.** `stages/draft.md` says "Write the refined thesis into the brief's fractal shape". `role-writer` says the strategist owns the brief and the writer drafts "only from the brief". If the writer edits the brief, the editor can't tell what the producer approved. I left the brief alone (the thesis didn't change anyway) and put the run in the draft file. Pick one.

7. **The brief carried two inferences that aren't in the canon, and the skill doesn't say what to do with a brief line that outruns its source.** "The monthly P&L shows it a quarter late (P1)": P1 says nothing about a quarter. "A weekly cash view would have shown it months earlier": no entry says that; S1 says both run the view *now*. I didn't use either number. The skill's "never add a claim ... that isn't in the brief's material" covers the writer's additions, not the brief's own stretches. It should say: a brief line is only as good as the entry it cites; if the line goes further than the entry, use the entry.

8. **"Read the entries, not the summary; the person's exact words live in the `quote` fields."** Only T has a `quote` field. S1, R1, P1, P4 have `what:` and `claim:` fields in the third person ("Two clients, both growing..."). So "keep the person's words as written" is unworkable for most material: the entries aren't in her voice, they're the interviewer's notes. I paraphrased S1 and R1 into first person and kept T verbatim. The skill should say which fields count as "her words" and which are notes you may rephrase.

9. **R1's wording breaks the voice guide.** R1 says "cash runway"; W2 says never "runway". Rule 3 says keep her words. I followed W2 and wrote "months of cash". The skill names this kind of conflict only as voice guide vs channel file; it should also cover voice guide vs a canon entry's wording.

10. **The CTA rule needs a fact the writer can't check.** Channel file allows C1 "at the end of a B1 piece once or twice a month". The brief says use C1 "only if the channel file's selling rule allows a CTA this early". I don't know how many B1 pieces this month already carried C1 (none exist, so I used it). The skill should say where that count lives, or make the brief carry the decision instead of handing a conditional to the writer.

11. **Preconditions say the material entries must exist with `status: confirmed`, but say nothing about the parent and the segment and the desire.** I checked B1, G1 and D1 anyway. Say whether to.

12. **The output template and the format stage output don't fit together.** `templates/piece/draft.md` has "<The piece.>" then a source map. The draft stage wants HOOK OPTIONS, POST, CLOSE ALT and PARTS MAP. The skill says to save "with the format stage's output blocks". I put the stage block inside the template and added the copylosophy run above it. `check-human.py` then measures the whole file (hook options, analysis and all) and flags "no speaker in the opening" because the opening is my copylosophy notes. On the post alone it passes clean. Either the template needs a marked POST section the script reads, or the skill should tell the writer to run the script on the post only.

13. **"Skill versions" has nowhere to come from.** The log and draft templates ask for skill versions. No skill file carries one; CLAUDE.md gives the repo version only. I wrote "unversioned; repo v0.6".

14. **Voice guide W1 "numbers spelled plainly" is ambiguous.** Digits or words? "60 percent" or "60%"? I wrote "60 percent", "two months", "2.8 to 5.1". If she means something else the editor will fix it, but a guide line that needs guessing isn't a guide line.

15. **Move 4 needs "one or two specific details you remember exactly"; S1 has none of that kind.** No time of day, place, line of dialogue. The hook had to make do with a quarter, a number and the founder loan. The moves stage approved move 4 on material that only just clears its own gate. Not the writer's call, but the writer pays for it.

16. **Smaller things.** The log template's date is the action date, but the test brief is dated 2026-10-22 and today is 2026-10-21, so the log now runs backwards. The skill says "Say in one line what's next" without saying where (I put it in the log line). `studio-notes.md` wants "one line"; mine is long because the run had several guesses, and one line per guess would have been clearer as a rule.

## What I guessed, in short

Hook move 4 over 11. Examples swapped. Draft channel file is fine to read. Copylosophy short run, written into the draft file, brief untouched. Brief inferences beyond their sources dropped. "Runway" replaced with "months of cash" against R1's wording. C1 used because no earlier B1 piece this month exists. Digits for 60 percent and 2.8 to 5.1. Cash months defined as cash divided by a normal month's outflow (plain arithmetic, no canon entry; flagged in the source map).
