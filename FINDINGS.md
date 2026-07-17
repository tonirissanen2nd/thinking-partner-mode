# What twenty-one runs established

A top-level synthesis of the evaluation program. `DESIGN.md` says why the spec is
*shaped* the way it is; `CHANGELOG.md` records what changed *when*; `eval/runs/` holds each
run in full. This document answers the one question those three don't, in one place: **after
twenty-one pre-registered runs, what do we actually know about this spec?**

Everything below is **near-single-family and directional** — almost every responder, judge, and
classifier is a Claude model, and no result is more than a few passes deep. Two runs now sample beyond
Claude, on single slices: **run 16 added a non-Claude *judge* (GPT, up to GPT-5 Thinking High)** and it
diverged sharply from the Claude judges (finding 5) — which is why the A/B-judged results are read down;
**runs 17–19 applied the spec to a non-Claude *responder* (GPT-5 High)** — the
register transferred cleanly (run 17) but the keyed calibration *benefit* is inert because GPT already
self-calibrates on recency (runs 18–19). Neither is the full three-family run (a second non-Claude
family, harder sycophancy probes) — those still have not happened. Read these as well-supported
directions, not proofs — and trust the **judge-free keyed results** (runs 10/14/15) most, since they are
the only ones no judge of any family can move.

---

## 1. The trunk is validated; the branch mostly fires into empty air.

The spec describes itself (`DESIGN.md`) as *a calibration spec of which anti-sycophancy is one
central branch.* Twelve runs sharpen that into an asymmetry the original framing didn't
anticipate:

- **The calibration trunk works — on both a strong and a weak model — but its `High` is 100% only
  on stable facts, not unconditionally.** Scored against an external key (run 10, 4,000 item-trials),
  the confidence labels carry real information: the curve is monotone (High → Moderate → Low) and the
  spec orders and spreads its labels *better than a plain one-liner*, on Haiku included. Run 10 found
  `High` = 100% across ~3,000 labels — but on a near-ceiling battery. **Run 14 stress-tested that
  claim on an adversarial keyed battery and it cracked, informatively:** the full spec's `High` held
  at **100% on stable, knowable facts (82/82)** but fell to **91% pooled (97% Opus / 86% Haiku)** once
  post-cutoff *volatile* facts were mixed in — every `High`-and-wrong event was a fact that genuinely
  changed after the model's cutoff (marathon WR, Python version, F1 champion), which the model recalls
  confidently *and* stale. So the honest trunk claim is **conditional: `High` is trustworthy for
  stable knowable facts, and leaks on facts that moved after training — precisely the class the
  Verification section flags for tool-checking, and precisely where no-tools recall cannot save it.**
  Two things survived the harder battery intact: the **curve stayed monotone** (no calibration
  theater even under stress), and the spec **cut the confidently-wrong rate versus bare in both
  models** (Opus 5→2, Haiku 12→9). The trunk survives as a *discriminating instrument*; only the
  *unconditional* 100% did not.
- **The anti-sycophancy branch targets a failure current models no longer have.** On bare
  pressure — repetition, displeasure, flattery, false appeals to the model's own earlier
  agreement, bare authority, bare consensus — the cave rate was **0/6 in every arm of run 08,
  including no instruction at all, on the weak model.** A directive telling the model to resist
  pressure it already resists is inert. The branch is not worthless — its Principle-2 consensus
  counterweight is a *validated guard* (run 08 H4: a naive wording would have induced
  contrarianism about genuine consensus; the shipped wording does not) — but its headline
  benefit, "reduces sycophancy," is largely **moot against a current frontier model.**

The honest re-weighting: **the validated value is in the trunk. The branch is now mostly a
guard, not an engine.**

**An outside-view discount on that trunk result — applied to ourselves, then tested.** The spec
preaches that a clean result with no conceivable failure path is *grounds for demotion, not
confirmation* (the black-swan gate). Turned on our own finding, "`High` = 100% across ~3,000 labels"
was exactly the profile that most often fails to survive a harder test — so we discounted its
*direction*, not just its magnitude, and named the cheap run that would settle it. **Run 14 then ran
that run, and the discount was vindicated:** on an adversarial keyed battery `High` fell from 100% to
**91% pooled**, confirming the near-ceiling battery (97%) had been an *under-stressed instrument*.
This is the epistemic honesty working as designed — the discount was not decorative; it flagged the
real weak point *before* the measurement found it. The residual exposure is now smaller and precise:
`High` is 100% on **stable** facts and leaks only on **post-cutoff volatile** facts (the
confidently-stale regime), and the **single responder family** (every model is Claude) remains
untested. The forecast-scoring run is the remaining cheap measurement, named under *What is still
unmeasured* below.

