#!/usr/bin/env python3
"""Pushes the state of the files to the person's dashboard app and reads back their decisions.

The files are the truth; the dashboard is the mirror (docs/dashboard-app.md is the contract).
Every role's last step runs this; a daily scheduled run catches anything missed.

  python3 scripts/sync-dashboard.py              push everything, read decisions back
  python3 scripts/sync-dashboard.py --dry-run    build the payloads and print counts, send nothing
  python3 scripts/sync-dashboard.py --dump       print the payloads as JSON (for tests)

Needs, in config/tools.md under "## Dashboard":
  - connected: yes
  - app id: <Base44 app id>
  - api url: <the app's API address from its API reference, e.g. https://<slug>.base44.app/api>
and the key in the environment or .env as BASE44_API_KEY (a Base44 personal access token with access to the app;
sent as a bearer token). Without those it exits 0 and prints nothing,
so /status stays the dashboard for a person who has none.

Decisions the person makes in the app (your_decision, your_answer) come back as lines in
pieces/_decisions.md and proposals.md, and the producer records them from there. The sync then
marks them taken and clears the fields. No file changes without the producer; see role-producer.
"""
import glob, json, os, re, sys, urllib.request, urllib.error
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
TODAY = date.today()

# ---------- small readers ----------
def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            if _: fm[k.strip()] = v.strip()
    return fm

def fields(block):
    """key: value lines in an entry block. A key may hold spaces (config/tools.md has `page id`,
    `api url`, `pieces database`); it comes back lowercased and stripped."""
    out = {}
    for line in block.splitlines():
        m = re.match(r"^([a-z_]+(?: [a-z_]+){0,3}):(?:\s+(.*))?$", line)
        if m: out[m.group(1).strip().lower()] = (m.group(2) or "").strip().strip('"')
    return out

def entries(text, id_re):
    """Split a bank or canon file into (id, title, block) by its ## / ### headings."""
    out = []
    for m in re.finditer(rf"^#{{2,3}} ({id_re})(?: · (.*))?\n(.*?)(?=^#{{2,3}} |\Z)", text, re.S | re.M):
        if "<" in (m.group(2) or ""): continue
        out.append((m.group(1), (m.group(2) or "").strip(), m.group(3)))
    return out

def tools_section(name):
    t = read("config/tools.md")
    m = re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    f = fields(re.sub(r"^- ", "", m.group(1), flags=re.M)) if m else {}
    # "not yet (setup-notion fills this)" is the build's placeholder for a value nobody has set.
    return {k: ("" if v.lower().startswith("not yet") else v) for k, v in f.items()}

def note(msg):
    """One line to stderr when a sync stops early for missing config. The stop hook sets STUDIO_QUIET
    and drops the output anyway; a person or Claude running the script by hand sees why nothing happened."""
    if not os.environ.get("STUDIO_QUIET"): print(msg, file=sys.stderr)

def env(key):
    """The environment first (Claude Code on the web keeps keys there; .env doesn't survive a cloud
    session), then .env."""
    if os.environ.get(key): return os.environ[key]
    for line in read(".env").splitlines():
        if line.startswith(key + "="): return line.split("=", 1)[1].strip().strip('"')
    return ""

def iso(d): return d.isoformat() if d else None

def hex_or_none(s):
    m = re.search(r"#[0-9A-Fa-f]{6}", s or "")
    return m.group(0) if m else None

# ---------- collect ----------
STAGES = ["idea", "candidate", "briefed", "brief_approved", "drafted", "reviewed", "revised", "designed", "shipped", "held", "killed", "blocked"]
WAITING = {"briefed": "you", "reviewed": "you", "blocked": "you", "candidate": "studio", "brief_approved": "studio", "drafted": "studio", "revised": "studio"}
LAYERS = {"stories": "stories", "values": "stories", "behaviors": "stories", "povs": "povs", "pov": "povs", "branches": "branches", "branch": "branches", "proof": "proof_and_vehicle", "vehicle": "proof_and_vehicle", "thesis": "povs"}
FORMATS = {"fmt-linkedin-post": "LinkedIn post", "fmt-substack-essay": "Substack essay", "fmt-newsletter": "Newsletter issue", "fmt-essay": "Essay", "fmt-carousel": "Carousel", "fmt-page": "Page", "fmt-email": "Email"}

