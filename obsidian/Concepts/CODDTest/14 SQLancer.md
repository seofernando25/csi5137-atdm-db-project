# SQLancer

**SQLancer** is an open-source framework for automated DBMS testing.

Project: https://github.com/sqlancer/sqlancer

## What SQLancer provides

- generation of random database states;
- generation of SQL statements and expressions;
- DBMS-specific syntax and adapters;
- execution of different test oracles;
- logging and reduction infrastructure.

CODDTest is implemented using SQLancer.

## Important distinction

SQLancer is the **testing framework**.

CODDTest is the **new oracle / testing technique** implemented in that ecosystem.

This distinction matters in the presentation because random SQL generation is not itself the paper's main contribution. The contribution is the constant-optimization-driven oracle.

Related: [[15 Abstract Syntax Tree (AST)]]
