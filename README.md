# seem-sunder-bridge

Claim-capped **interop contract** among:

- `sunder` (SCAN → SNAP → SUNDER agent; `sunder/vsa.py`, `agent.py`, `gate.py`, `fork.py`)
- `sovereign-clean-room` (FHRR / BaNEL VSA core)
- `SEEM-2.0-Self-Evolving-Emergent-Mind` (`seem.py`, `banel.py`, `resonator_vsa.py`, `dream_phase.py`)
- `sunder-cleanroom-vsa-adapter` (Q-FUNC-002 VSA surface only)
- `forge-aegis` (FLS identities; no runtime claim)

This repository closes queue item **Q-003** from `adl-capability-matrix`.

It does **not** close `Q-FUNC-003` (`seem-identity-unifier`). Duplicate SEEM microservice identities remain distinct.

## Claim contract

| Claimed | Not claimed |
|---|---|
| Named module surfaces exist on default branches as of 2026-09-04/05 | Runtime import of sunder, SEEM, or clean-room |
| Shared *named* operations: bind, unbind, similarity, register/query, gate, fork, dream | Vector-space isomorphism |
| Deterministic mapping table + validation tests | Working autonomous agent across repos |
| Distinct identities (no SUPERSEDES) | Equivalence of SEEM hyphen/underscore forks |

Claim cap of this repo: **MODULE_SURFACE**.

## Run

```bash
pip install -r requirements.txt
python -m bridge.engine
python -m pytest -q
```

## Related

- `adl-capability-matrix` Q-003
- `adl-function-census` Q-FUNC-002 (closed by `sunder-cleanroom-vsa-adapter`)
- `ADL-Governance`, `ADL-SEEM`, `forge-aegis`
