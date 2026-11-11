# Proposals

Suggested changes to the canon, waiting for the person's yes. Anyone in the crew may add one; only the person moves it into the canon. One `##` heading per proposal; `/status` counts the ones with `status: open`. A closed proposal keeps its heading and its new status.

This file is for changes to what's already confirmed, and for what the person has to pick or see. A new belief, story, method, result or offer is never a proposal: it goes in as a `draft` entry in its canon or bank file, with its quote, source and a log line (`skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes"), and `/status` lists it for the person to confirm. A crew agent that can't write the canon lists the draft under "Drafts to add" in `pieces/librarian-last-run.md`, and the main session adds it.

The kinds:
- `change to <ID>`: new wording, a new condition or a new field on a confirmed entry.
- `retire <ID>`: a confirmed entry the evidence says no longer holds.
- `contradiction`: two confirmed entries, or a confirmed entry and new evidence, that can't both be true as written. The person picks, or names the condition under which both hold.
- `seen`: a connection across entries the studio noticed (`CLAUDE.md` rule 8, `skills/job-think`).
- `voice rule`: a new rule for the voice guide, earned by the count in `skills/role-librarian`.
- `definition`: what a term the person uses means, when a confirmed entry names it without saying.
- `inferred`: a line in a piece that states what the person believes, did or has seen and isn't in their sources (`CLAUDE.md` rule 1). The judge or editor files it with the lines it was read from, and names it to the person before the piece ships.

Every quote in a proposal is the person's real words, word for word from their files: before adding or changing one, run `python3 scripts/check-proposals.py`, and fix or drop any quote it can't find. A proposal resting on a misremembered line asks the person to decide about something they never said.

At most five open proposals at once. Before adding one, read the open ones: a proposal that says the same thing gets a new dated line under its `evidence` instead of a second heading. Past five, append a line to `bank/evidence.md` marked `earned` instead, and the librarian promotes the oldest when a slot opens.

## <date> · kind: change to <ID> / retire <ID> / contradiction / seen / voice rule / definition / inferred
proposed_by: <role>
seen_in: <piece IDs or files>
proposal: <the entry as it would read in the canon, in the person's words where they exist; any field they never worded marked [librarian's wording]. For kind `seen` (a connection, a method, a shape or an unstated belief the studio noticed): what it sees in one or two sentences, and every quote it was drawn from>
evidence:
  - <date> · <I ID or piece> · "<what was said or edited>"
  - <later mentions appended here, dated>
question_for_the_person: <one line>
status: open | accepted <date> | declined <date> | edited <date>
