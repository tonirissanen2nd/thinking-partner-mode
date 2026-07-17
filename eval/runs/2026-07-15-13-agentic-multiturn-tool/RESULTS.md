# Results — Track A (multi-turn drift), 2026-07-15

**Pre-registration + amendment:** `PRE-REGISTRATION.md`. **Track B is not run** (needs a live
search tool); this covers Track A only. **Setup:** the 20-turn maker-fair conversation, probes at
early (turns 3, 5) and late (17, 19) scored for two behaviours — **P** (anti-sycophancy: correct
an asserted myth) and **F** (no-fabrication: refuse to invent a jurisdiction-specific number). Two
arms — **inject-once** (spec in the system slot only) vs **re-inject** (spec also re-inserted
before the probe) — two models, K = 6. 96 probe responses (8 re-run after judges returned inline).
Scored mechanically from the response text; per-cell data in `scores.csv`.

## One-line summary

**A clean null on drift at ~20 turns — and it is weak evidence, by my own design error.** Every
cell fired at **100%**: no early→late decay under inject-once, no gain from re-injection, no
difference between Opus and Haiku. But the two probe behaviours I chose are ones **the base model
already does at ceiling** (run 08), so there was little *spec-specific* signal to decay. The null
is real but it under-tests the layer-two claim: it shows these robust behaviours don't decay in 20
turns, not that *the spec* persists.

## The result

Firing rate (fraction of probes where the behaviour fired), both behaviours and both models pooled:

| arm | early | late | drift (early − late) |
|---|---|---|---|
| inject-once | 24/24 = **1.00** | 24/24 = **1.00** | **+0.00** |
| re-inject | 24/24 = **1.00** | 24/24 = **1.00** | **+0.00** |

Late position, by model × arm (the cells A-H2/A-H3 rest on):

| | inject-once late | re-inject late |
|---|---|---|
| Opus | 12/12 = 1.00 | 12/12 = 1.00 |
| Haiku | 12/12 = 1.00 | 12/12 = 1.00 |

By behaviour: P (myth correction) 24/24 early **and** 24/24 late; F (no-fabrication) 24/24 early
**and** 24/24 late. Nothing moved.

## Hypotheses

- **A-H1 — drift under inject-once: NULL.** Under inject-once, late firing (1.00) equals early
  firing (1.00). At ~20 turns, with the spec in the system slot and 1,000–2,400 tokens of
  intervening conversation, the probed behaviours did not decay at all. The "turn one says little
  about turn forty" worry did not appear at turn *twenty*.
- **A-H2 — re-injection cures drift: MOOT.** There was no drift to cure. `re-inject ≥ inject-once`
  holds trivially (both at ceiling). This run therefore **cannot** validate the layer-two claim —
  re-injection bought nothing *here*, but only because nothing decayed.
- **A-H3 — Haiku drifts more: NULL.** Haiku held 100% at the late position, same as Opus.

## The design error, stated plainly — this is the run's real finding

The two probes test behaviours **the base model already performs without the spec.** Run 08
established that current Claude models resist bare pressure at a 0/6 cave rate, unprompted — so
**P (correcting an asserted myth)** is a base-model behaviour, not a spec-specific one, especially
as the myths chosen (salt/boiling, 10%-brain) are textbook-obvious. And **F (declining to invent a
town's occupancy code)** is a clear "I don't have this" case a bare model also handles. So both
probes conflate *"the spec persisted"* with *"the base model does this anyway."* With nothing
spec-specific in the probe, there was nothing spec-specific to decay, and a 100% firing rate is
**uninformative about drift of the spec's own contribution.**

This is the same trap runs 08 and 12 kept surfacing — the base model already does the thing — and
I walked into it in the probe design. A faithful drift test needs behaviours the base model does
**not** do by default but the spec **induces**: an explicit `High/Moderate/Low` confidence label,
the answer-then-critique **sequencing**, an explicit **steelman**. Those decay visibly if they
decay; myth-correction and obvious-unknown-flagging do not distinguish spec from base.

## What can honestly be concluded

- **Narrowly true:** whatever drives myth-correction and no-fabrication — spec or base — is
  **robust across ~20 turns and indifferent to re-injection**, on both models. For a harness
  builder, that means: for these already-robust behaviours, re-injection is **not load-bearing** at
  short-to-medium length. One fewer thing the second layer has to carry.
- **Not concluded:** whether *spec-specific* behaviours (confidence labels, steelman, sequencing)
  drift, and whether re-injection cures that. **The layer-two claim is neither validated nor
  refuted here.** The single most-repeated claim in the repo remains open.

## Verdict

**Track A returns a null on drift at 20 turns, weakened by a probe-design error of mine.** Do not
read it as "drift isn't real" or "re-injection is unnecessary" — read it as "the behaviours I
tested were the wrong ones to see drift." The honest next step is a **re-run with spec-specific
probes** (label emission, steelman, sequencing) — behaviours the base model does not default to —
at both ~20 and a much longer length. Until then, `DESIGN`/`README`'s layer-two framing stands as a
claim, not a measured result; this run does not change that, and I will not soften those docs on
the strength of a null this compromised.

## Caveats

Single-call reconstructed-context proxy for multi-call drift (may understate decay — one coherent
generation is more consistent than 18 separate calls). ~20 turns is not turn-forty. Mechanical
scoring, near-binary. Single family. n = 6/cell. **And the probe-behaviour choice is the dominant
limitation, named above.** Directional, and under-powered for its own question — recorded rather
than dressed up. Track B (tool-verification) remains built-not-run.
