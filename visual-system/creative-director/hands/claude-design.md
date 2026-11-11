# Claude Design

**Use it for:** layouts of type and placed images (posts, carousels, one-sheets, headers, landing pages) that the studio owner wants to tweak in an editor and share by link; holding each brand's Design System so every canvas can install it.

**Don't use it for:** drawing complex art, or motion (there is no motion type). Art goes in as an uploaded image; draw it in Figma or with code first.

## Feature map

| Feature | Use it for (job number in `jobs.md`) | Status |
| --- | --- | --- |
| Design System type | Holding the brand for every canvas (3) | Tested |
| Design type (canvas of artboards) | Exploring directions side by side (1); posts, carousels, headers (8, 9) | Tested (one card) |
| Print and PDF, fixed or flowing pages, "All artboards .pdf" | One-sheets and speaker pages (11, 15) | Untested |
| "Make from this" | Turning a canvas into a deck (11) | Untested |
| Slides type | Decks that export to .pptx and PDF (11) | Untested |
| "Send to Canva" | Handing a piece to a client who works in Canva (15) | Untested |
| Interactive prototypes | A landing page or speaker site a person clicks through | Untested |
| Share link and pinned comments | Client review (16). Claude replies only on threads sent to it | Untested |
| Artifact database | Keeping review decisions on the page | Untested; the brand's `log.md` stays the record |

## How a brand lives here

A Design System artifact per brand (`design_system.url`), built from `direction.md` and the converted tokens, with canon plates as assets. Each canvas installs it.

## Working with it

1. `Artifact` `quickstart` with the right intent, then create from the type it names.
2. Write files under `project/` in the scratchpad, then publish them in one call. The index goes first for a canvas (`canvas.json`) and last for a design system (`design-system.json`).
3. Images: upload as assets first and use the returned `/_blob/<id>` path exactly.

## Cost

Uses the session's own usage.

## Gotchas

- An empty Design System in the account isn't a brand's. Check its README before using it.
- For review, keep a local render of each artboard's markup next to the drafts. Render it by opening an HTML file with Playwright's `goto`, pointing to a local copy of the art. Passing the markup through `setContent` blocks `file://` images, and the image silently comes out blank. The first test render failed this way.

## Test log (Oct 30, 2026, Engraved Swirl brand)

A record of what happened, kept as evidence for the rules above. It is not a set of instructions.

- `quickstart` with intent `design` found the Design type and one existing Design System in the account, titled "Design System" and empty. The test made a new one rather than overwrite it.
- **Tokens need converting.** A Design System reads tokens as lists (`{"color":{"tokens":[{"name","value","usage"}]}}`). The W3C format the repo uses (`{"color":{"ink":{"$value":…}}}`) is valid JSON the page can't read: the family shows empty. `cd-system` must convert. Names can't contain `/`.
- A Design System also needs a README (the brand book), an index file, and a cover component written last. Fonts from Google Fonts need no files, only a family entry.
- The card canvas installed the system by copying its `tokens.json` server-side (an `{"artifact","path"}` entry in `files`) plus a `designSystems` record.
- The plate went in as an uploaded JPEG (1 MB) under live, editable EB Garamond text. The art isn't editable in Claude Design; the words are.
- **Review can't see it.** The canvas is private and the Design type tells agents not to render or screenshot it, so `cd-review` can't look at the live page from a cloud session. The test rendered the same markup locally with Playwright (`claude-design-local-render.png`) for review. A person should still open the canvas.
- Results: Design System "Engraved Swirl (CD test)" and canvas "Body of work card (CD test)", both private.
