"""The lists and matchers the studio's check scripts share, kept in one place so they can't drift
apart. Imported by check-mechanical.py, check-human.py, check-prose.py, check-stitch.py, voice-diff.py
and voiceprint.py, and by tests/studio/house-rules/run.py. Import it from a script in this folder:

    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import studio_checks

It holds no facts about any person.
"""
import re

APOS = "['’]"   # a straight or a curly apostrophe

# Reveal devices, in their withhold form only: the line holds the point back and ends there
# ("Here's the thing." then the point in the next sentence). The same words followed by a colon and
# the point ("Here's why: the P&L looks back") are an explanation and pass. "So:" is never flagged.
REVEAL = re.compile(
    rf"\bHere{APOS}s (?:the thing|the kicker|the catch|the truth|the problem|the twist|why|how|what (?:I learned|I found|happened|matters|changed|I mean|nobody tells you))\s*[.!]"
    r"|\bThe (?:result|truth|catch|kicker|twist|answer)\?"
    r"|\bLet that sink in\b"
    r"|\bRead that again\b",
    re.I,
)

# Decoration adverbs: words that decorate a claim instead of doing work. One list for both scripts.
DECORATION = ["quietly", "truly", "deeply", "incredibly", "remarkably", "profoundly",
              "seamlessly", "effortlessly", "undeniably", "fundamentally"]
DECORATION_RE = re.compile(r"\b(" + "|".join(DECORATION) + r")\b", re.I)

# Stance words a talker uses. They stay in a draft; zero of them is a reason to read for stance.
STANCE = ["actually", "honestly", "to be honest", "i'd say", "i think", "kinda", "kind of", "sort of",
          "way too", "way more", "pretty much", "not necessarily", "basically", "in my experience",
          "i've found", "i'm not sure", "probably", "maybe", "at least", "frankly", "i guess",
          "i don't think", "i'm not convinced", "i doubt", "i'd argue", "to me", "if you ask me", "i'm pretty sure",
          "i get why", "i get it", "to be fair", "fair enough", "i'll admit", "i still think", "i'm not saying", "my guess", "i suspect", "just"]

def stance_count(text):
    low = text.lower().replace("’", "'")
    return sum(len(re.findall(rf"\b{re.escape(w)}\b", low)) for w in STANCE)

# A speaker in the room: first person only ("you" alone is a billboard). Case-insensitive, so a
# sentence that starts "My" or "We" counts the same as one with "my" or "we" in the middle.
SPEAKER = re.compile(rf"\b(?:I|I{APOS}m|I{APOS}ve|I{APOS}d|I{APOS}ll|me|my|we|we{APOS}re|we{APOS}ve|our)\b", re.I)

# "Not X. Y." pairs. Flagged only when both sides are short fragments: the "Not" segment is six words
# or fewer and has none of the finite verb words in FINITE, and the next sentence is six words or
# fewer. "Not a crisis. A warning." is flagged; "Not because it was late. The client had moved on
# to a new vendor." is not, since the first side has a verb and the second is a full sentence.
FINITE = {"is", "was", "are", "were", "am", "be", "do", "does", "did", "has", "have", "had", "can", "will",
          "would", "should", "could", "may", "might", "must", "shall",
          "isn't", "wasn't", "aren't", "weren't", "don't", "doesn't", "didn't", "hasn't", "haven't", "hadn't",
          "can't", "cannot", "won't", "wouldn't", "shouldn't", "couldn't", "it's", "that's", "there's"}
_NOT_PAIR = re.compile(r"(?:^|(?<=[.!?]\s)|(?<=[.!?][\"”]\s))(Not\b[^.!?\n]*[.!?])\s+([A-Z\"“][^.!?\n]*[.!?])", re.M)

def _words(s):
    return re.findall(r"[\w'’&$%-]+", s)

def not_x_y(text):
    """Every "Not X. Y." fragment pair in the text, as (offset, the matched text)."""
    out = []
    for m in _NOT_PAIR.finditer(text):
        first, second = _words(m.group(1)), _words(m.group(2))
        if len(first) > 6 or len(second) > 6:
            continue
        if any(w.lower().replace("’", "'") in FINITE for w in first):
            continue
        out.append((m.start(1), m.group(0)))
    return out

# The five kinds a source map row can have.
KINDS = ["verbatim", "said again", "writer", "borrowed: verify", "inferred"]
NUMBER_KINDS = {"verbatim", "said again", "borrowed: verify"}   # rows whose numbers count as sourced

def norm_kind(cell):
    k = re.sub(r"[`*_\"]", "", cell or "").strip().lower()
    return re.sub(r"\s+", " ", re.sub(r"\s*:\s*", ": ", k))

# ---------------------------------------------------------------------------------------------
# House rules (skills/craft-house-rules/SKILL.md). These lists are the machine-readable half of
# that file. Change a rule there first, then the list here. Three tiers:
#   AI_TELLS   words and phrases that almost never appear in a person's own prose. A fail (H21).
#   AI_LIKELY  phrases that are usually machine filler but turn up in real prose. A flag; the judge decides.
#   LATINATE   the complex word where a plain one exists (H2). A flag.
# A match inside a quoted line (> ...) or a source map never counts: those are the person's or a
# source's words.

