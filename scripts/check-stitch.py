#!/usr/bin/env python3
"""Finds the person's sentences lifted into a draft word for word, so a post is written from what
they think instead of stitched from what they once said.

Usage: python3 scripts/check-stitch.py pieces/<id>/draft-vN.md [--sources <dir or file> ...]
                                        [--min-run 8] [--cap 2] [--json] [--draft A]

What it does:
  lifted runs      every run of --min-run or more consecutive words (default 8) that the post shares with
                   the person's sources: material/, inbox/ and canon/ by default (never the piece's own
                   folder, whose brief already quotes the material). Each run is reported with its file.
  declared         a lifted run inside a source-map row of kind `verbatim` is a quote on purpose and passes.
                   Any other lifted run fails: it's a `said again` line that kept the source's words, which
                   is stitching, not writing. Say it fresh, or mark it `verbatim` if the exact words are the
                   point (a coined term, a number, a line the piece is about).
  the cap          verbatim rows (minus those marked `supplied`) above --cap fail (2 for a post, 4 for an
                   essay: templates/piece/draft.md). Supplied copy never counts.
  the share        the share of the post's words that sit inside lifted runs, as a reading.

A draft file with Posts A, B and C is checked draft by draft; --draft A checks one. Exit 1 when a run is
undeclared or the cap is over, 0 otherwise. Reads only; never writes a file.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

WORD = re.compile(r"[a-z0-9]+(?:'[a-z]+)?")
DEFAULT_SOURCES = ("material", "inbox", "canon")
SOURCE_EXT = (".md", ".txt", ".csv", ".json", ".yaml", ".yml")


def words(text):
    return WORD.findall(text.lower().replace("’", "'"))


def find_root(path):
    d = os.path.dirname(os.path.abspath(path))
    while d != os.path.dirname(d):
        if os.path.isfile(os.path.join(d, "CLAUDE.md")):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


def source_files(paths, skip_dir):
    out = []
    for p in paths:
        if os.path.isfile(p):
            out.append(p)
        elif os.path.isdir(p):
            for base, _, files in os.walk(p):
                if skip_dir and os.path.abspath(base).startswith(skip_dir):
                    continue
                for f in files:
                    if f.endswith(SOURCE_EXT):
                        out.append(os.path.join(base, f))
    return out


def shingles(files, n):
    """shingle -> file it was first seen in."""
    seen = {}
    for f in files:
        try:
            ws = words(open(f, encoding="utf-8", errors="ignore").read())
        except OSError:
            continue
        for i in range(len(ws) - n + 1):
            seen.setdefault(" ".join(ws[i:i + n]), f)
    return seen


def lifted_runs(post, seen, n):
    """Runs of >= n consecutive words of the post present in the sources, as (words, file)."""
    ws = words(post)
    runs, i = [], 0
    while i <= len(ws) - n:
        key = " ".join(ws[i:i + n])
        f = seen.get(key)
        if not f:
            i += 1
            continue
        j = i + n
        while j < len(ws) and seen.get(" ".join(ws[j - n + 1:j + 1])) == f:
            j += 1
        runs.append((ws[i:j], f))
        i = j
    return runs, len(ws)


def source_map_rows(text):
    m = re.search(r"^## Source map\s*\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M)
    rows = []
    if not m:
        return rows
    for line in m.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Line or claim", "") or set(cells[0]) <= {"-"}:
            continue
        rows.append({"line": cells[0], "kind": cells[1].lower(), "note": cells[3].lower() if len(cells) > 3 else ""})
    return rows


def main():
    sc.per_draft(os.path.abspath(__file__))
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__); sys.exit(2)
    path = args[0]
    as_json = "--json" in args
    n = int(args[args.index("--min-run") + 1]) if "--min-run" in args else 8
    cap = int(args[args.index("--cap") + 1]) if "--cap" in args else 2
    root = find_root(path)
    piece_dir = os.path.dirname(os.path.abspath(path))
    if "--sources" in args:
        i = args.index("--sources") + 1
        srcs = []
        while i < len(args) and not args[i].startswith("--"):
            srcs.append(args[i]); i += 1
    else:
        srcs = [os.path.join(root, d) for d in DEFAULT_SOURCES]
    skip = None if "--sources" in args else piece_dir   # named sources are read as given
    text = open(path, encoding="utf-8").read()
    post = sc.post_section(text)
    if post is None:
        print(f"check-stitch: no ## Post section in {path}"); sys.exit(1)

    seen = shingles(source_files(srcs, skip), n)
    runs, total = lifted_runs(post, seen, n)
    rows = source_map_rows(text)
    declared = [words(r["line"]) for r in rows if r["kind"] == "verbatim"]
    counted = sum(1 for r in rows if r["kind"] == "verbatim" and "supplied" not in r["note"])

    fails, notes, found = [], [], []
    lifted_words = 0
    for run, f in runs:
        lifted_words += len(run)
        joined = " ".join(run)
        is_declared = any(" ".join(d) and (joined in " ".join(d) or " ".join(d) in joined) for d in declared)
        rel = os.path.relpath(f, root)
        found.append({"words": len(run), "text": joined, "file": rel, "declared": is_declared})
        if not is_declared:
            fails.append(f"lifted, not marked verbatim ({len(run)} words from {rel}): \"{joined}\". "
                         "Say it fresh in the person's register, or mark it verbatim if the exact words are the point.")
    if counted > cap:
        fails.append(f"{counted} verbatim rows; the cap is {cap}. Keep the ones where the exact words are the point and say the rest again.")
    share = (lifted_words / total) if total else 0.0
    notes.append(f"{len(runs)} lifted run(s); {share:.0%} of the post's words sit inside them; sources scanned: "
                 + ", ".join(os.path.relpath(s, root) for s in srcs if os.path.exists(s)))
    if not seen:
        notes.append("no source text found to compare against; nothing could be lifted")

    if as_json:
        print(json.dumps({"fails": fails, "notes": notes, "runs": found, "share": round(share, 3), "verbatim_rows": counted}, indent=2))
    else:
        for f in fails: print("FAIL " + f)
        for r in found:
            if r["declared"]: print(f"ok   quote on purpose ({r['words']} words, {r['file']}): \"{r['text']}\"")
        for m in notes: print("note " + m)
        print("check-stitch: " + ("fix" if fails else "pass"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