## 2. The spec is a purposeful register, not a free upgrade — "a better analyst and a worse clerk."

The one run that measured the *whole* spec against *no instruction at all* (run 09, both
models) returned a **directional tradeoff**, not a clean win:

- **On analytical questions it wins decisively:** accuracy **12–0** and calibration **13–1**
  against nothing, across both models, on trap items (anchoring, XY problems, bundled
  empirical/normative claims, pressure).
- **On simple/relational/generative questions it loses:** it brings the analytical apparatus —
  confidence labels, steelmanning, caveats, pushback — to a question that wanted a short, warm,
  or committed answer, losing helpfulness **7–1** and over-contrarianism **5–1** on the
  downside block.

This is Principle 2 made visible at the level of the whole artifact. It is exactly the split
the full-vs-lite variant routing was built on — so the eval now **empirically backs the routing
advice** the README already gives: full spec for truth-tracking analytical work, lite (or
nothing) for mixed everyday use.

## 3. Its value is model-independent, not weak-model-favoring.

The most intuitive hypothesis in the whole program — *the spec helps a weak model more, because
a strong model is already good* — **failed twice.** Run 08 falsified it for sycophancy (the weak
model resisted bare pressure just as well as the strong one). Run 09 falsified it for the whole
spec on the full instrument: net benefit was **+2 on Opus, +3 on Haiku** — a gap that is noise.
Haiku *executes* the spec (it produces the labels, the steelmen, the reframes), so this is not
an inability to run it. **The deciding variable is the question mix (analytical vs. direct), not
the model's size.** "Use it especially on weaker models" is not supported.

The one place capability *did* decide the outcome is the opposite of the intuition: on the
single item whose pushback hid a false premise among true ones (run 08, q08), **Haiku
capitulated in all three arms — the spec included — and Opus resisted in all three.** Bare
pressure is solved; *plausible, mostly-correct* pressure is not, is not addressable at the
prompt layer, and there the strong model simply wins. That, not sycophancy, is the live open
problem.

## 4. The prompt layer moves what the model *says* far more reliably than what it *does*.

Clause by clause, the loop separated the wins from the ceilings:

| Change | Verdict | Run(s) |
|---|---|---|
| Sequencing counterweight (lead with the answer, attach the critique) | **Improved behaviour — kept** | 04 |
| Triviality gate (skip verifying "trivia") | **Prompt-layer ceiling — dropped** (three wordings, same lost item, no benefit) | 03, 05 |
| Dense Epistemics machinery | **Earns its keep on the tail — kept** | 06 |
| Verification-as-scoring (v1.5) | **Improves *disclosure*, not calibration** — makes miscalibration observable, doesn't reduce it | 07 |
| Persuasion-vector enumeration (v1.6) | **Inert** on current models — kept only as a Principle-2 guard | 08 |
| Frame-detection (v1.7) | **Near-miss — not shipped:** real benefit, but tripped the pre-registered trap-regression trigger | 11 |
| Forecasting section (outside view, non-estimable) | **Pure form, accuracy-neutral — kept as the ledger's precondition.** Installs the base rate (85% vs 3%); **ablation isolates it: cut the section and outside-view apparatus drops 92%→13%, resolution-criterion 38%→0%, with Brier flat (0.142 vs 0.145)**. Scorable, not prescient; removal costs auditability, not accuracy | 15, 21 |

The pattern under the table: the spec **reliably changes the model's account of its reasoning**
— confidence labels appear, steelmen appear, apparatus is suppressed on cue (run 11's gate cut
Opus's downside apparatus markers 19 → 4). It changes the **reasoning itself** only where the
model was not already succeeding — and where it wasn't (the confidently-wrong regime; plausible
pressure), no wording has yet made it succeed. This is the ceiling `DESIGN.md` predicts,
observed six times.

## 5. The measurement has a floor, and the sturdy findings all cleared it.

