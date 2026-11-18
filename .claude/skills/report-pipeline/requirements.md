# Project 1 requirements (course guide, CSI 5137 ATDM)

Source: "ATDM_Guide_for_Project_Report 1 2026.pdf" (Verena Kantere), in the course-content
zip in ~/Downloads. That guide is authoritative; this file maps each item to where the report
meets it. Stage 7 of the pipeline ticks every row against the rebuilt PDF. The course PDFs
are not committed.

| ID | Guide requirement | Where met |
|---|---|---|
| R1 | 3 to 6 recent papers on one research theme (PVLDB, SIGMOD, ...) | four PVLDB and SIGMOD papers, 2024 to 2025 |
| R2 | Include some of the papers' references as needed | seven background oracles, `refs.tex`, Fig. `fig:lineage` |
| R3 | Critical point of view; inventive viewpoint | verdicts, the three reporting patterns, scorecard |
| R4 | Qualitative and quantitative results; compare the works | `tab:coverage`; `tab:fresh`, `fig:homeset`, `fig:units`, `fig:triage` |
| R5 | 10 to 20 pages, Times New Roman 11 | gate: pages; 11 pt Liberation Serif (metric twin; TNR not installed here) |
| R6 | If LLMs are used, acknowledge them and describe in detail how | `sec:llm`: tool, period, workflow, per-task table with checks |
| R7 | Introduction gives the context, the broad area of interest | first paragraph of `sec:intro` |
| R8 | Problem stated narratively at a high level, emphasizing intuition | `sec:problem`, high-level description (running example) |
| R9 | Problem stated formally: definitions, given and sought, a pseudoalgorithm | `sec:formal`, Given/Find box, `alg:oracle` |
| R10 | The formal definition described in detail, narratively | `sec:detailed` |
| R11 | Motivation: interest to many communities, benefit if solved | motivation, "why it matters" |
| R12 | Motivation: hard to solve, with explicit challenges | challenges C1 to C4 |
| R13 | Motivation: deficiencies of existing work, connected to the challenges | limitations subsection, mapped to C1 to C4 |
| R14 | Motivation: whether existing work is adaptable or extendable | "can it be extended" paragraph |
| R15 | A motivating example, ideally a running example that shows the challenges and deficiencies | `Product` table in Sections 2.1, 2.4 and 3.1 |
| R16 | Related work in groups, each with a brief description and essential contribution | `sec:related`, three groups plus earlier methods |
| R17 | State the limitations of each work or group | one limitation sentence per group |
| R18 | Homogeneous citation style; never start a sentence with [n] | names followed by [n] throughout |
| R19 | Experimental setup: machines, software, tuning | `tab:glance`, setup paragraph |
| R20 | Datasets: why appropriate; synthetic construction described; synthetic-only use motivated; roles of real and synthetic data | datasets paragraphs |
| R21 | Metrics, with unusual ones motivated | metrics paragraph (plans, schema structures, coverage) |
| R22 | Methodology: series of experiments, their purpose and procedure, default parameters, whether they are sufficient | series sentence per paper, `tab:glance`, verdicts |
| R23 | Graphs from the papers: readable, every axis labelled, described narratively, non-intuitive parts explained | figures; gate plus visual review |
| R24 | A closing paragraph of conclusions after the experiments | "Conclusions of the experimental study" |

Course boundaries (from `AGENTS.md`): do not present results as evidence that one DBMS is
buggier than another. Project 1 is a literature review; reproduction work belongs to
Project 2.
