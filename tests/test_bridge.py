from bridge.contract import (
    CLAIM_CAP,
    DISTINCT_IDENTITIES,
    FORBIDDEN_CLAIMS,
    QUEUE_ID,
    SHARED_OPS,
    SURFACES,
    claims_ok,
    shared_op_coverage,
)
from bridge.engine import report


def test_queue_and_cap():
    assert QUEUE_ID == "Q-003"
    assert CLAIM_CAP == "MODULE_SURFACE"


def test_shared_ops_have_multiple_surfaces():
    cov = shared_op_coverage()
    for op in SHARED_OPS:
        assert len(cov[op]) >= 3


def test_sunder_and_seem_present():
    repos = {s.repo for s in SURFACES}
    assert "sunder" in repos
    assert "SEEM-2.0-Self-Evolving-Emergent-Mind" in repos
    assert "sovereign-clean-room" in repos


def test_identities_remain_distinct():
    assert len(set(DISTINCT_IDENTITIES)) == len(DISTINCT_IDENTITIES)


def test_forbidden_claims_detected():
    assert claims_ok("contract only")
    assert not claims_ok("working autonomous agent across repos")


def test_report_does_not_claim_runtime():
    text = report()
    assert "NOT_CLAIMED" in text
    assert "runtime_interop=NOT_CLAIMED" in text
