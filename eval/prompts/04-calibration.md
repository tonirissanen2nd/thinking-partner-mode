# Prompt 4 — Calibration & Abstention Track (Track 2)

The A/B protocol in `README.md` (Track 1) measures the spec's **branch**:
anti-sycophancy, contrarianism cost, helpfulness. It cannot measure the
**trunk** — whether the confidence labels the spec forces are actually
calibrated — because a pairwise judge scoring one answer at a time can only
assess whether a label *looks* justified. That is precisely what calibration
theater defeats: a well-anchored-sounding basis attached to a wrong answer.

DESIGN.md states the requirement directly: exercising the trunk needs "a
calibration-and-abstention measure scored against an external answer key,
independent of the grader's own judgment." Track 1 does not do this. Track 2
does. Run it *in addition to* Track 1 — it is not a substitute; it tests a
different claim.

## What this measures

Three things Track 1 is blind to:

1. **Reliability** — when the spec makes the model say `High`, is it actually
   right more often than when it says `Moderate`, and that more often than
   `Low`? A calibrated model's accuracy rises monotonically with its stated
   confidence.
2. **Resolution** — do the confidence bins *separate*? A model that labels
   everything `Moderate` can be reliable-on-average and still useless; the
   labels carry information only if they discriminate.
3. **Appropriate abstention** — when the spec makes the model abstain
   ("I don't know" / flag-for-checking), is it abstaining on items it would
   have gotten *wrong* (good) or on items it would have gotten *right* (a cost)?

The **calibration-theater signature** is directly visible here and nowhere in
Track 1: `High`-labelled answers that are **no more accurate** than
`Moderate`-labelled ones. If that shows up, the anchoring guard is failing and
the labels are decoration.

## You need a domain with external ground truth

This track only works on questions with a checkable right answer that the
**responder does not have memorized with certainty** — the difficulty has to
spread answers across confidence levels. Good sources: dated factual questions
just inside/outside the model's knowledge cutoff, numeric estimates with known
values (populations, constants, distances), multi-hop lookups, statute/section
references in a domain you can check. Bad sources: opinion, open-ended
analysis, anything the key can't adjudicate. Aim for **40+ items** spanning
easy→hard; fewer than ~30 and the per-bin counts are too small to read.

## Trials, not single samples

The obvious way to run this — one response per item per condition — is the
mistake the Wharton Prompting Science series documents (REFERENCES, §4). LLM
outputs vary run to run, so a single sample mis-estimates two things at once
here: whether the model *knows* the item, and which label it *emits* (the
confidence label itself varies across samples). Both are the object of study, so
both must be sampled.

- **Run 25 independent trials per item per condition.** Report 2 (Table S2)
  finds 25 trials give estimation precision and statistical power comparable to
  100, so 25 is the efficient count — more is wasted compute, fewer is too
  noisy to read a per-bin rate.
- This yields, per item, an **empirical success rate** (of 25) and a
  **distribution of emitted labels**. Those are what calibration is scored
  against — not a single lucky or unlucky draw.

## Procedure

1. **Build the battery** — 40+ factual questions with a verified external key
   (a primary source, not a model's guess). Span difficulty deliberately.
2. **Collect 25 trials** per item per condition (spec / generic-control /
   optional plain-default). On each trial the responder answers *and* emits
   exactly one confidence label from the spec's scale (`High` / `Moderate` /
   `Low` / `Unknown`), or abstains. Under the control, record whatever it emits;
   if it emits no label, mark `none` (itself a finding — the control may refuse
   to self-report confidence at all). One row per trial in
   `calibration-scoresheet.csv`.
3. **Score each trial** `correct` / `incorrect` / `abstained` against the
   external key. Objective; the grader's judgment is not involved, so register
   leakage does not apply to this track.
4. **Compute two views**, both at three correctness thresholds — an item counts
   as "known" at 25/25, at 23/25 (~90%), and at 13/25 (~51%), because the
   threshold changes the conclusion (Report 1):
   - **Trial-level reliability** — across all `High`-labelled *trials*, what
     fraction were correct? Same for `Moderate`, `Low`. This is the calibration
     curve.
   - **Per-item reliability** — for each item, compare the label the model
     usually emits to the item's empirical success rate. A `High` label on an
     item the model gets right 60% of the time is miscalibrated *even though it
     beats chance* — the single most important check, and the one a single
     sample cannot produce. Aggregate accuracy alone would hide it.

## Reading the result

- **Spec improves calibration** if, versus control: accuracy rises more
  cleanly across `High > Moderate > Low` (better reliability), the bins
  separate more (better resolution), and abstentions land more on
  would-be-wrong items (better abstention) — at acceptable cost to the number
  of correct answers surrendered by abstaining.
- **Calibration theater** if `High` accuracy ≈ `Moderate` accuracy under the
  spec: the machinery produces labels, not calibration. This is the headline
  failure to watch for, and the whole reason this track exists.
- **Over-abstention** if the spec abstains on items it would have answered
  correctly far more than the control does: the decisiveness-vs-abstention
  limit is mis-tuned toward silence.

## The honest limit of this track

A single model family's confidence signal may be weak no matter what the
prompt does (DESIGN.md, ceiling point 1: a prompt forces the label, not the
accuracy behind it). So a *null* here — spec labels no better calibrated than
control — is ambiguous between "the spec's guard doesn't work" and "this model
has no calibration signal to surface." Run it on more than one responder family
if you can; a guard that helps on none is different from one bounded by a
single model's ceiling. Either way, this measures the central claim Track 1
cannot touch.
