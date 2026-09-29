# Test Oracle

## In one sentence

A **test oracle** is the rule that tells us whether a program's output is correct.

## Tiny example

A crash gives us an easy oracle:

    query → DBMS → crash

A logic bug is harder:

    query → DBMS → 42

The result looks normal. How do we know 42 is wrong?

## Why CODDTest cares

For arbitrary generated SQL, computing the correct result independently can be almost as hard as implementing another SQL engine.

CODDTest avoids that problem by generating a second query that **should mean the same thing** as the first one.

Instead of asking:

> Is this result correct?

CODDTest asks:

> Do these two equivalent queries agree?

That makes CODDTest a [[02 Metamorphic Testing|metamorphic-testing]] oracle.

## Don't confuse it with

A **query optimizer** decides how to execute SQL efficiently.

A **test oracle** decides whether observed behavior is correct.

## Related

- [[02 Metamorphic Testing]]
- [[12 Logic Bugs]]
- [[17 How CODDTest Fits Together]]
