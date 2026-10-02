<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · runtime interop · a mind
```

</div>

---

# seem-sunder-bridge

Claim-capped **interop contract** (v0.1.1) among:

- `sunder` at `c7d4596` — local SCAN/SNAP/gate/fork heuristic, not a supervisor (`sunder/vsa.py`, `agent.py`, `gate.py`, `fork.py`)
- `sovereign-clean-room` at `4878918` — offline VSA core (`core/clean_room_vsa.py`), not a mind
- `SEEM-2.0-Self-Evolving-Emergent-Mind` at `2354210` (`seem.py`, `banel.py`, `resonator_vsa.py`, `dream_phase.py`)
- `sunder-cleanroom-vsa-adapter` at `1a28322` — name-only VSA surface (Q-FUNC-002)

This repository closes queue item **Q-003** from `adl-capability-matrix` as a contract checker.

It does **not** close `Q-FUNC-003` (`seem-identity-unifier`). The SEEM hyphen and underscore repositories stay distinct. Nothing here imports those trees, runs an agent, or unifies a mind.

## Claim contract

| Claimed | Not claimed |
|---|---|
| Locked paths, plus the frozen 2026-10-01 symbol witness | Importing sunder, SEEM, clean-room, or the adapter |
| 2026-10-02 re-read: which claimed op strings are exact `def` names at the commits above | That a shared op string is an isomorphism |
| `ResonatorVSA.similarity` is new since that witness; scan, gate, fork, cycle, dream, and banel still are not exact defs | A cross-repo agent, a supervisor LLM, or a mind |
| Default dims differ: sunder 4096, clean-room 8192, SEEM resonator 16384 | Equal dimensions or equal algebras |
| Adapter bind/unbind/similarity are NAME_ONLY; register/query stay UNMAPPED and are not local function defs | Q-FUNC-003 identity unification |

Claim cap: **MODULE_SURFACE**.

`bridge/contract.py` still lists the original claimed op strings. `shared_op_coverage()` counts those strings only. Exact def presence is the witness files, not that table. The 2026-10-01 witness is kept as written, including absences that the later re-read no longer shares.

## Install and run

Python 3.11+. From a fresh clone of the default branch:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m bridge
python -m pytest -q
```

`python -m bridge` (same as `python -m bridge.engine`) prints the contract and `OK`, then exits 0. A drifted witness prints `ERROR` lines and `FAIL`, then exits 1.

No configuration file. The checker does not use the network.

`requirements.txt` only pins pytest for the existing workflow, which installs that file and runs pytest from the repository root. The install above is the supported path.

## Related

- `adl-capability-matrix` Q-003
- `adl-function-census` Q-FUNC-002 (closed by `sunder-cleanroom-vsa-adapter`, name contract only)
- `ADL-Governance`, `ADL-SEEM`, `forge-aegis` (no runtime claim)


---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
