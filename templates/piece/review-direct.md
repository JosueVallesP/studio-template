---
piece: <piece ID>
draft: draft-vN.md
draft_sha256: <sha256 of the draft as you read it: `sha256sum pieces/<id>/draft-vN.md`>
reviewer: judge agent (studio version from studio.manifest.yaml)
date: <yyyy-mm-dd>
verdict: <pass / revise / redo>
---
# Review: <piece ID>, draft vN

This is the review for any direct piece (`path: direct`: `/post`, `/essay`, the first post). The `judge` agent writes it in a fresh context, against the brief, the draft and the material the brief cites. The grades come from the gates table in `skills/role-editor`, and the verdict from the ladder in the format's judge stage.

## Source

The material files read: <file names>.

## Verdict

<pass, revise or redo, and one line on why.>

## The one thing

<The deepest failing lever (`skills/craft-refine`), the quoted line and the fix; "none" on a pass. The writer revises from this line and every graded fail.>

## Fails

Numbered, in the judge's order. For each: the check number, the rule number for a writing-rule or machine-pattern fail (the H number from the house rules or the W number from the voice guide), the line quoted, its grade (revise or redo), what's wrong, the fix if it's obvious.

1.

## Argument chain

The chain check (`skills/craft-copylosophy`, "The chain check"): the one idea in a sentence, then the numbered steps with the draft's lines quoted, and each fail marked on the step where it sits.

1.

## Outside cases

Each `borrowed: verify` case: the link it was checked against and the details that held, or "not checked" with the details to confirm (`skills/role-editor`, "Checking an outside case").

## Human check

`skills/check-human`: pass or fix, with the patterns and quoted lines. Lines quoted word for word from the person's material are marked "theirs" and not counted. Detector: the label and fractions, which draft it was run on (the first judged draft only), or "not run" with the reason.

## Voiceprint

The VOICEPRINT block from `python3 scripts/voiceprint.py score <draft>` on the first judged draft, once `bank/voiceprint/profile.json` exists (`skills/check-voiceprint`); a reading, never a fail by itself. "no profile yet" otherwise, and "read on v1" on a revision.

## Worth noting

At most two things the draft does well.

## For the person

Every `inferred` line, quoted, with the proposal it went to; nothing ships until the person has seen these. If this is the last pass, each remaining fail as one plain line they can read without knowing the checks.
