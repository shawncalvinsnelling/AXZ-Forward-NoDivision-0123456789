from axz_forward_nodivision_0123456789.core import EXPECTED_HASHES, compute_hashes


def test_hashes_match_expected():
    assert compute_hashes() == EXPECTED_HASHES
