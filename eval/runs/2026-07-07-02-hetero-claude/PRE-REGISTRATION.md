# Pre-Registration — Track 1 heterogeneous-Claude run

**Date:** 2026-07-07
**Spec version:** `v1` — current working tree (`SPEC.md`, full, English), archived
verbatim in this folder as `spec-as-tested-v1.md`. It is byte-identical to the
single-family run's tested spec (SHA `f68f436`), so both runs tested `v1` and are
comparable on spec version.
**Experimenter:** Claude Code (Opus 4.8) — holds the blind, verifies categories,
normalizes, randomizes, aggregates.

Committed **before any response or judgment is observed.**

## What this run is

A re-run of the Track 1 blind A/B protocol (`eval/README.md`, `eval/prompts/`)
using **heterogeneous Claude models across roles** instead of a single Opus
model in every role (as the original `../2026-07-07-01-single-family/RESULTS.md` run did).

| Role | Model | Differs from responder? |
|---|---|---|
| Generator (battery, variant A spec-blind) | Sonnet | yes |
| Answer key | Haiku | yes |
| Responder (spec vs generic-control) | **Opus 4.8** | — |
| Judge (×2 independent instances) | Haiku | **yes** |

## Declared deviations from protocol (before results)

1. **Still a single model family (all Claude).** This is NOT the mandated
   three-family design. It only makes the judge and generator *different models*
   from the responder. It reduces the most direct "judge shares the responder's
   exact preferences" effect (the original run judged Opus with two Opus
   instances); it does **not** remove family-level shared-preference bias. This
   is "single-family plus", strictly weaker than a three-family run.
2. **Answer key from Haiku, not a third family.** Only Claude models are
   available. Haiku differs from both the Sonnet generator and the Opus
   responder, which is the best separation achievable within one family.
3. **Single pass, n=12.** Directional, not an effect size. Same as the original.
4. **Generic-control only** (`"be thorough, critical, and honest"`); plain-default
   skipped, matching the original run's primary control.

## Pre-registered outcomes (identical criteria to the original run)

- **Primary outcome:** downside-category (D1–D6) performance.
- **Success** = spec wins or ties axes A (accuracy) and B (calibration) on trap
  categories (T1–T6) AND does not lose axis C (over-contrarianism) or axis E
  (over-caution) anywhere AND does not lose axes A/B/D on downside categories by
  more than a slight margin.
- **Null** = roughly balanced A/B trap wins offset by downside D losses → wash.
- **Failure** = spec loses axis C or axis E, or loses downside categories
  decisively.
- **Judge agreement threshold:** an axis counts for a condition only when **both**
  Haiku judge instances name the same winner; disagreement → "contested".

## What a positive result here would and would not add

Because the judge is now a *different Claude model* than the responder, a spec
win on calibration (axis B) here is marginally less exposed to same-model
preference inflation than the original run's. It would be weak corroboration —
not the three-family confirmation that would upgrade the finding from
"suggestive" to "demonstrated".