AI_TELLS = [
    # chat residue and sycophancy (Pangram: "Sure! Here's" 70x the human rate; Wikipedia AI Cleanup)
    "certainly!", "of course!", "sure! here", "i hope this helps", "hope this helps", "would you like me to",
    "is there anything else", "i'd be happy to", "i would be happy to", "here's a comprehensive", "a more detailed breakdown",
    "great question", "that's a great question", "you're absolutely right", "you're touching on",
    "as an ai", "as a language model", "as a large language model", "as of my last knowledge", "my last training update",
    # the opener family (Pangram: 35x)
    "in today's fast-paced world", "in today's digital age", "in today's world", "in the digital age",
    "in this day and age", "in the modern era", "in an era of", "in the ever-evolving", "ever-evolving landscape",
    "rapidly evolving landscape",
    # the words with the strongest corpus evidence (Kobak 2024: delve 28x; Reinhart 2025: tapestry 100x)
    "delve", "delves", "delved", "delving", "tapestry",
    # the editorializing family (Pangram: "crucial to note" 22x)
    "it's important to note", "it is important to note", "it's crucial to note", "it is crucial to note",
    "it should be noted", "it's worth noting", "it is worth noting", "worth noting that", "it's worth mentioning",
    # engagement filler
    "let's dive in", "let's dive into", "without further ado", "look no further", "buckle up",
    "the answer might surprise you", "you might be surprised",
]

# Vocabulary that marks machine text in clusters, not alone. Three or more distinct words from this list per
# 500 words is a fail; one or two is a flag. (Wikipedia AI Cleanup's study-backed list; Juzek and Ward 2025;
# Liang et al. 2024; Reinhart et al. 2025.)
AI_VOCAB = [
    "showcasing", "showcases", "showcase", "boasts", "underscore", "underscores", "underscoring", "comprehending",
    "intricacies", "intricate", "surpassing", "surpasses", "garnered", "garner", "emphasizing", "realm", "groundbreaking",
    "advancements", "aligns with", "pivotal", "crucial", "meticulous", "meticulously", "commendable", "multifaceted",
    "a vital role", "a crucial role", "testament to", "a testament", "bolstered", "enduring", "interplay", "vibrant",
    "seamless", "seamlessly", "holistic", "harness", "unleash", "elevate", "navigate the", "navigating the", "landscape of",
    "beacon", "cornerstone", "paramount", "noteworthy", "transformative", "game-changer", "game changer", "game-changing",
    "synergy", "synergies", "paradigm shift", "embark", "embarking", "camaraderie", "palpable", "amidst",
    "cutting-edge", "state-of-the-art", "robust framework", "holistic approach", "actionable insights", "key takeaways",
    "foster", "fosters", "fostering", "cultivate", "empower", "empowering", "empowers", "impactful", "mindset shift",
    "in conclusion", "to sum up", "in summary,", "ultimately, the", "the bottom line is", "in a nutshell", "in essence",
    "furthermore", "moreover", "additionally", "consequently", "firstly", "secondly", "thirdly",
    "plays a crucial role", "plays a vital role", "cannot be overstated", "shining example", "beacon of", "cornerstone of",
    "whether you're a", "whether you are a", "a wide range of", "deep dive", "dive deep", "let's explore", "let's unpack",
    "supercharge", "revolutionize", "leverage the power", "harness the power", "unlock the power",
    "undeniably", "nestled", "in the heart of", "rich cultural heritage", "renowned", "diverse array", "breathtaking",
    "enduring legacy", "indelible mark", "setting the stage", "key turning point", "marks a pivotal",
    # added 0.80.0 (Corey Haines, ella79, sergebulaev, Juelinton)
    "nuanced", "keen", "whilst", "enhance", "enhances", "enhancing", "highlighting", "exemplifies", "deeply rooted",
    "notably", "spearhead", "spearheading", "amplify", "unparalleled", "invaluable", "bespoke", "plethora", "myriad",
    "treasure trove", "arsenal of", "orchestrate", "revolutionary", "unprecedented", "world-class",
]

