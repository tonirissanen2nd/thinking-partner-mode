# Pre-Registration — lean-Epistemics vs full ablation (Track 1)

**Date:** 2026-07-07
**Experimenter:** Claude Code (Opus 4.8). Committed **before any response or
judgment is observed.**

## What this run is

A direct A/B testing whether the dense Epistemics paragraph earns its length.
`full` = v1's `SPEC.md` (`spec-full-v1.md`). `lean` = the same spec with the
Epistemics paragraph cut to a short core (`spec-lean.md`): confidence
labels-anchored-to-basis, do-not-fabricate/flag load-bearing facts, name
omissions. **Removed in lean:** the "how could this be wrong" High gate, the
fat-tail demotion rule, the estimable/non-estimable distinction, the decisiveness
clause, "what evidence would change this." Everything else in the spec — including
the **Forecasting** and **Ruin/irreversibility** sections — is identical.

**Purpose-built battery** (`battery.md`), NOT the ordinary 12-question one: 3
fat-tailed/non-estimable (F), 3 irreversibility/ruin (R), 3 hidden-failure-path (H),
3 ordinary factual controls (C). The first three groups are exactly where the
removed machinery claims to matter; the controls are where lean should suffice.

Responder = Opus (both conditions, fresh); Judge ×2 = Haiku, blind. n=1 per
question; single family; directional.

## Why this battery, and the interpretation caveat

The original Track-2 null found the full machinery redundant with a generic
instruction — but only on *ordinary* facts, which is exactly where the machinery
is NOT aimed. This battery aims at the machinery's claimed job. **Caveat:** lean
still keeps the Forecasting and Ruin sections, so a null on F/R items could mean
either "the Epistemics tail machinery adds nothing" OR "it is redundant with the
Ruin/Forecasting sections that lean retains." Both are reportable; the run cannot
distinguish them by itself.

## Pre-registered hypotheses

- **H1 (the machinery earns its keep):** on F, R, H items, `full` beats `lean` on
  **accuracy (A)** and/or **calibration (B)** — full surfaces the non-estimable/
  fat-tail framing (F), names the ruin path (R), or catches the hidden failure (H)
  where lean gives a more confident, less-hedged, or less-complete answer.
- **H2 (no free lunch on controls):** on C items, `full` and `lean` are
  indistinguishable (ties) — the machinery neither helps nor hurts where there is
  no tail. If `full` *loses* controls (e.g. over-hedging a simple fact), that is a
  cost of the density.
- **H3 (the lean upside):** if H1 fails (full ≈ lean on F/R/H too), then the dense
  paragraph is not earning its length on this battery — evidence for the leaner
  variant (same behaviour, shorter, more salient, cheaper).

## Outcomes

- **Machinery justified:** H1 holds on ≥2 of the three stress groups → keep the
  dense Epistemics; the length buys tail behaviour a short core misses.
- **Lean wins on value density:** H1 fails (full ≈ lean on F/R/H) AND H2 holds →
  the dense paragraph is largely redundant here; the lean core is a strict
  improvement (same behaviour, shorter). Subject to the Forecasting/Ruin caveat.
- **Mixed:** full helps on some stress groups but not others → keep the parts that
  fire, cut the rest.

n=1, single family, Haiku judge — directional. Weight accuracy/calibration on the
F/R/H items; read controls for over-hedging cost.
