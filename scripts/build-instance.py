#!/usr/bin/env python3
"""Builds, or fills, a person's instance of the studio from their intake answers.

Two ways to run it:

  New instance from the form's answers (run from anywhere):
    python3 scripts/build-instance.py answers.yaml --studio /path/to/content-studio --out /path/to/their-studio [--inbox /path/to/their/uploads]

  Fill an instance that already exists (run from inside it, as setup-intake does):
    python3 scripts/build-instance.py config/intake.yaml --fill

What it writes, all person-owned, never a studio path:
  config/intake.yaml              the answers, kept as the record
  config/tools.md                 channels, Notion and Figma lines
  canon/strategy/outcomes.md      the goal and channels in their words, hours under Capacity
  canon/visual/brand-assets.md    logo, colors, fonts, references, the never word
  YOUR-STUDIO.md                  the one-page guide written for them
  canon/setup-progress.md         intake ticked, stage "quick wins"

This script is the one source for the shape of those files; there are no separate templates for them.
`setup-start` updates the "Where you are in setup" section of YOUR-STUDIO.md as the stages pass, and
fills its "What you say" table at "Setup done".
  inbox/                          their uploads, original names, if --inbox is given

It never guesses: a blank answer stays blank. Notion and Figma are optional: a blank answer counts as
wanted, "no" is written as not wanted, and the quick-win skills that build them (setup-figma, setup-notion)
run right after, before any interview. The dashboard app (setup-dashboard) is the studio owner's own path:
it runs only when someone adds `- dashboard: app` under "## Dashboard" in config/tools.md by hand.

No dependencies beyond Python 3. The answers file is a flat YAML: key: value, or key: followed by
"- item" lines. Multi-line text is indented under its key.
"""
import os, re, shutil, subprocess, sys
from datetime import date