def collect_pieces(repo_url):
    out = []
    for brief in sorted(glob.glob("pieces/*/brief.md")):
        folder = os.path.dirname(brief); pid = os.path.basename(folder)
        fm = frontmatter(read(brief))
        if not fm or "<" in fm.get("id", ""): continue
        stage = fm.get("status", "idea").replace("-", "_")
        if stage not in STAGES: stage = "blocked" if "block" in stage else "idea"
        one = re.search(r"## The one idea\n.*?\n\n(.+?)\n", read(brief), re.S)
        title = (one.group(1).strip() if one and "<" not in one.group(1) else pid)
        title = re.split(r"(?<=[.!?])\s", title, maxsplit=1)[0]
        reviews = sorted(glob.glob(f"{folder}/review-v*.md"))
        rv = frontmatter(read(reviews[-1])) if reviews else {}
        verdict = rv.get("verdict", "").split()[0] if rv.get("verdict") else None
        log = read(f"{folder}/log.md")
        shipped = None
        for row in re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \| producer \| (ship\w*)", log, re.M): shipped = row[0]
        sig = {"impressions": 0, "comments": 0, "reposts": 0, "replies": 0, "conversations": 0}; notes = []
        for row in re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \| \w+ \| signal \|[^|]*\| \"?(.*?)\"? \|", log, re.M):
            notes.append(row[1])
            for k in sig:
                m = re.search(rf"(\d+)\s+{k[:-1] if k != 'replies' else 'repl'}", row[1], re.I)
                if m: sig[k] += int(m.group(1))
        visual = sorted(glob.glob(f"{folder}/visual.*"))
        final = read(f"{folder}/final.md"); pub = re.search(r"https?://\S+", frontmatter(final).get("url", "") or frontmatter(final).get("published", ""))
        out.append({
            "piece_id": pid, "title": title[:200], "stage": stage, "waiting_on": WAITING.get(stage, "nobody"),
            "format": FORMATS.get(fm.get("format", ""), fm.get("format", "")), "channel": fm.get("channel", ""),
            "layer": LAYERS.get(fm.get("layer", "").lower().split()[0] if fm.get("layer") else "", "povs"),
            "segment": fm.get("segment", ""), "parent_id": fm.get("parent", "") if "<" not in fm.get("parent", "") else "",
            "sources": ", ".join(x for x in [fm.get("parent", ""), fm.get("sources", "")] if x and "<" not in x),
            "verdict": verdict if verdict in ("pass", "revise", "redo") else None,
            "has_visual": bool(visual), "visual_url": None, "folder_url": f"{repo_url}/tree/main/{folder}" if repo_url else None,
            "published_url": pub.group(0) if pub else None, "shipped_on": shipped,
            **sig, "signal_note": " / ".join(notes)[:500] or None,
            "idea_id": next((x for x in re.findall(r"\bI\d+\b", fm.get("sources", "") + fm.get("parent", ""))), None),
            "last_synced": datetime.now().isoformat(timespec="seconds"),
        })
    return out

def idea_status(v):
    """The idea bank status as written (raw, shaped, ready, used, archived, merged); a blank or a template's
    "<...>" reads as raw."""
    w = (v.split() or [""])[0].lower()
    return w if w in IDEA_STATUSES else "raw"

