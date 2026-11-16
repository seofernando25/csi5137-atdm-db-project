# Roadmap — CSI 5137 Group 12 deliverables

Group 12: Fernando Berti Cruz Nogueira, Saatvik Paul, Haekwon Ahn.
Theme: Bug Detection — *Detecting Logic Bugs in Relational Database Systems*.
Presentation slot: **Wed 9 Dec 2026, 20:25–20:50** (25 min), per the course schedule.

## Deliverables

| # | Deliverable | Folder | Status |
|---|---|---|---|
| 1 | Report of Project 1 (literature review, 10–20 pp.) | [project1-latex/](project1-latex/) (LaTeX, 16 pp.), [project1-logic-bugs-report/](project1-logic-bugs-report/) (Markdown) | LaTeX rewrite done; guide gaps fixed; five explainer diagrams |
| 2 | Project presentation (25 min) | [project-presentation/](project-presentation/) | 3-paper deck existed; Radar section added |
| 3 | Report of Project 2 (reproduction) | [project2-reproduction/](project2-reproduction/) | Fig. 2 reproduced (SQLite 3.42.0.0, reduced budget); bug replays done |

Each folder is self-contained. The root repository still holds the runnable
sources (`repro/`, `scripts/`, `compose.yaml`).

## Course requirements (from the ATDM guides)

- **Project 1:** 3–6 recent papers; 10–20 pages, Times New Roman 11. Sections: introduction; problem definition (narrative, formal, detailed); motivation; related work; experimental study. Critical viewpoint. Acknowledge LLM use in detail.
- **Project 2:** pick one Project 1 paper; reproduce **at least one graph**; report the whole journey (including failures), the extent of success and why, and what the paper's reporting taught. Link a repository with code, data, results. Acknowledge LLM use.
- **Presentation:** 25 min. No grading rubric or deadlines appear in the supplied PDFs.

## Remaining work (ordered by value)

1. **Project 2 graph reproduction.** The declaration fixes the target: CODDTest Fig. 2 (execution time per query and completed tests vs MaxDepth), expression-only, no subqueries, SQLancer with CODDTest ([PR 1054](https://github.com/sqlancer/sqlancer/pull/1054)), SQLite 3.42.0.0, MaxDepth 1,3,…,15. The paper used 10 threads × 24 h per depth; we ran 40 s per depth: tests −88.9% (paper −89.4%), time/query ×5.78 (paper ×9.91). See [project2-reproduction/graph-reproduction/](project2-reproduction/graph-reproduction/).
2. **Render Project 1 to PDF.** The guide asks for Times New Roman 11 and 10–20 pages. Convert `report.md` (pandoc or the original PDF) and confirm the page count.
3. **Rehearse the talk** with a timer. Timing files are model estimates, not measurements.
4. **Submission links.** Add the public repository URL where the Project 2 report has a TODO.
5. **Deadlines.** Not stated in the supplied PDFs. Check the course page.

## Method

Haiku subagents did bounded work (guide summary, figure redraw, Project 2 draft).
Each output was checked against the repo evidence before commit.
