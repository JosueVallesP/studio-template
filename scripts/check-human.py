#!/usr/bin/env python3
"""Mechanical half of check-human. Reads a draft and reports the measurable signs of patterns 1 to 4
in skills/craft-human/SKILL.md (nobody in the room, sentences that all weigh the same, ladders and
"Not X. Y." pairs, landing lines) and the decoration adverbs. Patterns 5 (no stance) and 6 (every
loop closed) are read by the judge; the script counts stance words only as a note, because its list
is short. It measures; it doesn't judge. The editor reads the report next to the draft, and its flags
are evidence for the editor, not fails.

Usage: python3 scripts/check-human.py path/to/draft.md
       python3 scripts/check-human.py path/to/draft.md --json

Pangram: with --detector, the script sends the post to Pangram's API (key in .env as `PANGRAM_API_KEY`, never in
config/, which is saved to GitHub) and records the label, the fractions and the flagged windows. It's one
paid call, so it runs once per piece (the judge or the editor) and once on the final (the producer),
never in a rewrite loop. When a review-v*.md in the draft's folder already records a detector reading,
--detector prints that reading and makes no call; --force makes the call anyway (the producer passes it
on a shipped final that differs from the last draft). Without --detector the line says "not run". The line
reads `detector: <label>`; the label is a reading, never a pass or a fail, and never an exit code.
With `detector: parked` in studio.manifest.yaml, --detector makes no call and the line reads
`detector: parked`; that check comes before the recorded-reading check.

Exit codes: 0 when nothing is raised or only pattern flags are (flags are evidence for the judge, as
check-draft.py treats them), 1 when a banned device is present (an em dash or a reveal device, which
the house rules fail), 2 on bad usage. With --strict, any flag exits 1.
"""
import json, re, statistics, sys, os, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

SPEAKER = sc.SPEAKER          # first person only, any case; "you" alone is a billboard too
LADDER = re.compile(r"(?:^|\.\s+)Then [^.]{1,40}\.\s+Then ", re.M)
REVEAL = sc.REVEAL

def detector_parked():
    """The detector can be parked studio-wide with `detector: parked` in studio.manifest.yaml; --detector then makes no call."""
    manifest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "studio.manifest.yaml")
    if not os.path.exists(manifest): return False
    m = re.search(r"^detector:\s*(\S+)", open(manifest, encoding="utf-8").read(), re.M)
    return bool(m) and m.group(1) == "parked"

def body_only(text):
    post = sc.post_section(text)   # a draft file: measure the post alone (one of Posts A, B, C when there are three)
    if post is not None: text = post
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)          # frontmatter
    text = re.sub(r"^#.*$", "", text, flags=re.M)                  # headings
    text = re.sub(r"^(PARTS MAP|SOURCE MAP|Source map)[\s\S]*$", "", text, flags=re.M)
    return text.strip()

def sentences(par):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", par) if s.strip()]

def pangram(text, key):
    """One call to Pangram 4. Returns a dict with label, fractions, windows and a note. Never raises."""
    out = {"label": None, "fraction_ai": None, "fraction_ai_assisted": None, "fraction_human": None, "windows": [], "note": ""}
    if not key:
        out["note"] = "no PANGRAM_API_KEY in .env, so the detector did not run"; return out
    H = {"Content-Type": "application/json", "x-api-key": key}
    try:
        req = urllib.request.Request("https://text.external-api.pangram.com/task",
                                     data=json.dumps({"text": text, "model": "default"}).encode(), headers=H)
        with urllib.request.urlopen(req, timeout=30) as r: tid = json.loads(r.read().decode())["task_id"]
        d = {}
        for _ in range(45):
            time.sleep(2)
            with urllib.request.urlopen(urllib.request.Request(f"https://text.external-api.pangram.com/task/{tid}", headers=H), timeout=30) as r:
                d = json.loads(r.read().decode())
            if d.get("stage") in ("STAGE_SUCCESS", "STAGE_FAILED"): break
        if d.get("stage") != "STAGE_SUCCESS":
            out["note"] = f"Pangram returned {d.get('stage')}: {d.get('headline')}"; return out
        out["label"] = d.get("prediction_short")
        for k in ("fraction_ai", "fraction_ai_assisted", "fraction_human"):
            out[k] = round(d.get(k) or 0, 2)
        out["windows"] = [{"label": w.get("label"), "score": float(w.get("ai_assistance_score") or 0),
                           "text": (w.get("text") or "").replace("\n", " ")[:70]} for w in d.get("windows", [])]
        out["note"] = d.get("headline") or ""
    except urllib.error.HTTPError as e:
        why = {401: "the key was refused", 402: "the Pangram account has no API credits", 429: "rate limited"}.get(e.code, f"HTTP {e.code}")
        out["note"] = f"{why}, so the detector did not run"
    except Exception as e:
        out["note"] = f"call failed ({e}), so the detector did not run"
    return out

