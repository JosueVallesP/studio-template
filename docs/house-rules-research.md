# What the house rules rest on

The research behind `skills/craft-house-rules`, read on 23 Oct 2026. Paper-level findings unless marked.

## Examples beat descriptions; the person's own text beats examples
- "How Well Do LLMs Imitate Human Writing Style?" (arXiv 2509.24930, 2025). Authorship verification rates by prompt: a statistical style profile 3 to 7%; one author paragraph 68 to 95%; two paragraphs 91 to 100%; completing the author's own half-written text 97 to 100%. Prompting strategy mattered more than model size.
- "Catch Me If You Can? Not Yet" (arXiv 2509.14543, 2025; six models, about 400 authors). Five examples beat zero-shot on nearly every metric; gains plateaued from two to ten; the single strongest lever was an opening snippet of the author's own text. Informal personal voice (blogs, Reddit) was the hard case.
- Chakrabarty and Dhillon (CHI 2026, arXiv 2601.18353). With 20 excerpts plus a description, judges still preferred the human 83% of the time; only fine-tuning flipped it. Prompting alone does not reach expert fidelity, so the person's final edit is part of the method.

## Models remove the person's markers more than they add polish
- "Voice Under Revision" (arXiv 2604.22142, 2026; 2,700 rewrites across three frontier models). Every rewrite moved the same markers the same way: contractions down 31%, first person down 9%, commas up 67%, word length up 8.5%, dashes up. A "preserve the voice" instruction cut the effect by about a third and did not reverse it.
- "How LLMs Distort Our Written Language" (arXiv 2603.18161). Even "minimal edit" instructions produced large lexical shifts and sometimes changed an essay's conclusion.
- "Base Models Look Human To AI Detectors" (arXiv 2605.19516). The detectable signature is largely a post-training artifact; continuing a human prefix read as human 97 to 99% of the time.
- Studio response: `scripts/voice-diff.py` measures contractions, first person, causal connectives, commas, word length and sentence spread against the person's corpus, and the share of their sentences that survived.

## Negative instructions prime what they forbid
- "Semantic Gravity Wells" (arXiv 2601.08070) and "Don't Think of the White Bear" (arXiv 2511.12381). "Do not use X" failed 9% of the time when X was unlikely and 46% when X was the natural completion; most failures were priming. Small open models; frontier models obey simple bans better in practice.
- Studio response: bans live in the scripts, which don't get primed; skills state the replacement behavior with the person's example.

## Mode collapse, and the prompt-level counter
- Padmakumar and He (ICLR 2024); "Artificial Hivemind" (NeurIPS 2025). Feedback tuning lowers output diversity; models repeat themselves and each other.
- Verbalized Sampling (arXiv 2510.01171). Asking for several candidates in one call raised diversity 1.6 to 2.1x and human ratings about 26%, with no logit access, on Claude and GPT.
- Studio response: three distinct drafts of the whole piece, judge picks.

## Self-critique
- Self-Refine (arXiv 2303.17651) helps on style tasks by LLM-judged metrics; "LLMs Cannot Self-Correct Reasoning Yet" (ICLR 2024) shows same-context loops without an outside signal can hurt. LAMP (arXiv 2409.14509): models asked to find AI idiosyncrasies in a paragraph reached span precision 0.38 to 0.46.
- Studio response: the judge is a separate pass with a fixed checklist and the person's examples, accepts or rejects, and picks among candidates rather than looping one draft.

## The word list
- Kobak et al. (Science Advances 2024, 15M PubMed abstracts): "delve" about 25x its trend, "showcasing" and "underscores" about 9x.
- Juzek and Ward (COLING 2025): 21 focal words confirmed, including delve, showcasing, boasts, underscore, comprehending, intricacies, surpassing, garnered, emphasizing, realm, groundbreaking, advancements, aligns.
- Liang et al. (2024): realm, intricate, showcasing, pivotal.
- Human experts (arXiv 2501.15654): five frequent ChatGPT users misclassified 1 of 300 articles; vocabulary was the top cue, then sentence structure.
- Structural tells (Wikipedia's WikiProject AI Cleanup, via TechCrunch and The Decoder, 2025): significance inflation, trailing -ing clauses, negative parallelism, the rule of three, false ranges, editorializing, transition overuse, compulsive summaries, chatbot residue. The editors' own caveat: look for combinations; humans use all of these.

## Sentence rhythm
- Tarım and Onan (2025): coefficient of variation of sentence length about 0.25 for LLM text, 0.33 for humans. Harris et al.: human sentences ranged 7.5 to 47.6 words; AI paragraphs sat uniformly at two to four sentences. A real but weak signal on its own; `voice-diff.py` compares against the person's own spread, not a fixed number.

## Practitioner guides read on 23 Oct 2026 (Every)
- "AI Style Guides" (Katie Parrott): a voice guide needs voice, structure, sentence-level preferences, signature moves, anti-patterns with before-and-after pairs, examples both ways, and a revision checklist built from the model's real repeated mistakes; build it by having the model interview the person and show them lines to react to, not by self-description. All of this is in the studio's voice guide template and the calibration loop. One line in it shows why the universal and personal layers must stay split: its blacklist deletes hedges ("actually", "just"), which for some writers carry their stance.
- "Compound Writing" (Parrott): the same loop as the studio (interview, outline, draft, review, finalize, save the lesson). Its "tracks" check (scaffolding and process narration left in a draft) is house rule H26; its named reviewer lenses map onto the judge, copylosophy and `/think`'s perspective moves.
- "Build Faster With Voice" (Naidu and Entis): spoken capture is the easiest way to get a person's own words, which the research above shows is the strongest lever. Capture and Journal should take voice transcripts as the preferred input and clean them the way rule 3 says: fillers out, meaning and sequence kept, claims never sharpened without asking.
