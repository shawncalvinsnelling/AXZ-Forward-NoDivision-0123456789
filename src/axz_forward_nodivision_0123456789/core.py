"""Core exact verifier for AXZ-Forward-NoDivision-0123456789."""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from pathlib import Path

DIGITS = "0123456789"
TRUTH_LABEL = "CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES"
EXPECTED = {
    "possible_cut_patterns": 512,
    "unique_integer_values_generated": 188911,
    "positive_integer_values_generated": 94455,
    "nonpositive_integer_values_generated": 94456,
    "negative_integer_values_generated": 94455,
    "zero_present": True,
    "consecutive_positive_integers_from_1": 8311,
    "first_missing_positive_integer": 8312,
    "min_value": -123456789,
    "max_value": 123456789,
    "max_absolute_final_bit_length": 27,
    "all_interval_unique_values_generated": 192785,
}
EXPECTED_HASHES = {
    "all_interval_values_sha256": "ad49a3d81fa8f91849393e5b09fa42f62b582b19859e379cf18b5cecd2684320",
    "all_values_sha256": "d8f9c17baa4e88267497cf1be38e4ab3c7fbad6b31c6ef1fcac12b0952d2d530",
    "negative_values_sha256": "595ece93bb0eea85c2518169f910d8a0a0d810b480bbbd500095fbbfa0df31e7",
    "nonpositive_values_sha256": "fcf638442b8b0bbb8e4d30dd83caf8cba77ef8ff56e0f5bfc5527b8dca9c4fed",
    "positive_values_sha256": "8dccc4802d76e7e91fc5999366314d63c72e5c70373830d81a7822141a54947b"
}


@lru_cache(maxsize=None)
def interval_values(i: int, j: int) -> frozenset[int]:
    """Return all values for DIGITS[i:j] under ordered +, -, * and concatenation."""
    if not (0 <= i < j <= len(DIGITS)):
        raise ValueError("interval must satisfy 0 <= i < j <= len(DIGITS)")

    out: set[int] = {int(DIGITS[i:j])}
    for k in range(i + 1, j):
        left = interval_values(i, k)
        right = interval_values(k, j)
        for a in left:
            for b in right:
                out.add(a + b)
                out.add(a - b)
                out.add(a * b)
    return frozenset(out)


def full_values() -> set[int]:
    return set(interval_values(0, len(DIGITS)))


def all_interval_values() -> set[int]:
    out: set[int] = set()
    for i in range(len(DIGITS)):
        for j in range(i + 1, len(DIGITS) + 1):
            out.update(interval_values(i, j))
    return out


def sorted_newline_sha256(values) -> str:
    payload = "".join(f"{int(v)}\n" for v in sorted(values)).encode("utf-8")
    return sha256(payload).hexdigest()


def consecutive_frontier(values: set[int]) -> int:
    n = 0
    while n + 1 in values:
        n += 1
    return n


def compute_certificate() -> dict[str, object]:
    values = full_values()
    positives = {v for v in values if v > 0}
    nonpositives = {v for v in values if v <= 0}
    negatives = {v for v in values if v < 0}
    all_intervals = all_interval_values()
    frontier = consecutive_frontier(values)
    max_abs = max(abs(v) for v in values)
    return {
        "possible_cut_patterns": 2 ** (len(DIGITS) - 1),
        "unique_integer_values_generated": len(values),
        "positive_integer_values_generated": len(positives),
        "nonpositive_integer_values_generated": len(nonpositives),
        "negative_integer_values_generated": len(negatives),
        "zero_present": 0 in values,
        "consecutive_positive_integers_from_1": frontier,
        "first_missing_positive_integer": frontier + 1,
        "min_value": min(values),
        "max_value": max(values),
        "max_absolute_final_bit_length": max_abs.bit_length(),
        "all_interval_unique_values_generated": len(all_intervals),
    }


def compute_hashes() -> dict[str, str]:
    values = full_values()
    return {
        "all_values_sha256": sorted_newline_sha256(values),
        "positive_values_sha256": sorted_newline_sha256(v for v in values if v > 0),
        "nonpositive_values_sha256": sorted_newline_sha256(v for v in values if v <= 0),
        "negative_values_sha256": sorted_newline_sha256(v for v in values if v < 0),
        "all_interval_values_sha256": sorted_newline_sha256(all_interval_values()),
    }


def read_int_file(path: str | Path) -> list[int]:
    return [int(line) for line in Path(path).read_text().splitlines() if line.strip()]
