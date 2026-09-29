# Existing Test Oracles

CODDTest compares against several earlier DBMS-testing approaches.

Use this page as the index.

| Technique | Core oracle idea |
|---|---|
| [[16A TLP - Ternary Logic Partitioning|TLP]] | Partition by p, NOT p, and p IS NULL |
| [[16B NoREC - No Rewriting Required|NoREC]] | Compare equivalent predicate computation through a rewritten form |
| [[16C PQS - Pivoted Query Synthesis|PQS]] | Generate a query that should contain a known pivot row |
| [[16D DQE - Differential Query Execution|DQE]] | Compare predicate behavior across SQL statement contexts |

## Why this matters

All four techniques address the same high-level [[01 Test Oracle|oracle problem]].

CODDTest's distinctive transformation is:

> evaluate an expression, then substitute its result.

That lets it test cases that do not fit naturally into the other oracles.

## Continue

Read the four child notes, then return to [[17 How CODDTest Fits Together]].

Paper comparison section: [[PDFs/CODDTest_SIGMOD2025.pdf#page=15]]
