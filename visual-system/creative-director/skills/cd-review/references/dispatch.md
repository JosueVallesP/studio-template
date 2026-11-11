# Starting a reviewer

A fresh sub-agent knows nothing about this brand. Its prompt must carry everything it needs, or it will judge against generic taste.

## Every reviewer's prompt includes

1. The persona file's full text.
2. The absolute paths of: `direction.md`, `system/tokens.json`, `brief.md`, the piece's `visual-brief.md` (when there is one), the `canon/` folder, and every draft image.
3. The absolute paths of every rule file that applies, resolved as `AGENTS.md` describes: the plugin's rules, replaced by workspace overrides, plus workspace-only rules and rule packs, filtered by `applies_when`. Include every file the persona lists under "Rules you rest on."
4. The absolute paths of the learnings that apply (by `applies_when`, or listing this brand).
5. The absolute path of the piece's format spec, when the brief names one.
6. The absolute path of `references/findings.md`, with the instruction to return findings in that format and nothing else.
7. The instruction: look at each draft image yourself; don't judge from file names or descriptions.
8. The instruction: don't edit any file.

## Failure

If a reviewer fails to start or returns nothing, retry it once. If it fails again, run that persona yourself and note it in the round. Never report a persona as run when it didn't run.
