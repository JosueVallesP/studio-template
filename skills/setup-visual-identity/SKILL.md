---
name: setup-visual-identity
description: >-
  The "make it yours" pass, after the interviews and the strategy. Uses what the studio now knows about the person (target association, values, stories, stop list) to build their visual identity with the genius-of-contradiction and visual-philosophy skills, or to check and tune the brand they already have, writes canon/visual/design-system.md, and applies it to everything built in the quick wins: the Figma visual kit, the dashboard and the guide. Use when /start reaches "make it yours", or when someone says "build my look", "my visual identity", "customize my templates", "make it look like me".
---

# Make it yours

The quick wins gave the person a visual kit and a dashboard on day one, in their brand if they had one and plain if they didn't. Now the studio knows what they believe and what they want to be known for, so the look can be built from that instead of from taste. This pass runs once at setup and again whenever the strategy's target association changes.


When `canon/manifesto.md` exists, read it first: the thesis gives the target association, and the then, the now and the vow are where the true tensions sit that `craft-contradiction` looks for.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## When it runs

After the strategy is confirmed (`canon/strategy/brand-strategy.md` `status: confirmed`). Before that, the target association it builds from doesn't exist. If someone asks earlier, say the look gets built from the interviews and the strategy, and point to the next step in setup.

## What you need

- From the canon: `core-summary.md`, `strategy/brand-strategy.md` (target association, anti-associations, character sheet), `person/values.md`, `person/thesis.md`, `person/branches.md`, `bank/stories.md`, `bank/proof.md`, `visual/brand-assets.md`. Confirmed entries only.
- `skills/craft-contradiction` (the identity method) and `skills/craft-visual-philosophy` (turning an idea into a picture's structure).
- `templates/design-system.md` in this folder.
- `config/tools.md` for what's connected: Figma library file, dashboard app, Notion.

## Procedure

### 1. Which path

Read `canon/visual/brand-assets.md` and ask one question only if the file doesn't answer it: "Do you want to keep the look you have, or build one from what we now know about you?"

Then, if those sections say "not asked yet" (the form doesn't ask for them), ask these three, one at a time, and write the answers under "References they like", "References they can't stand" and "Never", in their words:

1. "Name three things whose look you like: brands, sites, posts, books, anything. A few words on why, if you have them."
2. "Now three whose look you can't stand." This is the more useful half: say so.
3. "One word your look should never be?"

Both paths read them: tuning checks the brand against the never word, and building takes the visual codes from them.

- **Keep and tune.** They have a brand and like it. Don't rebuild it. Go to step 2a.
- **Build.** No brand, or one they've outgrown. Go to step 2b.

### 2a. Keep and tune

Check the brand they have against the strategy, one line per check, quoting the canon:

- Does it carry the target association? Name what in it does (a color, a typeface, a texture) and what fights it.
- Does anything in it look like an anti-association or the never word?
- Is there a second side to the person (from their values and stories) that the look leaves out entirely? If so, it's a candidate for a contradiction: run `craft-contradiction` steps 3 to 5 only, from the canon, and offer the one tension that holds up as an addition (a texture, a second accent, a way of drawing scenes), never as a replacement.

Propose at most three changes, each with its reason from the canon. They say yes or no to each.

### 2b. Build

Run `craft-contradiction` the way its "In the studio" section says: steps 1 and 2 from the canon, step 3's evidence from the banks, the collision test, the ratio, the visual codes and the clash points. Ask only what the canon doesn't hold (what exists visually today, who they sit next to). Write the brief where `craft-contradiction` says ("In the studio").

Turn the brief into concrete choices: two or three color directions and two type pairings that carry it, each shown on the same two pictures from the kit (the 2x2 and the carousel cover) so the only thing that changes is the look. Use Google Fonts so they're available in Figma. They pick one, or mix.

### 3. Write the design system

Fill `templates/design-system.md` into `canon/visual/design-system.md`: target association and "never" copied as written; colors by role with hex values; type; line and texture; composition; mark. Every section stays `draft` until they say yes; then set `status: confirmed` and add a log line. This file is theirs. Changing it later is a proposal, like any canon change.

### 4. Apply it everywhere

- **Figma.** Run `skills/setup-figma` from step 4 with the design system as the source. The Neutral mode stays as it is.
- **Signature visuals.** For each of their top two or three confirmed branches or frameworks (`person/branches.md`, ranked), run `craft-visual-philosophy`, then `skills/fmt-post-visual` door 2, and build it in their library in the Brand mode on a new page called "Your frameworks". Record each under "Signature visuals" in the design system with its canon ID, move and node. These are the pictures their body of work keeps coming back to.
- **Their channel assets.** On the LinkedIn and Substack placements pages, for the channels in `config/tools.md`, fill what their files now hold, in their own words: the profile banner line from their confirmed positioning or thesis (`canon/core-summary.md`, `canon/strategy/brand-strategy.md`), the newsletter or publication name from their channel file, their logo or mark. A line they haven't confirmed stays a placeholder; ask for it. Show them the set and say which ones to upload where.
- **Dashboard.** Run `python3 scripts/sync-dashboard.py` (it reads colors from the design system) only when `config/tools.md` has `dashboard: app`. On the Notion connector route, set the Home page's icon and cover to match if they want.
- **Their guide.** In `YOUR-STUDIO.md`, the "Your visual kit" row says the kit is in their look, with the link.
- **Writing.** If the contradiction brief named a voice consequence (for example, a formal side and a plain side), add it as a proposal for the voice guide in `proposals.md`. Don't edit the voice guide.

### 5. Close

Show three things at feed size: one template in their look, one signature visual, and the carousel cover. Tick "Make it yours" in `canon/setup-progress.md` with the date and the path taken (kept and tuned, or built), and set its `stage` line to `check`. The next step is "Say '/check'."

## Rules

- The look comes from the canon. A choice with no reason in the canon is taste; say so or drop it.
- Never change the person's confirmed brand without a yes to each change.
- The Neutral mode in Figma is never touched; visuals are judged there first.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
