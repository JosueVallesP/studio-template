---
name: capture
description: Turn what the person dropped (text, a transcript, files in inbox/) into idea bank entries.
---

Launch the `capture` agent (the crew agent in `.claude/agents/capture.md`) in the foreground, so the write guard holds it to its own files. Hand it whatever was pasted with the command, word for word, and tell it to process every file in `inbox/` that isn't in `inbox/done/`, following `skills/role-capture/SKILL.md`. In the app, where there are no agents, read `skills/role-capture/SKILL.md` and follow it exactly yourself.

When the agent returns, tell the person what it reported, in its few lines, and ask its one question if it has one. Anything it flagged for the main session (a method or definition the person asked out loud to have written down) you add yourself, as a `draft` entry in its canon file, as `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes", says, and say where it went.