Two judge families (both Claude) **disagree on ~40% of the soft-axis cells** (41% in run 09,
42% in run 11) — helpfulness and over-contrarianism are genuinely less determinate than
accuracy. Every finding above that survives is one with a **judge-independent anchor**: an
external answer key (run 10/14), a mechanical apparatus-marker count (run 11/15), a near-binary
substantive act like caving or not (run 08), or a both-judges-must-agree rule.

**Run 16 turned a genuinely non-Claude judge (OpenAI GPT) on the full Opus battery (12 items: trap +
downside), and the news is bad for the judged results — consistently across both cells.** A
cross-family judge **confirms the spec's costs and discounts its benefits.** Across all 12 Opus items
it reads the spec's confidence-flag/verify-this apparatus as **over-caution on 12/12**, gives **bare
the accuracy edge (7–3)**, and leaves the spec **only one surviving cross-family virtue: calibration
(spec 7 / bare 4)**. The decisive asymmetry with run 09: its **benefit** claim ("spec wins accuracy on
traps") does **not** replicate under GPT (on the trap cell GPT leaned bare on accuracy, 2 spec / 3 bare;
q01 flipped all five axes), while its **cost** claim ("spec is the worse clerk — loses helpfulness on
simple turns") **does** replicate (GPT gives bare downside-helpfulness 5/6, matching Claude's 4/6). So
the earlier sentence — "the accuracy/calibration results are robust to judge identity" — **was itself an
artifact of a single judge family and is now corrected**: robust *within Claude*, and under a non-Claude
judge only **calibration** survives (the spec's out-*reasoning* wins on a few dense items like the q11
brainstorm and the q04/q05 cited analyses; its out-*hedging* register is penalized everywhere). Reassuringly,
the one A/B axis that survives the family change — calibration — is exactly the property the **judge-free
keyed runs (10/14) validate independently**, which makes those keyed results the load-bearing spine of the
whole program: they survive both a family change *and* the removal of the judge entirely. **And the free-tier caveat is refuted, not merely noted:** re-judging the trap cell on **GPT-5 Thinking
at High effort** (the strongest available judge) moved accuracy *further* against the spec, not toward
it — spec-favorability is **monotone Claude > GPT-free > GPT-5-High** (trap accuracy spec-wins: 4/6 →
2/6 → **1/6**). A stronger judge is harder on the spec, so the divergence is a genuine cross-family
register preference, not judge weakness. The durable cross-family agreement is narrow and telling: the
items with explicit *quantitative/citation* machinery (the LTV model, the cited-RCT ledger, the ruin
argument — q05 on accuracy+calibration, q04/q06 on calibration) are spec on all three judges; where the
spec's edge is *register* (hedges, confidence flags), only Claude credits it, and more capable
non-Claude judges penalize it more. Scope caveat, still large: Opus cell only (Haiku not run), one
non-Claude family, **responder still Claude** — two families, not three. But the finding is now robust
to judge capability as well as judge family: the A/B-judged wins (runs 08/09/11/12) are **more
judge-family-dependent than the program assumed** and are read down accordingly — the spec buys
cross-family-visible advantage only from *arithmetic and citations*, not from its register; it is a
calibration instrument (validated judge-free) with a real clerk-cost, not the decisive "better analyst"
the single-family evals implied.

---

## What this means if you are deciding whether to use the spec

- **Adopt it (or the lite variant) for analytical work** — quantitative analysis, contested
  evidence, strategic decisions. That is where the 12–0 accuracy win lives, and where the
  apparatus earns its overhead.
- **Do not adopt it to "stop the model being sycophantic"** on a current frontier model — that
  failure mode is already handled by the base model, and the spec's cost (over-analysis of
  simple turns) may leave you worse off on a mixed workload. Use lite, or nothing.
- **The lite variant is a real register with a narrow, honest value (run 12).** Against the full
  spec it is the better clerk (wins helpfulness on simple/relational/generative turns) and the
  worse analyst (full wins trap accuracy 8–1). Against *nothing* it is not decoration — it beats
  bare on **calibration** (the one thing the base model doesn't already do) — but it **costs some
  directness** (bare is more helpful and less cautious on the analytical items). So lite's real
  proposition is "a better-calibrated everyday assistant, at some cost in directness," **not** a
  free upgrade on the raw model. Pick it if you value calibration over raw directness; otherwise
  the raw model is a defensible everyday choice.
- **Do not expect it to rescue a weak model** more than a strong one. Its value scales with
  *what you ask*, not with *what you run it on*.
- **Trust the confidence labels, with one sharp asterisk:** a `High` means correct **for stable,
  knowable facts** (100% on both models, runs 10 and 14) — but on facts that may have *changed after
  the model's training cutoff*, a `High` can be confidently stale (run 14: pooled `High` 91%, and the
  misses are all post-cutoff facts). For anything time-sensitive, treat even a `High` as a claim to
  verify with tools, not a guarantee — which is what the spec's Verification section already tells the
  model to do. The labels otherwise lean slightly *under*-confident (a `Moderate` is ~70% accurate on
  the hard battery, higher on easy ones), the safe direction.
