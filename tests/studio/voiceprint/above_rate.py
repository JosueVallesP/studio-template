#!/usr/bin/env python3
"""Check the "Above your own rate" reading in `voiceprint.py score`.

Builds a small corpus in a temp folder: six pieces by one writer, each using the
marker word "frankly" once, and six pieces by other writers who never use it. Then:
  - a draft that says "frankly" five times is flagged, with both rates given
  - a draft that says it once, as the writer does, is not flagged
  - with only four pieces the section says it can't be read yet
  - the exit code is 0 every time: the reading never fails a draft

  python3 -I tests/studio/voiceprint/above_rate.py
"""

import json
import os
import random
import subprocess
import sys
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SCRIPT = os.path.join(REPO, "scripts", "voiceprint.py")
MARKER = "frankly"

MINE = [
    "I spent the morning with a client who had rewritten her offer six times.",
    "She kept adding features because she thought the price needed defending.",
    "We cut the page down to the three things her buyers asked about on calls.",
    "The calls had the answers the whole time, and she had stopped listening to them.",
    "I think most of my work is helping people hear what they already said.",
    "When I write, I start from a story that happened to me that week.",
    "My best posts came from things I got wrong in front of a client.",
    "I keep a notebook of what people ask me twice, because that is the content.",
    "It took me years to stop writing for other writers and start writing for buyers.",
    "Last spring I ran a workshop where nobody asked a single question for an hour.",
    "Then one person asked how to price a service that has no clear result.",
    "That question became four essays and a small product.",
    "I don't plan a calendar, because I can't predict what will happen to me.",
    "I would rather post twice a week with something true than every day with filler.",
    "The people I work with have spent decades on one subject.",
    "They have more to say than they think, and less time than they need.",
]
OTHERS = [
    "Growth on social platforms comes down to consistency and volume over time.",
    "Post every day, test every format, and double down on whatever performs.",
    "The algorithm rewards early engagement in the first hour after publishing.",
    "Use a strong hook in the first line so readers stop scrolling.",
    "Carousels tend to get more saves than plain text posts.",
    "Repurpose every long video into ten short clips for each channel.",
    "Track impressions, followers and profile views every single week.",
    "Engagement pods were popular for a while before the platforms caught on.",
    "A content calendar keeps a team aligned across several channels.",
    "Batch your writing on Mondays and schedule the whole week in advance.",
    "Short sentences are easier to read on a phone screen.",
    "Comment on ten big accounts a day to borrow their audience.",
    "The newsletter is the only channel where you own the relationship.",
    "Brands that publish more often build awareness faster than brands that wait.",
    "Analytics dashboards show which topics bring in new followers.",
    "Templates save time once you know which formats your audience likes.",
]


def piece(rng, pool, n=9, marker_uses=0):
    sents = rng.sample(pool, n)
    for i in range(marker_uses):
        k = rng.randrange(len(sents))
        s = sents[k]
        sents[k] = f"{MARKER.capitalize()}, {s[0].lower()}{s[1:]}"
    # three paragraphs of three sentences, as a post would run
    return "\n\n".join(" ".join(sents[i:i + 3]) for i in range(0, len(sents), 3)) + "\n"


def write(folder, name, text):
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, name), "w", encoding="utf-8") as f:
        f.write(text)


def score(root, draft):
    p = subprocess.run([sys.executable, "-I", SCRIPT, "score", draft, "--mine", os.path.join(root, "mine"),
                        "--others", os.path.join(root, "others"), "--rewrites", "", "--no-impostors",
                        "--json", "--log", ""], capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def report(root, draft):
    p = subprocess.run([sys.executable, "-I", SCRIPT, "score", draft, "--mine", os.path.join(root, "mine"),
                        "--others", os.path.join(root, "others"), "--rewrites", "", "--no-impostors",
                        "--log", ""], capture_output=True, text=True)
    return p.stdout


def main():
    rng = random.Random(3)
    fails = []

    def check(ok, what):
        print(("pass  " if ok else "FAIL  ") + what)
        if not ok:
            fails.append(what)

    with tempfile.TemporaryDirectory() as root:
        for i in range(6):
            write(os.path.join(root, "mine"), f"post-{i}.md", piece(rng, MINE, marker_uses=1))
            write(os.path.join(root, "others"), f"other-{i}.md", piece(rng, OTHERS))
        heavy = os.path.join(root, "draft-heavy.md")
        write(root, "draft-heavy.md", piece(rng, MINE, n=12, marker_uses=5))
        normal = os.path.join(root, "draft-normal.md")
        write(root, "draft-normal.md", piece(rng, MINE, marker_uses=1))

        code, out, err = score(root, heavy)
        check(code == 0, f"heavy draft exits 0 (got {code}) {err.strip()[:200]}")
        r = json.loads(out) if code == 0 else {}
        ab = r.get("above_own_rate", {})
        check(ab.get("read") is True, "section is read with six pieces")
        hit = [x for x in ab.get("lines", []) if x["kind"] == "marker word" and x["what"] == MARKER]
        check(bool(hit), f"'{MARKER}' five times is flagged above the writer's rate")
        if hit:
            x = hit[0]
            check(x["draft_count"] == 5 and x["draft"] > x["yours_p85"] > 0 and x["yours_median"] > 0,
                  f"the line gives both numbers (draft {x['draft']}, yours {x['yours_median']}, p85 {x['yours_p85']})")
        check("close" in ab and ab["close"]["draft"] in ("question", "short line", "longer sentence"),
              "the close is read")
        text = report(root, heavy)
        check("## Above your own rate" in text and f'"{MARKER}"' in text, "the report shows the section")

        code, out, _ = score(root, normal)
        check(code == 0, "normal draft exits 0")
        ab = json.loads(out).get("above_own_rate", {}) if code == 0 else {}
        check(ab.get("read") is True and not [x for x in ab.get("lines", []) if x["what"] == MARKER],
              f"'{MARKER}' once, at the writer's rate, is not flagged")

        for i in (4, 5):
            os.remove(os.path.join(root, "mine", f"post-{i}.md"))
        code, out, _ = score(root, heavy)
        ab = json.loads(out).get("above_own_rate", {}) if code == 0 else {}
        check(code == 0 and ab.get("read") is False and "reason" in ab, "four pieces: the section can't be read yet")
        check("can't be read yet" in report(root, heavy), "the report says so")

    print("above_rate: " + ("FAIL (" + "; ".join(fails) + ")" if fails else "pass"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
