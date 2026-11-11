# Canon

Everything the studio knows about the person: their brand tree, vehicle, brand strategy, audience, voice and content plan. This folder belongs to the person. Studio updates never touch it.

Setup fills it in two phases. Intake (the form before install, or "set up my studio" inside Claude) writes `setup-progress.md`, `strategy/outcomes.md` and `visual/brand-assets.md`. The brand tree interview ("start my brand tree", which `/start` points you at) creates the rest from `skills/setup-brand-tree/templates/`; `core-summary.md` appears when the minimum is confirmed, and the content plan and channel files when the strategy runs. The layout:

```
canon/
  progress.md          the interview's tracker
  setup-progress.md    where you are in setup (written by intake, kept current by /start and the interview)
  core-summary.md      the digest, written once the minimum is confirmed
  canon-index.md       every ID, one line each
  about-you.md         the one page about you for any AI (setup-about-you, /about)
  readback.md          the read-back of your material before the interviews (setup-readback)
  manifesto.md         the full manifesto, a draft until you confirm it (/manifesto)
  person/              values, behaviors, POVs, philosophy, thesis, branches, stop list
  bank/                stories and proof, confirmed and draft (only confirmed ones feed content)
  vehicle/             goal, business, offers, calls to action
  strategy/            outcomes, brand strategy, audience, content plan, channels/<channel>.md, strategy-review.md,
                       personal-monopoly.md (/finding-your-personal-monopoly), messaging-framework.md (/building-your-message)
  voice/               voice guide
  visual/              brand assets from intake; design-system.md from setup-visual-identity; contradiction-brief.md from /genius-of-contradiction
```

The working banks (ideas, credibility, questions, the evidence ledger, the rewrites, the voiceprint, the tense bank and the swipe file) live in the top-level `bank/` folder, not here.

Which entries feed content is rule 2 in `CLAUDE.md`.
