# False Positives and Floating Point

A metamorphic oracle is only valid when its transformation genuinely preserves semantics.

A **false positive** occurs when the testing method reports a mismatch even though the DBMS has not violated the intended semantic property.

## Why floating point is tricky

Floating-point calculations can vary slightly because of:

- finite representation precision;
- evaluation order;
- casts and conversions;
- formatting and comparison behavior.

The CODDTest paper discusses false alarms encountered in the initial implementation, including floating-point-related cases.

## General lesson

The quality of metamorphic testing depends on the validity of the [[03 Metamorphic Relation|metamorphic relation]].

If the transformation itself changes semantics, the mismatch does not prove a DBMS bug.

## Presentation use

This is a useful limitation / validity point:

> A clever oracle also needs carefully defined conditions under which the equivalence is valid.

Paper: [[PDFs/CODDTest_SIGMOD2025.pdf#page=13]]
