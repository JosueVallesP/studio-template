#!/usr/bin/env python3
"""The house rules, checked on any text: a piece, a canon page, a handback, or the studio's own reply.
The rules live in skills/craft-house-rules/SKILL.md; the lists live in studio_checks.py. This script is
the mechanical half. It never judges voice: a match inside a quoted line (> ...), a code fence, a table
or a source map doesn't count, because those hold the person's or a source's words.

Usage:
  python3 scripts/check-prose.py <file> [--mode piece|prose|reply] [--json] [--voice canon/voice/voice-guide.md]
  cat text.md | python3 scripts/check-prose.py --stdin --mode reply

Modes:
  piece   a draft in pieces/: measures the ## Post section only (each of Posts A, B, C on its own; --draft A for one) (default when the path matches pieces/*/draft-*.md)
  prose   any other person-facing file (the default otherwise)
  reply   the studio's own message to the person: Part 1 plus the Part 2 openers, narration and labels

Output: FAILS (exit 1) and FLAGS (exit 0). A fail is a rule a script can decide. A flag is evidence for the judge.

--voice: a voice guide whose "Phrases they use" and approved samples make a phrase the person's own.
Any flagged or failed phrase that appears in those lines is dropped (the exception principle).
"""
import json, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

MAX_FAILS_SHOWN = 12

# Fields in the canon templates (skills/setup-brand-tree/templates/person, strategy, voice) whose value is
# the person's own words, confirmed by them: a belief's claim, ground and condition, a behavior, a stop-list
# item, a voice rule and its before/after lines, the audience's words. The house rules don't apply to the
# person's words (the exception principle), so these lines are skipped outside piece mode.
PERSON_WORDS = re.compile(r"^\s*(?:[-*+]\s+)?(?:claim|ground|condition|rejects|falsifier|behavior|item|why|story|cost|"
                          r"catalyst_story|rule|before|after|their_words|quotes|language_bank|emotional_words|"
                          r"struggling_moment|tried|believes|wants)\s*:", re.I)

def strip_for_prose(text, mode):
    """Keep only the lines the studio wrote as prose."""
    if mode == "piece":
        post = sc.post_section(text)   # one of Posts A, B, C when the file holds three
        if post is not None: text = post
    text = re.sub(r"^---\n.*?\n---\s*", "", text, flags=re.S)            # frontmatter
    text = re.sub(r"```.*?```", "", text, flags=re.S)                    # code fences
    text = re.sub(r"^(PARTS MAP|SOURCE MAP|Source map|ARGUMENT CHECK|BRIEF DEFECTS)[\s\S]*?(?=^## |\Z)", "", text, flags=re.M)
    lines = []
    for ln in text.splitlines():
        s = ln.strip()
        if s.startswith(">"): continue                                   # quotes: the person's or a source's words
        if s.startswith("|"): continue                                   # tables
        if re.match(r"^\s*(?:[-*+]\s+)?\[?[A-Z]\d+\]?[\s·:]", s): continue  # ID lines in canon drafts
        if re.match(r"^\s*(?:source|sources|log|status|id|type|date|permission|links|who_said_it|expiry|raw|quote)\s*:", s, re.I): continue
        if mode != "piece" and PERSON_WORDS.match(s): continue            # a canon field that holds what the person said
        lines.append(ln)
    return "\n".join(lines)

def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

def sentences(par):
    par = re.sub(r"^#+\s*", "", par, flags=re.M)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", par) if s.strip()]

def own_phrases(voice_path):
    """The person's own uses the rules let through: studio_checks.exceptions reads the voice guide's
    "## House-rule exceptions" section and its "Phrases he uses" line."""
    if not voice_path or not os.path.exists(voice_path): return set()
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(voice_path))))
    return sc.exceptions(root)

def find_all(rx, text):
    return [(m.start(), m.group(0)) for m in rx.finditer(text)]