NOT_A_READING = re.compile(r"^(?:not run|no key|did not run|didn't run|no result|none|n/a|<)", re.I)
DETECTOR_LINE = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:detector|pangram)(?:\*\*)?\s*(?:reading)?\s*[:|]?\s+(.+?)\s*$", re.I | re.M)

def recorded_reading(path):
    """The detector reading an earlier review of this piece recorded, as (file, line), or None.
    A "not run" or "no key" line isn't a reading, so it doesn't stop a call."""
    import glob
    for rv in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(path)), "review-v*.md"))):
        try: txt = open(rv, encoding="utf-8").read()
        except OSError: continue
        for m in DETECTOR_LINE.finditer(txt):
            val = m.group(1).strip().strip("`")
            if val and not NOT_A_READING.match(val):
                return os.path.basename(rv), val
    return None

def main():
    sc.per_draft(__file__)
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    path = sys.argv[1]
    text = body_only(open(path, encoding="utf-8").read())
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith(("|", "-", "*", ">"))]
    sents = [s for p in paras for s in sentences(p)]
    lens = [len(s.split()) for s in sents] or [0]
    words = sum(lens)
    low = text.lower()

    mid = sum(1 for n in lens if 8 <= n <= 14)
    landing = 0
    for p in paras:
        ss = sentences(p)
        if len(ss) >= 2 and len(ss[-1].split()) <= 10 and not SPEAKER.search(ss[-1]):
            landing += 1
    report = {
        "words": words,
        "sentences": len(sents),
        "paragraphs": len(paras),
        "p1_first_person_per_100_words": round(100 * len(SPEAKER.findall(text)) / max(words, 1), 1),
        "p1_first_person_in_first_two_sentences": bool(SPEAKER.search(" ".join(sents[:2]))) if sents else False,
        "p2_sentence_length_mean": round(statistics.mean(lens), 1),
        "p2_sentence_length_stdev": round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0,
        "p2_share_of_sentences_8_to_14_words": round(mid / max(len(lens), 1), 2),
        "p3_then_ladders": len(LADDER.findall(text)),
        "p3_not_x_y_pairs": len(sc.not_x_y(text)),
        "p4_paragraphs_ending_on_a_short_impersonal_line": landing,
        "p4_share": round(landing / max(len(paras), 1), 2),
        "p5_stance_words": sc.stance_count(text),
        "p5_decoration_adverbs": {w: len(re.findall(rf"\b{w}\b", low)) for w in sc.DECORATION if re.search(rf"\b{w}\b", low)},
        "reveal_devices": len(REVEAL.findall(text)),
        "em_dashes": text.count("—"),
    }
    flags = []
    if report["p1_first_person_per_100_words"] < 1.5: flags.append("1: almost nobody in the room (little first person)")
    if not report["p1_first_person_in_first_two_sentences"]: flags.append("1: no speaker in the opening")
    if report["p2_sentence_length_stdev"] < 5 and len(lens) >= 6: flags.append("2: sentences all weigh the same")
    if report["p2_share_of_sentences_8_to_14_words"] > 0.6 and len(lens) >= 6: flags.append("2: most sentences are 8 to 14 words")
    if report["p3_then_ladders"] or report["p3_not_x_y_pairs"]: flags.append("3: ladders or Not X. Y. pairs")
    if report["p4_share"] > 0.5 and len(paras) >= 3: flags.append("4: landing lines on most paragraphs")
    if report["p5_stance_words"] == 0 and words > 80: report["note"] = "5: none of the listed stance words found; read for stance (the list is short)"
    if report["p5_decoration_adverbs"]: flags.append("decoration adverbs present")
    if report["reveal_devices"] or report["em_dashes"]: flags.append("banned devices present")
    report["flags"] = flags

    # The detector is one paid call, so it runs only when asked (--detector). The patterns above are
    # the gate; Pangram's label is a reading, recorded once per piece by the judge and once on the final.
    if "--detector" in sys.argv and detector_parked():
        report["pangram"] = {"label": None, "note": "parked (detector: parked in studio.manifest.yaml); no call made", "windows": []}
        report["detector"] = "parked"
    elif (prior := recorded_reading(path) if "--detector" in sys.argv and "--force" not in sys.argv else None):
        report["pangram"] = {"label": None, "windows": [],
                             "note": f"not called again: {prior[0]} already records the reading for this piece ({prior[1]}); pass --force to call anyway"}
        report["detector"] = f"recorded in {prior[0]}: {prior[1]}"
    elif "--detector" in sys.argv:
        # The environment first (on Claude Code on the web .env doesn't survive), then .env.
        key = os.environ.get("PANGRAM_API_KEY")
        if not key and os.path.exists(".env"):
            m = re.search(r'^PANGRAM_API_KEY=["\']?([^"\'\s]+)', open(".env").read(), re.M)
            if m: key = m.group(1)
        report["pangram"] = pangram(text, key)
        report["detector"] = report["pangram"].get("label") or "no result"
    else:
        report["pangram"] = {"label": None, "note": "not run (pass --detector to call Pangram; one call per piece)", "windows": []}
        report["detector"] = "not run"

    if "--json" in sys.argv:
        print(json.dumps(report, indent=2))
        if report["reveal_devices"] or report["em_dashes"] or (flags and "--strict" in sys.argv): sys.exit(1)
        return
    print(f"check-human: {path}")
    print(f"  {report['words']} words, {report['sentences']} sentences, {report['paragraphs']} paragraphs")
    print(f"  1 speaker: {report['p1_first_person_per_100_words']} first-person words per 100; speaker in opening: {report['p1_first_person_in_first_two_sentences']}")
    print(f"  2 rhythm: mean {report['p2_sentence_length_mean']} words, spread {report['p2_sentence_length_stdev']}, share 8 to 14 words {report['p2_share_of_sentences_8_to_14_words']}")
    print(f"  3 ladders: {report['p3_then_ladders']} 'Then' ladders, {report['p3_not_x_y_pairs']} Not X. Y. pairs")
    print(f"  4 landing lines: {report['p4_paragraphs_ending_on_a_short_impersonal_line']} of {report['paragraphs']} paragraphs")
    print(f"  stance words (a note; pattern 5 is read): {report['p5_stance_words']}; decoration adverbs: {report['p5_decoration_adverbs'] or 'none'}")
    if report.get("note"): print(f"  note: {report['note']}")
    print(f"  devices: {report['reveal_devices']} reveals, {report['em_dashes']} em dashes")
    pg = report["pangram"]
    print(f"  pangram: {pg.get('label') or 'no result'}; ai {pg.get('fraction_ai')}, assisted {pg.get('fraction_ai_assisted')}, human {pg.get('fraction_human')}; {pg.get('note','')}".rstrip("; "))
    for w in pg.get("windows", []):
        print(f"    {w['label']:<14} {w['score']:.2f}  {w['text']}")
    print("  flags: " + ("; ".join(flags) if flags else "none"))
    print(f"  detector: {report['detector']}")
    banned = report["reveal_devices"] or report["em_dashes"]
    if banned or (flags and "--strict" in sys.argv): sys.exit(1)

if __name__ == "__main__":
    main()
