# Test: strategy-brand on a fictional canon

Mara Lindqvist is invented. Her canon (`canon/`) is a complete minimum canon for a fractional CFO serving bootstrapped SaaS founders: thesis, two values, five confirmed POVs and one draft, one confirmed branch and one draft, five stop list entries, three stories, three proof entries, a goal with a stated pace ("not in a rush"), one segment with two scored desires, a first-draft voice guide, and about four hours a week of capacity.

Run `skills/strategy-brand` against it and check the output for these, which the first run got right and later runs must keep:

- route-clients, with a pace weighted toward "body of work first" because the goal says so, and a reason that cites the goal.
- Gate 1 passed on the second route (she has fixed the reader's problem many times, R1 to R3), not failed because she has never been a founder.
- Anti-associations drawn from X1 to X5, and the goal-derived one routed to `proposals.md`.
- Proven credibility position citing R1 to R3; enemy from P1 (and P4 as the same enemy from another side); value types with evidence IDs.
- One LinkedIn file carrying several jobs, one newsletter file with a `starts when` condition.
- Cadence trimmed to four hours with the arithmetic shown; no cadence above what she can hold.
- Only B1 feeding content; B2 and P6 named as drafts, not used.
- No paid promotion anywhere. No topic-popular posts offered.
- A review file at `canon/strategy/strategy-review.md` that asks for a yes per part and lists the open questions, including the newsletter timing and the lists she doesn't have yet.
- Nothing set to `status: confirmed`.

`reference-run/` holds the first run's outputs (before the skill fixes in 0.4.1) for comparison, and `first-run-notes.md` holds what that run found unclear in the skill. A new run should produce fewer such notes. This run predates 0.34; its files use the old paths and letters.
