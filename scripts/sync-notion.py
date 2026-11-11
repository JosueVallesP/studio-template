#!/usr/bin/env python3
"""Mirrors the files to the person's Notion dashboard (a duplicate of the master template) and reads
their decisions back. Same data as scripts/sync-dashboard.py; this is the Notion half.

  python3 scripts/sync-notion.py              push everything, read decisions back
  python3 scripts/sync-notion.py --dry-run    build the payloads and print counts, send nothing
  python3 scripts/sync-notion.py --discover   find the five databases under the shared page and write their IDs
  python3 scripts/sync-notion.py --dump       print what it would write, in the shape the Notion connector in Claude
                                              takes, for a studio that connects Notion through Claude instead of a token

Needs, in config/tools.md under "## Notion":
  - connected: yes
  - page id: <the duplicated "Content Studio" page the integration was shared with>
  - pieces database / ideas database / proposals database / canon index database / weekly database: <ids>
    (written by --discover)
  - home page: <the Home page id>   (optional; the five callouts get rewritten)
and NOTION_TOKEN in the environment or .env (an internal integration token). Without those it exits 0
and prints nothing.

The files are the truth. Every property the person doesn't own is overwritten. Decisions they make in
Notion (Your decision, Your answer) come back as lines in pieces/_decisions.md for the producer, then
the fields are cleared. Names here are the as-built names in docs/notion-template.md.
"""
import importlib.util, json, os, re, sys, urllib.request, urllib.error
from datetime import date, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
spec = importlib.util.spec_from_file_location("sd", os.path.join(ROOT, "scripts", "sync-dashboard.py"))
sd = importlib.util.module_from_spec(spec); spec.loader.exec_module(sd)

API = "https://api.notion.com/v1"
TITLE = {"Piece": "Name", "Idea": "Name", "Proposal": "Name", "CanonEntry": "Name", "WeeklyStat": "Week"}
DB_KEYS = {"Piece": "pieces database", "Idea": "ideas database", "Proposal": "proposals database", "CanonEntry": "canon index database", "WeeklyStat": "weekly database"}
DB_TITLES = {"Pieces": "Piece", "Ideas": "Idea", "Proposals": "Proposal", "Canon index": "CanonEntry", "Weekly": "WeeklyStat"}
STAGE = {"idea": "Idea", "candidate": "Candidate", "briefed": "Briefed", "brief_approved": "Brief approved", "drafted": "Drafted", "reviewed": "Reviewed",
         "revised": "Revised", "designed": "Designed", "shipped": "Shipped", "held": "Held", "killed": "Killed", "blocked": "Blocked"}
LAYER = {"stories": "Stories", "povs": "POVs", "branches": "Branches", "proof_and_vehicle": "Proof and vehicle"}
DECISION = {"Approve the brief": "approve brief", "Change the brief": "change brief", "Kill it": "kill", "Ship it": "ship", "Send it back": "revise", "Hold it": "hold"}
KIND = {"thesis": "Thesis", "value": "Value", "behavior": "Behavior", "pov": "POV", "branch": "Branch", "stop_list": "Stop list", "story": "Story", "proof": "Proof",
        "offer": "Offer", "cta": "CTA", "segment": "Segment", "desire": "Desire", "voice_rule": "Voice rule"}
TREE = {"Value": "Roots", "Behavior": "Roots", "POV": "Roots", "Thesis": "Trunk", "Branch": "Branches", "Offer": "Vehicle", "CTA": "Vehicle", "Segment": "Vehicle", "Desire": "Vehicle"}
PKIND = {"change": "Change to an entry", "retire": "Retire an entry", "contradiction": "Contradiction", "seen": "Seen", "voice_rule": "Voice rule", "definition": "Definition", "inferred": "Inferred"}
PERSON = {"Piece": ["Your decision", "Your note", "Published", "Impressions", "Comments", "Reposts", "Replies", "Conversations", "Signal note"], "Idea": ["Your note"], "Proposal": ["Your answer", "Your note"]}

# ---------- Notion property builders ----------
def t(s): return {"rich_text": [{"text": {"content": str(s)[:2000]}}] if s else []}
def title(s): return {"title": [{"text": {"content": str(s)[:2000]}}]}
def sel(s): return {"select": {"name": s} if s else None}
def status(s): return {"status": {"name": s}}
def num(n): return {"number": n if n is not None else None}
def chk(b): return {"checkbox": bool(b)}
def dt(d): return {"date": {"start": d} if d else None}
def url(u): return {"url": u or None}

