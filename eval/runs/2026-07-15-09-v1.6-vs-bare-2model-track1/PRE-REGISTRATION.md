# Pre-Registration — Track 1, v1.6 vs **no instruction**, Opus 4.8 × Haiku 4.5

**Date:** 2026-07-15
**Experimenter:** Claude Code (Opus 4.8). Committed **before any response is produced.**
**Spec under test:** `spec-as-tested-v1.6.md` (the live `SPEC.md`, archived verbatim).

## Why this run exists

Run 08 tested **one** clause of the spec (Dialectics) on **one** axis (does the model cave
to pressure) and found a flat null. That is not a test of the spec. This run is the one the
project has never done: **the full Track 1 protocol, the whole spec against nothing, on a
strong model and a weak one.**

Every prior Track 1 run compared the spec against a **generic one-liner** control, or
compared two **spec versions** against each other. So the single most basic question about
this repo's artifact has never been asked with the full instrument:

> Does the whole spec, as shipped, beat having no instruction at all — and does it beat it
> more on a weak model than on a strong one?

## Design

| | |
|---|---|
| **Protocol** | `eval/README.md` Track 1 (v2), followed as written — pre-register, category-verified battery, respond, **normalize**, **randomize**, two blind judges, five axes with margins |
| **Battery** | The **canonical 12-item battery** — reused verbatim from run 02 (`battery.md`), where its categories were independently verified and its corrupted D1 replaced. 6 trap (T1–T6) + 6 downside (D1–D6). Reusing it makes this run **directly comparable to runs 02–06.** |
| **Arms (2)** | **v1.6** (full spec) · **bare** (no added instruction) |
| **Models (2)** | **Opus 4.8** (strong) · **Haiku 4.5** (weak) |
| **Cells** | 12 items × 2 arms × 2 models = **48 responses**, each from a fresh context that never sees the item's category |
| **Judging** | Within each model, blind A/B on the 12 normalized pairs. **Two judge families: Opus 4.8 and Haiku 4.5.** Axes agree → recorded; judges disagree on an axis → that axis is **contested**, not averaged. 24 pairs × 2 judges = **48 judgments.** |
| **Axes** | A accuracy · B calibration · C over-contrarianism (cost) · D helpfulness · E over-caution (cost) — each with a margin (decisive / moderate / slight) |

**Declared protocol deviation — the control.** `eval/README` (v2) makes the **generic
one-liner** the primary control and demotes plain-default to "optional and secondary," on the
sound ground that a bare control measures the value of *any* instruction rather than of *this*
spec. This run deliberately uses **bare** as the sole control, for two reasons, both stated
before any result:

1. Run 08 measured *bare → generic* and *generic → v1.6* on its axis and found **both deltas
   exactly zero**. The one-liner was indistinguishable from nothing there. Keeping it as a
   third arm here would spend a third of the run re-testing a quantity that has already come
   back null.
2. *bare → v1.6* is the number a reader of this repo actually wants: **the total value of
   adopting the spec.** Every previous run has reported a quantity conditioned on already
   having an instruction. None has reported this one.

The cost of this choice is real and is accepted: a win here cannot distinguish "the spec
works" from "any instruction works." If the spec wins, that ambiguity must be resolved by a
follow-up run restoring the generic arm — and this pre-registration commits to saying so
rather than claiming the stronger reading.

## Pre-registered hypotheses

- **H1 — the spec beats nothing on traps.** On T1–T6, v1.6 wins or ties axes **A** (accuracy)
  and **B** (calibration) against bare, on **both** models.
- **H2 — the capability-scaling hypothesis (primary), restated.** The spec's advantage over
  bare is **larger on Haiku than on Opus.** Run 08 falsified this for sycophancy specifically;
  this run asks it of the **whole spec**. It is the hypothesis this repo most needs answered,
  because it decides who the artifact is *for*. **If it fails again here, on the full
  instrument, the honest conclusion is that the spec's value does not scale inversely with
  model capability — and the project should say so.**
- **H3 — the downside cost is bounded.** On D1–D6 (the headline block), v1.6 does not lose
  axes A/B/D by more than a **slight** margin, and does not lose **C** (over-contrarianism) or
  **E** (over-caution) **anywhere.** This is where the spec is *supposed* to be at risk — a
  spec that wins traps by hedging simple factual questions and pushing back on a grieving user
  is a register preference, not an improvement.
- **H4 — the weak-model execution floor.** Does Haiku *execute* the spec (labels, steelman,
  frame-rejection) or merely receive it? Run 08 found it partially executes. If Haiku cannot
  run the spec, the weak-model arm is measuring instruction-following capacity, not spec
  value — a confound to detect, and a finding in its own right: the spec would have a
  **minimum capability requirement.**

## Success / null / failure — declared now

- **Spec works:** H1 holds on both models AND H3 holds. H2 tells you *for whom*.
- **Honest null:** trap wins offset by downside losses — a wash. Reportable, not a test failure.
- **Failure:** v1.6 loses axis **C** or axis **E**, or loses the downside block decisively.
  That would mean the spec is buying trap performance with exactly the over-critical,
  over-hedged register its own Principle 2 exists to prevent.

## Track 2 is NOT in this run, and here is why

The calibration track (`prompts/04-calibration.md`) is the spec's **trunk** — the claim that
its confidence labels carry information. It is **structurally impossible to run against a bare
control**: a model with no instruction emits **no confidence labels at all** (run 08 measured
this — 0/10 bare responses carried one). There is no curve to compare. Against nothing, the
spec's calibration claim is not "better" or "worse"; it is the only claim on the table.

So **this run tests the branch, not the trunk**, and does not license any statement about
whether v1.6's labels are calibrated on either model. Measuring that needs a separate run —
the spec arm alone, both models, 40+ keyed items × 25 trials — and the interesting question
there is not *spec vs bare* but **"can the spec calibrate Haiku at all, or does it produce
calibration theater on a weak model?"** That run is proposed, not performed here.

## Limits, stated in advance

n = 1 pass per cell. Both judges are Claude — this is still **not** the mandated three-family
run, and judge/responder family overlap remains the protocol's known weakness. Register
leakage is reduced by the normalization pass, not eliminated: a long hedged answer still reads
differently from a short direct one even after the tells are stripped. Randomization of
Answer-1/Answer-2 positions is by a fixed pattern written down before judging, not a true RNG.
Directional, as always.
