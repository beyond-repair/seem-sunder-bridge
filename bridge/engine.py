from __future__ import annotations

from .contract import (
    CLAIM_CAP,
    QUEUE_ID,
    SHARED_OPS,
    SURFACES,
    shared_op_coverage,
)


def report() -> str:
    cov = shared_op_coverage()
    lines = [
        f"queue={QUEUE_ID}",
        f"claim_cap={CLAIM_CAP}",
        f"surfaces={len(SURFACES)}",
    ]
    for op in SHARED_OPS:
        lines.append(f"{op}: {len(cov[op])} surfaces")
    lines.append("runtime_interop=NOT_CLAIMED")
    return "\n".join(lines)


def main() -> None:
    print(report())


if __name__ == "__main__":
    main()
