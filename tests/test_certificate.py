from axz_forward_nodivision_0123456789.core import EXPECTED, compute_certificate, full_values


def test_certificate_matches_expected():
    assert compute_certificate() == EXPECTED


def test_frontier_and_first_missing():
    values = full_values()
    assert all(n in values for n in range(1, 8312))
    assert 8312 not in values
