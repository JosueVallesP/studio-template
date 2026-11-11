#!/usr/bin/env python3
"""voiceprint: stylometry for the content studio.

Measures how a person writes, from their own texts, and checks drafts against it.
Methods (see references/methods.md for sources):
  - Burrows's Delta and Cosine Delta on the most frequent words (Burrows 2002;
    Smith & Aldridge 2011; Evert et al. 2017)
  - General Impostors verification (Koppel & Winter 2014; Kestemont et al. 2016)
  - Craig's Zeta for marker words (Burrows 2007; Craig & Kinney 2009)
  - Style measures: sentence length and its spread, punctuation, contractions,
    pronouns, vocabulary range, sentence openers

Standard library only. Python 3.8+.

Commands:
  profile   build the person's voiceprint and writer targets from their texts
  score     check one draft against the person's texts
  patterns  what the person's rewrites in bank/rewrites/ have in common, measured
  markers   list the words the person uses that others don't, and the reverse

Where it reads and writes, from the instance root (skills/check-voiceprint has the why):
  the person's writing    material/ (files with "transcript" or "swipe-file" in the path are skipped: they hold other voices)
  the comparison set      bank/voiceprint/others/ (other writers in the person's formats), plus the studio's
                          side of every pair in bank/rewrites/ (read in place, never copied)
  outputs                 bank/voiceprint/profile.json, voice-targets.md, readings.jsonl

Run `python3 voiceprint.py <command> -h` for options.
"""

import argparse
import csv
import datetime as _dt
import json
import math
import os
import random
import re
import statistics
import sys
from collections import Counter

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

VERSION = "1.0.1"

DEFAULT_MINE = "material"
DEFAULT_MINE_EXCLUDE = r"transcript|swipe[-_ ]?file|linkedin[-_ ]?comments"   # other voices, and comments (too short to measure); README.md is always skipped
# Files marked in their first lines as not the person's own writing: a recorder's summary
# (scripts/inbox-to-text.py) or posts someone else wrote for them (the intake's ghostwriting question).
NOT_THEIR_WORDS = ("<!-- studio: looks like a summary, not their words", "<!-- studio: written for them, not by them")
DEFAULT_OTHERS = "bank/voiceprint/others"
DEFAULT_REWRITES = "bank/rewrites"
DEFAULT_PROFILE = "bank/voiceprint/profile.json"
DEFAULT_TARGETS = "bank/voiceprint/voice-targets.md"
DEFAULT_LOG = "bank/voiceprint/readings.jsonl"

MIN_SEPARATION = 0.7     # below this the verdict is withheld
FIT_READS_LIKE_YOU = 0.25  # set on held-out tests; see references/methods.md
FIT_CLOSE = 0.10
MIN_MINE_WORDS = 3000    # below this the verdict is withheld

# Very common words left out of the pairs word lists: their counts move with length.
PAIRS_SKIP = {"the", "a", "an", "to", "of", "and", "in", "is", "it", "that", "for", "on", "be", "as",
              "at", "by", "this", "with", "are", "was", "or"}

# English function words. Writers use these without thinking, which is why they
# carry the author signal (Mosteller & Wallace 1964; Burrows 2002).
FUNCTION_WORDS = set("""
a about above after again against all almost along already also although always am among an and another any anybody
anyone anything are around as at back be because been before being below between both but by can could did do does
doing done down during each either else enough even ever every everybody everyone everything few for from further
had has have having he her here hers herself him himself his how however i if in into is it its itself just least
less like many may me might mine more most much must my myself neither never no nobody none nor not nothing now
of off often on once one only onto or other others otherwise our ours ourselves out over own perhaps quite rather
really same several shall she should since so some somebody someone something sometimes still such than that the
their theirs them themselves then there these they this those though through thus till to together too toward
towards under until up upon us very was we well were what whatever when whenever where whether which while who
whoever whole whom whose why will with within without would yet you your yours yourself yourselves
""".split())

PRONOUN_I = {"i", "me", "my", "mine", "myself"}
PRONOUN_WE = {"we", "us", "our", "ours", "ourselves"}
PRONOUN_YOU = {"you", "your", "yours", "yourself", "yourselves"}

# Words often reported as overused in LLM output. Inside the studio the lists come from
# scripts/studio_checks.py (AI_TELLS and AI_VOCAB), the same ones the house rules use; this
# set is the fallback when the script runs on its own.
AI_WORDS = set("""
delve delves delving tapestry testament landscape realm pivotal crucial seamless seamlessly robust leverage
leveraging foster fostering elevate elevating navigate navigating navigates intricate intricacies multifaceted
underscore underscores showcasing showcase nuanced holistic paramount meticulous meticulously transformative
embark embarking unwavering resonate resonates vibrant bustling harness harnessing unlock unlocking unleash
empower empowering synergy streamline streamlining endeavor endeavors commendable noteworthy groundbreaking
""".split())

try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import studio_checks as _sc
    AI_PHRASES = [p.lower() for p in (_sc.AI_TELLS + _sc.AI_VOCAB)]
except Exception:  # running outside the studio
    _sc = None
    AI_PHRASES = sorted(AI_WORDS)
AI_RE = re.compile(r"(?<![\w'])(?:" + "|".join(re.escape(p) for p in sorted(AI_PHRASES, key=len, reverse=True)) + r")(?![\w'])", re.I)

LY_NOT_ADVERBS = {"only", "family", "early", "reply", "apply", "supply", "belly", "ally", "rally", "holy",
                  "ugly", "silly", "lonely", "lovely", "friendly", "likely", "daily", "weekly", "monthly",
                  "yearly", "italy", "july", "jelly", "fly", "bully", "costly", "elderly", "orderly", "curly",
                  "anomaly", "assembly", "butterfly", "lily", "melancholy", "monopoly", "rely", "imply", "comply",
                  "multiply", "ally", "kelly", "emily", "billy", "molly", "sally", "holly", "early"}

ABBREVIATIONS = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|vs|etc|e\.g|i\.e|U\.S|U\.K|Inc|Ltd|Co|No)\.", re.I)
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)*")
URL_RE = re.compile(r"https?://\S+|www\.\S+")


# --------------------------------------------------------------------------
# Loading and cleaning
# --------------------------------------------------------------------------

def clean_text(raw):
    """Strip markdown, front matter and links, keep line breaks and punctuation."""
    t = raw.replace("\r\n", "\n").replace("\r", "\n")
    t = t.replace("’", "'").replace("‘", "'")
    if t.startswith("---\n"):
        end = t.find("\n---", 4)
        if end != -1:
            t = t[end + 4:]
    want = os.environ.get("STUDIO_DRAFT") or ""
    for m in re.finditer(r"^## Post(?:[ \t]+([A-Z]))?[ \t]*\n(.*?)(?=^## |\Z)", t, flags=re.S | re.M):
        if not want or (m.group(1) or "") == want:  # a studio draft or final: measure the post (the named
            t = m.group(2)                           # one of Posts A, B, C), not the notes around it
            break
    t = re.sub(r"^(PARTS MAP|SOURCE MAP|Source map|ARGUMENT CHECK|BRIEF DEFECTS)[\s\S]*$", "", t, flags=re.M)
    t = "\n".join(l for l in t.split("\n") if not l.strip().startswith("|"))
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)          # images
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)         # links keep text
    t = URL_RE.sub(" ", t)
    t = re.sub(r"^\s{0,3}#{1,6}\s*", "", t, flags=re.M)    # headings
    t = re.sub(r"^\s{0,3}>\s?", "", t, flags=re.M)         # quotes
    t = re.sub(r"(\*\*|__)(.+?)\1", r"\2", t)              # bold
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", t)  # italics
    t = re.sub(r"<[^>]+>", " ", t)                         # html tags
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def read_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def marked_not_theirs(raw):
    """True when the first lines of a file say it isn't the person's own writing."""
    head = "\n".join(raw.lstrip().splitlines()[:5])
    return any(m in head for m in NOT_THEIR_WORDS)


def load_texts(source, text_col=None, label_col=None, where=None, label=None, exclude=None, skip_marked=False):
    """Load texts from a folder, a file, or a CSV. Returns list of dicts. With skip_marked, files whose
    first lines carry a NOT_THEIR_WORDS marker are left out."""
    out = []
    if source is None:
        return out
    if os.path.isdir(source):
        for root, _, files in os.walk(source):
            for name in sorted(files):
                if name.startswith(".") or name.lower() == "readme.md":
                    continue
                p = os.path.join(root, name)
                if exclude and re.search(exclude, os.path.relpath(p, source), re.I):
                    continue
                if name.lower().endswith(".csv"):
                    out.extend(load_texts(p, text_col, label_col, where, label))
                elif name.lower().endswith((".txt", ".md", ".markdown")):
                    raw = read_file(p)
                    if skip_marked and marked_not_theirs(raw):
                        continue
                    t = clean_text(raw)
                    if t:
                        out.append({"id": os.path.relpath(p, source), "label": label or "", "text": t})
        return out
    if not os.path.exists(source):
        sys.exit(f"voiceprint: can't find {source}. Put the texts there, or point to them with --mine / --others "
                 "(a folder of .md or .txt files, or a CSV).")
    if source.lower().endswith(".csv"):
        with open(source, encoding="utf-8", errors="replace", newline="") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            return out
        col = text_col or next((c for c in ("Full text", "text", "Text", "body", "content") if c in rows[0]), None)
        if not col:
            sys.exit(f"voiceprint: no text column in {source}; pass --text-col")
        for i, r in enumerate(rows):
            if where:
                k, v = where.split("=", 1)
                if r.get(k, "") != v:
                    continue
            t = clean_text(r.get(col, "") or "")
            if t:
                lab = (r.get(label_col, "") if label_col else "") or label or ""
                out.append({"id": f"{os.path.basename(source)}:{r.get('ID', i)}", "label": lab, "text": t})
        return out
    raw = read_file(source)
    if skip_marked and marked_not_theirs(raw):
        return out
    t = clean_text(raw)
    return [{"id": os.path.basename(source), "label": label or "", "text": t}] if t else []


