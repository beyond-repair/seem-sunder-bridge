"""Consistency checks for the locked witnesses. Does not import foreign repos."""

from __future__ import annotations

import ast
from pathlib import Path

from bridge.contract import CLAIM_CAP, QUEUE_ID, SURFACES
from bridge.witness import row_map

# Exact names the 2026-10-01 witness recorded as absent. Do not rewrite that file
# to match later commits.
HISTORICAL_ABSENT = (
    ("sunder", "sunder/agent.py", "scan"),
    ("sunder", "sunder/agent.py", "snap"),
    ("sunder", "sunder/agent.py", "sunder"),
    ("sunder", "sunder/gate.py", "gate"),
    ("sunder", "sunder/fork.py", "fork"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "seem.py", "cycle"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py", "similarity"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "banel.py", "banel"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "dream_phase.py", "dream"),
)

# similarity on resonator_vsa.py moved to exact_def_present on 2026-10-02.
REREAD_STILL_ABSENT = tuple(
    item for item in HISTORICAL_ABSENT if item[1:] != ("resonator_vsa.py", "similarity")
)

REREAD_PRESENT = (
    ("sunder", "sunder/vsa.py", "bind"),
    ("sunder", "sunder/vsa.py", "unbind"),
    ("sunder", "sunder/vsa.py", "similarity"),
    ("sunder", "sunder/vsa.py", "register"),
    ("sunder", "sunder/vsa.py", "query"),
    ("sovereign-clean-room", "core/clean_room_vsa.py", "bind"),
    ("sovereign-clean-room", "core/clean_room_vsa.py", "unbind"),
    ("sovereign-clean-room", "core/clean_room_vsa.py", "similarity"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py", "bind"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py", "unbind"),
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py", "similarity"),
)

COMMITS = {
    "sunder": "c7d4596c13b8aa0e672b40db94edc6655512b385",
    "sovereign-clean-room": "4878918cf9f95d3c19e1890bef6d2fd6713e0a16",
    "SEEM-2.0-Self-Evolving-Emergent-Mind": "2354210da84ab6a6389ae6108c3b889e028fd5da",
    "sunder-cleanroom-vsa-adapter": "1a2832243ee99cb1f250b90147f641c4979f04a2",
}

UNCHANGED_BLOBS = {
    ("sunder", "sunder/vsa.py"): "584190696218d2ccf3146c4ecfd427f92a060980",
    ("sunder", "sunder/gate.py"): "a3bd5dac7b184dc0645223b9ffad02d7d50a98e6",
    ("sovereign-clean-room", "core/clean_room_vsa.py"): "b086ae84d397415716b16cd9b36c2c15c624ad46",
}

REREAD_BLOBS = {
    ("sunder", "sunder/agent.py"): "ef41ab54b1fdd59509630fc4fbdc8a977a4e1524",
    ("sunder", "sunder/fork.py"): "28d78bfc1762fb900fc8e3c02e323cd3f6989090",
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py"): "20cdcc9f28d5dbba0b29e5d1dbdce700f744558c",
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "banel.py"): "2fa37f095f148cc04c723dc53002244e24e20e26",
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "seem.py"): "16ee336100c6cbbae9a03aaac8cd9ed130968e12",
    ("SEEM-2.0-Self-Evolving-Emergent-Mind", "dream_phase.py"): "22f0d0437d1666acd0611ace7fbd38d2c5253be8",
}

LOCAL_DEF_BAN = frozenset(
    {
        "bind",
        "unbind",
        "similarity",
        "register",
        "query",
        "scan",
        "snap",
        "sunder",
        "gate",
        "fork",
        "dream",
        "cycle",
        "banel",
    }
)


