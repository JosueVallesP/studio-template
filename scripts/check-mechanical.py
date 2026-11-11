#!/usr/bin/env python3
"""The mechanical checks on a draft: the things a script can decide without judgment.
Runs before the editor reads anything. Exit code 1 when any check fails.

Usage: python3 scripts/check-mechanical.py pieces/<id>/draft-vN.md [--json]

Checks:
  house rules (script)         every rule skills/craft-house-rules marks `script`, from scripts/studio_checks.py: em dashes,
                               the word "expert", placeholders, decoration adverbs, reveal lines in their withhold
                               form ("Here's the thing."), "Not X. Y." fragment pairs. Quoted text and blockquotes
                               are the person's or someone else's words and are skipped.
  house rules (flag)           the rules marked `flag` ("most people" claims, cliches, tics for effect) come back
                               as notes for the judge, not fails
  post section                 the draft has a ## Post section (or ## Post A, B and C: each is checked on its own;
                               --draft A checks one)
  source map                   the draft has a source map table with at least one row
  IDs resolve                  every ID in the source map's "Source ID or file" column exists in canon/ or bank/
                               (T, V, A, P, B, X, S, R, O, C, G, D, W, I, Q, K); a cell naming a file adds no IDs
  IDs can feed                 a cited entry whose status is `retired` fails (rule 2); a canon `draft` and an idea or
                               credibility entry that isn't ready or used come back as notes for the judge
  verbatim is verbatim         a verbatim row's words (the quoted part, when the row has quotation marks) are in the
                               file or canon entry it cites, word for word; supplied copy and "said today" are exempt
  word numbers                 a number written as a word that counts people, money or time ("eleven clients") is
                               held to the same test as a digit
  names and frameworks         a name the source map never mentions, and a named framework ("the three-layer model",
                               "five pillars") not found in the person's files, come back as notes for the judge
  kinds                        every row's Kind is one of the five: verbatim, said again, writer, borrowed: verify, inferred
                               (a warning, not a fail); the count of verbatim rows is reported for the format's cap
  numbers sourced              every number in the post appears in a verbatim, said again or borrowed: verify row,
                               or in a cited entry's text; a number found only in a writer row fails
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import studio_checks as sc

ID_RE = re.compile(r"(?<![\w\"'`/.])([TVAPBXSROCGDWIQK])(\d*)\b(?![\w\"'`/])")   # an ID stands alone, not inside quotes, words or paths
ID_FILES = {
    "T": "canon/person/thesis.md", "V": "canon/person/values.md", "A": "canon/person/behaviors.md",
    "P": "canon/person/povs.md", "B": "canon/person/branches.md", "X": "canon/person/stop-list.md",
    "S": "canon/bank/stories.md", "R": "canon/bank/proof.md", "O": "canon/vehicle/vehicle.md",
    "C": "canon/vehicle/vehicle.md", "G": "canon/strategy/brand-strategy.md", "D": "canon/strategy/audience.md",
    "W": "canon/voice/voice-guide.md", "I": "bank/ideas.md", "Q": "bank/questions.md", "K": "bank/credibility.md",
}
SMALL = ("1", "2", "3")   # small counts are structure, not claims

def section(text, name):
    m = re.search(rf"^## {name}\s*\n(.*?)(?=^## |\Z)", text, flags=re.S | re.M)
    return m.group(1) if m else None

def find_root(path):
    d = os.path.dirname(os.path.abspath(path))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "studio.manifest.yaml")): return d
        d = os.path.dirname(d)
    return os.getcwd()

def canon_ids(root):
    ids = {}
    for letter, rel in ID_FILES.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p): continue
        txt = open(p, encoding="utf-8").read()
        # an entry is any line that starts a heading or a bullet with the ID: "## P1 ·", "### G1 ·", "- W2 ...", "- C1 ..."
        for m in re.finditer(rf"^(?:#{{2,3}}|-)\s*({letter}\d*)\b", txt, flags=re.M):
            ids[m.group(1)] = txt
    return ids

FEEDS_BANK = {"ready", "used"}   # idea and credibility bank entries feed a piece at these (rule 2)
BANK_LETTERS = {"I", "Q", "K"}

def entry_status(root):
    """The status line of every canon and bank entry, by ID: "## P3 · name" up to the next heading,
    its `status:` field, first word, lower case. An entry with no status line is left out."""
    out = {}
    for letter, rel in ID_FILES.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p): continue
        txt = open(p, encoding="utf-8").read()
        heads = list(re.finditer(rf"^#{{2,3}}\s*({letter}\d+)\b.*$", txt, flags=re.M))
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(txt)
            nxt = re.search(r"^#{1,3}\s", txt[m.end():end], flags=re.M)
            block = txt[m.end():m.end() + nxt.start()] if nxt else txt[m.end():end]
            st = re.search(r"^status:\s*([A-Za-z]+)", block, flags=re.M)
            if st: out[m.group(1)] = st.group(1).lower()
            if re.search(r"^heard:\s*recorder", block, flags=re.M | re.I):
                HEARD.add(m.group(1))
    return out

HEARD = set()   # entries whose number or name came only from a recorder transcript and isn't confirmed yet

WORD_NUMBERS = {"four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
    "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14", "fifteen": "15", "sixteen": "16",
    "seventeen": "17", "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30", "forty": "40",
    "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90", "hundred": "100",
    "thousand": "1000", "million": "1000000", "dozen": "12", "dozens": None, "hundreds": None, "thousands": None}
CLAIM_NOUNS = r"(?:clients?|customers?|people|students?|members?|subscribers?|followers?|readers?|employees?|staff|hires?|companies|founders?|users?|buyers?|calls?|deals?|projects?|years?|months?|weeks?|days?|hours?|minutes?|times|percent|dollars?|euros?|pounds?|k\b|grand|figures|books?|talks?|workshops?|cohorts?|countries|cities|offices)"
WORD_NUMBER_CLAIM = re.compile(r"\b(" + "|".join(WORD_NUMBERS) + r")\b(?:[ -](?:" + "|".join(WORD_NUMBERS) + r"))?(?:\s+\w+){0,2}?\s+" + CLAIM_NOUNS, re.I)

NAME_SKIP = {"I", "I'm", "I've", "I'd", "I'll", "LinkedIn", "Substack", "AI", "Claude", "ChatGPT", "Google", "YouTube",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "January", "February", "March",
    "April", "May", "June", "July", "August", "September", "October", "November", "December", "OK", "CEO", "CTO",
    "CFO", "COO", "VP", "PS", "P.S.", "TV", "US", "UK", "EU", "PDF", "Zoom", "Slack", "Notion", "Figma", "X", "Twitter",
    "Instagram", "TikTok", "Facebook", "Reddit", "Mr", "Mrs", "Ms", "Dr", "God", "English", "Spanish"}

def proper_names(post):
    """Capitalised words (and runs of them) that aren't at the start of a sentence or a line."""
    out = []
    body = re.sub(r"`[^`]*`|https?://\S+", " ", post)
    for m in re.finditer(r"(?<=[a-z0-9,;:)\]] )((?:[A-Z][\w'’&.-]*[a-z0-9]\w*|[A-Z]{2,})(?: (?:of |the |& |and )?(?:[A-Z][\w'’&.-]*[a-z0-9]\w*|[A-Z]{2,}))*)", body):
        run = []
        for w in m.group(1).replace("’", "'").split() + [None]:
            if w is not None:
                w = w.rstrip(".'")
            if w is None or w in NAME_SKIP or re.fullmatch(r"I'\w+", w):
                name = " ".join(run).strip()
                name = re.sub(r"^(?:of|the|and|&) |(?: (?:of|the|and|&))+$", "", name)
                if name and name not in NAME_SKIP: out.append(name)
                run = []
            else:
                run.append(w)
    return out

