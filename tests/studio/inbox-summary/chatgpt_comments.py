#!/usr/bin/env python3
"""scripts/inbox-to-text.py marks text pasted from ChatGPT as written for the person, not by them, and turns
LinkedIn's Comments.csv (loose or inside the archive ZIP) into linkedin-comments.md, which voiceprint leaves out.
Builds a small studio in a temp folder; touches nothing in the repo.
Usage: python3 -I tests/studio/inbox-summary/chatgpt_comments.py"""
import importlib.util, io, os, subprocess, sys, tempfile, zipfile

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GHOST = "<!-- studio: written for them, not by them"
CHATGPT_MARK = GHOST + ": pasted from ChatGPT ("
SUMMARY = "<!-- studio: looks like a summary, not their words"

ESSAY = """# Why I stopped posting every day

For three years I posted every weekday. I had the numbers to show for it and nothing I was proud of.
Last spring I stopped. I wrote one essay a month instead, and I made each one the thing I'd say if a
client asked me what I believe about their work. My following grew slower. My inbox didn't. The people
who wrote to me had read four or five of the essays, and they already knew whether they agreed with me.
"""
OAICITE = "Positioning is a choice about who you leave out. :contentReference[oaicite:0]{index=0}\n\n" + ESSAY
CONTENTREF = "A body of work compounds over time contentReference[ and posts don't.\n\n" + ESSAY
BRACKET = "Most buyers read three pieces before they reach out 【12†source】.\n\n" + ESSAY
UTM = "See [the study](https://example.com/study?utm_source=chatgpt.com).\n\n" + ESSAY
SEARCH = "Readers trust what they can check. citeturn0search3\n\n" + ESSAY
ALREADY = SUMMARY + ": summary headings (Summary) -->\n\nSome notes :contentReference[oaicite:1]{index=1}\n\n" + ESSAY

COMMENTS = ('Date,Link,Message\n'
            '2024-03-02 10:15:00,https://www.linkedin.com/feed/update/urn:li:activity:111,"Yes. The first draft is for you,\nthe second is for the reader."\n'
            '2024-05-20 08:00:00,https://www.linkedin.com/feed/update/urn:li:activity:222,"I\'d push back on ""always post daily"" here."\n'
            '2024-01-10 09:00:00,https://www.linkedin.com/feed/update/urn:li:activity:333,""\n')
# Some exports escape quotes with a backslash instead of doubling them.
COMMENTS_BACKSLASH = ('Date,Link,Message\n'
                      '2023-11-05 12:00:00,https://www.linkedin.com/feed/update/urn:li:activity:444,"He called it \\"the slow way\\", and\nhe was right."\n')

ok = True
def check(name, cond, extra=""):
    global ok
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"\n     {extra}"))
    ok = ok and cond

def run(cwd):
    return subprocess.run([sys.executable, "-I", os.path.join(REPO, "scripts", "inbox-to-text.py")],
                          capture_output=True, text=True, cwd=cwd)

