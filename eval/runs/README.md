# Eval runs

One folder per run, named `YYYY-MM-DD-NN-slug` where `NN` is the run's sequence
number — so a directory listing sorts in **run order**. Each run is self-contained:
its own pre-registration, results writeup, and raw artifacts, so a run can be read,
audited, or reproduced without reference to any other. Keep both conventions when
adding a run (next index, self-contained).

**Run folders are immutable historical records.** A run's `RESULTS.md` reports what
*that* run found against the spec version *it* tested; it is **not** updated later to
reflect newer versions — that would corrupt the record, and duplicated across N
folders it would inevitably go stale. The only place that tracks the *current*
picture is **this index** plus the top of `../../CHANGELOG.md`. Only those two are
updated per push; the run folders never are.

Each run folder contains:

- `PRE-REGISTRATION.md` — committed **before** any result (removes researcher
  degrees of freedom).
- `RESULTS.md` — the writeup, judged against the pre-registration.
- `spec-as-tested-vN.md` — the exact spec this run evaluated, archived verbatim, so
  the tested version is preserved even as the live `SPEC.md` evolves. `v1` is the
  first tested spec (SHA `f68f436`); later modified specs are `v1.1`, `v1.2`, …
  stamped into the filename. (The lean-Epistemics run archives `spec-full-v1.md` and
  `spec-lean.md` instead — it tests a fork, not a version bump.)
- the run's data (scores CSV, battery, answer key, workflow scripts where used, …).
- optionally `raw/` — the process intermediates (per-question responses, normalized
  answers, blind judge inputs, individual judgments), committed for auditability.

The protocol these runs implement lives one level up: `../README.md` (Track 1),
`../prompts/` (the role prompts), `../scoring/` (the scoresheet tools).

## Runs to date (newest first)

