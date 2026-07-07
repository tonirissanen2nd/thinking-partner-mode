# Results — v1.3 vs v1 ablation (2026-07-07)

**Pre-registration:** `PRE-REGISTRATION.md` (committed before any v1.3 result).
**Setup:** `v1` vs `v1.3`, same battery, Responder = Opus, Judge ×2 = Haiku, blind.
`v1` responses **reused from the v1.1 ablation** (shared baseline across the v1.1,
v1.2, v1.3 runs). Only the triviality-gate wording differs between v1.2 and v1.3;
the sequencing change is identical. n=1 per question; directional.

**One-line summary.** The narrowing **did not** recover the triviality gate:
`q7` accuracy went to v1 for the **third consecutive run**, and v1.3 produced the
*barest* trivial-fact answers of all three versions ("1989.", "100 °C.") despite the
strongest completeness-protection wording. That is a **ceiling** answer, not a
wording answer — drop the gate. Separately, this run's sequencing cells are unusually
weak (trap helpfulness fell to 2–1 v1 from v1.2's 4–0) purely from resampling the
*same* wording — a vivid demonstration that n=1 is thin.

## Results

v1.3 vs v1, both Haiku judges must agree. **v1 / v1.3 / tie / contested**, n=6/scope.

| Axis | Trap | Downside |
|---|---|---|
| A Accuracy | 1 / 1 / 0 / 4 | 2 / **4** / 0 / 0 |
| B Calibration | 1 / 0 / 3 / 2 | 2 / 0 / 1 / 3 |
| C Over-contrarianism (inv.) | 0 / 0 / 5 / 1 | 0 / 1 / 1 / 4 |
| D Helpfulness | 2 / 1 / 0 / 3 | 1 / 2 / 0 / 3 |
| E Over-caution (inv.) | 0 / 1 / 2 / 3 | 0 / 1 / 2 / 3 |

## The decisive signal — q7 accuracy across all three runs (same v1 baseline)

| Run | Gate wording | q7 accuracy | v1.3/v1.2/v1.1 q7 answer |
|---|---|---|---|
| v1.1 vs v1 | aggressive ("drop it") | **v1** | bare "1989." |
| v1.2 vs v1 | "keep context" clause | **v1** | "1989. …breached Nov 9… demolition 1990" |
| v1.3 vs v1 | "completeness is not what this touches; answer as fully as warranted" | **v1** | bare "1989." |

Three different gate wordings — including v1.3's explicit, forceful protection of
completeness — and the trivial-fact answer lost accuracy to v1's fuller one **every
time**. v1.3, with the *strongest* completeness language, produced the *tersest*
answers. The prompt layer does not reliably make the model "suppress the empty label
but keep the substance": told a fact is settled, it collapses to the minimal answer
regardless of the surrounding instruction.

**Verdict on experiment (a): CEILING, not wording.** The triviality gate does not
earn its place. Recommendation: **drop it** — revert the Epistemics addition — and
keep only the (validated) sequencing change. A distilled `v1.4 = v1 + sequencing
only` is the clean end state of this loop.

## The other finding — n=1 noise, demonstrated

v1.3 and v1.2 share **identical sequencing wording**, so the sequencing effect is the
same by construction. Yet trap helpfulness read **4–0 (v1.2)** and **2–1 (v1.3)**, and
q3's C/D/E went from clean v1.2 wins to ties/contested — purely from a fresh draw of
the responder. This is exactly the small-n fragility flagged earlier: a single
response per question is a noisy sample, and one run's axis tallies can swing on
resampling alone. Read the sequencing change against the *weight* of v1.1 + v1.2
(where it was strong and consistent), not this single noisy draw. It is the clearest
in-repo argument for n≥3 per item and/or more items before treating any single ablation
cell as settled.

## Caveats

Single family; n=1; Haiku judge; this run is noisier than the prior two. The robust,
cross-run signal is q7 (v1 wins accuracy 3/3 regardless of gate wording); q12 flips
run-to-run (noise). Do not over-read the downside-A 4–2 v1.3 cell — it is driven by the
non-trivial downside items on this particular draw, not the gate. The one conclusion
that survives the noise: **the triviality gate is at the prompt-layer ceiling.**
