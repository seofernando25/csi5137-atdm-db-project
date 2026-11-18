---
name: report-pipeline
description: Staged improvement pipeline for the Project 1 LaTeX report (report/project1-latex). Use whenever the report's prose, structure, figures or tables are rewritten or reviewed, when the user asks to "improve the paper", "run the pipeline" or "check the deliverable", and before committing a rebuilt main.pdf. Ends only at stage COMPLETE, when every gate passes.
---

# Report pipeline

The report is graded against the course guide (`requirements.md`) and read by one professor.
The goal is a full score on the guide and a paper a visual reader can skim in five minutes and
read in thirty. The pipeline runs in stages. Each stage has an exit gate. Do not start a stage
before the previous gate passes. A user steer (`feedback.md`) can reopen any stage.

Related skills: `academic-illustration` (draw figures), `image-review` (rate figures).

## Stages

| # | Stage | Output | Exit gate |
|---|---|---|---|
| 0 | **Intake** | `requirements.md` up to date | Every guide item has an ID (R1...) and a target section |
| 1 | **Audit** | List of defects in the current PDF | Each defect tagged: requirement gap, factual error, broken reference, figure defect, prose defect |
| 2 | **Blueprint** | Story, section openers, display list | One display per idea; no two displays carry the same fact; section takeaways read as a summary of the paper |
| 3 | **Facts** | `report/project1-latex/FACTS.md` | Every number in the report has a source (paper, table or figure, page). Re-derive arithmetic |
| 4 | **Displays** | Figures and tables | `image-review` rating of 8/10 or higher for each new or changed figure, checked on the rendered page |
| 5 | **Prose** | Rewritten `sec_*.tex` | The prose gate in this file passes on a full read |
| 6 | **Gate** | `check_report.sh` output | Zero FAIL lines |
| 7 | **Review** | Adversarial read as the grader | No open item in the rubric below; fixes go back to stage 4 or 5 |
| — | **COMPLETE** | Commit on `main` (no branches) with the rebuilt PDF, docs refreshed, then `git push origin main` | Stages 0 to 7 all passed on the same build |

Run the gate from the repository root:

```sh
bash .claude/skills/report-pipeline/check_report.sh
```

It rebuilds the PDF with XeLaTeX and checks the following:

- page count (10 to 20) and 11 pt Times-metric fonts;
- undefined or duplicate labels and unused labels;
- citations that are never used;
- the required section labels and the LLM disclosure;
- floats that the text never references;
- overfull boxes;
- banned words and AI-tell patterns.

## Rubric for stage 7 (grade as the professor)

Course guide items first (see `requirements.md`), then quality, adapted from the
PaperOrchestra literature-review and overall-quality rubrics (arXiv:2604.05018, App. D):

1. **Motivation.** Problem, why it matters, and the gap are clear by the end of page 2.
2. **Coverage and synthesis.** Papers are grouped by idea, not listed one after another. Each
   comparison says what differs and why it matters.
3. **Critical viewpoint.** Each paper's claims are tested against its own evidence:
   - what is supported, what is directional only, and what is not shown;
   - each verdict carries its reason (sample size, single run, the bug set chosen, the
     baseline setup).
4. **Logical flow.** Section openers, read alone, tell the story.
5. **Evidence integration.** Every figure and table is referenced in the text, sits near its
   first reference, and adds something the prose does not.
6. **Clarity and style.** No filler, no repetition, a consistent term for each concept, and
   abbreviations defined at first use.

## Prose gate (stage 5)

Write like a careful graduate student explaining to a smart reader, not like a template.

- **Open each section with its takeaway.** The first sentence states the point. The rest
  supports it.
- **Vary the rhythm.** Mix short and long sentences. Avoid runs of three or more sentences of
  about the same length, and avoid long runs of subject-verb-object fragments.
- **Be concrete.** Use one real example, query, table or number in place of three abstract
  nouns. Name the bug ID or the table.
- **Limit questions.** Use at most one rhetorical question per section, and only when the next
  sentence answers it.
- **AI tells to remove on sight:**
  - repeated "X, not Y" or "rather than" contrasts (at most one per page);
  - lists of three adjectives;
  - "In summary", "Overall", "Moreover", "Furthermore", "Notably", "Importantly";
  - "plays a crucial role", "landscape", "delve", "leverage", "underscore", "highlight",
    "robust", "seamless", "comprehensive", "novel";
  - colon-led reveals in every paragraph;
  - closing sentences that restate the paragraph;
  - hedges stacked on hedges.
