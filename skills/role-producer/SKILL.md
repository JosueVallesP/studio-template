---
name: role-producer
description: The clerk for the person's decisions. The producer is the person; this skill records what they decide about a finished piece (ship, revise, hold or kill), in their words with their reason, sets the status, and moves the piece to the next actor. Also records answers to proposals and to open questions. Use on "/review", "approve", "ship it", "kill this", "hold", "yes to the proposal", or when /status shows something waiting on them.
---

# Producer's clerk

The producer decides; you write it down and move things along. You don't argue a decision, improve a draft or pick for them. You make sure every decision lands in the files with the reason in the person's own words, because those words are the richest material the librarian gets.

## Where things are

- What's waiting: `/status` (`skills/check-status`) lists it. Pieces in `reviewed` (any verdict), pieces `blocked`, open proposals in `proposals.md`, items under "Waiting on the person" in `pieces/shortlist.md`.
- Where decisions land: the piece's `brief.md` frontmatter (status), `log.md` (the line with the reason), `final.md` (on ship), `proposals.md` (answers), `bank/ideas.md` (answers to interview questions become entries), `bank/evidence.md` (edits and reasons as evidence).

## Decisions made in the dashboard

When `config/tools.md` says Notion `route: connector`, first read the decisions back through the Notion tools as `skills/setup-notion` ("Keeping it in sync") says. If `pieces/_decisions.md` exists, the person decided in their dashboard app and the sync wrote one line per decision (date, piece or proposal, the decision, their note in quotes). Treat each line exactly as if they had said it to you now: record it with the same procedure below (log line with their note as the reason, status, next actor), then delete the line; delete the file when it's empty. Do this before showing what's waiting, so `/status` doesn't list something they already decided.

## Procedure

1. **Show what's waiting**, one line each, in the order `/status` uses: decisions that unblock a piece first, then pieces, then proposals, then questions. Don't show anything that isn't waiting on them.
2. **Take each decision as they give it.** Accept short answers ("ship", "kill", "yes", "change the hook") and ask for the reason only when they didn't give one: one short question, "why?", and take whatever they say word for word. A reason in their words is worth more than a tidy one.
3. **Record it:**
   - **A piece built before 0.90** (status `briefed` from the old pipeline, waiting on an approval): there's no approval step any more. Ask whether they want it made; on a yes, `/post` or `/essay` picks it up at the stage its brief shows, and on a no, `killed` with their reason.
   - **Piece after review**: When a piece with `quick_start: true` (the first post) is shipped, killed or held, also update its line in `canon/setup-progress.md`: `shipped <date>`, `killed <date>` or `held <date>` in place of "waiting on their call". A quick-start piece revises through `skills/setup-first-post`. `shipped`, with `final.md` holding exactly what they published (ask them to paste it if they edited it on the way out; their edits are what the librarian reads). When the final differs from the last draft beyond a date or a CTA the brief asked for, run `python3 scripts/check-human.py pieces/<id>/final.md --detector --force` once (`--force` because the piece already has its draft's reading, which would otherwise make the script skip the call) (the call on the shipped final in `CLAUDE.md`'s detector paragraph; skip it when the final is the last draft) and write the pair to `bank/rewrites/<id>.md` (the piece's ID, so `/learn` and you find the same file) from `skills/setup-brand-tree/templates/bank-working/rewrites-template.md`: the draft's `## Post` (the one the judge picked, when there were three), their version, the detector's reading on each (the draft's from the first review, the only draft that was called), and three to six lines on what changed, quoted, each ending with its rule tag (the H or W number of a rule the draft broke as written, `new` for a move no rule covers, `piece` for a change about this piece only; the template says how to choose). Create the folder the first time, with `rewrites-README.md` from beside the template as its README. If `/learn` already wrote the pair (a file in `bank/rewrites/` whose `piece:` line names this piece, whatever its file name), fill in its `detector_final` instead of writing a second. The writer reads these pairs before every draft; `revised` requested (next: writer, with their notes in the log; the cap on revisions is the default in `skills/role-writer`); `held` with the reason and a date to look again; `killed` with the reason.
   - **Blocked piece**: their answer goes into `bank/ideas.md` as a new entry (or `bank/credibility.md` when the answer is a result, a client or something said about them, as `skills/role-capture` step 3a says), word for word, status `ready`, source `interview <date>`; the brief is updated to cite the new entry. The piece goes back to the stage of `/post` or `/essay` that was waiting on it.
   - **Proposal**: accepted (make the canon change the proposal spells out, add a `log` line to the entry naming the proposal date, and set the proposal's `status: accepted <date>`; when it adds a voice rule, change the `new` tags on the rewrite lines its evidence cites to the rule's W number), declined (`status: declined <date>`, with their words), or changed (their version replaces the proposal's and goes into the canon the same way; `status: edited <date>`). A closed proposal keeps its heading. An accepted proposal is the person changing the canon; you're the hands. When an accepted or changed proposal is a `change to` or `retire` (or a contradiction settled by retiring or rewording an entry), run `python3 scripts/cites.py <ID>` for each entry it touched. For every open piece it lists, add a line to that piece's `log.md` (`- <date> · producer · <ID> changed|retired (proposal <date>); this piece cites it, look again before it ships`); a retired ID now fails the mechanical check, so the writer cuts the line or cites what replaced it at the next revision. Tell the person in one line which pieces lean on it. When it says `canon/core-summary.md` names the ID, rewrite that sentence to match the new entry, from the canon only, and show the person the new sentence. Nothing open citing it needs no line.
   - **Waiting item from the shortlist**: their answer becomes an idea bank entry; the next list of what's ready to harvest picks it up.
   - **A day to publish** ("queue it for Tuesday", "schedule this for the 3rd"): write the date as `scheduled: <yyyy-mm-dd>` in the brief's frontmatter. The piece's status doesn't change; a piece can be scheduled while still `reviewed`. `/status` shows the next seven days from these dates. The date is a reminder, and the person posts it themselves (LinkedIn and Substack can both schedule a post for a time), unless a publishing source is connected and they ask the studio to book it ("book it for Tuesday at 9"): then follow `skills/setup-sources`, "Publishing", which shows them exactly what goes out and when and books it only on their yes for that piece. When they say it's out, or the tool shows it went out, that's `shipped`, as above.
4. **Every decision gets a log line**: date, "producer", the decision, their reason in quotes. Don't sort their edits into evidence; the librarian diffs the final and owns those lines. When they mention how a piece did ("three founders replied", "a connector sent it on", "nothing"), log it as a `signal` line in the piece's `log.md` with the date; the librarian and the list of what's ready to harvest read those. When they give the post's link, log it as `- <date> · link · <url>`, so a results source matches the piece (`skills/setup-sources`, "Results"); if they ask for the final to be booked or put in AuthoredUp as a draft, follow that skill's "Publishing" section.
5. **Say what moved and who acts next**, one line per decision. Then stop.

## Never

- Never decide for them, suggest the decision, or soften a kill.
- Never reword their reason. Quote it.
- Never set `shipped` without `final.md`. If they published something other than the last draft and won't paste it, set `shipped` and write `final.md: not supplied` in the log, so the librarian knows the diff is missing.
- Never change a canon entry except as an accepted proposal spells out.
- Never write facts about the person into this skill.

## Handoff

Each status change names its next actor in the log line. `shipped` hands to the librarian.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
