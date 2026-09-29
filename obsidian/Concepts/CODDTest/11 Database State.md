# Database State

A **database state** is the schema and data at a particular moment.

CODDTest's equivalence is defined relative to a fixed state s:

E_s(O) = E_s(F)

## Why fixed state is essential

Suppose the auxiliary query evaluates MIN(c0) to 1.

CODDTest then substitutes 1 into the folded query.

If another transaction changes the table before the comparison, MIN(c0) might now be 0. The constant 1 would no longer necessarily represent the original expression.

Therefore the fixed-state assumption is a real correctness condition, not just mathematical notation.

Related: [[03 Metamorphic Relation]] · [[04 Constant Folding]]
