from __future__ import annotations

from axz_forward_nodivision_0123456789.core import EXPECTED, TRUTH_LABEL, compute_certificate, full_values


def main() -> None:
    cert = compute_certificate()
    for key, expected in EXPECTED.items():
        actual = cert[key]
        assert actual == expected, f"{key} mismatch: {actual!r} != {expected!r}"
    values = full_values()
    assert all(n in values for n in range(1, EXPECTED["consecutive_positive_integers_from_1"] + 1))
    assert EXPECTED["first_missing_positive_integer"] not in values
    print(f"PASS: {TRUTH_LABEL}")


if __name__ == "__main__":
    main()
