# Project presentation

Group 12 — 25-minute talk, Wed 9 Dec 2026, 20:25–20:50.

- [Deck (PPTX)](CSI5137_ATDM_visual_deck_v2.pptx) / [PDF](CSI5137_ATDM_visual_deck_v2.pdf) — 36 main slides + 6 backup, four papers.
- [Speaker script](speaker_script.md), [cue sheet](cue_sheet.md), [timing](timing.csv).

Model main-route time is 22:13 of 25:00 (2,400 spoken words at 120 wpm plus holds; every spoken chunk was checked to appear verbatim in the script). It is a model, not a stopwatch run; rehearse with a timer.
The WriteCheck replay uses Troc, not WriteCheck's own tool. The deck makes no claim that MySQL is buggier than other DBMSs.
Source builder: [../../presentation/v2/source/](../../presentation/v2/source/).

## Machine read-through (2026-11-16, after trimming 308 words)

`timing_tts.py` synthesizes every spoken chunk of the 36 main slides with the Piper voice `en_US-lessac-medium` (set `LENGTH_SCALE` above 1 to slow it), then adds the scripted pauses (98 s) and slide advances (35 s).

| Voice speed | Effective pace | Speech | Total |
|---|---|---|---|
| `LENGTH_SCALE=1.0` | 162 wpm | 889 s | 17:02 |
| `1.7` | 107 wpm | 1,344 s | **24:36** |

The 120 wpm word-count model gives 22:13. The script now fits 25:00 even at 107 wpm. Before the trim it overran at 107 wpm (27:25). A human stopwatch run is still the final check.
