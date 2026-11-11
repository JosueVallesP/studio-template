#!/usr/bin/env python3
"""Turns what people upload into text the studio can read, in inbox/.

  python3 scripts/inbox-to-text.py            convert everything new in inbox/
  python3 scripts/inbox-to-text.py --dry-run  say what it would do

What it does with each file in inbox/ (not in inbox/done/ or inbox/originals/):
  Shares.csv (LinkedIn data export)  -> linkedin-posts.md, one section per post with its date
  Comments.csv (LinkedIn data export)-> linkedin-comments.md, one section per comment with its date and the
                                        link of the post it was on; voiceprint leaves this file out (comments
                                        are too short to measure a voice by), the map and capture read it
  .zip (a Substack export, or any)   -> unpacked; Substack posts become substack-posts.md, one section per
                                        post with its title, subtitle and date, and the ZIP is deleted
                                        (it holds the subscriber list, which the studio never keeps);
                                        other ZIPs are converted by the rules here (a LinkedIn archive gives
                                        Shares.csv and Comments.csv; its other CSVs are left out)
  .docx                              -> <name>.md with the document's text
  .html / .htm                       -> <name>.md with the page's text
  .pdf, .md, .txt, other .csv        -> left as they are (the studio reads them directly)
  audio and video                    -> left, and listed as "needs a transcript"
  anything else                      -> left, and listed as "can't read"

Every text file it writes, and every .md and .txt left in inbox/, gets three more steps:
  - Hidden characters out. Zero-width characters, soft hyphens and Unicode tag characters are removed,
    and non-breaking spaces become plain spaces. Tag characters can hide instructions, so the output
    names any file that had them.
  - A summary check. A recorder's AI summary (Fathom, Otter, Granola, Fireflies: "Summary", "Action
    items", "Key takeaways") reads like notes about the person, not their words. Plain rules decide it,
    with no model call: summary headings, no speaker turns, the person or "they" reported in the third
    person ("she explained", "the team discussed"), mostly short bullet points, almost no "I". A file that
    scores high enough gets this line at the top, and the output lists it:
      <!-- studio: looks like a summary, not their words: <the signals found> -->
    Capture and the map read that line: nothing in the file becomes the person's words (CLAUDE.md
    rules 1 and 3). A transcript with speaker turns is never marked. Nothing is blocked or deleted.
  - A ChatGPT check. Text copied out of ChatGPT carries tokens nothing else leaves behind (oaicite,
    contentReference[, turn0search0, citation brackets like 【12†source】, utm_source=chatgpt.com in links).
    A file with any of them gets the ghostwritten line at the top, and the output lists it:
      <!-- studio: written for them, not by them: pasted from ChatGPT (<the token found>) -->
    The text is kept as it is. The person says which parts are theirs. A file already marked either way
    isn't marked again, and a file marked as pasted from ChatGPT skips the summary check.

Originals that were converted move to inbox/originals/, so nothing is lost and nothing is read twice.
No dependencies beyond Python 3. Run from the instance root. make-client.sh runs it after the build;
job-map, setup-first-post and role-capture run it before they read the inbox.
"""
import csv, html, io, os, re, shutil, sys, zipfile
from html.parser import HTMLParser

INBOX = "inbox"
SKIP_DIRS = {"done", "originals"}
READ_AS_IS = {".pdf", ".md", ".txt", ".csv", ".markdown"}
AV = {".mp3", ".m4a", ".wav", ".aac", ".ogg", ".mp4", ".mov", ".m4v", ".webm", ".avi"}
IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ai", ".eps"}
DRY = "--dry-run" in sys.argv

SUMMARY_MARK = "<!-- studio: looks like a summary, not their words"
GHOST_MARK = "<!-- studio: written for them, not by them"

# Hidden characters: removed (zero-width, word joiner, BOM, soft hyphen, Unicode tags) or made plain spaces.
ZERO_WIDTH = re.compile("[\u200b-\u200d\u2060\ufeff\u00ad]")
TAGS = re.compile("[\U000E0000-\U000E007F]")
NBSP = re.compile("[\u00a0\u202f]")