| # | Run | What it found |
|---|---|---|
| 14 | `2026-07-17-14-adversarial-trunk-battery/` | **Stress-tested run 10's trunk result on an adversarial keyed battery — and it cracked, informatively.** Run 10's method (no-tools recall, deterministic external-key grading) on a battery built to *break* the ceiling: 7 post-cutoff volatile facts + 5 gotcha/precision traps + 2 obscure numerics + 1 control, full spec vs bare × Opus/Haiku, K=10 (600 item-trials). **H1 (primary) CONFIRMED:** the full spec's `High` fell from run 10's 100% to **91% pooled (97% Opus / 86% Haiku)** — so run 10's clean 100% *was* an under-stressed-battery artefact, exactly as the `FINDINGS` outside-view discount predicted. **But the crack is sharply bounded:** `High` stayed **100% on stable knowable facts (82/82)** and every `High`-and-wrong event was a **post-cutoff volatile fact** the model recalls confidently *and* stale (marathon WR, Python version, F1 champion) — the prompt-layer ceiling, caught red-handed. The reflexive-100°C boiling trap caught no one; "India most populous" was High-and-right (that change is internalised — the cutoff boundary is visible in the data). **H2 HELD:** curve stayed monotone under stress (no calibration theater). **H3 CONFIRMED (both models):** the spec cut confidently-wrong vs bare (Opus 5→2, Haiku 12→9). **H4 supported:** more abstention on obscure items (High 9 vs 15). **Consequence, pre-committed:** the `FINDINGS` trunk claim is downgraded from unconditional "100%" to "**100% on stable facts; ~91% once post-cutoff volatile facts are included, residual in the confidently-stale regime the Verification section flags for tools.**" The trunk survives as a discriminating instrument; only the unconditional 100% did not. |
| 13 | `2026-07-15-13-agentic-multiturn-tool/` | **First agentic run — Track A run, Track B still built-not-run.** Track A: a 20-turn conversation, probes at early/late depths, **inject-once vs re-inject**, both models, to test long-context drift and whether re-injection cures it (the repo's central unmeasured claim, "layer two = the harness"). **Result: a clean null on drift at ~20 turns** — every cell fired 100%, no early→late decay, no re-injection gain, no model difference. **But the run's real finding is a probe-design error of mine:** the two behaviours tested (anti-sycophancy myth-correction; refusing to invent an obvious unknown) are ones the **base model already does at ceiling** (the run-08/12 trap again), so there was no *spec-specific* signal to decay — the null under-tests the layer-two claim rather than settling it. A faithful re-run needs spec-specific probes (confidence labels, steelman, sequencing) the base model does not default to. **Track B** (tool-verification vs bare-with-tools) still needs a live search tool; pre-registration, batteries, and runner are committed. The layer-two claim remains open. |
| 12 | `2026-07-15-12-lite-vs-full-vs-bare-2model/` | **First evaluation of `SPEC-lite.md`** — the inverted eval, 3 arms (lite / full / bare) × 2 models, reusing run 9's battery and its full/bare responses as a shared baseline (only lite is new). Plus a ruin probe and a mechanical marker count. **Lite vs full — the intended tradeoff, confirmed:** lite is the better clerk (downside helpfulness 5–2, less contrarian) and the worse analyst (full wins trap accuracy 8–1). Routing validated from both sides. **Lite vs bare — the load-bearing question for a default:** lite is **not** decoration — it beats bare on **calibration** (traps 5–0, strongest on the weak model, the one thing the base model doesn't already do) — but it **costs directness**: bare wins helpfulness 7–1 on traps and is less over-cautious. So lite **trades directness for calibration** even versus nothing; not a free upgrade. **Ruin gap: does not exist** — all three arms (bare included) name the irreversible cost on the 401(k)-cashout probe, so the full spec's explicit ruin clause is redundant and no cue should be added to lite. Apparatus markers: lite hugs bare (light register), far below full. **Verdict: ship lite as-is; its honest value is "a better-calibrated everyday assistant, at some cost in directness," not a free default.** |
| 11 | `2026-07-15-11-v1.7-frame-detection-ablation/` | **Acted on run 9's named fix.** `v1.7 = v1.6 + one section, `Register`** — a frame-detector that switches the analytical apparatus OFF on turns with no truth-or-decision stake (simple/relational/generative), with a Principle-2 counterweight keeping it ON for traps. Clean one-section ablation, both models, blind A/B (two judges) + a judge-independent apparatus-marker count. **The benefit is real: downside helpfulness 6–1, over-contrarianism 4–1; Opus apparatus markers on downside 19 → 4.** But it **tripped the pre-registered revert trigger** — on Opus traps, v1.7 lost accuracy (0–3) and calibration (0–2). Reading those responses, the loss is **marginal completeness, not a missed trap** (v1.7 caught every trap with full apparatus), but I committed in advance to revert on any trap A/B loss, so **v1.7 is NOT shipped; the live spec stays v1.6.** Unlike the triviality gate (run 5), this is a near-miss with a large benefit and a milder, targeted cost — the next iteration (v1.7.1) should protect trap *depth*, not just trap apparatus, then re-run this exact ablation. |
| 10 | `2026-07-15-10-track2-calibration-2model/` | **The spec's trunk, finally isolated: are the confidence labels actually calibrated,** scored against an external numeric key, on Opus 4.8 **and — for the first time — Haiku 4.5.** Run-1 hard battery, 25 trials × 2 arms (spec / one-liner) × 2 models = 4000 item-trials, **deterministic** grading against pre-committed acceptance bands. Result: **no calibration theater anywhere — `High` was 100% accurate across ~3,000 labels, Haiku included** (0 High-and-wrong). The spec's curve is **monotone** on both models (High 1.00 → Moderate ~0.94 → Low ~0.70); the one-liner **breaks monotonicity on Opus**. The spec also **spreads labels better** (reserves `High` less) and abstains only on the single hardest item. Costs are minor and safe-direction: slight **under-confidence** on `Moderate` (its Moderate answers are ~94% accurate), which makes the one-liner look marginally tighter on a fixed-mass ECE. **The trunk claim holds on both models.** Two honest asterisks: my pre-registered theater threshold was mis-specified (trips on the letter, not the substance), and the battery is **near-ceiling (97%)** so it only lightly stresses the claim — the confidently-wrong regime needs post-cutoff facts + tools (run 07), not recall. |
| 9 | `2026-07-15-09-v1.6-vs-bare-2model-track1/` | **The run the project never did: the whole spec (v1.6) vs no instruction, full five-axis Track 1, on Opus 4.8 and Haiku 4.5.** Canonical 12-item battery, two blind judge families, both-must-agree. Result is a **tradeoff, not a null — and by the pre-registered criteria a `FAILURE`.** The spec wins **accuracy 12–0 and calibration 13–1** on traps vs nothing (zero accuracy losses anywhere) — the repo's strongest positive result, against the hardest control. It pays with **over-contrarianism (loses C 5–1) and helpfulness (loses D 7–1) on the downside block** — friction and needless caveats on simple/relational/generative questions — which trips the pre-registered failure trigger (losing axis C). **Primary hypothesis H2 fails again:** net benefit is +2 on Opus, +3 on Haiku — the spec is **not** a weak-model aid; its value is workload-dependent (question mix), not capability-dependent. Haiku executes the spec fully (H4). 41% of soft-axis cells are contested — the accuracy win is judge-robust, the helpfulness cost is judge-dependent. **The spec makes the model a better analyst and a worse clerk.** |
| 8 | `2026-07-15-08-persuasion-3arm-2model/` | The **value decomposition** the project had never done: **no instruction** vs a **generic one-liner** vs the **full spec (v1.6)**, on **Opus 4.8 and Haiku 4.5**, over a purpose-built persuasion battery. Result: **cave rate 0/6 in all six arms** — the bare-pressure failure mode the spec's Dialectics clause targets **does not fire in either model, with no instruction at all.** The ceiling is not an Opus artefact; it is a Claude artefact. The clause is **safe** (the Principle-2 consensus trap was tested and does not fire: all v1.6 consensus-with-basis cells revised correctly) and **very likely inert** — a validated *guard*, not a validated improvement. **The finding that outranks the hypotheses:** on the one item whose "correction" hid a false premise among true ones, **Haiku capitulated in all three arms — spec included — and Opus resisted in all three.** Sycophancy toward bare pressure is solved; sycophancy toward *plausible* pressure is not, and is not a prompt-layer problem. |
| 7 | `2026-07-15-07-v1.5-vs-v1.4-tool-equipped/` | First **tool-equipped** run (live web search). `v1.4` vs `v1.5` on a purpose-built stale-fact battery — the one thing Track 2's battery structurally could not do: produce `High`-and-wrong events. Result: the confidence-gate *bug fix* is weakly supported (v1.4 verified 7/8 anyway), but the **disclosure effect is strong** — on the same items, with the same correct final answers, v1.4 concealed that its unaided recall had been confidently wrong and v1.5 reported it. No over-verification, no defensive hedging. **Keep v1.5** — the mechanism makes miscalibration *observable*, exactly as `DESIGN` claims, without improving calibration. **Scope:** isolates the Verification change only. The live spec is `v1.6`, whose Dialectics change (persuasion vectors) is orthogonal to this battery and **remains untested**. |
| 6 | `2026-07-07-06-leanEpistemics-vs-full-ablation/` | `full` (v1) vs `lean` (Epistemics machinery cut), on a purpose-built fat-tail / ruin / hidden-failure / control battery. Full beats lean on the stress items (accuracy 5–2, calibration 4–2; fat-tail group 2–0/2–0), even on controls → the dense Epistemics earns its keep on the tail. Reconciles the Track-2 ordinary-facts null. **Keep the dense Epistemics.** |
| 5 | `2026-07-07-05-v1.3-vs-v1-ablation/` | `v1` vs `v1.3` (narrowed triviality gate). Narrowing did NOT recover q7 — v1 wins its accuracy the 3rd straight run regardless of wording → the gate is a prompt-layer ceiling. **Drop the gate.** Also a vivid n=1-noise demo (same sequencing wording, helpfulness swung 4–0→2–1 on resampling). |
| 4 | `2026-07-07-04-v1.2-vs-v1-ablation/` | `v1` vs `v1.2` (shared v1 baseline). The sequencing counter-counterweight recovered the q3 accuracy while keeping the gains → **sequencing is a keeper**; the triviality gate still a wash. |
| 3 | `2026-07-07-03-v1.1-vs-v1-ablation/` | `v1` vs `v1.1`. Isolates the two v1.1 counterweights: less contrarian / more helpful, but a small accuracy cost (Principle 2 live) → motivates v1.2. |
| 2 | `2026-07-07-02-hetero-claude/` | Track 1 re-run with a *different Claude model* judging (Haiku) than responding (Opus). Calibration win replicates; a mild trap-contrarianism cost same-model judging missed shows up. |
| 1 | `2026-07-07-01-single-family/` | The first pass. Both tracks (blind A/B + calibration), all roles Opus 4.8. Directional, single-family — the weakest role separation. |