def load_rewrite_pairs(folder):
    """The pairs in bank/rewrites/: (id, the studio's text, the person's text) for each file
    that has both sections (skills/setup-brand-tree/templates/bank-working/rewrites-template.md)."""
    pairs = []
    if not folder or not os.path.isdir(folder):
        return pairs
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or "readme" in name.lower():
            continue
        t = read_file(os.path.join(folder, name))
        st = re.search(r"^## The studio wrote\s*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
        pe = re.search(r"^## The person wrote\s*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
        if st and pe:
            a, b = clean_text(st.group(1)), clean_text(pe.group(1))
            if a and b and not a.startswith("<") and not b.startswith("<"):
                pairs.append((name, a, b))
    return pairs


# --------------------------------------------------------------------------
# Tokenizing
# --------------------------------------------------------------------------

def words_of(text):
    return [w.lower() for w in WORD_RE.findall(text)]


def sentences_of(text):
    """Split into sentences. A line break ends a sentence, as it does in a post."""
    protected = ABBREVIATIONS.sub(lambda m: m.group(0).replace(".", "\u0000"), text)
    sents = []
    for line in protected.split("\n"):
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^(?:[-*•→>]|\d+[.)])\s+", "", line)   # list markers
        parts = re.split(r"(?<=[.!?…])[\"'”)\]]*\s+(?=[\"'“(\[]?[A-Z0-9])", line)
        for p in parts:
            p = p.replace("\u0000", ".").strip()
            if WORD_RE.search(p):
                sents.append(p)
    return sents


def lines_of(text):
    return [l.strip() for l in text.split("\n") if WORD_RE.search(l)]


def chunk_text(text, size):
    """Split text into chunks of about `size` words at sentence breaks."""
    sents = sentences_of(text)
    chunks, cur, n = [], [], 0
    for s in sents:
        k = len(WORD_RE.findall(s))
        cur.append(s)
        n += k
        if n >= size:
            chunks.append("\n".join(cur))
            cur, n = [], 0
    if cur and (n >= size * 0.5 or not chunks):
        chunks.append("\n".join(cur))
    elif cur and chunks:
        chunks[-1] += "\n" + "\n".join(cur)
    return chunks


def chunk_corpus(docs, size):
    out = []
    for d in docs:
        n = len(WORD_RE.findall(d["text"]))
        if n <= size * 1.5:
            out.append(d)
        else:
            for j, c in enumerate(chunk_text(d["text"], size)):
                out.append({"id": f"{d['id']}#{j + 1}", "label": d["label"], "text": c, "parent": d["id"]})
    return out


# --------------------------------------------------------------------------
# Style features
# --------------------------------------------------------------------------

# name: (plain label, unit, what a higher value means in plain words)
FEATURES = {
    "sent_mean":        ("Average sentence length", "words", "longer sentences"),
    "sent_median":      ("Typical sentence length", "words", "longer sentences"),
    "sent_cv":          ("Sentence length variety", "spread (sd / mean)", "more mix of short and long sentences"),
    "short_sent_share": ("Short sentences (7 words or fewer)", "% of sentences", "more short sentences"),
    "long_sent_share":  ("Long sentences (25 words or more)", "% of sentences", "more long sentences"),
    "line_words":       ("Words per line or paragraph", "words", "denser blocks of text"),
    "one_line_share":   ("Lines that are a single sentence", "% of lines", "more one-sentence lines"),
    "word_len":         ("Average word length", "letters", "longer words"),
    "long_word_share":  ("Long words (9+ letters)", "% of words", "more long words"),
    "mattr":            ("Vocabulary range", "MATTR, 0 to 1", "less repetition of the same words"),
    "contractions":     ("Contractions (it's, don't)", "per 100 words", "more contractions"),
    "i_rate":           ("I / me / my", "per 100 words", "more first person"),
    "we_rate":          ("We / us / our", "per 100 words", "more 'we'"),
    "you_rate":         ("You / your", "per 100 words", "more direct address"),
    "and_but_so_start": ("Sentences starting with And / But / So", "% of sentences", "more conversational openers"),
    "i_start":          ("Sentences starting with I", "% of sentences", "more sentences starting with I"),
    "commas":           ("Commas", "per 1,000 words", "more commas"),
    "questions":        ("Question marks", "per 1,000 words", "more questions"),
    "exclaims":         ("Exclamation marks", "per 1,000 words", "more exclamation marks"),
    "colons":           ("Colons", "per 1,000 words", "more colons"),
    "semicolons":       ("Semicolons", "per 1,000 words", "more semicolons"),
    "dashes":           ("Dashes (em, en, spaced hyphen)", "per 1,000 words", "more dashes"),
    "ellipses":         ("Ellipses", "per 1,000 words", "more ellipses"),
    "parens":           ("Parentheses", "per 1,000 words", "more asides in parentheses"),
    "quotes":           ("Quotation marks", "per 1,000 words", "more quoted words"),
    "caps_words":       ("Words in capitals for emphasis", "per 1,000 words", "more capitals"),
    "numerals":         ("Numbers written as digits", "per 1,000 words", "more figures"),
    "ly_adverbs":       ("-ly adverbs", "per 100 words", "more -ly adverbs"),
    "ai_words":         ("Words common in AI text", "per 1,000 words", "more AI-typical words"),
}

# what a lower value means, for the writer targets
FEATURE_LOWER = {
    "sent_mean": "shorter sentences", "sent_median": "shorter sentences",
    "sent_cv": "more even sentence lengths", "short_sent_share": "fewer short sentences",
    "long_sent_share": "fewer long sentences", "line_words": "shorter lines and paragraphs",
    "one_line_share": "fewer one-sentence lines", "word_len": "shorter words",
    "long_word_share": "fewer long words", "mattr": "more repetition of the same words",
    "contractions": "fewer contractions", "i_rate": "less first person", "we_rate": "less 'we'",
    "you_rate": "less direct address", "and_but_so_start": "fewer conversational openers",
    "i_start": "fewer sentences starting with I", "commas": "fewer commas", "questions": "fewer questions",
    "exclaims": "fewer exclamation marks", "colons": "fewer colons", "semicolons": "fewer semicolons",
    "dashes": "fewer dashes", "ellipses": "fewer ellipses", "parens": "fewer asides in parentheses",
    "quotes": "fewer quoted words", "caps_words": "fewer capitals", "numerals": "fewer figures",
    "ly_adverbs": "fewer -ly adverbs", "ai_words": "fewer AI-typical words",
}

PERCENT_FEATURES = {"short_sent_share", "long_sent_share", "one_line_share", "long_word_share",
                    "and_but_so_start", "i_start"}


def mattr(words, window=50):
    if not words:
        return 0.0
    if len(words) <= window:
        return len(set(words)) / len(words)
    counts = Counter(words[:window])
    total = len(counts) / window
    n = 1
    for i in range(window, len(words)):
        out_w = words[i - window]
        counts[out_w] -= 1
        if counts[out_w] == 0:
            del counts[out_w]
        counts[words[i]] += 1
        total += len(counts) / window
        n += 1
    return total / n


def style_features(text):
    words = words_of(text)
    nw = max(len(words), 1)
    sents = sentences_of(text)
    slen = [len(WORD_RE.findall(s)) for s in sents] or [0]
    lines = lines_of(text)
    raw_tokens = WORD_RE.findall(text)
    per_k = 1000.0 / nw
    per_c = 100.0 / nw
    mean_s = statistics.mean(slen)
    sd_s = statistics.pstdev(slen) if len(slen) > 1 else 0.0
    first_words = [words_of(s)[:1] for s in sents]
    first_words = [f[0] for f in first_words if f]
    ns = max(len(first_words), 1)
    line_sent_counts = [len(sentences_of(l)) for l in lines]
    f = {
        "sent_mean": mean_s,
        "sent_median": statistics.median(slen),
        "sent_cv": (sd_s / mean_s) if mean_s else 0.0,
        "short_sent_share": 100.0 * sum(1 for x in slen if x <= 7) / len(slen),
        "long_sent_share": 100.0 * sum(1 for x in slen if x >= 25) / len(slen),
        "line_words": nw / max(len(lines), 1),
        "one_line_share": 100.0 * sum(1 for c in line_sent_counts if c == 1) / max(len(lines), 1),
        "word_len": sum(len(w.replace("'", "")) for w in words) / nw,
        "long_word_share": 100.0 * sum(1 for w in words if len(w) >= 9) / nw,
        "mattr": mattr(words),
        "contractions": per_c * sum(1 for w in words if "'" in w and not w.endswith("'s") or w in
                                   {"it's", "that's", "there's", "here's", "what's", "he's", "she's",
                                    "who's", "let's", "where's", "how's"}),
        "i_rate": per_c * sum(1 for w in words if w in PRONOUN_I),
        "we_rate": per_c * sum(1 for w in words if w in PRONOUN_WE),
        "you_rate": per_c * sum(1 for w in words if w in PRONOUN_YOU),
        "and_but_so_start": 100.0 * sum(1 for w in first_words if w in {"and", "but", "so", "because"}) / ns,
        "i_start": 100.0 * sum(1 for w in first_words if w == "i") / ns,
        "commas": per_k * text.count(","),
        "questions": per_k * text.count("?"),
        "exclaims": per_k * text.count("!"),
        "colons": per_k * len(re.findall(r":(?!\d)", text)),
        "semicolons": per_k * text.count(";"),
        "dashes": per_k * (text.count("\u2014") + text.count("--") + len(re.findall(r" [\u2013-] ", text))),
        "ellipses": per_k * (text.count("…") + len(re.findall(r"\.\.\.", text))),
        "parens": per_k * text.count("("),
        "quotes": per_k * (len(re.findall(r"[\"“”]", text)) / 2.0),
        "caps_words": per_k * sum(1 for w in raw_tokens if len(w) >= 2 and w.isupper() and w not in {"OK", "AI", "TV", "US", "UK", "CEO"}),
        "numerals": per_k * len(re.findall(r"\b\d[\d,.]*", text)),
        "ly_adverbs": per_c * sum(1 for w in words if w.endswith("ly") and len(w) > 4 and w not in LY_NOT_ADVERBS),
        "ai_words": per_k * len(AI_RE.findall(text)),
    }
    return f


def ai_words_found(text):
    return sorted({m.lower() for m in AI_RE.findall(text)})


# --------------------------------------------------------------------------
# Most frequent words, z-scores, Delta
# --------------------------------------------------------------------------

def rel_freqs(words):
    n = max(len(words), 1)
    c = Counter(words)
    return {w: k / n for w, k in c.items()}


def choose_mfw(docs_words, n_max=300, min_doc_share=0.2):
    """Most frequent words over the whole corpus, culled to words found in at least
    min_doc_share of texts (Hoover 2004) so one text's topic words don't dominate."""
    total = Counter()
    docfreq = Counter()
    for ws in docs_words:
        total.update(ws)
        docfreq.update(set(ws))
    nd = max(len(docs_words), 1)
    ranked = [w for w, _ in total.most_common() if docfreq[w] / nd >= min_doc_share]
    return ranked[:n_max]


class ZSpace:
    """Standardizes word frequencies against a corpus (Burrows 2002)."""

    def __init__(self, mfw, freq_rows):
        self.mfw = mfw
        self.mean, self.sd = [], []
        for j, w in enumerate(mfw):
            col = [r.get(w, 0.0) for r in freq_rows]
            m = statistics.mean(col)
            s = statistics.pstdev(col) or 1e-9
            self.mean.append(m)
            self.sd.append(s)

    def z(self, freqs):
        return [(freqs.get(w, 0.0) - self.mean[j]) / self.sd[j] for j, w in enumerate(self.mfw)]


def centroid(vectors):
    if not vectors:
        return []
    n = len(vectors)
    return [sum(v[j] for v in vectors) / n for j in range(len(vectors[0]))]


def burrows_delta(a, b, idx=None):
    idx = idx if idx is not None else range(len(a))
    idx = list(idx)
    return sum(abs(a[j] - b[j]) for j in idx) / max(len(idx), 1)


def cosine_delta(a, b, idx=None):
    idx = idx if idx is not None else range(len(a))
    dot = na = nb = 0.0
    for j in idx:
        dot += a[j] * b[j]
        na += a[j] * a[j]
        nb += b[j] * b[j]
    if na == 0 or nb == 0:
        return 1.0
    return 1.0 - dot / math.sqrt(na * nb)


def percentile(values, p):
    if not values:
        return float("nan")
    v = sorted(values)
    k = (len(v) - 1) * p / 100.0
    lo, hi = math.floor(k), math.ceil(k)
    if lo == hi:
        return v[int(k)]
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


# --------------------------------------------------------------------------
# The analysis behind score
# --------------------------------------------------------------------------

class Analysis:
    """Holds the person's texts and the comparison texts, chunked to a length."""

    def __init__(self, mine, others, size, n_mfw=300, min_doc_share=0.2, seed=7):
        self.size = size
        self.mine = chunk_corpus(mine, size)
        self.others = chunk_corpus(others, size)
        if len(self.mine) < 3:
            sys.exit("voiceprint: need at least 3 of the person's texts (or enough text to cut into 3 pieces)")
        if len(self.others) < 3:
            sys.exit("voiceprint: need at least 3 texts by other writers to compare against")
        self.mine_words = [words_of(d["text"]) for d in self.mine]
        self.others_words = [words_of(d["text"]) for d in self.others]
        allw = self.mine_words + self.others_words
        self.mfw = choose_mfw(allw, n_mfw, min_doc_share)
        if len(self.mfw) < 30:
            self.mfw = choose_mfw(allw, n_mfw, min_doc_share / 2)
        rows = [rel_freqs(w) for w in allw]
        self.space = ZSpace(self.mfw, rows)
        self.mine_z = [self.space.z(r) for r in rows[:len(self.mine)]]
        self.others_z = [self.space.z(r) for r in rows[len(self.mine):]]
        self.center = centroid(self.mine_z)
        self.rng = random.Random(seed)
        self._calibrate()
        self._style_setup()

    def _loo_center(self, i):
        n = len(self.mine_z)
        return [(self.center[j] * n - self.mine_z[i][j]) / (n - 1) for j in range(len(self.center))]

    def _calibrate(self):
        self.own_cos, self.own_bur = [], []
        # leave one parent text out, so pieces of the same text don't vouch for each other
        parents = [d.get("parent", d["id"]) for d in self.mine]
        for i, z in enumerate(self.mine_z):
            keep = [k for k in range(len(self.mine_z)) if parents[k] != parents[i]]
            if not keep:
                continue
            c = centroid([self.mine_z[k] for k in keep])
            self.own_cos.append(cosine_delta(z, c))
            self.own_bur.append(burrows_delta(z, c))
        self.oth_cos = [cosine_delta(z, self.center) for z in self.others_z]
        self.oth_bur = [burrows_delta(z, self.center) for z in self.others_z]

    def _style_setup(self):
        """Style distance: mean gap from the person's medians, in spreads measured
        over everyone's pieces, so a big gap on a measure that varies a lot counts less."""
        self.style_keys = [k for k in FEATURES if k != "ai_words"]
        self.mine_f = [style_features(d["text"]) for d in self.mine]
        self.others_f = [style_features(d["text"]) for d in self.others]
        allf = self.mine_f + self.others_f
        self.style_sd = {k: (statistics.pstdev([f[k] for f in allf]) or 1e-9) for k in self.style_keys}
        self.style_med = {k: statistics.median([f[k] for f in self.mine_f]) for k in self.style_keys}
        parents = [d.get("parent", d["id"]) for d in self.mine]
        self.own_sty = []
        for i, f in enumerate(self.mine_f):
            keep = [self.mine_f[k] for k in range(len(self.mine_f)) if parents[k] != parents[i]]
            if not keep:
                continue
            med = {k: statistics.median([g[k] for g in keep]) for k in self.style_keys}
            self.own_sty.append(self._sdist(f, med))
        self.oth_sty = [self._sdist(f, self.style_med) for f in self.others_f]

    def _sdist(self, f, med):
        return statistics.mean(abs(f[k] - med[k]) / self.style_sd[k] for k in self.style_keys)

    def distances(self, text):
        z = self.space.z(rel_freqs(words_of(text)))
        return z, cosine_delta(z, self.center), burrows_delta(z, self.center)

    def fit_of(self, dcos, dsty):
        """Share of the person's own pieces the text is at least as close as, taking the
        lower of the word measure and the style measure. A draft has to pass both: AI
        text tends to sit near the middle on word habits (it is uniform) while missing
        on style, and an average would let one hide the other."""
        a = sum(1 for x in self.own_cos if x >= dcos) / max(len(self.own_cos), 1)
        b = sum(1 for x in self.own_sty if x >= dsty) / max(len(self.own_sty), 1)
        return min(a, b)

    def reading(self, text):
        z, dcos, dbur = self.distances(text)
        dsty = self._sdist(style_features(text), self.style_med)
        fit = self.fit_of(dcos, dsty)
        oth_fit = [self.fit_of(c, s) for c, s in zip(self.oth_cos, self.oth_sty)]
        closer = sum(1 for x in oth_fit if x < fit) / max(len(oth_fit), 1)
        if fit >= FIT_READS_LIKE_YOU:
            v = "reads like you"
        elif fit >= FIT_CLOSE:
            v = "close"
        else:
            v = "off"
        return {"z": z, "cosine_delta": dcos, "burrows_delta": dbur, "style_distance": dsty,
                "fit": fit, "verdict": v, "closer_than_others": closer}

    def separation(self):
        """How well the measure tells the person's pieces from others' at this length:
        the chance a random piece of theirs fits better than a random piece by someone
        else (0.5 = coin flip). Own pieces are scored leave-one-out."""
        own_fit = []
        for i in range(min(len(self.own_cos), len(self.own_sty))):
            oc = self.own_cos[:i] + self.own_cos[i + 1:]
            os_ = self.own_sty[:i] + self.own_sty[i + 1:]
            a = sum(1 for x in oc if x >= self.own_cos[i]) / max(len(oc), 1)
            b = sum(1 for x in os_ if x >= self.own_sty[i]) / max(len(os_), 1)
            own_fit.append(min(a, b))
        oth_fit = [self.fit_of(c, s) for c, s in zip(self.oth_cos, self.oth_sty)]
        self.own_fit, self.oth_fit = own_fit, oth_fit
        if not own_fit or not oth_fit:
            return float("nan")
        wins = sum((a > b) + 0.5 * (a == b) for a in own_fit for b in oth_fit)
        return wins / (len(own_fit) * len(oth_fit))

    def impostors(self, z, exclude_mine=None, exclude_other=None, iters=100, feat_share=0.5, imp_share=0.5):
        """General Impostors: how often, over random feature and impostor subsets,
        the text sits closer to the person's texts than to every impostor."""
        nf = len(self.mfw)
        mine_idx = [i for i in range(len(self.mine_z)) if i not in (exclude_mine or set())]
        oth_idx = [i for i in range(len(self.others_z)) if i not in (exclude_other or set())]
        if not mine_idx or not oth_idx:
            return float("nan")
        hits = 0
        for _ in range(iters):
            feats = self.rng.sample(range(nf), max(1, int(nf * feat_share)))
            imps = self.rng.sample(oth_idx, max(1, int(len(oth_idx) * imp_share)))
            best_mine = min(cosine_delta(z, self.mine_z[i], feats) for i in mine_idx)
            best_imp = min(cosine_delta(z, self.others_z[i], feats) for i in imps)
            if best_mine < best_imp:
                hits += 1
        return hits / iters

    def impostor_calibration(self, max_n=40, iters=60):
        mine_scores, oth_scores = [], []
        parents = [d.get("parent", d["id"]) for d in self.mine]
        idx = list(range(len(self.mine_z)))
        self.rng.shuffle(idx)
        for i in idx[:max_n]:
            same = {k for k in range(len(self.mine_z)) if parents[k] == parents[i]}
            mine_scores.append(self.impostors(self.mine_z[i], exclude_mine=same, iters=iters))
        oidx = list(range(len(self.others_z)))
        self.rng.shuffle(oidx)
        for i in oidx[:max_n]:
            oth_scores.append(self.impostors(self.others_z[i], exclude_other={i}, iters=iters))
        return mine_scores, oth_scores


# --------------------------------------------------------------------------
# Profile summaries
# --------------------------------------------------------------------------

def feature_table(docs):
    rows = [style_features(d["text"]) for d in docs]
    return {k: [r[k] for r in rows] for k in FEATURES}


def summarize(values):
    return {
        "p20": percentile(values, 20), "median": percentile(values, 50), "p80": percentile(values, 80),
        "p10": percentile(values, 10), "p90": percentile(values, 90),
        "sd": statistics.pstdev(values) if len(values) > 1 else 0.0,
    }


def effect(mine_vals, oth_vals):
    """Difference between the person and other writers, in pooled spreads."""
    if len(mine_vals) < 2 or len(oth_vals) < 2:
        return 0.0
    sd = math.sqrt((statistics.pvariance(mine_vals) + statistics.pvariance(oth_vals)) / 2.0)
    if sd == 0:
        return 0.0
    return (statistics.median(mine_vals) - statistics.median(oth_vals)) / sd


def zeta_markers(mine_docs, others_docs, seg=150, min_count=3, top=40):
    """Craig's Zeta (Craig & Kinney 2009): share of the person's segments that use a
    word minus the share of other writers' segments that use it. Range -1 to 1."""
    def segs(docs):
        out = []
        for d in docs:
            ws = words_of(d["text"])
            if len(ws) <= seg * 1.5:
                out.append(set(ws))
            else:
                for i in range(0, len(ws), seg):
                    part = ws[i:i + seg]
                    if len(part) >= seg * 0.5:
                        out.append(set(part))
        return out
    ms, os_ = segs(mine_docs), segs(others_docs)
    if not ms or not os_:
        return [], []
    cm, co = Counter(), Counter()
    for s in ms:
        cm.update(s)
    for s in os_:
        co.update(s)
    vocab = {w for w in cm if cm[w] >= min_count} | {w for w in co if co[w] >= min_count * 2}
    rows = []
    for w in vocab:
        pm, po = cm[w] / len(ms), co[w] / len(os_)
        rows.append((pm - po, w, pm, po))
    rows.sort(reverse=True)
    markers = [r for r in rows if r[2] >= 0.1][:top]
    anti = [r for r in reversed(rows) if r[3] >= 0.1][:top]
    fmt = lambda r: {"word": r[1], "zeta": round(r[0], 3), "mine": round(r[2], 3), "others": round(r[3], 3),
                     "function_word": r[1] in FUNCTION_WORDS}
    return [fmt(r) for r in markers], [fmt(r) for r in anti]


# --------------------------------------------------------------------------
# House-rule patterns in the person's own writing
# --------------------------------------------------------------------------
# The house rules (skills/craft-house-rules) fail or flag patterns that mark machine text. Some people
# use one of them in their own writing, often, and then it's theirs (the exception principle). The
# profile counts each pattern in the person's pieces, the way a writer's pre-AI baseline is used to
# flag a pattern only above that writer's own density, so a rule they break themselves can become an
# exception on their yes, and "Above your own rate" can hold a draft to their rate even then.

HOUSE_RULES = {   # rule ID: the pattern in plain words. H5 (passive), H6 and the "likely tic" list are left out: too common to tell a person apart.
    "H2": "a longer word where a plain one exists",
    "H16": "em dashes",
    "H17": "\"it's not X, it's Y\" and \"Not X. Y.\" contrasts",
    "H18": "reveals, such as \"Here's the thing.\" or \"The result: ...\"",
    "H19": "adverbs the rules cut, such as \"truly\" or \"incredibly\"",
    "H20": "the word \"expert\"",
    "H21": "words the rules list as machine vocabulary",
    "H22": "hedges, unnamed sources and staged sincerity",
    "H23": "semicolon chains, parenthetical asides and other structural habits",
    "H29": "staged rhythm, such as \"No X. No Y. Just Z.\", and negation lists",
}
SKIP_FORMS = {"H19 adverb, judge decides"}   # "very", "highly": a judge's call for everyone, too common to tell a person apart
PHRASE_RULES = {"H2", "H19", "H20", "H21"}   # matched word by word: a phrase exception fits these better than the whole rule
OWN_RULE_SHARE = 0.30    # a pattern in this share of the person's pieces counts as theirs...
OWN_RULE_RATE = 2.0      # ...or one used more often than this per 1,000 words
OWN_RULE_PIECES = 3      # and in at least this many pieces either way


def _house_form(rule):
    """A house_check rule label without the counts it carries: "H23 parenthetical asides"."""
    r = re.sub(r"\s*\((?:\d+ distinct in \d+ words|one every \d+ words)\)", "", rule)
    r = re.sub(r"\s*\(your own pattern[^)]*\)", "", r)
    return "H2 plain word exists" if r.startswith("H2 ") else r.strip()


def _sentence_with(line, matched):
    """The sentence in a line that holds the match, for a short quote."""
    sents = sentences_of(line) or [line]
    key = (matched or "").lower()[:30]
    pick = next((s for s in sents if key and key in s.lower()), sents[0])
    return pick if len(pick) <= 220 else pick[:217].rstrip() + "..."


def house_counts(text):
    """The house-rule patterns in one text, with no exceptions applied. A use is one sentence that
    shows the pattern, so two matchers catching the same sentence count once."""
    out = {"words": len(WORD_RE.findall(text)), "rules": Counter(), "forms": Counter(),
           "phrases": {}, "quotes": {}, "fails": set()}
    if _sc is None:
        return out
    fails, flags = _sc.house_check(text)
    lines = text.split("\n")
    seen = set()
    for kind, hits in (("fail", fails), ("flag", flags)):
        for rule, matched, ln in hits:
            rid = rule.split()[0]
            if rid not in HOUSE_RULES or _house_form(rule) in SKIP_FORMS:
                continue
            line = lines[ln - 1] if 0 < ln <= len(lines) else ""
            quote = _sentence_with(line, matched)
            if kind == "fail":
                out["fails"].add(rid)
            key = (rid, ln, quote)
            if key in seen:
                continue
            seen.add(key)
            out["rules"][rid] += 1
            out["forms"][_house_form(rule)] += 1
            if rid in PHRASE_RULES:
                out["phrases"].setdefault(rid, Counter())[matched.lower()] += 1
            out["quotes"].setdefault(rid, []).append(quote)
    return out


def house_profile(docs):
    """Each house-rule pattern across the person's pieces: uses, the rate per 1,000 words, the share of
    pieces that use it, and up to three short quotes from different pieces."""
    rows = [(d, house_counts(d["text"])) for d in docs]
    words = sum(r["words"] for _, r in rows)
    n = len(rows)
    rules = {}
    for rid in HOUSE_RULES:
        counts = [r["rules"].get(rid, 0) for _, r in rows]
        total = sum(counts)
        if not total:
            continue
        rates = [1000.0 * c / max(r["words"], 1) for c, (_, r) in zip(counts, rows)]
        using = sum(1 for c in counts if c)
        forms = Counter()
        phrases = Counter()
        for _, r in rows:
            forms.update({f: c for f, c in r["forms"].items() if f.split()[0] == rid})
            phrases.update(r["phrases"].get(rid, Counter()))
        quotes = []
        for d, r in rows:
            for q in r["quotes"].get(rid, [])[:1]:
                quotes.append({"text": q, "source": d.get("parent") or d["id"]})
            if len(quotes) >= 3:
                break
        per_1000 = 1000.0 * total / max(words, 1)
        share = using / max(n, 1)
        rules[rid] = {
            "pattern": HOUSE_RULES[rid],
            "check": "fail" if any(rid in r["fails"] for _, r in rows) else "flag",
            "uses": total, "per_1000": round(per_1000, 2),
            "pieces_using": using, "share": round(share, 3),
            "median_per_1000": round(percentile(rates, 50), 2), "p85_per_1000": round(percentile(rates, 85), 2),
            "forms": dict(forms.most_common()),
            "phrases": dict(phrases.most_common(6)),
            "quotes": quotes,
            "yours": using >= OWN_RULE_PIECES and (share >= OWN_RULE_SHARE or per_1000 >= OWN_RULE_RATE),
        }
    order = sorted(rules, key=lambda k: (rules[k]["share"], rules[k]["per_1000"]), reverse=True)
    return {"pieces": n, "words": words, "rules": {k: rules[k] for k in order},
            "break_yourself": [k for k in order if rules[k]["yours"]],
            "thresholds": {"share": OWN_RULE_SHARE, "per_1000": OWN_RULE_RATE, "pieces": OWN_RULE_PIECES}}


def render_house_rules(h):
    """The "Rules you break yourself" section of voice-targets.md."""
    if not h:
        return []
    pct = lambda x: f"{x * 100:.0f}%"
    lines = ["## Rules you break yourself", "",
             "The studio's house rules ban or flag some patterns that mark machine-written text. Your own pieces "
             f"use a few of them anyway. Each pattern below shows up in at least {pct(OWN_RULE_SHARE)} of your pieces, "
             f"or more than {OWN_RULE_RATE:.0f} times per 1,000 words, and in at least {OWN_RULE_PIECES} pieces, so "
             "it's part of how you write. The studio proposes each one to you with these counts and quotes; only "
             "your yes puts it in your voice guide as an exception. After that the scripts flag each use for the "
             "judge instead of failing it, and a draft still can't use it more often than you do.", ""]
    mine = [k for k in h.get("break_yourself", [])]
    if not mine:
        lines.append("None of these patterns shows up often enough in your writing to count as yours. The house "
                     "rules apply as written.")
    for rid in mine:
        r = h["rules"][rid]
        now = ("The scripts fail this today; as an exception it becomes a flag."
               if r["check"] == "fail" else "The scripts flag this for the judge already; the counts are the evidence the judge reads.")
        lines.append(f"- **{rid}, {r['pattern']}:** in {r['pieces_using']} of {h['pieces']} pieces ({pct(r['share'])}), "
                     f"{r['per_1000']:.1f} times per 1,000 words. {now}")
        forms = [f"{f.split(' ', 1)[1] if ' ' in f else f} ({c})" for f, c in r["forms"].items()]
        if len(forms) > 1:
            lines.append(f"  The forms you use: {', '.join(forms)}.")
        if rid in PHRASE_RULES and r["phrases"]:
            lines.append("  This rule matches word by word, so a phrase exception for the words you use fits better "
                         f"than the whole rule: {', '.join(chr(34) + p + chr(34) for p in r['phrases'])}.")
        for q in r["quotes"]:
            lines.append(f"  > \"{q['text']}\" ({q['source']})")
    others = [k for k in h["rules"] if k not in mine]
    if others:
        lines += ["", "Patterns you use now and then, below that line. These stay under the house rules:", ""]
        for rid in others:
            r = h["rules"][rid]
            rate = f"{r['per_1000']:.1f}" if r["per_1000"] >= 0.1 else "under 0.1"
            lines.append(f"- {rid}, {r['pattern']}: in {r['pieces_using']} of {h['pieces']} pieces, "
                         f"{rate} per 1,000 words.")
    lines.append("")
    return lines


def fmt_num(k, v):
    if v != v:  # nan
        return "n/a"
    if k == "mattr":
        return f"{v:.2f}"
    if k in PERCENT_FEATURES:
        return f"{v:.0f}%"
    if abs(v) >= 10:
        return f"{v:.0f}"
    return f"{v:.1f}"


# --------------------------------------------------------------------------
# Plain-language guidance
# --------------------------------------------------------------------------

ADVICE = {
    "sent_mean": ("Your sentences run longer than this. Let some of them carry a full thought with its reason.",
                  "Your sentences run shorter than this. Break the long ones where you'd take a breath."),
    "sent_median": ("Your typical sentence is longer.", "Your typical sentence is shorter."),
    "sent_cv": ("You mix short and long sentences more than this draft does. Even sentence lengths are one of the clearest signs of machine text.",
                "This draft swings between very short and very long more than you do."),
    "short_sent_share": ("You use more short sentences than this.", "This draft has more short sentences than you write. Join some fragments into full sentences."),
    "long_sent_share": ("You write more long sentences than this.", "This draft has more long sentences than you write. Split some."),
    "line_words": ("Your paragraphs are denser than this.", "You break lines more often than this draft does."),
    "one_line_share": ("You use more one-sentence lines than this.", "This draft has more one-sentence lines than you use."),
    "word_len": ("Your words are longer on average than this.", "This draft uses longer words than you do. Swap them for the plain word you'd say."),
    "long_word_share": ("You use more long words than this.", "This draft has more long words than you use. Use the plain word."),
    "mattr": ("Your vocabulary is more varied than this draft.", "This draft is more varied than you usually are. You repeat words more, and that's fine."),
    "contractions": ("You contract more than this draft does (it's, don't, you'll). Use the forms you'd say out loud.",
                     "This draft contracts more than you do."),
    "i_rate": ("You speak in first person more than this.", "This draft says I more than you usually do."),
    "we_rate": ("You say 'we' more than this.", "This draft says 'we' more than you usually do."),
    "you_rate": ("You talk to the reader directly more than this.", "This draft says 'you' more than you usually do."),
    "and_but_so_start": ("You start sentences with And, But or So more than this.", "This draft starts with And, But or So more than you do."),
    "i_start": ("You start more sentences with I.", "This draft starts more sentences with I than you do."),
    "commas": ("You use more commas than this.", "This draft has more commas than you use. Some sentences may be doing too much."),
    "questions": ("You ask more questions than this.", "This draft asks more questions than you do."),
    "exclaims": ("You use more exclamation marks than this.", "This draft has more exclamation marks than you use."),
    "colons": ("You use more colons than this.", "This draft has more colons than you use."),
    "semicolons": ("You use more semicolons than this.", "This draft has semicolons you don't use."),
    "dashes": ("You use more dashes than this.", "This draft has dashes you don't use."),
    "ellipses": ("You use ellipses for asides more than this.", "This draft has more ellipses than you use."),
    "parens": ("You use parentheses for asides more than this.", "This draft has more parentheses than you use."),
    "quotes": ("You quote words more than this.", "This draft has more quote marks than you use."),
    "caps_words": ("You use capitals for emphasis more than this.", "This draft has more capitals than you use."),
    "numerals": ("You use more numbers than this.", "This draft has more numbers than you use."),
    "ly_adverbs": ("You use more -ly adverbs than this.", "This draft has more -ly adverbs than you use. Cut the ones that do no work."),
    "ai_words": ("", "This draft uses words that show up far more in AI text than in yours."),
}


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def add_corpus_args(p):
    p.add_argument("--mine", default=DEFAULT_MINE, help="folder, file or CSV of the person's own writing (default material/)")
    p.add_argument("--mine-exclude", default=DEFAULT_MINE_EXCLUDE,
                   help="skip files in --mine whose path matches this pattern (default: transcripts, swipe files and LinkedIn comments; '' to keep all)")
    p.add_argument("--rewrites", default=DEFAULT_REWRITES,
                   help="rewrite pairs whose studio side joins the comparison set (default bank/rewrites; '' to skip)")
    p.add_argument("--mine-where", help="CSV filter for --mine, e.g. Author=Dan Koe")
    p.add_argument("--others", default=DEFAULT_OTHERS, help="folder, file or CSV of other writers' texts to compare against")
    p.add_argument("--others-where", help="CSV filter for --others; prefix with ! to exclude, e.g. '!Author=Dan Koe'")
    p.add_argument("--text-col", help="CSV column holding the text (default: Full text / text)")
    p.add_argument("--label-col", help="CSV column holding the writer's name")


def load_corpora(a):
    mine = load_texts(a.mine, a.text_col, a.label_col, a.mine_where, label="mine", exclude=a.mine_exclude or None,
                      skip_marked=True)
    where = a.others_where
    others = []
    if a.others and (os.path.exists(a.others) or a.others != DEFAULT_OTHERS):
        if where and where.startswith("!"):
            k, v = where[1:].split("=", 1)
            others = [d for d in load_texts(a.others, a.text_col, k) if d["label"] != v]
        else:
            others = load_texts(a.others, a.text_col, a.label_col, where, label="others")
    # the studio's own drafts are the comparison that matters most: does this sound like the
    # person, or like the studio?
    for name, studio, _ in load_rewrite_pairs(a.rewrites):
        others.append({"id": f"rewrites/{name}", "label": "studio", "text": studio})
    return mine, others


def word_count(docs):
    return sum(len(WORD_RE.findall(d["text"])) for d in docs)


def cmd_profile(a):
    mine, others = load_corpora(a)
    if len(mine) < 3:
        sys.exit("voiceprint: need at least 3 of the person's texts to build a profile")
    mw, ow = word_count(mine), word_count(others)
    mt = feature_table(mine)
    ot = feature_table(others) if others else {k: [] for k in FEATURES}
    feats = {}
    for k in FEATURES:
        s = summarize(mt[k])
        s["others_median"] = percentile(ot[k], 50) if ot[k] else None
        s["effect"] = round(effect(mt[k], ot[k]), 2) if ot[k] else 0.0
        feats[k] = {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in s.items()}
    markers, anti = zeta_markers(mine, others) if others else ([], [])
    allw = Counter()
    for d in mine:
        allw.update(words_of(d["text"]))
    profile = {
        "voiceprint_version": VERSION,
        "built": _dt.date.today().isoformat(),
        "mine": {"source": a.mine, "texts": len(mine), "words": mw},
        "others": {"source": a.others, "texts": len(others), "words": ow},
        "features": feats,
        "markers": markers,
        "anti_markers": anti,
        "top_words": [w for w, _ in allw.most_common(60)],
        "house_rules": house_profile(mine),
        "warnings": profile_warnings(len(mine), mw, len(others), ow),
    }
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)
    targets = render_targets(profile)
    os.makedirs(os.path.dirname(a.targets) or ".", exist_ok=True)
    with open(a.targets, "w", encoding="utf-8") as f:
        f.write(targets)
    print(f"Profile: {a.out}\nWriter targets: {a.targets}")
    print(f"Built from {len(mine)} of your texts ({mw:,} words), compared with {len(others)} texts by others ({ow:,} words).")
    for w in profile["warnings"]:
        print(f"Note: {w}")


