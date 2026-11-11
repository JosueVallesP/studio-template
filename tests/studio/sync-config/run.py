#!/usr/bin/env python3
"""Runs the sync-config test: scripts/sync-dashboard.py's config reader against a sample
config/tools.md. Keys with spaces (page id, api url, pieces database) must come back, a "not yet"
placeholder must read as unset, and both syncs must say why they stop when run by hand. Also the
proposal kinds and idea statuses the syncs map, and the Notion sync's compare-before-update.
Usage, from anywhere: python3 tests/studio/sync-config/run.py"""
import importlib.util, io, os, sys, contextlib, tempfile, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

SAMPLE = """# Tools

## Notion
- connected: yes
- route: token
- page id: 0123456789abcdef0123456789abcdef
- pieces database: aaaa
- home page: bbbb

## Dashboard
- connected: no
- app id: not yet (setup-dashboard fills this)
- api url: https://example.base44.app/api
"""

ok = bad = 0
def check(name, got, want):
    global ok, bad
    if got == want:
        ok += 1; print(f"ok   {name}")
    else:
        bad += 1; print(f"FAIL {name}: expected {want!r}, got {got!r}")

tmp = tempfile.mkdtemp()
try:
    os.makedirs(os.path.join(tmp, "scripts")); os.makedirs(os.path.join(tmp, "config"))
    for f in ("sync-dashboard.py", "sync-notion.py"):
        shutil.copy(os.path.join(REPO, "scripts", f), os.path.join(tmp, "scripts", f))
    open(os.path.join(tmp, "config", "tools.md"), "w").write(SAMPLE)
    os.environ.pop("NOTION_TOKEN", None); os.environ.pop("BASE44_API_KEY", None); os.environ.pop("STUDIO_QUIET", None)

    def load(name, file):
        spec = importlib.util.spec_from_file_location(name, os.path.join(tmp, "scripts", file))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
    sd = load("sd", "sync-dashboard.py")
    notion = sd.tools_section("Notion"); dash = sd.tools_section("Dashboard")
    check("page id", notion.get("page id"), "0123456789abcdef0123456789abcdef")
    check("pieces database", notion.get("pieces database"), "aaaa")
    check("home page", notion.get("home page"), "bbbb")
    check("connected", notion.get("connected"), "yes")
    check("api url", dash.get("api url"), "https://example.base44.app/api")
    check("not yet reads as unset", dash.get("app id"), "")
    check("entry fields still parse", sd.fields("status: ready\nwanted_now: yes\n"), {"status": "ready", "wanted_now": "yes"})

    check("kind: retire", sd.proposal_kind("kind: retire V2", ""), "retire")
    check("kind: seen", sd.proposal_kind("kind: seen", ""), "seen")
    check("kind: contradiction", sd.proposal_kind("kind: contradiction", ""), "contradiction")
    check("kind: change to P3", sd.proposal_kind("kind: change to P3", ""), "change")
    check("idea status kept", sd.idea_status("archived 2026-10-01"), "archived")
    check("idea status shaped", sd.idea_status("shaped"), "shaped")
    check("kind: inferred", sd.proposal_kind("kind: inferred", ""), "inferred")
    check("idea status unknown reads raw", sd.idea_status("<raw / ready>"), "raw")

    sn = load("sn", "sync-notion.py")
    check("notion same: unchanged", sn.same({"Name": {"type": "title", "title": [{"plain_text": "A"}]}}, {"Name": sn.title("A")}), True)
    check("notion same: changed", sn.same({"Name": {"type": "title", "title": [{"plain_text": "A"}]}}, {"Name": sn.title("B")}), False)
    for k in sd.KINDS: check(f"notion label for {k[1]}", k[1] in sn.PKIND, True)
    for label, mod in (("dashboard", sd), ("notion", sn)):
        err = io.StringIO(); sys.argv = ["x"]
        with contextlib.redirect_stderr(err): mod.main()
        check(f"{label} says why it stopped", bool(err.getvalue().strip()), True)
    os.environ["STUDIO_QUIET"] = "1"
    err = io.StringIO()
    with contextlib.redirect_stderr(err): sn.main()
    check("quiet under the stop hook", err.getvalue(), "")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

print(f"sync-config: {ok} ok, {bad} broken")
sys.exit(1 if bad else 0)
