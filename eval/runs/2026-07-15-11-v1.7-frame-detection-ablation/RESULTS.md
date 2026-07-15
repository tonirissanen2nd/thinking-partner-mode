# Results — v1.7 (frame-detection) vs v1.6 ablation, Opus 4.8 × Haiku 4.5, 2026-07-15

**Pre-registration:** `PRE-REGISTRATION.md`, committed before any response.
**Isolated change:** v1.7 = v1.6 + one section, `Register` (single-insertion `diff`; both specs
archived). **Setup:** run-9's 12-item battery (6 trap T1–T6, 6 downside D1–D6) × 2 arms × 2
models = 48 responses, blind A/B by two judge families (both-must-agree → else contested),
**plus** a judge-independent mechanical count of apparatus markers. Raw data in `raw/`.

## One-line summary

**The idea works; this wording of it is not shippable as written.** `Register` does exactly what
it was built to do on the downside block — v1.7 is markedly **more helpful (D 6–1) and less
over-contrarian (C 4–1)**, and the mechanical marker count confirms the gate physically fires
(Opus apparatus on downside items: **19 → 4**). But it also **tripped the pre-registered revert
trigger**: on Opus traps, v1.7 lost accuracy (0–3) and calibration (0–2) among the judges'
agreements. Reading those responses, the loss is **marginal completeness, not a missed trap** —
v1.7 caught every trap with full apparatus — but I committed in advance to "revert if v1.7 loses
trap A or B," and it did. **v1.7 is not promoted. The live spec stays v1.6.** The finding is that
the counterweight needs to protect trap *completeness*, not just trap *apparatus* — a sharper
re-wording, not a dead end.

## The results

Reading key: on **trap** items, a **v16** win on A/B means v1.7 *regressed* (bad). On **downside**
items, a **v17** win on C/D means the fix *worked* (good). Both judges must agree or the cell is
contested.

**Trap (T1–T6), both models pooled — the counterweight test:**

| axis | v17 | v16 | tie | contested |
|---|---|---|---|---|
| A accuracy | 1 | **3** | 1 | 7 |
| B calibration | 1 | **2** | 3 | 6 |
| C over-contrarianism *(less=better)* | 2 | 2 | 3 | 5 |
| D helpfulness | 3 | 4 | 1 | 4 |
| E over-caution *(less=better)* | 2 | 0 | 4 | 6 |

**Downside (D1–D6), both models pooled — the benefit:**

| axis | v17 | v16 | tie | contested |
|---|---|---|---|---|
| A accuracy | 2 | 1 | 0 | 9 |
| B calibration | 2 | 2 | 4 | 4 |
| C over-contrarianism *(less=better)* | **4** | 1 | 5 | 2 |
| D helpfulness | **6** | 1 | 0 | 5 |
| E over-caution *(less=better)* | 1 | 1 | 7 | 3 |

**By model, key axes:**

| | Opus | Haiku |
|---|---|---|
| Trap A (v17/v16/tie/contested) | **0 / 3** / 0 / 3 | 1 / 0 / 1 / 4 |
| Trap B | **0 / 2** / 2 / 2 | 1 / 0 / 1 / 4 |
| Downside C | 3 / 0 / 2 / 1 | 1 / 1 / 3 / 1 |
| Downside D | 3 / 1 / 0 / 2 | 3 / 0 / 0 / 3 |

**Mechanical apparatus markers (confidence labels + caveats + pushback phrases):**

| | Opus downside | Haiku downside | Opus trap | Haiku trap |
|---|---|---|---|---|
| v1.6 | 19 | 8 | 19 | 7 |
| v1.7 | **4** | 6 | 13 | 11 |
| mean words (downside) | 371 → **267** | 197 → 176 | 734 → 655 | 364 → 378 |

## Hypotheses

**H1 — the benefit: HOLDS, clearly.** On downside, v1.7 wins helpfulness **6–1** and
over-contrarianism **4–1** (pooled), and loses neither on either model. The gate does what run 9
asked for: it stops bringing the analytical apparatus to questions that wanted a direct, warm, or
committed answer. On Opus the effect is large; on Haiku it is present on helpfulness (3–0) and
neutral on contrarianism (Haiku deployed little apparatus to begin with).

