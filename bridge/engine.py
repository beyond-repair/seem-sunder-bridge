"""Print the Q-003 contract. Does not import sunder, SEEM, or clean-room."""

from __future__ import annotations

from bridge import __version__
from bridge.check import invariants
from bridge.contract import CLAIM_CAP, QUEUE_ID, SURFACES
from bridge.witness import load_reread, load_witness, row_map

_RESONATOR = ("SEEM-2.0-Self-Evolving-Emergent-Mind", "resonator_vsa.py")
_ADAPTER = ("sunder-cleanroom-vsa-adapter", "adapter/")


def report() -> str:
    historical = load_witness()
    reread = load_reread()
    errors = invariants(historical, reread)
    historical_rows = row_map(historical)
    reread_rows = row_map(reread)
    old_similarity = "similarity" in historical_rows[_RESONATOR]["exact_def_absent"]
    new_similarity = "similarity" in reread_rows[_RESONATOR]["exact_def_present"]
    dims = reread["dims"]
    distinct = len({dims["sunder"], dims["cleanroom"], dims["seem_resonator"]}) == 3
    mismatch = dims["equal"] is False and distinct
    absent = sum(len(row["exact_def_absent"]) for row in reread["rows"])
    adapter = reread_rows[_ADAPTER]
    historical_paths = sum(1 for row in historical["rows"] if row["path_present"] is True)
    reread_paths = sum(1 for row in reread["rows"] if row["path_present"] is True)
    lines = [
        f"queue={QUEUE_ID}",
        f"claim_cap={CLAIM_CAP}",
        f"version={__version__}",
        f"surfaces={len(SURFACES)}",
        f"witness_2026-10-01_paths={historical_paths}",
        f"witness_2026-10-02_paths={reread_paths}",
        f"exact_def_absent_2026-10-02={absent}",
        f"resonator_similarity_was_absent={str(old_similarity).lower()}",
        f"resonator_similarity_now_present={str(new_similarity).lower()}",
        f"dims={dims['sunder']}/{dims['cleanroom']}/{dims['seem_resonator']}",
        f"dim_mismatch={str(mismatch).lower()}",
        f"adapter_algebra={adapter['algebra']}",
        f"register_query={adapter['register_query']}",
        "runtime_interop=NOT_CLAIMED",
        "isomorphism=NOT_CLAIMED",
        "mind=NOT_CLAIMED",
    ]
    for err in errors:
        lines.append(f"ERROR {err}")
    lines.append("FAIL" if errors else "OK")
    return "\n".join(lines)


def main() -> int:
    text = report()
    print(text)
    return 0 if text.endswith("OK") else 1


if __name__ == "__main__":
    raise SystemExit(main())
