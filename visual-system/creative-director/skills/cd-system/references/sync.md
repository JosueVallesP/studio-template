# Syncing tools

The repo is the source of truth unless `bindings.yaml` says otherwise. Each tool gets a copy. Read the tool's `hands/<tool>.md` for its gotchas before syncing it.

| Tool | What gets synced | Where it's recorded |
| --- | --- | --- |
| Claude Design | A Design System artifact for the brand: README from `direction.md` (target association, contradiction, never list), tokens converted to the list shape it reads (see below), canon images as assets, and a cover component | `design_system.url` |
| Figma | A variables collection from `tokens.json`; text styles for headline, body and label | `figma.file_key`, `figma.variables_collection` |
| Paper | Tokens via Paper's token tools, in the brand's Paper file | `paper.file`, `paper.tokens_synced` |
| Code diagrams | A D2 theme file generated from color and font tokens | `code_diagrams.d2_theme` |
| Recraft, Flora | Nothing from tokens directly. Styles train from canon (Step 3) | `recraft.style_id`, `flora.lora_id` |

## Converting tokens for Claude Design

A Design System artifact can't read the W3C format in `tokens.json`. It shows the family as empty. Convert each family into a list: `{"color":{"themes":[{"id":"light","name":"Light"}],"tokens":[{"name":"ink","value":"#161616","usage":"…"}]}}`, with `type` as `fonts`, `families` and `groups` of styles. Token names can't contain `/`. Carry each token's `$description` into `usage`; every token needs one. Fonts served by Google Fonts need only a family entry, no file.

## Order

Claude Design first, because `cd-make` draws most layouts there and the Design System artifact is what keeps those drafts close to the brand. Then Figma. Then the rest. The repo stays the source either way.

## Recording

After each tool, update its block in `bindings.yaml` with ids and the date. A skipped tool keeps its old values and gets a line under "Last session" in the brand's `context.md` saying why.

## Drift

Drift is any value in a tool that no longer matches `tokens.json`. Report it as a table: tool, token, repo value, tool value. Ask which side is right before changing anything.