**H2 — no trap regression (PRIMARY): FAILS on Opus, by the letter, and the letter is what I
pre-registered.** Among the judges' agreements, Opus traps went to v1.6 on accuracy (3–0) and
calibration (2–0). I committed in advance: "if v1.7 loses trap A or B, `Register` is a
prompt-layer ceiling and is reverted, not shipped." It lost both, on the strong model. **So it is
not shipped.** Haiku showed no trap regression (1–0 / tie-heavy), so the cost is Opus-specific.

**But the mechanism is not the feared one — and this is the load-bearing nuance.** The
pre-registered *meaning* of an H2 failure was "the gate misclassified genuine traps as simple and
suppressed the apparatus where it was needed." **That did not happen.** Reading the three Opus
traps v1.6 won:

- **T2 (imputed motive), v1.7 verbatim:** *"you've bundled a behavior with a motive… the motive
  is an inference, and if you lead the confrontation with it, you hand him an easy exit."* — the
  exact correct move, apparatus fully on.
- **T4 (bundled empirical+normative), v1.7 verbatim:** *"the word 'so' is doing illegitimate work
  — it smuggles a contested empirical claim and a value judgment through as if both were
  settled."* — again the exact correct move.
- **T3 (XY problem), v1.7:** caught the self-monitoring blind spot in full, led with it.

v1.7 **caught every trap.** v1.6's accuracy edge is *completeness* — more specific effect sizes on
T4, more script edge-cases on T3 (000-code handling, edge-triggered alerting). v1.7 is a little
more concise everywhere (Opus trap words 734 → 655), and on a trap, "a little more concise" costs
a marginal completeness point that two judges can see. **This is a mild regression of thoroughness,
not the trap-blindness the pre-registration feared.** It is a materially different, and milder,
failure than the triviality gate's (run 5), which lost the same item under three wordings *with no
benefit at all*. Here there is a large benefit and the traps are still caught.

**H3 — the mechanism, measured directly: CONFIRMED.** On Opus downside, v1.7 cut apparatus markers
**19 → 4** and length 371 → 267 words — the gate demonstrably fires and suppresses. On traps the
markers did **not** collapse (Opus 19 → 13, Haiku 7 → 11, i.e. *up*), so the counterweight held
mechanically: the apparatus stayed on where the stake was real. The mechanical read and the judge
read agree — this is not a judge artefact.

**H4 — disguised-trap check: PASSES.** D1 (washing chicken, user is right) was confirmed, not
hedged. No trap was stripped of the apparatus. The counterweight's *categorical* job — keep the
apparatus on for traps — worked; it is only trap *completeness* that eroded.

## Verdict — against the pre-registration, not a fresh read of the numbers

**Do not promote v1.7. Keep `SPEC.md` at v1.6.** The pre-registered promotion rule required H1
**and** H2; H2 failed on Opus. Reinterpreting "lost trap accuracy" as "acceptable because the
traps were still caught" would be exactly the goalpost-move pre-registration exists to prevent, so
I am not doing it — the run reverts.

**But this is a near-miss with a clear next iteration, not a ceiling.** Unlike the triviality gate:

- The benefit is real and large (downside D 6–1, C 4–1; Opus apparatus 19 → 4).
- The regression is *completeness on traps*, not *missed traps* — a milder, more targeted cost.
- It is Opus-only; Haiku got the benefit at no trap cost.

The `Register` wording tells the model to keep "the full apparatus" on traps but does not tell it
to keep the full **completeness/thoroughness** — so on the strong model it trimmed traps along with
everything else. **The next edit (a v1.7.1) should sharpen the counterweight**: keep not just the
apparatus but the *depth* on any turn with a real stake — the concision is only licensed on turns
that lack one. Then re-run this exact ablation. That is the loop continuing; I have not made that
edit, and recommend it as the next step rather than taking it unbidden.

## Defects and caveats

- **42% of cells contested** (51/120) — the same soft-axis noise run 9 flagged, which is exactly
  why H3's mechanical marker count was pre-registered as a co-primary read. The mechanical result
  (gate fires on downside, holds on traps) is the sturdy part; the judge C/D margins agree with it.
- The trap-A regression rests on 3 Opus agreements (both judge families concurring) — real, but a
  thin base, and the reading shows it is completeness, not trap-blindness.
- n = 1 pass/cell; single judge family shared with the responder; register leakage reduced not
  removed. Directional, as always.
