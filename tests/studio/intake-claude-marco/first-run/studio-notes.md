# Studio notes

One line per place a skill made a run guess, from any role, any run. Format: date · skill · what was unclear. The studio's own loop: these feed the next version of the skill, and the test set gets rerun after the fix.


- 2026-10-22 · setup-intake · Q4 joins location and language in one question; the person answered only the city. The skill allows follow-ups only "to make an answer usable", and a blank language is usable, so language stayed blank with no follow-up. Guess: whether a half-answered double question counts as "already given".
- 2026-10-22 · setup-intake · Q11 (material) and Q12 (recordings) overlap when the person's material is video of themselves talking. Guessed to record the videos under both fields; YOUR-STUDIO.md then listed them twice.
- 2026-10-22 · setup-intake · Q18 asks for three references "with links or uploads" and "one line each on what you like about it". The person gave two names and no reasons. Guessed not to follow up (the skill bans follow-ups except for usability) and not to ask for a third.
- 2026-10-22 · setup-intake · Q15 to Q17 say "Upload". There is no upload inside Claude Code. Guessed to say "drop the file in inbox/" instead, which step 4 says for material but not for the look.
- 2026-10-22 · setup-intake · Step 6 says fix "only wording; never the facts" in YOUR-STUDIO.md. Guessed how far that reaches: collapsed the duplicated feeds list into one sentence and turned "Instagram (I hate it)" into "which you said you hate" so the sentence stays in the second person. Both touch his words.
- 2026-10-22 · setup-intake · build-instance.py wrote "nobody else touches the content" from a blank team answer, against "Never fill a blank with a guess". Guessed to leave it, because step 6 only lets the skill fix YOUR-STUDIO.md.
- 2026-10-22 · setup-intake · build-instance.py --fill does not write intake_date into config/intake.yaml (it only rewrites the yaml when the answers file is a different path). Template says the build fills it. Guessed to leave it blank rather than hand-fill.
- 2026-10-22 · setup-start · Material named in intake but not in inbox/: the skill says "name it and ask them to drop it in". A handwritten notebook can't be dropped in. Guessed to ask him how he wants to get it in, which is a question the skill didn't give me.
- 2026-10-22 · setup-start · Step 3 says "On the first session ... write one log line, not two". For the second session it says nothing about how many lines; guessed one.
