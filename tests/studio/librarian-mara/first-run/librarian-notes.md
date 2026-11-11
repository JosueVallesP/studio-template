# Notes on role-librarian, from the first run (2026-10-23)

For the skill's author. Blunt, as asked.

## What I read

33 files. CLAUDE.md; `skills/role-librarian/SKILL.md`; `.claude/skills/librarian/SKILL.md` and `.claude/agents/librarian.md`; the five files in the shipped piece's folder and the two in the blocked one; `pieces/index.md`, `pieces/shortlist.md`, `pieces/README.md`; `canon/bank/evidence.md`, `ideas.md`, `stories.md`, `proof.md`; `canon/person/povs.md`, `thesis.md`, `branches.md`, `values.md`, `stop-list.md`; `canon/README.md`; `canon/voice/voice-guide.md`; `canon/strategy/content-plan.md` and `channels/linkedin.md`; `templates/proposals.md`, `templates/piece/index.md`, `log.md`, `final.md`, `README.md`; `studio-notes.md`; `proposals.md`; the 10-22 memo in `inbox/done/`; and grep hits in `skills/role-producer/SKILL.md` and `skills/check-status/SKILL.md`. I did not read `audience.md`, `brand-strategy.md`, the vehicle file or the other role skills; the piece files quoted what I needed from them.

## Where the skill was unclear, contradictory or missing something

1. **Input 5 names a file that does not exist.** `canon/canon-index.md` is listed by this skill, role-capture, role-strategist and the canon README, and nobody creates it. Fifth role to hit this. Fix it at the source (setup-brand-tree) or drop it from every input list.

2. **"A voice edit made twice" does not define twice.** Two cuts of the same kind in one final, or the same kind in two finals? I counted two cuts in one piece as twice because the person also wrote the rule herself in the log ("Cut the hedges, it read like I was apologising"). If that is wrong, say "two pieces" and I would have left it in the ledger. Either way, the ledger line format (`voice edit · W? · <piece> · "<was> → <now>"`) is one line per edit, so the count is per edit, which argues for my reading. Say which.

3. **Step 2 and the contradiction rule pull against each other.** Step 2: a stretch the editor caught and the person kept is "evidence for the canon entry to grow". Step 3: "one contradiction with a confirmed entry is a proposal on its own". A kept line that goes against a `rejects` field is both. I treated the P4 line as a contradiction because the editor had already flagged it as a possible P4 change. The skill should say: a kept stretch that goes past an entry's claim is a repeat that grows it; a kept stretch that goes against a claim or a rejects field is a contradiction.

4. **The ledger has no kind for two things step 2 and step 5 ask me to write.** "A stretch the person cut confirms the entry's limit" has no kind; I wrote `limit confirmed`. "Note in evidence.md any ready entry older than a quarter" and the "say how many more mentions each needs" line have no kind; I wrote `note for the strategist`. Give the ledger a kind list (voice edit, repeat, contradiction, new story, new proof, definition, limit confirmed, note) and put it in the evidence template, which I could not find. Capture already invented `asked for` and `new method`, and `new method` points at layer `A?`, which no canon file has.

5. **`used_in` on entries "a shipped piece cited".** The brief cited no I entries. The final carries I7's and I11's words because the person typed them in. Cited by whom? I set `used_in` on both, because the strategist needs to know that material is now public. Say whether `used_in` tracks the brief's sources or the final's content.

6. **The skill assumes a final comes after a passing review.** This one shipped from draft v1 with verdict redo and no revised round. Fine, I diffed draft v1, but the skill should say "the last draft, whatever the verdict" and the index should be able to say "shipped over a redo", because that is a signal about the editor's calibration (she kept the hook the editor failed, cut the stance words check-human said to keep).

7. **role-producer and role-librarian both own the final's evidence lines.** The producer skill says every edit to a final gets an evidence line from the producer; this skill says the librarian diffs and writes them. The producer wrote none. Pick one owner. If it is the librarian, the producer only needs to paste the final and the reason; if it is the producer, the librarian only checks.

8. **The proposal template has no room for a second piece of evidence later.** The Monday call proposal got a second mention today. I appended to `evidence:` and signed it. Say that is the way, or give the template a dated evidence list.

9. **"Never let a proposal carry a reason it should be accepted" collides with proposing a changed `rejects` field.** For P4 the person's words only exist for the shipped line, not for a new rejects field, so I had to draft one in my words with "if the shipped line is her view". A rule for fields the person has never worded would help: quote what exists, mark the rest as the librarian's wording.

10. **Step 6 asks for things the index template can't hold.** The Layer column has no brief field (the strategist hit this too). "A leaf that drew replies but was never expanded" needs signals, and no file in `pieces/` holds signals; the log is the only place, and nothing says the person should log replies there. The template also has no row for a candidate without a folder. Fix the brief (add `layer:`) and say where replies get recorded.

11. **Step 7's criteria exclude a real fix.** "Same guess twice, or a template field with no source" misses a contradiction between two skills reported once (editor: check-human says write `check-human.md` beside the draft, role-editor says put the verdict in the review). I included it anyway and said why. Add "or two skills disagree" to the criteria.

12. **Five-proposal cap and "earned" lines.** The cap is clear; "hold the rest in the ledger marked `earned`" gives no format. I did not hit the cap (four open), but the next run might. Give the mark a place in the line.

13. **Part A step 8 says "then stop", part B says "say back in one sentence".** Fine. But nothing says where step 8's message goes when the librarian runs as an agent with no person in the room. I wrote it to a file because the task asked; the skill should say "write it to the log or return it to the caller".

14. **Small things.** The ledger's 10-20 line points at `2026-10-20-test-note`, which is not a piece folder; a test left it there. The ledger's I2 repeat line is cut off mid-quote (capture's bug, left as is). `canon/README.md` lists the canon layout from the brand-tree templates (vehicle, strategy, canon-index) and the actual canon has extra files (`setup-progress.md`, `strategy/outcomes.md`, `strategy/SUMMARY-for-review.md`) the README never mentions; not my job, but somebody's. `t.md` at the repo root is a stray test file.

## What I guessed

- Twice means two cuts in one piece (note 2).
- The P4 line is a contradiction, not a repeat (note 3).
- `limit confirmed` and `note for the strategist` as ledger kinds (note 4).
- `used_in` follows the final's content, not only the brief (note 5).
- Where to put the cash months definition: W2, because W2 is where the term lives and the editor pointed there; the question to Mara leaves the place open.
- The "before Monday" edit as a `repeat` for B1; it is really a brief-conformance fix with no canon meaning, but step 1 says every change is a signal and gives no "no signal" option.
- A librarian line in the piece's `log.md`; the Output list doesn't mention it, the piece README says everyone logs.
