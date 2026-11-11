---
name: setup-dashboard
description: >-
  The studio owner's own dashboard path, not the buyer's (buyers use Notion through setup-notion). Makes a dashboard app from the studio's master app, connects the sync, pushes the files into it for the first time, and hands over the link. Runs only when config/tools.md has `dashboard: app` under Dashboard; then "set up my dashboard" or "build the dashboard" comes here instead of setup-notion. Needs the Base44 tools in the session, or a person with editor access to the master app running the steps.
---

# Set up the dashboard

The dashboard is one app per person, copied from the studio's master app and styled from their files. The contract for what's in it is `docs/dashboard-app.md`; read it before you start. You copy, connect and fill. You don't redesign the app for one person; a change to the dashboard is a change to the master, for everyone.

## Where things are

- The master app: its ID is in `studio.manifest.yaml` under `dashboard_master`. The studio owns it.
- The person's app: `config/tools.md`, section Dashboard: `app id`, `api url`, `app url`. The person owns the file.
- The key the sync uses: `BASE44_API_KEY` in the instance's `.env` (ignored by git). Never in `config/`, never in a skill.
- The sync: `scripts/sync-dashboard.py`. `--dry-run` sends nothing; `--dump` prints what it would send.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Procedure

1. **Check.** Read `config/tools.md`. If Dashboard has no `dashboard: app` line, stop: this is the owner's path, and a buyer's dashboard is Notion (`setup-notion`). If Dashboard says `connected: yes` and `app id` is set, the app exists: go to step 5 and run the sync.
2. **Copy the master.** Remix the master app (`POST /api/apps/{master}/remix`, through the Base44 tools). Rename the copy "<person's name>: Content Studio" (`Update app`). Set `public_settings` to `private_with_login`. Poll until its status is `ready`.
3. **Connect.** Get the copy's API address and key: the app's OpenAPI reference (`GET /api/apps/{app_id}/openapi-spec`) gives the server URL; the key is an app API key the person (or you, as their editor) creates in the app's settings. Write `app id`, `api url` and `app url` (the published URL) into `config/tools.md`, set `connected: yes`, and put the key in `.env`. Invite the person as the app's user with their email from `config/intake.yaml`.
4. **Fill.** Run `python3 scripts/sync-dashboard.py --dry-run` and read the counts; then run it for real. The first run writes StudioSettings (their name, goal, channels, colors from `canon/visual/brand-assets.md` or the design system, the text of `YOUR-STUDIO.md`), every piece, idea, proposal and canon entry, and the first weekly row. Open the app and look at Home: the person's name in the header, their colors, "Nothing waiting on you" if nothing is, and the pipeline with whatever exists.
5. **Deploy and hand over.** Publish the app (`POST /api/apps/{app_id}/deploy`). Write the link into `YOUR-STUDIO.md` ("Your dashboard" row) and tick the dashboard item in `canon/setup-progress.md`. Tell the person in three lines: the link; that Home shows what's waiting on them and the pipeline moves by itself; that when they decide something in the app (the "Your decision" field on a piece, "Your answer" on a proposal), the studio records it and moves the piece, and dragging a card changes nothing.

## Rules

- **Files are the truth.** Never fix a wrong number in the app; fix the file and rerun the sync.
- **Never put the key anywhere but `.env`.**
- **Never change the person's copy by hand** (a page, a field, a color) to please one person. Propose the change to the master in `studio-notes.md`.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
