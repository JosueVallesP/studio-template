# Test: the per-piece strategist

Uses the fictional canon in `../strategy-brand-mara/canon/`, the strategy outputs from that test's reference run with their frontmatter set to `status: confirmed`, the piece from `../writer-editor-mara/` in state `reviewed` (verdict redo), and the three raw idea bank entries in `ideas.md` here (copy to `bank/ideas.md`). The person is not available for questions.

Run `role-strategist` part A, then part B on the top candidate. Check:

- The runway is counted against the live channel only (the newsletter has a `starts when` condition) and the redo piece is counted with a flag.
- I3 (the VC newsletter) is killed: no source, no reasoning in the canon, and it sits next to X1. I1 and I2 survive; I2 is marked as the person thinking out loud (strength "maybe").
- B1's parts 2 to 4, which the canon names but doesn't fill, land under "Waiting on the person" with a question each, not under killed.
- Ranking separates on rule 1 (a part of B1 outranks a POV linked to B1) and rule 2 (closes the reputation gap); nothing ranks on reach.
- The brief's Material lines are verbatim entry fields with IDs; the bracketed voice note appears where an entry's wording breaks W2; the CTA is decided (`C1` or `none`), never conditional; `layer` and `channel` are in the frontmatter.
- A part whose method isn't captured is briefed as the argument the canon holds, not as a framework post, with the method question in the waiting section.
- The brief's status is `briefed` (writer can draft) or `blocked` (writer can't without a guess), and the brief says which and why.
- With the person away, the strategist goes on to the next candidate until the runway target is met or the list runs out.
- A `seen` proposal (step 4a) is optional here; if the run files one, it quotes every line it rests on, asks one question, and stays under the cap in `templates/proposals.md`. A new belief never goes to `proposals.md`.

`first-run/` holds the first run's shortlist, index, brief and notes, before the fixes in 0.7.0. That run put B1 parts 2 to 4 under killed (now a waiting section), set the brief to `blocked` when `briefed` with open questions was the right call, and stopped after one brief.

This run predates 0.34; its files use the old paths and letters.
