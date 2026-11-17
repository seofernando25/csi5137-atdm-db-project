# Project 1 report: LaTeX source

- `main.pdf` is the submission PDF (13 pages, two columns, 11 pt; plots at column width, explainers and wide tables full width).
- Build: `xelatex main.tex` twice. Fonts are Liberation Serif/Sans/Mono, the metric twins of Times New Roman/Arial/Courier New; the names are set at the top of `main.tex`.
- `sec_a.tex` holds sections 1 to 4, `sec_b.tex` sections 5 to 7 and the LLM disclosure, `refs.tex` the references.
- `figures/`: TikZ explainers (sans labels, step badges, `fontawesome5` icons) (`fig_*.tex`, built with XeLaTeX and `tikzstyle.tex`) and data plots (`make_data_figures.py`, `paper.mplstyle`).