def profile_warnings(n_mine, w_mine, n_oth, w_oth):
    out = []
    if w_mine < 5000:
        out.append(f"Your sample is {w_mine:,} words. Stylometry gets steady around 5,000+ words of your writing; "
                   "below that, treat the numbers as a first read and add more texts.")
    if n_mine < 10:
        out.append(f"Only {n_mine} of your texts. With fewer than 10, one unusual piece can move your ranges.")
    if n_oth < 10:
        out.append("Fewer than 10 comparison texts. Markers and distances need a wider comparison set: add "
                   "posts or essays by people who write in your formats to bank/voiceprint/others/, and every "
                   "rewrite pair in bank/rewrites/ adds the studio's draft.")
    return out


def render_targets(p):
    """The writer's brief: what this person's writing measures, in plain words."""
    feats = p["features"]
    lines = ["# Voice targets", "",
             f"Measured from {p['mine']['texts']} of your texts ({p['mine']['words']:,} words) on {p['built']}, "
             f"against {p['others']['texts']} texts by other writers. The writer reads this before drafting; "
             "the numbers describe how you already write, they aren't rules to hit. A draft that matches every "
             "number can still say nothing, so this sits under your points of view, never above them.", ""]
    for w in p.get("warnings", []):
        lines.append(f"> Note: {w}")
    if p.get("warnings"):
        lines.append("")
    dist = sorted(((abs(v.get("effect", 0)), k) for k, v in feats.items()), reverse=True)
    strong = [k for e, k in dist if e >= 0.5 and k != "ai_words"]
    lines += ["## What sets your writing apart", "",
              "These are the measures where you differ most from the other writers in the comparison set.", ""]
    if not strong:
        lines.append("Nothing stands out strongly yet. Add more of your texts, or a comparison set closer to your format.")
    for k in strong[:10]:
        v = feats[k]
        label, unit, higher = FEATURES[k]
        phrase = higher if v["effect"] > 0 else FEATURE_LOWER[k]
        lines.append(f"- **{label}:** most of your texts sit between {fmt_num(k, v['p20'])} and "
                     f"{fmt_num(k, v['p80'])} ({unit}); other writers' median is {fmt_num(k, v['others_median'])}. "
                     f"You write with {phrase} than they do.")
    lines += ["", "## Your ranges", "", "| Measure | Your usual range | Your median | Others' median |", "| --- | --- | --- | --- |"]
    for k, (label, unit, _) in FEATURES.items():
        v = feats[k]
        lines.append(f"| {label} ({unit}) | {fmt_num(k, v['p20'])} to {fmt_num(k, v['p80'])} | "
                     f"{fmt_num(k, v['median'])} | {fmt_num(k, v['others_median']) if v['others_median'] is not None else 'n/a'} |")
    fw_m = [m for m in p["markers"] if m["function_word"]][:15]
    ct_m = [m for m in p["markers"] if not m["function_word"]][:20]
    fw_a = [m for m in p["anti_markers"] if m["function_word"]][:15]
    ct_a = [m for m in p["anti_markers"] if not m["function_word"]][:20]
    pct = lambda x: f"{x * 100:.0f}%"
    lines += ["", "## Words you reach for", "",
              "Small words you use more than other writers do. These are the strongest part of the fingerprint "
              "because nobody chooses them on purpose.", ""]
    lines.append(", ".join(f"{m['word']} ({pct(m['mine'])} of your pieces vs {pct(m['others'])})" for m in fw_m) or "None stand out yet.")
    lines += ["", "Other words you use more than other writers do. Some are topic words; keep the ones that are "
              "really yours and ignore the rest.", ""]
    lines.append(", ".join(f"{m['word']} ({pct(m['mine'])} vs {pct(m['others'])})" for m in ct_m) or "None stand out yet.")
    lines += ["", "## Words you avoid", "", "Words other writers use that you rarely do. If a draft leans on these, it drifts from you.", ""]
    lines.append(", ".join(f"{m['word']} ({pct(m['mine'])} vs {pct(m['others'])})" for m in (fw_a + ct_a)[:30]) or "None stand out yet.")
    lines += [""] + render_house_rules(p.get("house_rules"))
    lines += ["## How to use this", "",
              "- Draft from the person's material and points of view first. Then check the draft against these "
              "ranges with `python3 scripts/voiceprint.py score <draft>`.",
              "- Fix what the report flags once, in the person's way of saying it. Don't loop until every number "
              "lands; chasing the numbers produces text that matches on paper and reads worse.",
              "- Rebuild this file whenever the person adds material or a batch of rewrites lands "
              "(`python3 scripts/voiceprint.py profile`).", ""]
    return "\n".join(lines)


