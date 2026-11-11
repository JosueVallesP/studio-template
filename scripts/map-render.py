#!/usr/bin/env python3
"""Builds the person's map from its one source, bank/map/map.json (skills/job-map).

Writes three files beside it, all from the same data so they never disagree:
  bank/map/findings.md   the page: what was read, the ten findings to review, the spine, the rest, the root questions
  bank/map/map.html      the tree, one self-contained page that opens in any browser and works offline, with an orbit view of the same map
  bank/map/map.canvas    the same map as a JSON Canvas file, for anyone who uses Obsidian

Before building, it checks the file against skills/job-map/references/map-data.md and refuses to build when a
rule fails, naming each one. Edit map.json, never the built files: a rebuild overwrites them.

Usage, from the studio's folder:
  python3 scripts/map-render.py                      # bank/map/map.json
  python3 scripts/map-render.py path/to/map.json     # another map (the tests use this)
  python3 scripts/map-render.py --check              # check only, build nothing
  python3 scripts/map-render.py map.json --root=DIR  # where the source files' paths start (default: the studio's folder)

Every quote is also checked against the files its source lists: a quote that isn't there word for word (after
export backslashes, curly quotes and spacing are evened out) stops the build. Files that aren't found are named
and skipped, so a map can still be built from a copy.
"""
import html
import json
import os
import re
import sys

NODE_TYPES = {"claim", "story", "term", "root"}
LINK_KINDS = {"supports", "example_of", "carries", "same_as", "tension", "comes_before", "grows_from", "uses", "replaced_by"}
ACTIONS = {"post", "question", "confirm"}
PRIVACY = {"public", "private"}
CLAIM_STATUS = {"seen", "confirmed", "rejected", "renamed", "held before"}
FINDING_STATUS = {"open", "yes", "no", "renamed", "not sure"}
KIND_NAMES = {
    1: "One idea, said many ways", 2: "A method you haven't written down", 3: "A shape in your ideas",
    4: "Something you act on and never say", 5: "A tension worth keeping", 6: "An unmade piece",
    7: "Your spine", 8: "A gap", 9: "A dropped idea", 10: "How your thinking changed",
    11: "A story that could carry a claim", 12: "Said in private, never published",
}
STATUS_WORDS = {"open": "waiting for your answer", "yes": "you said yes", "no": "you said no",
                "renamed": "you reworded it", "not sure": "you're not sure yet"}
ACTION_WORDS = {"post": "A post to write", "question": "A question for the interviews", "confirm": "Yours to confirm"}


def check(m):
    """Every rule marked (checked) in references/map-data.md. Returns a list of plain-language problems."""
    errs = []
    if not isinstance(m, dict):
        return ["the file isn't a JSON object"]
    for key in ("person", "built", "sources", "nodes", "links", "findings"):
        if key not in m:
            errs.append(f"the top has no '{key}'")
    if errs:
        return errs
    src_ids = set()
    for i, s in enumerate(m["sources"]):
        sid = s.get("id")
        if not sid:
            errs.append(f"source {i + 1} has no id")
            continue
        if sid in src_ids:
            errs.append(f"source id '{sid}' is used twice")
        src_ids.add(sid)
        if s.get("privacy") not in PRIVACY:
            errs.append(f"source '{sid}': privacy must be public or private, not '{s.get('privacy')}'")
    node_ids, nodes = set(), {}
    for i, n in enumerate(m["nodes"]):
        nid = n.get("id")
        if not nid:
            errs.append(f"node {i + 1} has no id")
            continue
        if nid in node_ids:
            errs.append(f"node id '{nid}' is used twice")
        node_ids.add(nid)
        nodes[nid] = n
        t = n.get("type")
        if t not in NODE_TYPES:
            errs.append(f"node '{nid}': type must be claim, story, term or root, not '{t}'")
        if not (n.get("text") or "").strip():
            errs.append(f"node '{nid}' has no text")
        if t == "root":
            if not (n.get("text") or "").rstrip().endswith("?"):
                errs.append(f"root '{nid}' must be a question (end with '?'); the map never writes a value")
            continue
        vs = n.get("versions") or []
        if t == "claim":
            if not vs:
                errs.append(f"claim '{nid}' has no versions; a claim nobody can quote isn't on the map")
            if n.get("said") not in ("outright", "implied"):
                errs.append(f"claim '{nid}': said must be outright or implied")
            if n.get("status", "seen") not in CLAIM_STATUS:
                errs.append(f"claim '{nid}': status must be one of {', '.join(sorted(CLAIM_STATUS))}")
            if n.get("status") == "held before" and not (n.get("dropped") or "").strip():
                errs.append(f"claim '{nid}' is held before: it needs dropped: <date> and the person's reason")
        for j, v in enumerate(vs):
            if v.get("source") not in src_ids:
                errs.append(f"node '{nid}', version {j + 1}: source '{v.get('source')}' isn't in sources")
            has_quote = bool((v.get("quote") or "").strip())
            if t == "claim" and n.get("said") == "outright" and not has_quote:
                errs.append(f"claim '{nid}', version {j + 1}: an outright claim needs the quote, word for word")
            if not has_quote and not (v.get("line") or "").strip():
                errs.append(f"node '{nid}', version {j + 1}: needs a quote (or, for an implied claim, the line it was read from)")
    spine = [n for n in m["nodes"] if n.get("type") == "claim" and n.get("spine")]
    if len(spine) > 5:
        errs.append(f"{len(spine)} claims are marked spine; the spine is three to five")
    for i, l in enumerate(m["links"]):
        tag = f"link {i + 1} ({l.get('from')} to {l.get('to')})"
        for end in ("from", "to"):
            if l.get(end) not in node_ids:
                errs.append(f"{tag}: '{l.get(end)}' isn't a node")
        if l.get("kind") not in LINK_KINDS:
            errs.append(f"{tag}: kind must be one of {', '.join(sorted(LINK_KINDS))}")
        if l.get("kind") == "replaced_by":
            fn = next((n for n in m["nodes"] if n.get("id") == l.get("from")), {})
            if fn.get("status") != "held before":
                errs.append(f"{tag}: a replaced_by link starts at a claim marked held before")
        if l.get("kind") != "grows_from":
            ev = l.get("evidence") or []
            if not ev:
                errs.append(f"{tag}: needs at least one source as evidence")
            for e in ev:
                if e not in src_ids:
                    errs.append(f"{tag}: evidence '{e}' isn't in sources")
    review = 0
    fids = set()
    for i, f in enumerate(m["findings"]):
        fid = f.get("id") or f"finding {i + 1}"
        if fid in fids:
            errs.append(f"finding id '{fid}' is used twice")
        fids.add(fid)
        k = f.get("kind")
        if k not in KIND_NAMES:
            errs.append(f"{fid}: kind must be a number from 1 to 12")
        if not (f.get("title") or "").strip():
            errs.append(f"{fid} has no title")
        ev = f.get("evidence") or []
        need = 1 if k == 9 else 2
        if len(ev) < need:
            errs.append(f"{fid}: needs at least {need} quotes as evidence; a finding the quotes don't carry is cut")
        for j, e in enumerate(ev):
            if not (e.get("quote") or "").strip():
                errs.append(f"{fid}, evidence {j + 1}: no quote")
            if e.get("source") not in src_ids:
                errs.append(f"{fid}, evidence {j + 1}: source '{e.get('source')}' isn't in sources")
            elif k == 12:
                priv = next((s.get("privacy") for s in m["sources"] if s.get("id") == e.get("source")), None)
                if priv != "private":
                    errs.append(f"{fid}: a 'said in private' finding quotes only private sources; '{e.get('source')}' is public")
        for nid in f.get("nodes") or []:
            if nid not in node_ids:
                errs.append(f"{fid}: node '{nid}' isn't on the map")
        act = f.get("action") or {}
        if act.get("type") not in ACTIONS:
            errs.append(f"{fid}: action type must be post, question or confirm")
        if f.get("status", "open") not in FINDING_STATUS:
            errs.append(f"{fid}: status must be one of {', '.join(sorted(FINDING_STATUS))}")
        if f.get("review"):
            review += 1
    if review > 10:
        errs.append(f"{review} findings are marked for review; the review is at most ten")
    return errs