# ---------- a small YAML reader for the flat answers file ----------
def read_answers(path):
    data, key, buf, mode = {}, None, [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            if key is not None:
                data[key] = _close(buf, mode)
            key, rest = m.group(1), m.group(2)
            rest = _uncomment(rest)
            if rest in ("", "[]"):
                buf, mode = [], "list" if rest == "[]" else None
                if rest == "[]":
                    data[key] = []; key = None
            else:
                data[key] = _scalar(rest); key = None
            continue
        s = line.strip()
        if s.startswith("- "):
            mode = "list"; buf.append(_scalar(_uncomment(s[2:])))
        else:
            mode = mode or "text"; buf.append(s)
    if key is not None:
        data[key] = _close(buf, mode)
    return data

def _uncomment(s):
    s = s.strip()
    if s and s[0] in "\"'":                 # a quoted value keeps its # signs
        end = s.find(s[0], 1)
        return s if end < 0 else s[:end + 1]
    return re.sub(r"\s+#.*$", "", s).strip()

def _scalar(s):
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s

def _close(buf, mode):
    if mode == "list": return buf
    if mode == "text": return "\n".join(buf)
    return ""

# ---------- helpers ----------
def lst(v):
    if v is None: return []
    if isinstance(v, list): return [x for x in v if str(x).strip()]
    return [v] if str(v).strip() else []

def yn(v):
    return str(v).strip().lower() in ("yes", "y", "true", "sí", "si")

def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    print(f"  wrote {path}")

# Lines the setup skills write after intake (tool IDs, links, connection state). A rebuild keeps them.
KEEP = re.compile(r"^(time zone|scout|librarian|tidy|numbers|calls|calls rule|reading|reading rule|readers|talks|results|dashboard|connected|route|page id|home page|library file|file url|brand applied|design system mode|app id|api url|app url|url|.*database.*)$")

def merge_tools(path, new):
    """Rebuild config/tools.md from intake without losing what setup-figma, setup-notion or setup-dashboard wrote."""
    if not os.path.exists(path):
        return new
    old, sec = {}, None
    for line in open(path, encoding="utf-8").read().splitlines():
        if line.startswith("## "): sec = line; old.setdefault(sec, {}); continue
        m = re.match(r"^- ([^:]+):\s*(.*)$", line)
        if sec and m: old[sec][m.group(1)] = line
    out, sec, seen = [], None, {}
    lines = new.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("## "):
            sec = line; seen[sec] = set()
        m = re.match(r"^- ([^:]+):\s*(.*)$", line)
        if sec and m:
            k = m.group(1); seen[sec].add(k); prev = old.get(sec, {}).get(k)
            if prev and KEEP.match(k) and not re.match(r"^- [^:]+:\s*(not yet|no)\b", prev):
                line = prev
        out.append(line)
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if sec and m and not nxt.startswith("- "):   # end of this section's list
            for k, l in old.get(sec, {}).items():   # lines a skill added that the template doesn't have
                if k not in seen[sec] and KEEP.match(k): out.append(l)
    return "\n".join(out) + "\n"

def merge_guide(path, new):
    """Rebuild YOUR-STUDIO.md from intake but keep what /start wrote: the next step, the ticks on
    the road and any links already in it. Reads guides from before 0.75 too ("Where you are in setup")."""
    if not os.path.exists(path):
        return new
    old = open(path, encoding="utf-8").read()
    m = re.search(r"## (?:Your next step|Where you are in setup)\n.*?(?=\n## |\Z)", old, re.S)
    if m:
        body = re.sub(r"^## [^\n]*\n", "", m.group(0))
        new = re.sub(r"## Your next step\n.*?(?=\n## |\Z)", lambda _: "## Your next step\n" + body, new, flags=re.S)
    # a step marked "(done <date>)" or "(skipped <date>)" keeps its mark on the rebuilt road
    marks = dict(re.findall(r"^- \*\*(.+?)\*\* (\((?:done|skipped)[^)]*\))", old, re.M))
    q = re.search(r"Quick wins done on ([0-9-]+)", old)   # a guide from before 0.75 closed the quick wins in one line
    if q:
        for label in ("The map of your ideas", "Your visual kit", "Your dashboard", "Your libraries", "Your first post"):
            marks.setdefault(label, f"(done {q.group(1)})")
    for label, mark in marks.items():
        new = re.sub(rf"^(- \*\*{re.escape(label)}\*\*) \([^)]*\)", lambda mm: f"{mm.group(1)} {mark}", new, flags=re.M)
    for row in ("Your dashboard", "Your visual kit"):
        r = re.search(rf"^\| {row} \|.*http.*$", old, re.M)
        if r: new = re.sub(rf"^\| {row} \|.*$", lambda _: r.group(0), new, flags=re.M)
    return new

def bullets(items, blank="<none given>"):
    return "\n".join(f"- {i}" for i in items) if items else f"- {blank}"

def label(item):
    """The name part of a list item: before the first ": " or " (", so "LinkedIn: 3k" and "Instagram (I hate it)" both give the channel."""
    return re.split(r":\s|\s\(", str(item), maxsplit=1)[0].strip()

def join(items):
    items = [str(i) for i in items]
    if not items: return ""
    if len(items) == 1: return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]

def sentence(v):
    v = str(v).strip()
    return v if not v or v[-1] in ".!?" else v + "."

def or_blank(v, blank=""):
    v = str(v).strip() if v is not None else ""
    return v if v else blank

