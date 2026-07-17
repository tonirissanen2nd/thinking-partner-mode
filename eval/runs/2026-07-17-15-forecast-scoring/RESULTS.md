# Results — forecast scoring (run 15, the rung before the ledger)

**TL;DR — the Forecasting section is validated on *form*, not on *accuracy*, and that split is the
finding.** The spec makes the model produce **scorable, base-rate-anchored forecasts** where bare
gives a bare number: explicit outside-view apparatus **85% vs 3%** of forecasts (92% vs 26% even
counting implicit base-rate reasoning), and it correctly declines a point estimate on the one genuine
black swan (**AGI: non-estimable 67% vs 0%**). But it does **not** improve calibration accuracy —
Brier **0.202 (full) vs 0.181 (bare)**, marginally *worse* — because on genuine post-cutoff surprises
both arms are ceiling-bound, and on knowable items the spec's outside-view caution drags confident-
correct recall toward 50%. **The spec makes forecasts scorable, not prescient** — which is precisely
the argument that the accuracy loop needs a *ledger* (real-world scored feedback), not a better prompt.
This is the first evaluation of the spec's Forecasting section, previously the largest unvalidated
surface.

Method: full spec (Forecasting + Epistemics + Ruin clauses) vs bare, Opus 4.8 / Haiku 4.5, K=6, 13
items (11 resolvable + 2 fat-tail) = 312 item-forecasts. Outcomes established by search 2026-07-17 or
reused from run 07's key (`key-outcomes.json`). Track A markers are **mechanical** (regex, judge-
independent); Track B is deterministic Brier against the frozen outcome key. Grader in `graded.json`.

---

## Track A — forecast well-formedness (primary; H1 CONFIRMED)

Share of the 156 forecasts per arm carrying each marker:

| Marker | Full | Bare |
|---|---|---|
| Numeric probability emitted | 99% | 100% |
| **Explicit outside-view apparatus** ("base rate" / "reference class" / "outside view") | **85%** | **3%** |
| — any base-rate-flavored reasoning (loosest count, incl. implicit) | 92% | 26% |
| Decomposition into factors | 9% | 0% |
| Ruin / exposure framing | 6% | 0% |
| Resolution criterion restated | 9% | 3% |

