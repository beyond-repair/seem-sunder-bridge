# Claim status

Lifecycle: RESEARCH
Claim: ≤1 (MODULE_SURFACE)
Version: 0.1.1
Queue: Q-003 closed as a contract checker only

This file records the Sweep-209 re-audit. It does not raise the claim cap.

Claimed:
- Locked surface paths and frozen witnesses `bridge/symbol_witness_2026-10-01.json` and `bridge/symbol_witness_2026-10-02.json`.
- Exact-def presence and absence recorded in those witnesses.
- Default dims 4096 / 8192 / 16384 are unequal.
- Adapter bind/unbind/similarity are NAME_ONLY. register/query stay UNMAPPED.

Not claimed:
- Runtime import or interop.
- Vector-space isomorphism.
- A mind, an agent, or identity unification (Q-FUNC-003).
- That the 2026-10-02 pins still match later default-branch heads. This sweep did not re-read foreign blobs.

CI gate added this sweep: pytest, then `python -m bridge`.