- **Bold run-in heads** (`\textbf{...}`) only for parallel items the reader will scan, such as
  the four evidence verdicts or the open questions. Never for emphasis inside a sentence.
- **Keep numbers in figures and tables.** Prose cites a number only when the argument turns on
  it, and gives its basis (N, run length, runs).
- **Keep the voice honest.** The authors reviewed published work. Every measurement is the
  original authors'. The formal model, the matrices and the verdicts are ours, and the text
  says so once.

## Display rules (stage 4)

- Page target: 10 pages. The guide allows 10 to 20, so never go below 10. At the target, the
  last page should hold more than the references.
- Style:
  - editorial graphics in the style of graphics.wsj.com;
  - thin rules and direct labels;
  - a one-line finding as the caption title ("Fewer tests, far more plans");
  - real data or a real bug before an abstract box diagram.
- Chart forms: small multiples, unit charts (one square per item), tile grids, dumbbells for
  with/without pairs, index charts on a log scale for sweeps, and lollipops on a log scale for
  ratios.

- Every display must do one of three jobs: explain a mechanism (TikZ explainer), compare
  across papers (matrix or chart), or hold exact lookup values (table). If it does none of
  these, cut it.
- When a set of numbers forms a shape (a funnel, a share, a trade-off), use a chart. When the
  reader needs a few exact values, use a table.
- Cross-paper displays use one paper order everywhere: CODDTest, DDLCheck, Radar,
  WriteCheck.
- Color by role, not by paper. The reviewed tool is blue `#0072B2` and baselines are grey
  `#8A8A8A`. Per-paper colors would clash with the explainers' blue-baseline/orange-variant
  grammar.
- Use symbols for verdicts and coverage: ● (yes), ◐ (partial or conditional), ○ (no), each
  with a legend in the caption.
- White text on a colored chip needs a dark fill: `vartext` `#A84800`, not `corange`.
- Callout boxes (`takeaway`) are rationed: at most one per main section, two lines or fewer,
  stating a finding rather than a slogan.

## Build

```sh
cd report/project1-latex
python3 figures/make_data_figures.py                       # matplotlib charts
for f in figures/fig_*.tex; do (cd figures && xelatex -interaction=nonstopmode -halt-on-error "$(basename "$f")" >/dev/null) || echo "FAIL $f"; done
xelatex -interaction=nonstopmode -halt-on-error main.tex && xelatex -interaction=nonstopmode -halt-on-error main.tex
```

## Lessons

These came out of earlier passes. Add a lesson each time the user corrects the work, in
`feedback.md`, and turn it into a rule here or in the gate script.

- Re-derive the denominator of every percentage. WriteCheck's Fig. 2 shares are over its 32
  WSS violations, with rows per table and statements per transaction, not over the 35 critical
  bugs. 96.9% = 31/32 gives it away.
- When a paper reports the same number for two different sets, check both definitions.
  WriteCheck has two different sets of 29 bugs: 29 of its 32 WSS violations trigger
  deterministically, and its tool-comparison set also has 29 bugs, 13 found by WriteCheck and
  16 by DT², Troc and TxCheck.
- When a figure and a chart share a `\label`, LaTeX only warns, and the reference silently
  points to the wrong float. The gate fails on duplicate labels.
- A capability study run on a paper's own confirmed bugs scores that tool 100% by
  construction. Say so wherever such a study is compared.
- Check table and figure numbers against the paper as well as the values. The earlier draft
  cited Radar's "Tables 4 and 5", but the comparisons are its Tables 5 and 6.
- Layout traps found in this pass:
  - A two-sided `article` defaults to `\flushbottom`, which stretches the gaps between
    paragraphs. `main.tex` sets `\raggedbottom`.
  - `\part` is a sectioning command, so a macro must not be named `\part`.
  - TikZ macros used inside captions must be defined with `\DeclareRobustCommand`.
  - A `\paragraph{}` heading directly before a tabular sets the table inline, and the table
    overflows the column.
- A column float that comes after a page with a full-width figure needs to fit in the space
  left below that figure. If it does not fit, it drifts two pages away. Keep column tables
  short (one line per row), or move their source earlier.
