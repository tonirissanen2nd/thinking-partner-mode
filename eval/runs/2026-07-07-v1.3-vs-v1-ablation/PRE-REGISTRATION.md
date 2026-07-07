# Pre-Registration — v1.3 vs v1 ablation (Track 1)

**Date:** 2026-07-07
**Experimenter:** Claude Code (Opus 4.8). Committed **before any v1.3 response or
judgment is observed.**

## What this run is

A direct A/B of `v1` vs `v1.3` on the same 12-question battery, same roles
(Responder = Opus, Judge ×2 = Haiku, blind). The `v1` responses are **reused
verbatim from the v1.1 ablation** — the same shared baseline as the v1.1 and v1.2
runs, so all three (`v1.1 vs v1`, `v1.2 vs v1`, `v1.3 vs v1`) are directly
comparable. Only v1.3 responses are generated fresh. Both specs archived here.

## What v1.3 changed vs v1.2

Only the **triviality gate** wording. v1.3 narrows it to govern *only* the
confidence phrase and explicitly forbids shortening the answer or dropping context
("completeness is not what this touches"). The **sequencing** change is identical to
v1.2. So any difference between the v1.2-vs-v1 result and this v1.3-vs-v1 result, on
the trivial-fact / downside items, isolates the gate wording change (sequencing is
held constant).

## The question this run answers

Is the triviality gate a **wording problem** or a **prompt-layer ceiling**?

- **Wording problem** → the narrowing recovers the downside completeness v1.2 lost.
- **Ceiling** → the narrowing does not move it; the model over-trims trivial-fact
  answers however the gate is phrased.

## Pre-registered hypotheses

- **H1 (the target):** v1.3 **recovers completeness** relative to v1.2 — on **q7**
  (Berlin Wall) v1.3 does not lose accuracy to v1 (ties or wins, vs v1.2's loss),
  and net **downside accuracy** is no longer v1-favoured (v1.2 was v1 3 / v1.2 1).
- **H2 (retention):** v1.3 keeps the sequencing gains — helpfulness, anti-
  contrarianism, anti-over-caution vs v1 stay broadly as in v1.2 (esp. q3), since
  that wording is unchanged. The trap cells should look like v1.2's (a consistency
  check: if they move a lot, something other than the gate changed).
- **H3 (guard):** no new regression — no accuracy loss on the misframe items
  (q2, q4) beyond what v1.2 showed.

## Outcomes

- **Wording problem confirmed (gate salvageable):** H1 holds — q7 accuracy no longer
  lost, downside accuracy ≥ tie — AND H2 holds. Keep the narrowed gate.
- **Ceiling confirmed (drop the gate):** H1 fails — q7 / downside accuracy still
  v1-favoured despite the narrowing. Then the gate does not earn its place; the
  recommendation becomes remove it, keeping only the (validated) sequencing change.
- **Ambiguous:** movement within noise. Given n=1 and a Haiku judge this is likely;
  weight the q7 cell and the downside-accuracy column, and read against the v1.2 run.

n=1 per question; single family; directional. Do not over-read thin cells.
