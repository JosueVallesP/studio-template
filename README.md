# Your content studio

This is a studio that writes posts, essays and visuals that sound like you, from what you believe and what you've actually done. It runs inside Claude, on plain files you own. The setup questions take about five to ten minutes, and you can use it the same day.

## What you need

- **Claude** on a paid plan (Pro or Max), and the **Claude app** on your Mac or Windows computer (free, from claude.com/download). Claude Code, which runs the studio, comes with those plans; it's the app's Code tab.
- A free **GitHub** account. Your studio lives in a private repository there that only you (and whoever built it for you) can see.
- Optional: free accounts on **Notion** (your dashboard) and **Figma** (your visual kit). The studio works without them, and you can add them later.

## If your studio was built for you (15 minutes)

You got an email with your studio's name and a link to your private repository. Then:

1. **Accept the GitHub invite.** GitHub emailed it separately: click **View invitation**, then **Accept invitation**. Can't find it? Check spam, or go to github.com/notifications while signed in. Invites expire after 7 days; if yours did, reply to the email and you'll get a new one.
2. **Install the Claude app.** Go to claude.com/download and pick Mac or Windows.
   - On a Mac: open the file you downloaded, drag Claude into your Applications folder, then open it from there.
   - On Windows: open the file you downloaded and follow the steps. Claude opens when it's done.
   - Sign in with the account that has your paid plan. Already have the app? Update it first (Mac: **Claude** in the top menu bar, then **Check for Updates**; Windows: **Help**, then **Check for Updates**).
3. **Open Claude Code and choose Cloud.** In the app, click **Code** near the top of the left sidebar. Under the box where you type, click the first button and choose **Cloud**. Not Local: Local works on a folder on your computer, and your studio lives on GitHub. The app remembers this.
4. **Connect GitHub and pick your studio.** The first time you start a Cloud session, Claude asks you to connect GitHub: click the button, sign in with the GitHub username you gave, and click **Authorize**. If GitHub offers to install Claude on your own account, click **Skip**; whoever built your studio has already set that up on their side. If Claude doesn't ask, connect it in the app: your name in the bottom-left corner, **Settings**, **Connectors**, GitHub, **Connect**. Then choose your studio from the list.
5. **Type `/start`** and press enter (or anything at all, even "hi"). The studio opens with a welcome: what it does, the order to do things in, and what you can use right away.

The only thing you install is the Claude app. You don't need a terminal, Node.js or any code: the studio runs in Claude's own workspace online, so it works the same on a Mac and on Windows. (If you install it yourself instead, below, the studio runs on your computer, and its automatic checks and saves need a Mac, Linux, or Windows with WSL or Git Bash installed.)

If Claude asks for permission to run something, allow it. Those are the studio's own small programs: one saves your work after every reply, others check your drafts. They run in Claude's workspace online and only touch your studio's files.

Your studio already knows your name and your answers from the form, and your uploads are in its inbox. Every session saves and backs itself up to your repository.

Next time, open the Claude app, click **Code**, and click your last session (or **New**). That's it.

## If you're installing it yourself (5 minutes)

This path runs the studio on your own computer. It needs a Mac, Linux, or Windows with WSL or Git Bash, because the studio's automatic checks and saves are small shell programs.


1. Make an empty folder on your computer and name it, for example, `my-studio`.
2. Open the Claude desktop app, go to the **Code** tab, and choose that folder.
3. Paste this and press enter:

   > Set up my content studio: clone https://github.com/JosueVallesP/studio-template into this folder, then run /start.

That's it. Claude copies the studio into your folder and starts. The copy stays linked to the template only for updates; your own files never go back to it. If it asks you to trust the folder, say yes; that's what lets the studio save your work after every reply.

## What happens next

`/start` asks you a short set of questions about facts (who you are, what you do, where you publish, what you want a year from now) and asks for a few things you've already made: old posts, a talk, a transcript, anything in your words. Paste them into the chat, or attach the files: drag them into the box where you type and send them. The studio files them in your inbox, a folder in your studio where things you hand over wait until it reads them. If a file is too big for the chat, the studio gives you a link to upload it on GitHub instead (see "Handing over files" below). Then it builds the things you can use today: a map of how your ideas connect, read from everything you handed over (`/map`), your visual kit in Figma and your dashboard in Notion if you use them, and a post from your own material. The interviews, where it learns what you believe and how you talk, come after, in short sessions, whenever you want them.

Whenever you don't know what to do, say `/start` during setup or `/coach` after. Say `/end` when you're done for the day; the studio writes down what you decided so the next session starts from it.

## Handing over files

Your studio runs in Claude's workspace online, so its folders aren't on your computer and there's nothing for you to open in Finder or File Explorer. You hand things over in the chat:

- **Text** (an old post, notes, a transcript you can copy): paste it into the box where you type.
- **A file** (a PDF, a Word document, a Substack export, your logo): drag it into the box where you type, or use the attach button beside it, and send it with a line saying what it is. The studio puts it in your inbox.
- **A file the chat won't take** (too big, or a type it won't open): ask the studio for the upload link. It opens your studio's inbox on GitHub's website; drag the files onto the page, click the green **Commit changes** button, then tell the studio it's done.
- **Audio or video:** the studio reads text, so send the transcript. Zoom, Otter, Fathom, Descript and YouTube all export one.

If you installed the studio yourself on your own computer, you can also drag files into the folder called `inbox` inside your studio folder.

## Keeping it yours and backed up

Your files save themselves after every reply, journal entries included: a journal entry marked private is never read by the studio, but it's backed up with everything else. If your studio was built for you, it already lives in a private GitHub repository and backs itself up there. If you installed it yourself and it isn't in a GitHub repository yet, the studio offers once during `/start` to make a private one in your own account; say yes if you have a GitHub account, or skip it and come back to it with "back up my studio".

When the studio improves, say `/update`. It replaces the studio's own files and never touches yours.