MIN_PIECES_ABOVE = 5     # fewer of the person's pieces than this and "Above your own rate" isn't read
VERDICT_LINE_WORDS = 8   # a closing sentence this short reads as a verdict line


def _paragraphs(text):
    return [p for p in re.split(r"\n\s*\n", text) if WORD_RE.search(p)]


def shape_of(text, marker_words):
    """The habits a writer drifts into when it imitates a person: marker word rates, the most
    repeated sentence opener, paragraphs that end on a short line, and how the piece closes."""
    words = words_of(text)
    nw = max(len(words), 1)
    counts = Counter(words)
    sents = sentences_of(text)
    openers = Counter(w[0] for w in (words_of(s)[:1] for s in sents) if w)
    top, top_n = (openers.most_common(1)[0] if openers else ("", 0))
    paras = [sentences_of(p) for p in _paragraphs(text)]
    paras = [ss for ss in paras if len(ss) >= 2]   # a one-sentence paragraph has no line to land on
    verdict_paras = sum(1 for ss in paras if len(WORD_RE.findall(ss[-1])) <= VERDICT_LINE_WORDS)
    close = None
    if sents:
        last = sents[-1].rstrip(" \"'”)]")
        if last.endswith("?"):
            close = "question"
        elif len(WORD_RE.findall(last)) <= VERDICT_LINE_WORDS:
            close = "short line"
        else:
            close = "longer sentence"
    return {
        "words": len(words),
        "marker_counts": {w: counts.get(w, 0) for w in marker_words},
        "marker_rates": {w: 100.0 * counts.get(w, 0) / nw for w in marker_words},
        "opener": top, "opener_count": top_n,
        "opener_share": 100.0 * top_n / len(sents) if sents else None,
        "verdict_paras": verdict_paras, "paras": len(paras),
        "verdict_share": 100.0 * verdict_paras / len(paras) if paras else None,
        "close": close,
    }


