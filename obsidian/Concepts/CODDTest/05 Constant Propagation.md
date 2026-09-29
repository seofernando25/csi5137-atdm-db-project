# Constant Propagation

**Constant propagation** substitutes a known value for the expression it represents.

Suppose folding establishes:

φ = SELECT MIN(c0) FROM t0  
Rφ = 1

Then a predicate using the subquery can be transformed into an equivalent predicate using the constant 1.

## Folding vs propagation

- folding = compute the value;
- propagation = substitute the value.

Together, these two compiler-inspired operations generate CODDTest's follow-up query.

Related: [[04 Constant Folding]] · [[06 Original Auxiliary and Folded Queries]]
