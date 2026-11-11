# Test: writer and editor on one piece

Uses the fictional canon in `../strategy-brand-mara/canon/` plus the strategy outputs from that test's reference run. `piece/brief.md` is an approved brief for a LinkedIn post built on story S1, with two deliberate defects that the first run exposed and the skills now handle:

- The format plan's hook move label (4, put the reader in the room) and its description ("the finding", move 11) disagree.
- Two brief lines outrun their cited entries ("the P&L shows it a quarter late (P1)"; "a weekly cash view would have shown it months earlier").

The brief is an older one: its format plan has no QUESTIONS or SHAPE line. Run `role-writer` on the brief (the `writer` agent: it builds `packet.md` with `python3 scripts/packet.py pieces/<id>` and reads the packet, the writer's sheet and the draft stage, nothing else), then `role-editor` in a fresh context (the `editor` agent, which has not seen the writer's work). Check:

Writer:
- Builds the packet and drafts from it; doesn't open the libraries or the example posts.
- Adds the missing QUESTIONS and SHAPE lines from the moves stage's steps 2 and 3 and says so under `## Brief defects`, changing nothing else in the brief.
- Drafts to the plan's card number (4, put the reader in the room), not the description ("the finding", move 11), and logs the mismatch under `## Brief defects`.
- Says under `## Brief defects` that the plan's examples (L104, L142 are not story arcs) don't match the move and structure, and drafts from the cards in the packet.
- Drops the brief's two stretched lines and uses the entries instead, writing each gap under `## Brief defects`.
- Keeps T's quote verbatim; restates S1 and R1 in first person; writes "months of cash", not "runway" (W2).
- Does not define "cash months" in the post; writes the missing definition to `proposals.md` as a question.
- Does not state what the two clients' P&L showed; S1 doesn't record it.
- Drafts the no-CTA close as the post and C1 as CLOSE ALT, because the brief handed it a conditional.
- Writes three drafts under `## Post A`, `## Post B` and `## Post C`, each holding only its post; `python3 scripts/self-check.py` passes on each; status set to `drafted` in brief.md.

Editor:
- Reads `## Brief defects` with the draft and judges the hook against card 4, the card number; files the label/description contradiction as a brief defect, not a writer fail.
- Picks one of Posts A, B and C in one line, then runs the full checks on that one.
- Fidelity gate: no new fact, no stretch (if the writer did its job). Where a stretch exists, grades it revise, not redo.
- Passes check-human with at most two patterns, none in more than two places.
- Every grade and the verdict (pass, revise or redo) come from the gates table in `role-editor`; the review opens with THE ONE THING and carries no score.
- Sets `status: reviewed` in brief.md; nothing written twice across the gates table, the format block and check-human.

`first-run/` holds the first run's draft, review and both agents' notes, before the 0.6.1 fixes. That run ended in a redo on two gates (a stretched P&L sentence, an invented definition of cash months) and a hook judged against the wrong card; all three are now rules.