def above_own_rate(mine, others, draft):
    """What the draft does more than the person does, piece for piece (after the --check mode
    of the voice-baseline census): a writer that learns from someone's pieces drifts toward their
    most frequent choices, and a habit used five times as often turns into a caricature. A reading
    for the judge, never a fail."""
    out = {"read": False, "pieces": len(mine), "lines": []}
    if len(mine) < MIN_PIECES_ABOVE:
        out["reason"] = (f"There are {len(mine)} of your pieces; this section needs at least {MIN_PIECES_ABOVE} "
                         "to know your usual rate.")
        return out
    markers = [m["word"] for m in (zeta_markers(mine, others)[0] if others else [])]
    rows = [shape_of(d["text"], markers) for d in mine]
    df = shape_of(draft, markers)
    lines = []
    for w in markers:
        rates = [r["marker_rates"][w] for r in rows]
        p85 = percentile(rates, 85)
        if df["marker_counts"][w] >= 2 and df["marker_rates"][w] > p85:
            lines.append({"kind": "marker word", "what": w, "draft": round(df["marker_rates"][w], 2),
                          "draft_count": df["marker_counts"][w], "yours_median": round(percentile(rates, 50), 2),
                          "yours_p85": round(p85, 2), "unit": "per 100 words"})
    lines.sort(key=lambda x: x["draft"] - x["yours_p85"], reverse=True)
    shares = [r["opener_share"] for r in rows if r["opener_share"] is not None]
    if df["opener_share"] is not None and shares and df["opener_count"] >= 3 \
            and df["opener_share"] > percentile(shares, 85):
        lines.append({"kind": "opener", "what": df["opener"], "draft": round(df["opener_share"], 1),
                      "draft_count": df["opener_count"], "yours_median": round(percentile(shares, 50), 1),
                      "yours_p85": round(percentile(shares, 85), 1), "unit": "% of sentences"})
    vs = [r["verdict_share"] for r in rows if r["verdict_share"] is not None]
    if df["verdict_share"] is not None and vs and df["verdict_paras"] >= 2 \
            and df["verdict_share"] > percentile(vs, 85):
        lines.append({"kind": "verdict lines", "what": f"{df['verdict_paras']} of {df['paras']} paragraphs",
                      "draft": round(df["verdict_share"], 1), "draft_count": df["verdict_paras"],
                      "yours_median": round(percentile(vs, 50), 1), "yours_p85": round(percentile(vs, 85), 1),
                      "unit": "% of paragraphs"})
    hrows = [house_counts(d["text"]) for d in mine]
    hd = house_counts(draft)
    for rid, c in sorted(hd["rules"].items()):
        rates = [1000.0 * r["rules"].get(rid, 0) / max(r["words"], 1) for r in hrows]
        if not any(rates):
            continue          # a pattern the person never uses: the house rules already catch it
        dr = 1000.0 * c / max(hd["words"], 1)
        p85 = percentile(rates, 85)
        if c >= 2 and dr > p85:
            lines.append({"kind": "house pattern", "what": rid, "pattern": HOUSE_RULES[rid], "draft": round(dr, 1),
                          "draft_count": c, "yours_median": round(percentile(rates, 50), 1),
                          "yours_p85": round(p85, 1), "yours_pieces": sum(1 for x in rates if x),
                          "unit": "per 1,000 words"})
    closes = Counter(r["close"] for r in rows if r["close"])
    n_close = sum(closes.values())
    if df["close"] and n_close:
        share = 100.0 * closes[df["close"]] / n_close
        out["close"] = {"draft": df["close"], "yours_share": round(share, 1), "unusual": share < 100.0 / 3}
    out.update({"read": True, "markers_checked": len(markers), "house_patterns_checked": len(hd["rules"]), "lines": lines})
    return out