with tempfile.TemporaryDirectory() as t:
    inbox = os.path.join(t, "inbox"); os.makedirs(inbox)
    files = {"oaicite.md": OAICITE, "contentref.md": CONTENTREF, "bracket.md": BRACKET, "utm.txt": UTM,
             "search.md": SEARCH, "essay.md": ESSAY, "already.md": ALREADY}
    for name, text in files.items():
        open(os.path.join(inbox, name), "w", encoding="utf-8").write(text)
    open(os.path.join(inbox, "Comments.csv"), "w", encoding="utf-8-sig", newline="").write(COMMENTS)
    b = io.BytesIO()
    with zipfile.ZipFile(b, "w") as z:
        z.writestr("Basic_LinkedInDataExport/Comments.csv", COMMENTS_BACKSLASH)
        z.writestr("Basic_LinkedInDataExport/Connections.csv", "First Name,Last Name\nAna,Ruiz\n")
    open(os.path.join(inbox, "linkedin-archive.zip"), "wb").write(b.getvalue())

    r = run(t)
    out = r.stdout
    read = lambda n: open(os.path.join(inbox, n), encoding="utf-8").read()
    check("the script runs", r.returncode == 0, r.stderr)

    # ChatGPT
    check("a file with oaicite is marked at the top", read("oaicite.md").startswith(CHATGPT_MARK), read("oaicite.md")[:200])
    check("the mark names the token found", read("oaicite.md").splitlines()[0] == CHATGPT_MARK + ":contentReference[) -->",
          read("oaicite.md").splitlines()[0])
    check("a file with contentReference[ is marked", read("contentref.md").startswith(CHATGPT_MARK), read("contentref.md")[:200])
    check("a citation bracket is marked", read("bracket.md").startswith(CHATGPT_MARK), read("bracket.md")[:200])
    check("a chatgpt.com link tag is marked", read("utm.txt").startswith(CHATGPT_MARK), read("utm.txt")[:200])
    check("a turnNsearchN id is marked", read("search.md").startswith(CHATGPT_MARK + "turn0search3"), read("search.md")[:200])
    check("the text is otherwise kept as it is", read("oaicite.md").endswith(OAICITE), read("oaicite.md")[:300])
    check("an ordinary essay is not marked", read("essay.md") == ESSAY, read("essay.md")[:200])
    check("a file with the summary mark isn't marked again", read("already.md") == ALREADY, read("already.md")[:200])
    check("the output lists ChatGPT files under their own heading",
          "Looks pasted from ChatGPT (ask the person which parts are theirs):" in out
          and "oaicite.md" in out.split("Looks pasted from ChatGPT")[1] and "essay.md" not in out.split("Looks pasted from ChatGPT")[1], out)

    r2 = run(t)
    check("a second run doesn't mark a file twice", read("oaicite.md").count(GHOST) == 1 and "Looks pasted" not in r2.stdout,
          read("oaicite.md")[:300] + "\n" + r2.stdout)

    # Comments.csv
    loose = read("linkedin-comments.md")
    check("a loose Comments.csv becomes linkedin-comments.md", loose.startswith("# LinkedIn comments (from the data export, 2 comments"), loose[:200])
    check("the note says what the file is", "comments on other people's posts" in loose and "Voiceprint leaves them out" in loose, loose[:400])
    check("each comment has its date and the post's link",
          "## Comment, 2024-03-02" in loose and "On the post: https://www.linkedin.com/feed/update/urn:li:activity:111" in loose, loose)
    check("newest first", loose.index("2024-05-20") < loose.index("2024-03-02"), loose)
    check("a comment with a newline keeps it", "The first draft is for you,\nthe second is for the reader." in loose, loose)
    check("a doubled quote comes through as one quote", "I'd push back on \"always post daily\" here." in loose, loose)
    check("an empty comment is left out", "activity:333" not in loose, loose)
    check("the loose Comments.csv moves to originals", os.path.exists(os.path.join(inbox, "originals", "Comments.csv"))
          and not os.path.exists(os.path.join(inbox, "Comments.csv")))
    zipped = read("linkedin-comments-2.md")
    check("Comments.csv inside the archive ZIP is converted too",
          "## Comment, 2023-11-05" in zipped and "On the post: https://www.linkedin.com/feed/update/urn:li:activity:444" in zipped, zipped)
    check("a backslash-escaped quote and a newline come through",
          'He called it "the slow way", and\nhe was right.' in zipped, zipped)
    check("other CSVs in the archive are still left out", not any("onnections" in n for n in os.listdir(inbox)), os.listdir(inbox))
    check("the comments file isn't marked as a summary or ChatGPT", not loose.startswith("<!--") and not zipped.startswith("<!--"))

    # voiceprint leaves the ChatGPT file and the comments out of the person's corpus
    spec = importlib.util.spec_from_file_location("voiceprint", os.path.join(REPO, "scripts", "voiceprint.py"))
    vp = importlib.util.module_from_spec(spec); spec.loader.exec_module(vp)
    mat = os.path.join(t, "material"); os.makedirs(mat)
    open(os.path.join(mat, "mine.md"), "w").write(ESSAY)
    open(os.path.join(mat, "chatgpt.md"), "w").write(read("oaicite.md"))
    open(os.path.join(mat, "2026-10-27-linkedin-comments.md"), "w").write(loose)
    ids = [d["id"] for d in vp.load_texts(mat, label="mine", exclude=vp.DEFAULT_MINE_EXCLUDE, skip_marked=True)]
    check("voiceprint leaves the ChatGPT file and the comments out of the person's corpus", ids == ["mine.md"], ids)
    a = vp.argparse.Namespace(mine=mat, text_col=None, label_col=None, mine_where=None, mine_exclude=vp.DEFAULT_MINE_EXCLUDE,
                              others="", others_where=None, rewrites="")
    try:
        mine = vp.load_corpora(a)[0]
        check("voiceprint's default corpus does the same", [d["id"] for d in mine] == ["mine.md"], [d["id"] for d in mine])
    except SystemExit as e:
        check("voiceprint's default corpus does the same", False, str(e))

    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import studio_checks
    got = [os.path.basename(p) for p in studio_checks.corpus_files(mat)]
    check("studio_checks.corpus_files leaves out the ChatGPT file", "chatgpt.md" not in got, got)

print("all passed" if ok else "some failed")
sys.exit(0 if ok else 1)
