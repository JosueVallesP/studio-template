#!/usr/bin/env python3
"""Builds the writer's packet: the one file the writer reads at the moment of writing, instead of the
whole repo. Written to pieces/<id>/packet.md and printed with a word count.

Usage: python3 scripts/packet.py pieces/<id> [--samples 6] [--sample-words 700] [--quiet]

What goes in, in order:
  the writer's sheet        skills/craft-house-rules/writer-sheet.md, whole
  the brief                 the one idea, the reader, purpose, material (with sources), not saying, outcome,
                            open questions and the format plan; the frontmatter is kept for the format and path
  the cards the plan picked the hook move, the shape, the inside moves and the close named in the format plan,
                            cut out of the format's library files by their headers; never the whole library
  the type's draft step     when the plan names a TYPE: that type file from its "Draft" step up to the judge's checks
  the voice                 the rewrite pairs scripts/rewrites.py picks, the voice guide when it exists, and five to
                            eight of the person's own pieces from material/ (the same kind first), each cut at
                            --sample-words so the packet stays readable

Facts the brief cites by file aren't copied in whole: the brief's material lines carry the quoted words, and the
writer reads a cited file only for a fact the brief names. Copying source files into the packet is how lines get
lifted. The packet never holds the judge's checks.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
BRIEF_SECTIONS = ["The one idea", "Fractal shape", "The reader", "Purpose", "Material", "Outcome", "Not saying",
                  "Call to action", "Open questions", "Format plan"]
CARD_HEAD = re.compile(r"^## ([A-Z]{0,2}\d+)\. (.+?)\s*$", re.M)
KIND_WORDS = {"fmt-linkedin-post": ("post", "linkedin"), "fmt-substack-essay": ("essay", "substack", "newsletter")}


def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except OSError:
        return ""


def words(s):
    return len(re.findall(r"\S+", s))


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M)
    return m.group(1).strip() if m else ""


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, flags=re.S)
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), flags=re.M)) if m else {}


def cards(library_dir, plan):
    """Every card in the format's library files whose code or name the plan mentions."""
    plan_l = plan.lower()
    plan_codes = set(re.findall(r"\b([A-Z]{0,2}\d+)\b", plan))
    out = []
    for fn in sorted(os.listdir(library_dir)) if os.path.isdir(library_dir) else []:
        if not fn.endswith(".md"):
            continue
        text = read(os.path.join(library_dir, fn))
        heads = list(CARD_HEAD.finditer(text))
        for i, m in enumerate(heads):
            code, name = m.group(1), m.group(2)
            key = re.sub(r"^the ", "", name.lower()).strip()
            by_name = len(key) > 3 and re.search(rf"\b{re.escape(key)}\b", plan_l) is not None
            hit = code in plan_codes or by_name
            if code.isdigit():   # a hook move: match "HOOK MOVE 13" or the name, not a stray number
                hit = bool(re.search(rf"HOOK MOVE\s+{code}\b|MOVE\s+{code}\b", plan)) or by_name
            if hit:
                nxt = re.compile(r"^#{1,3} ", re.M).search(text, m.end())
                end = nxt.start() if nxt else len(text)
                out.append(text[m.start():end].rstrip())
    return out


def type_draft_step(format_skill, plan):
    m = re.search(r"^TYPE\s+(.+)$", plan, flags=re.M)
    if not m or m.group(1).strip().lower().startswith("none"):
        return ""
    slug = re.sub(r"[^a-z]+", "-", m.group(1).split(",")[0].split("(")[0].strip().lower()).strip("-")
    p = os.path.join(ROOT, "skills", format_skill, "types", slug + ".md")
    text = read(p)
    if not text:
        return ""
    start = re.search(r"^## Step \d+\. [^\n]*Draft[^\n]*$", text, flags=re.M)
    stop = re.search(r"^## Checks the judge adds", text, flags=re.M)
    if not start:
        return ""
    return f"### From `skills/{format_skill}/types/{slug}.md`\n\n" + text[start.start(): stop.start() if stop else len(text)].rstrip()


def rewrite_pairs(format_skill):
    r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "rewrites.py"), "pick", "--format", format_skill],
                       capture_output=True, text=True, cwd=ROOT)
    out = []
    for line in r.stdout.splitlines():
        path = line.split("\t")[0].strip()
        note = line.split("\t")[1].strip() if "\t" in line else ""
        full = path if os.path.isabs(path) else os.path.join(ROOT, path)
        text = read(full)
        if text:
            out.append(f"### `{path}`" + (f" ({note})" if note else "") + "\n\n" + text.strip())
    return out


