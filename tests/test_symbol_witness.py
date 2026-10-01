from bridge.witness import absent_exact_defs, load_witness, path_present_count


def test_witness_paths_still_recorded_present():
    data = load_witness()
    assert data["runtime_import"] is False
    assert path_present_count() == 10


def test_known_op_mismatches_remain_absent():
    missing = set(absent_exact_defs())
    assert "sunder:sunder/agent.py::scan" in missing
    assert "sunder:sunder/gate.py::gate" in missing
    assert "sunder:sunder/fork.py::fork" in missing
    assert "SEEM-2.0-Self-Evolving-Emergent-Mind:seem.py::cycle" in missing
    assert "SEEM-2.0-Self-Evolving-Emergent-Mind:resonator_vsa.py::similarity" in missing
    assert "sunder:sunder/vsa.py::bind" not in missing
