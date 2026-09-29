# CSI 5137 / ATDM — Presentation v2

**Testing databases without an answer key**  
Advanced Topics in Databases and Data Management, University of Ottawa.

## Present this version

- `CSI5137_ATDM_visual_deck_v2.pptx`: editable PowerPoint, 32 main slides + 6 backups. Every slide has embedded speaker notes.
- `CSI5137_ATDM_visual_deck_v2.pdf`: fixed-layout preview of all 38 slides.
- `speaker_script.md`: spoken script with explicit show, look, gesture, move, pace, pause and advance cues.
- `cue_sheet.md`: shorter rehearsal prompts.
- `timing.csv` and `timing_summary.json`: reproducible word counts and modeled checkpoints.
- `source/content.py` and `source/build_deck.py`: editable content and deterministic deck-building logic.

The main route ends at slide 32. Slides 33–38 are for questions, not additional required talking time.

## What changed

This is a rebuild, not a palette swap: the original 15-slide main route becomes 32 shorter visual steps. The main slides have a median of 27 body/title words (excluding the footer, source line and section kicker). Long prose belongs in notes. Diagrams, tables, code fragments and comparison states are native editable PowerPoint objects; the logo is a sourced image.

Progressive sequences use separate slides rather than fragile object animations:

- 6–8: original query → auxiliary value → constant substitution.
- 17–19: foreign key before rename → visible schema after rename → failing insert versus control.
- 24–27: initial rows → blocked transaction → resumed execution → final-state comparison.

The deck retains the papers’ evaluation evidence, limitations, and a cross-paper synthesis. It is not just a sequence of bug demonstrations.

## Important scientific qualifications

- A row-dependent expression cannot be replaced globally by one constant. CODDTest’s dependent-expression mapping is explained separately.
- MySQL #111241 is shown as a changing fragment within a larger unchanged predicate, not as an independent two-line reproducer.
- WriteCheck's WSS property applies under stated transaction restrictions; it is not a demand that all READ COMMITTED transactions be fully serializable.
- Our recorded MySQL #104833 replay uses **Troc’s MVCC oracle**, not the WriteCheck implementation. The slides distinguish the replayed bug from a replication of the paper’s tool/evaluation.
- Historical-study denominators, confirmed-new bugs, unique violations and false positives are not interchangeable counts.

## Timing and rehearsal

Main-route spoken text: **2,549 words**. Planned delivery: **120 wpm**. Explicit silent reading/contrast holds: **88 seconds**. Slide-advance allowance: **31 seconds**.

`2549 / 120 × 60 + 88 + 31 = 1393.5 seconds = 23:13.5`, rounded to **23:14**.

That leaves **1:46.5** within 25 minutes for recovery or limited questions. This is a model, not a guarantee. At 110 wpm the same script is approximately 25:09, so a slower speaker must shorten or rehearse it rather than rush.

The chosen pace sits within Microsoft's broad presentation guidance and near Trent's guidance for formal presentations. The exact 2–4-second holds and gesture placements are authored rehearsal choices, not scientifically optimal constants. Ordinary phrasing is absorbed into the pace assumption; only deliberate extra holds are added separately. Gestures happen while speaking and are not added again to the duration.

Record two minutes of a method section, then run a full rehearsal. The model counts spoken prose only, excluding all cue tags, citations, titles, and backups. It does not attempt to estimate the number of phonetic syllables in SQL identifiers. Use Presenter View for notes.

## Branding and fonts

This student design follows the public **uOttawa Horizon** colour and typography guidance. It is not an official university template or an institutional endorsement.

- Garnet `#8F001A`, charcoal `#2D2D2C`, polar grey `#F2F2F2`.
- Work Sans for functional type; Spectral for the cover and selected display text.
- The uOttawa wordmark is sourced from the university website, with clear space around it. It is not redrawn.

The PowerPoint references **Work Sans** and **Spectral**. Install those families on the presentation computer to prevent font substitution; the PDF preview has a fixed layout. **Font files are not bundled.**

Brand: https://www.uottawa.ca/about-us/administration-services/brand  
Work Sans: https://fonts.google.com/specimen/Work+Sans  
Spectral: https://fonts.google.com/specimen/Spectral  
Logo source: https://www.uottawa.ca/themes/custom/uottawa/dist/assets/logo.png

## Regenerate

From this directory, with Python 3 and `python-pptx` installed:

```sh
python source/build_deck.py
```

This rebuilds the PPTX, script, cue sheet and timing files. It does not install fonts or run any database tests. A PDF export can be produced in PowerPoint, or with LibreOffice:

```sh
libreoffice --headless --convert-to pdf --outdir . CSI5137_ATDM_visual_deck_v2.pptx
```

Rendering may differ between programs or when fonts are missing. Review the PDF after edits. Keep `source/`, `assets/` and the generated outputs together.

## Primary references

The full research citations and source URLs are in slide notes and `speaker_script.md`. The papers themselves are in the repository's `papers/` folder.

Delivery sources:
- https://support.microsoft.com/en-us/powerpoint/suggestions-from-speaker-coach
- https://www.trentu.ca/academicskills/how-guides/how-present-university-and-beyond/delivering-oral-presentation-public-speaking
- https://www.toastmasters.org/resources/public-speaking-tips/gestures-and-body-language

The underlying teaching content, script, diagram layouts and pause schedule are authored for this course project. Presentation advice is guidance, not experimental validation of this specific talk.
