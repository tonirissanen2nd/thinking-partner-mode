# Track 2 — first run (ceiling effect, reported for transparency)

The first Track 2 battery (40 general-knowledge items: capitals, constants,
famous dates, atomic numbers) was **too easy for Claude Opus 4.8**. Result:

- **spec:** 1000/1000 correct, 0 abstained. Curve: High acc 1.00 (n=936),
  Moderate acc 1.00 (n=64).
- **generic:** 1000/1000 correct, 0 abstained. Curve: High acc 1.00 (n=954),
  Moderate acc 1.00 (n=46).

With 100% accuracy and zero errors there is nothing for a lower confidence label
to predict — the calibration curve is degenerate and the run measures nothing
about calibration. This is precisely the "honest limit of this track" the
protocol names: a single strong model can hit the ceiling, at which point the
battery, not the spec, is the bottleneck.

The one directional signal even here: the spec used `Moderate` on the genuinely
approximate items (populations, Great Wall length) more than the control did —
i.e. it lowered confidence in the right places — but since the model got those
right too, the move could not be scored.

**Action taken:** rebuilt a hard, high-precision battery with strict grading to
force error spread. That re-run is the one reported in `RESULTS.md` and in
`track2-curve.csv` / `track2-peritem.csv`.
