#!/usr/bin/env python3
"""Does a draft keep the person's fingerprints, or did the model sand them off?

Research (Voice Under Revision, 2026; Catch Me If You Can, 2025) found that every rewrite by a frontier
model moves the same markers the same way: contractions down, first person down, commas and word length
up, sentence lengths evened out, the person's own sentences replaced. A "preserve the voice" instruction
only cuts the drift by a third. So this script measures the markers on the draft and on the person's own
corpus, and flags the draft where it has drifted toward the machine average.

Usage:
  python3 scripts/voice-diff.py <draft.md> [--corpus material/ bank/rewrites/ ...] [--source raw.md] [--voice guide.md] [--json]

Corpus: by default, every .md and .txt under material/ except README.md, swipe files and transcripts
(they hold other people's words), the right-hand side (the person's version) of each
pair in bank/rewrites/, and the approved samples quoted in canon/voice/voice-guide.md. Pass --corpus to
override. With fewer than 300 words of corpus the script says so and compares against nothing.

--source: the raw words the draft was made from (a memo, a transcript excerpt, a rough draft). The script
reports how many of the source's sentences survive in the draft (loosely matched), because the method says
the studio edits and shapes the person's sentences rather than replacing them. It also pairs each source
sentence with the draft sentence that took its place (the one sharing most of its content words) and flags
two things the other checks miss:
  sure where they weren't  a bound the person put on a claim (usually, in my experience, I think, can,
                           might, unless ...) that the draft sentence dropped; a modal made stronger
                           (might/may/can/could to will/must/always/never); a booster the draft added
                           (clearly, obviously, always, every, the only ...); an "I" or "my" sentence
                           turned into a general claim. Hedges per 1,000 words, source and draft.
  their terms gone         a term of the person's (a capitalised name of two or more words, a coined term
                           in double quotes, a hyphenated compound, a term from the voice guide's
                           Vocabulary section) missing from the draft where the draft talks about the same
                           thing. --voice <voice-guide.md> names the guide; by default the script looks
                           for canon/voice/voice-guide.md at the studio root.
These are flags for the judge. They never change the exit code.

Markers, per 100 words unless noted:
  contractions        don't, it's, I've ...
  first person        I, me, my, we, our ...
  causal connectives  because, so, since, which is why ...
  commas
  mean word length    characters
  sentence spread     coefficient of variation of sentence length (stdev / mean); humans about 0.33, LLM text about 0.25

Exit 1 when two or more markers have drifted (a flag for the judge, not a fail by itself).
"""
import glob, json, os, re, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

