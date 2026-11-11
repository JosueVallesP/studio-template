# Ownership map

The 17 skills were written in isolation, so each file's "Where this skill
should lose" section was an independent guess about its neighbours. This file
is the single statement of which skill owns what, which version of a shared rule
holds, and the ground nothing covers. Read it before changing any boundary
statement. Earlier versions of this file, in the git history, record how each
conflict was decided.

## The map

One line per area, naming the single owner and the thing the owner decides.

### Placement and order

| Area | Owner | The decision |
|---|---|---|
| Which element is first, and the full rank list | `dsn-hierarchy` | the ranking, in words, and how much separation each rank needs |
| Where each element sits, and the eye's path between them | `dsn-composition` | the arrangement that enforces a ranking already decided |
| Whether the arrangement tips, and its counterweight | `dsn-balance` | the stability target: symmetry, asymmetry or deliberate tension |
| Which region of the frame is empty, and what it points at | `dsn-composition` | placement of the emptiness |
| How large an empty region is | `dsn-spacing` | the value |

The three-way split is stated in `dsn-composition` and `dsn-hierarchy` in the
same words: if the fix is a different ranking you are in hierarchy, if the fix
is to move something you are in composition, if the fix is weight on the
opposite side without changing what is loudest you are in balance.

### Structure and space

| Area | Owner | The decision |
|---|---|---|
| Space measured from the canvas: page margin, column count, gutter, spans | `dsn-grid` | the grid |
| Space measured from the content: gaps, padding, empty regions | `dsn-spacing` | the ladder |
| The base unit everything else is a multiple of | `dsn-spacing` | the unit, which grid consumes |
| Safe zone and crop-safe box | `dsn-spacing` | a platform constraint that outranks the grid's margin |
| Whether a borrowed number transfers to a new canvas | `dsn-grid` and `dsn-spacing` | each carries its own transfer check |

### Type

| Area | Owner | The decision |
|---|---|---|
| Which face, which pairing, which weights | `dsn-typeface` | ends at the slot table |
| Size, leading, tracking, measure, the scale and its ratio | `dsn-typeset` | begins at the slot table |
| The smallest size that survives a feed | `dsn-typeset` | the floor |
| Type that is a drawn mark rather than set copy | `dsn-mark` | the lockup's internal relationships |

### Colour

| Area | Owner | The decision |
|---|---|---|
| Which colours exist, the role structure, the set | `dsn-palette` | the set |
| What one colour is doing, its three numbers, relational behaviour | `dsn-color` | the job and the values |
| Whether a pair clears a measured floor | `dsn-contrast` | the ratio and the verdict |

`dsn-contrast` takes two values in and returns one verdict, for every file that
sends it a pair, and it never chooses a colour, a size, a rank or a picture.

### Frames

| Area | Owner | The decision |
|---|---|---|
| One frame that must stand alone: element count, level count, what gets cut | `dsn-poster` | the cut |
| How many frames the piece needs | `dsn-sequence` | the frame count |
| Order across frames, what crosses each seam, which frames are templated | `dsn-sequence` | the sequence |
| Whether a layout survives having its content swapped | `dsn-balance` | the substitution test that feeds the templating call |
| Which picture, its crop, its focal point, what it gives up | `dsn-image` | the picture |

A carousel's first frame, and any frame that will be reposted alone, belongs to
both poster and sequence: poster for whether it stands up with nothing around
it, sequence for whether it is the right frame in that position.

### Brand

| Area | Owner | The decision |
|---|---|---|
| Which elements exist at all, and the unit each is measured in | `dsn-identity` | the inventory and the units |
| Coherence across separate pieces | `dsn-identity` | whether two posts read as one brand |
| Coherence across the frames of one piece | `dsn-sequence` | what repeats across a seam |
| One mark: its idea, construction and optical correction | `dsn-mark` | the drawing |
| A family of small marks that must read small and look related | `dsn-icon` | the set and its spec |
| Names that resolve, and the rule producing the next value | `dsn-tokens` | the names, never the values |
| Clear space around the mark, in units of the mark | `dsn-identity` | the rule |
| Motion | `dsn-identity` | thin, and the only coverage anywhere here |

## Rules that more than one skill states, and the version that holds

Several skills state a rule on the same subject in different words or with
different numbers. One version holds. Where a skill says otherwise, this table
wins until that skill is corrected.

