# Logic Bugs

A **logic bug** occurs when the DBMS successfully executes a query but produces an incorrect result.

Contrast:

- crash bug → obvious error or crash;
- logic bug → plausible-looking but wrong answer.

Logic bugs are difficult because there may be no exception, warning, or visible failure.

## CODDTest's strategy

CODDTest creates two queries that should be equivalent.

If:

result(O) ≠ result(F)

then at least one execution is inconsistent, even though both may have completed normally.

The paper reports 24 previously unknown logic bugs.

Related: [[01 Test Oracle]] · [[03 Metamorphic Relation]]
