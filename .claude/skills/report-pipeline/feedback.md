# User feedback log, turned into rules

Newest first. Each entry gives the steer, the rule it produced, and where that rule is
enforced.

## 2026-11-18: "Slogan captions, 'Back to the shop', text too small"

- **Steer:**
  - "Four oracles, four real bugs." reads as AI slop.
  - "Back to the shop." is not something a person writes.
  - Figure 2's labels are too small to read.
  - Re-review the whole paper for slop. Over-compressed prose, where sentences lose their
    connections, is itself slop (Every, "AI & I", 2026-11-17).
- **Rules:**
  - Caption titles describe what is shown, as a noun phrase or plain sentence. No slogans,
    parallel punchlines or verdicts.
  - No cute openers ("Picture", "Imagine", "Back to") and no slang metaphors ("trick",
    "home turf", "pile of").
  - Each sentence states how it connects to the previous one, using "because", "so",
    "however" or "which". Keep articles and subjects; no fragment chains.
  - Cut length by removing repeated content, never by compressing sentences.
  - Draw figures at their final width so that labels print at 7 pt or more. Never shrink a
    figure to fit.
  - No labelled "Takeaway" boxes.
- **Enforced in:** `SKILL.md` prose gate; `check_report.sh` (banned openers and metaphors,
  fragment-sentence ratio of 8% or less, slogan-caption heuristic).

## 2026-11-18: "Shrink to 10 pages, more wow figures, less prose"

- **Steer:**
  - Fit the report on 10 pages.
  - Prose-only pages are boring for the professor; add small diagrams in the style of
    graphics.wsj.com.
  - Rework big explainers that take a full page "with no purpose".
- **Rules:**
  - Target 10 pages, never below the guide's minimum.
  - Lead page 1 with one striking figure that shows real data (here, one real bug per paper).
  - Replace per-method explainer pages with small multiples.
  - Each display must earn its space. Prefer compact charts (tile grid, unit chart, dumbbell,
    index chart, log dot plot) over tables when the shape is the message.
  - Cut prose by about 40% by moving comparisons into displays.
- **Enforced in:** `SKILL.md` (display rules, page target), `check_report.sh` (page bounds).

## 2026-11-18: "Work on main, commit and push"

- **Steer:** Do not create branches for this repository. Commit directly on `main` and push
  when the pipeline completes.
- **Rule:** Stage COMPLETE ends with a commit on `main` followed by `git push origin main`.
- **Enforced in:** `SKILL.md` (COMPLETE row).

## 2026-11-18: "Improve the whole deliverable"

- **Steer:**
  - The reader is a visual learner.
  - Do not lose the professor over 10 to 20 pages.
  - No plain, boring read, and none of the AI tells of old-school academic prose.
  - Use your own judgment, and do not stop before every gate passes.
- **Rules:**
  - Section openers carry the takeaway. Each main section ends with at most one takeaway box.
  - Cross-paper comparisons are shown as matrices and charts, not paragraphs.
  - Every claim about evidence gets a visible verdict symbol.
  - The prose gate bans template phrases.
  - The pipeline runs to stage COMPLETE without asking questions.
- **Enforced in:** `SKILL.md` (prose gate, display rules), `check_report.sh` (banned
  patterns).

## Earlier steers (taken from the commit history)

- **"Tone down LLM disclosure"** (2733395): the disclosure is factual and detailed, with no
  apology and no self-deprecation. It lists the tool, the tasks it did, and what the authors
  verified.
- **"Student-voice rewrite"** (db488bc, 195a1e0): plain words, abbreviations defined, fewer
  numbers in prose.
- **"Remove reproduction material"** (cb7b238): Project 1 reviews the papers and does not
  report our MySQL replays.
- **"No in-figure provenance notes"** (8b4ffad): the caption carries the source and caveat,
  once per figure.
- **"Tables for small counts"** (fe89e8e): exact small integers go in a table. A chart is used
  only when the shape is the message.
