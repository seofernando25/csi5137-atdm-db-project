# Foreign-Key Dependencies and Circularity

## In one sentence

Foreign keys impose creation-order dependencies that DDLCheck must respect when synthesizing the direct schema.

## Simple dependency

If:

    orders.customer_id
        REFERENCES customers.id

then customers must normally exist before the foreign key in orders can be created.

Conceptually:

    customers
        ↓
      orders

## Why synthesis becomes harder

seq_syn tries to construct the final schema directly.

It therefore needs to order CREATE statements according to foreign-key dependencies.

## Circular dependency

Sometimes:

    table A → table B
       ↑         ↓
       └─────────┘

No single table can be fully created first with all foreign keys already present.

DDLCheck handles such cases by:

1. creating tables first;
2. adding certain foreign-key constraints afterward using ALTER TABLE.

## Why this matters for our project

Our reproduced MySQL #114904 bug itself involves:

- a foreign key;
- a referenced table rename;
- stale metadata after schema evolution.

See [[24 MySQL 114904 Walkthrough]].
