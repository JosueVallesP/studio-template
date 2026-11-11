# Selling copy judge

Input: the piece's `brief.md` and latest `draft-vN.md` (Post A, B and C, the source map, the argument check), the material files the brief cites, `canon/vehicle/vehicle.md`, `canon/strategy/audience.md` and `canon/strategy/brand-strategy.md` when they exist. Read `skills/craft-sales-copy/SKILL.md` first; its truth tests are the checks in section A.

Grades (pass, revise, redo) come from the gates table in `skills/role-editor`. Where a check below names its grade, that grade applies only when the gates table has no row for it.

Leave the draft's `## Argument check` unread until your own premise verdicts are written.

## Checks

Each check is PASS or FAIL. A FAIL quotes the line and says what's wrong in one sentence. Never rewrite the copy.

### A. True on the day it goes out

1. **Every price, result, client, number, testimonial and guarantee has a source** in the vehicle, the proof file, the cited material or `said today`. One without a source is invented material (redo).
2. **No line is true only if things go well.** Participants named before they took part, results claimed for an offer nobody has bought yet, "clients say" with no client. Redo.
3. **Scarcity and urgency are real and the reason is stated.** A limit or a deadline with no source in the vehicle or the person's words fails (redo). A real one with no reason given fails (revise).
4. **No value figure in public copy** that isn't a real standalone price with its source. Revise.
5. **Care, not leverage.** A pain pressed harder than the research shows, a fear the research doesn't hold, a reader made to feel stupid for not buying, an unconfirmed WON'T. Redo for the WON'T (the gates table), revise for the rest.
6. **Transparent selling.** A piece that leads to a paid step and hides it, or a free part that isn't useful on its own. Revise.
7. **Stop list and anti-associations.** Anything on either. Redo.

### B. It does the selling job

8. **The opening is about the reader.** The first lines describe their situation, in words from the language bank or the person's record of what buyers said, before the offer or the person's credentials. Cite the source line.
9. **One offer, one next step,** and the call to action matches a `C` entry word for word, or the brief says there's none yet.
10. **Every claim has its why** (house rules H7). A benefit stated with no mechanism fails.
11. **The objections answered are the reader's,** traced to `tried`, the reasoning column, a call or a quote; not a generic list.
12. **The copy kind's own checks.** The calling skill's gates for this kind: the pamphlet's four sections and its sales page parts (`skills/job-pamphlet-power`), the invitation's four parts, truth and swap tests (`skills/job-turning-prospects-into-collaborators`), the follow-up in the buyer's words (`skills/job-diagnosis-call`), the positioning line's and the About section's gates (`skills/job-personal-monopoly`, `skills/job-building-your-message`). For offer copy, the offer document's quality checks (`skills/job-offer-designer`) are readings: note them under WORTH NOTING, and never grade the value-to-price ratio (the 10x reading) as a fail.

### C. The writing

13. Run `python3 scripts/check-prose.py <draft>` and `python3 scripts/voice-diff.py <draft>`. Every script fail is a FAIL here. Read the flags as evidence.
14. **House rules.** A line that breaks one, with its H number. Hype words, capitals for emphasis and curiosity gaps fail under H23.
15. **The swap test.** If a competitor's name could go on this page and it would still work, it's not the person's. FAIL as "not theirs".
16. **Supplied copy kept as written** (`CLAUDE.md` rule 3).
17. **The argument holds.** The judge pass of `skills/craft-copylosophy` on the chosen draft. A `false` premise is a redo.
18. **Reads like a person.** `skills/check-human` on the chosen draft. On the piece's first judged draft only, add `--detector` as `CLAUDE.md`'s detector paragraph says, unless a `review-v*.md` in the folder already records a reading (then don't call again); record the label, never grade it.

### D. Three drafts

19. Judge A, B and C against sections A to C, then pick the one with the fewest fails that reads most like the person's own samples. Say which and why in one line. If none passes, send all three back with what each needs. Never merge them.

## Output

THE ONE THING first: the deepest failing lever, the quoted line and the fix, ordered as `skills/craft-refine` orders them. "none" on a pass.

```
VERDICT        pass / revise / redo
               redo: any fail in A graded redo, or a false premise
               revise: any other fail
               pass: no fails
CHOSEN         A, B or C, and why in one line
FAILS          numbered: check number, the line quoted, what's wrong, the fix if it's obvious
WORTH NOTING   at most two
FOR THE PERSON every `inferred` line with the proposal it went to; each open fail as one plain line
```

Save it as `review-vN.md` from `templates/piece/review-direct.md`. An `inferred` line the material supports goes to `proposals.md` as the judge agent's instructions say.
