# Test Oracle

## In one sentence

A **test oracle** is the rule that tells a tester whether observed behavior is correct.

## Why DBMS testing makes this difficult

A crash is obvious:

    query → DBMS → crash

A logic bug can look completely normal:

    query → DBMS → plausible but wrong result

For arbitrary generated SQL, computing the expected answer independently may require implementing much of a second DBMS.

## How our papers solve it

**CODDTest**

    original query ≡ folded query

**DDLCheck**

    evolved database ≡ directly constructed database

**WriteCheck**

    concurrent execution ≡ appropriate oracle execution

None of these techniques needs to precompute every correct answer. Instead, each manufactures a relationship that correct executions should preserve.

## Related

- [[02 Logic Bugs]]
- [[04 Equivalence-Based Testing]]
- [[03 Metamorphic Testing]]
