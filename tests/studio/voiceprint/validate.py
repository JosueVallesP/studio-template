#!/usr/bin/env python3
"""Check that voiceprint tells writers apart on texts it hasn't seen.

Uses either a folder of essays (the studio's own library,
skills/fmt-substack-essay/library/essays/, where each file names its author in
its frontmatter and the text sits under "## Essay"), or any CSV with a text
column and an author column. For each writer A and each other writer B:
  - A's profile is built from A's essays minus a held-out set
  - the comparison set is every other writer except B
  - A's held-out pieces should read as A; B's pieces (a writer the system has
    never seen, like a model's draft) should not

Reports how often the method separates the two, plus nearest-writer
attribution accuracy, at a given piece length.

  python3 tests/studio/voiceprint/validate.py --length 300            (the repo's essay library)
  python3 tests/studio/voiceprint/validate.py <folder or essays.csv> --author-col Author --length 300
"""

import argparse
import os
import random
import re
import statistics
import sys

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path.insert(0, os.path.join(REPO, "scripts"))
import voiceprint as vp  # noqa: E402

LIBRARY = os.path.join(REPO, "skills", "fmt-substack-essay", "library", "essays")


def load_library(folder):
    """The essay files in a folder: the author from each file's frontmatter (author:), the text from
    under "## Essay" to the end. A file with no author or no essay section is skipped."""
    docs = []
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name.lower() == "readme.md":
            continue
        raw = vp.read_file(os.path.join(folder, name))
        au = re.search(r'^author:\s*"?(.*?)"?\s*$', raw, re.M)
        body = re.search(r"^## Essay\s*\n(.*)\Z", raw, re.S | re.M)
        if not au or not body:
            continue
        t = vp.clean_text(body.group(1))
        if t:
            docs.append({"id": name, "label": au.group(1).strip(), "text": t})
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", default=LIBRARY,
                    help="a folder of essay files with author: frontmatter (default: the repo's essay library), or a CSV")
    ap.add_argument("--author-col", default="Author")
    ap.add_argument("--text-col", default=None)
    ap.add_argument("--length", type=int, default=300, help="piece length in words")
    ap.add_argument("--holdout", type=int, default=3, help="essays held out per writer")
    ap.add_argument("--max-test", type=int, default=12, help="test pieces per side per run")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 when a rate falls below its floor (--min-own, --min-off, --min-attr); test-all.sh uses this")
    ap.add_argument("--min-own", type=float, default=80, help="floor for own held-out pieces read as theirs, in percent")
    ap.add_argument("--min-off", type=float, default=65, help="floor for unseen writers' pieces read as off, in percent")
    ap.add_argument("--min-attr", type=float, default=70, help="floor for nearest-writer attribution, in percent")
    a = ap.parse_args()

    if os.path.isdir(a.source):
        docs = load_library(a.source)
    else:
        docs = vp.load_texts(a.source, a.text_col, a.author_col)
    by = {}
    for d in docs:
        by.setdefault(d["label"], []).append(d)
    authors = sorted(k for k, v in by.items() if len(v) > a.holdout + 2)
    rng = random.Random(a.seed)
    print(f"{len(docs)} texts, {len(authors)} writers: {', '.join(authors)}; pieces of ~{a.length} words\n")

    # split each writer into train and held-out essays
    train, test = {}, {}
    for au in authors:
        ds = by[au][:]
        rng.shuffle(ds)
        test[au], train[au] = ds[:a.holdout], ds[a.holdout:]

    seps, own_ok, oth_ok, n_own, n_oth = [], 0, 0, 0, 0
    print("| Writer | Unseen writer | Own pieces read as theirs | Unseen pieces read as 'off' | Calibration separation |")
    print("| --- | --- | --- | --- | --- |")
    for au in authors:
        for bu in authors:
            if bu == au:
                continue
            others = [d for x in authors if x not in (au, bu) for d in train[x]]
            an = vp.Analysis(train[au], others, a.length)
            seps.append(an.separation())
            own_pieces = vp.chunk_corpus(test[au], a.length)
            oth_pieces = vp.chunk_corpus(by[bu], a.length)
            rng.shuffle(own_pieces)
            rng.shuffle(oth_pieces)
            o_ok = t_ok = 0
            for p in own_pieces[:a.max_test]:
                o_ok += an.reading(p["text"])["verdict"] in ("reads like you", "close")
            for p in oth_pieces[:a.max_test]:
                t_ok += an.reading(p["text"])["verdict"] == "off"
            no, nt = min(len(own_pieces), a.max_test), min(len(oth_pieces), a.max_test)
            own_ok += o_ok
            oth_ok += t_ok
            n_own += no
            n_oth += nt
            print(f"| {au} | {bu} | {o_ok}/{no} | {t_ok}/{nt} | {seps[-1]:.2f} |")
    print(f"\nOwn held-out pieces read as theirs: {own_ok}/{n_own} ({100 * own_ok / n_own:.0f}%)")
    print(f"Unseen writers' pieces read as 'off': {oth_ok}/{n_oth} ({100 * oth_ok / n_oth:.0f}%)")
    print(f"Median calibration separation: {statistics.median(seps):.2f}")

    # nearest-writer attribution on held-out pieces (Cosine Delta to each centroid)
    pieces_all = [d for au in authors for d in train[au]]
    chunks = vp.chunk_corpus(pieces_all, a.length)
    words = [vp.words_of(c["text"]) for c in chunks]
    mfw = vp.choose_mfw(words, 300, 0.2)
    space = vp.ZSpace(mfw, [vp.rel_freqs(w) for w in words])
    cents = {}
    for au in authors:
        zs = [space.z(vp.rel_freqs(vp.words_of(c["text"]))) for c in chunks if c["label"] == au]
        cents[au] = vp.centroid(zs)
    right = total = 0
    for au in authors:
        for p in vp.chunk_corpus(test[au], a.length)[:a.max_test]:
            z = space.z(vp.rel_freqs(vp.words_of(p["text"])))
            guess = min(cents, key=lambda x: vp.cosine_delta(z, cents[x]))
            right += guess == au
            total += 1
    print(f"Nearest-writer attribution on held-out pieces: {right}/{total} ({100 * right / total:.0f}%), "
          f"chance is {100 / len(authors):.0f}%")
    if a.check:
        rates = [("own read as theirs", 100 * own_ok / n_own, a.min_own), ("unseen read as off", 100 * oth_ok / n_oth, a.min_off),
                 ("attribution", 100 * right / total, a.min_attr)]
        low = [f"{n} {r:.0f}% < {m:.0f}%" for n, r, m in rates if r < m]
        print("voiceprint validate: " + ("FAIL (" + "; ".join(low) + ")" if low else "pass"))
        sys.exit(1 if low else 0)


if __name__ == "__main__":
    main()
