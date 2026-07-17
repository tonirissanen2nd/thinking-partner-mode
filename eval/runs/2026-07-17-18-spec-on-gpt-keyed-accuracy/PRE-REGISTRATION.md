# Pre-Registration — keyed accuracy/calibration on a GPT responder

**Date:** 2026-07-17
**Experimenter:** Claude Code (Opus 4.8). Committed before any GPT elicitation.
**Responder:** OpenAI **GPT-5 Thinking (High)** via ChatGPT Plus, temporary chat. Arms: **spec** (full
`SPEC.md` v1.6 preamble) vs **bare** (elicitation only).

## Why

Run 17 showed the spec *changes* GPT's behaviour (it installs the register). It did **not** test whether
the spec makes GPT more **accurate/calibrated** — the spec's *validated core* on Claude (runs 10/14).
This run applies run 14's method to a GPT responder: **does the calibration trunk transfer across
training lineages?** It is judge-free (scored against run 14's frozen external key), the only kind of
result no judge of any family can move.

## Design

Reuse **run 14's exact 15-item adversarial battery and frozen `key-and-tolerances.json`** (7 post-cutoff
volatile facts, 5 gotcha/precision traps, 2 obscure numerics, 1 control). Each arm answers all 15 with a
confidence label (High/Moderate/Low/Unknown). K = 2 trials per arm (browser-driven; compact outputs).
Deterministic grading (name-keyword or numeric band) exactly as run 14. Primary measures: **`High`-and-
wrong rate** and the **reliability curve** (accuracy by confidence bin), spec vs bare, compared to
run 14's Claude result.

## Search control (critical)

GPT-5 Thinking can browse. This must be a **recall** test. Mitigation: (1) the elicitation forbids
searching; (2) the **7 volatile items are their own search-detector** — their *current* answers are
post-cutoff, so a stale answer (Kiptum / Python 3.13 / Verstappen) proves recall, while a correct
current answer (Sawe / 3.14 / Norris) means the model searched or has a very recent cutoff. Each trial
is inspected and flagged; if a trial clearly used live data on the volatile items, it is reported as
search-contaminated and excluded from the recall-calibration read (kept for the record).

## Pre-registered predictions

- **P1 — the trunk transfers in shape.** GPT-under-spec's confidence curve is monotone (High > Moderate
  > Low) and its `High` is accurate on **stable** facts, cracking on **post-cutoff volatile** facts —
  the exact run-14 Claude pattern (`High` 100% stable, ~91% pooled). Basis: run 17 showed GPT executes
  the confidence-labelling directive; run 15 showed GPT's calibration is real; the confidently-stale
  failure is a base-model-knowledge property every model shares.
- **P2 — spec cuts confidently-wrong vs bare, if bare labels at all.** As on Claude (run 14: Opus 5→2,
  Haiku 12→9), the spec's "how could this be wrong" + "flag < High recall" gates should make spec-GPT
  demote volatile facts more than bare-GPT, lowering its `High`-and-wrong rate. Uncertain because
  bare-GPT may label erratically or refuse the format.
- **P3 — the interesting divergence: GPT's cutoff may be more recent than the battery.** If GPT-5 gets
  the volatile items *right from recall* (recent cutoff), the battery is not adversarial for it and
  `High` may stay ~100% — which would be a *weaker* test on GPT, not a stronger spec result. Flagged so
  a clean `High`=100% is not over-read.

## Interpretation — declared now

- **Trunk transfers (P1 holds):** the spec's calibration core is model-family-portable — its most
  important validated property is not Claude-specific. Strengthens `FINDINGS` #3 (model-independence)
  to cross-lineage.
- **Trunk fails on GPT (flat curve / High-and-wrong on stable facts):** the calibration behaviour is
  Claude-specific; the spec installs the *labels* on GPT (run 17) but not the *calibration* — a real
  boundary on portability.
- **Search-contaminated:** report honestly and treat as inconclusive on the volatile items; the
  gotcha/obscure/control items remain a valid (if easier) recall read.

## Limits

One model/tier, K=2, single responder family beyond Claude. Deterministic grading inherits run 14's
frozen bands. Browser-driven (format-fragility possible). Recall-only by instruction, verified via the
volatile-item detector, not by disabling tools at the API level.
