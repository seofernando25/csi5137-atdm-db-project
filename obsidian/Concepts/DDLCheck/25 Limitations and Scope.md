# DDLCheck Limitations and Scope

## In one sentence

DDLCheck is powerful because it defines a practical equivalence oracle, but that oracle and its generators deliberately cover only part of the full SQL/schema space.

## Unsupported or avoided SQL behavior

The paper excludes SQL features that make deterministic comparison unreliable, including:

- nondeterministic functions;
- time-related functions;
- ambiguous queries that can legitimately yield different results across executions.

## Test-space limitation

The number of possible schemas and DDL histories is enormous.

DDLCheck cannot enumerate them all, so it relies on:

- randomized generation;
- grammar restrictions;
- stateful validity checks;
- DSTG-based diversity filtering.

Coverage is therefore broad but not exhaustive.

## Equivalence approximation

DDLCheck uses a practical definition of table-structure equivalence.

For its sequence-selection optimization, some incidental differences such as column ordering can be ignored when a valid structural mapping exists.

That improves exploration efficiency but is a testing abstraction, not a universal proof of schema equivalence.

## DBMS-specific engineering

Different DBMSs expose schema information through different catalogs and support different DDL grammars/options.

Supporting another DBMS therefore requires engineering work.

## Presentation takeaway

> DDLCheck trades exhaustive formal equivalence for a practical oracle that can explore real DBMS schema-evolution behavior at scale.
