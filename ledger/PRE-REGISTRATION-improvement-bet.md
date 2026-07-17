# Pre-Registration — the improvement bet

**Date:** 2026-07-17
**Committed before the experiment is run.** The ledger (measurement instrument) is built and seeded;
this registers the *separate, uncertain* question it does not assume.

## The bet, stated plainly

The ledger's **measurement** value is certain and already realised (`ledger/README.md`). The **bet** is
whether the ledger's *feedback* also *improves* the model — i.e. whether **giving the model its own
scored track record at forecast time makes its next forecasts better-calibrated** than forecasting cold.

This is Tetlock's mechanism (calibration is earned by scored feedback, not by a good rule). It is the
one thing that could reach past the prompt-layer ceiling the program documented — *because a retrieved,
concrete record of your own past errors is evidence to condition on, not a bare instruction.* But it may
hit the **same say-vs-do ceiling** the spec did: the model may merely *say* it will recalibrate, or
reflexively hedge, without actually forecasting better. **That is the open question.**

## Design (the runnable proxy)

The *true* test is longitudinal (forecast → wait → resolve → score → forecast again months later with an
accumulated ledger) and only running the ledger over time delivers it. The runnable **proxy** now:

- **Battery:** a *fresh* set of ~12 resolvable forecast questions the model genuinely cannot know
  (post-cutoff / withheld, outcomes established by the scorer — built like run 15 / run 19).
- **Arm A (cold):** the model forecasts the battery under the spec, as in run 15.
- **Arm B (ledger-fed):** the *same* model, *same* battery, but **prepended with its own ledger report**
  — the calibration summary the instrument already produces (overall ECE + reliability curve +
  per-reference-class Brier, e.g. *"your past forecasts are systematically underconfident (+0.15);
  on sports-records you forecast ~4% for events that resolved 100%; on software-release you are
  well-calibrated"*).
- Both arms scored by the ledger against the known outcomes. Same model/tier; A/B order irrelevant
  (deterministic key). K trials each.

## The metric — and the trap that must be pre-registered

Report **all four**: Brier, ECE, the reliability curve, **and discrimination** (the ledger already
computes it: top-half-minus-bottom-half resolve rate).

**The trap:** a model told "you were miscalibrated" can improve its *calibration* by collapsing every
forecast toward 50% — which destroys **discrimination** and makes the forecasts useless. So:

> **Win condition (pre-committed): Arm B improves ECE/Brier *while holding discrimination* (loses no
> more than a small margin of the top-vs-bottom separation). A calibration gain bought by a
> discrimination collapse is a FAILURE, not a success.**

There is a sharper wrinkle unique to *this* seed: the model is **underconfident**, so the *correct*
recalibration is to be **more** extreme (sharpen), not to hedge. The reflexive response to "you were
wrong" is to hedge toward 50% — which here is the **wrong direction**. So this battery specifically
tests whether the model can move *against its safe instinct* on the strength of concrete evidence.

## Pre-registered predictions (honest, low confidence)

- **P1 (primary) — genuinely uncertain, slight lean to failure-via-reflexive-hedge.** [Low] I expect
  Arm B to *change* its forecasts (it will visibly "take the feedback"), but I lean slightly toward it
  **hedging toward 50% rather than sharpening** — improving apparent calibration on the metric while
  losing discrimination, i.e. tripping the pre-registered trap. Reason: sharpening against your own
  underconfidence requires trusting per-class feedback over the safe instinct, and the program's whole
  finding is that the prompt/context layer installs the *appearance* of a fix more readily than the fix.
- **P2 — the optimistic branch is live.** [Low] The concrete, per-class, numeric record ("you said 4%
  and it happened") is qualitatively stronger evidence than any bare instruction, so a *real* gain
  (calibration up, discrimination held) is a genuine possibility — and would be the most important
  positive result in the whole program: feedback doing what instruction could not.
- **P3 — the null is also live.** [Moderate] Arm B ≈ Arm A: the model cannot use its own track record
  in-session to recalibrate. Then the ledger's value is **purely measurement** (still real and certain),
  and improvement needs training-loop feedback, not context.

## Interpretation — declared now

- **B better (P2):** feedback breaks the prompt-layer ceiling. The ledger is an improvement mechanism,
  not just a scoreboard. Then: build the longitudinal loop for real.
- **B ≈ A (P3):** the ledger is a scoreboard only. Honest and still valuable — you correct for the
  miscalibration yourself; the model doesn't.
- **B worse / hedged (P1):** in-context feedback *harms* via reflexive hedging. Cautionary: do not feed
  raw scores back naively; the miscalibration must be corrected by the *user*, not the model.

## Prerequisites & limits

Requires (a) a populated ledger — **met** (264 seeded resolved forecasts); (b) a fresh unknowable
resolvable battery — to be built. Single-session proxy for a longitudinal mechanism: it tests whether
the model can *use* a track record, not whether accumulating one over months works (only running the
ledger delivers that). One model/tier, small K. Same pre-register / judge-free-key / revert discipline
as every run. Do **not** read a positive proxy as the longitudinal result — it is the necessary first
rung, exactly as run 15 was the rung before this.
