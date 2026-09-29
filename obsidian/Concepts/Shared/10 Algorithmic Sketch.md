# Algorithmic Sketch

## In one sentence

An **algorithmic sketch** is a high-level pseudocode description that exposes the important control flow without every implementation detail.

## How to read one

Instead of memorizing line numbers, ask:

1. What is the input?
2. What state is maintained?
3. What decision points exist?
4. What output is produced?
5. What condition reports a bug?

## CODDTest

Its main sketch becomes:

    generate φ
    evaluate φ
    build O and F
    compare

## DDLCheck

Its algorithms separately cover:

- dynamic DDL generation;
- direct schema synthesis;
- bug detection;
- translation into schema-transition graphs.

## Presentation use

Explain what an algorithm accomplishes before discussing pseudocode details. Most audience members need the data flow, not the line numbers.