AI_LIKELY = [
    "not just", "not only", "not merely", "more than just", "isn't just", "is more than", "it's not about", "it's about",
    "the truth is", "the reality is", "the fact is", "make no mistake", "here's the kicker", "here's the catch",
    "think again", "spoiler alert", "plot twist", "stop scrolling", "hot take", "unpopular opinion",
    "unlock", "streamline", "scalable", "insightful", "the importance of", "is key to", "a journey", "your journey",
    "at the heart of", "lies in", "the key lies", "stands as a", "serves as a", "essentially", "fundamentally", "arguably", "indeed",
    "at the end of the day", "when it comes to", "the key is", "the secret is", "the secret to",
    "here's why", "here's how", "here's what", "the thing is", "truth be told", "simply put", "put simply",
    "the good news is", "the bad news is", "the problem is", "the result?", "the catch?",
    "picture this", "imagine this", "imagine a world", "think about it", "think of it as", "think of it like",
    "take a step back", "zoom out", "double down", "level up", "move the needle", "low-hanging fruit",
    "circle back", "touch base", "best practices", "next level", "north star", "secret sauce", "silver bullet",
    "a recipe for", "the perfect storm", "a double-edged sword", "the tip of the iceberg", "a no-brainer",
    "food for thought", "at the forefront", "in the grand scheme", "on the same page", "think outside the box",
    "the elephant in the room", "push the envelope", "hit the ground running", "raise the bar",
    "it goes without saying", "needless to say", "as you can see", "as mentioned", "as we all know", "we all know",
    "everyone knows", "nobody talks about", "no one talks about", "what most people", "most people",
    "the vast majority", "most founders", "most creators", "most leaders", "most marketers",
    "rest assured", "to be clear", "make sense?", "sound familiar?", "does this sound familiar",
    "ever wondered", "have you ever", "what if i told you", "did you know",
    "that's the point", "that's the whole point", "and that's okay", "and that's fine", "and that matters",
    "this is where", "this is why", "that's why", "which is why", "and that's exactly",
    "the difference between", "there's a difference", "big difference",
    # added 0.80.0: throat-clearing, faux insight, LinkedIn openers and closers (sergebulaev, ella79, Juelinton, kvsdileep)
    "let's be honest", "let's break this down", "let's face it", "it's no secret that", "we've all been there",
    "the part everyone misses", "what they don't tell you", "what nobody tells you", "in recent years",
    "that's the real story", "doing the heavy lifting", "load-bearing", "it turns out", "at its core", "in a world where",
    "lean into", "full stop.", "a feature, not a bug", "but that's another post", "can we talk about",
    "excited to share", "excited to announce", "thrilled to share", "thrilled to announce", "humbled to",
    "had the opportunity to", "drop a comment", "comment below", "save this for later", "save this post",
    "who's with me", "tag someone", "repost if", "agree?", "thoughts?", "what are your thoughts",
    "the future is here", "the future of work", "the choice is yours", "the future looks bright", "you're welcome.",
    "no matter if you're", "in today's market", "in today's landscape",
]

LATINATE = {
    "utilize": "use", "utilise": "use", "utilization": "use", "facilitate": "help", "leverage": "use",
    "implement": "do or set up", "commence": "start", "terminate": "end", "subsequently": "then",
    "prior to": "before", "in order to": "to", "numerous": "many", "endeavor": "try", "ascertain": "find out",
    "methodology": "method", "paradigm": "model", "robust": "strong", "holistic": "whole",
    "comprehensive": "full", "optimize": "improve", "optimal": "best", "demonstrate": "show",
    "indicate": "show", "approximately": "about", "sufficient": "enough", "additional": "more",
    "assistance": "help", "obtain": "get", "purchase": "buy", "require": "need", "possess": "have",
    "regarding": "about", "concerning": "about", "component": "part", "individuals": "people",
    "initiate": "start", "attempt": "try", "necessitate": "need", "ameliorate": "improve",
    "articulate": "say", "conceptualize": "think up", "operationalize": "put to work",
    "actionable": "something you can do", "impactful": "that matters", "insightful": "sharp",
    "resonate": "land", "resonates": "lands", "resonated": "landed", "curate": "pick", "curated": "picked",
    "ecosystem": "the people and tools around it", "narrative": "story", "journey": "the road",
}

def latinate_pattern(w):
    """The word and its inflected forms: utilize, utilizes, utilized, utilizing; leverage, leveraging."""
    if " " in w or not w.isalpha():
        return re.escape(w)
    if w.endswith("e"):
        return re.escape(w[:-1]) + r"(?:e|es|ed|ing)"
    if w.endswith("y") or w.endswith("ly") or w.endswith("al") or w.endswith("ous"):
        return re.escape(w)
    return re.escape(w) + r"(?:s|ed|ing)?"

PLACEHOLDER = re.compile(r"\[(?:YOUR|INSERT|ADD|TBD|TODO|NAME|EXAMPLE|CLIENT|NUMBER|X)\b[^\]]*\](?!\()|_{3,}|\bTBD\b|\bTODO\b|\blorem ipsum\b", re.I)   # a markdown link [text](url) is not a placeholder

# "it's not about X, it's about Y" and "not just X, but Y" in their full-sentence forms (H17; the fragment form is not_x_y above)
NOT_ABOUT = re.compile(
    rf"\b(?:it|this|that)(?:{APOS}s| is| isn{APOS}t| is not) (?:not |)(?:just |only |merely |really |)about\b[^.!?\n]{{0,80}}?\b(?:it|this|that)(?:{APOS}s| is) about\b"
    rf"|\bnot (?:just|only|merely) \w[^.!?\n]{{0,60}}?,? but (?:also |rather |)\w",
    re.I,
)

# More H17 forms the two above miss (sergebulaev's NEG_PARALLEL_PATTERNS, ella79's slop.json, Juelinton's sanitizer):
# "This isn't a tactic. This is a philosophy." "It isn't about money. It's about attention." (across a full stop)
# "The real problem isn't money, it's attention." "It's not just a tool, it's a system." "Not a tactic, but a habit."
NOT_SWAP = re.compile(
    rf"\b(?:it|this|that|these|those)(?:{APOS}s not| is not| isn{APOS}t| are not| aren{APOS}t| was not| wasn{APOS}t)\s+(?:just |only |merely |really |)(?:about )?[^.!?\n;]{{1,50}}[.!?]\s+(?:it|this|that|these|those)(?:{APOS}s| is| are| was)\s+(?:about )?\w"
    rf"|\b(?:isn{APOS}t|is not|aren{APOS}t|are not|wasn{APOS}t|was not|{APOS}s not)\s+(?:just |only |merely |really |)[^.!?\n,;]{{1,40}},\s+(?:it{APOS}s|it is|they{APOS}re|they are|that{APOS}s|this is|it was)\s+\w"
    rf"|(?:^|(?<=[.!?]\s)|(?<=\n))Not (?:a |an |the |just |only |)[^.!?\n,]{{1,30}},? but (?:a |an |the |)\w",
    re.M | re.I,
)

