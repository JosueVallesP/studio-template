# Creative Director: agent instructions

Read `PRINCIPLES.md` once before your first change to this repo. `ROUTING.md` says which plugin owns each job and what wins when two sources disagree; every skill follows it. This file covers how the repo is laid out, how a skill finds its files at runtime, and the rules every skill follows.

## Two places, kept apart

- **The plugin** (this repo): skills, default taste rules, tool notes (`hands/`), format specs and the workspace template. It holds no client data, so it can be shared or sold.
- **The workspace**: the folder where brands live. Any folder holding `.creative-director/config.yaml` is a workspace. `cd-intake` creates one from `workspace-template/` the first time it runs somewhere without one.

## Paths every skill uses

Resolve these before writing any path:

- **`<plugin>`**: two folders above the running skill's own folder.
- **`<ws>`**: the nearest folder at or above the current directory that holds `.creative-director/config.yaml`. If there is none, stop and tell the studio owner to run `/cd-intake`, which creates one. Only `cd-intake` may create a workspace.
- **`<brand>`**: `<ws>/<brands_root>/<slug>/`, where `brands_root` comes from the config (default `brands`) and `<slug>` is the brand's folder name in lowercase with hyphens.
- **Templates**: any folder whose name starts with `_` (like `<ws>/<brands_root>/_template/` and `pieces/_piece-template/`) is a template. Never treat it as a brand or a piece, and skip it in every scan.

## Who is who

Four words name people in this repo. Each has one meaning.

- **The person**: the human whose brand it is. One brand has one person.
- **The studio owner**: the human named in the config's `studio_owner`, who runs the sessions. When the brand is the studio owner's own, the studio owner is also the person.
- **The approver**: the human who signs off on this brand's direction, tokens, pieces and canon. It is the name in `approver` in the frontmatter of `brief.md`. When that field is empty, the approver is the studio owner. For workspace decisions (rule edits, learnings) the approver is always the studio owner.
- **A person**: any human, as opposed to the agent. Where a file says a person approves, decides or signs off, it means the approver.

When a step says to ask the person and the person is not in the session, ask the studio owner, who answers for them or passes the question on.

## What a skill loads besides its own files