def samples(format_skill, n, cap):
    mat = os.path.join(ROOT, "material")
    if not os.path.isdir(mat):
        return []
    kind = KIND_WORDS.get(format_skill, ())
    files = []
    for base, _, fns in os.walk(mat):
        for fn in fns:
            if fn.endswith((".md", ".txt")):
                files.append(os.path.join(base, fn))
    files.sort(reverse=True)   # newest by name first

    def same_kind(p):
        head = "\n".join(read(p).splitlines()[:3]).lower()
        return any(k in head for k in kind)
    picked = [p for p in files if same_kind(p)] + [p for p in files if not same_kind(p)]
    out = []
    for p in picked[:n]:
        text = read(p).strip()
        ws = text.split()
        if len(ws) > cap:
            text = " ".join(ws[:cap]) + "\n\n[cut here; the file goes on]"
        out.append(f"### `{os.path.relpath(p, ROOT)}`\n\n" + text)
    return out


def held_before():
    """Views the person told the studio they no longer hold (the map's `held before` claims), so the writer
    never states one as what they think now. Each as the claim, its date and reason, and the lines it was said in."""
    try:
        m = json.load(open(os.path.join(ROOT, "bank", "map", "map.json"), encoding="utf-8"))
    except Exception:
        return []
    out = []
    for n in m.get("nodes", []):
        if n.get("type") == "claim" and n.get("status") == "held before":
            qs = [v.get("quote") for v in n.get("versions") or [] if v.get("quote")][:2]
            out.append(f"- {n.get('text')} ({n.get('dropped', 'no longer held')})" + "".join(f'\n  - said before: "{q}"' for q in qs))
    return out

def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__); sys.exit(2)
    piece = args[0].rstrip("/")
    piece_abs = piece if os.path.isabs(piece) else os.path.join(ROOT, piece)
    n = int(args[args.index("--samples") + 1]) if "--samples" in args else 6
    cap = int(args[args.index("--sample-words") + 1]) if "--sample-words" in args else 700
    brief = read(os.path.join(piece_abs, "brief.md"))
    if not brief:
        print(f"packet: no brief.md in {piece}"); sys.exit(1)
    fm = frontmatter(brief)
    format_skill = fm.get("format", "fmt-linkedin-post").strip("<> ")
    plan = section(brief, "Format plan")

    parts = []
    parts.append(read(os.path.join(ROOT, "skills", "craft-house-rules", "writer-sheet.md")).strip())
    kept = "\n".join(f"{k}: {v}" for k, v in fm.items() if k in ("id", "format", "channel", "path", "thinks_out_loud", "adapted_from", "kind"))
    body = "\n\n".join(f"## {name}\n\n{section(brief, name)}" for name in BRIEF_SECTIONS if section(brief, name))
    parts.append("# The brief\n\n```\n" + kept + "\n```\n\n" + body)
    cs = cards(os.path.join(ROOT, "skills", format_skill, "library"), plan)
    if format_skill == "fmt-substack-essay":   # essays take their inside moves and closes from the LinkedIn library
        cs += cards(os.path.join(ROOT, "skills", "fmt-linkedin-post", "library"), plan)
    parts.append("# The cards the plan picked\n\n" + ("\n\n".join(cs) if cs else "(no card codes or names found in the format plan; read the plan's own lines)"))
    t = type_draft_step(format_skill, plan)
    if t:
        parts.append("# The type's draft step\n\n" + t)
    voice = []
    pairs = rewrite_pairs(format_skill)
    voice.append("## Rewrite pairs\n\n" + ("\n\n".join(pairs) if pairs else "(none yet)"))
    guide = read(os.path.join(ROOT, "canon", "voice", "voice-guide.md")).strip()
    voice.append("## Voice guide\n\n" + (guide if guide else "(none yet; the pieces below are the voice)"))
    ss = samples(format_skill, n, cap)
    voice.append("## The person's own pieces\n\n" + ("\n\n".join(ss) if ss else "(no material yet; write plain)"))
    parts.append("# The voice\n\n" + "\n\n".join(voice))
    voice_part = parts[-1]
    held = held_before()
    if held:
        parts.append("# Views they no longer hold\n\nThey told the studio they've moved on from these. Never state one as what they think now; "
                     "a line that says it as theirs fails the mechanical check. Their old words below may still show up in the pieces above.\n\n" + "\n".join(held))

    packet = "\n\n---\n\n".join(parts) + "\n"
    out = os.path.join(piece_abs, "packet.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(packet)
    if "--quiet" not in args:
        print(f"packet: {os.path.relpath(out, ROOT)} ({words(packet)} words: sheet {words(parts[0])}, brief {words(parts[1])}, "
              f"cards {words(parts[2])}, type {words(t)}, voice {words(voice_part)}{f", views no longer held {len(held)}" if held else ""})")


if __name__ == "__main__":
    main()
