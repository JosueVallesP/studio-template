---
name: librarian
description: After pieces ship: diff finals against drafts, count the evidence, propose canon changes, keep the body of work true, turn studio notes into skill fixes.
---

Launch the `librarian` agent (the crew agent in `.claude/agents/librarian.md`) in the foreground, so the write guard holds it to its own files, and ask it to run part A of `skills/role-librarian/SKILL.md`. In the app, where there are no agents, read that skill and run part A yourself.

When the agent returns, read `pieces/librarian-last-run.md`. Add each entry under "Drafts to add" to its canon file as a `draft` entry, exactly as listed, as `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes", says, then mark it `added <date>` in that file. Then tell the person what the librarian reported, and that the new drafts wait for their yes in `/status`.
