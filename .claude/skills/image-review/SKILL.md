---
name: image-review
description: Use for ANY creation, edit, or review of figures, charts, diagrams, or graphical tables in this report — TikZ explainers, matplotlib re-plots, rendered PDF pages with images — and whenever the user asks for a figure to be critiqued, rated, or "given a visual pass". Produces or receives feedback in the format "Visual Rating: X/10 + specific visual issues + quick fixes". Also apply the drawing rules silently while creating or editing any image asset here; do not wait to be asked.
---

# Image Review — figure craft standard for this report

To draw or redraw a figure, start from the `academic-illustration` skill (kit, templates, mistake checklist); this skill rates the result.

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

### Diagram composition (fan-in / compare patterns)

These rules exist because the report's own redesign burned several review rounds learning them; they generalize:

- Exactly one decision/comparison locus per compare stage. Never repeat the decision diamond in four cards *and* again in the shared box — the diamond is a routing node, not a decoration. Cards carry their dichotomy and their observation; the shared stage carries the branch.
- Shared invariants go in ONE shared element (a bus/conduit bar, a common oracle box) — never copied into each sibling.
- Fan-in from N branches to one shared stage: use ONE orthogonal conduit (vertical drops at uniform x, one horizontal bus, a single centered arrow). Diagonal converging arrows with varied angles read as imbalance; uniform orthogonal drops read as "all feed the same oracle".
- Converging-to-shared is the report's visual motif — reuse it instead of inventing per-figure connector vocabularies.
- Parallel structures with three or more reads (e.g., method/scope → dichotomy → observation) take faint left-gutter tier labels in italic ink!60; they orient skimmers without adding in-card clutter.
- Balance by content width, not by leftover space: pills and pill-like outcomes are compact (minimum width ~2.6 cm), centered under their diamond, and the composition is centered on the figure's optical middle.

### Palette and color

- Text/axes/borders: ink `#2D2D2C`, borders `#B8B8B8`, grid `#DDDDDD` on the value axis only.
- Garnet `#8F001A` is reserved for bug/mismatch semantics — never a data category, never a frame around a neutral stage. A neutral comparison box uses a white fill and ink!60 border; the bug color appears only on the bug outcome text/pill.
- Green vs pink contrast: use forest `#1E5631` for "fine/ok" text on pale red backgrounds (≥ 4.5:1), not mid-tone cgreen.
- Primary series `#0072B2` or `#2B6CB0`; secondary series `#D55E00` or `#D9822B`; `#009E73` / `#CC79A7` only as non-text fills.
- Connectors that carry no semantic weight default to ink!60, not saturated orange; reserve orange for accent/arrow meaning.
- Shares/sequential data: single-hue blue scale `#C6DBEF`/`#6BAED6`/`#2B6CB0`. Never rainbow. Stacked bars only for genuine part-to-whole with every segment ≥ 3%.
- No red/green adjacency (CVD-hostile). No off-system hues.
- Contrast floor: any text (including 7–8 pt labels) needs ≥ 4.5:1 against its fill or the white page. White on `#D9822B` (2.9:1) or `#E69F00` (2.2:1) is a defect. Black on all fills except `#0072B2` (white OK at 5.2:1). Colored text on white needs ≥ 4.5:1 or it is `#1A1A1A`.

### Typography

- Figure labels are sans (Liberation Sans, set as the default family in `tikzstyle.tex` and `paper.mplstyle`); prose and captions stay serif; mono (Liberation Mono) only for literal code chips. Pick the role per element, never mix arbitrarily.
- Panel titles in multi-stage explainers carry a step badge (`\stepnum{n}`, blue disc, white number) in pipeline order; tier rows in the overview use `badge`. Icons come from `fontawesome5`, one per concept, in `stepblue` or ink, never decorative.
- Captions open with a bold one-line title (what the figure shows, not a claim), then source and caveat.
- Plots follow the explainers: horizontal grid replaces the y spine, no y tick marks, direct end labels instead of legends, panel letters `a`/`b` with a short title.
- Every label ≥ 7 pt; caveats and footnotes ≥ 6.5 pt.
- Counts are integers: no one-decimal fake precision (1 case in 35 ≈ 2.9 pp; print "1/35" or round to integers).
- Two-line chips: first line operand/expression, second line the muted rule (e.g., a small low-chroma "vs" at 6.5 pt). Uniform line count across siblings; center-anchored, identical fonts.
- Ship vector PDFs sized to their include width (`\columnwidth`); check the render at 100% zoom.

### Charts vs tables (hard rule)

