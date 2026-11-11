# Proposing rule edits

A rule says what every piece must honor, so changing one changes every future review. Treat it with care.

## When a lesson becomes a rule edit

- It applies beyond one brand.
- It's backed by at least two independent pieces of evidence (two brands, or two people, or a person overruling a reviewer twice for the same reason).
- It can be written as a principle with specific moves as possibilities, like every other rule.

Otherwise it stays a learning.

## How to show it

```diff
--- taste/rules/<rule>.md
+++ taste/rules/<rule>.md
@@ <section>
- <old line>
+ <new line>
```

Under the diff: the evidence lines, one sentence on what changes in future reviews, and one sentence on when this edit would be wrong.

## Where edits go

Always to `<ws>/taste/rules/`. If the workspace has no override for that rule yet, copy the plugin's file there first, then edit the copy. The plugin's own rules change only when the plugin's maintainer edits them directly.

## generic-tells.md

This rule goes stale fastest. Add a tell when the sameness reviewer noted it on two or more pieces and a person agreed. Remove one when it hasn't appeared in rejections for three months. Date every change in the file.

## Self-changing safety

The agent never applies its own rule edit. Every edit is a proposal, a person accepts it, and git keeps the history for rollback.
