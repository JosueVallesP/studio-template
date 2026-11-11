---
name: setup-notion
description: >-
  Connects a person's Notion dashboard. The person duplicates the studio's master template into their workspace with one click; this skill finds the copy, records its five databases in config/tools.md, fills them from the files and hands over the link. Works two ways: through the Notion connector in Claude (no token, the default for anyone non-technical) or through an integration token and scripts/sync-notion.py. One of the quick wins: it runs before the interviews. Use when someone says "set up Notion", "connect my Notion", "the Notion dashboard", or when config/tools.md says Notion is wanted and not connected.
---

# Set up the Notion dashboard

The Notion dashboard is a duplicate of the master template (`notion_master` in `studio.manifest.yaml`, shared as a public template at `notion_template_link`; the contract is `docs/notion-template.md`, "as built" section). You don't build it per person; you connect the copy and fill it. A change to the dashboard is a change to the master, for everyone.

It runs before the interviews on purpose. On day one it shows an empty pipeline, the one next step and the page on how the studio works. That's enough to make the studio feel real, and it fills itself as the work starts.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Pick the route

- **Connector route.** The Notion tools are available in this session (the person connected Notion in Claude's settings, under Connectors). To check, load them if they're listed but not loaded, and run a Notion search for "Content Studio"; a tool that is only named, or a call that fails, means not connected. No token, no script talks to Notion. Use this whenever it's available.
- **Token route.** No Notion tools, but the person is comfortable creating an integration. `scripts/sync-notion.py` does the work.

If neither is possible: write `- [ ] Dashboard in Notion: waiting on Connectors` in `canon/setup-progress.md`, say the one step in one sentence ("Connect Notion in Claude's settings, under Connectors, then say 'set up my dashboard'"), say `/status` shows the same things inside Claude until then, and name the next quick win in one line.

## Procedure

1. **Check.** Read `config/tools.md`, section Notion. If `connected: yes` and the database IDs are set, go to step 4. If `wanted: no`, stop.
2. **The person's one step.** Send them the template link (`notion_template_link` in `studio.manifest.yaml`) and say: open it, click "Duplicate" at the top right, and pick their workspace. That's all. Token route only: they also create an internal integration named "Content Studio" (Notion settings, Connections), share the duplicated page with it, and paste the token once. Put it in `.env` as `NOTION_TOKEN`, never in `config/` or a skill.
3. **Find the copy and its databases.**
   - *Connector route:* search their workspace for "Content Studio". Fetch the page, read its five databases by title (Pieces, Ideas, Proposals, Canon index, Weekly) and the Home page, and write their IDs and data source URLs into `config/tools.md` under Notion (`page id`, `home page`, `pieces database`, and so on, plus `route: connector`), then set `connected: yes`. If a title is missing, the copy isn't the master's; say so.
   - *Token route:* put the page ID in `config/tools.md` as `page id` and run `python3 scripts/sync-notion.py --discover`. It finds the databases and writes `connected: yes`. Add `route: token`.
4. **Fill.**
   - *Connector route:* run `python3 scripts/sync-notion.py --dump`. It prints every row the dashboard should hold, already in the shape the Notion tools take, plus the field names that belong to the person. For each database, fetch its rows, match on ID (Week for Weekly), update the ones that exist and create the ones that don't. Never write a field listed under `never_overwrite` on a row that already exists.
   - *Token route:* `python3 scripts/sync-notion.py --dry-run`, read the counts, then run it for real.
   Either way, delete the master's sample rows if the copy carried them (every sample row starts with "Sample"). Rewrite the "Next step" callout on Home with the one next step from `canon/setup-progress.md`, and if `config/tools.md` has a Figma `file url`, put it in the "Your visual kit" callout on Home.
5. **Hand over**, in three lines: the link to their Home; that the pipeline moves by itself and dragging a card changes nothing; that deciding on a piece (Your decision, Your note) or answering a proposal (Your answer) is recorded by the studio and moves the piece. Write the link into `YOUR-STUDIO.md` ("Your dashboard" row) and tick the Notion item in `canon/setup-progress.md` in the format `setup-start` sets: `- [x] Dashboard in Notion: done <date>`.

## Keeping it in sync

The stop hook runs `scripts/sync-notion.py` (and `scripts/sync-dashboard.py`) after every reply, so no skill runs them. On the token route that is the whole sync. On the connector route the script exits silently (there's no token), so when `config/tools.md` says `route: connector`, `/end` (`skills/job-end`) does this half through the Notion tools when the session changed pieces, ideas, proposals or the canon, and the producer does it before reading `pieces/_decisions.md`: run `--dump`, apply it as in step 4, then read decisions back: any Pieces row with "Your decision" set and "Decision taken" unchecked becomes a line in `pieces/_decisions.md` in the shape `- <date> · <piece ID> · <decision> · "<note>"` (the decision words: approve brief, change brief, kill, ship, revise, hold), and the row gets "Decision taken" checked and "Your decision" and "Your note" cleared. Proposals with "Your answer" set and Status Open become `- <date> · proposal <ID> · <answer> · "<note>"`, and the answer is cleared. The producer records each line.

## Rules

- Files are the truth. Never fix a number in Notion; fix the file and sync again.
- Never rename a database or a property in a person's copy; the sync matches on the names.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
