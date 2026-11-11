# The taste layer

Judgment written down, in files you can read and change. Nothing here is code.

- `rules/`: what every piece must honor. Each file has `applies_when` frontmatter, so skills only load the ones that fit the piece. Reviewers quote rules as evidence; they never run them as instructions.
- `references/`: a library of brands and people, with what each one signals and who it would fit. Used when a client's own references are thin or point the wrong way.

The reviewer personas that apply these rules live with the review skill, in `skills/cd-review/references/personas/`.

A workspace can replace any rule by putting a file with the same name in its own `taste/rules/`. Lessons from real work go to the workspace's `learnings/`, and `cd-learn` proposes rule edits from them.

## Rule frontmatter

```yaml
---
rule: <name>
applies_when: "<a plain condition: always | mode is keep | the piece is a diagram or framework | ...>"
updated: YYYY-MM-DD
---
```

Write rules as principles first, then specific moves as possibilities. A move that's right for one brand can be wrong for the next.