def line_of(text, pos):
    return text.count("\n", 0, pos) + 1

def excerpt(text, pos, width=70):
    a = max(0, pos - 25); b = min(len(text), pos + width)
    return re.sub(r"\s+", " ", text[a:b]).strip()

def main():
    sc.per_draft(__file__)
    args = sys.argv[1:]
    as_json = "--json" in args
    mode = None
    voice = None
    if "--mode" in args: mode = args[args.index("--mode") + 1]
    if "--voice" in args: voice = args[args.index("--voice") + 1]
    if "--stdin" in args:
        raw = sys.stdin.read(); path = "<stdin>"
    else:
        files = [a for a in args if not a.startswith("--") and a not in (mode, voice)]
        if not files: print(__doc__); sys.exit(2)
        path = files[0]; raw = open(path, encoding="utf-8").read()
    if mode is None:
        mode = "piece" if re.search(r"(^|/)pieces/[^/]+/draft-v\d+\.md$", path) else "prose"
    if voice is None and os.path.exists("canon/voice/voice-guide.md"): voice = "canon/voice/voice-guide.md"
    own_list = own_phrases(voice)
    own = " ".join(own_list)

    text = strip_for_prose(raw, mode)
    low = text.lower().replace("’", "'")
    fails, flags = [], []

    def hit(kind, rule, label, pos, word=None):
        if word and own and word.lower().replace("’", "'") in own: return   # the person's own phrase
        (fails if kind == "fail" else flags).append({"rule": rule, "what": label, "line": line_of(text, pos), "text": excerpt(text, pos)})

    # ---- Part 1 and Part 2, the rules a script can decide (one shared function) -----------------
    allow = set(own_list)
    f_hits, fl_hits = sc.house_check(text, reply=(mode == "reply"), allow=allow, mode=mode)
    for rule, what, ln in f_hits: fails.append({"rule": rule.split()[0], "what": rule.split(" ", 1)[1] + f": {what}", "line": ln, "text": ""})
    for rule, what, ln in fl_hits: flags.append({"rule": rule.split()[0], "what": rule.split(" ", 1)[1] + f": {what}", "line": ln, "text": ""})
    for pos, w in find_all(sc.RHETORICAL_OPENER, text):
        if mode != "reply" and '"' not in w and "“" not in w: flags.append({"rule": "H23", "what": f"rhetorical question opens a paragraph: {w.strip()[:60]}", "line": line_of(text, pos), "text": ""})

    # ---- the six patterns, measured -------------------------------------------------------
    paras = [p for p in paragraphs(text) if not p.lstrip().startswith(("#", "-", "*", "1.", "2.", "3."))]
    sents = [s for p in paras for s in sentences(p)]
    lens = [len(s.split()) for s in sents]
    words = sum(lens)
    # elegant variation: machine text avoids repeating a content word in the next sentence (Opace 2026: median overlap 0.021 machine vs 0.063 human, the strongest single separator measured)
    if len(sents) >= 8 and sum(len(x.split()) for x in sents) >= 150:
        stop = set("the a an and or but so to of in on for with that this it is was are be i you we they my your our not no if as at by from have has had do does did will would can could just very really".split())
        def cw(x): return {w for w in re.findall(r"[a-z’']+", x.lower()) if w not in stop and len(w) > 2}
        ov = []
        for a, b in zip(sents, sents[1:]):
            A, B = cw(a), cw(b)
            if A and B: ov.append(len(A & B) / min(len(A), len(B)))
        if ov:
            mean_ov = statistics.mean(ov)
            if mean_ov < 0.025: flags.append({"rule": "H23", "what": f"synonym cycling: neighbouring sentences almost never repeat a word (mean overlap {mean_ov:.3f}; people sit near 0.06)", "line": 0, "text": ""})
    if words >= 60 and mode != "reply":
        passive_total = len(sc.PASSIVE.findall(text))
        if passive_total / max(words, 1) * 100 > 2.5: flags.append({"rule": "H5", "what": f"passive constructions: about {passive_total} in {words} words", "line": 0, "text": ""})
        if len(lens) >= 6:
            sd = statistics.pstdev(lens); mid = sum(1 for n in lens if 8 <= n <= 14) / len(lens)
            if sd < 5: flags.append({"rule": "H28", "what": f"sentences all weigh the same (spread {sd:.1f} words)", "line": 0, "text": ""})
            if mid > 0.6: flags.append({"rule": "H28", "what": f"{int(mid*100)}% of sentences are 8 to 14 words", "line": 0, "text": ""})
        if not sc.SPEAKER.search(" ".join(sents[:2])) and mode == "piece":
            flags.append({"rule": "H27", "what": "no speaker in the opening two sentences", "line": 1, "text": sents[0][:70] if sents else ""})
        landing = sum(1 for p in paras if len(sentences(p)) >= 2 and len(sentences(p)[-1].split()) <= 10 and not sc.SPEAKER.search(sentences(p)[-1]))
        if len(paras) >= 3 and landing / len(paras) > 0.5:
            flags.append({"rule": "H30", "what": f"landing lines on {landing} of {len(paras)} paragraphs", "line": 0, "text": ""})
        # triads: three consecutive short sentences of similar length (ladders), or a sentence of exactly three short parallel fragments
        for p in paras:
            ss = sentences(p)
            for i in range(len(ss) - 2):
                trio = [len(x.split()) for x in ss[i:i+3]]
                if all(n <= 7 for n in trio) and max(trio) - min(trio) <= 2:
                    flags.append({"rule": "H29", "what": "three short sentences in a row, same weight (a ladder)", "line": line_of(text, text.find(ss[i])), "text": " ".join(ss[i:i+3])[:90]}); break
        # H13 one speaker: first person present early, then a run of "you" with no "I" for 3+ paragraphs
        if len(paras) >= 6 and sc.SPEAKER.search(paras[0]):
            run = 0
            for p in paras[1:]:
                if re.search(r"\byou\b", p, re.I) and not sc.SPEAKER.search(p): run += 1
                else: run = 0
                if run >= 4:
                    flags.append({"rule": "H13", "what": "the speaker drops out: four paragraphs of 'you' with no 'I'", "line": 0, "text": ""}); break

    # ---- Part 2, replies ------------------------------------------------------------------
    if mode == "reply":
        qs = len(re.findall(r"\?", text))
        if qs > 2: flags.append({"rule": "S3", "what": f"{qs} questions in one reply", "line": 0, "text": ""})
        if words > 350: flags.append({"rule": "S2", "what": f"long reply: {words} words", "line": 0, "text": ""})

    report = {"path": path, "mode": mode, "words": words, "fails": fails, "flags": flags, "voice_guide": voice}
    if as_json:
        print(json.dumps(report, indent=2)); sys.exit(1 if fails else 0)
    print(f"check-prose: {path} ({mode}, {words} words)")
    if fails:
        print(f"  FAILS ({len(fails)}):")
        for f in fails[:MAX_FAILS_SHOWN]: print(f"    {f['rule']:<10} line {f['line']:<4} {f['what']}" + (f"  | {f['text']}" if f['text'] else ""))
        if len(fails) > MAX_FAILS_SHOWN: print(f"    ... and {len(fails) - MAX_FAILS_SHOWN} more")
    else:
        print("  fails: none")
    if flags:
        print(f"  flags ({len(flags)}), for the judge:")
        for f in flags[:MAX_FAILS_SHOWN]: print(f"    {f['rule']:<10} line {f['line']:<4} {f['what']}" + (f"  | {f['text']}" if f['text'] else ""))
        if len(flags) > MAX_FAILS_SHOWN: print(f"    ... and {len(flags) - MAX_FAILS_SHOWN} more")
    else:
        print("  flags: none")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