def to_props(entity, r):
    if entity == "Piece":
        return {"Name": title(r["title"]), "ID": t(r["piece_id"]), "Stage": status(STAGE[r["stage"]]), "Format": sel(r["format"] or None), "Channel": sel(channel(r["channel"])),
                "Layer": sel(LAYER[r["layer"]]), "Parent": t(r.get("parent_id", "")), "Segment": t(r["segment"]), "Sources": t(r["sources"]),
                "Verdict": sel(cap(r["verdict"])), "Has visual": chk(r["has_visual"]), "Folder": url(r["folder_url"]), "Shipped on": dt(r["shipped_on"]),
                "Decision taken": chk(False), "Last synced": {"date": {"start": datetime.now().isoformat(timespec="seconds")}}}
    if entity == "Idea":
        return {"Name": title(r["title"]), "ID": t(r["idea_id"]), "Status": sel(cap(r["status"])), "Type": sel("POV" if r["type"] == "pov" else cap(r["type"])),
                "Strength": sel(cap(r["strength"])), "Permission": sel(cap(r["permission"])), "Wanted now": chk(r["wanted_now"]), "Source": t(r["source"]),
                "Who said it": t(r["who_said_it"]), "Links to": t(r["links_to"]), "Raw": t(r["raw"]), "Captured": dt(r["captured"])}
    if entity == "Proposal":
        return {"Name": title(r["title"]), "ID": t(r["proposal_id"]), "Kind": sel(PKIND[r["kind"]]), "Evidence": t(r["evidence"]), "Question": t(r["question"]),
                "Status": sel(cap(r["status"])), "Proposed on": dt(r["proposed_on"])}
    if entity == "CanonEntry":
        k = KIND[r["kind"]]
        return {"Name": title(r["title"]), "ID": t(r["entry_id"]), "Kind": sel(k), "Tree layer": sel(TREE.get(k, "Around the tree")), "Status": sel(cap(r["status"])),
                "Used in": t(r["used_in"]), "Times used": num(r["times_used"]), "Last touched": dt(r["last_touched"])}
    if entity == "WeeklyStat":
        return {"Week": title(r["week"]), "Week of": dt(r["week"]), "Shipped": num(r["shipped"]), "Plan cadence": num(r.get("plan_cadence")), "Captured": num(r["captured"]),
                "Input minimum": num(r["input_minimum"]), "Runway weeks": num(r["runway_weeks"]), "Confirmed entries": num(r["confirmed_entries"]),
                "Open proposals": num(r["open_proposals"]), "Waiting on you": num(r["waiting_on_you"]), "Replies": num(r["replies"]), "Conversations": num(r["conversations"])}

CHANNEL = {"linkedin": "LinkedIn", "newsletter": "Newsletter", "substack": "Newsletter", "site": "Site", "youtube": "YouTube", "podcast": "Podcast"}
def cap(s): return (s[0].upper() + s[1:]) if s else None
def channel(s): return CHANNEL.get((s or "").lower(), cap(s))