def enrich(m):
    """Fills what the script computes: each node's privacy, its piece count and its first and last dates."""
    srcs = {s["id"]: s for s in m["sources"]}
    for n in m["nodes"]:
        ids = sorted({v.get("source") for v in n.get("versions") or [] if v.get("source") in srcs})
        privs = {srcs[i]["privacy"] for i in ids}
        n["privacy"] = "both" if len(privs) == 2 else (privs.pop() if privs else "")
        n["pieces"] = len(ids)
        dates = sorted(srcs[i].get("date") or "" for i in ids if srcs[i].get("date"))
        if dates:
            n.setdefault("first", dates[0])
            n.setdefault("last", dates[-1])
        n.setdefault("status", "seen" if n.get("type") == "claim" else "")
    return m


def norm(t):
    """Text as compared for the receipts check: no export backslashes or markdown marks, straight quotes, one space."""
    t = (t or "").replace("\\", "")
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2026", "..."), ("\u00a0", " ")):
        t = t.replace(a, b)
    t = re.sub(r"[*_>]+", "", t)
    t = re.sub(r"\[sic\]", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def receipts(m, root):
    """Every quote must appear in one of its source's files. Returns (problems, how many checked, files missing)."""
    errs, checked, missing, cache = [], 0, set(), {}
    srcs = {s["id"]: s for s in m["sources"]}

    def text_of(sid):
        out = []
        for f in srcs.get(sid, {}).get("files") or []:
            fp = os.path.join(root, f)
            if fp not in cache:
                try:
                    cache[fp] = norm(open(fp, encoding="utf-8").read())
                except OSError:
                    cache[fp] = None
            if cache[fp] is None:
                missing.add(f)
            else:
                out.append(cache[fp])
        return out

    def one(where, q, sid):
        nonlocal checked
        shown = (q or "").strip()
        q = norm(q).strip(' "')
        if not q:
            return
        texts = text_of(sid)
        if not texts:
            return
        checked += 1
        # a quote may join two short paragraphs, or skip words with "...": each part must be there
        parts = [x.strip() for x in re.split(r"\.\.\.", q) if len(x.strip()) > 3]
        if not all(any(p in t for t in texts) for p in parts):
            errs.append(f"{where}: the quote isn't in {sid}'s files, word for word: \"{shown[:70]}{'...' if len(shown) > 70 else ''}\"")

    for n in m["nodes"]:
        for j, v in enumerate(n.get("versions") or []):
            if v.get("quote"):
                one(f"node '{n['id']}', version {j + 1}", v["quote"], v.get("source"))
    for f in m["findings"]:
        for j, e in enumerate(f.get("evidence") or []):
            one(f"{f.get('id')}, evidence {j + 1}", e.get("quote"), e.get("source"))
    return errs, checked, sorted(missing)


def src_label(m, sid):
    s = next((x for x in m["sources"] if x["id"] == sid), None)
    if not s:
        return sid
    bits = [sid]
    if s.get("date"):
        bits.append(s["date"])
    if s.get("privacy") == "private":
        bits.append("private")
    return ", ".join(bits)


def md_quote(m, q, source):
    q = (q or "").strip().replace("\n", " ")
    return f"> \"{q}\" ({src_label(m, source)})"


def build_md(m):
    out = []
    srcs = m["sources"]
    pub = sum(1 for s in srcs if s["privacy"] == "public")
    prv = len(srcs) - pub
    kinds = {}
    for s in srcs:
        kinds[s.get("kind") or "other"] = kinds.get(s.get("kind") or "other", 0) + 1
    read = ", ".join(f"{v} {k}{'s' if v != 1 and not k.endswith('s') else ''}" for k, v in sorted(kinds.items(), key=lambda x: -x[1]))
    out.append(f"# What your work adds up to\n")
    out.append(f"Read from: {read}. That's {len(srcs)} separate pieces, {pub} public and {prv} private. Built on {m['built']}"
               + (f", last updated {m['updated']}" if m.get("updated") and m.get("updated") != m["built"] else "") + ".")
    out.append("")
    out.append("Nothing here is confirmed. It's what your own material shows when it's read in one sitting, and you say what's true. "
               "The sentences under each heading are the studio's reading; the quoted lines are yours, word for word.")
    if (m.get("left_out") or "").strip():
        out.append("")
        out.append(m["left_out"].strip())
    out.append("")
    out.append("Private lines (from calls, memos and notes) are marked private. They show here so you can see them, and they never go into a post without your yes.")
    out.append("")
    out.append("The picture of the whole map is in the file beside this one, map.html. It opens in any browser.")
    out.append("")

    out.append("## The pieces, by code\n")
    out.append("| Code | What | When | Public or private |")
    out.append("| --- | --- | --- | --- |")
    for s in srcs:
        title = (s.get("title") or "").replace("|", "/")
        out.append(f"| {s['id']} | {title} | {s.get('date') or ''} | {s['privacy']} |")
    out.append("")

    fs = sorted(m["findings"], key=lambda f: f.get("rank") or 999)
    review = [f for f in fs if f.get("review")]
    rest = [f for f in fs if not f.get("review")]
    nodes = {n["id"]: n for n in m["nodes"]}

    def finding_block(i, f, full=True):
        lines = [f"### {i}. {f['title'].strip()}"]
        lines.append(f"{KIND_NAMES[f['kind']]}{' (new since the last update)' if f.get('new') else ''}. Status: {STATUS_WORDS.get(f.get('status', 'open'), 'waiting for your answer')}.")
        lines.append("")
        if (f.get("what") or "").strip():
            lines.append(f["what"].strip())
            lines.append("")
        ev = f.get("evidence") or []
        for e in (ev if full else ev[:2]):
            lines.append(md_quote(m, e.get("quote"), e.get("source")))
        lines.append("")
        act = f.get("action") or {}
        if (act.get("text") or "").strip():
            lines.append(f"{ACTION_WORDS[act['type']]}: {act['text'].strip()}")
            lines.append("")
        if (f.get("answer") or "").strip():
            lines.append(f"What you said: {f['answer'].strip()}")
            lines.append("")
        return lines

    if review:
        out.append("## The ten to look at first\n" if len(review) == 10 else f"## The {len(review)} to look at first\n")
        out.append("These are the strongest. The review goes through them one at a time, about 20 minutes, and you say what's true.\n")
        for i, f in enumerate(review, 1):
            out += finding_block(i, f)

    held = [n for n in m["nodes"] if n.get("type") == "claim" and n.get("status") == "held before"]
    if held:
        out.append("## Views you no longer hold\n")
        out.append("You told the studio you've moved on from these. Nothing quotes them as what you think now.\n")
        for n in held:
            out.append(f"- {n.get('text')} ({n.get('dropped')})")
        out.append("")
    spine = [n for n in m["nodes"] if n.get("type") == "claim" and n.get("spine")]
    if spine:
        out.append("## Your spine\n")
        out.append("The claims the rest of your work hangs from, counted in separate pieces.\n")
        for n in spine:
            span = f", from {n['first']} to {n['last']}" if n.get("first") and n.get("last") and n["first"] != n["last"] else ""
            out.append(f"- **{n['text'].strip()}** In {n['pieces']} piece{'s' if n['pieces'] != 1 else ''}{span}.")
            v = (n.get("versions") or [{}])[0]
            if v.get("quote"):
                out.append(f"  > \"{v['quote'].strip()}\" ({src_label(m, v['source'])})")
        out.append("")

    if rest:
        out.append("## Everything else the map found\n")
        for i, f in enumerate(rest, len(review) + 1):
            out += finding_block(i, f, full=False)

    roots = [n for n in m["nodes"] if n.get("type") == "root"]
    if roots:
        out.append("## Questions for the interviews\n")
        out.append("Where your spine seems to grow from. These are questions, not answers: the interviews ask them.\n")
        grows = {}
        for l in m["links"]:
            if l.get("kind") == "grows_from":
                grows.setdefault(l["to"], []).append(l["from"])
        for r in roots:
            under = [nodes[c]["text"].strip() for c in grows.get(r["id"], []) if c in nodes]
            out.append(f"- {r['text'].strip()}" + (f" (under: {'; '.join(under)})" if under else ""))
        out.append("")

    out.append("## What happens next\n")
    open_review = [f for f in review if f.get("status", "open") == "open"]
    if open_review:
        out.append("Say \"review my map\". We go through the findings above one at a time and you say what's true, about 20 minutes. "
                   "Anything you confirm goes into your files; anything you say no to is never raised again.")
    else:
        out.append("You've been through the review. Say \"update my map\" when you've handed over new material, and \"start my brand tree\" to carry on with the interviews.")
    out.append("")
    return "\n".join(out)


def layout(m):
    """Column per spine claim. Shared by the canvas; the page lays itself out the same way in the browser."""
    nodes = {n["id"]: n for n in m["nodes"]}
    spine = [n["id"] for n in m["nodes"] if n.get("type") == "claim" and n.get("spine")]
    if not spine:
        spine = [n["id"] for n in sorted((n for n in m["nodes"] if n.get("type") == "claim"), key=lambda n: -n.get("pieces", 0))[:3]]
    col = {s: i for i, s in enumerate(spine)}
    adj = {}
    for l in m["links"]:
        adj.setdefault(l["from"], []).append(l["to"])
        adj.setdefault(l["to"], []).append(l["from"])
    loose = len(spine)
    # nearest spine claim by links (breadth first), else shared sources, else the loose column
    for n in m["nodes"]:
        nid = n["id"]
        if nid in col:
            continue
        seen, frontier, hit = {nid}, [nid], None
        while frontier and hit is None:
            nxt = []
            for x in frontier:
                for y in adj.get(x, []):
                    if y in col and (n["type"] != "root" or y in spine):
                        hit = col[y]
                        break
                    if y not in seen:
                        seen.add(y)
                        nxt.append(y)
                if hit is not None:
                    break
            frontier = nxt
        if hit is None and n.get("versions"):
            mine = {v.get("source") for v in n["versions"]}
            best = max(spine, key=lambda s: len(mine & {v.get("source") for v in nodes[s].get("versions") or []}), default=None)
            if best and mine & {v.get("source") for v in nodes[best].get("versions") or []}:
                hit = col[best]
        col[nid] = loose if hit is None else hit
    return spine, col


def build_canvas(m):
    spine, col = layout(m)
    W, GAP, H = 360, 80, 140
    colors = {"claim": "4", "story": "2", "term": "5", "root": "6"}
    stacks, cnodes = {}, []
    for n in m["nodes"]:
        c = col[n["id"]]
        x = c * (W + GAP)
        if n["type"] == "root":
            k = stacks.setdefault((c, "root"), 0)
            y = 200 + k * (H + 30)
            stacks[(c, "root")] = k + 1
        elif n["id"] in spine:
            y = 0
        else:
            k = stacks.setdefault((c, "up"), 0)
            y = -(k + 1) * (H + 30)
            stacks[(c, "up")] = k + 1
        label = n["text"].strip()
        if n["type"] == "claim":
            label = ("**" + label + "**") if n["id"] in spine else label
            label += f"\n\n{n.get('pieces', 0)} pieces · {n.get('privacy') or ''} · {n.get('status', 'seen')}"
        elif n["type"] == "story":
            label = "Story: " + label
        elif n["type"] == "term":
            label = "Framework: " + label + (f" (credit: {n['credit']})" if n.get("credit") else "")
        cnodes.append({"id": n["id"], "type": "text", "text": label, "x": x, "y": y, "width": W, "height": H,
                       "color": colors.get(n["type"], "0")})
    edges = []
    for i, l in enumerate(m["links"]):
        e = {"id": f"e{i + 1}", "fromNode": l["from"], "toNode": l["to"], "label": l["kind"].replace("_", " ")}
        if l["kind"] == "tension":
            e["color"] = "1"
        edges.append(e)
    return {"nodes": cnodes, "edges": edges}


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{--bg:#f6f3ec;--paper:#fffdf8;--ink:#1d1b17;--soft:#5f5a50;--line:#cfc7b6;--accent:#2f5d8a;--warm:#b5652b;--private:#7a4f9a;--tension:#b3392f;--dim:.18}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15140f;--paper:#1f1d17;--ink:#ece7db;--soft:#a9a291;--line:#4a4538;--accent:#7fb0e0;--warm:#e0975e;--private:#c39be0;--tension:#e57367;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15140f;--paper:#1f1d17;--ink:#ece7db;--soft:#a9a291;--line:#4a4538;--accent:#7fb0e0;--warm:#e0975e;--private:#c39be0;--tension:#e57367;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));background:var(--bg);color:var(--ink);font:16px/1.5 Georgia,"Iowan Old Style","Palatino Linotype",serif}
header{padding-block:28px 8px;max-width:1200px;margin:0 auto}
h1{font-size:28px;line-height:1.2;margin:0 0 6px;font-weight:600}
.lede{color:var(--soft);margin:0 0 4px;max-width:70ch}
.bar{display:flex;flex-wrap:wrap;gap:8px;padding-block:12px;max-width:1200px;margin:0 auto;align-items:center}
.bar label{font:13px/1.2 system-ui,sans-serif;color:var(--soft)}
.bar select,.bar button{font:14px system-ui,sans-serif;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:6px 8px}
main{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:16px;max-width:1200px;margin:0 auto;padding-block:0 40px}
@media (max-width:900px){main{grid-template-columns:1fr}}
.treewrap{background:var(--paper);border:1px solid var(--line);border-radius:10px;overflow-x:auto}
svg{display:block}
.card{font:13px/1.35 system-ui,sans-serif;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:8px 10px;height:100%;overflow:hidden;cursor:pointer}
.card.spine{border:2px solid var(--accent);font-size:14px;font-weight:600}
.card.root{border-style:dashed;color:var(--soft);font-style:italic}
.card.story{border-left:4px solid var(--warm)}
.card.term{border-left:4px solid var(--accent)}
.loosehead{font:13px system-ui,sans-serif;color:var(--soft);margin:0 16px 8px}
#loose .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px;padding:0 16px 16px}
.card .meta{display:block;font-weight:400;font-size:11px;color:var(--soft);margin-top:4px}
.card.private{box-shadow:inset 0 0 0 1px var(--private)}
.card.confirmed{background:color-mix(in srgb,var(--accent) 10%,var(--paper))}
.dim{opacity:var(--dim)}
.leaf{fill:var(--accent)}
.leaf.private{fill:var(--private)}
.trunk{stroke:var(--soft);stroke-width:3;fill:none}
.twig{stroke:var(--line);stroke-width:1.5;fill:none}
.tension{stroke:var(--tension);stroke-width:1.5;stroke-dasharray:5 4;fill:none}
.ground{stroke:var(--soft);stroke-width:1}
.lbl{font:11px system-ui,sans-serif;fill:var(--soft)}
aside{min-width:0;display:flex;flex-direction:column;gap:12px}
.panel{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px}
.panel h2{font-size:18px;margin:0 0 8px}
.finding{border-top:1px solid var(--line);padding:10px 0;cursor:pointer}
.finding:first-of-type{border-top:0}
.finding h3{font-size:15px;margin:0 0 4px;line-height:1.3}
.finding .k{font:12px system-ui,sans-serif;color:var(--soft)}
.finding.on{background:color-mix(in srgb,var(--accent) 8%,transparent)}
blockquote{margin:6px 0;padding-left:10px;border-left:3px solid var(--line);font-size:14px}
blockquote.private{border-left-color:var(--private)}
.src{font:12px system-ui,sans-serif;color:var(--soft)}
.act{font:13px system-ui,sans-serif;margin-top:6px}
.badge{display:inline-block;font:11px system-ui,sans-serif;border:1px solid var(--line);border-radius:999px;padding:1px 7px;margin-right:4px;color:var(--soft)}
.badge.private{border-color:var(--private);color:var(--private)}
#orbit{display:none;width:100%;height:560px;cursor:grab;touch-action:none}
#orbit.drag{cursor:grabbing}
.orbiton #orbit{display:block}.orbiton #tree,.orbiton #loose{display:none}
.hint{font:12px system-ui,sans-serif;color:var(--soft);margin:0;padding:8px 12px;display:none}.orbiton .hint{display:block}
.key{font:12px system-ui,sans-serif;color:var(--soft);display:flex;flex-wrap:wrap;gap:12px;padding-block:8px;max-width:1200px;margin:0 auto}
.sw{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:4px;vertical-align:middle}
</style>
</head>
<body>
<header>
<h1>__H1__</h1>
<p class="lede">__LEDE__</p>
</header>
<div class="key">
<span><span class="sw" style="background:var(--accent)"></span>Leaves: your pieces</span>
<span><span class="sw" style="border:2px solid var(--accent)"></span>Spine: the claims the rest hangs from</span>
<span><span class="sw" style="background:var(--warm)"></span>A story</span>
<span><span class="sw" style="border:1px dashed var(--soft)"></span>Roots: questions for the interviews</span>
<span><span class="sw" style="background:var(--private)"></span>Private</span>
<span><span class="sw" style="border-top:2px dashed var(--tension)"></span>Pulls against</span>
</div>
<div class="bar">
<label>View <select id="fview"><option value="tree">tree</option><option value="orbit">orbit</option></select></label>
<label>Show <select id="fprivacy"><option value="all">public and private</option><option value="public">public only</option><option value="private">private only</option></select></label>
<label><select id="fstatus"><option value="all">confirmed and guessed</option><option value="confirmed">confirmed only</option><option value="seen">guessed only</option></select></label>
<button id="clear" type="button">Clear selection</button>
</div>
<main>
<div class="treewrap"><svg id="tree" xmlns="http://www.w3.org/2000/svg"></svg><div id="loose"></div><p class="hint">Drag to turn it. Click a dot to see what it rests on. The spine sits in the middle; each claim's stories (orange) and other claims and frameworks (blue) gather around it, and the questions for the interviews hang below as open circles.</p><canvas id="orbit"></canvas></div>
<aside>
<div class="panel" id="detail"><h2>Pick anything</h2><p class="src">Click a claim, a story or a finding to see the lines it rests on.</p></div>
<div class="panel"><h2 id="fhead">Findings</h2><div id="findings"></div></div>
</aside>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
var M=JSON.parse(document.getElementById('data').textContent);
var KINDS=__KINDS__, STATUS=__STATUS__, ACTIONS=__ACTIONS__;
var byId={};M.nodes.forEach(function(n){byId[n.id]=n});
var src={};M.sources.forEach(function(s){src[s.id]=s});
function esc(t){return String(t==null?'':t).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function srcLabel(id){var s=src[id];if(!s)return esc(id);return esc(id+(s.date?', '+s.date:'')+(s.privacy==='private'?', private':''))}
// columns: one per spine claim, a loose column for anything not tied to the spine
var spine=M.nodes.filter(function(n){return n.type==='claim'&&n.spine}).map(function(n){return n.id});
if(!spine.length)spine=M.nodes.filter(function(n){return n.type==='claim'}).sort(function(a,b){return b.pieces-a.pieces}).slice(0,3).map(function(n){return n.id});
var col={};spine.forEach(function(s,i){col[s]=i});
var adj={};M.links.forEach(function(l){(adj[l.from]=adj[l.from]||[]).push(l.to);(adj[l.to]=adj[l.to]||[]).push(l.from)});
var loose=spine.length,usedLoose=false;
M.nodes.forEach(function(n){if(n.id in col)return;var seen={},fr=[n.id],hit=null;seen[n.id]=1;
 while(fr.length&&hit===null){var nx=[];for(var i=0;i<fr.length&&hit===null;i++){(adj[fr[i]]||[]).forEach(function(y){if(hit!==null)return;if(y in col&&spine.indexOf(y)>=0){hit=col[y];return}if(!seen[y]){seen[y]=1;nx.push(y)}})}fr=nx}
 if(hit===null){usedLoose=true;hit=loose}col[n.id]=hit});
var ncol=Math.max(1,loose),PAD=24,G=12,AV=document.querySelector('.treewrap').clientWidth||1000,CW=Math.max(190,Math.min(270,Math.floor((AV-2*PAD-2)/ncol))),W0=CW-16,WI=W0-20,ORDER={claim:0,story:1,term:2};
var ups={},downs={},looseNodes=[];M.nodes.forEach(function(n){var c=col[n.id];if(c===loose&&loose>0){looseNodes.push(n);return}if(n.type==='root')(downs[c]=downs[c]||[]).push(n);else if(spine.indexOf(n.id)<0)(ups[c]=ups[c]||[]).push(n)});
Object.keys(ups).forEach(function(c){ups[c].sort(function(a,b){return (ORDER[a.type]-ORDER[b.type])||((b.pieces||0)-(a.pieces||0))})});
function cardClass(n,cls){return 'card '+cls+(n.privacy==='private'?' private':'')+(n.status==='confirmed'?' confirmed':'')}
function cardHTML(n){var meta=n.type==='root'?'':(n.pieces?n.pieces+' piece'+(n.pieces>1?'s':''):'')+(n.privacy==='private'?' · private':n.privacy==='both'?' · public and private':'')+(n.type==='claim'&&n.status==='held before'?' · you no longer hold this':n.type==='claim'&&n.status!=='confirmed'?' · guessed':'');
 return (n.type==='story'?'Story: ':n.type==='term'?'Framework: ':'')+esc(n.text)+(meta?'<span class="meta">'+meta+'</span>':'')}
// measure each card at its width, so text never spills
var probe=document.createElement('div');probe.style.cssText='position:absolute;visibility:hidden;left:-9999px;top:0';document.body.appendChild(probe);
function hOf(n,cls,w){var d=document.createElement('div');d.className=cardClass(n,cls);d.style.width=w+'px';d.style.height='auto';d.innerHTML=cardHTML(n);probe.appendChild(d);var h=Math.ceil(d.getBoundingClientRect().height)+2;probe.removeChild(d);return h}
var H_={},upH=[],downH=[],spH=[],leafRows=[],per=Math.max(1,Math.floor(W0/14));
for(var c=0;c<ncol;c++){var sid=spine[c],u=0,dn=0,ids={};
 if(sid){H_[sid]=Math.max(84,hOf(byId[sid],'spine',W0));(byId[sid].versions||[]).forEach(function(v){ids[v.source]=1})}
 (ups[c]||[]).forEach(function(n){H_[n.id]=hOf(n,n.type,WI);u+=H_[n.id]+G;(n.versions||[]).forEach(function(v){ids[v.source]=1})});
 (downs[c]||[]).forEach(function(n){H_[n.id]=hOf(n,'root',WI);dn+=H_[n.id]+G});
 upH[c]=u;downH[c]=dn;spH[c]=sid?H_[sid]:84;leafRows[c]=Object.keys(ids)}
document.body.removeChild(probe);
var maxUp=Math.max.apply(null,upH.concat([0])),maxDown=Math.max.apply(null,downH.concat([0])),maxSp=Math.max.apply(null,spH.concat([84]));
var rows=Math.max.apply(null,leafRows.map(function(k){return Math.ceil(k.length/per)}).concat([1]));
var top=PAD+rows*14+20,spineY=top+maxUp+30,groundY=spineY+maxSp+40,H=groundY+30+maxDown+PAD,W=PAD*2+ncol*CW;
var svg=document.getElementById('tree');svg.setAttribute('width',W);svg.setAttribute('height',H);svg.setAttribute('viewBox','0 0 '+W+' '+H);
var NS='http://www.w3.org/2000/svg',pos={};
function el(t,a,p){var e=document.createElementNS(NS,t);for(var k in a)e.setAttribute(k,a[k]);(p||svg).appendChild(e);return e}
var gLines=el('g',{}),gCards=el('g',{});
el('line',{x1:0,y1:groundY,x2:W,y2:groundY,'class':'ground'},gLines);
el('text',{x:8,y:groundY-6,'class':'lbl'},gLines).textContent='what you say';
el('text',{x:8,y:groundY+16,'class':'lbl'},gLines).textContent='where it may come from';
function card(n,x,y,w,h,cls){pos[n.id]={x:x+w/2,y:y,yb:y+h,cx:x+w/2};
 var fo=el('foreignObject',{x:x,y:y,width:w,height:h,'data-id':n.id},gCards);
 var d=document.createElement('div');d.className=cardClass(n,cls);d.innerHTML=cardHTML(n);
 d.addEventListener('click',function(){showNode(n.id)});fo.appendChild(d)}
for(var c=0;c<ncol;c++){var x0=PAD+c*CW+8,cx=PAD+c*CW+CW/2,sid=spine[c];
 if(sid){card(byId[sid],x0,spineY,W0,H_[sid],'spine');el('path',{d:'M'+cx+' '+groundY+' L'+cx+' '+(spineY+H_[sid]),'class':'trunk'},gLines)}
 else{el('text',{x:x0,y:spineY+30,'class':'lbl'},gLines).textContent='not tied to the spine yet'}
 var cur=spineY-30,below=spineY;
 (ups[c]||[]).forEach(function(n){var h=H_[n.id],y=cur-h;card(n,x0+10,y,WI,h,n.type);
  el('path',{d:'M'+cx+' '+(y+h)+' L'+cx+' '+below,'class':'twig'},gLines);below=y;cur=y-G});
 var dy=groundY+30;(downs[c]||[]).forEach(function(n){var h=H_[n.id];card(n,x0+10,dy,WI,h,'root');
  el('path',{d:'M'+cx+' '+groundY+' L'+cx+' '+dy,'class':'twig'},gLines);dy+=h+G});
 // leaves: the pieces this column's claims rest on
 leafRows[c].forEach(function(k,i){var r=Math.floor(i/per),q=i%per;
  var cc=el('circle',{cx:x0+7+q*14,cy:top-12-r*14,r:5,'class':'leaf'+(src[k]&&src[k].privacy==='private'?' private':''),'data-src':k},gLines);
  el('title',{},cc).textContent=k+(src[k]&&src[k].title?': '+src[k].title:'')})}
if(looseNodes.length){var lb=document.getElementById('loose');lb.innerHTML='<p class="loosehead">Not tied to your spine yet: ideas the map found that don\'t connect to the claims above. Some of them are findings.</p><div class="grid"></div>';
 var gr=lb.querySelector('.grid');looseNodes.sort(function(a,b){return (ORDER[a.type]||0)-(ORDER[b.type]||0)}).forEach(function(n){var d=document.createElement('div');d.className=cardClass(n,n.type==='root'?'root':n.type);d.setAttribute('data-id',n.id);d.innerHTML=cardHTML(n);d.addEventListener('click',function(){showNode(n.id)});gr.appendChild(d)})}
M.links.forEach(function(l){if(l.kind!=='tension')return;var a=pos[l.from],b=pos[l.to];if(!a||!b)return;
 if(Math.abs(a.cx-b.cx)<2){var ox=a.cx+W0/2+14,ya=(a.y+a.yb)/2,yb=(b.y+b.yb)/2;el('path',{d:'M'+(a.cx+W0/2-12)+' '+ya+' C'+ox+' '+ya+' '+ox+' '+yb+' '+(b.cx+W0/2-12)+' '+yb,'class':'tension'},gCards);return}
 var midY=Math.min(a.y,b.y)-40;el('path',{d:'M'+a.cx+' '+a.y+' C'+a.cx+' '+midY+' '+b.cx+' '+midY+' '+b.cx+' '+b.y,'class':'tension'},gLines)});
var sel=null;
function visible(n){var p=document.getElementById('fprivacy').value,s=document.getElementById('fstatus').value;
 if(p!=='all'&&n.privacy&&n.privacy!==p&&n.privacy!=='both')return false;
 if(s==='confirmed'&&n.type==='claim'&&n.status!=='confirmed')return false;
 if(s==='seen'&&n.type==='claim'&&n.status==='confirmed')return false;return true}
function paint(){document.querySelectorAll('#tree foreignObject,#loose .card').forEach(function(fo){var n=byId[fo.getAttribute('data-id')];
 var on=visible(n)&&(!sel||sel.indexOf(n.id)>=0);fo.classList.toggle('dim',!on)});if(window.orbitDraw)orbitDraw()}
function quotes(vs){return (vs||[]).map(function(v){var p=src[v.source]&&src[v.source].privacy==='private';
 return '<blockquote class="'+(p?'private':'')+'">'+esc(v.quote?'"'+v.quote+'"':v.line)+'<div class="src">'+srcLabel(v.source)+(v.note?' · '+esc(v.note):'')+'</div></blockquote>'}).join('')}
function showNode(id){var n=byId[id];sel=[id];M.links.forEach(function(l){if(l.from===id)sel.push(l.to);if(l.to===id)sel.push(l.from)});paint();
 var rel=M.links.filter(function(l){return l.from===id||l.to===id}).map(function(l){var o=byId[l.from===id?l.to:l.from];
  return '<li>'+esc(l.kind.replace('_',' '))+': '+esc(o?o.text:'')+'</li>'}).join('');
 document.getElementById('detail').innerHTML='<h2>'+esc(n.text)+'</h2>'+(n.privacy?'<span class="badge '+(n.privacy==='private'?'private':'')+'">'+esc(n.privacy)+'</span>':'')+
  (n.type==='claim'?'<span class="badge">'+(n.status==='confirmed'?'confirmed':'guessed')+'</span><span class="badge">'+(n.said==='implied'?'read between the lines':'said outright')+'</span>':'')+
  (n.first?'<span class="badge">'+esc(n.first)+(n.last&&n.last!==n.first?' to '+esc(n.last):'')+'</span>':'')+
  (n.type==='root'?'<p class="src">A question for the interviews, not an answer.</p>':quotes(n.versions))+(rel?'<p class="src">Connected to:</p><ul>'+rel+'</ul>':'')}
var fs=M.findings.slice().sort(function(a,b){return (a.rank||999)-(b.rank||999)}),box=document.getElementById('findings');
var nrev=fs.filter(function(f){return f.review}).length;document.getElementById('fhead').textContent=nrev?'The '+(nrev===10?'ten':nrev)+' to look at first, then the rest':'Findings';
fs.forEach(function(f,i){var d=document.createElement('div');d.className='finding';
 d.innerHTML='<div class="k">'+(i+1)+'. '+esc(KINDS[f.kind])+(f.review?'':' · more')+(f.new?' · new':'')+' · '+esc(STATUS[f.status||'open'])+'</div><h3>'+esc(f.title)+'</h3>';
 d.addEventListener('click',function(){box.querySelectorAll('.finding').forEach(function(x){x.classList.remove('on')});d.classList.add('on');sel=(f.nodes||[]).slice();paint();
  var a=f.action||{};document.getElementById('detail').innerHTML='<h2>'+esc(f.title)+'</h2><p>'+esc(f.what||'')+'</p>'+quotes(f.evidence)+
   (a.text?'<p class="act"><strong>'+esc(ACTIONS[a.type])+':</strong> '+esc(a.text)+'</p>':'')+(f.answer?'<p class="act"><strong>What you said:</strong> '+esc(f.answer)+'</p>':'');if(window.innerWidth<900)document.getElementById('detail').scrollIntoView({behavior:'smooth',block:'start'})});
 box.appendChild(d)});
['fprivacy','fstatus'].forEach(function(id){document.getElementById(id).addEventListener('change',paint)});
document.getElementById('clear').addEventListener('click',function(){sel=null;box.querySelectorAll('.finding').forEach(function(x){x.classList.remove('on')});paint()});
// orbit: the same nodes and links turned in 3D, drawn on a canvas, no library, works offline
(function(){
 var cv=document.getElementById('orbit'),wrap=document.querySelector('.treewrap'),ctx=cv.getContext('2d'),P={},yaw=0.6,pitch=-0.25,drag=null,still=0;
 var calm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 var nc=Math.max(1,spine.length),gold=Math.PI*(3-Math.sqrt(5));
 function place(n,i){var c=col[n.id],a=(c<nc?c/nc:0)*2*Math.PI;
  if(spine.indexOf(n.id)>=0)return [Math.cos(a)*(nc>1?140:0),0,Math.sin(a)*(nc>1?140:0)];
  if(c>=nc||c===undefined){var y=1-(i%40)/20,r=Math.sqrt(Math.max(0,1-y*y)),t=i*gold;return [Math.cos(t)*r*300,y*200,Math.sin(t)*r*300]}
  var k=(n.type==='root'?(downs[c]||[]):(ups[c]||[])).indexOf(n),sp=0.45,b=a+((k%3)-1)*sp,rad=170+Math.floor(k/3)*55;
  return [Math.cos(b)*rad,n.type==='root'?-130-Math.floor(k/3)*25:60+(k%3)*35,Math.sin(b)*rad]}
 M.nodes.forEach(function(n,i){P[n.id]=place(n,i)});
 function css(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()||'#888'}
 var pr=[];
 function size(){var r=window.devicePixelRatio||1,w=wrap.clientWidth;cv.width=w*r;cv.height=560*r;cv.style.height='560px';ctx.setTransform(r,0,0,r,0,0)}
 function proj(p){var cy=Math.cos(yaw),sy=Math.sin(yaw),cp=Math.cos(pitch),sp=Math.sin(pitch);
  var x=p[0]*cy-p[2]*sy,z=p[0]*sy+p[2]*cy,y=p[1]*cp-z*sp;z=p[1]*sp+z*cp;var f=700/(700+z),w=cv.clientWidth;
  return {x:w/2+x*f*Math.min(1,w/760),y:280-y*f*Math.min(1,w/760),f:f,z:z}}
 function on(n){return visible(n)&&(!sel||sel.indexOf(n.id)>=0)}
 window.orbitDraw=function(){if(!document.body.classList.contains('orbiton'))return;var w=cv.clientWidth;ctx.clearRect(0,0,w,560);
  var C={paper:css('--paper'),ink:css('--ink'),soft:css('--soft'),line:css('--line'),acc:css('--accent'),warm:css('--warm'),pri:css('--private'),ten:css('--tension')};
  var Q={};M.nodes.forEach(function(n){Q[n.id]=proj(P[n.id])});
  M.links.forEach(function(l){var a=Q[l.from],b=Q[l.to];if(!a||!b)return;var lit=on(byId[l.from])&&on(byId[l.to]);
   ctx.globalAlpha=lit?0.7:0.12;ctx.strokeStyle=l.kind==='tension'?C.ten:C.line;ctx.lineWidth=l.kind==='tension'?1.5:1;ctx.setLineDash(l.kind==='tension'?[5,4]:[]);
   ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke()});
  ctx.setLineDash([]);pr=M.nodes.map(function(n){return {n:n,q:Q[n.id]}}).sort(function(a,b){return b.q.z-a.q.z});
  pr.forEach(function(o){var n=o.n,q=o.q,isS=spine.indexOf(n.id)>=0,r=(isS?9:n.type==='root'?4:6)*q.f,lit=on(n);
   ctx.globalAlpha=lit?1:0.15;ctx.beginPath();ctx.arc(q.x,q.y,r,0,2*Math.PI);
   if(n.type==='root'){ctx.strokeStyle=C.soft;ctx.setLineDash([2,2]);ctx.stroke();ctx.setLineDash([])}
   else{ctx.fillStyle=n.privacy==='private'?C.pri:n.type==='story'?C.warm:C.acc;ctx.fill();if(isS){ctx.strokeStyle=C.ink;ctx.lineWidth=1.5;ctx.stroke()}}
   var picked=sel&&sel.indexOf(n.id)>=0;if(lit&&(picked||(isS&&!sel&&q.z<=20))){var t=n.text.length>40?n.text.slice(0,38)+'…':n.text;ctx.font=(isS?'600 ':'')+'12px system-ui,sans-serif';ctx.lineWidth=4;ctx.strokeStyle=C.paper;ctx.lineJoin='round';ctx.strokeText(t,q.x+r+4,q.y+4);ctx.fillStyle=C.ink;ctx.fillText(t,q.x+r+4,q.y+4)}});
  ctx.globalAlpha=1};
 function tick(){if(!drag&&!calm&&!sel&&Date.now()-still>2500){yaw+=0.0025;orbitDraw()}requestAnimationFrame(tick)}
 cv.addEventListener('pointerdown',function(e){drag={x:e.clientX,y:e.clientY,m:0};cv.classList.add('drag');cv.setPointerCapture(e.pointerId)});
 cv.addEventListener('pointermove',function(e){if(!drag)return;var dx=e.clientX-drag.x,dy=e.clientY-drag.y;drag.m+=Math.abs(dx)+Math.abs(dy);yaw+=dx*0.008;pitch=Math.max(-1.3,Math.min(1.3,pitch+dy*0.008));drag.x=e.clientX;drag.y=e.clientY;orbitDraw()});
 cv.addEventListener('pointerup',function(e){var moved=drag&&drag.m>4;drag=null;still=Date.now();cv.classList.remove('drag');if(moved)return;
  var b=cv.getBoundingClientRect(),x=e.clientX-b.left,y=e.clientY-b.top,best=null,bd=18*18;
  pr.forEach(function(o){if(!visible(o.n))return;var d=(o.q.x-x)*(o.q.x-x)+(o.q.y-y)*(o.q.y-y);if(d<bd){bd=d;best=o.n}});
  if(best){showNode(best.id);if(window.innerWidth<900)document.getElementById('detail').scrollIntoView({behavior:'smooth',block:'start'})}});
 document.getElementById('fview').addEventListener('change',function(e){var o=e.target.value==='orbit';document.body.classList.toggle('orbiton',o);if(o){size();orbitDraw()}});
 window.addEventListener('resize',function(){if(document.body.classList.contains('orbiton')){size();orbitDraw()}});
 requestAnimationFrame(tick)})();
paint();
})();
</script>
</body>
</html>
"""


def build_html(m):
    srcs = m["sources"]
    pub = sum(1 for s in srcs if s["privacy"] == "public")
    lede = (f"Read from {len(srcs)} pieces, {pub} public and {len(srcs) - pub} private. Nothing here is confirmed until you say so: "
            "the sentences are the studio's reading, and every quoted line is yours. Click anything to see what it rests on.")
    data = json.dumps(m, ensure_ascii=False).replace("</", "<\\/")
    name = m["person"].strip()
    return (PAGE.replace("__TITLE__", html.escape(f"{name}'s map"))
            .replace("__H1__", html.escape(f"What {name}'s work adds up to"))
            .replace("__LEDE__", html.escape(lede))
            .replace("__KINDS__", json.dumps({str(k): v for k, v in KIND_NAMES.items()}))
            .replace("__STATUS__", json.dumps(STATUS_WORDS))
            .replace("__ACTIONS__", json.dumps(ACTION_WORDS))
            .replace("__DATA__", data))


def main(argv):
    only_check = "--check" in argv
    args = [a for a in argv if not a.startswith("--")]
    path = args[0] if args else os.path.join("bank", "map", "map.json")
    try:
        with open(path, encoding="utf-8") as fh:
            m = json.load(fh)
    except FileNotFoundError:
        print(f"map-render: no map at {path}. The map skill (skills/job-map) writes it first.")
        return 1
    except json.JSONDecodeError as e:
        print(f"map-render: {path} isn't valid JSON (line {e.lineno}, column {e.colno}): {e.msg}")
        return 1
    errs = check(m)
    if errs:
        print(f"map-render: {len(errs)} problem{'s' if len(errs) != 1 else ''} in {path}; nothing built.")
        for e in errs:
            print("  - " + e)
        return 1
    root = next((a.split("=", 1)[1] for a in argv if a.startswith("--root=")), None)
    if root is None:
        here = os.path.dirname(os.path.abspath(path))
        root = os.path.dirname(os.path.dirname(here)) if here.replace(os.sep, "/").endswith("bank/map") else here
    rerrs, checked, missing = receipts(m, root)
    if rerrs:
        print(f"map-render: {len(rerrs)} quote{'s' if len(rerrs) != 1 else ''} not found in the person's files; nothing built. "
              "A quote on the map is word for word or it comes off.")
        for e in rerrs:
            print("  - " + e)
        return 1
    note = f" Checked {checked} quotes against the person's files." if checked else ""
    if missing:
        note += f" Couldn't check the quotes from {len(missing)} file{'s' if len(missing) != 1 else ''} not found ({', '.join(missing[:3])}{'...' if len(missing) > 3 else ''})."
    enrich(m)
    if only_check:
        print(f"map-render: {path} checks out ({len(m['nodes'])} nodes, {len(m['links'])} links, {len(m['findings'])} findings).{note}")
        return 0
    out = os.path.dirname(os.path.abspath(path))
    with open(os.path.join(out, "findings.md"), "w", encoding="utf-8") as fh:
        fh.write(build_md(m))
    with open(os.path.join(out, "map.html"), "w", encoding="utf-8") as fh:
        fh.write(build_html(m))
    with open(os.path.join(out, "map.canvas"), "w", encoding="utf-8") as fh:
        json.dump(build_canvas(m), fh, ensure_ascii=False, indent=1)
    rel = os.path.relpath(out)
    if rel.startswith(".."):
        rel = out
    print(f"map-render: built {rel}/findings.md, {rel}/map.html and {rel}/map.canvas "
          f"({len(m['nodes'])} nodes, {len(m['links'])} links, {len(m['findings'])} findings).{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
