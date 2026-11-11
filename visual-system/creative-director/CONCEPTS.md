# Concepts

The words this repo uses, and what they mean here. `AGENTS.md` defines the four words for people (the person, the studio owner, the approver, a person). `ROUTING.md` lists the words the other two plugins use differently.

**Brand.** One person's brand, held in one folder: `<ws>/brands/<slug>/`. The folder is the source of truth. Figma, Recraft and the rest hold copies.

**Mode.** What the job is for this brand, set at intake in `brief.md`: `keep` (protect an existing brand), `refresh` (keep what people recognize, update the rest), `rebrand` (move to a new look on purpose) or `new` (no brand yet). The mode decides how much the agent may change on its own.

**Caliber.** The real level of the person's work: how deep, how proven, how rare. The creative director's job is to make the brand show that level, no higher and no lower. Overselling looks like hype. Underselling looks like a template.

**Direction.** The decision about how the brand looks and why, written in `direction.md`: the target association, the contradiction, the visual codes, the clash points, the recurring shapes and the never list.

**Target association.** What people should think and feel when they see the brand, specific enough to design for. "Trustworthy like a family doctor" works. "Trustworthy" doesn't.

**Contradiction.** Two opposite things that are both true of the person, whose collision produces the target association. One side leads (the base), the other surprises or grounds (the accent). Method: `skills/cd-direction/references/contradiction.md`.

**Equities.** In refresh mode, the parts of the existing brand people already recognize. They get protected while everything around them changes.

**System.** The direction turned into values a tool can use: `system/tokens.json` (color, type, spacing) and `system/bindings.yaml` (where the brand lives in each tool).

**Canon.** Pieces a person has approved as "this is right." Only a person decides what goes in; the agent copies a piece in when asked. Reviewers compare new work against it.

**Assets.** The person's own material in `<brand>/assets/`: headshots, logo and mark files, an approved bio, approved talk descriptions, testimonials. Pieces draw their words and images from here. Different from `references/`, which holds work the person likes by others.

**Piece.** One thing being made: a post visual, a carousel, a one-sheet, a header. It lives in `pieces/<date>-<slug>/` with its visual brief, drafts and review.

**Visual brief.** The handoff into `cd-make`: the claim, where it comes from in the person's work, what the visual must show, the platform and the format. A content system writes it, or `cd-make` writes it with the person.

**Hand.** A tool that makes things: Claude Design, Figma, Recraft, Flora, Paper, or code tools like D2. Each has a notes file in `hands/`.

**Rule.** A file in `taste/rules/` that says what work must honor, with `applies_when` so only the relevant ones load. Rules are your judgment written down.

**Persona.** A reviewer prompt in `skills/cd-review/references/personas/` that judges one thing: fidelity, caliber, legibility, sameness, the contradiction, the diagram's shape, or the copy.

**Learning.** One lesson from past work in `<ws>/learnings/`, written by `cd-learn` only when losing it would mean making the same mistake again.

**Log.** `<brand>/log.md`, an append-only list of every approval, rejection and reason.

**Framer.** The word `PRINCIPLES.md` uses for the humans who decide what matters. In skills and rules, use the exact word instead: the person, the studio owner or the approver.
