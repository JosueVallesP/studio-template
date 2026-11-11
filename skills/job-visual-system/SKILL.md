---
name: job-visual-system
description: >-
  Builds the person's own visual system and keeps it in their studio: an intake about how they want to look, three directions shown across real pieces for them to choose from, and one system (mark, colours, type, shapes, rules) with exact values. The package that makes pieces from those values comes in a later version. Runs the creative director method that ships in `visual-system/`, one stage per run, with every approval left to the person. Use for /visual-system, "build my visual system", "show me directions for my brand", "make my brand package", "what stage is my visual system at".
---

# /visual-system

Method by Josué Valles, the studio's author.

A visual system is what lets a feed look like one person made it. It is built in a fixed order, because each step is cheap to change and the next one is not: what the person wants to be seen as, then three directions they can compare on real pieces, then one system with exact values, then a package that makes pieces without anyone redrawing the brand.

This skill does not hold the method. It routes to it. The method is three sets of skills that ship with the studio in `visual-system/` and work as one:

| Set | Folder | Skills | What it owns |
| --- | --- | --- | --- |
| Creative director | `visual-system/creative-director/` | `cd-intake`, `cd-direction`, `cd-system`, `cd-make`, `cd-review`, `cd-learn` | The order of work, the brand folder and every approval |
| Art direction | `visual-system/art-direction/` | `ad-brief`, `ad-rules`, `ad-board`, `ad-critique` | Methods a creative director step calls by name |
| Design | `visual-system/design/` | 17 skills named `dsn-*` | Craft checks and the default numbers for a canvas |

`visual-system/creative-director/ROUTING.md` says which set owns each job and which source wins when two disagree. Read it once before the first run.

## How a skill is found

These skills are not installed as commands. When a step names one, read its file and follow it:

- `cd-<name>`: `visual-system/creative-director/skills/cd-<name>/SKILL.md`
- `ad-<name>`: `visual-system/art-direction/skills/ad-<name>/SKILL.md`
- `dsn-<name>`: `visual-system/design/skills/dsn-<name>/SKILL.md`

Read `visual-system/creative-director/CLAUDE.md` and `PRINCIPLES.md` in the same folder once before the first stage. Two of their path rules are fixed here, and these lines win:

- **The plugin folder** is `visual-system/creative-director/`.
- **The workspace** is the folder `visual/` at the top of this studio. It is the person's. `cd-intake` makes it the first time, by copying everything inside `visual-system/creative-director/workspace-template/` into it, the hidden `.creative-director/` folder included. The brand folder is `visual/brands/<their-name>/`.

Nothing in `visual-system/` is ever edited in a person's studio. An update replaces it. What the person changes lives in `visual/` (their rules in `visual/taste/rules/`, their learnings in `visual/learnings/`).

## Before the first stage

Read what the studio already knows, so the intake asks only for what is missing:

- `canon/`: the brand tree, the voice guide and the audience, when they exist.
- `canon/visual/`: a Contradiction Brief from `/identity` or `/genius-of-contradiction`, and `design-system.md`, when they exist. A contradiction the person confirmed is the strongest input a direction can have.
- `config/tools.md`: which tools are connected (Figma, an image model).
- The person's own photographs, when they have handed any over.

Then propose, as `skills/craft-house-rules` S3 says: make the next thing from what is on file and let the person react. Never open with a list of questions.

## The stages

One stage per run. Say where the person is and what the stage gives them before it starts (`CLAUDE.md` rule 7).

| # | Stage | Skill | What the person gets | What they decide |
| --- | --- | --- | --- | --- |
| 1 | Intake | `cd-intake` | A brief: what stays, what it means, references, their own photographs | The answers |
| 2 | Directions | `cd-direction` | Three directions, each shown on the same set of pieces, side by side | Which direction, or which parts of which |
| 3 | System | `cd-system` | The mark, colours, type, shapes and rules with exact values. The package comes in a later version | The values |
| 4 | Making | `cd-make` | A piece made from the package | Which draft |
| 5 | Review | `cd-review` | A verdict on a piece: pass, revise or sent back | Whether it ships |
| 6 | Learning | `cd-learn` | Proposed changes to their own rules, from what they corrected | Which to keep |

To find the stage, read `visual/context.md` and the brand's `context.md`. When `visual/.creative-director/config.yaml` doesn't exist, the stage is 1.

## The package

A package is one folder that holds a script, the values it reads, the fonts, the person's photographs, the rules and worked examples, with a README in the person's first person, so any AI session can make an on-brand piece from it. It lives at `visual/brands/<their-name>/system/package/`.

**The kit that builds a package is not in this version** (`visual-system/creative-director/kit/README.md` says why). So stage 3 runs as far as the approved values in `system/tokens.json` and stops before "Build the package". Say so in one line when the person reaches that point, and don't write a script of your own in its place. Until a package exists, `/visual` works as it did before, styled from the person's approved values.

## Images

`visual-system/creative-director/taste/rules/images.md` holds the rule. A generated image has to start from something of the person's: a story of theirs, a post, a photograph they took or sent. The person's own photographs come first.

## Money

Before any batch on a paid image tool, say what it will cost. Above the limit in `visual/.creative-director/config.yaml`, wait for a yes.

## Never

- Never approve a direction, a value, a piece or a package. Every approval is the person's.
- Never skip the three directions and go straight to one system.
- Never edit a file under `visual-system/`.
- Never put anything from another person's brand into this studio.
- Never run two stages in one run.

## Studio notes

Where this skill made a run guess (a path that didn't resolve, a tool that wasn't there), one line in `studio-notes.md`.
