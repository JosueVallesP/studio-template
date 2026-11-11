# Methods

What each measure in voiceprint comes from, what it's good for, where it breaks, and how this version was tested. Read this before changing the script.

## The idea underneath

Every method here rests on one finding: people use small, common words at rates that stay steady across their writing and differ from person to person. Mosteller and Wallace used it in 1964 to settle which of the disputed Federalist Papers Madison wrote and which Hamilton wrote, largely on how often each used words like "upon" and "while". Nobody picks those words on purpose, which is why they're hard to fake and why they still carry the signal sixty years later.

Studies of AI text add a second finding: machine writing is uniform where human writing varies. A 2026 study in *Digital Scholarship in the Humanities* (Chen, Xiong, He and Ross) compared paired human and AI essays across 110 subjects and found AI texts strikingly alike in style while human writing varied from person to person. That uniformity shapes one of the design choices below.

## The measures

### Burrows's Delta and Cosine Delta (word habits)

**Source.** John Burrows introduced Delta in 2002: take the most frequent words in a corpus, turn each text's rate for each word into a z-score (how far above or below the corpus average it sits), and measure the distance between a text and an author by the average gap in those scores. It became the most widely used method in authorship attribution.

**What improved it.** Hoover (2004) showed that using more frequent words, culling words that are frequent only because one text uses them a lot, and sometimes dropping pronouns all help. Smith and Aldridge (2011) proposed Cosine Delta, which compares the shape of the z-score profile instead of its size. Jannidis and colleagues (2015) tested Delta variants across English, French and German novels and found Cosine Delta the most reliable, holding steady as the word list grows where the others start to slip. Evert and colleagues (2017) explained why: the author signal sits in the pattern of over- and under-use across many words, not in how extreme any single word is, and normalizing the profile (what the cosine does) is the step that matters.

**In voiceprint.** The person's pieces and the comparison pieces are cut to the draft's length, the 300 most frequent words are taken from both sets (culled to words that appear in at least 20% of pieces), and the z-scores are computed across both sets. The person's profile is the average of their pieces. The main distance is Cosine Delta; Burrows's original Delta is reported alongside.

**Where it breaks.** Genre and format move it: Delta is known to be sensitive to genre differences and to change over an author's career. That's why the comparison set has to be in the person's formats, and why the profile needs rebuilding as they change.

### Style measures

**Source.** Sentence length, its spread, punctuation rates, vocabulary range and word length are the oldest stylometric measures (Eder and Rybicki describe the field as reaching back to the mid-1800s). Studies of AI text lean on them: StyloAI (Opara, 2024) separated AI from human writing with 31 such features, and a 2025 study, *Stylometry recognizes human and LLM-generated texts in short samples*, found AI text more grammatically standardized and heavy on a set of overused words.

**In voiceprint.** 29 measures (listed in `reading-a-report.md`), each compared with the person's own range. The style distance is the average gap between a draft and the person's medians, each gap scaled by how much that measure varies across all pieces, so a measure that swings a lot counts for less. Vocabulary range uses the moving-average type-token ratio over 50-word windows, which doesn't shrink as a text gets longer the way a plain type-token ratio does.

**Where it breaks.** These measures are easy to imitate one at a time, and some move with format more than with the writer (line breaks, list use). They're good at showing what to change and weak as proof on their own.

### General Impostors (verification)

