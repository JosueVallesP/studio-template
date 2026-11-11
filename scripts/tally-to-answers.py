#!/usr/bin/env python3
"""Turns one Tally submission into the intake answers file that scripts/build-instance.py reads.

  python3 scripts/tally-to-answers.py export.csv  --out answers.yaml [--row N | --email a@b.com] [--uploads DIR]
  python3 scripts/tally-to-answers.py webhook.json --out answers.yaml [--uploads DIR]

Input is either the CSV you download from Tally (Results, Download) or the JSON body Tally sends to a
webhook (one submission). With a CSV, the last row is used unless --row (1 = first submission) or
--email picks one.

The form is described in docs/tally-form.md. Questions are matched by the start of their title, so
small edits to the help text don't matter, but keep the titles as written there.

--uploads DIR downloads every uploaded file into DIR with its original name; build-instance.py
--inbox DIR then copies them into the person's inbox/. Without --uploads the links are listed in the
answers file under "uploads" and nothing is downloaded.

No dependencies beyond Python 3. It never guesses: an empty answer stays empty.
"""
import csv, json, os, re, sys, urllib.request

# Question titles on the form (docs/tally-form.md), lowercased, matched with startswith.
QUESTIONS = [
    ("name", "your name"),
    ("email", "your email"),
    ("language", "what language"),
    ("what_you_do", "what do you do"),
    ("business", "your business name"),
    ("goal", "a year from now"),
    ("measured_by", "how would you know"),
    ("publishes_on", "where do you publish"),
    ("wants_to_start", "anywhere you want to start"),
    ("hours_per_week", "about how many hours"),
    ("linkedin_status", "linkedin:"),
    ("substack_status", "substack:"),
    ("other_channels", "anywhere else you publish"),
    ("links", "your links"),
    ("material_files", "upload what you've already written"),
    ("recording_files", "upload transcripts"),
    ("material", "anything you've made that you can't upload"),
    ("team", "does anyone else touch"),
    ("material", "what have you already made"),
    ("material_files", "upload what you've made"),
    ("recordings", "do you have recordings"),
    ("recording_files", "upload recordings"),
    ("figma", "do you use figma"),
    ("figma_email", "your figma email"),
    ("notion", "do you use notion"),
    ("notion_workspace", "your notion workspace"),
    ("logo", "upload your logo"),
    ("colors", "your brand colors"),
    ("fonts", "your brand fonts"),
    ("references_liked", "three things whose look you like"),
    ("references_disliked", "three things whose look you can't stand"),
    ("never_look", "one word your look should never be"),
    ("notes", "anything the studio should know"),
    ("github", "your github username"),
]
LISTS = {"publishes_on", "wants_to_start", "other_channels", "links", "team", "material", "recordings", "colors", "fonts", "references_liked", "references_disliked"}
FILES = {"material_files", "recording_files", "logo"}
ORDER = ["name", "email", "github", "what_you_do", "business", "location", "language", "goal", "measured_by", "publishes_on",
         "wants_to_start", "other_channels", "links", "hours_per_week", "team", "material", "recordings", "notion", "notion_workspace", "figma", "figma_email",
         "logo", "colors", "fonts", "references_liked", "references_disliked", "never_look", "notes"]


def key_for(title):
    t = re.sub(r"\s+", " ", (title or "").strip().lower()).replace("’", "'")
    for key, start in QUESTIONS:
        if t.startswith(start):
            return key
    return None


def split_lines(v):
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip(" -•\t") for x in re.split(r"[\r\n]+", str(v or "")) if x.strip(" -•\t")]


def from_csv(path, row=None, email=None):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("tally: the CSV has no submissions")
    if email:
        pick = [r for r in rows if any(email.lower() == str(v).strip().lower() for v in r.values())]
        if not pick:
            sys.exit(f"tally: no submission with the email {email}")
        r = pick[-1]
    else:
        r = rows[(row - 1) if row else -1]
    out, files = {}, {}
    for title, value in r.items():
        k = key_for(title)
        if not k:
            continue
        if k in FILES:
            # Tally writes uploaded files as their URLs, separated by commas or new lines.
            files[k] = [u for u in re.split(r"[\s,]+", value or "") if u.startswith("http")]
        else:
            out[k] = value or ""
    return out, files


