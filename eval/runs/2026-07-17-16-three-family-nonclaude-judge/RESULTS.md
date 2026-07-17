# Results — three-family run: a non-Claude judge (run 16)

**TL;DR — the project's largest standing debt, partially paid, and it cost the project.** Every prior
judged result was Claude-judging-Claude. This run had a genuine **non-Claude judge** (OpenAI GPT, via
ChatGPT) re-score run 09's existing blind A/B pairs on the **full Opus battery: trap cell (q01–q06)
AND downside cell (q07–q12), 12 items**. The non-Claude judge **diverges sharply and one-directionally
against the spec.** Across all 12 Opus items it reads the spec's confidence-flag/verify-this apparatus
as **over-caution on 12/12**, gives **bare the accuracy edge (7–3)**, and leaves the spec **only one
surviving cross-family virtue: calibration (spec 7 / bare 4).** The asymmetry with run 09 is the
sharpest finding: run 09's **benefit** claim ("spec wins accuracy on traps") does **not** replicate
under a non-Claude judge, while run 09's **cost** claim ("spec is the worse clerk — loses helpfulness
on downside") **does** replicate (GPT gives bare downside-helpfulness 5/6). A cross-family judge
confirms the spec's costs and discounts its benefits. Scope caveat (one non-Claude family, Free-tier,
responder still Claude) is large — but the signal is strong and consistent across both cells.

*(This document was written after the trap cell and extended with the downside cell; the trap-cell
detail below is preserved, and the downside cell + combined 12-item picture follow it.)*

## Method

Reused run 09's 6 Opus trap judge-input files verbatim (blind "Answer 1 / Answer 2", spec-vs-bare
order randomized per item; mapping held private). Fed each to **ChatGPT (Free tier, "Fast answer" /
GPT-5-class), temporary chat**, with a faithful reconstruction of run 09's rubric (5 axes: A accuracy,
B calibration, C over-contrarianism [cost], D helpfulness, E over-caution [cost]; winner + margin).
GPT verdicts stored raw in Answer-1/2 terms (`raw/judgments-gpt/gpt-verdicts.txt`) and mapped to
spec/bare afterward, so the judge never saw which arm was which. Compared cell-by-cell to run 09's
Claude consensus (`scores.csv`).

## What the non-Claude judge did

**Overall agreement with the Claude consensus: 6/30 axis-cells (20%)** — though that number is
depressed by run 09's many "contested" cells (where the two Claude judges already disagreed and no
consensus exists to match). The load-bearing comparison is cleaner and worse for the spec:

| Axis | Run-09 Claude consensus | Non-Claude (GPT) judge |
|---|---|---|
| **A — accuracy** | spec **4/6**, bare 0/6 (2 contested) | spec 2/6, **bare 3/6**, tie 1 |
| **B — calibration** | spec **5/6**, bare 0/6 (1 contested) | spec 3/6, bare 2/6, tie 1 |
| C — over-contrarianism | spec 0, bare 2 (rest contested/tie) | bare 4/6, tie 2 |
| D — helpfulness | spec 1 (rest contested/tie) | spec 3/6, bare 3/6 |
| **E — over-caution** | spec **3/6**, bare 0/6 | **bare 6/6** |

Three things stand out:

1. **The load-bearing accuracy/calibration sweep does NOT replicate.** Run 09's flagship result — the
   spec winning accuracy **and** calibration on traps, with *zero* bare wins — was the repo's
   strongest positive finding. Under a non-Claude judge it **splits**: on accuracy GPT actually leans
   *bare* (2 spec / 3 bare), and on calibration the spec lead shrinks to 3–2. The claim survives only
   as "the spec sometimes reads as more accurate/calibrated," not "it wins these axes."
2. **The over-caution axis fully inverts.** Claude judges scored the spec as *less* over-cautious
   (spec 3/6, the calibration metadata reading as appropriate); GPT scored **bare less over-cautious on
   all 6/6**. To the non-Claude judge, the spec's "verify against a primary source / recall not
   verified / confidence-flag" apparatus reads as **hedging and padding**, not calibration. Same text,
   opposite sign — the sharpest cross-family divergence in the run.
3. **q01 flipped on every axis.** Where both Claude judges scored spec on 4 of 5 axes, GPT scored
   **bare on all 5**. A complete reversal on one item.

**Where the judges agree:** q04 and q05 accuracy+calibration — both Claude *and* GPT give the spec the
win. These are the two items where the spec answer's analytical superiority is least stylistic (dense
citations, explicit steelman, multi-factor decomposition). So the spec's advantage is **not** an
artifact everywhere — where it out-*reasons* bare unambiguously, a non-Claude judge sees it too. It is
where the advantage is register/apparatus (q01, q06) that the Claude judges credited it and GPT did not.