def clean_hidden(text):
    """Text with hidden characters taken out, and how many of them were Unicode tag characters."""
    tags = len(TAGS.findall(text))
    text = TAGS.sub("", text)
    text = ZERO_WIDTH.sub("", text)
    return NBSP.sub(" ", text), tags


# The summary check. Plain rules, no model call. Each signal adds to a score; at SUMMARY_AT or more the
# file is marked. Speaker turns mean a transcript, and a transcript is never marked.
SUMMARY_AT = 5
SUMMARY_HEADS = ["meeting summary", "summary", "action items", "action item", "key takeaways", "takeaways",
                 "next steps", "overview", "highlights", "meeting notes", "key points", "topics discussed",
                 "meeting purpose", "outline", "chapters", "decisions"]
HEAD_RE = re.compile(r"^\s*(?:#{1,6}\s*|\*\*|__)?\s*(" + "|".join(re.escape(h) for h in SUMMARY_HEADS)
                     + r")\s*(?:\*\*|__)?\s*:?\s*(?:\*\*|__)?\s*$", re.I)
NOT_SPEAKERS = {"summary", "overview", "date", "time", "attendees", "participants", "duration", "title",
                "meeting", "note", "notes", "link", "location", "subject", "re", "from", "to", "cc", "purpose",
                "agenda", "owner", "due", "status", "topic", "topics", "highlights", "outline", "decisions",
                "action items", "next steps", "key takeaways", "takeaways", "recording", "transcript", "source",
                "published", "q", "a", "ps", "p.s", "edit", "update", "tl;dr", "tldr"}
STAMP = r"(?:\[?\(?\d{1,2}:\d{2}(?::\d{2})?\)?\]?)"
TURN_RE = re.compile(r"^\s*(?:" + STAMP + r"\s*)?(?:\*\*)?(Speaker \d+|[A-Z][\w.'-]*(?: [A-Z][\w.'-]*){0,3})(?:\*\*)?"
                     r"\s*(?:" + STAMP + r")?\s*(?:\*\*)?:(?:\*\*)?\s+\S")
STAMP_LINE = re.compile(r"^\s*" + STAMP + r"\s*(?:[-\u2013]\s*)?(?:Speaker \d+|[A-Z][\w.'-]*(?: [A-Z][\w.'-]*){0,3})?\s*:?\s*$|^\s*" + STAMP + r"\s+\S")
NAME_STAMP_LINE = re.compile(r"^\s*(?:Speaker \d+|[A-Z][\w.'-]*(?: [A-Z][\w.'-]*){0,3})\s+" + STAMP + r"\s*$")  # Otter: "Ana Ruiz  0:03"
REPORTING = re.compile(r"\b(?:he|she|they|the speaker|the host|the guest|the team|the client|the group|[A-Z][a-z\u00c0-\u017f]+)\s+"
                       r"(?:also\s+)?(?:explained|discussed|mentioned|noted|emphasi[sz]ed|highlighted|outlined|shared|"
                       r"expressed|stressed|described|suggested|reiterated|walked through)\b")
BULLET = re.compile(r"^\s*(?:[-*\u2022\u25aa]|\d+[.)])\s+")
FIRST_PERSON = re.compile(r"\b(?:I|I'm|I've|I'd|I'll|me|my|mine|myself)\b")


