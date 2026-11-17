---
name: image-review
description: Use for ANY creation, edit, or review of figures, charts, diagrams, or graphical tables in this report — TikZ explainers, matplotlib re-plots, rendered PDF pages with images — and whenever the user asks for a figure to be critiqued, rated, or "given a visual pass". Produces or receives feedback in the format "Visual Rating: X/10 + specific visual issues + quick fixes". Also apply the drawing rules silently while creating or editing any image asset here; do not wait to be asked.
---

# Image Review — figure craft standard for this report

Figures in this report are the submission artifact, not decoration. A figure that is illegible, misleading, or redundant with prose damages the report more than a missing figure. Apply the rules below while drawing, and the rated format when reviewing.

## When this fires

- Creating or editing `figures/fig_*.tex` (TikZ explainers) or `figures/make_data_figures.py` (matplotlib re-plots)
- Replacing a figure with a table (and vice versa)
- Rebuilding and re-rendering pages where figures appear
- Any "critique / rate / look at / is this any good" request about a figure, chart, diagram, or report page containing one

## Drawing rules

### Layout and grid

- Snap siblings to a shared grid: card titles, chips, divider rules and icons sit on exact common horizontal baselines across every card. Left-align related elements; never float.
- Kill dead space. Cards and figure panels size to their content; 25–30% padding bloat is a defect, not "breathing room". Aim ≤ 2.7 in for simple single-panel plots.
- One visual job per element. If a graphic encodes a fact the prose or the caption also states, delete one encoding (the report once triple-encoded "96.9% use one initial table" across prose, bar label, and caption).
- Arrow/comparison grammar is consistent everywhere: `⇒` = "is folded/simplified to" (directional transformation only); `vs` = "these two executions are being compared". Do not mix without that meaning.

### Palette and color

House palette (five re-plots and all TikZ figures):

- Text/axes/borders: ink `#2D2D2C`, borders `#B8B8B8`, grid `#DDDDDD` on the value axis only.
- Garnet `#8F001A` is reserved for bug/mismatch semantics. Never use it for data categories, never put anything maroon near it.
- Primary series `#0072B2` or `#2B6CB0`; secondary series `#D55E00` or `#D9822B`; `#009E73` / `#CC79A7` only as non-text fills.
- Shares/sequential data: single-hue blue scale `#C6DBEF`/`#6BAED6`/`#2B6CB0`. Never rainbow. Stacked bars only for genuine part-to-whole with every segment ≥ 3%.
- No red/green adjacency (CVD-hostile). No off-system hues.
- Contrast floor: any text (including 7–8 pt labels) needs ≥ 4.5:1 against its fill or the white page. White on `#D9822B` (2.9:1) or `#E69F00` (2.2:1) is a defect. Black on all fills except `#0072B2` (white OK at 5.2:1). Colored text on white needs ≥ 4.5:1 or it is `#1A1A1A`.

### Typography

- Serif (Liberation Serif) for prose, titles and captions; mono (Liberation Mono) only for literal code chips; never mix heavy serif + italic serif + thin mono arbitrarily in the same figure — pick the role per element.
- Every label ≥ 7 pt; caveats and footnotes ≥ 6.5 pt.
- Counts are integers: no one-decimal fake precision (1 case in 35 ≈ 2.9 pp; print "1/35" or round to integers).
- Ship vector PDFs sized to their include width (`\columnwidth`); check the render at 100% zoom.

### Charts vs tables (hard rule)

- Counts ≤ 29, categories < 3% of a share, or exact small integers → compact booktabs table, not bars/slivers.
- Bars only for real part-to-whole with ≥ 3% segments; line charts for trends only.
- Re-plots from published figures must fit the caption template: "Re-plot of \cite[Fig. N]{...} from values read off the published figure; values are approximate." The caveat appears exactly once per figure; never as in-figure watermark text.
- Absence is not zero: if a category has no reported data (e.g., DBMSs with no confirmed bugs), caption says so or omit the category — never invent a zero row.

### Redundancy

- No repeated bold lead-ins such as "Changed: / Stays equivalent: / Compared:" — show with icons/chips and one short line.
- Hoist shared invariants into one common element (e.g., the shared oracle bar) instead of repeating them per card.
- Captions carry what the figure cannot (source, caveat, validation note); they never restate data labels or prose.

## Review output format

When asked to review or rate a figure, answer in this exact shape:

```
Visual Rating: X / 10

<one-line verdict>

### Specific Visual Issues
- <Dead Space> ...
- <Alignment / Grid> ...
- <Typography / Contrast> ...
- <Color / Palette> ...
- <Information Design> ...

### Quick Fixes
1. ...
```

Scoring: ≤ 5 = encoding broken (contrast, semantics, illegibility); 6–7 = real defects; 7–8 = polish; 9+ = ship-ready. Name the single biggest defect first; never inflate. A figure can lose "points" for retaining redundant prose as easily as for bad color.

## Anti-slop checklist (before any commit that touches figures)

1. Dead space eliminated? 2. Shared baselines across sibling cards? 3. All text ≥ 7 pt? 4. Text contrast ≥ 4.5:1? 5. Garnet reserved for bug? 6. No red/green pair? 7. No white-on-amber/orange text? 8. Chart vs table rule honored? 9. Caption restates figure/prose? 10. `⇒` vs `vs` grammar consistent? 11. `xelatex` twice, pdfinfo page count acceptable, zero Overfull? 12. Every data claim checked against the source paper (grep the PDF, don't assume)? 13. Affected pages re-rendered to PNG and eyeballed?

## Project context

- Report: `report/project1-latex/` — build with `xelatex -interaction=nonstopmode -halt-on-error main.tex` (run twice), then `pdfinfo main.pdf | grep Pages`; render pages with `pdftoppm -r 110 -png main.pdf /tmp/opencode/pg`.
- House style: `figures/tikzstyle.tex` (panel fills `pblue`/`porange`/`pgreen`/`pgrey`/`pgarnet`, one accent per meaning) and `figures/paper.mplstyle` for matplotlib (serif, x-only grid, no top/right spines).
- Figures are included at `\columnwidth` (single-column, LeJEPA-style) unless they are wide TikZ explainers (`figure*`, `\linewidth`).
- The PDF is the submission artifact: never commit a figure change without rebuilding and re-rendering every affected page.