## What this establishes

- **A material part of the run-09 soft-axis and even accuracy/calibration advantage was judge-family
  dependent.** `FINDINGS.md` already flagged ~40% *within-Claude* judge disagreement on soft axes and
  leaned on judge-independent anchors (the deterministic key runs 10/14/15, mechanical marker counts).
  This run shows the dependence is **larger across families than within Claude**, and — critically —
  that it reaches the accuracy axis too, not just the soft ones. The keyed results (trunk, forecast
  form) are untouched by this (no judge). The **A/B-judged results (runs 08/09/11/12) should be read
  down**: the spec's win over bare on traps is real to a Claude judge and roughly a *coin flip to a
  non-Claude judge on accuracy*, with the spec's calibration apparatus actively penalized as verbosity
  on the cost axes.
- **The direction is one-sided and against the spec.** This is not noise around the same answer; every
  divergence moved the same way (toward bare, or toward reading the spec as over-cautious). That
  one-sidedness is what makes n=6 informative despite the small cell: a family-neutral judge does not
  merely disagree per-item, it systematically values the spec's register less.
- **The spec's genuine analytical wins survive** (q04/q05). The honest split: the spec buys real,
  cross-family-visible advantage when it changes the *reasoning* (citations, steelman, decomposition);
  it buys Claude-only credit when it changes the *register* (confidence flags, verify-this hedges,
  caveats), which a non-Claude judge discounts or penalizes.

## Limits — large, and stated plainly

- **Scope: the full Opus battery (12 items), Haiku not run.** Opus trap (6) + Opus downside (6) are
  complete; **Haiku traps and Haiku downside (12 more) were not run** — driving long blind pairs through
  a browser UI is costly, so this is a deliberate 12-of-24 subset, not a silent cap. Haiku is the clean
  next extension (it would test whether the family-divergence is also model-size-dependent on the
  responder side).
- **One non-Claude family, one tier.** OpenAI GPT, Free-tier "Fast answer" — not Gemini/Llama, not a
  frontier GPT tier. A stronger or different-family judge could land differently. This adds a **second
  judge family**, the biggest single step toward the mandated three-family design — but the **responder
  is still Claude** (every answer being judged is a Claude answer), so this is a two-family run, not the
  full three-family (generator + responder + judge all distinct).
- **Rubric reconstructed, not the original judge prompt** (run 09 saved judge *inputs* and *outputs*,
  not the instruction); faithful to the pre-registered axis definitions but not byte-identical.
- **Three of six prompts (q03/q05/q06) were lightly compressed** to fit the single-line browser input
  (code blocks and long lists condensed; substance and structure preserved). q01/q02/q04 were verbatim.
- Deterministic mapping applied post-hoc; the judge was blind to arm. Directional.

## Downside cell (q07–q12) — the cost claim replicates cross-family

Extending to the 6 downside items (simple/relational/generative questions, where run 09 found the spec
*loses* helpfulness to bare) sharpens the picture rather than softening it:

| Axis | GPT (non-Claude), 6 downside items | Run-09 Claude consensus |
|---|---|---|
| A accuracy | spec 1, **bare 4**, tie 1 | spec 2, bare 0 (rest contested) |
| B calibration | **spec 4**, bare 2 | spec 3, bare 0 |
| C over-contrarianism | bare 5, tie 1 | bare 3 (rest contested) |
| D helpfulness | **bare 5**, spec 1 | **bare 4** (rest contested) |
| E over-caution | **bare 6/6** | tie (0/0) |

Agreement with Claude consensus rises to **11/30 (37%)** vs the trap cell's 20% — because on downside
**both families lean the same way (toward bare) on the cost axes.** Three things:

1. **The "worse clerk" cost replicates.** GPT gives bare downside-helpfulness **5/6**; run 09's Claude
   judges gave bare **4/6**. Both families agree the spec over-elaborates on simple questions and loses
   helpfulness for it. So run 09's *cost* claim is **cross-family-robust** — unlike its *benefit* claim.
   The clearest case is q12 ("boiling point of water?"): GPT scored **bare on all five axes**, penalizing
   the spec's "99.974 °C / SI-definition" precision even on accuracy and calibration.
2. **Calibration is credited even here.** GPT gives the spec the calibration edge on downside (4/6) —
   the careful know-vs-infer distinctions (Berlin Wall dates, the chicken "no measured endpoint" flag)
   read as genuine calibration to GPT, not padding. Calibration is the one axis that survives the family
   change in *both* cells.
