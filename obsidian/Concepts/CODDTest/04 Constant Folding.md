# Constant Folding

## In one sentence

**Constant folding** means evaluating an expression when its value is already knowable.

## Tiny compiler example

    3 + 5  →  8

## SQL example

Suppose:

    SELECT MIN(c0) FROM t0

returns:

    1

Under the current database state, CODDTest can treat 1 as the evaluated result of that expression.

## Why CODDTest cares

CODDTest selects an expression φ and uses an auxiliary query A to compute its result Rφ.

In the paper's notation:

    Rφ = E_s(A[φ])

That evaluation step is the "folding" part.

## Don't confuse it with

CODDTest is **not mainly testing whether MySQL's optimizer performs constant folding**.

The researchers borrow constant folding as a way to create a second, equivalent test query.

## Next concept

Once CODDTest knows Rφ, it uses [[05 Constant Propagation|constant propagation]] to substitute the value into the query.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=5]]