FRAMEWORK_NAME = re.compile(
    r"\b(?:the |my |our |a |his |her |their )?(?:[A-Z][\w-]+ ){1,3}(?:Method|Framework|Model|Rule|Law|Principle|Loop|Ladder|Matrix|System|Formula|Playbook|Pyramid|Flywheel|Paradox|Effect|Test|Trap|Gap|Curve)\b"
    r"|\b(?:the )?(?:two|three|four|five|six|seven|eight|nine|ten|\d)[- ](?:layer|step|stage|part|pillar|level|phase|tier|lens)s? (?:model|framework|method|system|approach|rule|test|ladder|process)\b"
    r"|\b(?:three|four|five|six|seven|eight|nine|ten|\d) (?:pillars|laws|stages|principles|commandments|rules of|layers|levels|phases|tiers|truths)\b",
)

def named_frameworks(post):
    return sorted({m.group(0).strip() for m in FRAMEWORK_NAME.finditer(post)})

ROLE_WORDS = ["founded", "founder", "led", "lead", "built", "created", "invented", "ran", "run", "grew", "scaled",
              "launched", "designed", "owned", "headed", "managed", "pioneered", "architected", "spearheaded"]
ROLE_STEMS = {"led": "le(?:d|ad)", "lead": "le(?:d|ad)", "ran": "r(?:a|u)n", "run": "r(?:a|u)n", "grew": "gr(?:e|o)w", "built": "buil",
              "founder": "found", "founded": "found"}
