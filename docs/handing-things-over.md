# Handing things over, and naming places to the person

The person never sees the studio's folders unless they go looking, and most clients have never opened a GitHub repo. So a sentence like "drop the files in `inbox/`" asks them to do something with a thing they can't find. This page is the one place that says how the studio names its places to the person and how a file gets from them to the studio. Every skill that asks for a file, or names a folder or file to the person, follows it.

## The rule

**Never name a folder or file to the person without saying, in the same breath, what it is and how they get something into it or open it.** Once per conversation is enough: after the first time, "your inbox" alone is fine. A path in backticks with no explanation is never fine in a reply. This is house rule S14 (`skills/craft-house-rules`).

Better still, don't make them deal with a folder at all. The person hands things over in the chat, and the studio files them. "Send it to me here" beats "put it in `inbox/`" every time it works.

## Where the studio is running

The session-start hook prints one line, `WORKSPACE: cloud` or `WORKSPACE: local`. It decides which instructions you give.

- **Cloud** (how every client built by the studio's author works): the studio runs in Claude's workspace online, on a copy of their GitHub repo. Their studio's folders are not on their computer. There is no folder for them to open in Finder or File Explorer, so never tell them to drop a file in one.
- **Local** (someone who installed it themselves): the studio is a folder on their computer, the one they picked in the Code tab. `inbox` is a folder inside it they can open and drag files into.

## How a file gets to the studio

Say the first way that fits. Offer the next one only when the first doesn't work for them.

**Text: paste it.** Old posts, an essay, notes, a transcript they can copy: paste it into the box where they type. Nothing else to do. The studio saves it (to `material/` when it's something they made and want kept, as `CLAUDE.md` says under "save this to my material").

**A file, on Cloud: attach it to the message.** Drag the file into the box where they type, or use the attach button beside that box, and send it with a line saying what it is. When a message arrives with a file attached, copy it into `inbox/` under its original name, say in one line that it's in their inbox, and carry on. Their logo, a PDF, a Word file and an export ZIP all go this way.

**A file the chat won't take, on Cloud: upload it on GitHub.** Some files are too big for the chat or a type it won't accept. Then build the upload link from their repo (`git remote get-url origin`, turned into `https://github.com/<owner>/<repo>/upload/main/inbox`) and give it to them with three steps: open the link, drag the files onto the page, click the green **Commit changes** button. Then they tell you it's done, and you run `git pull --ff-only` so the files reach this session. Say once that this is the same studio, seen on GitHub's website.

**A file, on Local: put it in the inbox folder.** Tell them where it is in words: "the folder called `inbox` inside your studio folder (the one you picked when you opened the Code tab)". On a Mac they open it in Finder, on Windows in File Explorer, and drag the file in. Attaching it to the message works here too.

**Audio or video:** the studio reads text, so it needs a transcript first. Name the tool they already use if you know it (Zoom, Otter, Fathom, Descript and YouTube all export one). If a call recorder or YouTube is connected ("connect my sources"), pull it for them instead.

**Paper:** a photo of each page, attached like any file, or typed out and pasted.

**A link:** the studio can't read most links (a LinkedIn profile, a Substack page, a video). Ask for the text or the file instead, and say why in half a sentence.

## The places, in plain words

When you have to name one, use these words. Never "canon" or another studio label without its gloss (S4).

| Place | Say it like this |
| --- | --- |
| `inbox/` | "Your inbox, a folder in your studio where anything you hand over waits until the studio reads it. You don't sort or rename anything." |
| `material/` | "The folder where the studio keeps what you've already made (posts, essays, talks), so every piece can draw on it." The person never has to put anything here; the studio does. |
| `canon/` | "Your files: what you've confirmed in the interviews about what you believe, your stories and how you talk." |
| `YOUR-STUDIO.md` | "Your guide: your next step, the whole road and how to hand things over." Never send them to the file; "show my guide" puts it in the chat. |
| `config/intake.yaml` | "Your answers to the setup questions." To change one, they say "set up my studio" again; don't send them to edit the file. |
| `proposals.md` | "Suggested changes to your files, waiting for your yes." `/status` shows them, so they never need to open it. |
| `pieces/` | "Your pieces, one folder each." `/status` and the dashboard show them. |
| The visual kit | "Your visual kit, the set of templates in Figma for the pictures in your posts." |

## An example

The intake's last question, said badly:

> Do you already have a logo, brand colors or fonts? Name them or drop the files in `inbox/`; they go on your visual kit today.

The same question, on Cloud:

> Last question. Do you already have a logo, brand colors or fonts? If you do, tell me the names of your fonts and your colors (hex codes like #1A2B3C if you have them, or just "dark green"), and send me your logo: drag the file into the box where you type, and I'll put it in your studio. I'll use all of it on your visual kit, the templates in Figma for the pictures in your posts. If you don't have any of this, just say so. After the interviews, the studio builds a look from what it learns about you.

On Local, the logo line becomes: "send me your logo here, or drag it into the folder called `inbox` inside your studio folder."
