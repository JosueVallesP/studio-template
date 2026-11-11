# The package

Read this at Step 2 before building anything. The package is the folder that lets any agent, on any platform and in any account, make a piece that matches. A canvas or a Figma file shows the system. The package is the system. When this step is skipped, the look lives in one session's memory and the next agent has to guess.

## Where it lives

`<brand>/system/package/`. Start it by copying `<plugin>/kit/` and read `kit/README.md`.

One folder per direction inside it. Most brands have one. When the approver is still choosing between two or three, package each one, so they judge real pieces.

```
system/package/
  README.md            what an agent reads first, how to make a piece, what to check
  vis.py               draws every piece and runs the checks
  fonts/               the typefaces as files
  photos/              the person's photographs, with sources.md
  <direction>/
    tokens.json        the one source: colours, type, sizes, shapes, rules
    rules.md           written from the tokens by the script
    mark/              the mark as SVG, each size and ground
    specs/             one spec per reference piece
    examples/          each reference piece as HTML and PNG
    sheets/            the mark, colour and type, the shapes and the rules
```

## Who reads it

The person reads the package, and so does the person's own agent. Write every file in it in the person's first person: "my look", "my words", "photos of me". Never write "he said" or "in her words" about the person whose package it is. The same holds for the sheets and for any canvas made from the package.

Do not write a doubt about the work into the package. A line such as "a first proposal, to be redrawn by hand" belongs in your message to the studio owner, and only when a person asked for it.

## The rules of a package

1. **`tokens.json` is the one source.** `rules.md`, the sheets, the exports and the canvas are written from it by the script. Nobody edits those by hand. This keeps the rules and the drawings from drifting apart.
2. **The art is code.** Each direction's own art is one function in `vis.py`. A piece is a small spec file plus one command. Nothing is drawn by hand outside the script.
3. **Fonts and photographs are files in the folder.** A piece renders the same with no network.
4. **Every colour pairing that carries text has its contrast measured** and written beside the pairing. A colour that fails for text is listed as never used for type.
5. **The script checks what a script can check:** only palette colours, one mark, the smallest text size, no type in a colour that fails, nothing running off the piece, no text wider than its box. The README lists what a person still has to check.
6. **The person's words are not in the package.** The README says where they are.
7. **Two kinds of photograph, both recorded.** The person's own photographs go in `photos/`. Brand photographs, which show the brand's world with the person not in them, go in `photos/brand/`. Every one has a line in `photos/sources.md`. See `<plugin>/taste/rules/images.md`.

## The reference pieces

Build at least these, with the person's own content: a post with art and one line, a quote, a framework, an illustration, one of the person's own photographs, a brand photograph, an art print, a banner and a newsletter header. Add any format the content plan names.

## The cold test

A package is not done until an agent that has seen none of the work can use it.

1. Copy the package to an empty folder.
2. Start a fresh agent. Give it only that folder. Tell it to use nothing else.
3. Ask for pieces that are not among the examples, with content you supply. Include one that stretches a format: a long line, more rows than the example, an odd count, a photograph that is busy all over.
4. Tell it not to edit the package and to report every place it had to guess or read the code.
5. Put its pieces beside the examples.
6. Fix the package for every difference and every guess. Never fix the piece.
7. Run the test again with a new agent, different pieces and different formats. One test covers only the formats it asked for. Stop when a cold agent's pieces match and it reports no guesses that matter.

Write the date and result of each cold test under "Last session" in the brand's `context.md`.

## Moving it to other tools

- `python3 vis.py figma <direction>` writes the tokens in the W3C format, each piece as PNG and PDF, the art as SVG and the mark as SVG. Copy its `variables.json` to `system/tokens.json`, so the tools in `hands/` sync from the same values.
- `python3 vis.py canvas <direction> <folder>` writes the files for a Claude design canvas.
- Building editable frames in Figma follows `<plugin>/hands/figma.md`, with the package's PNGs as the target to match.

## Done

- Every example builds with `ok`.
- The sheets and `rules.md` are written from the tokens.
- One cold test passed after the last change to `vis.py` or the README.
- The approver has seen the sheets and the examples.