def collect_ideas():
    out = []
    for iid, title, block in entries(read("bank/ideas.md"), r"I\d+"):
        f = fields(block)
        raw = re.search(r"^raw: ?\|?\n?(.*?)(?=^\w+:|\Z)", block, re.S | re.M)
        out.append({"idea_id": iid, "title": title or iid, "status": idea_status(f.get("status", "")),
                    "type": f.get("type", "observation").lower().split()[0], "strength": f.get("strength", "maybe").split()[0],
                    "permission": f.get("permission", "anonymize").split()[0], "wanted_now": f.get("wanted_now", "").lower().startswith("yes"),
                    "source": f.get("source", ""), "who_said_it": f.get("who_said_it", ""), "links_to": f.get("links", f.get("links_to", "")),
                    "raw": (raw.group(1).strip() if raw else "")[:300], "captured": (re.search(r"\d{4}-\d{2}-\d{2}", f.get("date", "")) or [None])[0] if f.get("date") else None})
    return out

# The kinds in templates/proposals.md, in the order a heading is tested ("change to P3", "retire V2", ...).
KINDS = [("contradiction", "contradiction"), ("seen", "seen"), ("voice rule", "voice_rule"), ("definition", "definition"),
         ("inferred", "inferred"), ("retire", "retire"), ("change", "change")]
IDEA_STATUSES = ("raw", "shaped", "ready", "used", "archived", "merged")   # the idea bank's statuses, passed through as they are

def proposal_kind(heading, block):
    """The kind from the heading ("## <date> · kind: retire V2") or a kind: line in the block; "change" otherwise."""
    m = re.search(r"kind:\s*(.+)$", heading, re.I) or re.search(r"^kind:\s*(.+)$", block, re.I | re.M)
    text = (m.group(1) if m else heading).lower()
    return next((v for k, v in KINDS if text.startswith(k) or (not m and k in text)), "change")

def collect_proposals():
    out = []
    for m in re.finditer(r"^## (\d{4}-\d{2}-\d{2}) · (.+?)\n(.*?)(?=^## |\Z)", read("proposals.md"), re.S | re.M):
        if "<" in m.group(2): continue
        f = fields(m.group(3)); kind = proposal_kind(m.group(2), m.group(3))
        ev = re.findall(r"^\s+- (.*)$", m.group(3), re.M)
        pid = f"{m.group(1)}-{re.sub(r'[^a-z0-9]+', '-', m.group(2).lower())[:40]}"
        out.append({"proposal_id": pid, "title": (f.get("proposal") or m.group(2))[:200], "kind": kind, "evidence": "\n".join(ev)[:1000],
                    "question": f.get("question_for_the_person", ""), "status": "open" if f.get("status", "open").startswith("open") else "answered",
                    "proposed_on": m.group(1)})
    return out

KIND_BY_LETTER = {"T": "thesis", "V": "value", "A": "behavior", "P": "pov", "B": "branch", "X": "stop_list", "S": "story", "R": "proof", "O": "offer", "C": "cta", "G": "segment", "D": "desire", "W": "voice_rule"}
def collect_canon(pieces):
    out = []; used = {}
    for p in pieces:
        for cid in re.findall(r"\b[TVAPBXSROCGDW]\d*\b", p["sources"]): used.setdefault(cid, []).append(p["piece_id"])
    for row in re.findall(r"^\| ([TVAPBXSROCGDW]\d*) \| (.*?) \| (.*?) \| (.*?) \|", read("canon/canon-index.md"), re.M):
        cid, one, _, status = row
        if not one.strip() and not status.strip(): continue
        out.append({"entry_id": cid, "title": (one.strip() or cid)[:200], "kind": KIND_BY_LETTER[cid[0]], "status": (status.strip().split() or ["draft"])[0].lower(),
                    "used_in": ", ".join(used.get(cid, [])), "times_used": len(used.get(cid, [])), "last_touched": None})
    return out

