# Finding format

Each reviewer returns a list of findings in this shape:

```markdown
- **Draft:** <file name>
  **Reviewer:** <persona>
  **Severity:** must | should | consider
  **Rests on:** <the rule or learning file and the line quoted, or the line of direction.md / brief.md / tokens.json / the format spec quoted>
  **What's wrong:** <one or two plain sentences, naming the concrete thing on the page>
  **Fix:** <what would fix it, as a possibility rather than an order>
  **Sends back:** no | yes (only when the problem is the idea itself, not the drawing)
```

The sameness reviewer may add, after its findings:

```markdown
### Possible new defaults
- <a look that seems to be a new default, not yet in generic-tells.md, and where you saw it>
```

Return nothing else.

## Severity

- **must:** breaks a locked value, a never-list item, the target association, words the brief said must appear, or makes the piece unreadable or misleading. In keep mode, any token mismatch is `must`.
- **should:** weakens the piece noticeably, but a person could reasonably ship it.
- **consider:** a choice worth a second look; the reviewer isn't sure.

## A finding needs a source

If you can't quote a rule, a learning or a brand line it rests on, don't file it. Your own taste isn't a source; the brand's is.

## Write it plainly

Follow `<plugin>/taste/rules/copy-on-visuals.md`. Name the thing ("the accent orange fills the whole background") instead of the abstraction ("the color balance feels off").
