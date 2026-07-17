# Results — three-family run: a non-Claude judge (run 16)

**TL;DR — the project's largest standing debt, partially paid, and it cost the project.** Every prior
judged result was Claude-judging-Claude. This run had a genuine **non-Claude judge** (OpenAI GPT, via
ChatGPT) re-score run 09's existing blind A/B pairs on the **Opus trap cell (q01–q06)** — the exact
inputs the two Claude judges saw. The non-Claude judge **diverges sharply**, and the divergence runs
*against* the spec: it does **not** reproduce run 09's "spec wins accuracy/calibration on traps"
sweep, and it **inverts** the spec on the over-caution axis. The single most important caveat is scope
(one cell, 6 items, one non-Claude family, Free-tier model) — but within that scope the signal is
strong and one-directional, and it is the first evidence that a material part of the spec's measured
advantage was **Claude judges preferring the Claude-spec register**, not a family-independent quality gain.

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

- **Scope: one cell.** Opus trap items only (6). Haiku traps and all 12 downside items were **not run**
  — driving long blind pairs through a browser UI is costly and fragile, so this is a deliberate
  6-of-24 subset, not a silent cap. The downside block (where run 09 found the spec *loses* helpfulness
  to bare) is exactly where a non-Claude judge might diverge in the spec's *favor* or against it; untested.
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

## Verdict

The three-family debt is **partially discharged and the result is unfavorable**: a non-Claude judge
does not reproduce the spec's trap accuracy/calibration sweep and inverts its over-caution scoring.
The project's most-cited A/B result (run 09's "better analyst") is **downgraded to judge-family-
dependent** — robust to a Claude judge, roughly a wash-to-negative on accuracy under a GPT judge,
with the calibration apparatus read as padding. What survives cleanly is (a) the **keyed, judge-free**
results — the calibration trunk (run 10/14) and forecast well-formedness (run 15) — which no judge
touched, and (b) the spec's advantage on the two items where it out-reasons rather than out-hedges.
The honest headline update: **the spec is a purposeful register whose value a same-family judge scores
much higher than a cross-family judge does — and the part that survives the family change is the
reasoning, not the apparatus.**
