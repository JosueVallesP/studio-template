# State of the build

What exists in the repo today and what doesn't yet. `CHANGELOG.md` says what changed in each version; `docs/spec.md` holds the design.

## Built

- Developing an idea: `job-develop` (`/develop`) works one idea into an idea sheet in `bank/sheets/` and names the pieces it asks for. Three sheets written with the author; no piece has gone from a sheet to a shipped post yet.
- The visual system: `job-visual-system` (`/visual-system`) runs the creative director, art direction and design skills in `visual-system/`, and the person's workspace is `visual/`. Run with one person so far. The kit that builds a package was taken out in 0.92.1 and is not built yet in a form that can ship.
- Idea briefs and a wiki in the LinkedIn library (57 briefs over the 357 posts).

- The front door: `setup-start` (`/start`), which conducts setup and gives one next step each session.
- Intake in two forms: `setup-intake` inside Claude, and the form with `scripts/tally-to-answers.py` and `scripts/build-instance.py`, which writes the person's settings, outcomes, brand assets and `YOUR-STUDIO.md`.
- The map of the person's ideas, the first quick win: `job-map` (`/map`), with `scripts/map-render.py` building the page, the tree (`map.html`) and the Obsidian canvas from `bank/map/map.json`, and checking every quote against the person's files.
- The one page about the person for any AI: `setup-about-you` (`/about`), offered at the end of setup.
- The library tour, a quick win: `setup-libraries` (`/libraries`) shows the LinkedIn, Substack and visual libraries through the few moves the person's own material can carry.
- Schedules: `setup-schedules` (`/schedules`) sets up the scheduled runs (weekly tending, weekly librarian, tidy, weekly numbers), each a fresh session that finds and files and never decides, off until the person says yes.
- Sources: `setup-sources` (`/sources`) connects the person's call recorder (Granola and the like), a YouTube transcript connector for talks and podcasts, Readwise, a Reddit research connector, a results source (AuthoredUp, Metricool, Substack) for the routes that watch numbers, and a publishing source (Blotato, Metricool's planner) that books a passed piece for a set time on the person's yes for that piece. It defines how every skill pulls a call, a talk or reading notes into `inbox/` as text, and how numbers become signal lines.
- The first post as a quick win: `setup-first-post`, which runs `job-post`.
- The Figma visual kit: `setup-figma`, connecting the person's duplicate of the master library (marks as components, the 22 visual moves and nineteen variants as worked examples, a carousel set, a field guide, plates, the LinkedIn and Substack placements, and a Style collection with Neutral and Brand modes).
- The Notion dashboard for buyers: `setup-notion`, with `scripts/sync-notion.py`.
- The dashboard app in Base44, the studio owner's own path: `setup-dashboard`, with `scripts/sync-dashboard.py`.
- The interviews: `setup-brand-tree` (`/interview`), one short session per layer, each asking about events; the five person-layer sessions in `interviews/`, and the fields, questions, routing and tests in `references/`.
- The strategy: `strategy-brand`, with the method in `docs/strategy-method.md` and the named routes.
- "Make it yours": `setup-visual-identity`, which builds or tunes the look from the canon and applies it to the kit and the dashboard.
- The setup check: `setup-check` (`/check`) and `scripts/setup-check.sh`.
- `/status`: `check-status`, with the facts from `scripts/status.sh` and a seven-day view of scheduled pieces.
- How the studio asks: `craft-interview`, the eight questioning moves the interviews, `/strategy`, `/think` and `/coach` point to.
- The job commands: `job-post`, `job-essay`, `job-strategy`, `job-visual`, `job-identity`, `job-manifesto`.
- The helpers: `job-shape`, `job-journal`, `job-refine`, `job-understand`, `job-adapt`, `job-tidy`, `job-teardown`, `job-recall`, `job-think`, `job-scout`, `job-learn`, `job-end`, `job-coach`.
- The crew as skills and agents: capture, writer, judge, librarian, and the producer as the clerk for the person's decisions; `/harvest` lists what's ready to make. One way to make a piece since 0.90: the job commands' stops, with no separate pipeline.
- One gates table for every review, with one verdict ladder (pass, revise, redo), used by the judge.
- The LinkedIn post chain: `fmt-linkedin-post`, which works out the idea, the reader's questions and the shape first, drafts in stages (skeleton, body, hook, close), and draws on 18 hook moves, 9 body structures and 357 sorted real posts, and ten post types in `types/` (owned story, borrowed story, arbitraged content, newsjacking, op-ed, power listicle, simple listicle, proof post, shortie, super-specific how), each a command that runs `/post` with that type.
- The author's methods as their own commands: `/visual-philosophy`, `/genius-of-contradiction`, `/copylosophy`, `/articulation-ladder` (`job-articulation-ladder`), `/three-tenses`, `/finding-your-personal-monopoly` (`job-personal-monopoly`), `/building-your-message` (`job-building-your-message`).
- The selling tools: `/offer-designer`, `/pricing-tests`, `/diagnosis-call`, `/pamphlet-power`, `/turning-prospects-into-collaborators`, writing through the standard in `craft-sales-copy`.
- The Substack essay chain: `fmt-substack-essay`, with a pilot library from 57 essays across six newsletters.
- The post visual: `fmt-post-visual`, with a grammar of 22 visual moves and nineteen variants, all drawn in the Figma master, built from the idea first by `craft-visual-philosophy`.
- The craft standards: `craft-house-rules` (every universal writing rule, the drafting method, the exception principle), `craft-refine` (the bar, the one constraint, test versus cornerstone), `craft-copylosophy`, `craft-visual-philosophy`, `craft-contradiction`, `craft-human`, and the check `check-human`.
- The house-rule scripts: `scripts/check-prose.py` (on every person-facing file and every reply, through the hooks) and `scripts/voice-diff.py` (a draft against the person's own markers), with `tests/prose/` and `scripts/test-prose.sh`.
- The voiceprint: `check-voiceprint` (`/voiceprint`) and `scripts/voiceprint.py`, the person's writing habits measured from `material/` (Burrows's and Cosine Delta, General Impostors, Craig's Zeta, 29 style measures), a draft read against them once per piece, and the rewrite pairs measured; with `tests/studio/voiceprint/`.
- The mechanical checks: `scripts/check-mechanical.py` and the mechanical half of `scripts/check-human.py`, with the detector call behind `--detector`.
- The writer's packet: `scripts/packet.py` builds `pieces/<id>/packet.md`, the one file the writer reads at the moment of writing (the writer's sheet, the brief, the cards the plan picked, the type's draft step, the voice). `/post` and `/essay` plan in one context, draft in the `writer` agent from the packet, judge in a third.
- The stitch check: `scripts/check-stitch.py` finds the person's sentences lifted word for word from `material/`, `inbox/` or `canon/` into a draft without a `verbatim` mark, and enforces the verbatim cap. Run by `self-check.py`, the draft hook and the judge (H34).
- The working banks in `bank/` (ideas, credibility, questions, the evidence ledger, rewrites, the voiceprint, the tense bank and the swipe file, with the whole saved posts in `bank/swipe/`) apart from the confirmed canon.
- `material/` for what the person has already made, and `inbox/` with `scripts/inbox-to-text.py` and `scripts/inbox-done.py`.
- The six hooks: the state at session start, the write guard, the command guard, the checks on every draft and every person-facing file, the reply check, and a save after every reply (`docs/hooks.md`).
- The session log (`sessions/log.md`) and `/end`, which writes one `ran:` line per session.
- Recipes: `job-recipes` (`/recipes`). `/end` offers to save a chain of commands that ran with the same choices in three sessions; each recipe is the person's (`recipes/<name>.md`, run as `/<name>`), holds no method, and never changes a studio skill. `/tidy` and `/status` ask about recipes nobody runs.
- Updates: `scripts/update-studio.sh` (`/update`) from a folder or a URL, with `studio.manifest.yaml` as the ownership split.
- The public template: `scripts/make-template.sh`.
- One-command client builds: `scripts/make-client.sh`, and the scheduled run in `docs/automation.md`.
- The studio test set in `tests/studio/`, including the hook tests.

## Not built yet

- Formats beyond the LinkedIn post and the Substack essay: video scripts, talk outlines, newsletters, emails and pages. Each needs a library of real examples sorted into moves before its skill is worth using (`docs/briefs/formats.md` in the studio repo).
- Carousels as their own format skill.
- The post archive with performance numbers, and the librarian weighing what worked (what the pieces that worked have in common). The numbers already arrive as `signal` lines in each piece's log (`setup-sources`, "Results", since 0.64); weighing them is what's missing (`docs/briefs/librarian-results.md` in the studio repo).
- `/coach` as an advisor drawing on the author's and his mentors' thinking (parked; `docs/briefs/coach.md` in the studio repo).
- The Claude app path without Claude Code; the skills read each other by path.
- A separation layer for one studio running several people.
- Output tests for the new job skills (shape, journal, refine, manifesto, understand, adapt, tidy, teardown): briefs with known-good outcomes, like `tests/studio/`.
- What's still open from reading other people's repos (point edits, a blind reader, comments and replies as a format, a first-section stop for cornerstone essays, corrections for a shipped piece, the Substack pieces and more), one list with each item's source (`docs/briefs/borrowed-status.md` in the studio repo).
