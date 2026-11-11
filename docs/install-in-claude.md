# Installing the studio

## The template

The public template at github.com/JosueVallesP/studio-template is an empty instance of the studio, rebuilt by `scripts/make-template.sh` after every version. You open an empty folder in the Claude app's Code tab and paste one line (it's at the top of `docs/getting-started.md`, which is the template's README): clone the template, then `/start`. The setup questions run inside Claude (`setup-intake`), so there's no form, no build step and no invite. `/update` pulls the next version from the same URL.

Once the studio is installed, `docs/quick-start.md` is the page to read: what you can use on day one, what waits for the interviews, and the order.

## For selling at volume (optional)

None of this is needed; the template path above does the same job with the person answering inside Claude.

**Publishing the template.** `bash scripts/make-template.sh https://github.com/JosueVallesP/studio-template` rebuilds it from the studio repo.

**A form and a one-command build.** The Tally form is described in `docs/tally-form.md`. `scripts/make-client.sh` turns a submission into a buyer's private repo in one command, and `docs/automation.md` runs that from GitHub on a schedule.

**Building an instance by hand in Claude Code.** Make a separate instance, so a person's files never live inside the studio repo. From the intake answers (`docs/intake-questions.md`, as a form or by editing `templates/intake/answers.yaml`): `python3 scripts/build-instance.py answers.yaml --studio . --out ../my-studio --inbox ./their-uploads`. The instance comes out with their settings, outcomes, brand assets and `YOUR-STUDIO.md` already written, so the first `/start` greets them by name. Without answers: `bash scripts/update-studio.sh . --init ../my-studio`, and `/start` asks them to say "set up my studio" so the same questions run inside Claude. Either way, open `../my-studio` in Claude Code. When the studio updates, run `/update` in the instance; it replaces the studio's folders and never touches the person's.

## A built-for-you studio: the Claude app, Cloud environment

A buyer installs the Claude app (Mac or Windows) and nothing else: no terminal, no Git, no Node.js. Once their private repo exists, they connect GitHub in the app (Settings, Connectors), open the Code tab, pick the **Cloud** environment and their repo, and start a session; the hooks, skills and agents run in the cloud VM as they do locally. Cloud, not Local, on purpose: Local would need Git and a clone on their machine, the hooks need bash (not there on plain Windows), and the push-updates job only reaches a buyer who opens a fresh clone each session. The buyer email and `docs/getting-started.md` use only this path, matching the Notion course; the email links the course when `GUIDE_URL` is set and falls back to `docs/getting-started.md`. Uploads during a web session go in through the chat (the studio files them into `inbox/`).

**Keys on Cloud.** A Cloud session starts from a fresh copy of the repo, and `.env` is never saved to GitHub, so a key kept in `.env` is gone the next session. On Cloud, set each key as an environment variable of the Cloud environment instead (in the Code tab, the environment's settings): `PANGRAM_API_KEY` for the detector, `NOTION_TOKEN` when Notion connects through a token, and `BASE44_API_KEY` for the dashboard app. The scripts read the environment first and `.env` second, so the same studio works on a computer with `.env` and on Cloud with the environment's variables. `/check` warns about any key a connected tool needs that isn't set either way.

## The Claude app without Claude Code

Not supported yet; the skills read each other by path.