- **The dominant, robust effect is the outside view.** The spec makes the model *name a reference
  class and base rate* on 85% of forecasts and label it explicitly; bare does so on 3%. This is **not
  a keyword artifact** — bare genuinely reasons from base rates implicitly (~26%: "annual release
  cadence", "post-halving cycle"), but the spec turns that sporadic, unlabeled habit into a
  **consistent, explicit, labeled outside-view-before-inside-view discipline** (92% vs 26% even at the
  loosest). This is the single behavior the Forecasting section most directly prescribes, and it fires.
- **Numeric probability is a base-model default, not a spec effect** — bare already gives a number
  100% of the time (the run-08 ceiling pattern: the model does this unprompted). The spec's value is
  *not* "makes it give a number"; it is "anchors the number to a named base rate."
- **Two honest sub-nulls.** Decomposition (9%) and ruin-framing (6%) are real but *rare* under the
  spec — it decomposes and names exposure only on a minority of items (mostly the fat-tail ones).
  And the **resolution-criterion** marker is a genuine null (9% vs 3%, both low): the spec does *not*
  reliably restate a scorable resolution criterion beyond the window the question already supplied.
  So "states it as a scorable claim" is validated on the *probability + base rate* half and **not** on
  the *explicit resolution criterion* half.

## H3 — non-estimable discipline on the fat-tail items (CONFIRMED, and selective)

| Fat-tail item | Full: non-estimable | Bare: non-estimable |
|---|---|---|
| q13 — transformative AGI before 2028 | **8/12 (67%)** | 0/12 |
| q12 — single-day US market crash > 20% in 24mo | 2/12 | 0/12 |

- **AGI (q13): the clean spec win.** The spec declines a point estimate two-thirds of the time,
  correctly identifying a contested-definition, no-prior-instance target the reference class cannot
  bound; bare *always* gives a spurious number (10–25%). This is the Epistemics `non-estimable` rule
  firing exactly as designed, and it is a behavior bare does not have.
- **Crash > 20% (q12): the spec correctly *did not* refuse.** Full gave a point estimate (~4%) on the
  crash item in 10/12 trials — and this is *right*, not a failure: as the responses reasoned, the
  reference class *does* bound this tail (one instance in 40+ years, and post-1987 circuit breakers
  mechanically halt trading at −20%), so a small point estimate is defensible and the spec's
  non-estimable exception should *not* fire. The spec **discriminated** between the genuine black swan
  (AGI → refuse) and the structurally-bounded tail (crash → estimate + a ruin/exposure note). That
  selectivity is the sophisticated-correct behavior, not blanket refusal.

## Track B — calibration accuracy (secondary, underpowered; H2 = ceiling-bound, slight cost)

Brier score (lower = better) on the 11 resolvable items:

| | Overall | Base-rate items | Surprise items |
|---|---|---|---|
| **Full** | 0.202 | 0.135 | 0.320 |
| **Bare** | **0.181** | **0.106** | 0.313 |

Per cell: full-opus 0.155 vs bare-opus 0.149 (tie); full-haiku 0.249 vs bare-haiku 0.213.

- **The spec did not improve accuracy — it is marginally worse.** The gap (0.02) is within the noise
  this underpowered battery (n=11 questions) was pre-registered to treat as directional, so the honest
  read is **"no calibration-accuracy benefit, and a possible small cost"** — the H2 branch named in
  advance ("outside-view anchoring drags confident-correct recall toward 50%") partially materialised.
- **The cost is visible in the texture.** On items the model actually *knew*, bare gave the more
  confident-correct probability and the spec's outside-view caution pulled it toward 50%: Nvidia-#1
  (outcome YES) full 66 vs bare 72; Intel-new-CEO (YES) full 63 vs bare 73; Malta->540k (YES) full 57
  vs bare 66. The very discipline that *helps* on recall (run 14: demote volatile facts) slightly
  *hurts* on forecasts of things the model reliably knew, by over-applying the outside view.
- **On genuine surprises both arms are ceiling-bound** (Brier ~0.32 both): the marathon sub-2:00
  record broke (outcome YES) and both forecast ~10%; Verstappen lost the 2025 title (outcome NO) and
  both forecast ~52%. Neither arm can forecast a post-cutoff change it has no signal for — the run-14
  confidently-stale finding, transposed from recall to forecasting. **No prompt reaches this.**

---

## What this run establishes

1. **The Forecasting section is validated — on well-formedness.** It reliably installs the outside
   view (explicit base rate + reference class, 85% vs 3%), correct non-estimable refusal on the true
   black swan (67% vs 0%), and — more weakly — decomposition and ruin-framing. It makes the model's
   forecasts **scorable and legible**. That is the section's actual, prompt-layer-reachable claim, and
   it holds on both models. Before this run the section was entirely unvalidated; it now has form-level
   support.
2. **It does not make forecasts more accurate — and slightly costs accuracy.** Brier is marginally
   worse (0.202 vs 0.181). Accuracy is bounded by what the model knows (ceiling on surprises) and is
   even mildly *degraded* by outside-view caution where the model knew the answer. Well-formedness is a
   prompt-layer property; forecast accuracy is not — the exact ceiling `DESIGN.md` predicts, now shown
   for judgment as run 14 showed it for recall.
3. **This is the ledger argument, made concrete.** The spec is the necessary *front half* of the loop
   Tetlock credits: it makes forecasts scorable, which is the precondition for scoring them against
   reality. But scoring is what improves calibration, and scoring requires a **forecast ledger** —
   persistent, resolved-outcome feedback (`HARNESS.md`) — not a better prompt. Run 15 validates the
   precondition and, by finding form-without-accuracy, confirms the ledger is *necessary*, not
   optional. The rung is climbed: the ledger can now be built on a section shown to emit scorable
   forecasts — while knowing the prompt alone will not deliver the accuracy the ledger exists to earn.

## Verdict against pre-registration

- **H1 (well-formedness): CONFIRMED** — explicit outside-view apparatus 85% vs 3%; non-estimable
  refusal on AGI 67% vs 0%. (Sub-null: resolution-criterion restatement is *not* a spec win.)
- **H2 (calibration): as predicted — ceiling-bound, with the pre-named slight cost.** Brier marginally
  worse, not better; surprise items ceiling-bound on both arms; the "outside-view drags confident
  recall toward 50%" cost partially materialised.
- **H3 (non-estimable): CONFIRMED, and better than expected** — the refusal was *selective and
  correct* (AGI refused, structurally-bounded crash estimated), not a blanket rule.

## Limits

Single responder family (Claude). **Track B is underpowered** (11 questions) — Brier differences of
~0.02 are directional, not decisive. Per-item recall-vs-forecast status is uncontrolled: some 2025
events fall inside a responder's cutoff (partial recall), while Feb-2026 items (Super Bowl LX) are
cleanly post-cutoff — the battery mixes both. Mechanical Track-A markers detect *explicit* framing;
the loose-vs-strict re-scan (92/26 vs 85/3) is reported so the well-formedness claim does not rest on
one keyword list (the run-13 lesson). K=6/cell. Outcome key frozen and sourced in `key-outcomes.json`.
