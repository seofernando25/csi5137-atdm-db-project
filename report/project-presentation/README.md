# Project presentation

Group 12 — 25-minute talk, Wed 9 Dec 2026, 20:25–20:50.

- [Deck (PPTX)](CSI5137_ATDM_visual_deck_v2.pptx) / [PDF](CSI5137_ATDM_visual_deck_v2.pdf) — 36 main slides + 6 backup, four papers.
- [Speaker script](speaker_script.md), [cue sheet](cue_sheet.md), [timing](timing.csv).

Model main-route time is 24:47 of 25:00 (2,708 spoken words at 120 wpm plus holds; every spoken chunk was checked to appear verbatim in the script). It is a model, not a stopwatch run; rehearse with a timer.
The WriteCheck replay uses Troc, not WriteCheck's own tool. The deck makes no claim that MySQL is buggier than other DBMSs.
Source builder: [../../presentation/v2/source/](../../presentation/v2/source/).

## Machine read-through (2026-11-16)

`timing_tts.py` synthesizes every spoken chunk of the 36 main slides with the Piper voice `en_US-lessac-medium` and adds the scripted pauses and slide advances. Result: 1,001 s of speech (about 162 wpm), 98 s of holds, 35 s of advances, **18:53 total**. A synthetic voice is faster than a careful human delivery. At the 120 wpm planning rate the model gives 24:47. Both fit 25:00. A human stopwatch run is still the real test.

### Same read at three speaking speeds (`LENGTH_SCALE` slows the synthetic voice)

| Voice speed | Effective pace | Speech | Total with pauses and advances |
|---|---|---|---|
| `LENGTH_SCALE=1.0` | 162 wpm | 1,001 s | 18:53 |
| `1.36` | 131 wpm | 1,240 s | 22:53 |
| `1.7` | 107 wpm | 1,512 s | 27:25 |

The script fits 25:00 at about 120 wpm or faster (interpolating the runs above; the 120 wpm model gives 24:47) and overruns at about 107 wpm (27:25). Present at 120 wpm or above, or cut about 200 words. A human stopwatch run is still the final check.
