from __future__ import annotations

from pathlib import Path

from axz_forward_nodivision_0123456789.core import EXPECTED_HASHES, compute_hashes, read_int_file, sorted_newline_sha256

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FILE_MAP = {
    "all_values_sha256": DATA / "all_values_sorted.txt",
    "positive_values_sha256": DATA / "positive_values_sorted.txt",
    "nonpositive_values_sha256": DATA / "nonpositive_values_sorted.txt",
    "negative_values_sha256": DATA / "negative_values_sorted.txt",
    "all_interval_values_sha256": DATA / "all_interval_values_sorted.txt",
}


def main() -> None:
    computed = compute_hashes()
    for key, expected in EXPECTED_HASHES.items():
        assert computed[key] == expected, f"computed {key} mismatch"
        file_hash = sorted_newline_sha256(read_int_file(FILE_MAP[key]))
        assert file_hash == expected, f"file {key} mismatch"
    print("PASS: DATA_HASHES_MATCH")


if __name__ == "__main__":
    main()
