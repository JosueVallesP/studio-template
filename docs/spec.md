# Content Studio: the design

This page holds the studio's current design: what it is built on, what it stores, who does what and where it stops for the person. `CLAUDE.md` holds the rules every task follows, and this page refers to them by number instead of repeating them. `docs/state.md` says what is built. The design as it was written before the build, with the reasoning behind each part, is `docs/history/spec-2026-10-19.md` in the studio repo (it doesn't ship to clients); where the two differ, this page wins.

## Why the studio exists

The studio is a garden for one person's ideas. The person plants the seeds and decides what's worth growing; the studio plants, feeds, strengthens, prunes and harvests with them, and never plants an idea of its own. `CLAUDE.md` opens with what each of those five jobs means, and the test that follows from it: a part that does none of them doesn't belong.

The harvest is where the five jobs pay off, and where an AI writing for a person goes wrong if the garden is thin. It guesses wherever it lacks something: what they believe, which stories are true, who the reader is, how they sound, what the picture should be, whether the piece is ready. Each guess lands on the most common answer, and the most common answer is what makes a piece sound like nobody. So the garden holds what removes each guess before the writer reaches it.

| What the AI would guess | What removes the guess |
| --- | --- |
| What the person believes and would never say | The brand tree |
| Stories, examples, numbers, client cases | `material/`, the stories and proof in the canon, the idea bank |
| Who the piece is for and what they already want | The brand strategy, the audience file and the brief |
| The shape and length of the piece | The format skills |
| How it sounds | The voice guide and the rewrites the person made |
| How it looks | The visual identity and the Figma kit |
| Whether it's true, good and ready | The judge in a fresh context, then the person |

A part that removes no guess only adds text for the AI to read, and extra text dilutes the parts that matter.

## Principles

1. **Facts about the person come from the person.** Stories, numbers, clients, results and quotes come only from the four places in rule 1. A missing fact is asked for or blocks the piece. It is never filled in.
2. **The writer thinks.** The reasoning, the framing, the analogy, the answer to an objection and the outside example are the writer's own work, marked in the source map with the kinds rule 1 defines. A draft that only restates the person's entries isn't finished.
3. **The person confirms.** Nothing about the person enters the canon until they say yes (rules 2 and 6). Their words are kept as rule 3 says.
4. **The studio stays generic.** Skills hold procedures and standards and never a fact about a person (rule 5). Everything about one person lives in their own files, so one studio serves anyone and improves in one place.
5. **One way to make a piece.** The person shapes the idea in the job command's stops, the writer drafts, the judge reads it cold, and the person decides. The garden around it (capture, `/harvest`, the librarian, the tending run) keeps the ideas growing between pieces. Until 0.89 there was also a pipeline with a brief to approve; it folded into the job commands, because the stops already do what the approval did, with the person shaping the idea instead of signing off on a plan.
6. **The judge never wrote the piece** (rule 4). Judging runs in a fresh context that reads only the files.
7. **One idea, one place, one ID.** Each value, POV, branch, story and proof entry lives once, with a short ID. Briefs and drafts cite IDs, so every piece traces to its roots and the editor can check where each claim came from.
8. **Fixed rules go into scripts.** A rule that never needs judgment (em dashes, banned words, a source map whose IDs resolve) runs as a mechanical check instead of something the AI must remember.
9. **Slow and fast layers stay apart.** The person layer changes yearly, the vehicle quarterly, the idea bank daily. Keeping them in separate files stops stale facts from leaking into new pieces.

## The brand tree

The brand tree is the model the canon follows. Values, behaviors and POVs are the roots. The philosophy and the thesis are the trunk. Branches are the core ideas and frameworks. Pieces of content are the leaves. The exact fields of every entry, with weak and strong examples, are in `skills/setup-brand-tree/references/fields.md`; this section says what each part is for.

### The person layer

This layer says what the person can honestly be known for. It changes slowly and gets reread about once a year.

