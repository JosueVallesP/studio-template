# Test: capture

Uses the fictional canon in `../strategy-brand-mara/canon/` with the idea bank from `../strategist-mara/ideas.md` (I1 to I3) and the two inputs in `inbox/` here: an intro-call transcript and a voice memo. They were planted with five things in them:

- A definition of "cash months" that the canon lacks and an earlier editor flagged as missing.
- A description of what the Monday call is (B1 part 3), which the strategist listed as waiting on the person, and the person saying out loud that she should write it down.
- A client relaying a friend's advice to raise a round (stop list X1): an objection, not off limits to capture.
- A fourth case of the "everyone asks for a dashboard" observation already in the bank as I2.
- Client details (ARR, headcount) that force an anonymize default.

Run `role-capture`. Check:

- One entry per idea, raw text word for word with speaker labels kept and `[...]` where filler was cut; nothing summarized in place of raw.
- The dashboard passage is added to I2 as an `also:` item, not a new entry; I2's permission moves to the most restrictive.
- The Monday call is typed `method`, and because the person asked for it to be written down, it gets an `asked for` line in `bank/evidence.md` and is listed in the summary under "For the main session", in her words, for the main session to add as a `draft` entry (capture never writes the canon or `proposals.md`). Everything else goes to `bank/evidence.md` as one line per mention.
- The friend's fundraising advice is captured as an `objection` with `wanted_now: no`.
- Call entries default to `anonymize`; memo entries about only the person default to `public`; the summary asks one permission question per source at most.
- The summary names the Monday call entry as the thing the strategist can use first, because it answers a waiting item.
- Files land in `inbox/done/<processing date>_<original name>`.
- Any credibility in the inputs (a result, a client, something said about Mara) lands in `bank/credibility.md` as a K entry, numbers exactly as said, `checked: not yet`, paired with the idea entry where the passage is both. A client's own numbers (ARR, headcount) are context for the anonymize default, not a result of Mara's.
- Nothing written outside `ideas.md`, `credibility.md`, `questions.md`, `evidence.md` and `also:` blocks on existing story or proof entries; nothing in `proposals.md`.

`first-run/` holds the first run's bank, proposals, summary and notes, before the fixes in 0.8.0. That run put ten evidence lines into `proposals.md` under one heading (now the evidence ledger), typed the Monday call as a POV (now `method`), and had no default for a voice memo.

This run predates 0.34; its files use the old paths and letters.