**Net across the loop:** the sequencing counterweight was validated (kept), the
triviality gate hit a prompt-layer ceiling (dropped), and the dense Epistemics was
shown to earn its keep on tail risk (kept) — distilled into `v1.4` (see `CHANGELOG`).
Then `v1.5` was shown to make miscalibration **observable** rather than to fix it
(kept, run 7), and `v1.6` was shown to be **safe but inert** — it guards against a
Principle-2 trap, but the sycophancy it targets is already absent from the base models
(kept as a guard, run 8).

**The pattern across nine runs is worth stating plainly.** Of every clause measured,
exactly one improved behaviour (sequencing). One was a ceiling (the gate, dropped).
One earns its keep only on the tail (Epistemics). One improves *disclosure* without
improving *calibration* (verification). One is inert (the persuasion enumeration).
The prompt layer moves what the model **says about its reasoning** far more reliably
than it moves the reasoning — and where the reasoning does not already succeed, no
wording has yet made it succeed.

**And run 9 measured the whole spec at once, against nothing.** It is not an
across-the-board improvement and it is not a null: it is a **directional tradeoff**
— a decisive accuracy/calibration win on analytical questions bought with a real
over-contrarianism/helpfulness cost on simple ones, roughly independent of model
size. The spec is a *register with a purpose*, not a free upgrade. The next edit
worth making is frame-detection (don't deploy the analytical apparatus on a direct
or relational question), and that may be the next prompt-layer ceiling.

