# The dashboard app

This is the studio owner's own dashboard path (`dashboard: app` in `config/tools.md`); buyers use the Notion dashboard in `docs/notion-template.md`. One app per person, built in Base44 from this spec and styled from their brand assets. It is the face of the studio for the person: what's waiting on them, the production pipeline, their body of work, their idea bank, their numbers, and the one page on how their studio works. The files in the repo stay the truth; the app is the mirror. The stop hook runs `scripts/sync-dashboard.py` after every reply; it pushes state and reads back the few fields the person is allowed to change.

This page is the contract: entity names, field names and the stage list are exact. `setup-dashboard` creates the person's app from the master, writes its ID into `config/tools.md`, and runs the first sync.

## Pages

| Page | What's on it | Who writes it |
| --- | --- | --- |
| **Home** | Waiting on you (pieces at a gate, open proposals), This week (five numbers), the pipeline board, a link to How your studio works | The sync writes the numbers; the lists are live |
| **Pipeline** | The Piece board, kanban by Stage. A card opens a detail panel with the decision form. Dragging to a gate column (Brief approved, Shipped, Held, Killed, Revised) records the matching decision and asks for the note; any other drop snaps back. The app never changes `stage` | The sync, except the decision fields |
| **Body of work** | The tree of knowledge: roots (values, behaviors, POVs), trunk (thesis, philosophy), branches (B entries), leaves (shipped pieces hanging from their `parent_id`); click a node for its pieces; orphans and thin branches listed below; a table as a second tab | The sync |
| **Idea bank** | Ideas as a list with filters by Status, Type, Wanted now | The sync |
| **Your files** | The canon index: every entry the studio knows, its status, where it's been used | The sync, read-only for the person |
| **Numbers** | Weekly rows with four charts, and the Outcomes block (the goal in their words, the measure beside it) | The sync |
| **How your studio works** | The text of `YOUR-STUDIO.md` | The sync, from the file |

Home is the landing page. Nothing on it below the pipeline. If a person has to scroll to find what's waiting on them, the page has failed.

## Entities

Six entities. The sync writes every field except the ones marked **person**.

### Piece

| Field | Type | Values | Who sets it |
| --- | --- | --- | --- |
| title | string | The piece's one idea, from the brief | sync |
| piece_id | string, unique | The folder name, `yyyy-mm-dd-slug` | sync |
| stage | enum | idea, candidate, briefed, brief_approved, drafted, reviewed, revised, designed, shipped, held, killed, blocked | sync |
| waiting_on | enum | you, studio, nobody. You when stage is briefed, reviewed or blocked; studio when candidate, brief_approved, drafted or revised; nobody otherwise | sync |
| format | string | LinkedIn post, Newsletter issue, Essay, Carousel, Page, Email | sync |
| channel | string | | sync |
| layer | enum | stories, povs, branches, proof_and_vehicle | sync |
| parent_id | string | The canon entry the piece grows from (B, P, V or T), from the brief's `parent`; the tree hangs the leaf from it | sync |
| segment | string | The G ID and name | sync |
| sources | string | The canon and idea IDs the brief traces to | sync |
| verdict | enum | pass, revise, redo: the review's verdict | sync |
| has_visual | boolean | | sync |
| visual_url | string | The designed visual | sync |
| folder_url | string | The piece folder in the repo | sync |
| published_url | string | | person or sync |
| shipped_on | date | | sync |
| impressions, comments, reposts, replies, conversations | number | The signals | person or sync |
| signal_note | string | What happened in words | person or sync |
| **your_decision** | enum | approve_brief, change_brief, kill, ship, revise, hold | **person** |
| **your_note** | string | The reason or the change, in their words | **person** |
| decision_taken | boolean | The sync ticks it after the producer records the decision and clears the two fields above | sync |
| idea_id | string | The idea it came from | sync |
| last_synced | datetime | | sync |

### Idea

