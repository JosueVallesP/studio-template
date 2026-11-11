#!/usr/bin/env python3
"""What still rests on a canon entry: the open pieces that cite it, and whether the core summary names it.
The producer runs it when the person accepts a proposal that changes or retires an entry, so nothing in
progress keeps leaning on a belief, story or rule the person has changed or dropped.

Usage: python3 scripts/cites.py <ID> [<ID> ...] [--json]
       python3 scripts/cites.py P3 W12

An open piece is any folder in pieces/ whose brief.md status isn't shipped or killed. Its brief.md and
every draft-*.md are read for the ID standing alone (P3, not P31 or "P3" inside a quote of a file path).
canon/core-summary.md is listed when it names the ID, since every job reads it and it was written once.
Reads only; writes nothing. Exit 0 always (a list is the answer, not a pass or fail).
"""
import glob, json, os, re, sys

CLOSED = {"shipped", "killed"}

def root_of():
    d = os.getcwd()
    for _ in range(6):
        if os.path.exists(os.path.join(d, "studio.manifest.yaml")): return d
        d = os.path.dirname(d)
    return os.getcwd()

def status_of(brief):
    m = re.search(r"^status:\s*([A-Za-z\-]+)", brief, flags=re.M)
    return m.group(1).lower() if m else ""

def cites(text, idv):
    return re.search(rf"(?<![\w/.\-]){re.escape(idv)}(?![\w/])", text) is not None

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__.strip().split("\n\n")[1]); sys.exit(0)
    root = root_of()
    summary_path = os.path.join(root, "canon", "core-summary.md")
    summary = open(summary_path, encoding="utf-8").read() if os.path.exists(summary_path) else ""
    out = {}
    for idv in args:
        hits = []
        for folder in sorted(glob.glob(os.path.join(root, "pieces", "*", ""))):
            brief_p = os.path.join(folder, "brief.md")
            if not os.path.exists(brief_p): continue
            brief = open(brief_p, encoding="utf-8").read()
            st = status_of(brief)
            if st in CLOSED: continue
            files = [os.path.relpath(brief_p, root)] if cites(brief, idv) else []
            for dp in sorted(glob.glob(os.path.join(folder, "draft-*.md"))):
                if cites(open(dp, encoding="utf-8").read(), idv):
                    files.append(os.path.relpath(dp, root))
            if files:
                hits.append({"piece": os.path.basename(os.path.dirname(folder)), "status": st, "files": files})
        out[idv] = {"open_pieces": hits, "core_summary": bool(summary) and cites(summary, idv)}
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2)); return
    for idv, r in out.items():
        if not r["open_pieces"] and not r["core_summary"]:
            print(f"{idv}: nothing open cites it"); continue
        print(f"{idv}:")
        for h in r["open_pieces"]:
            print(f"  - {h['piece']} ({h['status']}): {', '.join(h['files'])}")
        if r["core_summary"]:
            print("  - canon/core-summary.md names it: rewrite that line too")

if __name__ == "__main__":
    main()
