# AXZ Forward 0-to-9 No-Division Ordered Arithmetic Gap

This repository is a finite exact computational proof for the ordered digit sequence:

```text
0 1 2 3 4 5 6 7 8 9
```

Source note: Forward decimal digit sequence with a leading zero leaf allowed.

## Theorem

Under the stated rules, every positive integer from 1 through **8311** is representable, and the first missing positive integer is:

```text
8312
```

## Rules

- Digit sequence: `0 1 2 3 4 5 6 7 8 9`.
- Each digit position is used exactly once.
- Digits must remain in order.
- Concatenation is allowed; leading-zero substrings such as `01` are interpreted by integer value.
- Allowed operations: `+`, `-`, `*`.
- Parentheses are allowed through all ordered binary expression trees.
- Subtraction is directional: left subtree minus right subtree only.
- Division, powers, factorials, square roots, decimals, logs, hidden constants, and digit reordering are forbidden.

## Dynamic-programming recurrence

Let `D = 0123456789`.

For each interval `D[i:j]`, define `V(i,j)` as the set that starts with the concatenation leaf `int(D[i:j])`, then combines all left/right split values using the allowed operators.

The full universe is `V(0,10)`.

## Certificate

- Possible cut patterns: **512**
- Unique integer values generated: **188,911**
- Positive integer values generated: **94,455**
- Non-positive integer values generated: **94,456**
- Negative integer values generated: **94,455**
- Zero present: **true**
- Consecutive positive integers from 1: **8,311**
- First missing positive integer: **8,312**

## Boundary witness

```text
8311 = ((((0123*(4+5))-67)*8)-9)
```

The integer `8312` is absent from the exact dynamic-programming value set.

## Reproduce locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
export PYTHONPATH="$PWD/src"      # Windows PowerShell: $env:PYTHONPATH="$PWD/src"

python scripts/verify_runtime_safety.py
python scripts/verify_challenge_3.py
python scripts/verify_data_hashes.py
python -m pytest -q
```

## Hashes

All-values SHA-256:

```text
d8f9c17baa4e88267497cf1be38e4ab3c7fbad6b31c6ef1fcac12b0952d2d530
```

Positive-values SHA-256:

```text
8dccc4802d76e7e91fc5999366314d63c72e5c70373830d81a7822141a54947b
```

Non-positive-values SHA-256:

```text
fcf638442b8b0bbb8e4d30dd83caf8cba77ef8ff56e0f5bfc5527b8dca9c4fed
```

Negative-values SHA-256:

```text
595ece93bb0eea85c2518169f910d8a0a0d810b480bbbd500095fbbfa0df31e7
```

All-interval-values SHA-256:

```text
ad49a3d81fa8f91849393e5b09fa42f62b582b19859e379cf18b5cecd2684320
```

## Truth label

```text
CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES
```

This repository proves only this finite ordered-expression universe under the exact stated rules.
