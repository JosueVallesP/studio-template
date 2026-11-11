#!/usr/bin/env python3
"""Every quote in an open proposal must be the person's real words. Proposals of kind contradiction, seen
and inferred rest on quoted lines, and the person is asked to decide on them; a misremembered quote turns
into a decision about something they never said. tidy, /think and the librarian run this before they
file a proposal, and /status before it lists them.

Usage: python3 scripts/check-proposals.py [proposals.md] [--all]
  --all   check closed proposals too (default: only status: open)

A quote is text in quotation marks, 8 characters or more, in a proposal's `proposal:`, `evidence:` or
`question_for_the_person:` lines. It's found when it appears word for word (same comparison as the
map and check-mechanical.py) in the person's files: material/, inbox/ (and inbox/done/), canon/, bank/ (not the
swipe file: other people's posts) and pieces/. A private journal entry is never read. Exit 1 when any open proposal has a quote that isn't
found; the proposal is listed so whoever filed it can fix the quote or drop that line.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

READ = ("material", "inbox", "canon", "bank", "pieces")

def root_of():
    d = os.getcwd()
    for _ in range(6):
        if os.path.exists(os.path.join(d, "studio.manifest.yaml")): return d
        d = os.path.dirname(d)
    return os.getcwd()

def corpus(root):
    texts = []
    for top in READ:
        for base, dirs, fns in os.walk(os.path.join(root, top)):
            dirs[:] = [x for x in dirs if x != "swipe"]   # bank/swipe/: other people's posts, never the person's words
            for fn in fns:
                if fn.endswith((".md", ".txt", ".json", ".csv")) and fn != "swipe-file.md":
                    try:
                        texts.append(sc.norm_quote(open(os.path.join(base, fn), encoding="utf-8", errors="replace").read()))
                    except OSError:
                        pass
    return texts

def proposals(text):
    """(heading, status, quotes) for each ## proposal."""
    out = []
    for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M):
        head, body = m.group(1).strip(), m.group(2)
        st = re.search(r"^status:\s*(\w+)", body, flags=re.M)
        status = st.group(1).lower() if st else "open"
        quotes = []
        for field in re.finditer(r"^(?:proposal|evidence|question_for_the_person):.*?(?=^\w[\w_]*:|\Z)", body, flags=re.S | re.M):
            for a, b in sc.QUOTED.findall(field.group(0)):
                q = a or b
                if "<" not in q:
                    quotes.append(q)
        out.append((head, status, quotes))
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = root_of()
    path = args[0] if args else os.path.join(root, "proposals.md")
    if not os.path.exists(path):
        print("check-proposals: no proposals.md yet"); sys.exit(0)
    items = proposals(open(path, encoding="utf-8").read())
    texts = corpus(root)
    bad = 0
    for head, status, quotes in items:
        if status != "open" and "--all" not in sys.argv: continue
        missing = [q for q in quotes if not sc.quote_found('"' + q + '"', texts)]
        if missing:
            bad += 1
            print(f"  FAIL  {head}")
            for q in missing:
                print(f"        not in their files, word for word: \"{q[:80]}{'...' if len(q) > 80 else ''}\"")
    print(f"check-proposals: {len(items)} proposals, {bad} with a quote that isn't in their files")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
