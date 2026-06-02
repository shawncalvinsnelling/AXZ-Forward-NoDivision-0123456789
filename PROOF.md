# Proof Outline

## Claim

For the ordered digit sequence `0123456789`, with concatenation and operations `+`, `-`, and `*`, every positive integer from `1` through `8311` is represented by at least one valid ordered expression, and `8312` is not represented.

## Formal universe

For every nonempty interval `D[i:j]`, the verifier computes a finite set `V(i,j)`.

1. The concatenation leaf `int(D[i:j])` is included.
2. For every split `i < k < j`, every `a in V(i,k)`, and every `b in V(k,j)`, the verifier includes `a+b`, `a-b`, and `a*b`.
3. No other values are included.

This is an exact recurrence over all ordered binary expression trees whose leaves are a partition of the digit string into adjacent nonempty blocks.

## Soundness

Every generated value corresponds to a legal expression by induction on interval length.

## Completeness

Every legal expression has a root split into a left interval and a right interval. By induction, the subexpressions appear in the appropriate interval sets, and the root operation is one of the three operations applied by the recurrence.

## Finite certificate result

The checked recurrence produces `188,911` final values. It verifies all values from `1` to `8311` are present and `8312` is absent.

Truth label: `CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES`.
