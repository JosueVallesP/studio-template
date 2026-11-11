# Packet test

`run.py` copies the writer-editor-mara brief into a temporary piece folder (adding a TYPE line), builds the writer's packet with `scripts/packet.py`, and checks what the packet holds: the writer's sheet first, the brief's sections, only the cards the plan names (never the whole library), the type's draft step without the judge's checks, and the voice. Run: `python3 tests/studio/packet/run.py`.