**Run 10 opened the trunk; run 14 found its real boundary.** Every run before 10 measured
the spec's *branch* (behaviour) or a proxy for calibration a pairwise judge cannot actually
resolve. Run 10 scored the confidence labels against an external key, on both a strong and a
weak model, and found they **carry real information** — monotone curve, `High` 100% across
~3,000 labels, the spec spreading labels better than a one-liner, no calibration theater.
But that battery was near-ceiling. **Run 14 stress-tested the `High` claim on an adversarial
keyed battery, and it cracked as the `FINDINGS` outside-view discount had predicted:** pooled
`High` fell to **91%** — 100% on stable facts, leaking only on **post-cutoff volatile facts**
the model recalls confidently and stale. The curve stayed monotone under stress and the spec
still beat bare on demotion, so the trunk survives as a *discriminating instrument*; what did
not survive is the *unconditional* 100%. So the picture across fourteen runs: the spec is a
purposeful analytical register whose confidence labels are honest **for stable facts** and
**flag-then-verify for volatile ones** — validated on the trunk (with a measured operating
point, not a perfect one), a measured tradeoff on the branch, and inert exactly where the base
model is already good (bare-pressure sycophancy).

None of these is the mandated **three-family** run (generator, responder, judge from
three different model families). All are directional. See each run's `RESULTS.md`
for what it can and cannot establish.
