import copy
import tomllib
from pathlib import Path

import bridge
from bridge.check import invariants
from bridge.contract import claims_ok
from bridge.engine import main, report
from bridge.witness import load_reread, load_witness


def test_version_pinned():
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    assert bridge.__version__ == "0.1.1"
    assert project["project"]["version"] == "0.1.1"


def test_reread_matches_historical_shape():
    assert invariants(load_witness(), load_reread()) == []


def test_report_is_honest_and_ok():
    text = report()
    assert text.endswith("OK")
    assert "runtime_interop=NOT_CLAIMED" in text
    assert "isomorphism=NOT_CLAIMED" in text
    assert "mind=NOT_CLAIMED" in text
    assert "dims=4096/8192/16384" in text
    assert "dim_mismatch=true" in text
    assert "adapter_algebra=NAME_ONLY" in text
    assert "register_query=UNMAPPED" in text
    assert "resonator_similarity_was_absent=true" in text
    assert "resonator_similarity_now_present=true" in text
    assert "exact_def_absent_2026-10-02=13" in text
    assert claims_ok(text)
    assert main() == 0


def test_hiding_new_similarity_fails():
    historical = load_witness()
    reread = copy.deepcopy(load_reread())
    row = next(item for item in reread["rows"] if item["path"] == "resonator_vsa.py")
    row["exact_def_present"].remove("similarity")
    row["exact_def_absent"].append("similarity")
    errors = invariants(historical, reread)
    assert any("similarity" in err for err in errors)
