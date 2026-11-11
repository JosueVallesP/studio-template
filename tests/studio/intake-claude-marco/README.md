# Test: a bare install, intake inside Claude, then /start again

A bare instance from `update-studio.sh --init` and a fictional person who did not fill in the form: Marco Bellini, a woodworker in Bologna who teaches furniture workshops, a small YouTube channel, an Instagram he hates, five hours a week, no Notion, no Figma, no logo, material on paper and in 40 videos, wants his workshops filled a year out.

Run `/start`, then "set up my studio" (`setup-intake`) answering as Marco, then `/start` again, with one agent playing both sides. Check:

- The first `/start` explains the studio once, says the road as `docs/welcome.md` gives it (and, only if he asks how long it takes, both numbers: a week or two to set up, then a month or two before the content works in a real way), glosses "brand tree", says "where things are and a one-page guide" rather than "settings", and ends with "say 'set up my studio'".
- Intake is the ten questions in `docs/intake-questions.md` less the GitHub question (nine inside Claude), counts down instead of naming groups, skips any question he already answered, asks for the missing language in a few words, asks him to paste his material or drop files in `inbox/`, tells him paper gets photographed or typed and video needs a transcript, and never promises colors.
- `config/intake.yaml` ends with `intake_date` and `built_by` filled in by the script in `--fill` mode; a note with a `#` in it survives the parser.
- The hand-back is three lines, names the quick wins in `/start`'s order (the one page, Figma and Notion only if wanted, the libraries, the first post), and `/start` in the same session adds nothing about what exists; it goes straight to the stage and the one next step.
- `YOUR-STUDIO.md` has no run-on list sentences and its setup section is rewritten by `/start`.
- `bash scripts/status.sh` prints the stage first and no "missing"; `bash scripts/setup-check.sh` ends with "the install is fine" and no FAIL.

`first-run/` holds the first run, before the fixes in 0.12.0: the transcript, the agent's notes, the intake file and guide the script wrote, and the studio notes.

This run predates 0.34; its files use the old paths and letters, and an intake of fourteen questions.
