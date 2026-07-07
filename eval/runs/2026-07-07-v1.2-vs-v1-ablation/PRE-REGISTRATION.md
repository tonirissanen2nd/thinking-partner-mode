# Pre-Registration — v1.2 vs v1 ablation (Track 1)

**Date:** 2026-07-07
**Experimenter:** Claude Code (Opus 4.8). Committed **before any v1.2 response or
judgment is observed.**

## What this run is

A direct A/B of `v1` vs `v1.2` on the **same 12-question battery**, same roles as
the two prior ablations (Responder = Opus, Judge ×2 = Haiku, blind). Both specs
archived here (`spec-as-tested-v1.md`, `spec-as-tested-v1.2.md`).

**Design choice — shared v1 baseline.** The `v1` responses (and their normalized
forms) are **reused verbatim from the v1.1 ablation**, holding v1 constant across
both ablations. This makes "v1.1 vs v1" and "v1.2 vs v1" directly comparable
item-by-item: the v1.1 ablation charged v1.1 a trap-accuracy cost (v1 2 / v1.1 1,
losses on q3 and q7); this run asks whether v1.2 removes that cost against the
*same* v1 answers. Only v1.2 responses are generated fresh.

## What v1.2 changed vs v1.1 (the counter-counterweights under test)

1. **Sequencing:** leading with the deliverable must **not** abbreviate the
   critique — surface the load-bearing failure mode with full weight, after the
   deliverable. (Targets q3: v1.1 led with the script but caught the structural
   flaw less fully.)
2. **Triviality gate:** drop the confidence *label*, not *substance* — keep a brief
   clarification that resolves a genuine ambiguity. (Targets q7: v1.1's bare
   "1989." dropped the "what does 'the fall' mean" context.)

## Pre-registered hypotheses

- **H1 (retention):** v1.2 **keeps** v1.1's gains vs v1 — still less contrarian
  (axis C), more helpful (axis D), and less over-cautious (axis E), broadly and on
  q3 specifically. If v1.2 has snapped back to v1's behaviour on these, the
  counter-counterweight over-corrected.
- **H2 (the target):** v1.2 **closes the accuracy cost** — on **q3** and **q7**,
  v1.2 does **not** lose accuracy to v1 (it ties or wins), and net trap accuracy is
  at least tied (no longer v1-favoured 2–1). This is the specific thing v1.2 was
  built to fix.
- **H3 (guard):** no new regression — v1.2 does not lose accuracy on the misframe
  items (q2, q4) and is not more over-cautious anywhere than v1.

## Outcomes

- **Success (clean win):** H1 holds (gains retained) AND H2 holds (accuracy no
  longer lost on q3/q7, net trap accuracy ≥ tie) AND H3 holds. → v1.2 is a
  candidate to promote: it beats v1 on the located costs with no accuracy price.
- **Partial:** gains retained but accuracy still lost (counter-counterweight
  insufficient), OR accuracy fixed but gains eroded (over-corrected). Either is
  informative and reportable.
- **Failure:** gains lost *and* accuracy still lost — the v1.2 edit made things
  worse.

**Judge agreement:** an axis counts for a condition only when **both** Haiku judges
agree; else "contested". n=1 per question, single family, directional — do not
over-read thin columns; weight the q3/q7 accuracy cells and the decisive
helpfulness column.
