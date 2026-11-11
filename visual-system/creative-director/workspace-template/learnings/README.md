# Learnings

One lesson per file, written by `/cd-learn`. A lesson earns a file only when losing it would mean making the same mistake again or redoing real work.

File name: `<topic>-<short-slug>.md`, for example `recraft-style-drifts-on-text.md`.

Each file starts with:

```yaml
---
title: One sentence stating the lesson
kind: taste | tool | process     # taste: what looks right; tool: how a hand behaves; process: how the work runs
applies_when: "a condition, in plain words"
brands: [slug, slug]             # brands the evidence came from; [] when general
created: YYYY-MM-DD
evidence: ["brands/<slug>/log.md line or piece path", "..."]
---
```

Then three short parts: what happened, what we now do, and when this lesson would be wrong.

Other files here: `log.md` records which learnings and rule edits a person accepted or declined; `proposed/` holds candidates from non-interactive runs waiting for a person; `.last-run` holds the dates of the last learning run and the last refresh.

Skills load the learnings whose `applies_when` fits their work, the same way they load rules.