| Field | Type | Values |
| --- | --- | --- |
| title | string | The entry's short title |
| idea_id | string, unique | I1, I2… |
| status | enum | raw, shaped, ready, used, archived, merged (the idea bank's statuses) |
| type | enum | story, pov, method, question, observation, proof, objection, outside |
| strength | enum | strong, maybe |
| permission | enum | public, anonymize, private |
| wanted_now | boolean | |
| source | string | Call, memo, journal, interview, email, with the date |
| who_said_it | string | The person, or a role, never a name |
| links_to | string | Canon IDs |
| raw | string | The first 300 characters of the raw text |
| captured | date | |
| **your_note** | string | **person**: "use this next", "not this", a correction |

### Proposal

| Field | Type | Values |
| --- | --- | --- |
| title | string | The proposal in one line |
| proposal_id | string, unique | |
| kind | enum | change, retire, contradiction, seen, voice_rule, definition, inferred (the kinds in `templates/proposals.md`) |
| evidence | string | The dated evidence list |
| question | string | The one question to answer |
| status | enum | open, answered |
| **your_answer** | enum | yes, no, change_it (**person**) |
| **your_note** | string | **person** |
| proposed_on | date | |

### CanonEntry

| Field | Type | Values |
| --- | --- | --- |
| title | string | The entry's short name |
| entry_id | string, unique | T, V1, P3, S2… |
| kind | enum | thesis, value, behavior, pov, branch, stop_list, story, proof, offer, cta, segment, desire, voice_rule |
| status | enum | draft, confirmed, retired |
| used_in | string | Piece IDs |
| times_used | number | |
| last_touched | date | |

### WeeklyStat

| Field | Type |
| --- | --- |
| week | date (the Monday) |
| shipped, captured, input_minimum, runway_weeks, confirmed_entries, open_proposals, waiting_on_you, replies, conversations | number |

### StudioSettings (one record)

| Field | Type | What it holds |
| --- | --- | --- |
| person_name | string | |
| what_they_do | string | In their words |
| goal | string | In their words |
| measured_by | string | |
| channels | string | |
| hours_per_week | number | |
| primary_color, accent_color, background_color | string | Hex, from `canon/visual/brand-assets.md` or the design system |
| font_heading, font_body | string | |
| logo_url | string | |
| how_it_works | string | The text of `YOUR-STUDIO.md`, markdown |
| plan_cadence_per_week | number | From the content plan |
| next_step | string | The one next step, from `/status` or `setup-progress.md` |
| last_synced | datetime | |

## The look

The default look is the studio's Engraved Swirl style (paper, ink, hairlines, EB Garamond and IBM Plex Mono, one blue, one yellow at most, a branching-tree plate on Home). The app reads StudioSettings on load and, where a person's colors or fonts are set, those override the defaults; where they're empty, the default is the look. One master layout, every person's colors. Empty states say what will fill them ("Your first brief lands here once the strategy is confirmed"), never a blank table. No marketing copy, no onboarding tour, no settings page for the person: the studio owns the data.

## The sync contract

- **Files are the truth.** Every field the person doesn't own is overwritten by the sync. The person-owned fields are your_decision, your_note, your_answer, published_url, the five signal numbers and signal_note.
- **Decisions come back through the producer.** The sync reads your_decision and your_note, hands them to `role-producer` as if the person had said them, the producer records them in the piece log in the person's words and moves the stage, and the sync sets decision_taken and clears the two fields. Nothing changes in the files without that step.
- **Stage names are one list.** The stage enum here, the status words in the brief frontmatter and the states in `templates/piece/README.md` are the same list in the same order.
- **IDs are the join.** The sync matches on piece_id, idea_id, proposal_id, entry_id, never on title.
- **Runs after every reply.** The stop hook runs `python3 scripts/sync-dashboard.py`, so no skill runs it, and its first run of the week writes the weekly row. The app ID lives in `config/tools.md`; the API key in `.env` as `BASE44_API_KEY`, never in the repo.
- **No dashboard, no problem.** When `config/tools.md` says no dashboard is connected, the sync exits silently and `/status` is the dashboard.

## One app per person

The master app is built once from this spec. `setup-dashboard` duplicates it for each person, writes their StudioSettings from intake and the canon, invites them as the app's user, and runs the first sync. Studio updates to the master reach the copies the way skill updates do, by re-running the duplication's code step without touching their data.