def clean(text):
    text = re.sub(r"^---\n.*?\n---\s*", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    post = sc.post_section(text)   # one of Posts A, B, C when the file holds three
    if post is not None: text = post
    text = re.sub(r"^(PARTS MAP|SOURCE MAP|Source map|ARGUMENT CHECK|BRIEF DEFECTS)[\s\S]*$", "", text, flags=re.M)
    text = "\n".join(l for l in text.splitlines() if not l.strip().startswith(("|", "#")))
    return text.strip()

def sentences(text):
    out = []
    for p in re.split(r"\n\s*\n", text):
        out += [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", p) if s.strip()]
    return out

def markers(text):
    words = re.findall(r"[A-Za-z’']+", text)
    n = max(len(words), 1)
    sents = sentences(text)
    lens = [len(s.split()) for s in sents] or [0]
    mean = statistics.mean(lens) if lens else 0
    cv = (statistics.pstdev(lens) / mean) if mean and len(lens) > 1 else 0
    return {
        "words": len(words),
        "contractions": round(100 * len(sc.CONTRACTION.findall(text)) / n, 2),
        "first_person": round(100 * len(sc.SPEAKER.findall(text)) / n, 2),
        "causal": round(100 * len(sc.CAUSAL.findall(text)) / n, 2),
        "commas": round(100 * text.count(",") / n, 2),
        "word_length": round(sum(len(w) for w in words) / n, 2),
        "sentence_cv": round(cv, 2),
    }

def rewrites_right_side(folder):
    """Each pair file holds the studio's draft and the person's version. Take the person's: the text under
    "## The person wrote", stopping at the next ## heading ("## What changed" is the studio's note, not theirs).
    README.md and files with no such section are skipped."""
    out = []
    for f in sorted(glob.glob(os.path.join(folder, "*.md"))):
        if os.path.basename(f).lower() == "readme.md": continue
        side = sc.person_side(open(f, encoding="utf-8").read())
        if side: out.append(side)
    return "\n\n".join(out)

def voice_samples(path):
    if not os.path.exists(path): return ""
    t = open(path, encoding="utf-8").read()
    return "\n".join(l.lstrip("> ").strip() for l in t.splitlines() if l.strip().startswith(">"))

def corpus_text(paths):
    chunks = []
    for p in paths:
        if os.path.isdir(p):
            if p.rstrip("/").endswith("rewrites"): chunks.append(rewrites_right_side(p)); continue
            for f in sc.corpus_files(p):   # skips README.md, swipe files and transcripts
                chunks.append(clean(open(f, encoding="utf-8", errors="ignore").read()))
        elif os.path.exists(p):
            chunks.append(voice_samples(p) if "voice-guide" in p else clean(open(p, encoding="utf-8", errors="ignore").read()))
    return "\n\n".join(c for c in chunks if c)

STOP = set("the a an and or but so to of in on for with that this it is was are be i you we they my your our".split())

def cw(s):
    """Content words: the words two sentences share when one says the same thing as the other."""
    return {w for w in re.findall(r"[a-z’']+", s.lower()) if w not in STOP and len(w) > 2}

def survival(source, draft):
    """Share of the source's sentences (6+ words) that survive in the draft, loosely: 70% of their content words appear in one draft sentence."""
    src = [s for s in sentences(source) if len(s.split()) >= 6]
    dr = [cw(s) for s in sentences(draft)]
    if not src: return None, []
    kept, lost = 0, []
    for s in src:
        c = cw(s)
        if not c: continue
        if any(len(c & d) / len(c) >= 0.7 for d in dr): kept += 1
        else: lost.append(s)
    return round(kept / len(src), 2), lost[:6]

# --- How sure the person was, and how sure the draft is ---------------------------------------------
A = "['’]"
HEDGES = [r"usually", r"often", r"sometimes", r"in my experience", r"i think", rf"i{A}d say", r"i suspect",
          r"i guess", r"i believe", r"for me", r"most of the time", r"not always", r"unless", r"tends? to",
          r"tended to", rf"can(?!{A}t)", r"could", r"may", r"might", r"probably", r"maybe", r"perhaps",
          r"likely", r"at least for", r"in some cases", r"in many cases", r"rarely", r"seems?( to)?"]
HEDGE = re.compile(r"\b(?:" + "|".join(HEDGES) + r")\b", re.I)
WEAK_MODAL = re.compile(rf"\b(?:might|may|can(?!{A}t)|could)\b", re.I)
STRONG_MODAL = re.compile(r"\b(?:will|must|always|never)\b", re.I)
BOOSTERS = [r"clearly", r"obviously", r"always", r"never", r"every", r"everyone", r"no one", r"nobody",
            r"the only", r"guaranteed", r"guarantees?", r"certainly", r"undeniably", r"without exception",
            r"definitely", r"of course"]
BOOSTER = re.compile(r"\b(?:" + "|".join(BOOSTERS) + r")\b", re.I)
SELF = re.compile(rf"\b(?:I|I{A}m|I{A}ve|I{A}d|I{A}ll|me|my|mine)\b")
SPEAKER_KEPT = re.compile(rf"\b(?:I|I{A}m|I{A}ve|I{A}d|I{A}ll|me|my|mine|we|we{A}re|we{A}ve|us|our)\b", re.I)
NOTE_SURE = "the draft states as settled what the person said with a bound; keep the bound or mark the line inferred"

def stance_free(s):
    """The sentence with its hedges, boosters and modals taken out, so matching looks at what it's about."""
    s = HEDGE.sub(" ", s); s = BOOSTER.sub(" ", s); s = STRONG_MODAL.sub(" ", s)
    return cw(s)

def match(source, draft):
    """Each source sentence paired with the draft sentence that took its place: the draft sentence holding
    most of its content words (hedges, boosters and modals left out), when that is half of them or more.
    Returns (source sentence, draft sentence) pairs; a source sentence with no such draft sentence is left out."""
    ds = sentences(draft)
    dc = [stance_free(d) for d in ds]
    pairs = []
    for s in sentences(source):
        c = stance_free(s)
        if not c: continue
        best, score = None, 0.0
        for i, d in enumerate(dc):
            shared = len(c & d)
            if shared < min(2, len(c)): continue
            r = shared / len(c)
            if r > score: best, score = i, r
        if best is not None and score >= 0.5: pairs.append((s, ds[best]))
    return pairs

def found(rx, s):
    return sorted({m.group(0).lower() for m in rx.finditer(s)})

def short(s, n=70):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n - 3].rstrip() + "..."

def per_1000(rx, text):
    n = len(re.findall(r"[A-Za-z’']+", text))
    return round(1000 * len(rx.findall(text)) / n, 1) if n else 0.0

def sureness(source, draft, pairs):
    out = {"source_hedges_per_1000": per_1000(HEDGE, source), "draft_hedges_per_1000": per_1000(HEDGE, draft),
           "bound_dropped": [], "modal_stronger": [], "booster_added": [], "first_person_gone": []}
    for s, d in pairs:
        sw, ds_ = found(WEAK_MODAL, s), [m for m in found(STRONG_MODAL, d) if m not in found(STRONG_MODAL, s)]
        stronger = bool(sw and ds_)
        if stronger:
            out["modal_stronger"].append({"from": sw, "to": ds_, "source": s, "draft": d})
        sh, dh = found(HEDGE, s), found(HEDGE, d)
        if stronger: sh = [h for h in sh if h not in sw]   # already named as a stronger modal
        if sh and not dh:
            out["bound_dropped"].append({"lost": sh, "source": s, "draft": d})
        added = [b for b in found(BOOSTER, d) if b not in found(BOOSTER, s) and not (sw and b in ds_)]
        if added:
            out["booster_added"].append({"added": added, "source": s, "draft": d})
        if SELF.search(s) and not SPEAKER_KEPT.search(d):
            out["first_person_gone"].append({"source": s, "draft": d})
    return out

# --- The person's own terms -----------------------------------------------------------------------------
LEAD = set("the a an in on at my our this that these those when if and but so i it as for to of with by from".split())
COMMON_HYPHEN = set("so-called well-known e-mail one-on-one long-term short-term follow-up day-to-day".split())

def voice_terms(path):
    """Terms from the voice guide's ## Vocabulary section: the "Phrases they use" and "Terms they coined" lines."""
    if not path or not os.path.isfile(path): return []
    t = open(path, encoding="utf-8", errors="ignore").read()
    m = re.search(r"^##\s*Vocabulary\s*$(.*?)(?=^##\s|\Z)", t, flags=re.M | re.S)
    if not m: return []
    out = []
    for line in m.group(1).splitlines():
        lm = re.match(r"\s*[-*]\s*(phrases they use|terms they coined)\s*:\s*(.*)", line, re.I)
        if not lm: continue
        for part in re.split(r"[;,]", lm.group(2)):
            part = part.strip().strip("\"“”'‘’` ").strip()
            if part and "<" not in part and "…" not in part: out.append(part)
    return out

def terms_in(sentence, extra):
    found_ = []
    for m in re.finditer(r"[A-Z][\w’'-]+(?:\s+(?:of|the|and|for|to)\s+[A-Z][\w’'-]+|\s+[A-Z][\w’'-]+)+", sentence):
        words = m.group(0).split()
        while words and words[0].lower() in LEAD: words = words[1:]
        if len(words) >= 2: found_.append(" ".join(words))
    for m in re.finditer(r"[\"“]([^\"“”]{3,40})[\"”]", sentence):
        if 1 <= len(m.group(1).split()) <= 4: found_.append(m.group(1).strip())
    for m in re.finditer(r"\b[A-Za-z]+(?:-[A-Za-z]+)+\b", sentence):
        if m.group(0).lower() not in COMMON_HYPHEN: found_.append(m.group(0))
    low = sentence.lower()
    for t in extra:
        if re.search(r"\b" + re.escape(t.lower()) + r"\b", low): found_.append(t)
    seen, out = set(), []
    for t in found_:
        if t.lower() not in seen: seen.add(t.lower()); out.append(t)
    return out

def terms_lost(draft, pairs, extra):
    low = draft.lower()
    out, seen = [], set()
    for s, d in pairs:
        for t in terms_in(s, extra):
            if t.lower() in seen: continue
            if re.search(r"(?<![\w-])" + re.escape(t.lower()) + r"(?![\w-])", low): continue
            seen.add(t.lower()); out.append({"term": t, "source": s, "draft": d})
    return out

def find_root(path):
    d = os.path.dirname(os.path.abspath(path))
    while d != os.path.dirname(d):
        if os.path.isfile(os.path.join(d, "CLAUDE.md")): return d
        d = os.path.dirname(d)
    return os.getcwd()

def main():
    sc.per_draft(__file__)
    args = sys.argv[1:]
    if not args or args[0].startswith("--"): print(__doc__); sys.exit(2)
    draft_path = args[0]
    as_json = "--json" in args
    corpus = []
    if "--corpus" in args:
        i = args.index("--corpus") + 1
        while i < len(args) and not args[i].startswith("--"): corpus.append(args[i]); i += 1
    else:
        corpus = ["material", "bank/rewrites", "canon/voice/voice-guide.md"]
    source = args[args.index("--source") + 1] if "--source" in args else None

    draft = clean(open(draft_path, encoding="utf-8").read())
    d = markers(draft)
    ctext = corpus_text(corpus)
    c = markers(ctext) if ctext else None
    report = {"draft": draft_path, "draft_markers": d, "corpus_words": c["words"] if c else 0, "corpus_markers": c, "drift": []}

    if c and c["words"] >= 300:
        # the directions a model drifts: fewer contractions, less first person, fewer causal words, more commas, longer words, flatter sentences
        def down(k, label):
            if c[k] > 0 and d[k] < 0.6 * c[k]: report["drift"].append(f"{label}: {d[k]} vs their {c[k]} per 100 words")
        def up(k, label, by):
            if d[k] > c[k] * by: report["drift"].append(f"{label}: {d[k]} vs their {c[k]}")
        down("contractions", "fewer contractions"); down("first_person", "less first person"); down("causal", "fewer because/so/which is why")
        up("commas", "more commas", 1.5); up("word_length", "longer words", 1.12)
        if d["sentence_cv"] < 0.75 * c["sentence_cv"] and d["words"] >= 80: report["drift"].append(f"flatter sentences: spread {d['sentence_cv']} vs their {c['sentence_cv']}")
    elif c:
        report["note"] = f"only {c['words']} words of the person's own prose found; need 300 or more to compare"
    else:
        report["note"] = "no corpus found (material/, bank/rewrites/, voice guide samples); nothing to compare against"

    if source and os.path.exists(source):
        stext = clean(open(source, encoding="utf-8").read())
        rate, lost = survival(stext, draft)
        report["source_sentences_kept"] = rate
        report["source_sentences_lost"] = lost
        if rate is not None and rate < 0.5: report["drift"].append(f"only {int(rate*100)}% of the person's own sentences survive; the draft replaced them")
        pairs = match(stext, draft)
        voice = args[args.index("--voice") + 1] if "--voice" in args else os.path.join(find_root(draft_path), "canon", "voice", "voice-guide.md")
        report["sureness"] = sureness(stext, draft, pairs)
        report["terms_lost"] = terms_lost(draft, pairs, voice_terms(voice))

    if as_json: print(json.dumps(report, indent=2)); sys.exit(1 if len(report["drift"]) >= 2 else 0)
    print(f"voice-diff: {draft_path} ({d['words']} words)" + (f" vs {c['words']} words of their own" if c else ""))
    for k in ("contractions", "first_person", "causal", "commas", "word_length", "sentence_cv"):
        print(f"  {k:<14} draft {d[k]:<6}" + (f" them {c[k]}" if c else ""))
    if "source_sentences_kept" in report:
        print(f"  their sentences kept: {report['source_sentences_kept']}")
        for s in report["source_sentences_lost"]: print(f"    lost: {s[:90]}")
    if "sureness" in report:
        u = report["sureness"]
        print(f"  hedges per 1,000 words: source {u['source_hedges_per_1000']}, draft {u['draft_hedges_per_1000']}")
        flags = ([f"bound dropped ({', '.join(f['lost'])})", f] for f in u["bound_dropped"])
        flags = list(flags) + [(f"modal stronger ({', '.join(f['from'])} to {', '.join(f['to'])})", f) for f in u["modal_stronger"]]
        flags += [(f"booster added ({', '.join(f['added'])})", f) for f in u["booster_added"]]
        flags += [("first person turned into a general claim", f) for f in u["first_person_gone"]]
        if flags:
            print("  sure where they weren't (flag): " + NOTE_SURE)
            for label, f in flags:
                print(f"    {label}: their \"{short(f['source'])}\" became \"{short(f['draft'])}\"")
        else:
            print("  sure where they weren't: none; the draft keeps the person's bounds")
    if "terms_lost" in report:
        if report["terms_lost"]:
            print("  their terms (flag): a term of theirs is gone where the draft talks about the same thing; keep their word (rule 3)")
            for f in report["terms_lost"]:
                print(f"    \"{f['term']}\": their \"{short(f['source'])}\" became \"{short(f['draft'])}\"")
        else:
            print("  their terms: all kept")
    if report.get("note"): print("  note: " + report["note"])
    print("  drift: " + ("; ".join(report["drift"]) if report["drift"] else "none"))
    sys.exit(1 if len(report["drift"]) >= 2 else 0)

if __name__ == "__main__":
    main()
