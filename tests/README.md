# Tests

Rerun the tests after any change to a skill or a library card. A change that makes the results worse gets reverted.

`bash scripts/test-all.sh` runs every automated suite in one go (the house-rule set in `tests/prose/`, `hooks/`, `rewrites/`, `house-rules/`, `drafts/`, `stitch/` and `packet/`). The update job runs it before a new version goes to any client and stops if anything fails. The other tests here are run by hand, by a person or an agent following each README.

- `tests/studio/`: the studio's own test set, owned by the studio and replaced on update.
- `tests/client/`: a person's own test briefs, never touched by an update.

Each test is a folder with a `README.md` that says what to stage, what to run and the properties the output must have. Most also have a `first-run/` folder with the files the first run produced, kept as a record to compare against; a few keep a `reference-run/` instead or as well. Some hold their inputs beside the README (a brief, an `inbox/`, an idea bank, a filled-in form). The files in `first-run/` and `reference-run/` are records of past runs and aren't edited when the studio changes.

The tests in `tests/studio/`:

- `strategy-brand-mara/`: a complete fictional minimum canon that `strategy-brand` runs against.
- `writer-editor-mara/`: an approved brief with two deliberate defects that `role-writer` and then `role-editor`, in a fresh context, must handle.
- `strategist-mara/`: three raw ideas, one of them a trap, for `role-strategist` to shortlist and brief.
- `capture-mara/`: a call transcript and a voice memo with five planted cases for `role-capture`.
- `librarian-mara/`: a shipped piece with the person's edits, a ledger and repeated studio notes for `role-librarian`.
- `welcome-tomas/`: a fresh instance taken through `/start` and the first brand tree session by a fictional person who publishes nothing and has his material on a drive.
- `intake-form-lena/`: a filled-in intake form built into an instance, then `/start` and the first interview session.
- `intake-claude-marco/`: a bare install taken through intake inside Claude.
- `quickstart-dana/`: a buyer from the Tally form through the quick wins and the first post.
- `readback-josue/`: the read-back on a real body of work; the checks only, since the run's notes describe private material. Kept in the studio repo only; it doesn't ship to clients.
- `rewrites/`: five tagged rewrite pairs and a review, for `scripts/rewrites.py`: the order the writer reads pairs in and the tally `/end` gives. Run with `python3 tests/studio/rewrites/run.py`.
- `voiceprint/`: `scripts/voiceprint.py` on six writers' essays it hasn't seen, with the numbers a change must keep. Uses the essays in `skills/fmt-substack-essay/library/essays/`.
- `argument-chain-chess/`: a real post that passes line by line but not as an argument; the judge's chain check, one-idea check and outside-case check must send it back as `redo`.
- `hooks/`: one tool-call payload per file for the write and command guards, with `run.sh` to check every decision.
- `house-rules/`: the house rules a script can decide, one short passage per case, each with what it must do. Run with `python3 tests/studio/house-rules/run.py`.
- `drafts/`: a draft with Posts A, B and C, where only B breaks the rules, so each check script must report the three separately. Run with `python3 tests/studio/drafts/run.py`.
- `stitch/`: a fake transcript, a post that lifts one of its sentences unmarked, and the same fact said fresh; `scripts/check-stitch.py` must fail the first and pass the second. Run with `python3 tests/studio/stitch/run.py`.
- `sync-config/`: the dashboard syncs' config reader against a sample `config/tools.md`: keys with spaces come back, a "not yet" placeholder reads as unset, and both syncs say why they stop. Run with `python3 tests/studio/sync-config/run.py`.
- `packet/`: builds the writer's packet from a brief and checks it holds the sheet, the brief, only the named cards, the type's draft step and the voice. Run with `python3 tests/studio/packet/run.py`.

Still to come: about 20 briefs for the LinkedIn post chain, drawn from the sorted library and approved by the studio's author, and essay test briefs.
