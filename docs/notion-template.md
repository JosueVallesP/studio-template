# The Notion dashboard: master template

**Status.** Built. Notion is the buyers' dashboard; the Base44 app (`docs/dashboard-app.md`) is the studio owner's own, and the two share one data model. The master lives in the studio author's Notion as "Content Studio (master template)" (`notion_master` in `studio.manifest.yaml`). It was built through the Notion MCP, which can create views, so the "no views from the API" limit below no longer applies when the studio builds it; it still applies to a plain API token, which is why the person duplicates the master rather than having it generated. `scripts/sync-notion.py` is the sync.

One Notion template, designed once, duplicated into every person's workspace. It is the face of the studio for the person: the production pipeline, what's waiting on them, their body of work, their idea bank, their numbers, and the one page on how their studio works. The files in the repo stay the truth; Notion is the mirror. The stop hook runs `scripts/sync-notion.py` after every reply; it pushes state and reads back the few fields the person is allowed to change.

This page is the contract, and the names on it are the as-built names in the master. `setup-notion` finds the databases by these exact titles and the sync reads and writes these exact property names. Change a name here and in the sync together, or not at all.

## Why a template and not a build from the API

Notion's API creates databases and properties but not views. A kanban board, a gallery of shipped pieces, a filtered "Waiting on you" list: none of those can be made by a script. A template carries them. The person duplicates it in one click and `setup-notion` connects to what's already there.

## The pages

The template is one top-level page, **Studio**, with six pages inside it. Only the first is a dashboard; the rest are the databases and one text page.

| Page | What's on it | Who writes it |
| --- | --- | --- |
| **Home** | Waiting on you (two linked views), This week (five numbers), Pipeline (kanban linked view), a link to How your studio works | The sync writes the numbers; the views are live |
| **Pipeline** | The Pieces database, every view | The sync, except the decision fields |
| **Body of work** | The Pieces database filtered to shipped, as a gallery and a table by layer | The sync |
| **Idea bank** | The Ideas database | The sync |
| **Your files** | The Canon index database: every confirmed and draft entry, with where it's been used | The sync, read-only for the person |
| **Numbers** | The Weekly database (one row a week) with four charts, and the Outcomes block | The sync |
| **How your studio works** | The text of `YOUR-STUDIO.md` | The sync, from the file |

Five databases: **Pieces**, **Ideas**, **Proposals**, **Canon index**, **Weekly**. Their titles are exact.

## Pieces

One row per piece, one per folder in `pieces/`. The kanban is this database grouped by Stage.

| Property | Type | Values | Who sets it |
| --- | --- | --- | --- |
| Name | title | The piece's one idea, from the brief | sync |
| ID | text | The folder name, `yyyy-mm-dd-slug` | sync |
| Stage | status | Idea, Candidate, Briefed, Brief approved, Drafted, Reviewed, Revised, Designed, Shipped, Held, Killed, Blocked. Groups: To do = Idea, Candidate, Blocked; In progress = Briefed through Designed; Done = Shipped, Held, Killed | sync |
| Waiting on | formula | "You" when Stage is Briefed, Reviewed or Blocked; "Studio" when Brief approved, Drafted, Revised or Candidate; "Nobody" otherwise | formula |
| Format | select | LinkedIn post, Newsletter issue, Essay, Carousel, Page, Email (grows with the formats) | sync |
| Channel | select | From the person's channel files | sync |
| Layer | select | Stories, POVs, Branches, Proof and vehicle | sync |
| Parent | text | The canon entry the piece grows from | sync |
| Segment | text | The G ID and name | sync |
| Sources | text | The canon and idea IDs the brief traces to | sync |
| Verdict | select | Pass, Revise, Redo: the review's verdict | sync |
| Has visual | checkbox | | sync |
| Visual | files | The designed visual, uploaded on ship | sync |
| Folder | url | Link to the piece folder in the repo | sync |
| Published | url | Where it went live | person or sync |
| Shipped on | date | | sync |
| Impressions, Comments, Reposts, Replies, Conversations | number | The signals, one property each | person or sync |
| Signal note | text | What happened in words ("three founders replied") | person or sync |
| **Your decision** | select | Approve the brief, Change the brief, Kill it, Ship it, Send it back, Hold it | **person** |
| **Your note** | text | The reason or the change, in their words | **person** |
| Decision taken | checkbox | The sync ticks it after the producer records the decision and clears the two fields above | sync |
| Idea | relation to Ideas | | sync |
| Last synced | date | | sync |

