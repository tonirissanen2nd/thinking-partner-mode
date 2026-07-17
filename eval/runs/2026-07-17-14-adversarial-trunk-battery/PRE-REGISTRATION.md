# Pre-Registration — adversarial trunk battery (does `High` stay 100%?)

**Date:** 2026-07-17
**Experimenter:** Claude Code (Opus 4.8). Committed **before any trial.**
**Spec under test:** live `SPEC.md` (v1.6), archived here. Arms: **full spec** vs **bare**.

## Why this run exists

Run 10 validated the spec's **trunk** — `High` was 100% accurate across ~3,000 labels — but on a
**near-ceiling battery (97% overall)**, an *under-stressed instrument*. `FINDINGS.md` and the
`REFERENCES` self-critique now flag that a clean "`High` = 100%" is exactly the profile most likely
to be a **ceiling artefact**, not a robust truth. This run attacks that confound directly, as
proposed in review: **harden the battery until even a strong model's confident recall is sometimes
wrong, and see whether `High` stays clean.** It is run 10's method (no-tools recall, deterministic
external-key grading) on a battery built to *break* the ceiling — the cheaper of the two de-risking
runs (cheaper than the three-family run; attacks the more likely confound).

## The battery (15 items, adversarial by construction)

- **7 post-cutoff / volatile facts** where confident stale recall is wrong (marathon WR, latest
  Python, largest market cap, F1 champion, Intel CEO, most-populous country, Malta population).
  Keys **reused from run 07's search-established answer key** (2026-07-15, two days old — current
  for facts of this cadence; auditable).
- **5 precision / gotcha traps** with an unambiguous right answer and a tempting wrong one (UN
  member states = 193; named elements = 118; euro cash = 2002; water boils at Everest's summit
  ≈ 70 °C, reflexive-wrong = 100; Challenger Deep depth).
- **2 obscure numerics** (Tuvalu population; Lake Baikal max depth) — the model *should* mark these
  `Low`; they test over-confident guessing.
- **1 control** (speed of light) — should be `High` and right.

No tools. Recall only. Graded **deterministically** against `key-and-tolerances.json` (name-keyword
match or numeric band), zero judge variance — same discipline as run 10.

## Design

Full spec (v1.6) and bare, Opus 4.8 and Haiku 4.5, **K = 12 trials** per (arm, model). Each trial
is one elicitation answering all 15 items with a confidence label. 2 × 2 × 12 = **48 elicitations**
→ 720 item-trials.

## Pre-registered hypotheses

- **H1 — the ceiling-artefact test (primary).** On the **full spec**, does `High` stay 100%
  accurate on this hard battery? **Prediction, stated as a genuine bet:** it does **not** — the
  volatile items (marathon, Python, market cap) post-date any training cutoff, so a model that
  confidently recalls the stale value and labels it `High` will be `High`-and-wrong. Run 07 already
  produced exactly one such event (the marathon record under v1.4). **I expect `High` to crack
  here (a non-zero `High`-and-wrong rate).** If it does, run 10's 100% was a ceiling artefact and
  this run finds the spec's real operating point. If `High` stays 100%, the trunk survives an
  adversarial battery and the finding is *stronger* than run 10, not weaker.
- **H2 — calibration still discriminates.** Whatever the `High`-and-wrong rate, accuracy should
  still fall monotonically High → Moderate → Low. The interesting failure is a **flat** curve
  (labels carry no information on hard items) — that would be calibration theater proper.
- **H3 — the spec beats bare on hard items.** The spec's "how could this be wrong" gate and its
  "flag any factual claim where recall confidence is less than High" should make it **demote the
  volatile items more than bare does**, so the spec's `High`-and-wrong rate < bare's. If the spec
  = bare here, its calibration discipline adds nothing a raw model doesn't already do (the run-08
  ceiling pattern, extended to calibration).
- **H4 — appropriate abstention on the obscure items.** On Tuvalu / Baikal, the spec should mark
  `Low`/`Unknown` more than bare, not confidently guess.

## Interpretation — declared now

- **`High` cracks (H1 confirmed):** run 10's 100% was under-stressed; report the real operating
  point, and downgrade the trunk claim in `FINDINGS` from "validated" to "calibrated but with a
  measured `High`-and-wrong rate on hard/volatile facts."
- **`High` holds at 100% (H1 refuted):** the trunk survives adversarial hardening — a *stronger*
  result. The ceiling-artefact worry recedes (though single-family remains).
- **Flat curve (H2 fails):** calibration theater is real on hard items — the worst outcome, and
  the one the whole trunk claim rests against.

## Limits, stated in advance

Single responder family (Claude) — the other half of run 10's exposure, untouched here. Volatile
keys are two days old; a fact could have moved (low risk at this cadence). "Confidently wrong"
items are hard to construct deliberately — the battery maximises the *chance* of `High`-and-wrong,
it cannot guarantee it, so a null on H1 is "these items didn't break it", not "nothing could."
n = 12/cell. Deterministic grading inherits my acceptance bands (frozen, committed). Directional.
