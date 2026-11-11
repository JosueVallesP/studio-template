# Rewrites: pick and tally

Tests `scripts/rewrites.py`, which decides which rewrite pairs the writer reads before a draft and what `/end` says about the session's rewrites.

## What's staged

`root/` is a small instance: five pairs in `bank/rewrites/` and one review.

- `P000`: an old LinkedIn pair with no rule tags. Untagged lines count as open.
- `P001`: LinkedIn, three changes: H19, W2 and one `new`. Its review names W2.
- `P002`: LinkedIn, W1 and one `piece` change. Closed.
- `E001`: a Substack essay with one `new` change. Open.
- `P003`: LinkedIn, W3 only. Closed.

## Run

`python3 tests/studio/rewrites/run.py`

## Properties

- `pick --format fmt-linkedin-post` lists open LinkedIn pairs first (P001, then P000), then the open essay pair, then closed LinkedIn pairs, newest first in each group.
- `pick --format fmt-substack-essay` lists the essay pair first.
- `tally --since 2026-10-10` finds four pairs and seven changes: three broke a rule no review named (H19, W1, W3), one broke a rule the review named (W2), two are new, one was about the piece only.
- With no pairs since the date, `tally` says so in one line.