# ---------- Notion API ----------
class Notion:
    def __init__(self, token): self.token = token
    def call(self, method, path, body=None):
        req = urllib.request.Request(f"{API}{path}", method=method, data=json.dumps(body).encode() if body is not None else None,
                                     headers={"Authorization": f"Bearer {self.token}", "Notion-Version": "2025-09-03", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise SystemExit(f"notion: {method} {path} failed: {e.code} {e.read()[:300]!r}")
    def data_source(self, database_id):
        db = self.call("GET", f"/databases/{database_id}")
        return db["data_sources"][0]["id"] if db.get("data_sources") else database_id
    def rows(self, ds):
        out, cursor = [], None
        while True:
            body = {"page_size": 100, **({"start_cursor": cursor} if cursor else {})}
            res = self.call("POST", f"/data_sources/{ds}/query", body)
            out += res["results"]
            if not res.get("has_more"): return out
            cursor = res["next_cursor"]
    def create(self, ds, props): return self.call("POST", "/pages", {"parent": {"type": "data_source_id", "data_source_id": ds}, "properties": props})
    def update(self, page_id, props): return self.call("PATCH", f"/pages/{page_id}", {"properties": props})
    def children(self, block_id): return self.call("GET", f"/blocks/{block_id}/children?page_size=100")["results"]

def plain(prop):
    if not prop: return ""
    k = prop["type"]
    if k in ("rich_text", "title"): return "".join(x["plain_text"] for x in prop[k])
    if k == "select": return (prop["select"] or {}).get("name", "")
    if k == "status": return (prop["status"] or {}).get("name", "")
    if k == "checkbox": return prop["checkbox"]
    return ""

def value_of(prop):
    """A property as a plain value, from either side: what the sync builds, or what Notion returns."""
    if not prop: return None
    k = prop.get("type") or next(iter(prop))
    v = prop.get(k)
    if k in ("title", "rich_text"):
        return "".join((x.get("plain_text") or (x.get("text") or {}).get("content", "")) for x in (v or [])) or None
    if k in ("select", "status"): return (v or {}).get("name")
    if k == "date": return ((v or {}).get("start") or "")[:10] or None
    if k == "number": return None if v is None else float(v)
    if k == "checkbox": return bool(v)
    return v

def same(current, props):
    return all(value_of(current.get(k)) == value_of(v) for k, v in props.items())

def upsert(n, ds, entity, records, dry):
    existing = {} if dry else {plain(p["properties"].get("ID") or p["properties"].get("Week")): p for p in n.rows(ds)}
    made = changed = 0
    key = "week" if entity == "WeeklyStat" else {"Piece": "piece_id", "Idea": "idea_id", "Proposal": "proposal_id", "CanonEntry": "entry_id"}[entity]
    for r in records:
        props = to_props(entity, r)
        cur = existing.get(r[key])
        if cur:
            for k in PERSON.get(entity, []): props.pop(k, None)       # never overwrite what the person owns
            props.pop("Last synced", None)                           # a timestamp alone isn't a change
            if entity == "Piece": props.pop("Decision taken", None)
            if same(cur["properties"], props): continue              # compare before updating, as sync-dashboard's upsert does
            if entity == "Piece": props["Last synced"] = {"date": {"start": datetime.now().isoformat(timespec="seconds")}}
            if not dry: n.update(cur["id"], props)
            changed += 1
        else:
            if not dry: n.create(ds, props)
            made += 1
    return made, changed

def read_back(n, ds_pieces, ds_props, dry):
    if dry: return 0
    lines = []
    for p in n.rows(ds_pieces):
        pr = p["properties"]
        if plain(pr.get("Your decision")) and not plain(pr.get("Decision taken")):
            lines.append(f"- {date.today()} · {plain(pr['ID'])} · {DECISION.get(plain(pr['Your decision']), plain(pr['Your decision']))} · \"{plain(pr.get('Your note'))}\"")
            n.update(p["id"], {"Decision taken": chk(True), "Your decision": {"select": None}, "Your note": t("")})
    for p in n.rows(ds_props):
        pr = p["properties"]
        if plain(pr.get("Your answer")) and plain(pr.get("Status")) == "Open":
            lines.append(f"- {date.today()} · proposal {plain(pr['ID'])} · {plain(pr['Your answer']).lower()} · \"{plain(pr.get('Your note'))}\"")
            n.update(p["id"], {"Your answer": {"select": None}, "Your note": t("")})
    if lines:
        os.makedirs("pieces", exist_ok=True); path = "pieces/_decisions.md"
        head = "" if os.path.exists(path) else "# Decisions from the dashboard\n\nThe person decided these in the dashboard. `role-producer` records each one (log line, status, next actor) and deletes the line. Nothing moves until it does.\n\n"
        open(path, "a", encoding="utf-8").write(head + "\n".join(lines) + "\n")
    return len(lines)

def discover(n, page_id):
    found = {}
    for b in n.children(page_id):
        if b["type"] == "child_database" and b["child_database"]["title"] in DB_TITLES:
            found[DB_KEYS[DB_TITLES[b["child_database"]["title"]]]] = b["id"].replace("-", "")
        if b["type"] == "child_page" and b["child_page"]["title"] == "Home":
            found["home page"] = b["id"].replace("-", "")
    missing = [k for k in DB_KEYS.values() if k not in found]
    if missing: raise SystemExit(f"notion: under that page I found {sorted(found)} but not {missing}. Is it a duplicate of the master, shared with the integration?")
    tools = open("config/tools.md", encoding="utf-8").read()
    for k, v in found.items():
        tools = re.sub(rf"^- {k}:.*$", f"- {k}: {v}", tools, flags=re.M) if re.search(rf"^- {k}:", tools, re.M) else tools.replace("## Notion\n", f"## Notion\n- {k}: {v}\n", 1)
    tools = re.sub(r"^- connected: no$", "- connected: yes", tools, count=1, flags=re.M) if "## Notion\n- connected: no" in tools else tools
    open("config/tools.md", "w", encoding="utf-8").write(tools)
    print("notion: found " + ", ".join(f"{k} {v[:8]}…" for k, v in found.items()) + "; written to config/tools.md")

def connector_value(prop_name, v):
    """One Notion API property value as the plain shape the Notion connector in Claude takes."""
    k = next(iter(v))
    if k in ("title", "rich_text"): return {prop_name: "".join(x["text"]["content"] for x in v[k])}
    if k in ("select", "status"): return {prop_name: (v[k] or {}).get("name")}
    if k == "number": return {prop_name: v[k]}
    if k == "checkbox": return {prop_name: "__YES__" if v[k] else "__NO__"}
    if k == "url": return {prop_name: v[k]}
    if k == "date":
        if not v[k]: return {f"date:{prop_name}:start": None}
        start = v[k]["start"]
        return {f"date:{prop_name}:start": start, f"date:{prop_name}:is_datetime": 1 if "T" in start else 0}
    return {}

def dump_for_connector(entities):
    """--dump: what the sync would write, in the connector's shape, for a studio with no token.
    The setup-notion skill (connector route) and every role's last step apply this with the Notion tools."""
    out = {"match_on": "ID (Week for Weekly)", "never_overwrite": PERSON, "databases": {}}
    names = {v: k for k, v in DB_TITLES.items()}
    for entity, recs in entities:
        rows = []
        for r in recs:
            flat = {}
            for pname, pval in to_props(entity, r).items():
                key = "userDefined:ID" if pname == "ID" else pname
                flat.update(connector_value(key, pval))
            rows.append(flat)
        out["databases"][names[entity]] = rows
    print(json.dumps(out, ensure_ascii=False, indent=1))

def main():
    dry = "--dry-run" in sys.argv
    cfg = sd.tools_section("Notion"); token = sd.env("NOTION_TOKEN")
    if "--dump" in sys.argv:
        gh = sd.tools_section("Repo").get("url", "")
        pieces = sd.collect_pieces(gh); ideas = sd.collect_ideas(); proposals = sd.collect_proposals()
        canon = sd.collect_canon(pieces); settings = sd.collect_settings(pieces, canon, proposals); weekly = sd.collect_weekly(pieces, ideas, canon, proposals, settings)
        for w in weekly: w["plan_cadence"] = settings.get("plan_cadence_per_week")
        dump_for_connector([("Piece", pieces), ("Idea", ideas), ("Proposal", proposals), ("CanonEntry", canon), ("WeeklyStat", weekly)])
        return
    if not dry and not token: sd.note("notion: NOTION_TOKEN isn't set in the environment or .env; nothing sent"); return
    if not dry and not cfg.get("page id"): sd.note("notion: no page id in config/tools.md under ## Notion; nothing sent"); return
    n = None if dry else Notion(token)
    if "--discover" in sys.argv: discover(n, cfg["page id"]); return
    if not dry and cfg.get("connected", "no") != "yes": sd.note("notion: not connected in config/tools.md (## Notion, connected: yes); nothing sent"); return
    missing = [k for k in DB_KEYS.values() if not cfg.get(k)]
    if not dry and missing: sd.note(f"notion: config/tools.md has no {', '.join(missing)}; run --discover first"); return
    gh = sd.tools_section("Repo").get("url", "")
    pieces = sd.collect_pieces(gh); ideas = sd.collect_ideas(); proposals = sd.collect_proposals()
    canon = sd.collect_canon(pieces); settings = sd.collect_settings(pieces, canon, proposals); weekly = sd.collect_weekly(pieces, ideas, canon, proposals, settings)
    for w in weekly: w["plan_cadence"] = settings.get("plan_cadence_per_week")
    out = []
    ds = {} if dry else {e: n.data_source(cfg[k]) for e, k in DB_KEYS.items()}
    for entity, recs in [("Piece", pieces), ("Idea", ideas), ("Proposal", proposals), ("CanonEntry", canon), ("WeeklyStat", weekly)]:
        made, changed = upsert(n, ds.get(entity), entity, recs, dry); out.append(f"{entity} {len(recs)} ({made} new, {changed} updated)")
    back = read_back(n, ds.get("Piece"), ds.get("Proposal"), dry)
    print(("notion dry run: " if dry else "notion synced: ") + "; ".join(out) + (f"; {back} decision(s) read back" if back else ""))

if __name__ == "__main__":
    main()
