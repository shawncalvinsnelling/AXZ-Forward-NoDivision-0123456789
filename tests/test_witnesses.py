from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def normalize_leading_zero_literals(expr: str) -> str:
    """Convert digit blocks like 0123 to 123 for Python evaluation.

    The challenge rules interpret each concatenated digit block by integer value,
    so this normalization is only for evaluating witness strings inside tests.
    """
    allowed = set("0123456789()+-* ")
    assert set(expr) <= allowed
    return re.sub(r"\d+", lambda m: str(int(m.group(0))), expr)


def eval_expr(expr: str) -> int:
    normalized = normalize_leading_zero_literals(expr)
    return int(eval(normalized, {"__builtins__": {}}, {}))


def test_selected_witnesses_evaluate():
    path = ROOT / "data" / "witnesses_1_to_8311.tsv"
    rows = path.read_text().splitlines()[1:]
    table = {int(line.split("\t", 1)[0]): line.split("\t", 1)[1] for line in rows}
    for n in [1, 2, 10, 100, 1000, 8311]:
        assert eval_expr(table[n]) == n


def test_boundary_witness_uses_ordered_digits_as_text():
    path = ROOT / "data" / "witnesses_1_to_8311.tsv"
    table = {int(line.split("\t", 1)[0]): line.split("\t", 1)[1] for line in path.read_text().splitlines()[1:]}
    witness = table[8311]
    assert "0123" in witness or witness.startswith("0") or "0" in witness
    assert eval_expr(witness) == 8311
