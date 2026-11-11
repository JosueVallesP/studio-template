import json, sys, os, re, subprocess
"""PostToolUse hook on Write and Edit. Two jobs:

1. A piece's draft (pieces/<id>/draft-vN.md): run check-mechanical (fails to fix), check-human (flags for the
   judge) and check-prose (the house rules: fails to fix, flags for the judge), voice-diff when the person
   has a corpus, and check-stitch (the person's sentences lifted word for word and not marked verbatim: fails).
2. Any other person-facing file the studio writes: check-prose in prose mode. That covers canon pages the studio
   drafts (about-you, readback, the manifesto, strategy files), the map's page (bank/map/findings.md;
   scripts/map-render.py builds it, and tests/studio/map holds it to the same rules), YOUR-STUDIO.md, proposals.md and every file under
   pieces/. The person's own words are never checked: material/, inbox/, journal/, bank/ (their idea bank, their
   rewrites), canon/bank/ (their stories and proof) and tests/ are skipped.

The detector is never called here (one paid call per piece, made by the judge).
"""
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
path = ((d.get("tool_input") or {}).get("file_path") or "").replace(os.sep, "/")
root = os.path.abspath(d.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or ".")
full = path if os.path.isabs(path) else os.path.join(root, path)
rel = os.path.relpath(full, root).replace(os.sep, "/")

SKIP = ("tests/", "material/", "inbox/", "journal/", "bank/", "canon/bank/", "skills/", "scripts/", "docs/", ".claude/", "templates/", "config/", "sessions/")
MAP_PAGE = "bank/map/findings.md"   # the map's page is the studio's prose about the person (its quotes are skipped by check-prose)
if not rel.endswith(".md") or (rel.startswith(SKIP) and rel != MAP_PAGE) or rel in ("CLAUDE.md", "README.md", "CHANGELOG.md", "studio-notes.md"):
    sys.exit(0)
is_draft = bool(re.search(r"(^|/)pieces/[^/]+/draft-v\d+\.md$", rel))
person_facing = is_draft or rel.startswith(("pieces/", "canon/")) or rel in ("YOUR-STUDIO.md", "proposals.md", MAP_PAGE)
if not person_facing:
    sys.exit(0)

def run(script, *extra):
    sp = os.path.join(root, script)
    if not os.path.exists(sp):
        return None
    try:
        r = subprocess.run([sys.executable, "-I", sp, full, *extra], capture_output=True, text=True, timeout=60, cwd=root)
        return (r.stdout + r.stderr).strip()
    except Exception as e:
        return f"{script}: could not run ({e})"

def clean(out, key, ok_word="none"):
    """True when every "<key>:" line in the output says ok_word. A draft file with Posts A, B and C
    prints one result per draft, so one clean draft mustn't hide flags on another."""
    lines = [l.strip() for l in (out or "").splitlines() if re.match(rf"\s*{key}\b", l)]
    return bool(lines) and all(l.startswith(f"{key}: {ok_word}") for l in lines)

parts = []
if is_draft:
    mech = run("scripts/check-mechanical.py")
    if mech and "FAIL" in mech:
        parts.append("check-mechanical found fails. Fix every fail before setting status: drafted.\n" + mech)
    human = run("scripts/check-human.py")
    if human and not clean(human, "flags"):
        parts.append("check-human's flags are evidence for the judge; not fails. Read them, and leave the verdict to the editor.\n" + human)
prose = run("scripts/check-prose.py", "--mode", "piece" if is_draft else "prose")
if prose and "FAILS" in prose:
    parts.append("check-prose found house-rule fails (skills/craft-house-rules). Fix every fail before this file is done; flags go to the judge.\n" + prose)
elif prose and not clean(prose, "flags"):
    parts.append("check-prose flags, for the judge:\n" + prose)
if is_draft:
    vd = run("scripts/voice-diff.py")
    if vd and not clean(vd, "drift") and "no corpus found" not in vd and "need 300" not in vd:
        parts.append("voice-diff: the draft has drifted from the person's own markers. Say it again closer to how they write.\n" + vd)
    brief = os.path.join(os.path.dirname(full), "brief.md")
    try:
        is_essay = "essay" in open(brief, encoding="utf-8").read().lower()   # the brief names the format skill
    except OSError:
        is_essay = False
    st = run("scripts/check-stitch.py", *(["--cap", "4"] if is_essay else []))
    if st and "FAIL" in st:
        parts.append("check-stitch: a line keeps the source's words without being marked verbatim (H34). Say it fresh in the person's register, or mark it verbatim if the exact words are the point.\n" + st)
if parts:
    msg = ("Checks on " + rel + " (run by the studio's hook; the detector is never called here):\n\n" + "\n\n".join(parts))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
sys.exit(0)
