# Project guidance

Write 3–5 concrete bullets of your own and save as `AGENTS.md`. Combine related points where useful.
The instructions below are example ideas. Keep them relatively short and specific.

- Project and Context: This is an in-memory meeting-room booking prototype. Implement move_booking in service.py to move existing reservations according to the rules in SPEC.md.
- Preservation and Scope: Keep changes strictly limited to service.py, test_student.py, and AGENTS.md. Do not modify models.py, test_baseline.py, test_move_smoke.py, or SPEC.md.
- Checks: Run uv run --python 3.12 python -m unittest -v test_baseline  and uv run --python 3.12 python -m unittest -v test_move_smoke to execute the full test suite and verify changes.
- Review: Stop and ask for my approval before making any helper edits to rules.py or modifying any public function signatures.

