#!/usr/bin/env python3
"""Check that a house rule the person breaks in their own writing can become their exception, and only
up to their own rate.

Builds a small instance in a temp folder: six pieces by one writer, each with one "it's not about X,
it's about Y" line (H17), and six pieces by other writers who never write it. Then:
  - `voiceprint.py profile` lists H17 under "Rules you break yourself", in profile.json and in
    voice-targets.md, with a quote from their pieces
  - with "- rule H17: ..." in the voice guide's House-rule exceptions, house_check returns that H17 as
    a flag marked as their own pattern, not a fail; "- H17 (rule): ..." works the same way
  - without it, the same line still fails
  - a phrase exception still lets its phrase through, as before, and leaves the rest of the rules alone
  - check-prose.py, which reads the exceptions through the voice guide, exits 0 on the line with the
    exception and 1 without it
  - a draft with three H17 lines, where the writer averages one a piece, is listed in "Above your own
    rate"; a draft with one is not

  python3 -I tests/studio/voiceprint/own_rules.py
"""

import json
import os
import subprocess
import sys
import tempfile

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SCRIPTS = os.path.join(REPO, "scripts")
sys.path.insert(0, SCRIPTS)
import studio_checks as sc  # noqa: E402

VOICEPRINT = os.path.join(SCRIPTS, "voiceprint.py")
PROSE = os.path.join(SCRIPTS, "check-prose.py")

CONTRASTS = [
    "It's not about the price, it's about the fear of choosing wrong.",
    "It's not about posting more, it's about having something to say.",
    "It's not about the logo, it's about what people repeat when you leave the room.",
    "It's not about the framework, it's about the twenty years behind it.",
    "It's not about reach, it's about who reads you twice.",
    "It's not about the headline, it's about the one idea under it.",
    "It's not about the tool, it's about the habit the tool supports.",
    "It's not about volume, it's about the second conversation.",
    "It's not about being liked, it's about being trusted with the hard question.",
]
FILLER = [
    "I spent the morning with a client who had rewritten her offer six times.",
    "She kept adding features because she thought the price needed defending.",
    "We cut the page down to the three things her buyers asked about on calls.",
    "The calls had the answers the whole time, and she had stopped listening to them.",
    "I keep a notebook of what people ask me twice, because that is the content.",
    "Last spring I ran a workshop where nobody asked a single question for an hour.",
    "Then one person asked how to price a service that has no clear result.",
    "That question became four essays and a small product.",
    "I would rather post twice a week with something true than every day with filler.",
    "The people I work with have spent decades on one subject.",
    "They have more to say than they think, and less time than they need.",
    "My best posts came from things I got wrong in front of a client.",
]
OTHERS = [
    "Growth on social platforms comes down to consistency and volume over time.",
    "Post every day, test every format, and double down on whatever performs.",
    "The algorithm rewards early engagement in the first hour after publishing.",
    "Use a strong hook in the first line so readers stop scrolling.",
    "Carousels tend to get more saves than plain text posts.",
    "Repurpose every long video into ten short clips for each channel.",
    "Track impressions, followers and profile views every single week.",
    "A content calendar keeps a team aligned across several channels.",
    "Batch your writing on Mondays and schedule the whole week in advance.",
    "Short sentences are easier to read on a phone screen.",
    "The newsletter is the only channel where you own the relationship.",
    "Templates save time once you know which formats your audience likes.",
]
LINE = "Clients ask me about pricing all the time. It's not about the price, it's about the fear of choosing wrong.\n"


def piece(i, contrasts):
    sents = [FILLER[(i + k) % len(FILLER)] for k in range(9)]
    for j, c in enumerate(contrasts):
        sents[1 + 3 * j] = c
    return "\n\n".join(" ".join(sents[k:k + 3]) for k in range(0, 9, 3)) + "\n"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def guide(root, lines):
    write(os.path.join(root, "canon", "voice", "voice-guide.md"),
          "# Voice guide\n\n## House-rule exceptions\n" + "".join(l + "\n" for l in lines) + "\n## Approved samples\n")


