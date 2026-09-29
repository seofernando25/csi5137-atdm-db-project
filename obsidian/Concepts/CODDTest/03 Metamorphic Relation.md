# Metamorphic Relation

A **metamorphic relation** is the precise relationship expected between the original and follow-up executions.

For CODDTest:

E_s(O) = E_s(F)

where:

- E is the DBMS engine;
- s is the fixed [[11 Database State|database state]];
- O is the original query;
- F is the folded query.

If E_s(O) ≠ E_s(F), CODDTest has a bug candidate.

The relation only makes sense if the transformation itself preserves semantics. This is why fixed state, NULL semantics, and floating-point behavior matter.

Related: [[18 False Positives and Floating Point]]
