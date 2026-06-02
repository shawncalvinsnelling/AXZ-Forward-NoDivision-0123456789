from __future__ import annotations


def main() -> None:
    a = 2**130 + 123456789
    b = 2**97 + 987654321
    assert (a + b) - b == a
    assert (a * b) // b == a
    assert (a - b) + b == a
    print("PASS: ARBITRARY_PRECISION_RUNTIME_GUARD")


if __name__ == "__main__":
    main()
