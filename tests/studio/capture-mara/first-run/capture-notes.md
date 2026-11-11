# Capture notes for the skill's author

Run of `skills/role-capture` on 2026-10-22, Mara Lindqvist test case. Two inbox files, eight entries written, one extended.

## Files read
17 files before writing: CLAUDE.md, the SKILL.md, the ideas template, both inbox files, `canon/bank/ideas.md`, `stories.md`, `proof.md`, `core-summary.md`, `povs.md`, `branches.md`, `values.md`, `stop-list.md`, `thesis.md`, `voice-guide.md`, `vehicle/vehicle.md`, `strategy/content-plan.md`. Plus `templates/proposals.md`, `templates/inbox/README.md`, `studio-notes.md`, `pieces/shortlist.md` (to find the "one thing the strategist can use first") and a grep through `scripts/status.sh` and `skills/check-status/SKILL.md` to see how proposals get counted. About 22 in all. The skill names five canon inputs; a real capture needs the person layer itself, since the index does not exist.

## Missing files the skill points at
- `canon/canon-index.md` does not exist (the strategist's notes said the same). Step 4 says to link "by ID, from the index". I read `povs.md`, `branches.md`, `values.md`, `stop-list.md`, `thesis.md` directly instead. Either build the index in setup or tell capture to read the person files.
- `proposals.md` did not exist. The skill says where the template is but not "create it from the template if missing" (role-strategist says that). I created it.
- `canon/bank/questions.md` does not exist. No reader questions this run, so nothing lost, but the skill should say to create it from a template, and there is no questions template under `skills/setup-brand-tree/templates/bank/`.
- `inbox/` existed without the README the skill says to create on first use. I copied `templates/inbox/README.md` in. The skill does not name that template.

## Contradictions
1. **Step 8 versus the proposals template.** Step 8 says write "one line" of `seen_in` evidence and "you don't propose the change; the librarian does." The template demands a full block per proposal: `proposal:`, `evidence:`, `question_for_the_person:`, `status: open`, and `/status` counts every `##` heading as an open proposal waiting on the person. If I had written one `##` per flag, Mara would see ten open proposals she can't act on. I put all evidence under one `##` heading with `proposal: none yet`. That is a guess, and `/status` will still count it as one open proposal. The skill needs a place for evidence lines that is not a proposal, or the template needs an "evidence" kind the status script skips.
2. **Step 5 and the template on duplicates.** Step 5 says append the new raw "with its own source line". The template has one `raw` and one `source` field. I added a second `raw:` and `source:` pair inside I2. Any parser of this file will choke. Say what the shape is (numbered raw fields? a `raw_2`? a sub-list?).
3. **Step 5, "repeats a confirmed canon entry word for word".** Nothing on a call repeats a canon claim word for word; I6 repeats P3's claim almost exactly and adds one clause. The rule as written never fires. Make it "the same claim with no new specific" and say what counts as a new specific.
4. **Permission by source (step 7) has no default for a voice memo**, which is the input the skill opens with ("they talk into a phone"). Journal is private, call is anonymize, post is public. The existing bank treats memos as public (I2) or anonymize (I1, names a founder). I set public for memo entries only about her and anonymize when clients appear, then asked. Add the memo default.
5. **The type list has no slot for a method or behavior.** I11 (what the Monday call is) and the "send me bank statements, not the P&L" line in I4 describe how she works. They are not stories, POVs, observations or proof. I typed I11 as POV and said so in the note. The canon has a behaviors layer in the setup templates, so capture should have a matching type, or the skill should say which type behaviors go under.
6. **Step 4 says link to "branches, POVs and values".** Half the useful links this run were to T (thesis), X1 (stop list), S1 (a story), R2 (proof) and W2 (voice rule). I linked them anyway. Say the link set is any canon ID.
7. **Step 10 says "the one question if any"** but step 7 says confirm permission "in one line at the end". With two sources and different defaults that is already two questions. Fine, but don't promise one.

## Guesses I had to make
- The date prefix on `inbox/done/` files: today's date or the source's? The memo already had its date in its name, so I prefixed the processing date (`2026-10-22-memo-2026-10-22.md`). Ugly. Say which.
- `wanted_now` for an entry on the stop list (I8, fundraising). Set no. The skill never says stop-list entries get captured at all; I captured it because how she declines is a V2 behavior and the objection itself is what a reader pushes back with.
- `wanted_now` for I6 (links P3 and the draft B2). B2 is not this quarter's branch, so no, even though P3 is in the plan's layer mix. The step says "fits one of this quarter's branches", so POV-layer fits don't count. Confirm that reading.
- `date` for the appended I2 raw. The entry has one `date` field (2026-10-19) and the appended passage is from 2026-10-21. I left the date and put the second date in the source line.
- Whether to downgrade I2's permission from public to anonymize after appending a sales-call passage. I did, and said so in the summary. The skill covers setting permission on new entries, not on an entry that gets extended with material from a more restricted source.
- Whether a founder's own words on a sales call can be the `raw` of a `story` entry (I4). The founder's moment is the story; Mara's lines are her reply. I kept the FOUNDER/MARA labels in the raw and used `who_said_it` for both. The field's template line says "the person, or the role of whoever said it", singular.
- Step 1 says read the whole thing before splitting; step 2 says a passage carrying two ideas goes into both entries. The P&L passage in the call carries P1 (I5) and feeds the story (I4). I did not copy it into I4; I used "[...]" to mark the cut. The skill does not say whether an ellipsis inside `raw` is allowed. It should, or raw fields will carry whole transcripts.
- "Inputs per week" says report entries this week against the plan's minimum. The plan has no minimum. I reported the count and said there is no number. The skill should tell the strategy skill to set one, or drop the section.

## Smaller things
- The ideas template header says "the writer may use only what a brief cites". Good, but the template's I1 example shows `status: raw` while step 9 says `ready` is the normal case. Show `ready`.
- The template has `wanted_now`, `who_said_it`, `note` fields; the three existing entries (I1 to I3) have none of them. Either the earlier capture skipped them or the fields are newer than the entries. The bank now has two shapes.
- Step 10 says "how many entries this week". A week from when? I used the first entry's date (2026-10-18).
- The memo's "note to self, I should write down what the Monday call is" is the person asking for a canon definition. The skill has no step for "the person asked for something"; I put it in the proposals evidence and the summary.
