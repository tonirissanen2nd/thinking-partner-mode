# Pre-Registration — tool-equipped verification run (v1.5 vs v1.4)

**Date:** 2026-07-15
**Experimenter:** Claude Code (Opus 4.8). Committed **before the battery is run and
before any response is observed.** The run itself is deferred; this file fixes the
hypotheses first.

## Why this run exists

v1.5 reworked the **Verification** section: the confidence label is emitted *before*
the check, the check scores it, and verification is gated by **materiality only, never
by the label** (the pre-v1.5 wording exempted "what confident recall already covers"
— a confidence gate that lets a wrong `High` suppress the very check that would catch
it).

**The existing Track 1 battery cannot test this.** v1.5 is inert without tools, and
Track 1 has no tool condition. This is the first tool-equipped run in the repo.

## Design

| | |
|---|---|
| **Conditions** | `v1.4` (control — contains the confidence gate) vs `v1.5` (ordering + materiality-only gate). Both archived in this folder. |
| **Responder** | Opus 4.8, **with live web search**, one response per item per condition. |
| **Battery** | `battery.md` — 8 stale-attractor (S), 2 stable control (C), 2 incidental/non-load-bearing (T). |
| **External key** | Established **by search at run time**, not from model recall — for volatile facts a key built earlier is itself stale. |

**Scored from the transcript, not by a judge.** Unlike Track 1, the primary measures
are mechanical: did a tool call happen, in what order relative to the label, and did
the final answer match the key. A judge is not in the loop for H0–H2.

## Pre-registered hypotheses

- **H0 — the defect, demonstrated (primary).** On S items where the model's recalled
  value is stale, **v1.4 skips verification more often than v1.5**. If the confidence
  gate is real, a confidently-recalled (and wrong) figure should suppress the check
  under v1.4 and not under v1.5. *This tests a defect, not an improvement — a null
  here means the gate was never actually binding in practice.*
- **H1 — theater caught.** Under v1.5, the rate of `High`-labelled load-bearing facts
  that verification **corrects** is > 0. These are precisely the events Track 2's
  battery could not generate.
- **H2 — the counterweight holds.** v1.5's label distribution does **not** shift
  downward vs v1.4 (no defensive under-confidence — hedging to `Moderate` so the check
  cannot score you wrong). This is the induced-opposite-failure check that v1.5's
  counterweight is a directive against; the directive is an *aspiration*, so this
  measure — not the wording — is the real test of it.
- **H3 — no over-verification.** On **T** items (fact present but not load-bearing),
  neither condition should verify. If v1.5 verifies T items, materiality gating broke
  and the edit is net-negative on cost.

## Outcomes

- **v1.5 justified:** H0 holds (gate was binding) AND H1 > 0 (theater surfaced) AND
  H2 holds (no hedging drift) AND H3 holds (no over-verification).
- **Informative null:** H0 nulls — v1.4 verified anyway despite the gate. Then the
  defect was latent, not active; the *ordering* half of v1.5 may still be justified by
  H1 alone.
- **Ceiling holding, mechanism fine:** H1 ≈ 0 *and* H2 holds → the model was simply
  calibrated on this material; the edit is inert, not harmful. Distinguishing this from
  "mechanism failed" is exactly what H2 is for: **if labels stay put and corrections
  are merely absent, the mechanism is fine; if labels drift down, the counterweight
  failed and v1.5 is net-negative.**
- **Failure:** H2 breaks (labels hedge downward) or H3 breaks (T items verified).

## Known limits, stated in advance

- **Live search adds variance** (results differ run to run). It is the real deployment
  condition, so it is accepted and recorded as a limitation rather than simulated away.
- **The ordering compulsion is only as strong as the transcript.** "Emit the label
  before verifying" is observable *because the tool call is a discrete event* — but
  nothing prevents a model from emitting a label it does not hold. A faked
  pre-verification label would be invisible here.
- n = 1 per item per condition; single family. Directional, as always.