# Second-generation tells: patterns a draft still shows after the first-generation list is cleaned out.
# Flags for the judge, never fails: each has an honest use, and the person's own words win (the exception
# principle). Sources: Corey Haines' ai-tells.md, sergebulaev's scrub-rules.md, Juelinton's sanitizer,
# ella79's slop.json, COG's no-ai-slop (tells measured on current models). Last checked 2026-10-27; tells
# age with the models, so the librarian's studio-notes pass rechecks them about every six months.
SENTENCE_START = r"(?:^|(?<=[.!?]\s)|(?<=[.!?][\"”]\s)|(?<=\n))"
SECOND_GEN = [
    ("H22 staged sincerity (state the fact flat)", re.compile(SENTENCE_START + rf"(?:let me be (?:honest|clear|real)|i{APOS}ll be honest|honestly\?|real talk|full transparency|i{APOS}ll say the quiet part|can i be vulnerable|the (?:hard|harsh|uncomfortable|brutal) truth is)", re.I | re.M)),
    ("H29 negation list", re.compile(r"\bno \w+(?:[ -]\w+){0,3}, no \w+(?:[ -]\w+){0,3},? (?:and |or |)no \w", re.I)),
    ("H29 staged rhythm (No X. No Y. Just Z.)", re.compile(r"\bNo [^.!?\n]{1,30}[.,] No [^.!?\n]{1,30}[.,] (?:Just|Only) \w")),
    ("H29 staged rhythm (All the X. None of the Y.)", re.compile(r"\bAll (?:the |of the )?[^.!?\n]{1,25}\. None of (?:the )?\w")),
    ("H29 staged rhythm (Stop X. Start Y.)", re.compile(r"\bStop \w[^.!?\n]{0,30}\. Start \w")),
    ("H18 colon reveal (say it as a sentence)", re.compile(SENTENCE_START + r"(?:The (?:result|answer|truth|lesson|catch|problem|secret|best part|kicker|twist|takeaway|upshot)|One word|Two words|Three words|The short version|Bottom line|Plot twist|Spoiler|Hint): \S", re.M)),
    ("H22 weasel source (name it or cut it)", re.compile(r"\b(?:studies (?:show|have shown|suggest|find)|research (?:shows|suggests|has shown|finds)|science (?:says|shows)|industry reports?(?: show| suggest)?|data (?:shows|suggests)|many (?:argue|believe|say)|some (?:say|argue)|widely (?:regarded|considered|seen) as|it is (?:widely |often |commonly |)(?:believed|said|thought|known) that)\b", re.I)),
    ("H22 both-sides hedge", re.compile(r"\bwhile [^.!?\n]{3,60}\b(?:offers?|brings?|has|have) [^.!?\n]{0,40}\b(?:benefits|advantages|upsides)\b[^.!?\n]{0,60}\b(?:challenges|drawbacks|downsides|risks)\b", re.I)),
    ("H22 despite these challenges", re.compile(r"\bdespite (?:these|the|its|their|such) (?:challenges|setbacks|obstacles|hurdles)\b", re.I)),
    ("H22 hedge stack", re.compile(r"\b(?:could|may|might) (?:potentially|possibly)\b|\bpossibly could\b|\bcould perhaps\b", re.I)),
    ("H23 opening -ing clause", re.compile(SENTENCE_START + r"(?:Leveraging|Harnessing|Building on|Drawing on|Recognizing|Recognising|Acknowledging|Embracing|Navigating|Unlocking|Empowering|Fostering)\b[^.!?\n]{0,60},", re.M)),
    ("H29 That's it.", re.compile(rf"\bThat{APOS}s it\.(?:\s+That{APOS}s (?:the|all)\b)?")),
]

