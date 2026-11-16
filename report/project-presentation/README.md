# Project presentation

Group 12 — 25-minute talk, Wed 9 Dec 2026, 20:25–20:50.

- [Deck (PPTX)](CSI5137_ATDM_visual_deck_v2.pptx) / [PDF](CSI5137_ATDM_visual_deck_v2.pdf) — 36 main slides + 6 backup, four papers.
- [Speaker script](speaker_script.md), [cue sheet](cue_sheet.md), [timing](timing.csv).

Model main-route time is 24:47 of 25:00 (2,708 spoken words at 120 wpm plus holds; every spoken chunk was checked to appear verbatim in the script). It is a model, not a stopwatch run; rehearse with a timer.
The WriteCheck replay uses Troc, not WriteCheck's own tool. The deck makes no claim that MySQL is buggier than other DBMSs.
Source builder: [../../presentation/v2/source/](../../presentation/v2/source/).

## Machine read-through (2026-11-16)

`timing_tts.py` synthesizes every spoken chunk of the 36 main slides with the Piper voice `en_US-lessac-medium` and adds the scripted pauses and slide advances. Result: 1,000 s of speech (about 163 wpm), 98 s of holds, 35 s of advances, **18:52 total**. A synthetic voice is faster than a careful human delivery. At the 120 wpm planning rate the model gives 24:47. Both fit 25:00. A human stopwatch run is still the real test.
