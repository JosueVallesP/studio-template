# Rewrites

One file per piece the person rewrote: the draft the studio wrote on the left, the version the person wrote instead on the right, same idea, with the detector's reading on each. This folder belongs to the person.

This is the closest thing to the person's hand the studio has. Before every draft the writer reads ten pairs (the default in `skills/role-writer`), chosen by `python3 scripts/rewrites.py pick --format <format>`, and writes like the right-hand side. The voice guide's rules are the summary; the pairs are the thing.

Every line under "What changed" ends with a rule tag (the template explains them):

- **A house or voice rule (`H19`, `W4`)** means the draft broke a rule the studio already has. If no review of the piece named that rule, the checks missed it, and the librarian notes it in `studio-notes.md` as a gap in the checks.
- **`new`** means the person made a move no rule covers. The librarian counts these; the second time a move shows up, it proposes a voice rule.
- **`piece`** means the change was about this piece only.

When a `new` move becomes a voice rule, the tag changes to the rule's W number. A pair with no `new` line left is closed: the writer reads open pairs first, same format before other formats, so its ten slots go to lessons the rules don't hold yet. `python3 scripts/rewrites.py tally --since <date>` counts the tags; `/end` says that count in one line.

Who writes here:
- The producer, on "ship it", when the final differs from the last draft (`skills/role-producer`).
- `/learn`, the moment the person hands back a rewrite in a session (`skills/job-learn`).

File name: `<yyyy-mm-dd>-<piece id>.md`, from `skills/setup-brand-tree/templates/bank-working/rewrites-template.md`.
