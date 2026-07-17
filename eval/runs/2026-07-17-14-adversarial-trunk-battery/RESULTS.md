# Results — adversarial trunk battery (run 14)

**TL;DR — H1 confirmed: `High` cracked, and *where* it cracked is the whole finding.** On a battery
built to break the ceiling, the full spec's `High` is **91% accurate (112/123), not 100%** — so run
10's clean 100% *was* an under-stressed-battery artefact, exactly as the outside-view discount in
`FINDINGS.md` predicted. But the crack is confined to one class: **`High` stayed 100% on stable,
knowable facts (82/82 full, 84/84 bare — zero wrong)** and leaked *only* on **post-cutoff volatile
facts the model recalls confidently and stale.** The calibration curve stayed monotone under stress,
and the spec cut the confidently-wrong rate versus bare in **both** models. The trunk is not broken;
its real operating point is now measured.

Method: run 10's (no-tools recall, deterministic external-key grading). 4 cells (full/bare ×
Opus/Haiku), K=10, 15 items = 600 item-trials. Grading in `key-and-tolerances.json`; per-trial
answers in `raw/trials/`; graded rows in `graded.json`.

---

## The reliability curves (pooled models)

| Confidence | Full spec | Bare |
|---|---|---|
| **High** | **112/123 = 91%** | 119/136 = 88% |
| **Moderate** | 89/128 = 70% | 92/138 = 67% |
| **Low** | 24/47 = 51% | 12/25 = 48% |

Both curves are **monotone** (High > Moderate > Low). H2 holds: even on a battery hard enough to
break `High`, the labels still carry real information — this is *not* calibration theater (a flat
curve). The interesting failure the pre-registration named did not occur.

Per cell, the model split dominates:

| Cell | High acc | High-and-wrong |
|---|---|---|
| full-opus | **58/60 = 97%** | 2 |
| bare-opus | 58/63 = 92% | 5 |
| full-haiku | 54/63 = 86% | 9 |
| bare-haiku | 61/73 = 84% | 12 |

## Where `High` cracked — and where it held

Split the 15 items by class:

- **Stable knowable facts (5 gotcha + 1 control): `High` = 100%, both arms.** 82 full / 84 bare
  `High` labels, **zero wrong.** The UN-193 / 118-elements / euro-2002 traps were all marked `High`
  and right. The reflexive-**100 °C** boiling-point trap **caught no one** — both arms answered
  ~70 °C and correctly hedged it (0/20 `High`, 100% accurate). Run 10's trunk result reproduces
  perfectly on this half of the battery.
- **Post-cutoff volatile facts (7): every single `High`-and-wrong event lives here** — and almost
  all are the three facts that genuinely moved after the model's cutoff: the **marathon WR** (the
  model confidently "knows" Kiptum 2:00:35; the real holder is Sawe, 1:59:30), the **Python
  version** (3.13 vs 3.14), and the **F1 champion** (Verstappen vs Norris). The model has *no
  internal signal* that its recall is stale, so the "how could this be wrong" gate cannot fire —
  this is the confidently-wrong regime, the prompt-layer ceiling `DESIGN.md` predicts, caught
  red-handed.
- **The cutoff boundary is visible in the data.** "India is the most populous country" (a change
  old enough to be internalized) was `High`-and-right **20/20 in both arms** — while the marathon
  record (a change too recent) was `High`-and-wrong. Same item type, opposite outcome, split by
  whether the fact's change predates the model's training. That boundary *is* the operating point.

## H3 — the spec beats bare on the demotion that matters (confirmed, both models)

The volatile-7 items are the demotion test: does the spec's calibration discipline mark
confidently-stale facts `High` *less* than a raw model does?

| Cell | Volatile answers marked `High` | of those, wrong |
|---|---|---|
| full-opus | 13/70 | **2** |
| bare-opus | 15/70 | 5 |
| full-haiku | 19/70 | **9** |
| bare-haiku | 22/70 | 12 |

In **both** models the spec demoted volatile facts more and cut the confidently-wrong count
(Opus 5→2, Haiku 12→9). This is the calibration trunk doing real work under adversarial load — not
a null, and not a ceiling. It is a **partial** fix, not a complete one: the residual (the marathon,
above all) is the hardest case, where the model is simply certain and wrong and no wording reaches it.

## H4 — abstention on the obscure items (directional support)

On Tuvalu / Baikal the spec pushed labels down: `High` **9 (full) vs 15 (bare)**, more mass on
`Moderate`. The spec abstains from confident recall on genuinely obscure numerics more than bare
does — the safe direction.

---

## What this run establishes, stated precisely

1. **Run 10's "`High` = 100%" was real but conditional.** It holds unconditionally on **stable,
   knowable facts** (reconfirmed here, 100% on the stable subset). It **does not** hold on
   **post-cutoff volatile facts under no-tools recall**, where the model can be confidently stale.
   The honest operating point for the full spec is **`High` ≈ 91% pooled (97% Opus / 86% Haiku)**
   on a battery that deliberately mixes in facts that moved after cutoff.
2. **The failure is exactly the one the spec's own Verification section exists to catch** — and
   this run shows *why that section needs tools to work.* The directive says to flag any factual
   claim below `High` recall and verify load-bearing facts against a primary source. Under no-tools
   recall the flag is the only defence, and it is structurally imperfect: **the model cannot flag
   staleness it has no signal for.** So the marathon record leaks through as `High`. This is not a
   spec defect; it is the boundary the spec draws — and the direct argument for **layer two doing
   the verification the recall layer cannot** (`HARNESS.md`).
3. **The calibration discipline measurably helps, even where it cannot fully win.** Monotone curve
   under stress; spec < bare on confidently-wrong in both models; more abstention on obscure items.
   The trunk survives adversarial hardening as a *discriminating instrument*; only the *unconditional*
   100% claim does not survive.

## Verdict against pre-registration

- **H1 (primary): CONFIRMED.** `High` did not stay 100%; it fell to 91% pooled. Per the
  pre-committed interpretation, this **downgrades the `FINDINGS.md` trunk claim** from an
  unconditional "validated / 100%" to "**100% on stable facts; ~91% once post-cutoff volatile facts
  are included, with the residual concentrated in the confidently-stale regime the Verification
  section flags for tools.**" `FINDINGS.md` updated accordingly.
- **H2: HELD.** Curve monotone under stress; no calibration theater.
- **H3: CONFIRMED (directional, both models).** Spec's `High`-and-wrong < bare's (11 vs 17 pooled).
- **H4: SUPPORTED (directional).** More abstention on obscure items under the spec.

## Limits

Single responder family (Claude) — untouched, still the standing debt. Volatile keys are two days
old (run 07's search-established set). K=10/cell, directional. Deterministic grading inherits the
frozen acceptance bands in `key-and-tolerances.json`. The battery *found* a crack, which answers the
question asked; a different hard battery could find a different operating point, so read 91% as "the
level this battery revealed," not a universal constant.
