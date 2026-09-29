# Shared Concepts

These notes are used by more than one paper in the project.

## Testing foundations

- [[01 Test Oracle]]
- [[02 Logic Bugs]]
- [[03 Metamorphic Testing]]
- [[04 Equivalence-Based Testing]]
- [[05 Database State]]
- [[06 Differential Testing]]

## Test generation and debugging

- [[07 Stateful Test Generation]]
- [[08 Grammar-Based Test Generation]]
- [[09 Test Case Reduction]]
- [[10 Algorithmic Sketch]]

## Why this folder exists

The three papers use different mechanisms, but they repeatedly return to the same ideas:

1. generate executions that should obey a known relation;
2. run the DBMS;
3. compare observable behavior;
4. reduce a mismatch into a useful bug report.

Keeping these ideas here avoids redefining them separately for CODDTest, DDLCheck, and WriteCheck.
