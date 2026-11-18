# User feedback log, turned into rules

Newest first. Each entry gives the steer, the rule it produced, and where that rule is
enforced.

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
