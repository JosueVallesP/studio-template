---
name: job-tidy
description: Keeps the workspace clean and free of bloat so the studio reads what's current instead of wading through what's stale. Prunes expired outside entries and raw entries that never got their missing piece, merges duplicates, archives a shipped piece's drafts and reviews, flags contradictions between newer and older entries for the person to settle, and compacts old session log lines. Never touches the canon, never deletes the person's material, journal or pieces; it moves to an archive. Runs on its own twice a week when the person sets the scheduled task, or on demand. Use for /tidy, "tidy up", "clean up the workspace", "what's stale".
---

# /tidy

Method by Josué Valles, the studio's author: the workspace stays clean and free of bloat, with a tidy-up twice a week.

## What it does

- **Prunes stale working material.** Outside entries in `bank/ideas.md` past their `expires` date (role-capture gives every outside entry one); tidy owns this, and the librarian leaves them for it. An outside entry with `expires: with the seed`, or one a seed's `fed` or `pushback` names, never expires on its own: it moves to the archive only with its seed, when the person cuts the seed. Entries marked `raw` that have waited more than 30 days (a starting default) for their missing field, once `/status` has reminded the person (it lists `raw` entries older than 21 days). Both move to `bank/archive/ideas-<year>.md`, never deleted. Entries at `status: shaped` (a card `/shape` wrote that waits for the person's yes) are never archived as stale. The seed record decides the rest (stages in the idea bank template): a seed the person marked `cut` moves to the archive on the next run; a seed at `resting`, or one past `seed` (`sprouting`, `growing`, `bearing`), is never archived as stale, because the person has already said it's worth keeping; only a `raw` entry still at `stage: seed` can go stale. Credibility entries never expire and never move on their own, but one whose `checked:` date (or capture date, when never checked) is more than a year old is listed for the person in one line each ("still true?"), because a number that was true last year can be wrong in a post today.
- **Merges duplicates.** Two idea bank entries that say the same thing become one. The older ID stays, with the newer entry's source and `raw` added as an `also:` item; the newer entry stays in place as `status: merged into I<n>`, so nothing that cites it breaks. The two seed records merge too: every `fed`, `pushback` and `fruit` line moves to the older entry, and it keeps the further of the two stages. Then update every line that cites the newer ID (a brief's material line, an `evidence.md` line) to the older one. The `raw` text of each is kept; nothing is reworded (`CLAUDE.md` rule 3).
- **Archives finished work.** For a piece with `status: shipped` for more than 14 days, the earlier drafts and reviews move to `pieces/<id>/archive/`. The last draft (it holds the source map) and the last review (the dashboard shows its verdict) stay, with the brief, the final and the log, where the studio reads them.
- **Flags contradictions.** When a newer idea bank entry or shipped piece contradicts a confirmed entry or an older one, it goes to `proposals.md` as `contradiction` with both lines quoted and one question: which stands? First read the open proposals: when one already names the same clash, add a dated line to its `evidence` instead, and past the cap in `templates/proposals.md` write an `earned` line to `bank/evidence.md`. Tidy never picks (`CLAUDE.md` rules 6 and 8). Run `python3 scripts/check-proposals.py` after filing; a quote it can't find is fixed or the proposal is dropped.
- **Compacts logs.** Lines in `sessions/log.md` older than 30 days roll into one dated summary line per week (files changed, pieces made, decisions). The `/end` entries stay whole, their `ran:` lines included, since `/end` counts them to offer recipes.
- **Asks about idle recipes.** Tidy is the one place that works out which recipes are idle: a recipe in `recipes/` whose `Last run` is more than 60 days old (or "never", 60 days after it was made) is named, with its last-run date, in tidy's report line, and `/status` reads that line and asks the person whether to keep it or retire it (`skills/check-status`, step 9). Tidy never retires one itself; retiring is the person's call (`skills/job-recipes`).
- **Reports in one line** to `/status`: what it pruned, merged, archived and flagged, and any idle recipes, with counts. Flags wait in `proposals.md`.

## What it never does

- Never touches `canon/` (rule 6). It can only propose.
- Never deletes anything. Everything moves to an archive the person can read, and anything in an archive can come back with "restore I23".
- Never reads a journal entry; `journal/` is the person's alone.
- Never overrides a `private` or `never:` flag, anywhere.
- Never archives a piece that isn't shipped, a rewrite pair, a recipe, or material in `material/` or `inbox/`.

## How it runs

- On a schedule: `skills/setup-schedules` (`/schedules`) sets it up; the default it offers is twice a week, three or four days apart, off until they say yes. With nobody present, a scheduled run does everything here except ask: it moves, merges and flags, writes its report line, and leaves every question (idle recipes, credibility entries due a check) for `/status`.
- On demand: `/tidy`, or "tidy up". A dry run first when the person asks ("what would you tidy?"): the list, nothing moved.
- Order: expire, merge, archive, flag, compact, recipes, report. Each step writes what it did to `sessions/log.md` as one line.

## Never

- Never delete. Move.
- Never resolve a contradiction. Ask.
- Never tidy the canon, the journal, the material or the inbox.