def summary_signals(text):
    """The signals that say a text reads as a summary about the person rather than their own words.
    Returns (score, signals); a transcript with speaker turns returns (0, [])."""
    lines = [l for l in text.splitlines() if l.strip() and not l.strip().startswith("<!--")]
    if not lines: return 0, []
    turns = 0
    for l in lines:
        m = TURN_RE.match(l)
        if m and m.group(1).lower().rstrip(".") not in NOT_SPEAKERS: turns += 1
        elif STAMP_LINE.match(l) or NAME_STAMP_LINE.match(l): turns += 1
    if turns >= 4: return 0, []
    score, found = 0, []
    heads = []
    for l in lines:
        m = HEAD_RE.match(l)
        if m and m.group(1).lower() not in [h.lower() for h in heads]: heads.append(m.group(1).strip().capitalize())
    if heads:
        score += 2 * min(len(heads), 3); found.append("summary headings (" + ", ".join(heads) + ")")
    reports = len(REPORTING.findall(text))
    if reports >= 2:
        score += 3 if reports >= 5 else 2
        found.append(f"the person reported in the third person ({reports} lines like \"they explained\")")
    bullets = [l for l in lines if BULLET.match(l)]
    if len(lines) >= 5 and len(bullets) / len(lines) >= 0.4:
        lens = sorted(len(BULLET.sub("", l).split()) for l in bullets)
        if lens[len(lens) // 2] <= 20:
            score += 2; found.append("mostly short bullet points")
    words = re.findall(r"[A-Za-z']+", text)
    if len(words) >= 80 and len(FIRST_PERSON.findall(text)) / len(words) < 0.005:
        score += 1; found.append("almost no \"I\"")
    if score < SUMMARY_AT: return score, []
    return score, ["no speaker turns"] + found


# Tokens that only ChatGPT's output leaves in copied text: its citation markup, its search-result ids
# (turn0search0, turn2news1, turn1view0), its citation brackets and the tag it adds to links.
CHATGPT = re.compile(r"oaicite|:?contentReference\[|turn\d+(?:search|news|view)\d+|\u3010\d+(?::\d+)?\u2020[^\u3011\n]{0,40}\u3011?"
                     r"|utm_source=chatgpt\.com")


def chatgpt_token(text):
    """The first ChatGPT-only token in the text, or None."""
    m = CHATGPT.search(text)
    return m.group(0) if m else None


def finish_text(text, label, notes):
    """Hidden characters out, then the ChatGPT check, then the summary check. Returns the text to write;
    notes collect what to say."""
    text, tags = clean_hidden(text)
    if tags: notes["tags"].append(f"{label}: removed {tags} hidden tag character{'' if tags == 1 else 's'} (they can hide instructions)")
    head = "\n".join(text.lstrip().splitlines()[:3])
    if SUMMARY_MARK in head:
        notes["summary"].append(f"{label}: marked before")
        return text
    if GHOST_MARK in head: return text
    token = chatgpt_token(text)
    if token:
        # Keeps GHOST_MARK as its exact prefix: voiceprint.py and studio_checks.corpus_files match on it.
        text = f"{GHOST_MARK}: pasted from ChatGPT ({token}) -->\n\n" + text
        notes["chatgpt"].append(f"{label}: found {token}")
        return text
    _, signals = summary_signals(text)
    if signals:
        text = f"{SUMMARY_MARK}: {'; '.join(signals)} -->\n\n" + text
        notes["summary"].append(f"{label}: {'; '.join(signals)}")
    return text


NOTES = {"tags": [], "summary": [], "partial": [], "chatgpt": []}


class Text(HTMLParser):
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "tr", "section", "article"}
    def __init__(self):
        super().__init__(); self.out, self.skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"): self.skip += 1
        if tag in self.BLOCK: self.out.append("\n\n")
        if tag == "li": self.out.append("- ")
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip: self.skip -= 1
        if tag in self.BLOCK: self.out.append("\n\n")
    def handle_data(self, data):
        if not self.skip: self.out.append(data)
    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t]+", " ", t)
        return re.sub(r"\n\s*\n+", "\n\n", t).strip()


def html_to_text(raw):
    p = Text(); p.feed(raw); return p.text()


def docx_to_text(data):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    paras = []
    for para in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        bits = re.findall(r"<w:t[^>]*>(.*?)</w:t>", para, re.S)
        paras.append(html.unescape("".join(bits)))
    return "\n\n".join(p for p in paras if p.strip())


def linkedin_shares(data):
    rows = list(csv.DictReader(io.StringIO(data.decode("utf-8-sig", "ignore"))))
    keys = {k.lower(): k for k in (rows[0].keys() if rows else [])}
    text_k, date_k, link_k = keys.get("sharecommentary"), keys.get("date"), keys.get("sharelink")
    if not text_k: return None
    posts = [r for r in rows if (r.get(text_k) or "").strip()]
    posts.sort(key=lambda r: r.get(date_k) or "", reverse=True)
    out = [f"# LinkedIn posts (from the data export, {len(posts)} posts, newest first)\n"]
    for r in posts:
        body = (r.get(text_k) or "").replace('""', '"').strip().strip('"')
        out.append(f"## Post, {(r.get(date_k) or '').split(' ')[0]}\n\n{body}\n" + (f"\nLink: {r.get(link_k)}\n" if link_k and r.get(link_k) else ""))
    return "\n".join(out)


