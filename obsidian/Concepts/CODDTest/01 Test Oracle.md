# Test Oracle

A **test oracle** is the mechanism that decides whether a program's output is correct.

A crash is easy to recognize. A DBMS logic bug is harder because the engine can return a plausible-looking answer with no warning.

For arbitrary generated SQL, independently computing the correct result can be almost as difficult as implementing another SQL engine.

CODDTest avoids needing a known answer. It creates a second query that should be semantically equivalent and compares the two results.

> Presentation sentence: The hard part is not generating SQL; it is knowing whether the DBMS's answer is correct.

Next: [[02 Metamorphic Testing]]  
Related: [[12 Logic Bugs]]