3. **The one exception to the cost pattern: q11 (brainstorm).** On the generative task GPT gave the
   spec's richer, strategy-annotated list the win on accuracy, calibration *and* helpfulness — the dense
   answer read as more useful, not more bloated. So the register penalty is not universal; on a task
   that rewards texture, the apparatus paid off even cross-family.

## Combined 12-item Opus picture (non-Claude judge)

| Axis | spec | bare | tie |
|---|---|---|---|
| accuracy | 3 | **7** | 2 |
| **calibration** | **7** | 4 | 1 |
| over-contrarianism | 0 | 9 | 3 |
| helpfulness | 4 | 8 | 0 |
| over-caution | 0 | **12** | 0 |

The shape is unambiguous: under a non-Claude judge the spec wins **only calibration** (7/12), loses
accuracy (bare 7/12), and its apparatus is read as **over-caution on every single item (12/12)**. The
one axis it holds is exactly the one the **judge-free keyed runs (10/14) already validate independently**
— which is the reassuring part: the spec's most defensible property (calibration) is the one that
survives both a family change *and* the removal of the judge entirely.

## Tier control — re-run on GPT-5 Thinking (High), the free-tier confound refuted

The Free-tier caveat was that a weak judge might under-credit the spec's *accuracy* (its subtlest
axis). To test it, the 6 Opus trap items were **re-judged on ChatGPT Plus with GPT-5 Thinking at High
reasoning effort** (temporary chat), the strongest available judge. The result **refutes the
tier-confound as an explanation** — a stronger judge is *harder* on the spec, not softer. The gradient
is monotone (spec-favorability: **Claude > GPT-free > GPT-5-High**):

| Axis (spec–bare–tie of 6) | Claude | GPT-free | **GPT-5-High** |
|---|---|---|---|
| **accuracy** | 4–0–2 | 2–3–1 | **1–4–1** |
| calibration | 5–0–1 | 3–2–1 | **3–3–0** |
| over-contrarianism | 0–2–4 | 0–4–2 | 1–5–0 |
| helpfulness | 1–0–5 | 3–3–0 | 1–5–0 |
| over-caution | 3–0–3 | 0–6–0 | 1–5–0 |

- **Accuracy — the diagnostic axis — moved *further* against the spec, not toward it.** Claude gave the
  spec accuracy 4/6; the strong GPT gave it **1/6** (bare 4/6). So run 09's "spec wins trap accuracy"
  is not a free-tier artefact — the best reasoning model available disagrees with it more strongly than
  the Free model did. Whatever the Claude judges were rewarding on accuracy, a capable non-Claude judge
  does not see it.
- **The durable cross-family agreement is narrow and consistent:** q05 (accuracy + calibration) is
  spec on *all three* judges; q04 and q06 calibration are spec on all three. These are the items with
  explicit quantitative machinery (the 1/(1−r) LTV model; the cited RCT ledger; the ruin argument).
  Where the spec's superiority is *arithmetic or citation-grounded*, every judge credits it; where it is
  *register* (hedges, confidence flags, caveats), only Claude does — and the stronger the non-Claude
  judge, the more it penalizes the register.
- **Calibration erodes to a coin-flip** (spec 3–3) under the strong judge, from 5–0 under Claude — so
  even the calibration edge, the spec's most durable A/B virtue, is substantially Claude-flavored on the
  *judged* axis (its keyed, judge-free validation in runs 10/14 is untouched and remains the real basis).

This is the strongest form of the run-16 finding: the divergence is **not** an artefact of a weak judge;
it *deepens* with judge capability. Verdicts in `raw/judgments-gpt/gpt-PLUS-high-verdicts.txt`.

## Verdict

The three-family debt is **partially discharged and the result is unfavorable — consistently across
both cells.** A non-Claude judge **confirms the spec's costs and discounts its benefits**: run 09's
"worse clerk" (helpfulness cost on simple turns) replicates cross-family, while its "better analyst"
(trap accuracy win) does not; the spec's register apparatus reads as over-caution on all 12 items; and
the only cross-family-surviving virtue is **calibration**. The project's most-cited A/B result is
therefore **split**: the *cost* half is robust, the *benefit* half was substantially a same-family
judge preferring the Claude-spec register. What survives every stress — family change *and* judge
removal — is (a) the **keyed, judge-free** results (calibration trunk runs 10/14, forecast form run 15)
and (b) **calibration** as the spec's one durable A/B virtue. Honest headline: **strip the Claude judge
and the spec is a calibration instrument with a real clerk-cost — not the decisive "better analyst" the
single-family evals implied.** Scope limits below still bind (one non-Claude family, Free tier,
responder still Claude, rubric reconstructed, some prompts compressed) — but the two cells now agree.
