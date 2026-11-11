# Test: intake through the form, then /start and the first interview session

`answers.yaml` is a fictional client's filled-in form: Lena Okafor, fractional CFO in Lisbon, 60 LinkedIn posts exported, four untranscribed calls, wants Notion, not Figma, one assistant, two stop-list rules in her notes.

Build her instance with `python3 scripts/build-instance.py tests/studio/intake-form-lena/answers.yaml --studio . --out <somewhere>` (put a stub `linkedin-posts.csv` in an `--inbox` folder), then run `/start` and "start my brand tree" once, with one agent playing both sides and inventing nothing beyond the files. Check:

- Every sentence in `YOUR-STUDIO.md` reads as a person wrote it: her words in quotes, lists rendered as sentences or bullets, no first-person inside a second-person sentence, no double period, no "(wants to start)" after "publish on".
- `config/tools.md` says "not yet" in words where a setup skill fills a line later; a skipped team question says "not given", not "nobody else".
- `setup-progress.md` has no tick next to a tool that isn't wanted.
- `/start` greets her by name, names the guide and her answers file, says the Notion half-sentence, says the road in two sentences without the first stage, and doesn't promise the read-back of material that isn't text in `inbox/`; it says the untranscribed calls need transcripts.
- The brand tree reads her intake back in two or three sentences, asks neither what she does nor what material she has, routes with the "two rows true" rule (material first, then her answer), and writes her two notes as draft X entries in `stop-list.md`.
- The goal is read back from `outcomes.md` and sharpened, not re-asked; the goal entry stays draft with the agreed line in its log.
- `bash scripts/status.sh` shows the stage first and no "missing" lines; `bash scripts/setup-check.sh` says the install is fine and the rest runs later, with no FAIL.
- The brand tree's ending sets the stage in `setup-progress.md` to "brand tree, in progress".

`first-run/` holds the first run, before the fixes in 0.12.0: the transcript, the agent's notes, the `YOUR-STUDIO.md` the script wrote, and the studio notes.

This run predates 0.34; its files use the old paths and letters.