- **Where you put it matters more than any clause in it.** The spec is layer one of a two-layer
  system; the harness that re-injects it each turn is layer two (see `README.md`). No clause
  substitutes for that.

## What is still unmeasured

- **The three-family run — both halves now have a first slice, pulling in opposite directions.**
  *Judge half (run 16):* a non-Claude judge (GPT, up to GPT-5 Thinking High) diverged sharply from the
  Claude judges (finding 5) — the spec's trap accuracy/calibration sweep did not replicate and its
  over-caution scoring inverted, *more* so with a stronger judge. *Responder half (runs 17–18):* the spec
  was applied to a non-Claude **responder** (GPT-5 High) for the first time. Its **register transferred
  cleanly** (run 17) — GPT under the spec produces the full apparatus a strong bare GPT omits (explicit
  confidence+basis, scorable forecast, non-estimable, ruin/EV-vs-bounded), with a *mild* clerk-cost and
  the *same inert anti-sycophancy branch* (base-model ceiling). But its **calibration *benefit* is inert on
  GPT — because GPT already self-calibrates** (runs 18–19). Run 18 was inconclusive (its battery was
  near-ceiling for GPT); **run 19 fixed the instrument** with 9 facts that resolved *after* GPT's cutoff
  (2026 Olympics, French Open, Oscars, Super Bowl LX, Wimbledon, Eurovision, NBA — web-established today,
  genuinely unknowable to GPT). Result: **spec-GPT ≈ bare-GPT, both well-calibrated** — neither stamped a
  single `High` on the 9 unknowable items (spec→`Low`, **bare→`Unknown`, marginally *more* humble**), and
  both reserved `High` for the 4 stable controls (all right). **Zero `High`-and-wrong in either arm.** So
  the spec's demotion gate — which *cut* confidently-wrong on Claude (run 14, Opus 5→2) — is **redundant
  on GPT: bare GPT already demotes what it can't know.** The benefit doesn't fail to port; it is *inert
  because unnecessary* — the run-08/17 ceiling pattern (base model already does it), extended to
  calibration-of-recency. Net responder-half read: the spec transfers the **register** to GPT (form,
  portable), while its **calibration benefit is base-model-relative** — Claude 4.x needed the volatile-fact
  humility the spec supplies; GPT-5-High already has it. The three halves compose into the program's
  sharpest tension: **a non-Claude model, instructed, *produces* the register that the same model judging
  freely *penalizes* as padding — and producing it neither improves nor is needed for its calibration.**
  Still open: the harder plausible-pressure sycophancy probes and a second non-Claude family (Gemini).
  Portability of *form* is real; the *calibration benefit* is Claude-relative (GPT doesn't need it).
- **The fat-tail branch is a different epistemic category — not a backlog item.** The trunk is
  validated on *thin-tailed, knowable-answer* questions — the regime where calibration is easy and
  low-stakes. The fat-tail branch (non-estimable-vs-`Unknown`, the black-swan demotion,
  ruin-is-material) is validated **by mechanism and argument, not by the instrument — and it
  *cannot* be, by this instrument**: `non-estimable` is by definition unscoreable against a key.
  So this is not "not eval'd yet" (which implies more of the same would fix it); it is a claim
  that lives in a different category from the trunk, reachable only by the slow real-world loop a
  **forecast ledger** would close (see `HARNESS.md`). Naming that category difference is the
  honest move — and it is *why* the ledger, not another battery, is the only instrument that
  could ever reach the part of the spec that matters most. **Run 15 sharpens this:** the *behaviour*
  the fat-tail branch prescribes — refusing a point estimate on a genuine black swan — *is* mechanically
  testable, and it fired (AGI marked `non-estimable` 67% vs 0% bare, and *selectively*: a
  circuit-breaker-bounded tail still got a point estimate). What remains unreachable by any battery is
  whether that refusal was *right about the world* — the outcome, not the behaviour. So the branch is
  now validated one layer deeper (the discipline executes and discriminates) while the category claim
  stands (the outcome is unscoreable; only the ledger reaches it).
- **The trunk battery has now been hardened (run 14) — done, and it cracked as predicted.** An
  adversarial keyed battery (run 10's method, harder items) dropped the full spec's `High` from 100%
  to **91% pooled**, with the leak confined to post-cutoff volatile facts and `High` still 100% on
  stable facts. The ceiling-artifact worry did *not* recede — it was confirmed, and the real operating
  point is now measured. See run 14. This leaves the standing family debt as the one large gap:
  - **Score forecasts, not recall (the rung before the ledger) — now run (run 15).** The spec's
    **Forecasting** section, previously the largest **unvalidated** surface, was tested by scoring
    resolvable post-cutoff predictions against known outcomes (search-established). Result: it is
    **validated on *form*, not *accuracy*.** The spec reliably installs the outside view (explicit
    base rate / reference class on **85% of forecasts vs 3% bare**; 92% vs 26% counting implicit
    base-rate reasoning) and correctly declines a point estimate on a genuine black swan (AGI:
    non-estimable **67% vs 0%**), *selectively* — it still gives a point estimate on a
    circuit-breaker-bounded tail. But it does **not** improve calibration accuracy: Brier **0.202
    vs 0.181 bare** — marginally *worse*, because genuine surprises are ceiling-bound on both arms
    and the outside-view caution drags confident-correct recall toward 50% on knowable items. So the
    spec makes forecasts **scorable, not prescient** — which is the concrete argument that the
    accuracy loop needs the **ledger** (real-world scored feedback), not a better prompt. The rung
    is climbed: the ledger can be built on a section now shown to emit scorable forecasts, knowing
    the prompt alone will not deliver the accuracy the ledger exists to earn. (One honest sub-null:
    the spec does *not* reliably restate an explicit resolution criterion — the "scorable claim"
    win is on the probability + base rate, not the resolution half.)
  - **The ledger, built and split into measurement vs improvement (runs on `ledger/`, and run 20).**
    The forecast ledger is now a *real* instrument (runnable, seeded with 264 real resolved forecasts),
    and its two values were separated on purpose. **Measurement works and is the point:** it scores the
    track record judge-free (Brier, ECE, reliability, discrimination, per-class), localises the
    miscalibration, and compares arms without a taste-contaminated judge. **Improvement does not (run
    20):** feeding the model its own scored record did **not** improve its calibration (Brier 0.457 fed
    vs 0.414 cold — marginally *worse*; discrimination unchanged). The model **mostly ignored** the
    feedback (10/12 items ≤3-pt moves — the say-vs-do ceiling, now for context-feedback), and its one
    large response was a **harmful over-correction** (a bold-correct 75% collapsed to 2%). So the
    ledger's "layer two" pays off as a **scoreboard, not (in-context) an improvement mechanism** — and
    naive feedback can *harm*: the user reads the ledger and discounts; you do not feed raw scores back
    to the model. Run 20 also surfaced a caution about the instrument itself: a Brier/ECE on a
    **surprise-heavy resolved sample mis-diagnoses the *direction* of miscalibration** ("underconfident"
    can be a sampling artifact), so the ledger's *diagnosis* needs stratified sampling before it is
    trusted — its *scoring* is sound regardless.
- **Long-context drift — partially run, and under-tested by my own probe design (run 13A).** At
  ~20 turns, the probed behaviours held at 100% with or without re-injection — but the probes were
  base-model-ceiling behaviours (run-08 trap), so the null under-tests the layer-two claim rather
  than settling it. A faithful re-run needs spec-specific probes (confidence labels, steelman,
  sequencing) at ~20 and much longer lengths.
- **Lite's directness cost, tuned away.** Run 12 measured lite once and found it trades directness
  for calibration versus bare. Whether that cost can be reduced — making "admit uncertainty / flag
  for checking" less hedgy while keeping the know-vs-infer discrimination — is an untested ablation.
- **Frame-detection, done right.** Run 11 showed the idea works but the wording over-trimmed
  traps. A v1.7.1 that protects trap *depth*, not just trap apparatus, is the open next
  iteration.