def linkedin_comments(data):
    text = data.decode("utf-8-sig", "ignore")
    # LinkedIn's Comments.csv sometimes escapes quotes with a backslash (\") instead of doubling them.
    escape = "\\" if '\\"' in text else None
    rows = list(csv.DictReader(io.StringIO(text), escapechar=escape))
    keys = {k.lower(): k for k in (rows[0].keys() if rows else []) if k}
    text_k, date_k, link_k = keys.get("message"), keys.get("date"), keys.get("link")
    if not text_k: return None
    comments = [r for r in rows if (r.get(text_k) or "").strip()]
    comments.sort(key=lambda r: r.get(date_k) or "", reverse=True)
    out = [f"# LinkedIn comments (from the data export, {len(comments)} comment{'' if len(comments) == 1 else 's'}, newest first)\n",
           "These are your comments on other people's posts. The map and capture read them for the positions you take. "
           "Voiceprint leaves them out, because comments are too short to measure your writing by.\n"]
    for r in comments:
        body = (r.get(text_k) or "").replace('""', '"').strip().strip('"')
        out.append(f"## Comment, {(r.get(date_k) or '').split(' ')[0]}\n\n{body}\n" + (f"\nOn the post: {r.get(link_k)}\n" if link_k and r.get(link_k) else ""))
    return "\n".join(out)


def substack_posts(z):
    names = z.namelist()
    meta = {}
    csv_name = next((n for n in names if n.endswith("posts.csv")), None)
    if csv_name:
        for r in csv.DictReader(io.StringIO(z.read(csv_name).decode("utf-8-sig", "ignore"))):
            pid = (r.get("post_id") or "").strip()
            if pid: meta[pid] = r
    htmls = [n for n in names if n.lower().endswith(".html") and "/posts/" in "/" + n]
    if not htmls: return None
    out, count = [], 0
    for n in sorted(htmls):
        pid = os.path.basename(n)[:-5]
        m = meta.get(pid, {})
        if m and str(m.get("is_published", "true")).lower() not in ("true", "1", "yes"): continue
        body = html_to_text(z.read(n).decode("utf-8", "ignore"))
        if not body: continue
        title = m.get("title") or pid.split(".", 1)[-1].replace("-", " ")
        sub, date = m.get("subtitle", ""), (m.get("post_date") or "")[:10]
        out.append(f"## {title}\n" + (f"\n*{sub}*\n" if sub else "") + (f"\nPublished {date}\n" if date else "") + f"\n{body}\n")
        count += 1
    return f"# Substack essays (from the export, {count} published post{'' if count == 1 else 's'})\n\n" + "\n".join(out)


def write(name, text, report):
    path = os.path.join(INBOX, name)
    base, ext = os.path.splitext(path); n = 2
    while os.path.exists(path): path = f"{base}-{n}{ext}"; n += 1
    text = finish_text(text, path, NOTES)
    if not DRY: open(path, "w", encoding="utf-8").write(text)
    report.append(f"wrote {path}")


def stash(path, report):
    dest_dir = os.path.join(INBOX, "originals")
    if not DRY:
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(path, os.path.join(dest_dir, os.path.basename(path)))
    report.append(f"moved {path} to inbox/originals/")


def check_as_is(path, label, report):
    """A .md or .txt left in inbox/: hidden characters out and the summary check, written back in place
    only when something changed."""
    raw = open(path, "rb").read()
    try: text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", "replace")
        NOTES["partial"].append(f"{label}: some characters couldn't be read (not UTF-8 text); they show as \ufffd")
    new = finish_text(text, label, NOTES)
    if new != text and not DRY:
        open(path, "w", encoding="utf-8").write(new)