| Subject | The rule that holds | Owner |
|---|---|---|
| Margin, gutter, columns, spacing unit, type sizes on a 1080 canvas | The default system in `reference/canvas-assumptions.md` | that file |
| How strongly a rank is marked | The lowest rank is the unstyled base. Each rank above it differs from the rank below by two channels, never one | `dsn-hierarchy` |
| How many ranks a frame holds | Only the ranks that are still distinct at the 4x stress check. Three at most. Two at most, plus one fringe band, when the frame stands alone in a feed | `dsn-hierarchy`, with `dsn-poster` for the frame that stands alone |
| How many typefaces | One family until a second earns its place by the second-family test. Never more than two | `dsn-typeface` |
| How a colour or a token is named | By its job (`color.text.primary`, `space.margin`), never by hue, size or a brand nickname | `dsn-tokens` |
| The unit a measure is counted in | Characters, including spaces | `dsn-typeset` |

## Orphaned ground found

Assigned where something had a real claim, stated plainly where nothing did.

- **Deriving a palette from a photograph.** Was a circular pointer: palette
  called it a gap and sent readers to image, image sent palette questions back
  to palette. Nothing does it. Both files now say so and both give the same
  substitute, which is to sample candidates by eye and then run them through
  palette's build procedure and tests, since the sampling has no method and the
  testing does.
- **The frame count.** Poster detected that a frame had run out of room and
  named no owner for what to do next; sequence computed per-frame budgets but
  never claimed the count. Assigned to `dsn-sequence`, which holds the
  arithmetic, with poster's measure ceiling as the input.
- **Motion.** Four files said nothing covers it while `dsn-identity` held thin
  rules on it. Assigned to identity, labelled thin in identity and in every file
  that points there, so a reader is not sent somewhere empty.
- **Weighing a photograph.** Balance consumes a tonal value and a focal point
  and neither file named the source. Assigned to `dsn-image`, which now supplies
  both and owns the judgement that a different picture is the cheaper repair.
- **Naming an icon set's figures.** Icon wrote a spec with stroke weights and
  minimum sizes and never mentioned tokens; tokens never mentioned icon.
  Assigned to `dsn-tokens` for the names, icon keeps every figure.
- **Transfer to a new canvas.** Composition and balance listed it as covered by
  nothing, while grid and spacing each carry a transfer procedure and identity
  carries the unit method. Corrected in both files. What genuinely has no owner
  is automatic reflow between live breakpoints.
- **Minimum contrast for a thin icon stroke on a dark ground.** Icon names it a
  gap and sends readers to contrast, which does not carry the figure. Stated
  plainly in contrast, with the published non-text floor as the best available
  answer.
- **Vertical rhythm as a system.** Grid assigned it to spacing; spacing lists
  baseline grids and vertical rhythm as not covered. Grid's claim was removed
  rather than spacing's disclaimer, since spacing is the file that would have to
  hold it.

Nothing covers these, and the files that touch them say so rather than
improvising: print reproduction including ink, gamut, spot colour, bleed, trim
and binding gutters; display calibration and colour management; accessibility
beyond the measured contrast floor, meaning focus order, semantic headings,
alternative text, keyboard navigation, screen reader behaviour, minimum touch
target size and user font scaling; right-to-left and non-Latin layout and
micro-spacing; responsive and fluid grids and automatic reflow; data
visualisation encoding, including which hue per series, sequential and diverging
scales, axis prominence and chart composition; colour-blind simulation beyond
greyscale and redundancy; optical margin alignment and hanging punctuation;
optical sizing, hinting, variable font axes beyond weight and width, and web
font loading; sets longer than about twelve frames; threads and newsletters;
measuring a design against an outcome; and whether the claim is true.

Choice of canvas, meaning 1080 x 1080 against 1080 x 1350, is not owned by a
skill either. It is fixed as a shared assumption in `reference/canvas-assumptions.md`,
which every skill quoting a pixel figure derives from.

## Unresolved, needing a judgement

**Whether `dsn-palette` and `dsn-color` should be one skill.** Their split is
internally consistent and stated the same way from three sides, so nothing here
is broken. But the pair is the only place in the plugin where one subject is cut
into "which ones exist" and "what one does", and a reader with a colour problem
has to know which half they are in before they can start. Merging them, or
renaming them so the split is legible from the names alone, is a structural
decision rather than a boundary repair, and it was left alone.