def local_def_names() -> set[str]:
    names: set[str] = set()
    package = Path(__file__).resolve().parent
    for path in sorted(package.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                names.add(node.name)
    return names


def _missing(row: dict | None, name: str, bucket: str) -> bool:
    return row is None or name not in row[bucket]


def invariants(historical: dict, reread: dict) -> list[str]:
    errors: list[str] = []
    if historical.get("observed_at") != "2026-10-01":
        errors.append("historical observed_at")
    if historical.get("runtime_import") is not False:
        errors.append("historical runtime_import")
    if reread.get("observed_at") != "2026-10-02":
        errors.append("reread observed_at")
    if reread.get("runtime_import") is not False:
        errors.append("reread runtime_import")
    if reread.get("isomorphism") is not False:
        errors.append("isomorphism must stay false")
    if reread.get("mind") is not False:
        errors.append("mind must stay false")
    if QUEUE_ID != "Q-003" or CLAIM_CAP != "MODULE_SURFACE":
        errors.append("queue or cap drifted")

    hrows = row_map(historical)
    rrows = row_map(reread)
    surface_keys = [(surface.repo, surface.path) for surface in SURFACES]
    if list(hrows) != surface_keys or list(rrows) != surface_keys:
        errors.append("witness rows do not match SURFACES")
    if len(surface_keys) != 10:
        errors.append("surface count")

    for repo, path, name in HISTORICAL_ABSENT:
        row = hrows.get((repo, path))
        if _missing(row, name, "exact_def_absent") or (
            row is not None and name in row["exact_def_present"]
        ):
            errors.append(f"historical absence lost {repo}:{path}::{name}")

    for repo, path, name in REREAD_STILL_ABSENT:
        row = rrows.get((repo, path))
        if _missing(row, name, "exact_def_absent") or (
            row is not None and name in row["exact_def_present"]
        ):
            errors.append(f"reread absence lost {repo}:{path}::{name}")

    for repo, path, name in REREAD_PRESENT:
        row = rrows.get((repo, path))
        if _missing(row, name, "exact_def_present") or (
            row is not None and name in row["exact_def_absent"]
        ):
            errors.append(f"reread presence lost {repo}:{path}::{name}")

    for surface in SURFACES:
        row = rrows.get((surface.repo, surface.path))
        if row is None or tuple(row["claimed_ops"]) != surface.ops:
            errors.append(f"claimed ops drifted {surface.repo}:{surface.path}")

    dims = reread.get("dims") or {}
    values = (dims.get("sunder"), dims.get("cleanroom"), dims.get("seem_resonator"))
    if values != (4096, 8192, 16384):
        errors.append("dims drifted")
    if dims.get("equal") is not False or len(set(values)) != 3:
        errors.append("dims marked equal")

    commits = reread.get("commits") or {}
    for repo, sha in COMMITS.items():
        if commits.get(repo) != sha:
            errors.append(f"commit pin {repo}")

    for key, row in rrows.items():
        repo, path = key
        if row.get("path_present") is not True:
            errors.append(f"path not present {repo}:{path}")
        if row.get("commit") != COMMITS[repo]:
            errors.append(f"row commit {repo}:{path}")

    for key, sha in UNCHANGED_BLOBS.items():
        if rrows[key].get("blob_sha") != sha or hrows[key].get("blob_sha") != sha:
            errors.append(f"unchanged blob drifted {key[0]}:{key[1]}")

    for key, sha in REREAD_BLOBS.items():
        if rrows[key].get("blob_sha") != sha:
            errors.append(f"reread blob drifted {key[0]}:{key[1]}")
        old = hrows[key].get("blob_sha")
        if old == sha:
            errors.append(f"reread blob was already historical {key[0]}:{key[1]}")

    adapter = rrows.get(("sunder-cleanroom-vsa-adapter", "adapter/"))
    if adapter is None or adapter.get("algebra") != "NAME_ONLY":
        errors.append("adapter algebra")
    elif adapter.get("register_query") != "UNMAPPED":
        errors.append("register/query mapping drifted")
    else:
        for name in ("bind", "unbind", "similarity", "register", "query"):
            if name not in adapter["exact_def_absent"] or name in adapter["exact_def_present"]:
                errors.append(f"adapter defines {name}")

    banned = sorted(LOCAL_DEF_BAN & local_def_names())
    if banned:
        errors.append("local defs " + ",".join(banned))
    return errors
