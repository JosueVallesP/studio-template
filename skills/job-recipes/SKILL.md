---
name: job-recipes
description: Saves the way a person keeps chaining the studio's commands as a recipe they can run with one command. A recipe holds the order of existing commands and the person's own choices for each step (which source, which format, what to skip); it never holds a new method, a writing rule or a change to a studio skill. /end offers one when the same chain has shown up in three separate sessions; the person can also ask any time. Use for /recipes, "save this as a recipe", "make this a command", "I always do this", "run my Monday recipe", "show my recipes", "change my recipe", "retire this recipe".
---

# /recipes

People who use the studio for a few weeks settle into a few routines. One person drops in a call every Thursday, runs `/shape` on it, picks the strongest idea and asks for a short post. Another opens the week with `/scout`, then `/think` on the best two finds, then plans two posts. Each time, they say the same five things in the same order. A recipe saves that order and those choices, so the next time they say one command and the studio runs the rest.

## What a recipe is, and what it isn't

A recipe is a saved route through commands the studio already has. Each step names a command and the choices the person made for it, in their words: "only my calls with clients", "the short format", "skip the visual", "show me the plan before writing".

A recipe never holds:

- **A method.** How to find ideas, write a post or judge a draft lives in the studio's skills, which rest on the author's theory. A recipe that tried to say how to write would be a thinner copy of a skill. If the person wants a step done differently every time, that's a choice the step's command already takes ("the short format") or a voice rule (`/learn` keeps those), and it goes there.
- **A change to a studio skill.** The studio's skills belong to the studio, and every update replaces them. When the person keeps correcting the same thing in a command's output and it isn't a voice rule, write one line to `studio-notes.md` (`person keeps asking: <what>, in /<command>, <dates>`) and tell them it's noted for the next version of the studio. Never edit the skill.
- **Facts about the person.** Rule 5 holds for recipes too. A recipe may name a file to read ("my calls in inbox/"), never a belief, a story or a number.
- **A one-off.** A chain that happened once, or twice, is a session, not a routine.

When the repeated work has no command behind it (the person asks for the same thing by hand each time and no studio command does it), a recipe can't hold it, because a recipe only chains commands. Say so in one line, and write it to `studio-notes.md` as `missing command: <what they keep doing>, <dates>`.

## Where recipes live

- `recipes/<name>.md`, from `templates/recipe.md`: the recipe itself. Person-owned; an update never touches it.
- `.claude/skills/<name>/SKILL.md`: the shortcut that makes `/<name>` a command. Three lines: the frontmatter (the name and a one-line description in the person's words) and "Read `recipes/<name>.md` and run it with `skills/job-recipes`, 'Running a recipe'." The manifest names the studio's own commands one by one, so a person's shortcut survives every update.
- `recipes/archive/`: retired recipes. Never deleted; "bring back <name>" restores one and its shortcut.

## Naming

The person picks the name. Offer one from what the recipe does, in their words ("thursday-call", "monday-plan"), lowercase with hyphens. Before saving, check the name against every folder in `.claude/skills/` and every studio command in `studio.manifest.yaml`. A name that's already a command is refused, with the reason in a line and two other names to pick from.

If a later studio version ships a command with the same name, the update keeps the person's shortcut in `studio-local-backup/<date>/` and installs the studio's. The recipe file is untouched. `/recipes` notices a shortcut that no longer points at its recipe and asks for a new name.

## Offering a recipe (from /end)

`/end` writes one `ran:` line per session (`skills/job-end`, step 4): the commands the session chained, in order, each with the person's choices in a few of their words. This step reads those lines.

1. Read the `ran:` lines in `sessions/log.md` from the last 60 days.
2. Look for a chain of two or more commands that shows up in three separate sessions, in the same order, with the same choices or nearly the same. Today's session counts as one. Three times in one session is still one.
3. Skip a chain that's already a recipe, one the person turned down (a `recipe declined:` line in the log), and one that's only a single command with a choice (`/post` in the short format is a command, not a routine).
4. If one qualifies, offer it in one message, after `/learn` and before the session entry:

```
You've done this in three sessions now (<dates>):
1. /<command>: <their choice, their words>
2. /<command>: <their choice>
3. /<command>: <their choice>

Want me to save it as one command? You'd say /<suggested-name> and I'd run all three, stopping where you'd normally decide something. Yes, a different name, or no?
```

5. Offer at most one recipe per session, the chain with the most sessions behind it. On yes, save it ("Saving a recipe" below). On no, write `recipe declined: <the chain>` to the session entry, so it isn't offered again unless the person asks.

When `/end` runs with nobody there to answer, skip this step.

## Saving a recipe

On an offer accepted, or when the person asks ("save this as a recipe", "make this a command"):

1. Write out the steps from what the session did, each with its choice in the person's words. When they asked mid-session, read back over the session to get the steps; ask only for what isn't clear.
2. Mark the stops. A recipe runs straight through except where a person decides: a plan to approve (`/post` shows one), an idea to pick from `/shape`'s cards, a draft to read. Keep every stop the commands already make, and name them so the person knows where the recipe will pause. A recipe never skips a stop its command needs, and never answers one for the person.
3. Show it back as it will be saved: the name, the steps, the stops. Ask "save it like this?"
4. On yes, write `recipes/<name>.md` and the shortcut, then say in one line: "Saved. Say /<name> to run it."

## Running a recipe

1. Read `recipes/<name>.md`. Say the steps in one line before starting ("Pulling your latest client call, then shape, then a short post. I'll stop at the ideas and at the plan.").
2. Run each step by reading its command's skill and following it exactly, with the recipe's choices handed in as if the person had said them. Each command's own rules hold, every check and hook included. The recipe only saves the person from saying the choices again.
3. At each stop, wait for the person. If they change a choice there ("long this time"), use it for this run only and keep going.
4. If a step can't run (the inbox is empty, a source isn't connected), stop there, say what's missing and what the steps after it need, and let the person choose.
5. At the end, update `last run` in the recipe file and add the run to the recipe's log. If the person changed the same choice in two runs in a row, ask whether to change the recipe.

## /recipes on its own

- `/recipes`: the person's recipes, one line each (name, what it does, last run), and any shortcut that no longer points at its recipe. No recipes yet: say what a recipe is in two lines and that `/end` will offer one when a routine shows up.
- "change <name>": show the steps, take the change, show it back, save. The shortcut stays.
- "retire <name>": move the recipe to `recipes/archive/` and remove its shortcut. Say how to bring it back.
- "bring back <name>": the reverse, after the name check.

## Rules

- A recipe holds only choices the person made. Never add a step, a choice or a stop they didn't make or approve.
- Never save a recipe without a yes on what will be saved.
- Never edit a studio skill to fit a recipe. Requests about how a skill works go to `studio-notes.md`.
- A recipe never skips a command's checks, a stop the command makes, or rule 6. It can't confirm a canon entry or approve a piece on the person's behalf.
- Keep the menu short. One offer per session, nothing offered twice after a no, and `/tidy` asks about recipes nobody runs.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