- Counts ≤ 29, categories < 3% of a share, or exact small integers → compact booktabs table, not bars/slivers.
- Bars only for real part-to-whole with ≥ 3% segments; line charts for trends only.
- Re-plots from published figures must fit the caption template: "Re-plot of \cite[Fig. N]{...} from values read off the published figure; values are approximate." The caveat appears exactly once per figure; never as in-figure watermark text.
- Absence is not zero: if a category has no reported data (e.g., DBMSs with no confirmed bugs), caption says so or omit the category — never invent a zero row.

### Redundancy

- No repeated bold lead-ins such as "Changed: / Stays equivalent: / Compared:" — show with icons/chips and one short line.
- Hoist shared invariants into one common element (e.g., the shared oracle bar) instead of repeating them per card.
- Captions carry what the figure cannot (source, caveat, validation note); they never restate data labels or prose. If fixing a figure leaves the caption restating it, cut the caption in the same commit.

## Hard rules from the report redesign (additive, not optional)

1. **Semantic role coloring across multi-figure sets.** Bind fill colors to fixed functional roles (baseline input = blue, derivation/derivation step = grey, transformed variant = accent) and keep the mapping identical in every explainer figure.
2. **Never pierce containers with connectors.** Edges route strictly between outer card boundaries (`east` to `west`, or `south` to `north`); a path never crosses text, tables or icons inside an adjacent node.
3. **Oracle drops come only from compared artifacts.** In differential pipelines, evaluate only from the nodes whose outputs are actually compared — never from helper/construction boxes.
4. **One decision locus, truly branching.** Never an `equal?` diamond beside repeated verdict text; the diamond is a routing vertex with two orthogonal branches ending in a green pass pill and a red failure pill.
5. **Compute coordinates with `calc`.** Bus midpoints, branch label positions, aligned slots and pill columns use `($(A)!0.5!(B)$)` and `(A |- B)`/`(A -| B)`; hardcoded decimals are a defect to flag in review.
6. **Constant clearance everywhere.** ≥ 6 pt between decision diamonds and adjacent labels; equal top/bottom margins around internal dashed dividers; placeholder badges in parallel cards share identical vertical rhythm.
7. **Uniform typography in code.** Code identifiers, SQL and subscripts inside code blocks are monospace (`\ttfamily` + `\textsubscript{...}`, never math mode `$...$`); titles and prose inherit the document's primary typeface.
8. **Colored branches are single continuous orthogonal paths** with `rounded corners=3pt` and one semantic color each — never two segments joined at a mitered corner, never split-color elbows.

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

Scoring: ≤ 5 = encoding broken (contrast, semantics, illegibility); 6–7 = real defects; 7–8 = polish; 9+ = ship-ready. Name the single biggest defect first; never inflate. A figure can lose "points" for retaining redundant prose as easily as for bad color. If the rating stays below 8, the author owes another adversarial pass after fixes; aggregate the fix round instead of tackling nits one at a time.

## Anti-slop checklist (before any commit that touches figures)

1. Dead space eliminated? 2. Shared baselines across sibling cards? 3. All text ≥ 7 pt? 4. Text contrast ≥ 4.5:1? 5. Garnet reserved for bug (not frames of neutral stages)? 6. No red/green pair? 7. No white-on-amber/orange text? 8. Chart vs table rule honored? 9. Caption restates figure/prose? 10. `⇒` vs `vs` grammar consistent? 11. No duplicated decision nodes; one locus per comparison?
12. **`xelatex` exit code is 0** — the engine may still write the PDF at `! Emergency stop.` and exit 1; a "successful render" with exit≠0 means a stale PDF may be committed. Check `grep -n "^!" log`, rebuild twice, then `pdfinfo | grep Pages`, zero Overfull.
13. Build chains with `&&`, not `;` — never let a failed XeLaTeX pass silently skip rebuilds and let `pdfinfo` inspect a stale file.
14. Affected pages re-rendered to PNG and eyeballed including edges; check for clipped/crawling text and cropped frames.
15. Every data claim checked against the source paper (grep the PDF, don't assume)?

## Project context

- Report: `report/project1-latex/` — build with `xelatex -interaction=nonstopmode -halt-on-error main.tex` (run twice), then `pdfinfo main.pdf | grep Pages`; render pages with `pdftoppm -r 150 -png main.pdf /tmp/opencode/pg`. At 150–200 dpi, zoom on the smallest glyphs (e.g., subscripts in chips).
- House style: `figures/tikzstyle.tex` (panel fills `pblue`/`porange`/`pgreen`/`pgrey`/`pgarnet`, one accent per meaning) and `figures/paper.mplstyle` for matplotlib (serif, x-only grid, no top/right spines).
- Figures are included at `\columnwidth` (single-column, LeJEPA-style) unless they are wide TikZ explainers (`figure*`, `\linewidth`).
- The PDF is the submission artifact: never commit a figure change without rebuilding and re-rendering every affected page.