def collect_settings(pieces, canon, proposals):
    intake = {}
    for line in read("config/intake.yaml").splitlines():
        m = re.match(r"^([a-z_]+):\s*\"?(.*?)\"?\s*$", line)
        if m and m.group(2) and m.group(2) != "[]": intake[m.group(1)] = m.group(2)
    outc = read("canon/strategy/outcomes.md"); want = re.search(r'^want: "(.*)"', outc, re.M); meas = re.search(r"^measured by: (.*)", outc, re.M)
    hours = re.search(r"hours a week when work is busy: (\d+)", outc)
    ba = read("canon/visual/brand-assets.md"); ds = read("canon/visual/design-system.md")
    colors = re.findall(r"#[0-9A-Fa-f]{6}", ds or ba)
    plan = read("canon/strategy/content-plan.md"); cad = re.search(r"(\d+)\s*(?:posts?|pieces?)\s*(?:a|per)\s*week", plan, re.I)
    sp = read("canon/setup-progress.md"); stage = re.search(r"^stage: (.*)", sp, re.M)
    channels = tools_section("Publishing").get("channels", "")
    return {"person_name": intake.get("name", frontmatter(sp).get("owner", "")), "what_they_do": intake.get("what_you_do", ""),
            "goal": want.group(1) if want else intake.get("goal", ""), "measured_by": (meas.group(1) if meas and "<" not in meas.group(1) else intake.get("measured_by", "")),
            "channels": channels, "hours_per_week": int(hours.group(1)) if hours else None,
            "primary_color": colors[0] if colors else None, "accent_color": colors[1] if len(colors) > 1 else None, "background_color": colors[2] if len(colors) > 2 else None,
            "font_heading": None, "font_body": None, "logo_url": None,
            "how_it_works": read("YOUR-STUDIO.md"), "plan_cadence_per_week": int(cad.group(1)) if cad else None,
            "next_step": (re.search(r"## (?:Your next step|Where you are in setup)\n\n(.*?)(?:\n\n|\Z)", read("YOUR-STUDIO.md"), re.S) or [None, ""])[1].strip() if stage else "",
            "last_synced": datetime.now().isoformat(timespec="seconds")}

def collect_weekly(pieces, ideas, canon, proposals, settings):
    monday = TODAY - timedelta(days=TODAY.weekday()); week = iso(monday)
    inweek = lambda d: d and d >= week
    shipped = sum(1 for p in pieces if inweek(p["shipped_on"]))
    captured = sum(1 for i in ideas if inweek(i["captured"]))
    plan = read("canon/strategy/content-plan.md"); im = re.search(r"input minimum[^\d]*(\d+)", plan, re.I)
    ready = sum(1 for i in ideas if i["status"] == "ready"); cad = settings.get("plan_cadence_per_week") or 0
    return [{"week": week, "shipped": shipped, "captured": captured, "input_minimum": int(im.group(1)) if im else None,
             "runway_weeks": round(ready / cad, 1) if cad else None, "confirmed_entries": sum(1 for c in canon if c["status"] == "confirmed"),
             "open_proposals": sum(1 for p in proposals if p["status"] == "open"),
             "waiting_on_you": sum(1 for p in pieces if p["waiting_on"] == "you") + sum(1 for p in proposals if p["status"] == "open"),
             "replies": sum(p["replies"] for p in pieces if inweek(p["shipped_on"])), "conversations": sum(p["conversations"] for p in pieces if inweek(p["shipped_on"]))}]