**Source.** Koppel and Winter (2014) turned "did this person write this?" into a contest: compare the text with the person's writing and with a set of impostors (other writers), many times over, each time on a random half of the features and a random half of the impostors. If the text sits closer to the person in most rounds, it's likely theirs. A version of it (Seidman's General Impostors method) placed first in the PAN 2013 authorship verification competition, and Kestemont and colleagues (2016) built the implementation that the R package stylo uses. Later work (Potha and Stamatatos) refined how impostors are ranked.

**In voiceprint.** 100 rounds, half the words and half the comparison pieces each round, Cosine Delta as the distance. The report shows how the person's own pieces and the comparison pieces score on the same test, so the draft's number has something to be read against.

**Where it breaks.** It runs on word habits only, so a draft on the person's topics can score well while missing their style. In testing, an AI paragraph on personal branding scored 95% against a writer who covers the same ground. The report says so when the impostor test and the verdict disagree. It also depends on the impostors: too few or too unlike the draft and it says yes too easily. Reading the studio's side of every pair in `bank/rewrites/` into the comparison set fixes the second problem over time.

### Craig's Zeta (marker words)

**Source.** Burrows (2007) proposed Zeta to find words one author uses consistently and another avoids, looking past the most common words to the middle of the frequency range. Hugh Craig's version (Craig and Kinney, 2009) is the one most used: cut each set into segments, and for each word subtract the share of the other set's segments that use it from the share of the author's segments that use it.

**In voiceprint.** Segments of 150 words. A score near 1 means the person uses the word in nearly every piece and others almost never do. Marker words are split into small words (the reliable part of the fingerprint) and other words.

**Where it breaks.** Zeta picks up topics. Craig's own attribution of parts of *Henry VI* to Marlowe drew on marker words about warfare, and critics pointed out that those words reflected the battle-heavy plays in Marlowe's small canon more than his style. Expect the person's subject matter in the non-function marker list and let them strike what isn't a habit.

## How much text it needs

Maciej Eder's tests on sample size (2010, 2015, 2017) are the reference. His early work found results fell apart below about 3,000 words per sample; later work showed 2,000 words is enough in many cases, and that some authors need far more because their fingerprint is faint. Two consequences for voiceprint:

1. A single LinkedIn post (100 to 300 words) is short for this kind of measurement. The tool compensates by comparing the draft with pieces of the same length, so the uncertainty shows up in the calibration instead of hiding, but short drafts get weaker readings.
2. The person's sample sets the ceiling. Below 3,000 words of their writing, the tool gives no overall verdict, only single-measure flags. Around 5,000 words the ranges settle.

## Design choices

**Fit takes the lower of the two measures.** The first version averaged the word measure and the style measure. Testing showed the problem: an AI paragraph on the person's topic sat closer to the person's average word habits than 92% of the person's own pieces (uniform text lands near the middle) while its style was further out than all of them, and the average called it "close". A draft now has to pass both. On human writers this changed nothing measurable (the ranking accuracy stayed the same at every length) and it closed the gap AI text slipped through.

**Calibration against the person's own pieces.** Raw Delta values mean nothing on their own; they shift with length, format and corpus. Every reading is placed against the same measure for each of the person's pieces, scored with that piece left out, and against the comparison pieces. "Fit 40%" means the draft is at least as close as 40% of the person's own pieces.

**A verdict only when the tool can tell.** Before giving a verdict the tool checks how often, at the draft's length, it can tell the person's pieces from the comparison pieces (0.5 is a coin flip). Below 0.7, or below 3,000 words of the person's writing, it withholds the verdict. In a test on a set of short rewrites (under a thousand words in all) with the studio's drafts as the comparison set, that figure fell between 0.03 and 0.2: the studio drafts sat closer to the writer's average than the writer's own pieces did, the uniformity problem again. Without the gate the tool would have called every draft "reads like you".

**House rules against the person's own rate.** A fixed list of banned patterns can't tell a person's habit from a machine's. A person who writes "it's not about X, it's about Y" in half their essays gets every such line failed, and the studio's own rules flatten their voice. So the profile counts each house-rule pattern in the person's pieces, and a rule they break often enough can become an exception on their yes. The exception turns fails into flags and never silences the rule, and "Above your own rate" flags a draft that uses the pattern more often than most of their pieces do. The idea of flagging a pattern only above a writer's own baseline density comes from setec-voiceprint's pattern audit and its restoration method (anotherpanacea-eng, on GitHub); the studio's version is written from the method, with the studio's own pattern lists.

**Thresholds.** "Reads like you" from a fit of 25%, "close" from 10%. Chosen on held-out tests (below) to keep most of a person's own pieces out of "off" while catching most strangers.

## Testing

`tests/studio/voiceprint/validate.py` runs the check on any CSV with a text column and an author column. The current figures, from the essays shipped in `skills/fmt-substack-essay/library/essays/`, are in `tests/studio/voiceprint/README.md`, and the check runs in `scripts/test-all.sh`; the table below is the first run, on the full set of the studio's Substack library (57 essays, six writers who all write about creators, business and self-improvement, which makes them hard to tell apart), each writer's profile was built from all but three essays, the comparison set was every other writer but one, and the held-out writer stood in for an unknown author, the way a model's draft would.

| Piece length | Own held-out pieces at least "close" | Unseen writer marked "off" | Ranking separation | Nearest-writer attribution (6 writers, chance 17%) |
| --- | --- | --- | --- | --- |
| 150 words | 88% | 46% | 0.80 | 55% |
| 300 words | 91% | 62% | 0.87 | 61% |
| 600 words | 91% | 65% | 0.87 | 65% |
| 1,000 words | 91% | 73% | 0.85 | 66% |

How to read it: the tool rarely calls a person's own writing "off", and it gets better at catching strangers as pieces get longer. At post length it catches about half to two-thirds of a stranger's pieces on a single reading. The ranking separation (the chance that a random piece of the person's fits better than a random stranger's) is the better summary of what the measure can do, and it sits between 0.80 and 0.87. These writers share a niche; writers further apart, and AI text with its uniform style, separate more easily.

A second test used a writer from the same library as "the person" (8 essays, 57,000 words) and scored two drafts: a 510-word excerpt from one of their essays the tool hadn't seen, and a 220-word AI-style paragraph on personal branding. The excerpt read as theirs (fit 53%). The paragraph scored a fit of 0% with eight flags, among them no contractions, long words, -ly adverbs and nine AI-typical words.

Rerun the tests after any change to the script and update this table.

## Sources

- Burrows, J. (2002). "Delta": a measure of stylistic difference and a guide to likely authorship. *Literary and Linguistic Computing* 17(3).
- Burrows, J. (2007). All the way through: testing for authorship in different frequency strata. *Literary and Linguistic Computing* 22(1).
- Chen, R., Xiong, S., He, J., Ross, G. J. (2026). Stylometric detection of AI-generated texts: evidence from human and machine-written essays. *Digital Scholarship in the Humanities*. https://doi.org/10.1093/llc/fqag064
- Craig, H., Kinney, A. (eds.) (2009). *Shakespeare, Computers, and the Mystery of Authorship.* Cambridge University Press.
- Eder, M. (2010). Does size matter? Authorship attribution, small samples, big problem. Digital Humanities 2010.
- Eder, M. (2017). Short samples in authorship attribution: a new approach. Digital Humanities 2017.
- Evert, S., Proisl, T., Jannidis, F., Reger, I., Pielström, S., Schöch, C., Vitt, T. (2017). Understanding and explaining Delta measures for authorship attribution. *Digital Scholarship in the Humanities* 32(suppl. 2). https://doi.org/10.1093/llc/fqx023
- Hoover, D. (2004). Testing Burrows's Delta. *Literary and Linguistic Computing* 19(4).
- Jannidis, F., Pielström, S., Schöch, C., Vitt, T. (2015). Improving Burrows' Delta: an empirical evaluation of text distance measures. Digital Humanities 2015.
- Kestemont, M., Stover, J., Koppel, M., Karsdorp, F., Daelemans, W. (2016). Authenticating the writings of Julius Caesar. https://doi.org/10.1016/j.eswa.2016.06.029
- Koppel, M., Winter, Y. (2014). Determining if two documents are written by the same author. *Journal of the Association for Information Science and Technology* 65(1).
- Mosteller, F., Wallace, D. (1964). *Inference and Disputed Authorship: The Federalist.* Addison-Wesley.
- Opara, C. (2024). StyloAI: distinguishing AI-generated content with stylometric analysis. arXiv:2405.10129.
- setec-voiceprint, `aic_pattern_audit.py` and the craft-restoration skill: flag a named pattern only above the writer's own baseline density. github.com/anotherpanacea-eng/setec-voiceprint. Method only; no code taken.
- Seidman, S. (2013). Authorship verification using the Impostors Method. PAN at CLEF 2013.
- Smith, P., Aldridge, W. (2011). Improving authorship attribution: optimizing Burrows' Delta method. *Journal of Quantitative Linguistics* 18(1).
- *Stylometry recognizes human and LLM-generated texts in short samples* (2025). arXiv:2507.00838.