def render_above(ab):
    lines = ["", "## Above your own rate", ""]
    if not ab["read"]:
        return lines + [f"This section can't be read yet. {ab['reason']}"]
    if ab["lines"]:
        lines += ["Where this draft runs above what your own pieces usually do. A reading, never a fail.", ""]
    else:
        lines.append("No marker word, opener, paragraph ending or house-rule pattern in this draft runs above your own rate.")
    for x in ab["lines"]:
        if x["kind"] == "marker word":
            lines.append(f"- **\"{x['what']}\":** this draft {x['draft']:.1f} per 100 words ({x['draft_count']} uses); "
                         f"your usual {x['yours_median']:.1f}.")
        elif x["kind"] == "opener":
            lines.append(f"- **Sentences opening with \"{x['what'].capitalize()}\":** this draft {x['draft']:.0f}% of "
                         f"sentences; your usual for your most repeated opener {x['yours_median']:.0f}%.")
        elif x["kind"] == "verdict lines":
            lines.append(f"- **Paragraphs ending on a line of {VERDICT_LINE_WORDS} words or fewer:** this draft "
                         f"{x['draft']:.0f}% ({x['what']}); your usual {x['yours_median']:.0f}%.")
        elif x["kind"] == "house pattern":
            lines.append(f"- **{x['what']}, {x['pattern']}:** this draft {x['draft']:.1f} per 1,000 words "
                         f"({x['draft_count']} uses); your usual {x['yours_median']:.1f}, and {x['yours_p85']:.1f} or less "
                         f"in most of your pieces. This holds even when the rule is excepted as yours.")
    c = ab.get("close")
    if c:
        if not ab["lines"]:
            lines.append("")
        lines += [f"- **How it closes:** this draft ends on a {c['draft']}; {c['yours_share']:.0f}% of your "
                  "pieces end that way."]
    return lines


