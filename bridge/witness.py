"""Load the dated symbol witness. Does not import foreign repositories."""

from __future__ import annotations

import json
from pathlib import Path

WITNESS_NAME = "symbol_witness_2026-10-01.json"


def load_witness() -> dict:
    path = Path(__file__).with_name(WITNESS_NAME)
    return json.loads(path.read_text(encoding="utf-8"))


def absent_exact_defs() -> list[str]:
    rows = load_witness()["rows"]
    out: list[str] = []
    for row in rows:
        for name in row["exact_def_absent"]:
            out.append(f"{row['repo']}:{row['path']}::{name}")
    return out


def path_present_count() -> int:
    return sum(1 for row in load_witness()["rows"] if row["path_present"] is True)
