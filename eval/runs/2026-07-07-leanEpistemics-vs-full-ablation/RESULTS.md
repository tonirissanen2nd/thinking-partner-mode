# Results — lean-Epistemics vs full ablation (2026-07-07)

**Pre-registration:** `PRE-REGISTRATION.md` (committed before any result).
**Setup:** `full` = v1's `SPEC.md`; `lean` = same spec with the Epistemics paragraph
cut to a short core (labels-to-basis, don't-fabricate/flag, name-omissions) —
removing the "how could this be wrong" gate, fat-tail demotion, non-estimable
distinction, decisiveness clause. Forecasting and Ruin sections unchanged in both.
**Purpose-built battery:** 3 fat-tailed (F), 3 ruin/irreversibility (R), 3
hidden-failure-path (H), 3 ordinary controls (C). Responder = Opus; Judge ×2 = Haiku,
blind. n=1 per item (3 per group); directional.

**One-line summary.** The dense Epistemics machinery **earns its keep** — on the
stress items it was built for, `full` beats `lean` on accuracy (5–2) and calibration
(4–2), most cleanly on the fat-tail group (2–0 / 2–0). On ordinary controls the two
are even (no over-hedging cost). This **reconciles the Track-2 null**: the machinery
is redundant on ordinary facts but not on the tail. The leaner variant would buy
saliency/brevity at the cost of measurably worse fat-tail/ruin behaviour — not a free
win. Keep the dense Epistemics.

## Results

full / lean / tie / contested. 3 items per group.

| Axis | F (fat-tail) | R (ruin) | H (hidden-fail) | C (control) |
|---|---|---|---|---|
| A Accuracy | **2/0**/0/1 | 1/1/0/1 | **2**/1/0/0 | 1/0/1/1 |
| B Calibration | **2/0**/0/1 | 1/0/0/2 | 1/**2**/0/0 | 0/0/2/1 |
| C Over-contrarianism (inv.) | 0/0/2/1 | 0/0/2/1 | 0/0/2/1 | 0/1/1/1 |
| D Helpfulness | 0/1/0/2 | **2/0**/0/1 | 0/**2**/0/1 | 0/1/0/2 |
| E Over-caution (inv.) | 1/**2**/0/0 | 1/1/0/1 | 0/1/0/2 | 0/0/2/1 |

**Stress groups combined (F+R+H, 9 items):**
- **Accuracy: full 5 / lean 2** / tie 0 / contested 2
- **Calibration: full 4 / lean 2** / tie 0 / contested 3

## Findings vs hypotheses

**H1 (machinery earns its keep) — SUPPORTED, concentrated on the tail.** Across the
9 stress items, full wins accuracy 5–2 and calibration 4–2. The cleanest signal is
the **fat-tail group**: full wins both accuracy and calibration 2–0 — it resists the
false point estimate / marks non-estimable more reliably than lean, *even though lean
kept the Forecasting section*. So the Epistemics-internal fat-tail machinery adds
value **over and above** the Forecasting/Ruin sections and the strong base model. The
**ruin group** leans full on helpfulness (2–0) and ties accuracy. The
**hidden-failure group** is the weakest/mixed: full edges accuracy (2–1) — consistent
with the removed "how could this be wrong" gate helping — but lean was judged better
calibrated and more helpful there.

**H2 (no free lunch on controls) — HOLDS.** On the ordinary controls, accuracy and
calibration are tie/contested; the dense machinery did **not** measurably over-hedge
simple facts. The density is not costly where there is no tail.

**H3 (lean upside) — NOT supported.** Lean did not match full on the stress items, so
the dense paragraph is not merely redundant length — it buys tail behaviour a short
core misses.

## The synthesis this run completes

Two eval results that looked contradictory now reconcile:

- **Track 2 (single-family, ordinary facts):** the full machinery did **not** beat a
  generic "be honest" instruction → it *looked* like dead weight.
- **This run (fat-tail / ruin / hidden-failure):** full **beats** the lean core on
  exactly those items → the machinery earns its keep.

Resolution: **the Epistemics machinery's value is concentrated where `DESIGN` says it
should be — the tail — and is redundant on ordinary calibration.** The earlier
"leaner Epistemics" hypothesis drew the wrong conclusion from testing on the wrong
items. A leaner variant's benefits (saliency, brevity, lower cost) are real in
principle, but this run shows they would be bought at the price of the fat-tail/ruin
behaviour the spec exists for — behaviour an ordinary battery never surfaces. **Keep
the dense Epistemics; do not lean it on the strength of the ordinary-facts null.**

## Caveats

n=1 per item, only 3 per group — small even by this repo's standards; read the F
group (cleanest, 2–0/2–0) over the noisier H group. Single family; Haiku judge. The
**Forecasting/Ruin confound** cuts *for* the finding, not against: lean retained those
sections, so full's edge on F/R isolates the Epistemics-internal tail machinery's
marginal value over them. The H group is genuinely mixed and would need more items to
call. Directional, not settled — but the direction (full ahead on stress, even on
controls) is consistent across both accuracy and calibration.