def from_webhook(path):
    body = json.load(open(path, encoding="utf-8"))
    fields = (body.get("data") or body).get("fields", [])
    out, files = {}, {}
    for f in fields:
        k = key_for(f.get("label"))
        if not k:
            continue
        v, kind = f.get("value"), f.get("type", "")
        if isinstance(v, list) and v and all(isinstance(x, dict) and x.get("url") for x in v):
            kind = "FILE_UPLOAD"   # the API doesn't always say; a list of {url} is a file answer
        if isinstance(v, dict):
            v = v.get("text") or v.get("value") or json.dumps(v, ensure_ascii=False)
        if kind == "FILE_UPLOAD":
            files[k] = [x.get("url") for x in (v or []) if isinstance(x, dict) and x.get("url")]
            continue
        if isinstance(v, list) and all(isinstance(x, str) for x in v) and (kind in ("MULTIPLE_CHOICE", "CHECKBOXES", "CHECKBOX", "DROPDOWN", "MULTI_SELECT") or f.get("options")):
            names = {o.get("id"): o.get("text") for o in f.get("options", [])}
            v = [names.get(x, x) for x in v]
            v = v[0] if kind in ("MULTIPLE_CHOICE", "DROPDOWN") and len(v) == 1 else v
        out[k] = v if v is not None else ""
    return out, files


def yes_no(v):
    s = str(v or "").strip().lower()
    if s.startswith(("yes", "sí", "si")):
        return "yes"
    if s.startswith("no"):
        return "no"
    return s


def q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def channels_from_status(a):
    """The form asks "LinkedIn: where are you now?" and the same for Substack. Turn the two answers into the
    lists the build reads: where they publish now, and where they want to start."""
    now, start = split_lines(a.get("publishes_on")), split_lines(a.get("wants_to_start"))
    for key, name in (("linkedin_status", "LinkedIn"), ("substack_status", "Substack")):
        v = a.get(key)
        v = (v[0] if isinstance(v, list) and v else v) or ""
        v = str(v).lower()
        if "now" in v and name not in now: now.append(name)
        elif "start" in v and name not in start: start.append(name)
    a["publishes_on"], a["wants_to_start"] = now, start
    if isinstance(a.get("hours_per_week"), list):
        a["hours_per_week"] = a["hours_per_week"][0] if a["hours_per_week"] else ""
    return a


def write_answers(a, files, path):
    lines = ["# Intake answers, converted from a Tally submission by scripts/tally-to-answers.py.",
             "# scripts/build-instance.py reads this file. A blank value stays blank in the instance.", ""]
    for k in ORDER:
        if k in LISTS:
            items = split_lines(a.get(k))
            lines.append(f"{k}:" + ("" if items else " []"))
            lines += [f"  - {q(i)}" for i in items]
        elif k == "logo":
            names = [os.path.basename(u.split("?")[0]) for u in files.get("logo", [])]
            lines.append(f"logo: {q(names[0]) if names else q(a.get('logo', ''))}")
        else:
            v = a.get(k, "")
            if k in ("notion", "figma"):
                v = yes_no(v)   # optional; blank (the form doesn't ask) counts as wanted in build-instance.py
            v = str(v).strip()
            if "\n" in v:
                lines.append(f"{k}:")
                lines += ["  " + x for x in v.splitlines() if x.strip()]
            else:
                lines.append(f"{k}: {q(v)}")
    links = [u for k in ("logo", "material_files", "recording_files") for u in files.get(k, [])]
    lines.append("uploads:" + ("" if links else " []"))
    lines += [f"  - {q(u)}" for u in links]
    lines += ["", "# Filled by the build, not the form:", 'intake_date: ""', 'built_by: "form"', ""]
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def download(files, folder):
    os.makedirs(folder, exist_ok=True)
    got = []
    for k, urls in files.items():
        for u in urls:
            name = os.path.basename(u.split("?")[0]) or "upload"
            dest = os.path.join(folder, name)
            try:
                with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (content-studio)"}), timeout=120) as r, open(dest, "wb") as f:
                    f.write(r.read())
                got.append(name)
            except Exception as e:  # keep going; the link stays in the answers file
                print(f"  could not download {u}: {e}")
    return got


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    src = args[0]
    opt = {args[i]: args[i + 1] for i in range(1, len(args) - 1) if args[i].startswith("--")}
    out = opt.get("--out", "answers.yaml")
    if src.lower().endswith(".json"):
        a, files = from_webhook(src)
    else:
        a, files = from_csv(src, int(opt["--row"]) if "--row" in opt else None, opt.get("--email"))
    a = channels_from_status(a)
    missing = [k for k in ("name", "what_you_do", "goal", "hours_per_week") if not str(a.get(k, "")).strip()]
    if not a["publishes_on"] and not a["wants_to_start"]: missing.append("a channel (LinkedIn or Substack)")
    write_answers(a, files, out)
    print(f"  wrote {out}" + (f" (blank required answers: {', '.join(missing)})" if missing else ""))
    if "--uploads" in opt and any(files.values()):
        got = download(files, opt["--uploads"])
        print(f"  downloaded {len(got)} upload(s) into {opt['--uploads']}")
    if not a.get("github"):
        print("  note: no GitHub username in the submission; make-client.sh will create the repo without an invite")


if __name__ == "__main__":
    main()
