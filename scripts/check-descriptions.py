#!/usr/bin/env python3
"""Two checks on every skill before it ships or zips. (1) The description fits the Claude app's limit for "Upload a skill" (1024 characters), so
make-skill-zips.sh never builds a zip the app turns away. Reads the frontmatter of skills/*/SKILL.md
and .claude/skills/*/SKILL.md, including folded descriptions (description: >-).

(2) No skill file holds a truncation placeholder ("[Rest of document continues...]", "[Full skill content
included]") where instructions should be: a skill cut off that way still shows in the list but does half
its job, and nobody notices until a run goes wrong. Every file under skills/ and .claude/skills/ is read.
Also checks that each file a SKILL.md names under its own folder (references/..., stages/...) exists, so
an upload that lost its reference files is caught before it ships.

Usage: python3 scripts/check-descriptions.py [--limit 1024]
Exit 1 when any description is over the limit or missing."""
import glob, os, re, sys

LIMIT = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 1024
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def description(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", t, flags=re.S)
    if not m: return None
    lines = m.group(1).split("\n")
    for i, line in enumerate(lines):
        d = re.match(r"description:\s*(.*)$", line)
        if not d: continue
        val = d.group(1).strip()
        if val in (">", ">-", "|", "|-", ">+", "|+"):
            parts = []
            for nxt in lines[i + 1:]:
                if nxt.strip() and not nxt.startswith((" ", "\t")): break
                parts.append(nxt.strip())
            return " ".join(p for p in parts if p)
        return val.strip("'\"")
    return None

bad = []
paths = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")) + glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "SKILL.md")))
for p in paths:
    rel = os.path.relpath(p, ROOT)
    d = description(p)
    if not d: bad.append(f"{rel}: no description in the frontmatter")
    elif len(d) > LIMIT: bad.append(f"{rel}: description is {len(d)} characters (limit {LIMIT})")
TRUNC = re.compile(r"\[(?:rest of (?:the )?(?:document|file|skill|steps)|full (?:skill )?content|content continues|remaining (?:steps|content|sections))[^\]\n]{0,80}\]|\.\.\. ?\(truncated\)|continues as in (?:the )?original", re.I)
for base in (os.path.join(ROOT, "skills"), os.path.join(ROOT, ".claude", "skills")):
    for d, _, fns in os.walk(base):
        for fn in fns:
            if not fn.endswith((".md", ".txt", ".json", ".yaml", ".yml")): continue
            fp = os.path.join(d, fn)
            try: t = open(fp, encoding="utf-8", errors="replace").read()
            except OSError: continue
            m = TRUNC.search(t)
            if m: bad.append(f"{os.path.relpath(fp, ROOT)}: looks cut off: \"{m.group(0)[:60]}\"")
for p in glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")):
    folder = os.path.dirname(p)
    t = open(p, encoding="utf-8").read()
    for ref in sorted(set(re.findall(r"`((?:references|stages|types|library|templates|interviews|assets|scripts)/[\w./-]+\.(?:md|py|json|csv|yaml|svg))`", t))):
        # a path relative to this skill, the repo, or another skill it names nearby ("skills/fmt-post-visual ... its library/...")
        if not os.path.exists(os.path.join(folder, ref)) and not os.path.exists(os.path.join(ROOT, ref)) and not glob.glob(os.path.join(ROOT, "skills", "*", ref)):
            bad.append(f"{os.path.relpath(p, ROOT)}: names {ref}, which isn't in its folder")
for b in bad: print("  FAIL  " + b)
print(f"check-descriptions: {len(paths)} skills, {len(bad)} problems (description length, cut-off text, missing reference files)")
sys.exit(1 if bad else 0)
