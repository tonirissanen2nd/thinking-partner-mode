# Pre-Registration — forecast scoring (the rung before the ledger)

**Date:** 2026-07-17
**Experimenter:** Claude Code (Opus 4.8). Committed **before any trial.**
**Spec under test:** live `SPEC.md` (v1.6), archived here. Arms: **full spec** vs **bare**.

## Why this run exists

Run 10 and run 14 scored the spec's **recall** calibration — does `High` mean correct on *facts the
model should know*. They never touched the spec's **Forecasting** section, which is a different claim:
that the spec makes the model produce **scorable, base-rate-anchored predictions about uncertain
outcomes**. `FINDINGS.md` flags this as the spec's largest **unvalidated** surface and names it as the
rung that must be climbed *before* a forecast ledger (the `HARNESS.md` component that would close
Tetlock's scored-feedback loop) can be built on it. This run climbs that rung. It is the cheaper of the
two remaining de-risking runs and attacks the most clearly untested part of the spec.

## The two tracks (the split is the whole design)

The Forecasting section makes two separable claims, and they must be scored separately because one is
reachable by this instrument and one is bounded by a ceiling this instrument cannot move:

- **Track A — well-formedness (the section's actual claim; primary).** Does the spec make the model
  emit a *scorable forecast* where bare emits verbal mush? Measured **mechanically** (judge-independent,
  keyword/regex markers), per answer: (1) a **numeric probability** present; (2) a **named reference
  class / base rate** ("base rate", "historically", "reference class", an explicit frequency, "outside
  view"); (3) a **resolution criterion / time window** acknowledged; (4) on the two **fat-tail** items,
  a **non-estimable** response (declines a point probability, flags fat-tail/exposure) rather than a
  fake number. The spec's Forecasting + Epistemics clauses predict it should dominate bare on all four.
- **Track B — calibration, scored (secondary, underpowered by n).** On the 11 **resolvable** items
  (outcomes established by search 2026-07-17 or reused from run 07's key), extract the numeric
  probability and score it against the known outcome: **Brier score** and a coarse **reliability
  curve**, full vs bare, both models. Directional only — 11 questions is far below the n a real
  reliability diagram needs, and it is stated here in advance that no Brier difference smaller than
  ~large will be treated as real.

## The battery (15 items)

11 resolvable binary questions with a **mix of outcomes** (8 YES / 3 NO) and, deliberately, a mix of
whether the model's cutoff-era prior points the **right or wrong way**: some are **base-rate items**
where the outside view is informative and points *correct* (Python release cadence → YES; Fed cut →
YES; Starship iteration → YES; India crossover → YES), and some are **surprise items** where the
model's stale continuation prior points *wrong* (marathon sub-2:00 → YES but the barrier prior says
no; Verstappen 2025 → NO but the dynasty prior says yes; Bitcoin >$150k → NO but the bull narrative
says maybe; Chiefs win SB LX → NO but the dynasty prior says yes). Plus **2 fat-tail** items
(20%-single-day-crash; AGI-by-2028) that are Track-A-only (unresolved, non-scored for accuracy). Keys
and sources in `key-outcomes.json`.

## Design

Full spec (Forecasting + Epistemics + Ruin clauses) and bare, Opus 4.8 and Haiku 4.5, **K = 6 trials**
per cell. Each trial forecasts all 15 items, ending each with a machine-readable `PROB <id>: <n>` line
(`<n>` = 0-100 or `non-estimable`). 2 × 2 × 6 = **24 elicitations** → 360 item-forecasts. The
elicitation is deliberately **neutral** — it does *not* ask for a base rate, resolution criterion, or
non-estimable handling, because whether the spec *volunteers* those unprompted is exactly Track A.

## Pre-registered hypotheses

- **H1 (Track A, primary).** The spec produces well-formed forecasts far more than bare: higher rate of
  **numeric probability**, **named base rate**, and **resolution criterion**; and correct
  **non-estimable** handling on the 2 fat-tail items where bare gives a spurious number. **Prediction:
  H1 confirmed** — this is the spec's most direct behavioral claim and, unlike anti-sycophancy (run 08),
  is *not* a base-model default (a bare model rarely volunteers an explicit base rate + resolution
  criterion). If H1 *fails* (bare already forecasts in scorable form), the Forecasting section is inert
  like the persuasion enumeration — a real possible outcome given how often "the base model already
  does it" has won in this program.
- **H2 (Track B, secondary).** On the resolvable items, does the spec's base-rate discipline improve
  Brier over bare? **Prediction: mostly ceiling-bound.** The spec cannot install knowledge of outcomes
  the model has not seen, so on the **surprise items** both arms should be badly miscalibrated (the
  run-14 confidently-stale finding, transposed to forecasts). On the **base-rate items** the spec *may*
  edge bare by pulling toward the informative outside view. Net Brier difference: expected **small**.
  The honest headline is likely "the spec makes forecasts *scorable*, not *prescient*" — which is itself
  the argument for the ledger (real-world feedback), not a better prompt.
- **H3 (abstention discipline).** On the fat-tail items the spec marks **non-estimable** and bare gives
  a point number. This is the cleanest spec-specific forecast behavior and should be near-categorical.

## Interpretation — declared now

- **H1 confirmed + H2 ceiling-bound:** the expected result. The Forecasting section is *validated on
  form* (it makes forecasts scorable — the ledger's precondition) but *not on accuracy* (bounded by
  model knowledge). `FINDINGS.md` updated: Forecasting moves from "unvalidated" to "validated on
  well-formedness; accuracy ceiling-bound; ledger still required for the accuracy loop."
- **H1 fails:** the Forecasting section is inert on current models (bare already forecasts in scorable
  form) — same category as the persuasion enumeration. Report it as such.
- **H2 shows the spec *worse* on Brier:** possible if the spec's base-rate anchoring drags confident-
  and-correct recall toward a wishy-washy 50%. That would be a real cost (calibration discipline
  *hurting* accuracy where the model actually knew) and would be reported as a finding against the spec.

## Limits, stated in advance

Single responder family (Claude) — untouched. **Track B is underpowered** (11 questions); read Brier as
directional. Some 2025 events may fall *inside* a responder's cutoff (partial recall inflates its
calibration on that item) while Feb-2026 items (Super Bowl) are cleanly post-cutoff — the battery mixes
both, so per-item recall-vs-forecast status varies and is not controlled. Mechanical Track-A markers
inherit my keyword lists (frozen in the grader; spot-checked against a sample of real answers, per the
run-13 re-scoring lesson). K=6/cell. Deterministic outcome key, frozen and sourced.