def cmd_score(a):
    if getattr(a, "draft_label", None):
        os.environ["STUDIO_DRAFT"] = a.draft_label.upper()
    try:
        labels = re.findall(r"^## Post[ \t]+([A-Z])[ \t]*$", open(a.draft, encoding="utf-8").read(), flags=re.M)
    except Exception:
        labels = []
    if len(labels) > 1 and not os.environ.get("STUDIO_DRAFT"):
        sys.exit(f"voiceprint: {a.draft} holds Posts {', '.join(labels)}. The reading runs once per piece, "
                 f"on the draft the judge picked: add --draft {' or '.join(labels)}.")
    mine, others = load_corpora(a)
    draft_docs = load_texts(a.draft)
    if not draft_docs:
        sys.exit(f"voiceprint: {a.draft} is empty")
    draft = "\n\n".join(d["text"] for d in draft_docs)
    dw = len(WORD_RE.findall(draft))
    size = max(dw, a.min_chunk)
    an = Analysis(mine, others, size, n_mfw=a.mfw)
    rd = an.reading(draft)
    sep = an.separation()
    mine_words = word_count(mine)
    warnings = profile_warnings(len(mine), mine_words, len(others), word_count(others))
    # No verdict when the method can't tell the person from the comparison set at this
    # length, or when there's too little of their writing (Eder 2015, 2017: results
    # below ~2,000-5,000 words are unstable). The style flags still apply.
    gated = None
    if sep != sep or sep < MIN_SEPARATION:
        gated = (f"At {dw} words, the method can only tell your pieces from the comparison set "
                 f"{sep * 100:.0f}% of the time, so it gives no verdict.")
    elif mine_words < MIN_MINE_WORDS:
        gated = (f"There are {mine_words:,} words of your writing; the verdict needs at least "
                 f"{MIN_MINE_WORDS:,} to be worth reading.")
    if gated:
        rd["verdict"] = "no verdict yet"
    gi = gi_own = gi_oth = None
    if not a.no_impostors:
        gi = an.impostors(rd["z"], iters=a.iters)
        gi_own, gi_oth = an.impostor_calibration(iters=max(30, a.iters // 2))
    mt = feature_table(an.mine)
    ot = feature_table(an.others)
    df = style_features(draft)
    flags = []
    for k in FEATURES:
        lo, hi = percentile(mt[k], 15), percentile(mt[k], 85)
        val = df[k]
        if k == "ai_words":
            if val > max(hi, 0) and val > 0:
                flags.append((k, val, lo, hi, "high"))
            continue
        spread = statistics.pstdev(mt[k]) if len(mt[k]) > 1 else 0.0
        margin = 0.25 * spread
        if val < lo - margin:
            flags.append((k, val, lo, hi, "low"))
        elif val > hi + margin:
            flags.append((k, val, lo, hi, "high"))
    # rank flags by how far outside, in your own spreads
    def dist(f):
        k, val, lo, hi, side = f
        s = statistics.pstdev(mt[k]) or 1e-9
        return (lo - val) / s if side == "low" else (val - hi) / s
    flags.sort(key=dist, reverse=True)
    result = {
        "file": a.draft, "words": dw, "date": _dt.datetime.now().isoformat(timespec="seconds"),
        "verdict": rd["verdict"], "fit": round(rd["fit"], 3),
        "closer_than_share_of_others": round(rd["closer_than_others"], 3),
        "cosine_delta": round(rd["cosine_delta"], 4), "burrows_delta": round(rd["burrows_delta"], 4),
        "style_distance": round(rd["style_distance"], 4),
        "separation": round(sep, 3),
        "impostors": None if gi is None else round(gi, 3),
        "impostors_your_texts_median": None if not gi_own else round(percentile(gi_own, 50), 3),
        "impostors_others_median": None if not gi_oth else round(percentile(gi_oth, 50), 3),
        "flags": [{"feature": k, "draft": round(val, 3), "your_range": [round(lo, 3), round(hi, 3)], "side": side}
                  for k, val, lo, hi, side in flags],
        "ai_words_found": ai_words_found(draft),
        "pieces": {"mine": len(an.mine), "others": len(an.others), "length": size, "mfw": len(an.mfw)},
        "own_fit": {"median": round(percentile(an.own_fit, 50), 3),
                    "reads_like_you": round(sum(x >= FIT_READS_LIKE_YOU for x in an.own_fit) / max(len(an.own_fit), 1), 3),
                    "close": round(sum(FIT_CLOSE <= x < FIT_READS_LIKE_YOU for x in an.own_fit) / max(len(an.own_fit), 1), 3)},
        "mine_words": mine_words,
        "gated": gated,
        "warnings": warnings,
        "above_own_rate": above_own_rate(mine, others, draft),
    }
    report = render_score(result, an, mt, ot, df)
    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(report)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(report)
    if a.log:
        os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
        with open(a.log, "a", encoding="utf-8") as f:
            f.write(json.dumps(result) + "\n")


def render_score(r, an, mt, ot, df):
    pct = lambda x: f"{x * 100:.0f}%"
    lines = [f"# Voiceprint reading: {os.path.basename(r['file'])}", ""]
    if r["gated"]:
        lines += [f"**No verdict yet.** {r['gated']} The style checks below still hold: they compare the draft "
                  "with your usual ranges one measure at a time. To get a verdict, add more of your own writing, "
                  "and keep rewriting studio drafts: every pair in bank/rewrites/ joins the comparison set."]
    else:
        lines += [f"**{r['verdict'].capitalize()}.** Fit {pct(r['fit'])}: the draft sits at least as close to your "
                  f"writing as {pct(r['fit'])} of your own pieces do, on word habits and on style, and closer "
                  f"than {pct(r['closer_than_share_of_others'])} of the comparison pieces. The fit takes the lower of the "
                  "two, so a draft has to match on both. 'Reads like you' starts at 25% and 'close' at 10%.",
                  "", f"For scale, your own pieces scored the same way: a typical one fits {pct(r['own_fit']['median'])}, "
                  f"{pct(r['own_fit']['reads_like_you'])} read like you and {pct(r['own_fit']['close'])} come out "
                  "close. One reading is a signal, not a ruling."]
        sep = r["separation"]
        lines += ["", f"At this length the method tells your pieces from the comparison set {pct(sep)} of the time, "
                  + ("so the reading is reliable." if sep >= 0.85 else "so read it as fair, not certain.")
                  + " That holds only as far as the comparison set looks like what you're up against: other "
                  "writers in your formats and the studio's own drafts."]
        if r["impostors"] is not None:
            lines += ["", f"Impostor test: in {pct(r['impostors'])} of the random trials the draft sat closer to your "
                      f"pieces than to any comparison piece. Your own pieces score a median of "
                      f"{pct(r['impostors_your_texts_median'])} on the same test; comparison pieces score "
                      f"{pct(r['impostors_others_median'])}."]
            if r["impostors"] >= 0.5 and r["verdict"] == "off":
                lines += ["", "The two disagree because the impostor test only looks at word habits, which a draft on "
                          "your topics can match. The style measures below are where this draft misses."]
    for w in r.get("warnings", []):
        lines += ["", f"> Note: {w}"]
    lines += ["", "## What to change", ""]
    if not r["flags"]:
        lines.append("Nothing in the style measures falls outside your usual range.")
    for f in r["flags"][:8]:
        k = f["feature"]
        label, unit, _ = FEATURES[k]
        adv = ADVICE[k][0 if f["side"] == "low" else 1]
        lines.append(f"- **{label}:** this draft {fmt_num(k, f['draft'])}, you usually "
                     f"{fmt_num(k, f['your_range'][0])} to {fmt_num(k, f['your_range'][1])} ({unit}). {adv}")
    if r["ai_words_found"]:
        lines.append(f"- **AI-typical words in the draft:** {', '.join(r['ai_words_found'])}. Replace them unless you'd say them.")
    if r["flags"] or r["ai_words_found"]:
        lines += ["", "Fix these once, the way the person would say it. Don't rewrite to chase the numbers."]
    if r.get("above_own_rate"):
        lines += render_above(r["above_own_rate"])
    lines += ["", "## All measures", "", "| Measure | Draft | Your usual range | Others' median |", "| --- | --- | --- | --- |"]
    for k, (label, unit, _) in FEATURES.items():
        lines.append(f"| {label} ({unit}) | {fmt_num(k, df[k])} | {fmt_num(k, percentile(mt[k], 15))} to "
                     f"{fmt_num(k, percentile(mt[k], 85))} | {fmt_num(k, percentile(ot[k], 50))} |")
    p = r["pieces"]
    lines += ["", f"Compared against {p['mine']} pieces of your writing and {p['others']} by others, cut to about "
              f"{p['length']} words to match the draft, on the {p['mfw']} most frequent words. "
              f"Cosine Delta {r['cosine_delta']}, Burrows's Delta {r['burrows_delta']}, "
              f"style distance {r['style_distance']}.", ""]
    return "\n".join(lines)


def pair_changes(d, r):
    fd, fr = style_features(d), style_features(r)
    wd, wr = Counter(words_of(d)), Counter(words_of(r))
    added = [w for w in wr if wr[w] > wd.get(w, 0) and w not in PAIRS_SKIP]
    removed = [w for w in wd if wd[w] > wr.get(w, 0) and w not in PAIRS_SKIP]
    return fd, fr, added, removed


def cmd_patterns(a):
    if a.draft or a.rewrite:
        if not (a.draft and a.rewrite):
            sys.exit("voiceprint patterns: give both a DRAFT and the person's REWRITE, or neither")
        d = "\n\n".join(x["text"] for x in load_texts(a.draft))
        r = "\n\n".join(x["text"] for x in load_texts(a.rewrite))
        fd, fr, added, removed = pair_changes(d, r)
        print(f"# What changed: {os.path.basename(a.draft)} to {os.path.basename(a.rewrite)}\n")
        print("| Measure | Draft | Rewrite |\n| --- | --- | --- |")
        for k, (label, unit, _) in FEATURES.items():
            if abs(fr[k] - fd[k]) > 1e-9:
                print(f"| {label} ({unit}) | {fmt_num(k, fd[k])} | {fmt_num(k, fr[k])} |")
        print(f"\nWords added: {', '.join(added[:20]) or 'none'}")
        print(f"Words cut: {', '.join(removed[:20]) or 'none'}")
        return
    pairs = load_rewrite_pairs(a.rewrites)
    n = len(pairs)
    if not n:
        sys.exit(f"voiceprint: no rewrite pairs with both sides filled in {a.rewrites}")
    rows_ = [pair_changes(st, pe) for _, st, pe in pairs]
    print(f"# What the rewrites have in common, measured ({n} pair{'s' if n != 1 else ''} in {a.rewrites})\n")
    if n < 3:
        print("Fewer than 3 pairs. Patterns below are a first read.\n")
    rows = []
    for k in FEATURES:
        ups = sum(1 for fd, fr, _, _ in rows_ if fr[k] > fd[k] * 1.05 + 1e-6)
        downs = sum(1 for fd, fr, _, _ in rows_ if fr[k] < fd[k] * 0.95 - 1e-6)
        if max(ups, downs) >= max(2, math.ceil(n * 0.6)):
            rows.append((max(ups, downs), k, "up" if ups > downs else "down"))
    rows.sort(reverse=True)
    print("## Consistent changes in style\n")
    if not rows:
        print("No measure moves the same way in most rewrites yet.")
    for cnt, k, side in rows:
        label, unit, _ = FEATURES[k]
        shown = label if label.startswith(("I ", "I /")) else label[0].lower() + label[1:]
        print(f"- In {cnt} of {n} rewrites, **{shown}** went {side} ({unit}).")
    added, removed = Counter(), Counter()
    for _, _, ad, rm in rows_:
        added.update(set(ad))
        removed.update(set(rm))
    thresh = max(2, math.ceil(n * 0.4))
    common_add = sorted(((c - removed.get(w, 0), w) for w, c in added.items() if c - removed.get(w, 0) >= thresh), reverse=True)
    common_cut = sorted(((c - added.get(w, 0), w) for w, c in removed.items() if c - added.get(w, 0) >= thresh), reverse=True)
    print("\n## Words the person keeps adding\n")
    print("Net count: rewrites that added the word minus rewrites that cut it.\n")
    print(", ".join(f"{w} ({c})" for c, w in common_add[:25]) or "None yet.")
    print("\n## Words the person keeps cutting\n")
    print(", ".join(f"{w} ({c})" for c, w in common_cut[:25]) or "None yet.")
    print("\nThese measure what the pairs' 'What changed' lines describe by hand. A pattern here that no line "
          "or rule records yet is a candidate for a `new` tag and a voice-guide proposal; the person decides. "
          "A pattern in a handful of rewrites can be chance.")


def cmd_markers(a):
    mine, others = load_corpora(a)
    markers, anti = zeta_markers(mine, others, seg=a.segment)
    if a.json:
        print(json.dumps({"markers": markers, "anti_markers": anti}, indent=2))
        return
    print("# Marker words (Craig's Zeta)\n")
    print("Share of your pieces that use the word, against the share of other writers' pieces.\n")
    print("## You use these more\n\n| Word | Yours | Others | Small word? |\n| --- | --- | --- | --- |")
    for m in markers:
        print(f"| {m['word']} | {m['mine'] * 100:.0f}% | {m['others'] * 100:.0f}% | {'yes' if m['function_word'] else ''} |")
    print("\n## You use these less\n\n| Word | Yours | Others | Small word? |\n| --- | --- | --- | --- |")
    for m in anti:
        print(f"| {m['word']} | {m['mine'] * 100:.0f}% | {m['others'] * 100:.0f}% | {'yes' if m['function_word'] else ''} |")


def main(argv=None):
    if hasattr(__import__("signal"), "SIGPIPE"):
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # exit quietly when output is cut short
    ap = argparse.ArgumentParser(prog="voiceprint", description=__doc__.split("\n\n")[0])
    ap.add_argument("--version", action="version", version=VERSION)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("profile", help="build the voiceprint and writer targets")
    add_corpus_args(p)
    p.add_argument("--out", default=DEFAULT_PROFILE)
    p.add_argument("--targets", default=DEFAULT_TARGETS)
    p.set_defaults(func=cmd_profile)

    s = sub.add_parser("score", help="check a draft against the person's writing")
    s.add_argument("draft")
    s.add_argument("--draft", dest="draft_label", metavar="LABEL",
                   help="which of Posts A, B, C to read, when the draft file holds three (the one the judge picked)")
    add_corpus_args(s)
    s.add_argument("--mfw", type=int, default=300, help="most frequent words to compare on (default 300)")
    s.add_argument("--min-chunk", type=int, default=150, help="shortest piece length for comparison (default 150 words)")
    s.add_argument("--iters", type=int, default=100, help="impostor trials (default 100)")
    s.add_argument("--no-impostors", action="store_true", help="skip the impostor test (faster)")
    s.add_argument("--json", action="store_true", help="print the result as JSON")
    s.add_argument("--out", help="also write the report to this file")
    s.add_argument("--log", default=DEFAULT_LOG, help="append the reading to this log ('' to skip)")
    s.set_defaults(func=cmd_score)

    q = sub.add_parser("patterns", help="what the rewrites in bank/rewrites/ have in common, measured")
    q.add_argument("draft", nargs="?", help="optional: compare one draft ...")
    q.add_argument("rewrite", nargs="?", help="... with the person's rewrite of it, without reading bank/rewrites/")
    q.add_argument("--rewrites", default=DEFAULT_REWRITES)
    q.set_defaults(func=cmd_patterns)

    m = sub.add_parser("markers", help="words the person uses more, and less, than others")
    add_corpus_args(m)
    m.add_argument("--segment", type=int, default=150, help="segment length in words (default 150)")
    m.add_argument("--json", action="store_true")
    m.set_defaults(func=cmd_markers)

    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