SCOPE_WORDS = ["clients", "customers", "companies", "teams", "every", "always", "dozens", "hundreds", "all of my", "every client",
               "my clients", "never", "everyone", "most of my"]

def cited_text_for(src, root, ids):
    """What a source-map cell cites, as text: the files it names, or the canon and bank entries it names."""
    texts = []
    for f in sc.FILE_REF.findall(src):
        fp = os.path.join(root, f)
        if os.path.exists(fp):
            texts.append(open(fp, encoding="utf-8", errors="replace").read())
    if not texts:
        col = re.sub(r"`[^`]*`|\"[^\"]*\"|“[^”]*”", "", src)
        for m in ID_RE.finditer(col):
            idv = m.group(1) + m.group(2)
            if idv in ids: texts.append(entry_block(ids[idv], idv))
    quoted = " ".join(a or b for a, b in sc.QUOTED.findall(src))
    return " ".join(texts) + " " + quoted

def entry_block(txt, idv):
    m = re.search(rf"^#{{2,3}}\s*{re.escape(idv)}\b.*?(?=^#{{1,3}}\s|\Z)", txt, flags=re.S | re.M)
    return m.group(0) if m else txt

def held_views(root):
    try:
        m = json.load(open(os.path.join(root, "bank", "map", "map.json"), encoding="utf-8"))
    except Exception:
        return []
    return [(n.get("text", ""), [v.get("quote") for v in n.get("versions") or [] if v.get("quote")])
            for n in m.get("nodes", []) if n.get("type") == "claim" and n.get("status") == "held before"]

def person_text(root):
    """Everything the person has written or confirmed, normalised, for checking a name is theirs."""
    parts = []
    for top in ("material", "canon", "bank", "inbox"):
        for base, dirs, fns in os.walk(os.path.join(root, top)):
            dirs[:] = [x for x in dirs if x != "swipe"]   # bank/swipe/: other people's posts, never the person's
            for fn in fns:
                if fn.endswith((".md", ".txt")) and fn != "swipe-file.md":
                    try: parts.append(open(os.path.join(base, fn), encoding="utf-8", errors="replace").read())
                    except OSError: pass
    return sc.norm_quote(" ".join(parts))

def cells_of(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]

def table(smap):
    """The source map's header cells and its data rows (each a list of cells)."""
    lines = [r for r in smap.split("\n") if r.strip().startswith("|")]
    header, rows = None, []
    for r in lines:
        cells = cells_of(r)
        if all(re.fullmatch(r":?-{2,}:?", c) or not c for c in cells):
            continue                                  # the |---| line
        if header is None and any(re.search(r"\b(kind|source)\b", c, re.I) for c in cells):
            header = cells; continue
        if not any(cells):
            continue                                  # an empty template row
        rows.append(cells)
    return header or [], rows

def col_index(header, rx, fallback):
    for i, c in enumerate(header):
        if re.search(rx, c, re.I): return i
    return fallback