Views, in this order:

1. **Board**: kanban by Stage, cards show Format, Waiting on, Verdict, Visual. The default.
2. **Waiting on you**: table, filter Waiting on = You, sorted by Stage. Columns: Name, Stage, Folder, Your decision, Your note.
3. **This quarter**: table, filter Shipped on within the quarter or Stage not Done, grouped by Layer. Shows the mix against the plan at a glance.
4. **All**: table, every property.

## Ideas

One row per entry in `bank/ideas.md`.

| Property | Type | Values | Who sets it |
| --- | --- | --- | --- |
| Name | title | The entry's short title | sync |
| ID | text | I1, I2… | sync |
| Status | select | Raw, Shaped, Ready, Used, Archived, Merged (the idea bank's statuses) | sync |
| Type | select | Story, POV, Method, Question, Observation, Proof, Objection, Outside | sync |
| Strength | select | Strong, Maybe | sync |
| Permission | select | Public, Anonymize, Private | sync |
| Wanted now | checkbox | Fits this quarter's branches | sync |
| Source | text | Call, memo, journal, interview, email, with the date | sync |
| Who said it | text | The person, or a role, never a name | sync |
| Links to | text | Canon IDs it touches | sync |
| Raw | text | The first 300 characters of the raw text | sync |
| Captured | date | | sync |
| Pieces | relation to Pieces | | sync |
| **Your note** | text | "Use this one next", "not this", a correction | **person** |

Views: **Ready** (filter Status = Ready, sorted by Wanted now then Captured), **By type** (board by Type), **All**.

## Proposals

One row per open proposal in `proposals.md`. The person answers here or in the file; either way the producer records it.

| Property | Type | Values | Who sets it |
| --- | --- | --- | --- |
| Name | title | The proposal in one line | sync |
| Kind | select | Change to an entry, Retire an entry, Contradiction, Seen, Voice rule, Definition, Inferred (the kinds in `templates/proposals.md`) | sync |
| Evidence | text | The dated evidence list | sync |
| Question | text | The one question the person has to answer | sync |
| Status | select | Open, Answered | sync |
| **Your answer** | select | Yes, No, Change it | **person** |
| **Your note** | text | The change, in their words | **person** |
| Proposed on | date | | sync |

Views: **Open** (filter Status = Open), **All**.

## Canon index

A read-only mirror of `canon/canon-index.md`, so the person can see what the studio knows and what it has used.

| Property | Type | Values |
| --- | --- | --- |
| Name | title | The entry's short name |
| ID | text | T, V1, P3, S2… |
| Kind | select | Thesis, Value, Behavior, POV, Branch, Stop list, Story, Proof, Offer, CTA, Segment, Desire, Voice rule |
| Tree layer | select | Roots, Trunk, Branches, Around the tree, Vehicle, so the board shows the tree |
| Status | select | Draft, Confirmed, Retired |
| Used in | text | Piece IDs |
| Times used | number | |
| Last touched | date | |

Views: **Confirmed** (what feeds content), **Waiting on you** (Status = Draft: the entries the next interview session will confirm), **Most used**, **All**.

## Weekly

One row per week, written by the sync on its first run of the week. The charts on the Numbers page read from it.

| Property | Type | What it holds |
| --- | --- | --- |
| Week | title | The Monday's date |
| Week of | date | The same Monday, as a date for the charts |
| Shipped | number | Pieces shipped that week |
| Plan cadence | number | Pieces a week the content plan sets |
| Captured | number | Idea bank entries captured |
| Input minimum | number | From the content plan |
| Runway weeks | number | Weeks of ready material at the plan's cadence |
| Confirmed entries | number | From the canon index |
| Open proposals | number | |
| Waiting on you | number | Pieces plus proposals |
| Replies | number | Sum of the week's Replies signals |
| Conversations | number | Sum of the week's Conversations signals |

Four charts (Notion's own charts, on the database): Shipped against the plan's cadence, Captured against Input minimum, Runway over time, Conversations over time. Above them, the **Outcomes** block: the goal in the person's words from `outcomes.md`, and the measure beside it, updated by the sync when the person records it.

## Home

Top to bottom:

1. **Waiting on you.** Two linked views side by side: Pieces "Waiting on you" and Proposals "Open". When both are empty, the page says so in one line, written into the template ("Nothing waiting on you.") under the views, which the empty views sit above.
2. **This week.** Five callouts the sync rewrites: shipped this week against the plan, captured against the input minimum, runway in weeks, entries waiting for your confirmation, the one next step in words (from `setup-progress.md` during setup; from `/status` after).
3. **Pipeline.** The Pieces board, linked.
4. **How your studio works**, as a link.

Nothing else on Home. If a person has to scroll to find what's waiting on them, the page has failed.

## How your studio works

A plain text page the sync overwrites from `YOUR-STUDIO.md` on every run, so the Notion copy and the file never disagree. The person edits the file through the studio, not this page.

## The sync contract

- **Files are the truth.** Every property the person doesn't own is overwritten by the sync; a hand edit there lasts until the next run. The person-owned fields are the ones in bold above: Your decision, Your note, Your answer, Published, the five signal numbers and Signal note.
- **Decisions come back through the producer.** The sync reads Your decision and Your note, hands them to `role-producer` as if the person had said them, the producer records them in the piece log in the person's words, moves the stage, and the sync ticks Decision taken and clears the two fields. Nothing changes in the files without that step, so the log stays the record.
- **Stage names are one list.** The Stage values here, the status words in the brief frontmatter and the states in `templates/piece/README.md` are the same list in the same order. A new state is added in all three in one change.
- **IDs are the join.** Every row carries the ID from the files. The sync matches on ID, never on Name, so renaming a piece in Notion changes nothing.
- **Runs after every reply.** The stop hook runs `python3 scripts/sync-notion.py`, so no skill runs it. On the token route that is the whole sync; the token lives in `.env` as `NOTION_TOKEN`, and `config/tools.md` holds the page and database IDs, never the token. On the connector route the script has no token and exits silently, and the session does the same work through the Notion tools (`setup-notion`, "Keeping it in sync").
- **No Notion, no problem.** When `config/tools.md` says Notion isn't connected, the sync exits silently and `/status` is the dashboard.

## How a person gets it

1. They connect Notion in Claude's settings, under Connectors. This is the default route, and it needs no token.
2. They open the template's public link and click "Duplicate" into their workspace.
3. `setup-notion` runs: finds the copy through the Notion tools, reads the five databases by title, writes their IDs to `config/tools.md`, fills them from the files, writes the first Weekly row, and hands over the link.

When the connector isn't available and the person is comfortable with it, the token route is the fallback: they also create an internal integration in Notion settings named "Content Studio", share the duplicated page with it, and give the studio the token once for `.env`. Then `scripts/sync-notion.py --discover` finds the databases. `setup-notion` has the steps for both routes.

## Building the template

A checklist for the first build, in Notion by hand:

- [ ] One page, **Studio**, with the six pages inside in the order above.
- [ ] Five databases with the exact titles and properties. Build Pieces first; Ideas, Proposals and Canon index after; Weekly last.
- [ ] The Waiting on formula on Pieces.
- [ ] The views, named as above, with the Board as the default view of Pieces.
- [ ] Home as a page of linked views and five callouts with placeholder text the sync will replace.
- [ ] Charts on Weekly with a few rows of sample data, then delete the rows before publishing.
- [ ] Publish the template; the duplicate link goes in the install guide.
- [ ] Test the duplicate in a second workspace: everything duplicates, the formula survives, the linked views point at the duplicated databases and not the master's.

What stays out of the template on purpose: no brand colors or fonts (Notion gives you cover images and icons; use one neutral set and let the person change the icon), no automations (the sync does that), no pages for Figma or formats that don't exist yet.
