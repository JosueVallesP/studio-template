# Test: the librarian

Builds on the other four tests. Stage the state like this: the fictional canon from `../strategy-brand-mara/canon/`; the piece from `../writer-editor-mara/` with its first-run draft, marked `shipped`, with `state/final.md` as the final (the person cut two hedges, put her own definition of cash months in, changed "13-week cash view" to "13-week view", and restored "before Monday") and `state/producer-log-line.md` appended to its log; the idea bank and evidence ledger as `../capture-mara/` leaves them (the ledger holds capture's lines plus one earlier `voice edit` line of the same kind); the Monday call as a `draft` method entry under B1, which the main session added from capture's report (it was asked for by the person); and `studio-notes.md` with the lines from the earlier runs, where two roles report the same missing file.

Run `role-librarian` part A. Check:

- The diff against the last draft is read whatever its review verdict was, and every change is sorted: the two cut hedges as `voice edit`; the cash months definition as a `definition`; "Monday" as no line (it only brings the piece back to the brief); the kept P4 line ("Hiring ahead isn't the problem by itself") as a `contradiction`, because it goes against P4's `rejects` field.
- The voice edit reaches the threshold (two cuts plus the person stating the rule in her log line) and becomes a proposed voice rule, quoting her reason.
- The cash months definition becomes a `definition` proposal with the call and the final as dated evidence (B1 names the term without saying what it means). The Monday call's second mention is listed under "Drafts to add" in `pieces/librarian-last-run.md` as a new quote and source for the existing draft, never as a proposal; the librarian writes nothing in `canon/`.
- The P4 contradiction becomes a proposal that asks which is right, with any field she never worded marked `[librarian's wording]`.
- Items below threshold stay in the ledger with how many more mentions each needs; nothing is proposed from one mention; no more than five proposals are open.
- `status: used` and `used_in` are set on the idea bank entries whose words the final carries, including ones the brief didn't cite. Expired outside entries are left for `/tidy`.
- The index is rewritten and notes that the piece shipped over a redo verdict.
- `studio-notes.md` gets a "Proposed skill fixes" section that groups repeated guesses by skill and marks as done the ones the current skill text already fixed.
- The summary names the proposal that matters most for the quarter and goes to `pieces/librarian-last-run.md` when nobody is in the room.

`first-run/` holds the first run's proposals, ledger, studio notes, summary and notes, before the fixes in 0.9.0. That run got the four proposals right and found the gaps: "twice" was undefined, repeat and contradiction overlapped for a kept stretch, the ledger had no kinds for what steps 2 and 5 asked for, the producer and the librarian both claimed the final's evidence lines, and the skill-fix criteria missed a contradiction between two skills.

This run predates 0.34; its files use the old paths and letters.
