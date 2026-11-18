# Project 1 report: LaTeX source

- `main.pdf` is the submission PDF: 15 pages, two columns, 11 pt Liberation Serif (the metric twin of Times New Roman).
- Build and check: `bash .claude/skills/report-pipeline/check_report.sh` from the repository root. It runs XeLaTeX twice and gates the page count, fonts, references, labels, the required sections and the prose style. The full procedure is the `report-pipeline` skill.
- Sources:
  - `sec_a.tex`: Sections 1 to 4.
  - `sec_b.tex`: Sections 5 to 7.
  - `disclosure.tex`: the LLM-use statement.
  - `refs.tex`: the references.
  - `FACTS.md`: maps every number in the report to its source table or section in the four papers.
- `figures/`:
  - TikZ explainers (`fig_*.tex`, built with XeLaTeX and `tikzstyle.tex`).
  - Data charts, built by `python3 figures/make_data_figures.py`:
    - `fig_depth`: CODDTest depth sweep;
    - `fig4`: CODDTest efficiency;
    - `fig5`: Radar ablation;
    - `fig_homeset`: capability studies;
    - `fig_funnel`: reporting stages.
