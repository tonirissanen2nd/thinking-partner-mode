# Results — ablate the Forecasting section (run 21)

**TL;DR — removing the Forecasting section removes the *form* almost entirely and changes the *accuracy*
not at all.** A clean one-section ablation (run-11 style): full spec vs full-spec-minus-the-Forecasting-
paragraph, everything else identical, on run 15's forecast battery, Claude Opus, K=4, scored judge-free.
The outside-view apparatus collapses **92% → 13%** without the section (and the 13% residual proves that
apparatus comes from the *Forecasting section specifically*, not the Epistemics section that stays); the
resolution-criterion and decomposition markers vanish entirely (38%→0%, 17%→0%). But **Brier is flat**
(0.142 vs 0.145 — noise). **So the Forecasting section is a pure legibility/scorability feature at zero
accuracy cost or benefit.** Answering the question directly: remove it and you lose the scorable,
base-rate-anchored, black-swan-declining apparatus (and the ledger's structured input) while forecast
accuracy stays exactly where it was.

Responder: Claude Opus 4.8, K=4 per arm (52 item-forecasts each). Battery + key = run 15's, verbatim.
Arm **full** = run 15's full-prompt (Priority + Epistemics + Forecasting + Ruin). Arm **minus** =
identical but the `**Forecasting:**` paragraph deleted (Priority + Epistemics — which keeps its *own*
non-estimable clause — + Ruin). Deterministic grading: mechanical apparatus markers + Brier on the 11
resolvable items. Raw in `raw/`.

## The numbers

| Marker / metric | full (with Forecasting) | minus Forecasting |
|---|---|---|
| **base rate / reference class / outside view** | **92%** | **13%** |
| resolution criterion / "scorable" | 38% | 0% |
| decomposition into factors | 17% | 0% |
| non-estimable on the 2 fat-tail items | 0/8 | 1/8 |
| **Brier (11 resolvable items, lower=better)** | **0.142** | **0.145** |

## What it establishes

1. **The Forecasting section *is* the outside-view apparatus — it is not redundant with Epistemics.**
   Base-rate/reference-class framing runs 92% with the section and **13% without it**, even though the
   Epistemics section (which stays in the minus arm) also talks about confidence and non-estimable. So
   run 15's headline — "the spec installs the outside view (85–92% vs 3% bare)" — is now *localised*:
   that apparatus is the Forecasting section's doing, almost entirely. Remove the section and the
   forecasts revert to unanchored numbers with no reference class, no resolution criterion, no
   decomposition — exactly the bare style.
2. **Removing it is accuracy-neutral.** Brier 0.142 (full) vs 0.145 (minus) is noise. This *refines*
   run 15, which found full-spec marginally worse than *bare* on Brier (0.202 vs 0.181): that small gap
   was **not** attributable to the Forecasting section — cutting the section here does not move accuracy.
   So the section adds the scorable apparatus at **zero accuracy cost** (and, symmetrically, zero
   accuracy benefit — consistent with the program's finding that the prompt installs *form*, not
   prescience).
3. **The real cost of removal is downstream: scorability and the ledger.** The section is the
   *precondition* for the forecast ledger (built and tested in run 20, since retired) — the ledger needs a numeric probability with a
   resolution criterion to log and score, and run 15 was "the rung before the ledger." Remove the
   section and forecasts stop being reliably scorable (resolution-criterion 38%→0%), which starves the
   ledger's structured input and forfeits the auditability that is the project's most valuable remaining
   direction. **Accuracy: unchanged. Auditability: lost.**

## Honest sub-finding (noisy, don't over-read)

The non-estimable refusal on the two fat-tail items barely fired in *either* arm here (full 0/8, minus
1/8) — unlike run 15, where full-opus declined ~67% on the AGI item. With only 8 fat-tail forecasts per
arm and a smaller preamble than run 15's, this is trial variance, not a clean signal. What it does show:
the Epistemics section's *own* non-estimable clause (present in the minus arm) is at least as likely to
fire as the Forecasting section's black-swan exception — so the non-estimable behaviour is not uniquely
the Forecasting section's, and neither clause fired reliably on this pass. A dedicated fat-tail battery
would be needed to isolate it.

## Verdict — should you remove it?

**Only if you do not want scorable, auditable forecasts.** The ablation says the section costs nothing in
accuracy, so a user who only wants a raw probability loses nothing measurable by cutting it — and gains a
little brevity (no base-rate/decomposition prose). But a user who wants forecasts that a **ledger** can
score over time, or that carry an explicit reference class and resolution criterion, should keep it: it
is the single clause that installs all of that, and nothing else in the spec supplies it. It is form, not
accuracy — and form is exactly what the ledger's back half needs.

## Limits

K=4, one model/tier, single battery (run 15's 13 items). Mechanical markers inherit the frozen keyword
lists. The non-estimable sub-finding is n=8/arm and noisy. Brier on 11 items is directional. "minus" is
full-spec-minus-one-paragraph, not "bare" — the comparison isolates the Forecasting section, not the
whole spec.