def main():
    sc.per_draft(__file__)
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    path = sys.argv[1]; root = find_root(path)
    text = open(path, encoding="utf-8").read()
    post = sc.post_section(text)   # one of Posts A, B, C when the file holds three
    smap = section(text, "Source map")
    fails, notes = [], []

    if post is None:
        fails.append("no ## Post section"); post = text
    hfails, hflags = sc.house_check(post, allow=sc.exceptions(root))
    for rule, matched, line in hfails:
        fails.append(f"{rule}: \"{matched}\" (post line {line})")
    for rule, matched, line in hflags:
        notes.append(f"flag {rule}: \"{matched}\" (post line {line}); the judge decides")

    header, rows = [], []
    if smap is None:
        fails.append("no ## Source map section")
    else:
        header, rows = table(smap)
        if not rows: fails.append("source map has no rows")
    # Find the columns by their header text; without a header row, fall back to the template's order
    # (Line or claim | Kind | Source ID or file | Note). A header with no Kind column has no kinds.
    kind_i = col_index(header, r"^kind\b", None if header else 1)
    src_i = col_index(header, r"source id or file|^source", 2)
    line_i = col_index(header, r"^line|claim", 0)
    note_i = col_index(header, r"^note", 3)
    verbatim_rows = []
    fact_rows = []

    ids = canon_ids(root)
    status = entry_status(root)
    cited = set()
    kinds, verbatim, unknown = [], 0, []
    sourced_text, writer_text = [], []
    for cells in rows:
        kind = sc.norm_kind(cells[kind_i]) if kind_i is not None and len(cells) > kind_i else ""
        src = cells[src_i] if len(cells) > src_i else ""
        kinds.append(kind)
        if kind in ("said again", "verbatim"):
            fact_rows.append((cells[line_i] if line_i is not None and len(cells) > line_i else "", src, kind))
        if kind == "verbatim":
            verbatim += 1
            note = cells[note_i] if note_i is not None and len(cells) > note_i else ""
            if "supplied" not in note.lower() and "said today" not in src.lower():
                verbatim_rows.append((cells[line_i] if line_i is not None and len(cells) > line_i else "", src))
        if kind and kind not in sc.KINDS and kind not in unknown: unknown.append(kind)
        row_text = " | ".join(cells)
        if kind in sc.NUMBER_KINDS: sourced_text.append(row_text)
        elif kind == "writer": writer_text.append(row_text)
        if "/" in src or ".md" in src:
            continue                                  # a cell naming a file contributes no IDs
        col = re.sub(r"`[^`]*`|\"[^\"]*\"|“[^”]*”", "", src)   # quoted text and code spans aren't IDs
        for m in ID_RE.finditer(col):
            idv = m.group(1) + m.group(2)
            if idv == "T" or m.group(2):
                cited.add(idv)
                if idv not in ids and not (m.group(1) == "T" and "T" in ids):
                    msg = f"ID {idv} in the source map is not in the canon or the idea bank"
                    if msg not in fails: fails.append(msg)
    # Rule 2: a retired entry feeds nothing, a canon draft feeds a piece only on the person's yes in the
    # session, and an idea or credibility entry feeds at ready or used. A retired ID fails; the rest are notes.
    for idv in sorted(cited):
        st = status.get(idv, "")
        if st == "retired":
            fails.append(f"ID {idv} is retired: a retired entry feeds nothing (rule 2). Cut the line or cite what replaced it")
        elif st == "draft" and idv[0] not in BANK_LETTERS:
            notes.append(f"ID {idv} is a draft: it feeds this piece only if the person confirmed it in the session (rule 2)")
        if idv in HEARD:
            fails.append(f"ID {idv} holds a number or name a recorder heard and the person hasn't confirmed (heard: recorder): ask them, then delete that line")
        elif idv[0] in {"I", "K"} and st and st not in FEEDS_BANK:
            notes.append(f"ID {idv} is `{st}`: bank entries feed a piece at ready or used (rule 2), or on the person's yes in the session")
    # Rule 3: a verbatim row is the person's words kept as written, so its words must be in the file or
    # entry it cites. Supplied copy and "said today" are exempt (nothing on disk to check against).
    for line, src in verbatim_rows:
        files = [f for f in sc.FILE_REF.findall(src)]
        texts, gone = [], []
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp): texts.append(sc.norm_quote(open(fp, encoding="utf-8", errors="replace").read()))
            else: gone.append(f)
        if not files:
            col = re.sub(r"`[^`]*`|\"[^\"]*\"|“[^”]*”", "", src)
            for m in ID_RE.finditer(col):
                idv = m.group(1) + m.group(2)
                if idv in ids: texts.append(sc.norm_quote(ids[idv]))
        shown = line.strip()[:70] + ("..." if len(line.strip()) > 70 else "")
        if gone and not texts:
            fails.append(f"verbatim row cites {', '.join(gone)}, which isn't in the studio: \"{shown}\"")
        elif texts and not sc.quote_found(line, texts):
            fails.append(f"verbatim row isn't word for word in what it cites ({src.strip()[:50]}): \"{shown}\". Quote it exactly, or mark it said again")
    for k in unknown:
        extra = " (\"seen\" is no longer a kind: a confirmed seen connection is cited as said again with its proposal, an unconfirmed one is inferred)" if k == "seen" else ""
        notes.append(f"warning: kind \"{k}\" isn't one of the five (" + ", ".join(sc.KINDS) + ")" + extra)
    if rows and not any(kinds):
        notes.append("warning: no Kind column found in the source map; numbers can't be checked against row kinds")
    if rows: notes.append(f"verbatim rows: {verbatim}; the format's cap applies")
    if rows and not cited and "writer" not in kinds: notes.append("no IDs found in the source map; every fact about the person needs one")
    if rows and "writer" not in kinds: notes.append("no `writer` rows in the source map: a draft that only restates the person's entries isn't finished")

    num_rx = lambda n: re.compile(rf"(?<![\d.,]){re.escape(n)}(?![\d]|[.,]\d)")
    cited_text = " ".join(ids.get(i, "") for i in cited)
    sourced = " ".join(sourced_text) + " " + cited_text
    writer_only = " ".join(writer_text)
    for num in sorted(set(re.findall(r"\b\d+(?:[.,]\d+)?\b", post))):
        if num in SMALL: continue
        rx = num_rx(num)
        if rx.search(sourced): continue
        if rx.search(writer_only):
            fails.append(f"number {num} in the post appears only in a writer row; a number needs a verbatim, said again or borrowed: verify row, or a cited entry")
        else:
            fails.append(f"number {num} in the post has no verbatim, said again or borrowed: verify row and isn't in a cited entry")

    # Numbers written as words get the same test when they count people, money or time ("we lost eleven
    # clients"): a digit-only check let them through. Other word numbers ("five trade-offs") are structure.
    word_hits = set()
    for m in WORD_NUMBER_CLAIM.finditer(post):
        w = m.group(1).lower(); digit = WORD_NUMBERS.get(w)
        if w in word_hits: continue
        word_hits.add(w)
        found = re.search(rf"\b{w}\b", sourced, re.I) or (digit and num_rx(digit).search(sourced))
        if found: continue
        fails.append(f"\"{m.group(0)}\" in the post: a number written as a word needs a verbatim, said again or borrowed: verify row, or a cited entry, the same as a digit")

    # Names (a company, a study, a person) the sources never mention: a note for the judge, since a name
    # can come from a borrowed case the writer forgot to log, or from nowhere (rule 1).
    smap_text = " ".join(" | ".join(c) for c in rows) + " " + cited_text
    smap_low = smap_text.lower()
    for name in sorted(set(proper_names(post))):
        if name.lower() not in smap_low:
            notes.append(f"name \"{name}\" in the post isn't in any source map row or cited entry: log it as borrowed: verify, cite where it comes from, or cut it (rule 1)")

    # A framework given a name the person never gave it is invented material (role-editor, Invented material):
    # "the three-layer model", "five pillars". Looked for in everything they've written and confirmed.
    # A view the person told the studio they no longer hold (a `held before` claim on the map) can't come back
    # as theirs: a post line that says it again in their words fails.
    for text, quotes in held_views(root):
        for q in quotes:
            if len(sc.norm_quote(q)) > 20 and sc.quote_found('"' + q + '"', [sc.norm_quote(post)]):
                fails.append(f"the post says \"{q[:60]}\", a view the person no longer holds (the map marks \"{text[:50]}\" held before). Cut it, or say it as what they used to think")
                break

    # A fact said again can grow without a number changing: "helped" becomes "led", "a client" becomes "my
    # clients", "co-founded" becomes "founded". Notes for the judge when a role word or a plural in the row
    # isn't in what it cites.
    for line, src, kind in fact_rows:
        cited = cited_text_for(src, root, ids)
        if not cited: continue
        low_line, low_cited = line.lower(), cited.lower()
        if re.search(r"\bfound(?:ed|er|ing)\b", low_line) and not re.search(r"\bco-?found", low_line) and re.search(r"\bco-?found", low_cited):
            notes.append(f"\"{line.strip()[:60]}\": the source says co-founded, the line drops the co- (an inflated fact; keep what the source says)")
            continue
        for w in ROLE_WORDS:
            if re.search(rf"\b{w}\b", low_line) and not re.search(rf"\b{ROLE_STEMS.get(w, w)}", low_cited):
                notes.append(f"\"{line.strip()[:60]}\": \"{w}\" isn't in what it cites ({src.strip()[:40]}); check the role wasn't made bigger")
                break
        for w in SCOPE_WORDS:
            if re.search(rf"\b{w}\b", low_line) and not re.search(rf"\b{w}\b", low_cited):
                notes.append(f"\"{line.strip()[:60]}\": \"{w}\" isn't in what it cites ({src.strip()[:40]}); check one case wasn't made into many")
                break

    named = named_frameworks(post)
    if named:
        theirs = person_text(root) + " " + sc.norm_quote(smap_text)
        for nm in named:
            if sc.norm_quote(nm) not in theirs:
                notes.append(f"named framework \"{nm}\" isn't in the person's files: if they never named it, the line is `inferred` and goes to proposals.md before the piece ships (rule 1)")

    out = {"fails": fails, "notes": notes, "ids_cited": sorted(cited), "verbatim_rows": verbatim, "root": root}
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2))
    else:
        print(f"check-mechanical: {path}")
        print("  " + ("PASS" if not fails else f"FAIL ({len(fails)})"))
        for f in fails: print("  - " + f)
        for n in notes: print("  note: " + n)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
