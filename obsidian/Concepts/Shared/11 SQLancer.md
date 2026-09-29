# SQLancer

## In one sentence

**SQLancer** is an open-source framework for automated DBMS testing.

Project: https://github.com/sqlancer/sqlancer

## What it provides

SQLancer supplies infrastructure for:

- generating random database states;
- generating SQL statements and expressions;
- connecting to multiple DBMSs;
- running testing oracles;
- logging failures;
- reducing and reproducing bugs.

## Why it is shared

Both CODDTest and WriteCheck are implemented by extending SQLancer.

The research contribution in those papers is **not SQLancer itself**. SQLancer is the framework that lets the authors focus on the new oracle.

## Paper-specific use

**CODDTest:** generates expressions, queries, and folded-query transformations.

**WriteCheck:** generates initial databases, SQL statements, transaction groups, and transaction test cases.

## Related

- [[07 Stateful Test Generation]]
- [[08 Grammar-Based Test Generation]]
- [[01 Test Oracle]]