def main():
    fails = []

    def check(ok, what):
        print(("pass  " if ok else "FAIL  ") + what)
        if not ok:
            fails.append(what)

    with tempfile.TemporaryDirectory() as root:
        mine, others = os.path.join(root, "material"), os.path.join(root, "others")
        for i in range(6):
            write(os.path.join(mine, f"post-{i}.md"), piece(i, [CONTRASTS[i]]))
            write(os.path.join(others, f"other-{i}.md"),
                  "\n\n".join(" ".join(OTHERS[(i + k) % 12] for k in range(j, j + 3)) for j in (0, 3, 6)) + "\n")
        prof, targets = os.path.join(root, "profile.json"), os.path.join(root, "voice-targets.md")

        # 1. The profile finds the rule they break
        p = subprocess.run([sys.executable, "-I", VOICEPRINT, "profile", "--mine", mine, "--others", others,
                            "--rewrites", "", "--out", prof, "--targets", targets], capture_output=True, text=True)
        check(p.returncode == 0, f"profile exits 0 {p.stderr.strip()[:200]}")
        data = json.load(open(prof, encoding="utf-8")) if p.returncode == 0 else {}
        h = data.get("house_rules", {})
        h17 = h.get("rules", {}).get("H17", {})
        check("H17" in h.get("break_yourself", []), "profile.json lists H17 under the rules they break")
        check(h17.get("pieces_using") == 6 and h17.get("share") == 1.0 and h17.get("per_1000", 0) > 0,
              f"H17 counted in all six pieces with a rate ({h17.get('pieces_using')}, {h17.get('per_1000')} per 1,000)")
        check(h17.get("check") == "fail", "H17 recorded as a rule the scripts fail")
        check(2 <= len(h17.get("quotes", [])) <= 3 and all("it's about" in q["text"] for q in h17.get("quotes", [])),
              "two or three quotes from their pieces")
        md = open(targets, encoding="utf-8").read() if os.path.exists(targets) else ""
        sect = md.split("## Rules you break yourself", 1)[1].split("\n## ", 1)[0] if "## Rules you break yourself" in md else ""
        check("**H17," in sect and "it's not about" in sect.lower(), "voice-targets.md shows H17 with a quote")
        check("—" not in sect, "the section has no em dash")

        # 2. A rule exception turns the fail into a flag
        guide(root, ['- rule H17: "It\'s not about the price, it\'s about the fear of choosing wrong." (material/post-0.md)'])
        allow = sc.exceptions(root)
        check("rule:h17" in allow, f"exceptions() reads the rule line ({sorted(allow)})")
        f, fl = sc.house_check(LINE, allow=allow)
        check(not [x for x in f if x[0].startswith("H17")], "with the rule exception, H17 doesn't fail")
        check(any(x[0].startswith("H17") and "your own pattern" in x[0] for x in fl),
              "with the rule exception, H17 comes back as a flag marked as their own pattern")
        f2, _ = sc.house_check(LINE + "It was a hard week — and a good one.\n", allow=allow)
        check(any(x[0].startswith("H16") for x in f2), "the rule exception leaves other rules failing (H16)")

        guide(root, ['- H17 (rule): "It\'s not about reach, it\'s about who reads you twice." (material/post-4.md)'])
        check("rule:h17" in sc.exceptions(root), "the \"H17 (rule)\" form reads the same way")

        # 3. Without it, still a fail
        guide(root, [])
        f, _ = sc.house_check(LINE, allow=sc.exceptions(root))
        check(any(x[0].startswith("H17") for x in f), "without the exception, H17 still fails")

        # 4. Phrase exceptions work as before
        guide(root, ['- game-changer: "That client was a game-changer for me." (material/post-2.md)'])
        allow = sc.exceptions(root)
        check(allow == {"game-changer"}, f"a phrase line still reads as a phrase ({sorted(allow)})")
        _, fl = sc.house_check("I think that call was a game-changer for the business.", allow=allow)
        check(not [x for x in fl if x[1].lower() == "game-changer"], "the phrase exception lets its phrase through")
        f, _ = sc.house_check(LINE, allow=allow)
        check(any(x[0].startswith("H17") for x in f), "a phrase exception doesn't touch H17")

        # 5. check-prose, through the voice guide
        draft = os.path.join(root, "note.md")
        write(draft, LINE)
        vg = os.path.join(root, "canon", "voice", "voice-guide.md")
        guide(root, ['- rule H17: "It\'s not about the price, it\'s about the fear of choosing wrong." (material/post-0.md)'])
        r1 = subprocess.run([sys.executable, "-I", PROSE, draft, "--voice", vg], capture_output=True, text=True)
        guide(root, [])
        r2 = subprocess.run([sys.executable, "-I", PROSE, draft, "--voice", vg], capture_output=True, text=True)
        check(r1.returncode == 0 and r2.returncode == 1,
              f"check-prose exits 0 with the exception and 1 without (got {r1.returncode}, {r2.returncode})")

        # 6. Above your own rate holds the draft to their rate
        heavy, normal = os.path.join(root, "draft-heavy.md"), os.path.join(root, "draft-normal.md")
        write(heavy, piece(2, CONTRASTS[6:9]))
        write(normal, piece(3, [CONTRASTS[7]]))

        def above(path):
            r = subprocess.run([sys.executable, "-I", VOICEPRINT, "score", path, "--mine", mine, "--others", others,
                                "--rewrites", "", "--no-impostors", "--json", "--log", ""], capture_output=True, text=True)
            return r.returncode, (json.loads(r.stdout).get("above_own_rate", {}) if r.returncode == 0 else {}), r.stderr

        code, ab, err = above(heavy)
        check(code == 0, f"heavy draft exits 0 {err.strip()[:200]}")
        hit = [x for x in ab.get("lines", []) if x["kind"] == "house pattern" and x["what"] == "H17"]
        check(bool(hit) and hit[0]["draft_count"] == 3 and hit[0]["draft"] > hit[0]["yours_p85"] > 0,
              f"three H17 lines, where they use one, are above their rate ({hit[0] if hit else ab.get('lines')})")
        code, ab, _ = above(normal)
        check(code == 0 and not [x for x in ab.get("lines", []) if x["kind"] == "house pattern"],
              "one H17 line, at their rate, is not listed")
        rep = subprocess.run([sys.executable, "-I", VOICEPRINT, "score", heavy, "--mine", mine, "--others", others,
                              "--rewrites", "", "--no-impostors", "--log", ""], capture_output=True, text=True).stdout
        check("**H17," in rep.split("## Above your own rate", 1)[-1], "the report shows the H17 line")

    print("own_rules: " + ("FAIL (" + "; ".join(fails) + ")" if fails else "pass"))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