def second_gen(text, mode=None):
    """The second-generation tells in a text, as (rule, matched text, offset). Counts that need the whole
    text (parenthetical asides, bold lead-in bullets, semicolon chains, one-word paragraphs) are added
    here too, each once."""
    out = []
    for rule, rx in SECOND_GEN:
        for m in rx.finditer(text):
            out.append((rule, m.group(0)[:60], m.start()))
    words = max(len(text.split()), 1)
    asides = [m for m in re.finditer(r"\([^()\n]{3,200}\)", text) if not re.match(r"\((?:https?:|[A-Z]?\d|see |e\.g|i\.e)", m.group(0))]
    if len(asides) >= 3 and words / len(asides) < 80:
        out.append(("H23 parenthetical asides (one every %d words)" % (words // len(asides)), asides[0].group(0)[:40], asides[0].start()))
    bullets = re.findall(r"(?m)^\s*(?:[-*]|\d+\.)\s+(.*)$", text)
    bold = [b for b in bullets if re.match(r"\*\*[^*]{1,60}\*\*", b)]
    if len(bullets) >= 3 and len(bold) >= 0.8 * len(bullets):
        m = re.search(r"(?m)^\s*(?:[-*]|\d+\.)\s+\*\*", text)
        out.append(("H23 bold lead-in on every bullet", m.group(0).strip(), m.start()))
    for m in re.finditer(r"[^.!?\n]*;[^.!?\n]*;[^.!?\n]*[.!?]", text):
        out.append(("H23 semicolon chain", m.group(0).strip()[:60], m.start()))
    if mode == "piece":
        for m in re.finditer(r"(?m)^[ \t]*[A-Z][a-z]+[.!][ \t]*$", text):
            out.append(("H29 one-word paragraph", m.group(0).strip(), m.start()))
    return out

# ---------------------------------------------------------------------------------------------
# Receipts: a quote that claims to be the person's exact words must be in the file it cites, word for
# word. The map has done this since 0.77 (map-render.py); check-mechanical.py (verbatim rows) and
# check-proposals.py (quotes in proposals) use the same comparison now.
# ---------------------------------------------------------------------------------------------
def norm_quote(t):
    """Text as compared for a receipt: no export backslashes or markdown marks, straight quotes, one space, lower case."""
    t = (t or "").replace("\\", "")
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2026", "..."), ("\u00a0", " "), ("\u202f", " ")):
        t = t.replace(a, b)
    t = re.sub(r"[*_>]+", "", t)
    t = re.sub(r"\[sic\]", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()

QUOTED = re.compile(r'"([^"\n]{8,})"|\u201c([^\u201d\n]{8,})\u201d')

def quote_parts(line):
    """The parts of a quoted line that must each be found: the text inside quotation marks when the line
    has any (the rest is framing), otherwise the whole line; split at line breaks written as " / " and at "..."."""
    inside = [a or b for a, b in QUOTED.findall(line or "")]
    chunks = inside or [line or ""]
    parts = []
    for c in chunks:
        for piece in re.split(r"\s/\s|\.\.\.|\u2026", c):
            piece = norm_quote(piece).strip(' "\'').strip(" .,;:!?").strip(' "\'')   # a full stop added inside the quotation marks isn't a misquote
            if len(piece) > 3:
                parts.append(piece)
    return parts

def quote_found(line, texts):
    """True when every part of the quoted line appears word for word in one of the normalised texts."""
    parts = quote_parts(line)
    return bool(parts) and all(any(p in t for t in texts) for p in parts)

FILE_REF = re.compile(r"(?<![\w/.-])((?:[\w.-]+/)*[\w.-]+\.(?:md|txt))\b")

# A rhetorical question used as an opener (H23): the first sentence of a piece or paragraph ends in ?
RHETORICAL_OPENER = re.compile(r"(?:^|\n\s*\n)\s*(?:[A-Z][^.!?\n]{3,120}\?)", re.M)

# Passive voice, roughly (H5): a form of "to be" followed by a past participle, allowing one adverb between.
# A heuristic; it misses irregular participles without -ed/-en and catches a few adjectives. Flag only.
PASSIVE = re.compile(
    rf"\b(?:am|is|are|was|were|be|been|being|{APOS}s|{APOS}re|get|gets|got|gotten)\s+(?:\w+ly\s+)?(?:\w+ed|\w+en|built|made|done|said|told|given|taken|shown|known|seen|held|kept|left|lost|found|put|set|sent|sold|spent|thought|understood|written|read|paid|met|led|felt|brought|bought|caught|taught|chosen|driven|drawn|thrown|worn|torn|born|begun|broken|forgotten|hidden|spoken|stolen|woken|frozen)\b(?!\s+(?:to|a|an|the|this|that|it|them|him|her|us|me)\b)",
    re.I,
)
# "by" right after the participle is the strongest sign
PASSIVE_BY = re.compile(PASSIVE.pattern + r"\s+by\b", re.I)

# Part 2 (how the studio talks). Openers and narration that never belong in a reply to the person.
REPLY_FILLER = re.compile(
    rf"^\s*(?:great|good|excellent|fantastic|wonderful|awesome|perfect|love (?:this|that|it)|what a great|that{APOS}s a great|brilliant|certainly|absolutely|of course|sure thing|happy to help|i{APOS}d be happy|i hope this helps|hope this helps|let me know if you have any other questions|i understand your|thank you for sharing|thanks for sharing)\b",
    re.I | re.M,
)
REPLY_NARRATION = re.compile(
    rf"\b(?:let me (?:read|check|look|start|take a look|dive|walk you through|break (?:this|that|it) down)|i{APOS}ll now\b|i will now\b|now,? i{APOS}ll\b|first,? i{APOS}ll\b|i{APOS}m going to (?:read|check|look|start|go ahead)|going ahead and\b|as requested\b|as per your\b|i{APOS}ve (?:kept|saved|filed|noted|recorded) (?:that|this|it) (?:as|in|for|under)\b)",
    re.I,
)
# Studio labels that need a gloss when they reach the person (S4). Flag when one appears with no plain word nearby.
STUDIO_LABELS = re.compile(r"\b(canon|source map|evidence ledger|idea bank|the brief|the pipeline|the crew|the librarian|the strategist|verbatim cap|proposals\.md|frontmatter|status: \w+|anti-associations?)\b", re.I)


# Structural tells the Wikipedia AI Cleanup editors list (via TechCrunch, The Decoder, 2025). Flags; the judge decides.
# A trailing -ing clause that inflates significance: "..., emphasizing the importance of X." "..., reflecting its continued relevance."
ING_TRAILER = re.compile(r",\s+(?:emphasizing|highlighting|underscoring|reflecting|showcasing|demonstrating|signaling|signalling|marking|cementing|solidifying|reinforcing|ensuring|fostering|contributing to|paving the way|setting the stage)\b[^.!?\n]{0,80}[.!?]", re.I)
# A false range: "from X to Y" where the pair is decorative ("from intimate gatherings to global movements")
FALSE_RANGE = re.compile(r"\bfrom\s+(?:\w+\s+){1,3}to\s+(?:\w+\s+){1,3}(?:alike|and everything in between|and beyond)\b|\beverything from\b", re.I)

# What a rewrite removes from a person's prose (Voice Under Revision, 2026): contractions, first person, their
# causal connectives. voice-diff.py measures these against the person's own corpus.
CONTRACTION = re.compile(rf"\b\w+{APOS}(?:t|s|re|ve|ll|d|m)\b", re.I)
CAUSAL = re.compile(r"\b(?:because|so|since|that{0}s why|which is why|which means|so that)\b".format(APOS), re.I)

# Copula avoidance (Wikipedia AI Cleanup, GPTZero): "serves as", "stands as" where "is" would do. Flag.
COPULA_AVOID = re.compile(r"\b(?:serves as|stands as|functions as|represents a|acts as a|is characterized by)\b", re.I)
# Markdown in a post that won't render it, and emoji used as bullets or badges (Pangram: ✅ 167x the human rate)
LITERAL_BOLD = re.compile(r"\*\*[^*\n]{2,60}\*\*")
FUNCTIONAL_EMOJI = re.compile(r"[\u2705\u274c\U0001F680\U0001F4A1\U0001F525\U0001F3AF\U0001F4CA\U0001F449\u27a1\u2b50\U0001F4CC\U0001F4CB\U0001F527\u26a0]")

# Adverbs the judge decides on: stance in one mouth, decoration in another ("genuinely useful").
# "truly" is in DECORATION (a fail); a word sits in one list only.
BORDER_ADVERBS = ["genuinely", "honestly", "literally", "absolutely", "completely", "totally", "extremely", "highly", "very"]
BORDER_ADVERBS_RE = re.compile(r"\b(" + "|".join(BORDER_ADVERBS) + r")\b", re.I)
MOST_PEOPLE = re.compile(r"\b(?:most (?:people|founders|leaders|companies|marketers|creators|writers|experts|teams)|the vast majority|nobody (?:sees|talks about|tells you)|everyone (?:knows|tells you|says)|no one (?:talks about|tells you))\b", re.I)

def strip_quoted(text):
    """The studio's own words only: drop blockquotes, code, quoted text and quote/raw fields, which hold
    the person's or someone else's words (the exception principle). Keeps line count so line numbers hold."""
    keep, in_code = [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code; keep.append(""); continue
        if in_code or line.lstrip().startswith(">") or line.lstrip().startswith("|") \
                or re.match(r"^\s*[-*]?\s*(quote|raw|verbatim|their words|source|sources|log)\s*:", line, re.I) \
                or re.fullmatch(r"\s*([-_*]\s*){3,}", line):
            keep.append(""); continue
        line = re.sub(r"`[^`]*`", "", line)
        line = re.sub(r"\"[^\"\n]*\"|“[^”\n]*”", "\"\"", line)
        keep.append(line)
    return "\n".join(keep)

def find_root(path):
    import os
    d = os.path.dirname(os.path.abspath(path))
    for _ in range(8):
        if os.path.exists(os.path.join(d, "studio.manifest.yaml")): return d
        d = os.path.dirname(d)
    return os.getcwd()

RULE_EXCEPTION = re.compile(r"^\s*-\s*(?:rule\s+(H\d+)\b|(H\d+)\s*\(rule\))", re.I)

def exceptions(root):
    """The person's own uses the house rules let through (the exception principle). Two sources in
    canon/voice/voice-guide.md: the "## House-rule exceptions" section and the "Phrases he uses" /
    "Phrases they use" line under Vocabulary. Lowercased.
    The section holds two kinds of line. "- <word or phrase>: <evidence>" lets that phrase through.
    "- rule H17: <evidence>" (or "- H17 (rule): <evidence>") names a pattern the person uses in their own
    writing; it comes back as "rule:h17", and house_check turns that rule's fails into flags."""
    import os
    p = os.path.join(root or ".", "canon", "voice", "voice-guide.md")
    try: txt = open(p, encoding="utf-8").read()
    except Exception: return set()
    out = set()
    m = re.search(r"^## House-rule exceptions\s*\n(.*?)(?=^## |\Z)", txt, flags=re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            rm = RULE_EXCEPTION.match(line)
            if rm:
                out.add("rule:" + (rm.group(1) or rm.group(2)).lower()); continue
            mm = re.match(r"^\s*-\s*\"?([^\":<]+?)\"?\s*:", line)
            if mm and not mm.group(1).strip().startswith("<"): out.add(mm.group(1).strip().lower())
    m = re.search(r"^-\s*Phrases (?:he|she|they) uses?:\s*(.+)$", txt, flags=re.M)
    if m:
        for ph in re.findall(r"\"([^\"]+)\"", m.group(1)): out.add(ph.strip().lower())
    return out

def house_check(text, reply=False, allow=None, mode=None):
    """The house rules a script can decide, on the studio's own words. Returns (fails, flags), each a list
    of (rule, matched text, line). `allow` is the person's exceptions, as exceptions() returns them: a phrase
    lets that phrase through; "rule:h17" turns every H17 fail into a flag marked as their own pattern, so the
    judge still sees each use and voiceprint's "Above your own rate" can still catch overuse. mode "piece"
    adds the post-only checks."""
    own = strip_quoted(text)
    low = own.lower().replace("’", "'")
    allow = {a.lower() for a in (allow or set())}
    own_rules = {a.split(":", 1)[1].strip() for a in allow if a.startswith("rule:")}
    fails, flags = [], []
    def ln(pos): return own[:pos].count("\n") + 1
    def add(lst, rule, m_text, pos):
        if m_text.strip().lower() in allow: return
        if lst is fails and rule.split()[0].lower() in own_rules:
            flags.append((rule + " (your own pattern, excepted in the voice guide; no more often than you use it)", m_text.strip(), ln(pos)))
            return
        lst.append((rule, m_text.strip(), ln(pos)))
    for m in re.finditer("—", own): add(fails, "H16 em dash", m.group(0), m.start())
    for m in REVEAL.finditer(own): add(fails, "H18 withhold-then-reveal", m.group(0), m.start())
    for m in DECORATION_RE.finditer(own): add(fails, "H19 decoration adverb", m.group(0), m.start())
    for m in re.finditer(r"\bexperts?\b", own, re.I): add(fails, "H20 the word expert", m.group(0), m.start())
    for o, t in not_x_y(own): add(fails, "H17 Not X. Y. pair", t, o)
    for m in NOT_ABOUT.finditer(own): add(fails, "H17 not-about pair", m.group(0), m.start())
    for m in NOT_SWAP.finditer(own): add(fails, "H17 not-X-it's-Y swap", m.group(0)[:70], m.start())
    for m in PLACEHOLDER.finditer(own): add(fails, "H25 placeholder", m.group(0), m.start())
    for ph in AI_TELLS:
        for m in re.finditer(r"(?<![\w-])" + re.escape(ph) + r"(?![\w-])", low): add(fails, "H21 AI-tell phrase", ph, m.start())
    found = {}
    for ph in AI_VOCAB:
        for m in re.finditer(r"(?<![\w-])" + re.escape(ph) + r"(?![\w-])", low):
            if ph in allow: continue
            found.setdefault(ph, m.start())
    n_words = max(len(low.split()), 1)
    if found:
        cluster = len(found) >= max(3, round(3 * n_words / 500))
        for ph, pos in found.items():
            add(fails if cluster else flags, f"H21 machine vocabulary ({len(found)} distinct in {n_words} words)", ph, pos)
    for m in MOST_PEOPLE.finditer(own): add(flags, "H6 most-people claim", m.group(0), m.start())
    for m in BORDER_ADVERBS_RE.finditer(own): add(flags, "H19 adverb, judge decides", m.group(0), m.start())
    for ph in AI_LIKELY:
        for m in re.finditer(r"(?<![\w-])" + re.escape(ph) + r"(?![\w-])", low): add(flags, "H22/H23 likely tic", ph, m.start())
    for w, plain in LATINATE.items():
        for m in re.finditer(r"(?<![\w-])" + latinate_pattern(w) + r"(?![\w-])", low): add(flags, f"H2 plain word exists ({plain})", m.group(0), m.start())
    for m in PASSIVE_BY.finditer(own): add(flags, "H5 passive", m.group(0), m.start())
    for m in ING_TRAILER.finditer(own): add(flags, "H23 trailing -ing clause", m.group(0)[:60], m.start())
    for m in FALSE_RANGE.finditer(own): add(flags, "H23 decorative range", m.group(0), m.start())
    for m in COPULA_AVOID.finditer(own): add(flags, "H23 copula avoidance", m.group(0), m.start())
    for rule, t, pos in second_gen(own, mode): add(flags, rule, t, pos)
    if mode == "piece":
        for m in LITERAL_BOLD.finditer(own): add(flags, "H23 markdown bold in a post", m.group(0)[:40], m.start())
        for m in FUNCTIONAL_EMOJI.finditer(own): add(fails, "H23 emoji as a bullet or badge", m.group(0), m.start())
    if reply:
        for m in REPLY_FILLER.finditer(own): add(fails, "S6 filler or flattery opener", m.group(0), m.start())
        for m in REPLY_NARRATION.finditer(own): add(fails, "S5 process narration", m.group(0), m.start())
        for m in STUDIO_LABELS.finditer(own): add(flags, "S4 studio label, gloss it", m.group(0), m.start())
    def dedupe(xs):
        seen, out = set(), []
        for x in xs:
            k = (x[0].split()[0], x[1].lower(), x[2])
            if k not in seen: seen.add(k); out.append(x)
        return out
    return dedupe(fails), dedupe(flags)


# ---------------------------------------------------------------------------------------------
# Draft files: one ## Post section, or three (## Post A, ## Post B, ## Post C) when the draft
# stage writes three drafts for the judge to pick from. Every check script reads the post through
# post_section() and calls per_draft() first, so each of the three is measured on its own.
# ---------------------------------------------------------------------------------------------
import os as _osd, subprocess as _spd, sys as _sysd, json as _jsond

POST_HEAD = re.compile(r"^## Post(?:[ \t]+([A-Z]))?[ \t]*$", re.M)
_NEXT_H2 = re.compile(r"^## ", re.M)

def post_labels(text):
    """The draft labels in a file: [""] for a single ## Post, ["A", "B", "C"] for three drafts."""
    return [(m.group(1) or "") for m in POST_HEAD.finditer(text)]

def post_section(text, label=None):
    """The body of one ## Post section: the one named `label`, else the one named in the
    STUDIO_DRAFT environment variable (set by per_draft or --draft), else the first one.
    None when the file has no ## Post section, or no section with that label."""
    if label is None:
        label = _osd.environ.get("STUDIO_DRAFT") or None
    for m in POST_HEAD.finditer(text):
        if label is None or (m.group(1) or "") == label:
            nxt = _NEXT_H2.search(text, m.end())
            return text[m.end(): nxt.start() if nxt else len(text)].lstrip("\n")
    return None

def per_draft(script, once_only=False):
    """Call first in a check script's main(). `--draft A` measures that draft alone. When the file
    holds two or more labelled drafts and no draft is named, run the script once per draft, print
    each result under "=== Post A" (or one JSON object keyed by label with --json), and exit with
    the worst exit code. A paid or once-per-piece call (once_only, or --detector) never fans out:
    it asks for --draft instead, since it runs on the draft the judge picked."""
    argv = _sysd.argv
    if "--draft" in argv:
        i = argv.index("--draft")
        if i + 1 < len(argv):
            _osd.environ["STUDIO_DRAFT"] = argv[i + 1].upper()
            del argv[i:i + 2]
        return
    if _osd.environ.get("STUDIO_DRAFT"):
        return
    path = next((a for a in argv[1:] if a.endswith(".md") and _osd.path.isfile(a)), None)
    if not path:
        return
    try:
        labels = [l for l in post_labels(open(path, encoding="utf-8").read()) if l]
    except Exception:
        return
    if len(labels) < 2:
        return
    if once_only or "--detector" in argv:
        print(f"{_osd.path.basename(script)}: {path} holds Posts {', '.join(labels)}. This runs once per piece, "
              "on the draft the judge picked: add --draft " + " or ".join(labels) + ".")
        _sysd.exit(2)
    worst, combined = 0, {}
    for lab in labels:
        env = dict(_osd.environ, STUDIO_DRAFT=lab)
        cmd = [_sysd.executable, "-I", script] + argv[1:]
        if "--json" in argv:
            r = _spd.run(cmd, env=env, capture_output=True, text=True)
            try:
                combined[lab] = _jsond.loads(r.stdout)
            except Exception:
                combined[lab] = {"output": r.stdout.strip(), "error": r.stderr.strip()}
        else:
            print(f"=== Post {lab}", flush=True)
            r = _spd.run(cmd, env=env)
            print(flush=True)
        worst = max(worst, r.returncode)
    if "--json" in argv:
        print(_jsond.dumps(combined, indent=2))
    _sysd.exit(worst)


# ---------------------------------------------------------------------------------------------
# The person's own writing, for the voice scripts (voice-diff.py, voiceprint.py). One rule for both:
# a file in material/ counts unless it's a README, a swipe file (other people's posts the person
# kept) or a transcript (other voices in the room).
# ---------------------------------------------------------------------------------------------
NOT_MINE = re.compile(r"(?:^|/)readme\.md$|swipe[-_ ]?file|transcript|linkedin[-_ ]?comments", re.I)   # comments are theirs, but too short to measure a voice by

def corpus_files(folder):
    """The .md and .txt files under `folder` that hold the person's own writing, sorted."""
    out = []
    for root, _, files in _osd.walk(folder):
        for name in sorted(files):
            p = _osd.path.join(root, name)
            rel = _osd.path.relpath(p, folder).replace(_osd.sep, "/")
            if name.startswith(".") or not name.lower().endswith((".md", ".txt")) or NOT_MINE.search(rel):
                continue
            try:
                head = "\n".join(open(p, encoding="utf-8", errors="replace").read(2000).lstrip().splitlines()[:5])
            except OSError:
                head = ""
            if "<!-- studio: looks like a summary, not their words" in head or "<!-- studio: written for them, not by them" in head:
                continue                       # a recorder's summary or a ghostwritten piece isn't their voice
            out.append(p)
    return sorted(out)

def person_side(pair_text):
    """The person's version in a rewrite pair: the text under "## The person wrote", up to the next
    ## heading. None when the file has no such section (a README, a pair in another shape)."""
    m = re.search(r"^## The person wrote\s*\n(.*?)(?=^## |\Z)", pair_text, re.S | re.M)
    return m.group(1).strip() if m else None
