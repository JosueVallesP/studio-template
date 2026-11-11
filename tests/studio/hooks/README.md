# Hook tests

Each `.json` file here is one tool call as Claude Code hands it to a hook, plus two fields the runner reads: `hook` (guard-writes or guard-bash; the file name's `writes-` or `bash-` prefix works too) and `expect` (allow or deny). Run `bash tests/studio/hooks/run.sh` from the repo root after any change to `.claude/hooks/`; it feeds every payload to its hook in an empty temp folder, prints one line per payload, and exits 1 when any decision differs from `expect`. To test a new rule, add a payload that the rule should allow and one it should deny.