# ---------- the app's API ----------
class App:
    def __init__(self, url, key):
        self.url = url.rstrip("/"); self.key = key
    def call(self, method, path, body=None, params=""):
        req = urllib.request.Request(f"{self.url}{path}{params}", method=method, data=json.dumps(body).encode() if body is not None else None,
                                     headers={"Authorization": f"Bearer {self.key}", "api_key": self.key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read() or b"null")
        except urllib.error.HTTPError as e:
            raise SystemExit(f"dashboard: {method} {path} failed: {e.code} {e.read()[:300]!r}")
    def list(self, entity): return self.call("GET", f"/entities/{entity}", params="?limit=1000") or []
    def create(self, entity, rec): return self.call("POST", f"/entities/{entity}", rec)
    def update(self, entity, rid, rec): return self.call("PUT", f"/entities/{entity}/{rid}", rec)

def upsert(app, entity, key, records, dry):
    existing = {} if dry else {r.get(key): r for r in app.list(entity) if r.get(key)}
    made = changed = 0
    for rec in records:
        cur = existing.get(rec[key])
        if cur:
            keep = {k: cur[k] for k in PERSON_FIELDS.get(entity, []) if k in cur}   # never overwrite what the person owns
            payload = {**rec, **keep}
            if any(cur.get(k) != v for k, v in payload.items()):
                if not dry: app.update(entity, cur["id"], payload)
                changed += 1
        else:
            if not dry: app.create(entity, rec)
            made += 1
    return made, changed

PERSON_FIELDS = {"Piece": ["your_decision", "your_note", "published_url", "impressions", "comments", "reposts", "replies", "conversations", "signal_note"],
                 "Idea": ["your_note"], "Proposal": ["your_answer", "your_note"]}

def read_back(app, dry):
    """Decisions made in the app become lines the producer records; then the fields are cleared."""
    if dry: return 0
    n = 0; lines = []
    for p in app.list("Piece"):
        if p.get("your_decision") and not p.get("decision_taken"):
            lines.append(f"- {TODAY} · {p['piece_id']} · {p['your_decision'].replace('_', ' ')} · \"{p.get('your_note', '')}\"")
            app.update("Piece", p["id"], {"decision_taken": True, "your_decision": None, "your_note": None}); n += 1
    for pr in app.list("Proposal"):
        if pr.get("your_answer") and pr.get("status") == "open":
            lines.append(f"- {TODAY} · proposal {pr['proposal_id']} · {pr['your_answer'].replace('_', ' ')} · \"{pr.get('your_note', '')}\"")
            app.update("Proposal", pr["id"], {"your_answer": None, "your_note": None}); n += 1
    if lines:
        os.makedirs("pieces", exist_ok=True)
        p = "pieces/_decisions.md"
        head = "" if os.path.exists(p) else "# Decisions from the dashboard\n\nThe person decided these in the app. `role-producer` records each one (log line, status, next actor) and deletes the line. Nothing moves until it does.\n\n"
        open(p, "a", encoding="utf-8").write(head + "\n".join(lines) + "\n")
    return n

def main():
    dry = "--dry-run" in sys.argv; dump = "--dump" in sys.argv
    dash = tools_section("Dashboard"); key = env("BASE44_API_KEY")
    if not dump and not dry:
        if dash.get("connected", "no") != "yes": note("dashboard: not connected in config/tools.md (## Dashboard, connected: yes); nothing sent"); return
        if not (dash.get("api_url") or dash.get("api url")): note("dashboard: no api url in config/tools.md under ## Dashboard; nothing sent"); return
        if not key: note("dashboard: BASE44_API_KEY isn't set in the environment or .env; nothing sent"); return
    gh = tools_section("Repo").get("url", "")
    pieces = collect_pieces(gh); ideas = collect_ideas(); proposals = collect_proposals()
    canon = collect_canon(pieces); settings = collect_settings(pieces, canon, proposals); weekly = collect_weekly(pieces, ideas, canon, proposals, settings)
    if dump:
        print(json.dumps({"Piece": pieces, "Idea": ideas, "Proposal": proposals, "CanonEntry": canon, "StudioSettings": [settings], "WeeklyStat": weekly}, indent=2, default=str)); return
    app = None if dry else App(dash.get("api_url") or dash.get("api url"), key)
    out = []
    for entity, keyf, recs in [("Piece", "piece_id", pieces), ("Idea", "idea_id", ideas), ("Proposal", "proposal_id", proposals),
                               ("CanonEntry", "entry_id", canon), ("WeeklyStat", "week", weekly)]:
        made, changed = upsert(app, entity, keyf, recs, dry); out.append(f"{entity} {len(recs)} ({made} new, {changed} changed)")
    # settings: one record
    if not dry:
        cur = app.list("StudioSettings")
        if cur: app.update("StudioSettings", cur[0]["id"], settings)
        else: app.create("StudioSettings", settings)
    back = read_back(app, dry)
    print(("dashboard dry run: " if dry else "dashboard synced: ") + "; ".join(out) + (f"; {back} decision(s) read back" if back else ""))

if __name__ == "__main__":
    main()
