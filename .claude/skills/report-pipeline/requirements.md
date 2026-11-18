# Project 1 requirements (course guide, CSI 5137 ATDM)

Source: the ATDM project guides, as summarized in `report/ROADMAP.md`. The report follows
the section order the guide asks for. Each item maps to where the report meets it. Stage 7 of
the pipeline ticks every row against the rebuilt PDF.

| ID | Requirement | Where met (label) |
|---|---|---|
| R1 | 3 to 6 recent papers on one theme | Four 2024 and 2025 papers (CODDTest, DDLCheck, WriteCheck, Radar); `sec:intro` |
| R2 | 10 to 20 pages | gate: page count |
| R3 | Times New Roman, 11 pt | Liberation Serif (metric twin), `11pt` class option; gate: fonts |
| R4 | Introduction | `sec:intro` |
| R5 | Problem definition: high-level (narrative) description | `sec:problem`, first subsection |
| R6 | Problem definition: formal definition (input, output, objective) | Given/Sought panel, `sec:formal` |
| R7 | Problem definition: detailed discussion of the formal definition | `sec:detailed` with the instantiation table |
| R8 | Pseudoalgorithm | `alg:oracle` |
| R9 | Motivation: running example | `sec:motivation`, running example |
| R10 | Motivation: importance and who benefits; what makes the problem hard | `sec:motivation` |
| R11 | Motivation: limitations of existing work and whether it can be extended | `sec:motivation`, gaps and extension |
| R12 | Related work: papers grouped and compared, with a comparison table | `sec:related`, capability matrix |
| R13 | Experimental study: setup and hardware | `sec:experiments`, setup |
| R14 | Experimental study: datasets and workloads | `sec:experiments`, datasets |
| R15 | Experimental study: metrics and methodology | `sec:experiments`, metrics |
| R16 | Experimental study: results per paper | one subsection per paper |
| R17 | Critical assessment: are the experiments sufficient for the claims? | evidence verdicts per paper and the cross-study scorecard |
| R18 | Critical viewpoint throughout, not a summary | rubric item 3 in `SKILL.md` |
| R19 | Conclusions and research directions | `sec:conclusions` |
| R20 | References | `refs.tex` |
| R21 | Detailed acknowledgment of LLM use | `sec:llm` |

Course boundaries (from `AGENTS.md`): do not present the results as evidence that MySQL is
buggier than other DBMSs. Project 1 is a literature review. Reproduction material belongs to
Project 2.
