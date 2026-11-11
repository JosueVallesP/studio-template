# Piece templates

Every piece of content gets its own folder in `pieces/`, named `yyyy-mm-dd-slug`. Copy these files into it as the piece moves through the crew:

| File | Written by | When |
| --- | --- | --- |
| `brief.md` | `/post` or `/essay` (or a selling tool), filled as the stops go | Before anything else; the person's yes at each stop is the approval |
| `draft-v1.md` | Writer (`role-writer`) | Once the stops are agreed (copy `draft.md`) |
| `review-v1.md` | The `judge` agent, with the gates table in `role-editor`, in a fresh context | After each draft (copy `review-direct.md`; `review.md` is for a piece left from the old pipeline). The verdict is pass, revise or redo |
| `draft-v2.md` | Writer | If the review says revise; one round, then the person decides |
| `visual-brief.md`, `visual-neutral.*`, `visual.*` | `/visual` (`job-visual`) | When the person asks for the picture; structure first, neutral, then the design system |
| `final.md` | Producer (`role-producer`), pasted exactly as published | On ship; the librarian diffs it against the last draft |
| `log.md` | Everyone | One line per action |

## States

The piece's status lives in the brief's frontmatter (`status:`), and nowhere else. This table is the operational copy: who sets each state and who acts next.

| State | Set by | Next |
| --- | --- | --- |
| `idea` | Capture (an idea bank entry, before any piece exists) | `/harvest` lists it when it's ready |
| `candidate` | `/harvest`, on the list of what's ready | The person picks |
| `briefed` | `/post`, `/essay` or a selling tool, as the stops go | The writer, once the stops are agreed |
| `drafted` | Writer | The `judge` agent |
| `reviewed` | The `judge` agent, with a pass, revise or redo verdict | Pass: the person (ship, hold, kill, or `/visual`). Revise: the writer. Redo: the command that made it, back at stage 1 |
| `revised` | Producer, when the person asks for changes | Writer |
| `shipped` | Producer, with `final.md` | Librarian |
| `held` | Producer, with a date to look again | The person, on that date |
| `killed` | Producer | Nobody |
| `blocked` | Any role missing an input, with what's missing in `log.md` | Whoever the log line names, usually the person |

Two states from before 0.90, when the studio also had a pipeline, can still appear on old pieces: `brief-approved` (the writer drafts it) and `designed` (the person decides).

## Files beside the piece folders

These sit in `pieces/` itself, not in a piece folder:

- `index.md`: the body of work (every piece by branch, layer, state), rewritten by the librarian. Template here.
- `shortlist.md`: what's ready to harvest and the items waiting on the person, from `/harvest`. Template here.
- `librarian-last-run.md`: the librarian's last report, and the drafts it couldn't write to the canon itself.
- `_decisions.md`: decisions the person made in their dashboard, waiting for the producer to record them. Deleted when empty.

`/think` writes its findings to `sessions/think-<date>.md`, not here.
