# CSI 5137 — ATDM Presentation

**Testing Databases Without an Answer Key**

## Files

- `CSI5137_ATDM_visual_deck_v2.pptx` — editable PowerPoint with speaker notes
- `CSI5137_ATDM_visual_deck_v2.pdf` — fixed-layout preview
- `speaker_script.md` — full annotated script
- `cue_sheet.md` — short rehearsal prompts
- `timing.csv` and `timing_summary.json` — word counts and timing estimates
- `source/` — deck content and build script
- `assets/` — presentation assets

Slides 1–36 are the main presentation. Slides 37–42 are backups for questions.

## Timing

The main script is planned for roughly **25 minutes (model total 22:13)** at about 120 words per minute, including deliberate pauses and slide changes.

Use the timing files as a rehearsal guide, then calibrate with a full spoken run.

## Scientific note

The MySQL #104833 transaction example in this project is replayed with **Troc's MVCC-based oracle**. It is used as a representative transaction bug and should not be described as a direct rerun of the WriteCheck implementation.

## Branding

The deck uses a uOttawa-inspired garnet, charcoal, grey, and white palette and references Work Sans and Spectral.

It is a student course presentation, not an official University of Ottawa template.

Font files are not included in the repository.

## Regenerate

From this directory, with Python 3 and `python-pptx` installed:

```bash
python source/build_deck.py
```

To export a PDF with LibreOffice:

```bash
libreoffice --headless --convert-to pdf --outdir . CSI5137_ATDM_visual_deck_v2.pptx
```

Check the exported PDF after edits because layout and font substitution can vary between programs.

## References

Research sources are cited in the slide notes and speaker script. The CODDTest, DDLCheck, and WriteCheck papers are also in the repository's [papers/](../../papers/) folder; the Radar paper is cited in the speaker script (PVLDB 17(8), 2024).

Presentation guidance used during preparation:

- https://support.microsoft.com/en-us/powerpoint/suggestions-from-speaker-coach
- https://www.trentu.ca/academicskills/how-guides/how-present-university-and-beyond/delivering-oral-presentation-public-speaking
- https://www.toastmasters.org/resources/public-speaking-tips/gestures-and-body-language
