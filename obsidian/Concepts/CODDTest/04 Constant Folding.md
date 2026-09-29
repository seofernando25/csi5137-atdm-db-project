# Constant Folding

**Constant folding** evaluates an expression whose result can already be determined.

Classic compiler example:

3 + 5 → 8

CODDTest applies the same idea to SQL under a fixed database state.

Suppose:

SELECT MIN(c0) FROM t0

returns 1. CODDTest treats 1 as the folded value Rφ for that state.

## Important nuance

CODDTest is not primarily checking whether the optimizer itself performs constant folding. Folding is used as a test transformation.

In the paper:

Rφ = E_s(A[φ])

The auxiliary query A evaluates φ.

Then [[05 Constant Propagation|constant propagation]] substitutes Rφ into a query.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=5]]
