"""Load dated symbol witnesses. Does not import foreign repositories."""

from __future__ import annotations

import json
from pathlib import Path

WITNESS_NAME = "symbol_witness_2026-10-01.json"
REREAD_NAME = "symbol_witness_2026-10-02.json"


def load_witness(name: str = WITNESS_NAME) -> dict:
    path = Path(__file__).with_name(name)
    return json.loads(path.read_text(encoding="utf-8"))


def load_reread() -> dict:
    return load_witness(REREAD_NAME)


def absent_exact_defs() -> list[str]:
    rows = load_witness()["rows"]
    out: list[str] = []
    for row in rows:
        for name in row["exact_def_absent"]:
            out.append(f"{row['repo']}:{row['path']}::{name}")
    return out


def path_present_count(name: str = WITNESS_NAME) -> int:
    return sum(1 for row in load_witness(name)["rows"] if row["path_present"] is True)


def row_map(data: dict) -> dict[tuple[str, str], dict]:
    return {(row["repo"], row["path"]): row for row in data["rows"]}
