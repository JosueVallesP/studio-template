#!/usr/bin/env python3
"""Reads the rewrite pairs in bank/rewrites/ and their rule tags.

Each line under "## What changed" in a pair ends with a tag saying which rule the change touches:
  · rule: H19   the draft broke house rule H19 (skills/craft-house-rules)
  · rule: W4    the draft broke voice-guide rule W4
  · rule: new   a move the person made that no rule covers yet
  · rule: piece about this piece only (a fact, the argument, a call to action); no voice lesson
A pair is "open" while any line is tagged new or untagged: it still holds a lesson no rule records.
Once every new line has been retagged with the rule it became, the pair is "closed".

Usage, from the instance root:
  python3 scripts/rewrites.py pick --format fmt-linkedin-post [--n 10]
      The pairs the writer reads before a draft, in order: open pairs in the same format, newest first,
      then open pairs in other formats, then closed pairs in the same format, then the rest.
  python3 scripts/rewrites.py tally [--since YYYY-MM-DD] [--json]
      What the pairs written since the date (default today) say: how many changes broke a rule the
      reviews missed, how many broke a rule a review had named, how many are new, how many were about
      the piece only. Lists the missed ones.
Both take --root <dir> when not run from the instance root.
"""
import datetime, glob, json, os, re, sys

TAG_RE = re.compile(r"[·•|]\s*rule:\s*([HW]\d+|new|piece)\s*\.?\s*$", re.I)
RULE_RE = re.compile(r"^[HW]\d+$", re.I)


def arg(name, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return default


def frontmatter(text):
    out = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip()
    return out


def changes(text):
    m = re.search(r"^## What changed\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith(("- ", "* ")):
            continue
        t = TAG_RE.search(line)
        tag = t.group(1) if t else "untagged"
        tag = tag.upper() if RULE_RE.match(tag) else tag.lower()
        out.append({"text": line[2:].strip(), "tag": tag})
    return out


def load(root):
    pairs = []
    for path in glob.glob(os.path.join(root, "bank", "rewrites", "*.md")):
        if os.path.basename(path).lower().startswith("readme") or os.path.basename(path) == "rewrites-README.md":
            continue
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)
        name = os.path.basename(path)
        # A pair is named <yyyy-mm-dd>-<piece>.md or <piece id>.md; its piece: and date: lines win either way.
        dated = bool(re.match(r"^\d{4}-\d{2}-\d{2}-", name))
        date = fm.get("date") or (name[:10] if dated else "")
        lines = changes(text)
        is_open = (not lines) or any(c["tag"] in ("new", "untagged") for c in lines)
        pairs.append({"path": os.path.relpath(path, root), "piece": fm.get("piece") or (name[11:-3] if dated else name[:-3]),
                      "date": date, "format": fm.get("format", ""), "changes": lines, "open": is_open})
    pairs.sort(key=lambda p: (p["date"], p["path"]), reverse=True)
    return pairs


DEFAULT_DIR = os.path.join("skills", "setup-brand-tree", "templates", "bank-working", "rewrites-default")

def load_default(root):
    """The default pairs the studio ships, for a person with fewer than three of their own. Read only
    their What changed lines; never write like their right-hand side."""
    out = []
    for path in glob.glob(os.path.join(root, DEFAULT_DIR, "*.md")):
        if os.path.basename(path).lower().startswith("readme"): continue
        fm = frontmatter(open(path, encoding="utf-8").read())
        out.append({"path": os.path.relpath(path, root), "format": fm.get("format", ""), "date": fm.get("date", ""), "open": False, "default": True})
    return sorted(out, key=lambda p: p["path"])

def pick(root):
    fmt = arg("--format", "")
    n = int(arg("--n", "10"))
    pairs = load(root)
    if len(pairs) < 3:
        defaults = load_default(root)
        if defaults:
            # Only pairs of the piece's own format: a studio-message pair never goes to a post or an essay.
            same_d = [p for p in defaults if fmt and p["format"] == fmt]
            for p in pairs: print(f"{p['path']}\tthe person's own, open")
            for p in same_d[:max(0, n - len(pairs))]: print(f"{p['path']}\tdefault pair: read only its What changed lines; never write like its right-hand side")
            if pairs or same_d: return
    if not pairs:
        print("no rewrite pairs yet")
        return
    same = lambda p: fmt and p["format"] == fmt
    order = ([p for p in pairs if p["open"] and same(p)] + [p for p in pairs if p["open"] and not same(p)] +
             [p for p in pairs if not p["open"] and same(p)] + [p for p in pairs if not p["open"] and not same(p)])
    for p in order[:n]:
        label = ("same format" if same(p) else "other format") + (", open" if p["open"] else ", closed")
        print(f"{p['path']}\t{label}")


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


def reviews_name(root, piece, rule):
    rx = re.compile(rf"\b{re.escape(rule)}\b")
    for path in glob.glob(os.path.join(root, "pieces", piece, "review-*.md")):
        if rx.search(open(path, encoding="utf-8").read()):
            return True
    return False


def tally(root):
    since = arg("--since", datetime.date.today().isoformat())
    pairs = [p for p in load(root) if p["date"] >= since]
    counts = {"missed": 0, "flagged": 0, "new": 0, "piece": 0, "untagged": 0}
    missed = []
    for p in pairs:
        for c in p["changes"]:
            if RULE_RE.match(c["tag"]):
                if reviews_name(root, p["piece"], c["tag"]):
                    counts["flagged"] += 1
                else:
                    counts["missed"] += 1
                    missed.append({"piece": p["piece"], "rule": c["tag"], "change": c["text"], "pair": p["path"]})
            else:
                counts[c["tag"]] += 1
    total = sum(counts.values())
    if "--json" in sys.argv:
        print(json.dumps({"since": since, "pairs": len(pairs), "changes": total, **counts, "missed_lines": missed}, indent=2))
        return
    if not pairs:
        print(f"No rewrites since {since}.")
        return
    parts = []
    if counts["missed"]: parts.append(f"{counts['missed']} broke a rule the reviews missed")
    if counts["flagged"]: parts.append(f"{counts['flagged']} broke a rule a review had named")
    if counts["new"]: parts.append(f"{counts['new']} {'is' if counts['new'] == 1 else 'are'} new")
    if counts["piece"]: parts.append(f"{counts['piece']} {'was' if counts['piece'] == 1 else 'were'} about the piece only")
    if counts["untagged"]: parts.append(f"{counts['untagged']} {'has' if counts['untagged'] == 1 else 'have'} no tag yet")
    print(f"{plural(len(pairs), 'rewrite', 'rewrites')}, {plural(total, 'change', 'changes')}: " + ", ".join(parts) + ".")
    for m in missed:
        print(f"  missed {m['rule']} in {m['piece']}: {m['change']}")


def main():
    root = arg("--root", os.getcwd())
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "pick":
        pick(root)
    elif cmd == "tally":
        tally(root)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
