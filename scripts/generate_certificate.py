from __future__ import annotations

import json
from pathlib import Path

from axz_forward_nodivision_0123456789.core import DIGITS, EXPECTED_HASHES, TRUTH_LABEL, compute_certificate

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cert = {
        "repository": "AXZ-Forward-NoDivision-0123456789",
        "challenge": "AXZ Forward 0-to-9 No-Division Ordered Arithmetic Gap",
        "challenge_number": 3,
        "digit_sequence": DIGITS,
        "truth_label": TRUTH_LABEL,
        "certificate": compute_certificate(),
        "hashes": EXPECTED_HASHES,
    }
    out = ROOT / "certificates" / "generated_certificate.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(f"PASS: wrote {out}")


if __name__ == "__main__":
    main()