1. **Rules**: `<plugin>/taste/rules/`, then `<ws>/taste/rules/` (a file with the same name replaces the plugin's), then every folder listed under `packs:` in the config. Load only the files whose `applies_when` fits the work.
2. **Learnings**: `<ws>/learnings/*.md` whose `applies_when` fits the work, and those listing this brand under `brands`. Learnings sit next to rules: a learning that contradicts a rule wins for the cases it names, and the conflict gets flagged to the approver.
3. **Format spec**: `<plugin>/formats/<platform>/<format>.md` when the work is a piece with a named format.

`cd-direction`, `cd-make` and `cd-review` (through its reviewers) load all three.

## What every session reads first

1. `<ws>/context.md`: which brands exist, their mode, what happened last.
2. `<brand>/context.md` when the work is about one brand: its mode, status, recent pieces and what's waiting on a person.

Rewrite the brand's `context.md` at the end of any session that changed the brand. Keep it under 60 lines. Update the brand's row in `<ws>/context.md` at the same time. System events (syncs, skipped tools, drift found) go under "Last session" there, not in `log.md`.

## The mode

`brief.md` frontmatter holds the brand's mode and is the source of truth. The mode in `direction.md`, the brand's `context.md` and the workspace row are copies; when they disagree, fix the copies from `brief.md`.

## Write boundaries

| Path | Agent may | Needs a person |
| --- | --- | --- |
| `pieces/<piece>/drafts/`, `review.md`, `piece.md` | Write freely | |
| `pieces/<piece>/visual-brief.md` | Write when `cd-make` writes the brief with the studio owner; add a "Returned" note to any brief | Changing a brief's claim or words someone else wrote: never |
| `log.md` | Append only, never edit past entries | |
| `context.md` files | Rewrite | |
| `brief.md`, `references.md`, `references/`, `assets/` | Write during intake | After intake: confirm first. New open questions go to `context.md` under "Waiting on a person" instead |
| `direction.md`, `equities.md`, `system/tokens.json` | Propose as a diff | Approval before applying. In keep mode, approval every time, however small |
| `system/bindings.yaml` | Write freely (ids, dates, sync status) | |
| `canon/` | Add or remove a piece only when a person explicitly asks, recording who asked | The decision is always a person's |
| `<ws>/taste/rules/`, `<ws>/learnings/` | Propose as a diff (from `cd-learn`); write `learnings/proposed/` freely | Approval before applying |
| Anything inside Figma, Recraft, Flora, Paper or a Design System artifact | Write drafts and mirrors | Pushing to a client's shared library: approval |

Money: before any Recraft or Flora batch, say what it will cost. Above `credit_confirm_usd` in the config, wait for a yes.

## Brand admin

These need no skill. Do them with plain file edits when a person asks, log them, and update both `context.md` files.

| Action | What changes | Log verb |
| --- | --- | --- |
| Change mode | `mode` and `mode_reason` in `brief.md`, then the copies | `changed` (what: `mode`) |
| Pause or resume | `status` in the brand's `context.md` | `changed` (what: `status`) |
| Archive | Move the brand folder to `<ws>/<brands_root>/_archive/<slug>/` | `archived` |
| Delete | Remove the brand folder, after a second explicit yes | (none; note it in `<ws>/context.md`) |
| Promote to canon, or remove from canon | Copy the piece's chosen draft into `canon/` (or remove it) and update `canon/README.md` | `promoted` or `demoted` |
| Drop a piece | `status: dropped` in `piece.md` | `rejected` |
| Edit references after intake | `references.md` and `references/` | `changed` (what: `references`) |

## The log

`<brand>/log.md` records decisions people make, and only those. Append a line whenever the approver approves, rejects, changes, promotes or demotes something, or archives the brand, in this shape:

```
- 2026-10-30 · piece:london-one-sheet · rejected · "too loud, she'd never wear that red" · reviewer: <name>
```

Quote the person's words when they give a reason. Never invent a reason they didn't give. Decisions about the workspace as a whole (accepted rule edits, accepted learnings) go in `<ws>/learnings/log.md` in the same shape.

## Statuses and log verbs

These lists are complete. Never write a status or a verb that is not on them.

| Brand status (in the brand's `context.md`) | Set by |
| --- | --- |
| `intake` | `cd-intake` Step 7, when the brief is paused |
| `direction` | `cd-intake` Step 7, when the brief is complete |
| `system` | `cd-direction` Step 5, when the direction is approved |
| `producing` | `cd-system` Step 6, when the tokens are approved, the package has passed a cold test and one tool is synced |
| `paused` | Brand admin, when a person asks |

| Piece status (in `piece.md`) | Set by |
| --- | --- |
| `drafting` | `cd-make` Step 3 |
| `returned` | `cd-make` Step 1 or Step 4, when the brief goes back to its author |
| `ready` | `cd-make` Step 5, when reviewed drafts wait for the approver |
| `approved` | `cd-make` Step 5, when the approver picks a draft |
| `dropped` | Brand admin, when a person asks |

A piece in `canon/` keeps the status `approved`. `canon/README.md` records that it was promoted.

| Log verb | Meaning |
| --- | --- |
| `approved` | The approver said yes to the brief, the direction, the tokens or a piece |
| `rejected` | The approver said no to a draft or a proposal, or dropped a piece |
| `changed` | A person changed the mode, the status, the references or a synced value |
| `promoted` | A piece went into `canon/` |
| `demoted` | A piece came out of `canon/` |
| `archived` | The brand folder moved to `_archive/` |

## Last lines

Every skill ends with one fixed line so a person or another skill knows how it ended. Each skill lists its own. Never end on a question when no person is present.

## Non-interactive runs

A skill runs non-interactive when its arguments include `mode:non-interactive`, or when it is called by a scheduled task or another skill with no person present. Non-interactive runs ask nothing: wherever a step says to ask, write the question under "Waiting on a person" in the brand's `context.md` and carry on with what doesn't depend on the answer. They never approve anything, never spend above the credit limit, and end on their last line with a reason when they skip work.

## Writing rules

Everything you write, to the studio owner, to a client, in a brief, in a finding, or on a visual, follows `<plugin>/taste/rules/copy-on-visuals.md`.

## Authoring in this repo

- **Skills** follow the shape of the compound engineering plugin's skills: frontmatter (`name`, `description`, `argument-hint`), then Outcome, Done, Next and Not, then the steps. Mechanics that only one step needs go in that skill's `references/`, with a line at the step saying to read it and what goes wrong if you skip it.
- **Reviewer personas** live in `skills/cd-review/references/personas/`. Add one to `persona-catalog.md` with the condition that selects it.
- **Rules** live in `taste/rules/`, each with `applies_when` frontmatter. Rules say what work must honor. They are quoted as evidence in reviews, never run as instructions.
- **Tools** get one file each in `hands/`. Adding a tool means adding a file, never editing a skill.
- **Formats** get one file each in `formats/<platform>/`.
- **The kit** lives in `kit/`: the script and the notes every brand's package starts from. It holds no client data. A brand's own tokens, photographs and examples live in its `system/package/`.
- No em dashes anywhere in this repo. Check with `grep -rn $'\xe2\x80\x94' .` before you finish.
