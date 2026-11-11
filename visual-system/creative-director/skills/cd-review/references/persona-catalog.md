# Persona catalog

Select personas by what the piece contains. Read the visual brief and look at the drafts; this is judgment, not keyword matching.

## Always

| Persona | File | Needs a visual brief | Asks |
| --- | --- | --- | --- |
| Fidelity | `personas/fidelity.md` | No | Does it match this brand's tokens, direction, never list and canon? |
| Caliber | `personas/caliber.md` | No (uses it when present) | Does it show the person at their real level, or above or below it? |

## When the piece calls for it

| Persona | File | Needs a visual brief | Run when |
| --- | --- | --- | --- |
| Legibility | `personas/legibility.md` | No | The piece must be understood on its own: social visuals, diagrams, field guides, headers, one-sheets |
| Sameness | `personas/sameness.md` | No | A model, a template or a stock source touched any part of it |
| Contradiction | `personas/contradiction.md` | No | The brand's mode is new or rebrand, or refresh with a contradiction in `direction.md` |
| Form | `personas/form.md` | Yes | The piece contains a diagram, framework, chart or field guide |
| Copy | `personas/copy.md` | Yes, for the "words that must appear" check; otherwise no | The piece has any words on it beyond a name or logo |

## The craft floor, before any persona runs

Legibility and form judge by reading the piece. One class of failure is measurable
instead, and a persona that eyeballs it will pass work that fails a standard. If any
text sits over a photograph, a gradient or a saturated colour, get the measured
contrast ratio from the design plugin's `dsn-contrast`, which owns the arithmetic and
the published thresholds. Record the ratio and the pass or fail in the finding rather
than describing the text as hard to read.

Two traps that skill documents and a persona will otherwise walk into: a greyscale or
lightness check is not a contrast ratio and must never be reported as one, and the
type floor has two cases, so a floor quoted without its case is incomplete. Take
both cases from design's `reference/canvas-assumptions.md`.

Craft questions beyond contrast route the same way, through `cd-make/references/craft.md`.
The dependency runs one way: this plugin reads design, design does not read this one.

## Keep mode

In keep mode, fidelity leads: its `must` findings come first in the round, and contradiction never runs.

## Model tiers

Caliber runs on the most capable model available, since it judges the hardest thing. Fidelity, legibility, form and copy can run on a mid-tier model. Sameness benefits from a different model family than the one that made the drafts, when the host offers one.
