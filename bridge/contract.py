"""Locked surface mapping. Dated 2026-09-05. Not a live importer."""

from __future__ import annotations

from dataclasses import dataclass

SNAPSHOT_DATE = "2026-09-05"
QUEUE_ID = "Q-003"
CLAIM_CAP = "MODULE_SURFACE"

FORBIDDEN_CLAIMS = (
    "working autonomous agent across repos",
    "vector-space isomorphism",
    "runtime import of sunder or SEEM",
    "SUPERSEDES among SEEM hyphen/underscore forks",
)


@dataclass(frozen=True)
class Surface:
    repo: str
    path: str
    ops: tuple[str, ...]
    cap: str


SURFACES: tuple[Surface, ...] = (
    Surface(
        "sunder",
        "sunder/vsa.py",
        ("bind", "unbind", "similarity", "register", "query"),
        "MODULE_SURFACE",
    ),
    Surface(
        "sunder",
        "sunder/agent.py",
        ("scan", "snap", "sunder"),
        "MODULE_SURFACE",
    ),
    Surface(
        "sunder",
        "sunder/gate.py",
        ("gate",),
        "MODULE_SURFACE",
    ),
    Surface(
        "sunder",
        "sunder/fork.py",
        ("fork",),
        "MODULE_SURFACE",
    ),
    Surface(
        "sovereign-clean-room",
        "core/clean_room_vsa.py",
        ("bind", "unbind", "similarity"),
        "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    ),
    Surface(
        "SEEM-2.0-Self-Evolving-Emergent-Mind",
        "resonator_vsa.py",
        ("bind", "unbind", "similarity"),
        "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    ),
    Surface(
        "SEEM-2.0-Self-Evolving-Emergent-Mind",
        "banel.py",
        ("banel",),
        "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    ),
    Surface(
        "SEEM-2.0-Self-Evolving-Emergent-Mind",
        "seem.py",
        ("cycle",),
        "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    ),
    Surface(
        "SEEM-2.0-Self-Evolving-Emergent-Mind",
        "dream_phase.py",
        ("dream",),
        "TREE_PRESENT_FUNCTIONS_UNAUDITED",
    ),
    Surface(
        "sunder-cleanroom-vsa-adapter",
        "adapter/",
        ("bind", "unbind", "similarity", "register", "query"),
        "MODULE_SURFACE",
    ),
)

SHARED_OPS = ("bind", "unbind", "similarity")

DISTINCT_IDENTITIES = (
    "SEEM-2.0-Self-Evolving-Emergent-Mind",
    "SEEM-Cognitive-Microservice",
    "SEEM-Cognitive_Microservice",
    "sunder",
    "sovereign-clean-room",
)


def shared_op_coverage() -> dict[str, list[str]]:
    """Count claimed op strings on SURFACES. This is not an exact-def census."""
    out: dict[str, list[str]] = {op: [] for op in SHARED_OPS}
    for s in SURFACES:
        for op in SHARED_OPS:
            if op in s.ops:
                out[op].append(f"{s.repo}:{s.path}")
    return out


def claims_ok(text: str) -> bool:
    lowered = text.lower()
    return not any(f.lower() in lowered for f in FORBIDDEN_CLAIMS)
