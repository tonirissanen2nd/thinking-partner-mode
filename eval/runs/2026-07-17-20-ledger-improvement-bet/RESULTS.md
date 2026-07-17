> **Note (tool retired):** the ledger was built and demonstrated as a measurement instrument this
> session, then **retired** — it will not remain in use. This run (20) is the permanent record of the
> improvement bet; the ledger *concept* and *finding* live on in `METHOD.md`, `HARNESS.md`, and
> `FINDINGS.md`, but the runnable code and store were removed.

# Results — the improvement bet (run 20)

**TL;DR — the improvement bet failed, and instructively.** Feeding the model its own scored forecast
track record (arm B) did **not** improve its calibration over forecasting cold (arm A) — it was
**marginally worse**, with discrimination unchanged. The mechanism: the model **mostly ignored** the
feedback (10 of 12 items moved ≤3 points — the say-vs-do ceiling, now shown for calibration-via-context),
and the one large response was a **catastrophic over-correction** that destroyed a bold-correct call.
A third finding emerged that neither arm's design anticipated: the fed-back *"you are underconfident"*
diagnosis is partly a **surprise-heavy-battery sampling artifact** — so the ledger, as a *feedback
source*, fed a possibly-spurious signal, which the model was arguably right to mostly ignore. The
ledger's *measurement* value (run 19) is untouched; its *improvement* value is not
demonstrated and naive feedback can harm. Pre-registered in `PRE-REGISTRATION.md` (this run).

Responder: Claude Opus 4.8 (the ledger *is* Claude's track record, from run 15). Fresh 12-item forecast
battery of 2026 events post-dating Opus's cutoff (outcomes web-established 2026-07-17). Arm A = spec,
cold; Arm B = spec + its own ledger report prepended, neutral instruction to "account for this
demonstrated calibration." K=4 per arm (48 forecasts each). Scored judge-free by the ledger.

## The scores

| Metric | Arm A (cold) | Arm B (ledger-fed) | Better |
|---|---|---|---|
| **Brier** (lower better) | **0.414** | 0.457 | A |
| **ECE** (lower better) | **0.443** | 0.483 | A |
| **Discrimination** (higher better) | 0.167 | 0.167 | tie |

**Win condition (pre-registered): B improves ECE/Brier *while holding discrimination*.** B did **not**
improve either — it worsened both — so the bet is **not supported.** Discrimination held (no collapse),
so this is the plain no-improvement failure, not the hedge-to-50% trap I predicted.

## What actually happened (per item, A → B)

The feedback was **mostly ignored, then misapplied once:**

- **10 of 12 items barely moved** (≤3 points): the model "received" the ledger but did not systematically
  recalibrate. This is the prompt-layer ceiling, transposed to context-feedback: shown its own errors, the
  model largely did not act on them.
- **q2 (Python 3.14.6 by mid-2026, YES): 31 → 46 (+15), the one *correct* move** — it sharpened upward
  toward a near-certain base-rate event. Evidence the model *can* use the record when the direction is
  obvious.
- **q9 (Bulgaria wins 2026 Eurovision, YES): 75 → 2 (−73), a catastrophic *wrong* move.** Arm A made a
  bold, correct call (75% on a first-ever winner); after the ledger, arm B collapsed it to 2% (the naive
  base rate for a random country). This single over-correction — Brier 0.06 → 0.96 — **accounts for the
  entire A-beats-B gap.** Shown a "you're miscalibrated" signal, the model over-adjusted one item in the
  wrong direction and destroyed a good forecast.

## The methodological catch (unanticipated, and the most useful part)

Both arms' reliability curves look **badly underconfident** — the low bins resolve far higher than
forecast ([0,0.1) resolved ~0.95). But this battery's resolved outcomes are **disproportionately
"surprises"** (marathon sub-2:00, the Knicks after 53 years, Bulgaria's first Eurovision — all a-priori
unlikely, all happened; the NO outcomes are all "the favourite didn't win"). **A perfectly calibrated
forecaster looks underconfident when the sample over-represents low-probability events that resolved
true.** So "underconfident" may be a property of the *battery selection*, not the *model.*

That matters because the ledger's fed-back diagnosis ("you are underconfident, +0.15") was itself
derived from run 15, which was *also* surprise-heavy. So arm B may have been handed a **spurious
signal** — and the model mostly ignoring it was arguably *correct*, while the one time it obeyed (q9) it
was harmed. This is a caution about the ledger **as a feedback source** (distinct from its validated
role as a **measurement instrument**): a Brier/ECE computed on a non-representative resolved sample can
mis-diagnose the *direction* of miscalibration, and feeding that back naively is worse than useless.

## What this establishes

1. **The improvement bet does not pay off in-context (here).** Giving a model its own scored track
   record did not make it better calibrated — the say-vs-do ceiling the whole program documented extends
   to context-feedback, not just instruction. Pre-registered prediction P1 (failure) confirmed, though by
   a different mechanism than predicted (ignore-then-over-correct, not reflexive hedge).
2. **Naive feedback can actively harm.** The one large correction was wrong. So the operational rule is
   the one the pre-registration named for this branch: **correct the miscalibration yourself (the user
   reads the ledger and discounts), do not feed raw scores back to the model** and expect it to self-fix.
3. **The ledger's measurement value is undamaged and is the point.** This run scored 96 forecasts
   judge-free, localised the miscalibration, and surfaced a real sampling subtlety — exactly the auditing
   the instrument exists for. Measurement: validated. In-context improvement: not shown, and hazardous
   naively.
4. **Before trusting the ledger's *diagnosis*, fix its sampling.** A calibration score is only as
   representative as the resolved-forecast sample. The next iteration of the ledger should weight or
   stratify by reference class and base-rate difficulty, so "underconfident" means the model, not the
   question mix.

## Verdict vs pre-registration

- **P1 (failure, slight lean): CONFIRMED** — B not better, marginally worse. Mechanism differed
  (ignore + one over-correction, not reflexive hedge); discrimination held rather than collapsing.
- **P2 (real improvement): not observed** — one item improved (q2), one destroyed (q9), the rest inert.
- **P3 (null / measurement-only): effectively the outcome** — the ledger is a scoreboard, not (here) an
  improvement mechanism; and this run added the caution that naive feedback harms and the diagnosis
  itself can be a sampling artifact.

## Limits

K=4 per arm, one model/tier, single-session proxy for a longitudinal mechanism (the *real* test — log,
wait, resolve, re-forecast months later with an accumulated, representative ledger — only running the
ledger over time delivers, and would also fix the sampling artifact). The fed-back report pooled
opus+haiku from run 15; a per-model report would be cleaner. The q9 over-correction is one item across
4 trials — replicated within this run, but a single question carries the headline, so read the *pattern*
(mostly-ignore + occasional harmful over-correction) rather than the exact Brier delta.
