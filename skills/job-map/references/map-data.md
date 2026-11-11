# The map's data file

`bank/map/map.json` is the one source for the map. The page (`bank/map/findings.md`), the picture (`bank/map/map.html`) and the Obsidian file (`bank/map/map.canvas`) are all built from it by `python3 scripts/map-render.py`, so they never disagree. Edit the JSON, never the built files; a rebuild overwrites them.

The script checks every rule marked **(checked)** below and refuses to build when one fails, naming the line.

## The top

```json
{
  "person": "Dana Ruiz",
  "built": "2026-10-26",
  "updated": "2026-10-26",
  "studio_version": "0.77.0",
  "left_out": "I read your call transcripts for what you said about your work and left out what clients said about their own lives.",
  "sources": [ ... ],
  "nodes": [ ... ],
  "links": [ ... ],
  "findings": [ ... ]
}
```

`left_out` is the one line on what was read and what was kept off the map (`references/reading.md`). It can be empty when nothing was.

## sources

One per piece, not per file. A post and its long essay version are one source with two files.

```json
{ "id": "post-03", "title": "People rarely buy stuff in isolation.", "files": ["material/posts.md", "material/essays.md"],
  "kind": "post", "date": "2025-04", "privacy": "public" }
```

- `id` **(checked: unique)**. Codes as `references/reading.md` sets them: post-01, essay-01, talk-01, call-01, note-01, book, workshop.
- `kind`: post, essay, talk, podcast, call, memo, note, message, workshop, course, book, other.
- `date`: as precise as the file allows (`2025`, `2025-04`, `2025-04-12`), or empty.
- `privacy` **(checked: public or private)**.

## nodes

Four types. Every node has `id` **(checked: unique across nodes)**, `type` and `text`.

**claim**: a sentence someone could disagree with.

```json
{ "id": "c4", "type": "claim", "text": "Your clients are your brand, more than your posts are.",
  "said": "outright", "layer": "pov", "spine": true, "status": "seen",
  "versions": [
    { "quote": "Picking clients is one of the biggest brand decisions you'll ever make.", "source": "post-05" },
    { "quote": "Who you work with says more about you than anything you post.", "source": "call-02" }
  ] }
```

- `text`: the claim in one tightened sentence, the studio's wording. The person's own words live in `versions`.
- `said`: `outright` (they state it) or `implied` (their pieces assume it and no line states it).
- `layer`: `pov` (an opinion about their field), `method` (how something should be done, step by step), `philosophy` (a claim that ties several POVs together), `thesis` (the one claim the work proves). The map never writes a value.
- `spine`: true for the three to five claims everything else hangs from.
- `status`: `seen` (the studio read it; nobody confirmed it), `confirmed`, `rejected`, `renamed`, `held before` (the person said they no longer hold it). A renamed claim's `text` is the person's new wording. A `held before` claim keeps its versions (it's still what they said, and when) and carries `dropped: <date> · "<their reason, as they said it>"`; a `replaced_by` link points to the claim that replaced it, when there is one. Nothing quotes a `held before` claim as what the person thinks now (`CLAUDE.md` rule 1).
- `versions` **(checked: a claim needs at least one, and an `outright` claim needs every version to carry a `quote`)**. Each version: `quote` (word for word), `source` **(checked: a source ID)**, and optional `note` ("the long version", "his report"). An `implied` claim may have versions with a `line` field instead of `quote`: the line it was read from, with what it shows.
- `privacy` is computed by the script from the sources (public, private or both); don't write it.
- `canon`: the canon ID once the claim is a draft or confirmed entry (`P3`), so the map and the canon find each other.

**story**: a case or event they tell.

```json
{ "id": "s2", "type": "story", "text": "Turning down the agency retainer in 2019",
  "teaching": false, "versions": [ { "quote": "...", "source": "essay-04" } ] }
```

`teaching: true` for a case they use to teach that isn't about what they did (`CLAUDE.md` rule 1).

**term**: a framework, model or coined term.

```json
{ "id": "t1", "type": "term", "text": "Network design", "credit": "",
  "versions": [ { "quote": "...", "source": "workshop" } ] }
```

`credit`: who they credit when it's borrowed; empty when it's theirs.

**root**: a question for the interviews about what a spine claim grows from. Never a value, never an answer.

```json
{ "id": "r1", "type": "root", "text": "What did it cost you, the first time you picked a client for who they were and not what they paid?" }
```

**(checked: a root's text ends with a question mark.)**

Optional on any node: `first` and `last` (dates of the first and last piece it appears in; the script fills them from the sources when left out).

## links

```json
{ "from": "s2", "to": "c4", "kind": "carries", "evidence": ["essay-04"], "note": "" }
```

- `from` and `to` **(checked: node IDs)**.
- `kind` **(checked: one of these)**:
  - `supports`: one claim gives a reason for another.
  - `example_of`: a story or case shows a claim.
  - `carries`: a story proves a claim (stronger than an example: the claim rests on it).
  - `same_as`: two claims say one thing; usually merged instead, kept as a link only when the person should pick.
  - `tension`: two claims pull against each other.
  - `replaced_by`: the person used to hold `from` and now holds `to` (set only on their answer to a "how the thinking changed" finding or a tension; `from` is `held before`).
  - `comes_before`: one has to be true or done first.
  - `grows_from`: a spine claim grows from a root question (`to` is the root).
  - `uses`: a claim uses a term or framework.
- `evidence` **(checked: at least one source ID, except `grows_from`)**: the pieces where both sit, or the piece whose line connects them.

## findings

```json
{ "id": "f3", "kind": 3, "title": "Your pricing posts and your client posts make one argument you haven't written",
  "what": "Two or three sentences in plain words: what the studio sees.",
  "evidence": [ { "quote": "...", "source": "essay-03" }, { "quote": "...", "source": "post-05" } ],
  "nodes": ["c4", "c9"],
  "action": { "type": "post", "text": "A post on why the client you pick sets your price, not the other way round" },
  "rank": 1, "review": true, "status": "open", "answer": "", "new": false }
```

- `kind` **(checked: 1 to 12)**: the kinds in `skills/job-think`, "What it looks for". `title`: one line the person can read on its own, concrete, no studio words.
- `evidence` **(checked: at least two items, each with a `quote` and a source ID; a kind 12 finding's quotes come from private sources only, and a kind 6 finding may have one)**.
- `nodes` **(checked: node IDs)**: what the finding is about, so the picture can light them up.
- `action.type` **(checked)**: `post` (a piece to write), `question` (for the interviews), `confirm` (a yes or no). `action.text`: the post idea, the question, or what a yes would mean.
- `rank`: 1 is the strongest. `review: true` for the ten shown in the review **(checked: at most ten)**.
- `status`: `open`, `yes`, `no`, `renamed`, `not sure`. `answer`: the person's words when they gave more than yes or no, kept raw (`CLAUDE.md` rule 3); a `no` keeps the reason, so no later run raises it again.
- `new`: true for a finding a map update added, until the person has seen it.
