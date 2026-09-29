# Test Case Reduction

## In one sentence

**Test case reduction** removes unnecessary parts of a failing test while preserving the failure.

## Why generated DBMS bugs need it

A random tester may discover a failure after:

- many DDL statements;
- many inserts/updates;
- a complex final query.

That is hard for a developer to understand.

Reduction tries:

    large failing case
          ↓
    remove something
          ↓
    still fails?
      yes → keep it removed
      no  → put it back

## DDLCheck

DDLCheck reduces both the generated DDL history and the SQL statements needed to reveal the bug.

## Related idea

This resembles delta debugging: repeatedly simplify while preserving the interesting behavior.
