# Test: the welcome path

A fresh instance made with `scripts/update-studio.sh . --init`, with nothing in `canon/`, taken through `/start` and the first brand tree session by one agent playing both the studio and a fictional person: Tomás Reyes, a landscape architect in a mid-sized city who publishes nothing, has two conference talks and a folder of proposals on a drive (not in hand), wants two or three plaza or park commissions a year from the content, has about three hours a week, and uses neither Notion nor Figma. He has one firm opinion (a plaza should be designed to be used, not to be photographed) and one forming one (the aerial render is the wrong question), and one dated client story behind the first.

There is no brief. The test is the two front-door skills themselves. Run `/start` and then "start my brand tree" with a person like Tomás and check:

- `/start` says the welcome in `docs/welcome.md` once, in plain words, says "your files" and never "canon", asks him nothing, doesn't ask about Notion or Figma, and ends on the one next step said as a phrase ("say 'set up my studio'"). The intake (`setup-intake`) then asks the questions in `docs/intake-questions.md`, the year-from-now goal and the hours among them. When `/start` reaches the interviews, it says the first session ends with one to three things written down, not a tree.
- `canon/strategy/outcomes.md` holds his goal answer word for word, with `measured by` from his own words and the hours under Capacity. `config/tools.md` has no copying instruction left in it. `canon/setup-progress.md` has one log line for the session.
- The brand tree skill doesn't explain the studio a second time; it says only the two new things (voice, pushback) and goes to intake.
- Intake Q2 doesn't read a nine-item list. When he says the talks are on a drive, the studio routes on what's in hand, writes "bring the two talks" into the next session's plan, and takes the story he offers now.
- The session plan in `progress.md` swaps sessions 2 and 3 for a POV start.
- Exactly 20 files are created by setup-brand-tree step 5 (15 in `canon/`: `progress.md`, `canon-index.md`, the seven `person/` files, `bank/stories.md` and `proof.md`, `vehicle/vehicle.md`, `strategy/brand-strategy.md` and `audience.md`, `voice/voice-guide.md`; and 5 in the top-level `bank/`: `ideas.md`, `credibility.md`, `questions.md`, `evidence.md`, `rewrites/README.md`), none of them `content-plan.md`, `channels/` or `core-summary.md`; the template example blocks are stripped; "what's known" means the goal copied into `vehicle.md` as draft, the capacity into Constraints, intake under "About them" in `progress.md`, and the two client types as draft segments. Nothing else is drafted.
- P1 is confirmed in his words after his correction ("used", not "sat in"), with limits (ceremonial squares) and what it rejects. P2 stays open, and the studio says what that means for him rather than the label "forming".
- S1 is read back (what, result, permission) and confirmed in the same session, not left draft.
- The permission question is "with names, without names, or not at all".
- No "which value is that from?" question of someone with no values written down.
- The studio acknowledges by restating what it captured, not with "Noted." and "Changed." in a row.
- The ending says the files are in `canon/`, names what to bring, and gives "continue my brand tree"; it doesn't ask him to share or upload files sitting in his folder.
- `bash scripts/status.sh` afterwards shows the drafts he has (P2, S1, the goal, two segments), not 14.

`first-run/` holds the first run, before the fixes in 0.11.0: the transcript, the agent's notes to the skills' author, the canon and config it created, and the five studio notes. That run explained the studio twice, asked the goal question in two skills, asked a tools question with no consequence, had no branch for "material exists but isn't here", left a fully told story as draft, created 17 files by guess and showed 14 drafts in `/status` where there were 3.

This run predates 0.34; its files use the old paths and letters, and it predates the welcome in `docs/welcome.md`, so its transcript shows `/start` asking questions that the intake asks now.