- **Values (V1 to V3).** One to three values, ranked. They are the few that win when two good things conflict, each with what it beats, what it costs and a story where the person chose it under pressure. The strategist uses them to pick angles; the editor uses them to catch a draft that contradicts the person. A list of everything someone cares about tells a reader nothing, which is why the list stays short.
- **Behaviors (A IDs).** How the person acts on their values, stated so someone could observe it, refusals included, each tied to a value and backed by a story or proof. Behaviors prove the values are real and feed most story-based content.
- **POVs (P IDs).** Claims about how the field should work, each specific enough to disagree with, naming the common view it rejects, with its ground (what they saw), evidence, its condition (when it's true) and a confidence (firm, forming or exploring). POVs make content distinct. Rule 2 says when a forming or exploring POV may feed a piece.
- **Philosophy.** Half a page to a page that connects the POVs into one logic, tested under four lenses: what's true about the field, how we know it, how things should be read, and what it's all for. A gap under a lens is a flag to look at. The philosophy keeps new arguments from contradicting old ones.
- **Thesis (T).** The one claim the person wants to be known for, with its catalyst (what they saw that others didn't, when, and why it made them act, backed by a story), who it's for, what it changes, what would prove it wrong and the branches that hold it up. The thesis is the filter: an idea that doesn't connect to it gets turned down.
- **Branches (B IDs).** Three to seven core ideas and methods, ranked, each needing a long piece to explain: the problem it solves, its parts, its origin, its limits, its key terms in plain words and its natural visual form.
- **Stop list (X IDs).** Topics, claims, names and words the person refuses. The AI drifts most in negative space, because nothing tells it what's missing on purpose.

### The vehicle layer

This layer says what the person needs to be known for. It moves with the business and gets reviewed every quarter.

- **Goal.** What the person wants to have happen, with a rough date, worked backward: what they need to be known for, what they need to do for that, and what they need to learn.
- **Vehicle (O and C IDs).** The business in a paragraph, each offer with its status (`draft`, `confirmed` or `retired`, like every entry) and its `availability:` (open, waitlist or closed), the proof with its permission, the current priorities and the approved calls to action. It keeps a piece from promoting a closed offer or citing a result the client never cleared.
- **Brand strategy (G IDs).** The segments in their own words, the target association (the first thing people should think of at the person's name), the anti-associations, the channels and the path from a piece to a conversation. `strategy-brand` writes it with a reason for every choice; the method is `docs/strategy-method.md`.
- **Audience (D IDs).** Per segment: the stage of awareness, the desires it already has, scored by the person, and what readers would say out loud about each desire and what they'd never admit, taken from real words. Content can't make people want the thesis; it can only connect the thesis to something they already want.
- **Content plan.** Rewritten each quarter: the reputation gap, the quarter's branches and why, each branch paired with the desires it answers, and the mix across the layers of the tree.

Each layer of the tree makes a different kind of piece, and the content plan sets the quarter's mix across them:

| Layer | Kind of piece | What it does for the reader |
| --- | --- | --- |
| Thesis and catalyst | The origin piece | Says what the person stands for and why |
| Values and behaviors | Stories of choices and refusals | Builds trust |
| POVs | Opinions that name what they reject | Sets the person apart |
| Branches | Frameworks, methods, long essays | Shows how the person thinks |
| Proof and vehicle | Cases, results, offers | Shows it works and what to do next |
| Philosophy | Rare long pieces, the About page | Ties it together |

The mix also follows the segment's stage of awareness. Readers who don't see the problem yet get stories and behaviors. Readers who know the problem, or know solutions exist, get the desire first, then POVs and branches. Readers who know the person get proof. Readers ready to buy get the offer and a reason to act now.

### Where the two layers meet

The person layer builds up to what the person can honestly be known for. The goal works down to what they need to be known for. The target association sits where the two overlap, and it must also answer a desire a segment already has. When the goal needs a reputation the person layer can't support, the goal or the vehicle changes. The canon never does, because content built on beliefs the person doesn't hold won't sound like them.

### Voice

The voice guide holds checkable rules with before and after examples, approved and rejected samples, the person's own vocabulary and their register by channel. Spoken material beats polished writing as a source, because it carries their real rhythm. The best voice data is the pair of a studio draft and the person's rewrite, which the studio keeps in `bank/rewrites/` and the writer reads before every draft.

## The fractal structure

A body of work is one claim expanded at every scale, and every unit has the same shape as the whole.

| Scale | What it is | Relation to the level above |
| --- | --- | --- |
| Thesis | The one claim | The generator |
| Branch | The thesis applied to one area or method | Expands it |
| Leaf | A branch applied to one case, step or objection | Expands it |
| Fragment | One line: a reply, a headline, a bio line | Compresses it |

Every unit, at every size, has four parts: a claim, why it's true, evidence, and what it changes for the reader. A fragment holds them in one sentence; an essay holds them in sections. Each unit links to the one above by its parent ID, so every brief on the pipeline names a parent, and the body-of-work index (`pieces/index.md`) shows the map, with pieces that have no parent and branches that have no leaves.

Two tests follow from the shape. Zoom out: a reader who sees only this piece could guess what the person believes overall. Zoom in: the piece could be expanded into something longer without inventing anything. The strategist picks by gap: a branch with no leaves, a leaf that drew replies and was never expanded. Growth comes from going deeper into the tree, and a new branch is allowed only when it grows from the thesis.

## The person's files

What lives in `canon/` and `bank/` is listed here; which paths belong to the person and which to the studio is in `studio.manifest.yaml`, the only source for that split.

### The canon (`canon/`)

| File | Holds | IDs |
| --- | --- | --- |
| `person/values.md` | One to three ranked values | V1… |
| `person/behaviors.md` | Observable behaviors and refusals | A1… |
| `person/povs.md` | Claims about the field | P1… |
| `person/philosophy.md` | The worldview under the four lenses | none |
| `person/thesis.md` | The one claim and its catalyst | T |
| `person/branches.md` | Core ideas and frameworks, ranked | B1… |
| `person/stop-list.md` | What the person refuses | X1… |
| `bank/stories.md` | Confirmed stories, with permission | S1… |
| `bank/proof.md` | Confirmed results and numbers, with permission | R1… |
| `vehicle/vehicle.md` | Goal, business, offers, calls to action, priorities | O1…, C1… |
| `strategy/outcomes.md` | What the person wants from the studio, in their words | none |
| `strategy/brand-strategy.md` | Segments, target association, anti-associations, channels | G1… |
| `strategy/audience.md` | Per segment: awareness, desires, what readers say and won't say | D1… |
| `strategy/content-plan.md` | The quarter's gap, branches, pairs and mix | none |
| `strategy/channels/<channel>.md` | One channel's job, formats, cadence and signals | none |
| `voice/voice-guide.md` | Voice rules, vocabulary, samples | W1… |
| `visual/brand-assets.md`, `visual/design-system.md` | What the person gave about their look; the identity built from it | none |
| `core-summary.md` | A one to two page digest that loads on every job | cites IDs |
| `canon-index.md` | Every ID with one line, its file and its status | all |
| `progress.md`, `setup-progress.md` | Where the interviews and the setup stand, and the minimum canon list | none |

Every entry is a heading with its ID first, then labeled fields in a fixed order, so scripts can parse them and checks can find empty ones. IDs are never reused or renumbered. Every entry has a status of `draft`, `confirmed` or `retired`; rule 2 says which feed content. An entry with no source stays `draft`. Entries point to each other by ID and never restate each other.

The minimum canon the strategy needs is defined once, in the "Minimum canon" list of `canon/progress.md` (template in `skills/setup-brand-tree/templates/progress.md`). The job commands don't wait for it.

### The working banks (`bank/`)

| File | Holds |
| --- | --- |
| `bank/ideas.md` | Raw captures, word for word, one idea each (I IDs), with source, type, links, strength, permission and where they were used |
| `bank/credibility.md` | What backs the person, one fact each (K IDs): results, clients, what people said about them, before and afters, track record, recognition, artifacts, who vouches; numbers as given, what it backs, permission, when last checked. Filed in the same pass as the idea bank |
| `bank/questions.md` | Questions from readers and clients, in their words |
| `bank/evidence.md` | One line per mention of something new to the canon, which the librarian counts |
| `bank/rewrites/` | Each studio draft the person rewrote, beside their version, with what changed and the rule each change touches (an H or W number, `new` or `piece`) |

An idea bank entry's status is `raw` (something is missing), `ready` (complete and usable), `used` (a shipped piece carries it) or `archived`. Rule 2 says `ready` and `used` entries feed content. Every entry carries a `permission:` of `public`, `anonymize` or `private`. Raw text stays raw; a summary sits beside it and never replaces it.

`material/` holds what the person has already made, read directly by every job command. `inbox/` is where they drop raw input for `/capture`. `proposals.md` holds changes to confirmed entries, contradictions and `seen` connections, waiting for their yes; a newly found belief, story, method or offer goes in as a `draft` entry in its file instead (rule 6).

## The crew

Each role does one job, reads only what that job needs and hands off through files. No role depends on what another said in a chat. In Claude Code each role is also an agent in `.claude/agents/` with a clean context.

| Role | Its one job | Never |
| --- | --- | --- |
| Capture | Turns raw input into idea bank entries in the person's words, and logs what's new to the canon as evidence | Rewords the raw text, or writes the canon |
| Harvest | Lists the ideas most ready to become a piece, by how grown they are and where the body of work is thin (`skills/role-strategist`) | Briefs, drafts, or lists a seed whose meaning the person hasn't confirmed |
| Writer | Drafts once the stops are agreed, with a source map | Invents a fact about the person, or judges its own draft |
| Judge | Judges every draft in a fresh context through the gates table in `skills/role-editor` | Rewrites the piece, or reads the writer's reasoning |
| Producer | Records the person's decisions in their words and moves the piece on | Decides for the person |
| Librarian | Diffs finals against drafts, counts the evidence, proposes canon changes, keeps the body-of-work index true | Changes the canon, or proposes from one mention |

The producer is the person. The skill of that name is the clerk that writes down what they decided.

One piece moves like this:

1. Capture turns what happened into idea bank entries (seeds); the tending run and the first wind feed them and bring them pushback.
2. `/harvest` lists the ideas most ready to become a piece, or the person hands one over.
3. `/post` or `/essay` builds it with them in stops: what they're saying, the openings, the outline.
4. The writer drafts in a fresh context, and the mechanical checks run on the draft as it's written.
5. The judge reviews it in a fresh context.
6. The writer revises once if it's needed.
7. The person ships, revises, holds or kills it, and asks for the picture with `/visual` when they want one.
8. The librarian reads what the person changed, counts what repeats, proposes canon changes and adds the piece to its seed's fruit.

### Piece states

A piece's state lives in one place: the `status` field in its `brief.md` frontmatter.

| State | Set by | Next |
| --- | --- | --- |
| `briefed` | `/post`, `/essay` or a selling tool, as the stops go | The writer, once the stops are agreed |
| `drafted` | Writer, after the mechanical checks | Judge |
| `reviewed` | Judge, with a verdict of pass, revise or redo | The person on pass; writer on revise (once); the command that made it on redo, back at stage 1. After the revision it goes to the person whatever the verdict |
| `revised` | Producer, when the person sends a reviewed piece back with notes | Writer |
| `shipped` | Producer, with `final.md` holding what was published | Librarian |
| `killed` | Producer, with the reason | Librarian |
| `held` | Producer, with the reason and a date to look again | The person, on that date |
| `blocked` | Any role missing a fact or an input it can't guess | The person answers; the producer moves it on |

Pieces from before 0.90 may still say `brief-approved` (the writer drafts it), `designed` (the person decides) or `path: pipeline`; they're read the same way.

Each piece is one folder in `pieces/`: `brief.md`, `draft-vN.md`, `review-vN.md`, the visual files, `final.md` and `log.md`, with one dated line per action. The templates are in `templates/piece/`. Fixed files mean the next role reads a file instead of a conversation, and any role can rerun alone.

### Permissions

Each crew agent writes only its own files. The lists in `.claude/hooks/guard-writes.py` are the source; this table summarises them, and where the two differ the hook wins. Every crew agent may also write `studio-notes.md`, `proposals.md` and `pieces/*/log.md`.

| Role | Writes |
| --- | --- |
| Capture | `bank/ideas.md`, `bank/credibility.md`, `bank/questions.md`, `bank/evidence.md`, `inbox/*` and `inbox/**`; in `canon/bank/stories.md` and `canon/bank/proof.md`, only `also:` blocks added to an existing entry |
| Writer | `pieces/*/draft-*.md`, `pieces/*/brief.md` |
| Judge | `pieces/*/review-*.md`, `pieces/*/brief.md` |
| Librarian | `bank/evidence.md`, `bank/ideas.md`, `bank/credibility.md`, `pieces/index.md`, `pieces/librarian-last-run.md`, `pieces/*/brief.md` |

`/capture` and `/librarian` launch their crew agent, so these lists apply to them; `/post` and `/essay` launch the writer and the judge. Every role reads what its skill names. A second hook, `.claude/hooks/guard-bash.py`, limits the commands each crew agent may run to its own short list of the studio's scripts and read-only git. The main session, with the person present, is never limited by either hook: setup, `/learn` and `/review` write the canon with the person in the room, and the main session and the job commands keep rule 6 by instruction. `docs/hooks.md` describes all six hooks.

### Gates

Two points need the person, and everything between them runs without stopping:

1. **The stops.** What the piece says, the opening and the outline, each agreed before the next. The cheapest place to fix a piece.
2. **The final decision.** Ship, revise, hold or kill.

And whenever a piece turns up something worth keeping, canon confirmation: a draft entry feeds content, and a proposal changes a confirmed entry, only after the person says yes.

### Reviews

The judge grades every failure through one gates table in `skills/role-editor`: each gate is pass, revise or redo, and the verdict is the worst grade. Ranked issues follow, with their lines quoted, and at most three "should" lines that are not graded. The detector call follows the paragraph in `CLAUDE.md`: once per piece on its first judged draft, and once on a shipped final that differs from the last draft. Its label is a reading, never a reason to rewrite.

## Setup

Setup runs in this order, conducted by `/start` (`skills/setup-start`), with the words for each stage in its "Every stage, explained" table:

1. **Intake.** A short set of questions about facts (the list is `docs/intake-questions.md`), inside Claude (`setup-intake`) or as a form whose answers `scripts/build-instance.py` builds from. It writes the person's tool settings, outcomes, brand assets and `YOUR-STUDIO.md`.
2. **Quick wins,** before any interview: the map of the person's ideas (`job-map`: everything they've handed over read as one body of work, the findings they can't see from inside, a tree to open in a browser, a 20-minute review, and draft entries for the interviews), the Figma kit (`setup-figma`), the dashboard (`setup-notion`), a look at the libraries the studio came with (`setup-libraries`) and a first post from their own material (`setup-first-post`). Every tool is optional; without one, the studio works in files.
3. **The interviews** (`setup-brand-tree`), in short sessions, until the minimum canon holds. They never gate the job commands: a person can make posts and essays from their material from day one, and `/strategy` gives a draft plan from material that the interviews then confirm. A person who skips the interviews gets the stage `interviews-skipped`, which counts as done for routing and for the check.
4. **The strategy** (`strategy-brand`).
5. **The manifesto** (`job-manifesto`), optional, once the thesis is confirmed.
6. **Make it yours** (`setup-visual-identity`): the look built from the canon and applied to the kit and the dashboard.
7. **The check** (`setup-check`): the install, the minimum canon (or, after `interviews-skipped`, what the direct path needs), the strategy and one test piece through the crew.

## Ownership and updates

`studio.manifest.yaml` is the only source for which paths belong to the studio and which to the person. An update (`scripts/update-studio.sh`, `/update`) replaces the studio's paths and never touches the person's. A path the manifest doesn't name belongs to the person, so a mistake never overwrites their work. A change one person needs goes into their files, or becomes a studio change everyone gets. Each instance carries `studio-source.md`, naming the studio version it runs.

## Failure rules

- **A missing fact about the person blocks the piece.** A story, a number, a client, a result or a quote the sources don't hold sets the piece to `blocked`, with a list of what's missing. No role fills that gap itself.
- **Reasoning and borrowed examples are the writer's.** They aren't gaps. They go in the source map as `writer` or `borrowed: verify` (rule 1), and the judge checks them for truth instead of for a source.
- **A fact with no source is a revise or a redo.** The gates table in `skills/role-editor` says which: a new fact is a redo, a stretch of a confirmed entry is a revise.
- **Two canon entries that contradict each other** go to the person as a proposal that asks which is right.
- **A path a skill names must exist.** A missing file blocks the piece instead of letting the model improvise.
- **A skill change that makes the test set worse gets reverted.** The tests are in `tests/`, and they rerun after any change to a skill or a library card.