# ---------- the fills ----------
def fill(instance, a, studio_dir):
    today = date.today().isoformat()
    name = or_blank(a.get("name"), "<name>")
    phrase = lambda c: re.sub(r"^(A|An|The) ", lambda m: m.group(1).lower() + " ", re.split(r",\s", label(c), maxsplit=1)[0])
    pub = [phrase(c) for c in lst(a.get("publishes_on"))]
    new = [phrase(c) for c in lst(a.get("wants_to_start"))]
    channels = pub + [f"{c} (wants to start)" for c in new]
    if pub and new: publish_line = f"You publish on {join(pub)} and want to start {join(new)}"
    elif pub: publish_line = f"You publish on {join(pub)}"
    elif new: publish_line = f"You don't publish yet and want to start {join(new)}"
    else: publish_line = "You haven't said where you publish"
    if lst(a.get("other_channels")):
        publish_line += f" (you also named {join([phrase(c) for c in lst(a.get('other_channels'))])}, which the studio doesn't write for yet)"
    hours = or_blank(a.get("hours_per_week"))
    # Notion and Figma are optional. A blank answer counts as wanted (the quick win offers it); only "no" turns one off.
    notion = str(a.get("notion") or "").strip().lower() not in ("no", "n", "false")
    figma = str(a.get("figma") or "").strip().lower() not in ("no", "n", "false")

    # config/tools.md
    tools_path = os.path.join(instance, "config/tools.md")
    write(tools_path, merge_tools(tools_path, f"""# Tools

The person's tools. `/start` and the setup skills fill this in; every role reads it to find them. This folder belongs to the person.

## Notion
- connected: no
- wanted: {"yes" if notion else "no"}
- workspace: {or_blank(a.get("notion_workspace"), "<not given>")}
- route: not yet (connector or token; setup-notion sets it)
- page id: not yet (setup-notion fills this and the five database IDs)

## Figma
- connected: no
- wanted: {"yes" if figma else "no"}
- account: {or_blank(a.get("figma_email"), "<not given>")}
- library file: not yet (setup-figma fills this)
- design system mode: not yet (setup-visual-identity fills this)

## Dashboard
- connected: no
- wanted: {"no (the dashboard is in Notion)" if notion else "no (no Notion; /status does the job)"}
- app id: not yet (setup-dashboard fills this)
- api url: not yet
- app url: not yet

## Sources
- calls: not yet (setup-sources fills this: the call recorder, e.g. Granola)
- reading: not yet (setup-sources fills this: Readwise)
- readers: not yet (setup-sources fills this: a Reddit research connector)
- talks: not yet (setup-sources fills this: a YouTube transcript connector)
- results: not yet (setup-sources fills this after the strategy: AuthoredUp or Substack)

## Schedules
- time zone: not yet (setup-schedules asks once)
- tending: not yet (setup-schedules: a weekly tending run, off until they say yes)
- librarian: not yet
- tidy: not yet
- numbers: not yet

## Repo
- url: not yet (the GitHub URL of this instance, so the dashboard can link to piece folders)

## Publishing
- channels: {join(channels) if channels else "<not given>"}
- language: {or_blank(a.get("language"), "the language of their material (not asked at intake)")}

## Team
{bullets(lst(a.get("team")), "<not asked yet: strategy-brand asks>")}
"""))

    # bank/: the working banks sit beside canon/, not inside it (ideas, questions, evidence, rewrites/)
    os.makedirs(os.path.join(instance, "bank/rewrites"), exist_ok=True)

    # canon/strategy/outcomes.md
    write(os.path.join(instance, "canon/strategy/outcomes.md"), f"""---
doc: outcomes
layer: strategy
version: 1
last_reviewed: {today}
owner: {name}
---
# Outcomes

What this person wants to have happened because of their content. Written at intake, in their words. The goal in `vehicle/vehicle.md` refines this once the brand tree reaches it; until then, this is what the studio aims at.

## In a year

status: draft
want: "{or_blank(a.get("goal"), "<not given>")}"
measured by: {or_blank(a.get("measured_by"), "<not asked yet: the vehicle session asks>")}
sources: intake, {today}

## Channels

{bullets(lst(a.get("publishes_on")), "<not given>")}
- wants to start: {join(lst(a.get("wants_to_start"))) or "none"}
- elsewhere, as context (the studio doesn't write for these yet): {join(lst(a.get("other_channels"))) or "<not asked yet: strategy-brand asks>"}{chr(10) + "- links (for people to look at; the studio can't read posts from a link): " + join(lst(a.get("links"))) if lst(a.get("links")) else ""}

## Capacity

- hours a week when work is busy: {hours or "<not given>"}. `strategy-brand` trims the cadence to this.

## Log

- {today} written from intake
""")

    # canon/visual/brand-assets.md
    def refs(items, empty="- <none given>"):
        out = []
        for r in items:
            parts = re.split(r":\s", str(r), maxsplit=1)
            out.append(f"- {parts[0].strip()}: {parts[1].strip()}" if len(parts) == 2 else f"- {r}")
        return "\n".join(out) if out else empty
    write(os.path.join(instance, "canon/visual/brand-assets.md"), f"""---
doc: brand-assets
layer: visual
version: 1
last_reviewed: {today}
owner: {name}
status: draft
---
# Brand assets

What the person gave the studio about their look, from intake. `setup-visual-identity` turns this into the design system (`canon/visual/design-system.md`); until then the designer stops at neutral. Nothing here is a decision yet. Blanks mean they didn't say.

## Given

- logo: {or_blank(a.get("logo"), "none")}
- colors: {", ".join(lst(a.get("colors"))) or "none given"}
- fonts: {", ".join(lst(a.get("fonts"))) or "none given"}

## References they like

{refs(lst(a.get("references_liked")), "- <not asked yet: setup-visual-identity asks>")}

## References they can't stand

{refs(lst(a.get("references_disliked")), "- <not asked yet: setup-visual-identity asks>")}

## Never

- the look should never be: {or_blank(a.get("never_look"), "<not asked yet: setup-visual-identity asks>")}

## Notes from intake

{or_blank(a.get("notes"), "<none>")}

## Log

- {today} written from intake
""")

    # YOUR-STUDIO.md
    team = lst(a.get("team"))
    team_line = ("\n\nWho else touches the content, as you said it:\n" + bullets(team)) if team else ""
    branded = bool(lst(a.get("colors")) or lst(a.get("fonts")) or or_blank(a.get("logo")))
    road = ["- **The map of your ideas** (none of your time while it reads, then a 20-minute review). The studio reads everything you've handed over, public and private, and shows you how your ideas connect: the few claims the rest hangs from, the same idea said many ways, two ideas that make a new one, what you tell clients and never publish. Say \"/map\"."]
    if figma: road.append("- **Your visual kit** (10 minutes). Your own copy of a Figma file with the templates for the pictures in your posts" + (", in your colors and fonts" if branded else "") + ". Say \"set up my Figma\".")
    if notion: road.append("- **Your dashboard** (10 minutes). One page in Notion that shows what's waiting on you and what's in progress. Say \"set up my dashboard\".")
    road.append("- **Your libraries** (10 minutes). The studio came with hundreds of real LinkedIn posts and Substack essays, sorted by what each one does for the reader. It shows you the few that fit what you've already made. Say \"/libraries\".")
    road.append("- **Your first post** (15 minutes). Paste something you've already made (an old post, notes from a talk, a call transcript) or attach the file, and say \"write a post from this\".")
    later = ["- **The interviews** (20 to 30 minutes each, about eleven or twelve over a few weeks). The studio asks about things that happened in your work and finds what you believe in them. Nothing it writes down is used until you say it's right. Say \"start my brand tree\".",
             "- **One page about you** (5 minutes, best after a few interviews). A page to paste at the top of a chat in ChatGPT or any other AI, written from what you've confirmed, so it stops starting from zero. Say \"/about\".",
             "- **Your strategy** (one session). What to be known for, for whom, where and how often, with the reason for each choice. Say \"build my strategy\".",
             "- **Your look** (one session). The studio builds the look of your pictures from what the interviews found. Say \"build my look\".",
             "- **A final check** (20 minutes). One piece goes through every step with your own files, so you see the whole thing work once. Say \"/check\"."]
    road_list = "\n".join(road)
    later_list = "\n".join(later)
    # The course link comes from GUIDE_URL (the environment, as docs/automation.md sets it) or the answers'
    # guide_url; without one, the line that points at the course is left out.
    guide_url = (os.environ.get("GUIDE_URL") or or_blank(a.get("guide_url")) or "").strip()
    course_line = f"\n\nThe course goes deeper on every step: {guide_url}" if guide_url else ""
    measured = or_blank(a.get("measured_by"))
    measured_line = f' How you\'d know it happened: "{sentence(measured)}"' if measured else ""
    guide_path = os.path.join(instance, "YOUR-STUDIO.md")
    write(guide_path, merge_guide(guide_path, f"""# Your studio

This page is your map: the one thing to do next, the whole road, and how to hand the studio what it needs. The studio keeps it up to date. To see it in the chat, say "show my guide".{course_line}

## Your next step

See how your ideas connect. The studio reads everything you've handed over and shows you what it adds up to, then you go through the strongest findings in about 20 minutes. If you haven't handed over your posts, talks or calls yet, do that first: paste them or attach the files. Then say "/map".

## The road

Each step gives you something you can use the same day. You can skip any of them, and the studio tells you what you'd lose. If you're ever unsure what to do, say "/start".

**Today, before any interview:**

{road_list}

**Then, over a few weeks:**

{later_list}

## Handing things over

- **Text** (an old post, notes, a transcript): paste it into the box where you type.
- **A file** (a PDF, a Word document, your logo): drag it into the box where you type and send it. The studio keeps it with your other material. You never need to find or sort anything.
- **Audio or video:** send the transcript instead. Zoom, Otter, Fathom, Descript and YouTube all export one.

## What you can do any time

- "/post" makes a LinkedIn post, and "/essay" a Substack essay, from something you hand over.
- "/capture" saves an idea the moment it happens. Don't tidy it up first.
- "/end" wraps up before you leave, so the next session starts where this one stopped.

The studio saves your work after every reply.

## What you told the studio

{name}. In your words: "{sentence(or_blank(a.get("what_you_do"), "<what you do>"))}" {publish_line}, and you can give this about {hours or "<hours>"} hours a week.{team_line}

What you want a year from now: "{sentence(or_blank(a.get("goal"), "<goal>"))}"{measured_line}

To change an answer, say "set up my studio".

## Your links

| | |
| --- | --- |
| Your dashboard | {"your Notion dashboard; the link lands here when it's set up" if notion else "\"/status\" in the chat shows what's waiting on you (say so if you want a Notion dashboard later)"} |
| Your visual kit | {"your Figma visual kit; the link lands here when it's set up" if figma else "the studio describes your pictures in words (say so if you want a Figma kit later)"} |

## Once you're set up

You don't need this part yet. When setup is done, this is your week:

- Whenever something happens worth saying (a client result, a conversation, an opinion): "/capture". Two minutes.
- Once a week: one session to make what's next, then "/status" to decide on what's waiting. About two hours a week in all.
- When the studio suggests a change to what it knows about you, it waits for your yes. "/status" shows those too.
- It never publishes anything. You do.
"""))

    # canon/setup-progress.md
    goal1 = or_blank(a.get("goal")).split("\n")[0]
    first = goal1 if len(goal1) <= 160 else goal1[:160].rsplit(" ", 1)[0] + "..."
    sp_path = os.path.join(instance, "canon/setup-progress.md")
    if os.path.exists(sp_path):   # a rebuild after intake changes keeps progress, ticks and skips
        open(sp_path, "a", encoding="utf-8").write(f"- {today}: intake answers changed; guide and settings rebuilt from them\n")
        print(f"  kept {sp_path} (progress), added a log line")
        return
    write(sp_path, f"""---
doc: setup-progress
owner: {name}
started: {today}
last_session: {today}
stage: quick wins
---
# Setup progress

Where this person is in setting up the studio. `setup-start` reads and updates this file. Stages, in order: intake, quick wins, interviews skipped, brand tree not started, brand tree in progress, strategy, make it yours, check, setup done. A quick win marked "skipped" counts as done.

## Quick wins (before the interviews)

- [x] Intake: outcomes, channels, tools and brand assets recorded ({"form" if a.get("built_by") == "form" else "setup-intake"})
- [ ] The map of your ideas
{"- [ ] Visual kit in Figma" if figma else "- Visual kit in Figma: not wanted"}
{"- [ ] Dashboard in Notion" if notion else "- Dashboard in Notion: not wanted"}
- [ ] The libraries
- [ ] First post from their own material

## The interviews and after

- [ ] Brand tree at minimum canon (see `canon/progress.md`)
- [ ] Strategy confirmed (`canon/strategy/brand-strategy.md`)
- [ ] Make it yours: visual identity applied
- [ ] Check passed (`/check`): install and one test piece through the crew

## Log

- {today}: intake done. Goal, as said: "{first or "<goal>"}"
""")

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    answers_path = args[0]
    opt = {args[i]: args[i + 1] for i in range(1, len(args) - 1) if args[i].startswith("--") and not args[i + 1].startswith("--")}
    fill_only = "--fill" in args

    a = read_answers(answers_path)
    for req in ("name", "what_you_do", "goal", "hours_per_week"):
        if not lst(a.get(req)) and not or_blank(a.get(req)):
            print(f"  note: required answer '{req}' is blank; the instance will say so")

    if fill_only:
        instance = os.getcwd()
        studio_dir = None
        a.setdefault("built_by", "setup-intake")
    else:
        studio_dir = opt.get("--studio"); instance = opt.get("--out")
        if not studio_dir or not instance:
            print("need --studio PATH and --out PATH (or --fill inside an instance)"); sys.exit(2)
        a.setdefault("built_by", "form")
        if not os.path.exists(os.path.join(instance, "studio.manifest.yaml")):
            print(f"Creating the instance at {instance}")
            subprocess.run(["bash", os.path.join(studio_dir, "scripts/update-studio.sh"), studio_dir, "--init", instance], check=True)
    if not a.get("built_by"): a["built_by"] = "form"
    a["intake_date"] = date.today().isoformat()

    # keep the answers as the record
    rec = os.path.join(instance, "config/intake.yaml")
    os.makedirs(os.path.dirname(rec), exist_ok=True)
    src = open(answers_path, encoding="utf-8").read()
    src = re.sub(r"^intake_date:.*$", f"intake_date: \"{a['intake_date']}\"", src, flags=re.M)
    src = re.sub(r"^built_by:.*$", f"built_by: \"{a['built_by']}\"", src, flags=re.M)
    open(rec, "w", encoding="utf-8").write(src); print(f"  wrote {rec}")

    # uploads into inbox/
    inbox_src = opt.get("--inbox")
    if inbox_src and os.path.isdir(inbox_src):
        dst = os.path.join(instance, "inbox")
        os.makedirs(dst, exist_ok=True)
        n = 0
        for f in os.listdir(inbox_src):
            if f.startswith("."): continue
            s = os.path.join(inbox_src, f)
            (shutil.copytree if os.path.isdir(s) else shutil.copy2)(s, os.path.join(dst, f))
            n += 1
        print(f"  copied {n} upload(s) into inbox/")

    print("Filling the person's files")
    fill(instance, a, studio_dir)

    todo = ["The map of their ideas: job-map (\"/map\"), from everything in material/ and inbox/"]
    wanted = lambda k: str(a.get(k) or "").strip().lower() not in ("no", "n", "false")   # blank counts as wanted, as in fill()
    if wanted("figma"): todo.append("Visual kit: setup-figma (they duplicate the master; the studio connects it and applies their brand)")
    if wanted("notion"): todo.append("Dashboard: setup-notion")
    todo.append("The libraries: setup-libraries (\"/libraries\"), the moves their material can carry")
    todo.append("First post: setup-first-post, from anything in inbox/")
    print("\nDone. The quick wins, before any interview:\n  - " + "\n  - ".join(todo))
    if not fill_only: print("Then: open the instance in Claude Code and say /start.")

if __name__ == "__main__":
    main()