def convert_zip(path, report, unread):
    with zipfile.ZipFile(path) as z:
        sub = substack_posts(z)
        if sub: write("substack-posts.md", sub, report)
        for n in z.namelist():
            if n.endswith("/") or n.startswith("__MACOSX") or "/posts/" in "/" + n and n.lower().endswith(".html"): continue
            ext, base = os.path.splitext(n)[1].lower(), os.path.basename(n)
            try:
                data = z.read(n)
            except Exception as e:
                NOTES["partial"].append(f"{base} (inside {os.path.basename(path)}): couldn't be read ({e}); the rest of the ZIP came through")
                continue
            if base.lower() == "shares.csv":
                t = linkedin_shares(data)
                if t: write("linkedin-posts.md", t, report)
            elif base.lower() == "comments.csv":
                t = linkedin_comments(data)
                if t: write("linkedin-comments.md", t, report)
            elif ext == ".docx": write(os.path.splitext(base)[0] + ".md", docx_to_text(data), report)
            elif ext in (".html", ".htm"): write(os.path.splitext(base)[0] + ".md", html_to_text(data.decode("utf-8", "ignore")), report)
            elif ext in (".md", ".txt"):
                write(base, data.decode("utf-8", "ignore"), report)
            elif ext == ".pdf":
                if not DRY: open(os.path.join(INBOX, base), "wb").write(data)
                report.append(f"wrote inbox/{base}")
            elif ext in AV: unread.append(f"{base} (inside {os.path.basename(path)}): needs a transcript")
    if sub:
        # A Substack export also holds the subscriber list. Keep only the posts: never store subscribers' emails.
        if not DRY: os.remove(path)
        report.append(f"deleted {path} after taking the posts (it also held the subscriber list)")
    else:
        stash(path, report)


def main():
    if not os.path.isdir(INBOX):
        print("no inbox/ here; run from the studio's folder"); return
    report, unread = [], []
    for name in sorted(os.listdir(INBOX)):
        path = os.path.join(INBOX, name)
        if os.path.isdir(path) or name.startswith(".") or name.lower() == "readme.md": continue
        ext = os.path.splitext(name)[1].lower()
        try:
            if name.lower() == "shares.csv":
                t = linkedin_shares(open(path, "rb").read())
                if t: write("linkedin-posts.md", t, report); stash(path, report)
            elif name.lower() == "comments.csv":
                t = linkedin_comments(open(path, "rb").read())
                if t: write("linkedin-comments.md", t, report); stash(path, report)
            elif ext == ".zip": convert_zip(path, report, unread)
            elif ext == ".docx": write(os.path.splitext(name)[0] + ".md", docx_to_text(open(path, "rb").read()), report); stash(path, report)
            elif ext in (".html", ".htm"): write(os.path.splitext(name)[0] + ".md", html_to_text(open(path, encoding="utf-8", errors="ignore").read()), report); stash(path, report)
            elif ext in (".md", ".txt", ".markdown"): check_as_is(path, path, report)
            elif ext in READ_AS_IS or ext in IMAGES: pass
            elif ext in AV: unread.append(f"{name}: audio or video, needs a transcript (Zoom, Otter, Descript and YouTube export one)")
            else: unread.append(f"{name}: a file type the studio can't read; save it as PDF, Word or text")
        except Exception as e:
            unread.append(f"{name}: couldn't convert ({e})")
    for line in report: print("  " + line)
    if unread:
        print("Can't read yet:")
        for line in unread: print("  " + line)
    if NOTES["partial"]:
        print("Read only in part:")
        for line in NOTES["partial"]: print("  " + line)
    if NOTES["summary"]:
        print("Looks like a summary (not filed as their words):")
        for line in NOTES["summary"]: print("  " + line)
    if NOTES["chatgpt"]:
        print("Looks pasted from ChatGPT (ask the person which parts are theirs):")
        for line in NOTES["chatgpt"]: print("  " + line)
    if NOTES["tags"]:
        print("Hidden characters removed:")
        for line in NOTES["tags"]: print("  " + line)
    if not report and not unread and not NOTES["summary"] and not NOTES["tags"] and not NOTES["partial"] and not NOTES["chatgpt"]:
        print("  inbox: nothing to convert")


if __name__ == "__main__":
    main()
