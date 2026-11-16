# Recreated figures

`make_figures.py` regenerates `fig1.png` to `fig5.png` (200 dpi) from values
read off the published papers' figures. The original images (from the submitted PDF, not kept here)
are the sources for the read-off values.

Run: `python make_figures.py` (requires matplotlib).

Numbers come from two sources:

- **Printed in the paper's figure or text (exact):**
  - Fig 1: category counts and percentages, e.g. 96.9%, 12.1%, 84.9%, 12.5%, 56.2%, 45.3%.
  - Fig 4: all bug-revealing statement counts per DBMS and in total (29 bugs).
  - Fig 5: final unique-bug counts (Radar 19, Radar_rand 12).
- **Read off the figure (approximate):**
  - Fig 1: segment widths not printed as a percentage (for example the 2 and 4 segments, and the small tail segments).
  - Fig 2: all curve points (execution time and completed tests vs. MaxDepth).
  - Fig 3: all curve points (unique query plans vs. MaxDepth).
  - Fig 5: all curve points (unique bugs vs. time).

Caveats:

- Fig 2 text facts (9.91x execution-time rise, 89.4% fewer completed tests) are
  not reproduced exactly. The read-off curves give about 11x and about 90%.
- Fig 1 row (b) tail labels ("5", "50+") are partly illegible in the original;
  the "50+" label is a best reading.
- Curve values carry visual reading error. Do not cite them as exact.
