# Claims

This repository implements `adl-capability-matrix` item Q-003 as a **contract**, not a runtime.

Assumptions:

- A1: User requested a portfolio sweep and a compatible next repository.
- A2: GitHub search `user:beyond-repair` on 2026-09-04/05 enumerated 70 repositories (67 public in earlier census lock + later governance repos).
- A2: Default-branch trees for `sunder`, `sovereign-clean-room`, and `SEEM-2.0-Self-Evolving-Emergent-Mind` contain the listed paths.
- A2 (2026-10-01 re-read): those paths are still present. Exact `def` names match `sunder/vsa.py` bind/unbind/similarity/register/query and clean-room bind/unbind/similarity. They do not match agent scan/snap/sunder, gate, fork, SEEM cycle/dream/banel, or resonator `similarity`.
- A4: Shared operation names do not imply isomorphic implementations.
- A2 (2026-10-02 re-read, raw files at named commits, no import): sunder `c7d4596` still has no exact defs named scan/snap/sunder/gate/fork (`VSAMemory` methods and dim 4096 unchanged); sovereign-clean-room `4878918` blob unchanged, dim 8192; SEEM-2.0 `2354210` now has `ResonatorVSA.similarity` and default dim 16384, while cycle/dream/banel are still not exact defs; adapter `1a28322` keeps bind/unbind/similarity as NAME_ONLY and register/query unmapped, with no function defs of those names.

Rejected hypotheses:

- All 70 repositories have AST-audited function inventories.
- Duplicate SEEM names are the same artifact.
- A bridge repository constitutes a running multi-repo agent.
- A claimed op string equals an exact `def` of that name (falsified 2026-10-01 for several surfaces; see `bridge/symbol_witness_2026-10-01.json`).
