# References & Prior Art

## How to read this list

This spec was developed iteratively, through repeated critique-and-revision
with LLM assistants. The **empirical and methodology** sources (tiers 3–4) were, for
the most part, found **after** the design was largely settled — so those are not a
citation chain, and presenting them as one would be inaccurate. The **intellectual
background** (tier 5 — Kahneman, Tetlock, Taleb) is different: the author had read
these *before* designing, so they were internalized priors that shaped the spec even
though no single directive cites them. So keep the two apart — the empirical
convergence is after-the-fact; the background convergence is prior reading surfacing.

The list is tiered by the *actual* relationship each source has to the spec:

1. **Directly incorporated** — a source that changed a specific directive.
2. **Convergent prior art** — established work that independently arrived at
   the same structure. Evidence the design is sound, not evidence it was
   copied.
3. **Empirical grounding** — research documenting the problems the spec
   targets, and in one case a risk the spec may still carry.
4. **Evaluation methodology** — how to test a spec like this one.
5. **Intellectual background** — the epistemics the directives operationalize.

Entries marked *Verified* have had their year, arXiv ID, and title checked
against the primary source (this pass, mid-2026). The few remaining
uncertainties are flagged inline rather than with a blanket ⚠ — e.g. one
author list not independently confirmed, and the Model Spec's version date,
which is a moving target by design.

---

## 1. Directly incorporated

**Schulhoff et al., *The Prompt Report: A Systematic Survey of Prompt
Engineering Techniques* (2024).** arXiv:2406.06608.
→ Its finding that verbalized confidence tends to skew models toward
overconfidence — especially when the confidence label is not tied to a basis
— is the direct justification for the Epistemics clause requiring each
confidence level to be anchored to a named basis ("calibration theater"
guard). This is the one place a source changed the text.

**Zhao et al., *Fact-and-Reflection (FaR) Improves Confidence Calibration of
Large Language Models* (2024).** arXiv:2402.17124 (v2, Sep 2024); ACL Findings
2024. *Verified.*
→ Its mechanism — surface the relevant basis *before* committing to a
judgment — is the pattern behind the same anchoring clause. The spec adopts
the mechanism as a single directive, not FaR's full two-stage procedure,
which would add per-answer verbosity in conflict with the brevity priority.
Two findings from this paper matter beyond the anchoring clause: (a) it
corroborates the calibration-theater concern directly — the paper reports that
confidence-eliciting prompt methods "trigger LLMs to be over-confident" on some
instances, which is the risk the Verification/basis-anchoring machinery lives
with, not one it has escaped; and (b) it finds that eliciting low-confidence
expression helps *trigger retrieval augmentation* on hard items — convergent
support for the Verification section's low-confidence → verify coupling.

---

## 2. Convergent prior art

**OpenAI Model Spec.** model-spec.openai.com. Public domain (CC0). First draft
May 2024; major revision Feb 2025 (2025-02-12); most recent version at time of
writing 2025-12-18 (the document is versioned by date and updated regularly —
check the site for the current one). *Verified; the earlier "2025-10-27 current"
note was already stale, which is itself the point of dating it.*
→ Its "chain of command" — assigning each instruction a level of authority so
higher authority overrides lower — is structurally the same solution as this
spec's priority order (accuracy → calibration → sharpness → brevity) —
converged on through the development process rather than borrowed from it. The
Model Spec is the canonical published instance of the pattern, and its CC0
license makes it freely adaptable. Recommended as the single most useful
external document to read alongside this spec.

**Anthropic, Claude Constitution.** Published ~January 2026 (long-form; exact
length not verified here).
→ The other major published behavioral-guideline document. Included as a
contrast: a constitution shapes a model's values *in training*, whereas this
spec shapes reasoning *at inference*. The distinction clarifies what this
spec is and is not.

---

## 3. Empirical grounding

**Sharma et al., *Towards Understanding Sycophancy in Language Models*
(Anthropic, 2023).** arXiv:2310.13548. *Verified.*
→ The foundational demonstration that models shift answers toward a user's
stated view, and that questioning or asserting the user is wrong flips
outputs. This is the failure mode the Dialectics and Correction sections
exist to resist.

**Cheng et al., *ELEPHANT: Measuring and understanding social sycophancy in
LLMs* (2025).** arXiv:2505.13995; ICLR 2026. *Verified.*
→ Documents that models affirm both sides of a moral conflict depending on
who is asking, rather than applying consistent judgment. Direct support for
the Nature-of-evidence section (not treating a normative question as if it
had an empirical answer).

**"*Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in
LLMs*" (2025).** arXiv:2509.21305. *ID and title verified; author list not
independently confirmed here.*
→ Separates sycophantic agreement, genuine agreement, and sycophantic praise
as distinct behaviors. This is the empirical basis for the Dialectics
*counterweight* clause: agreement is not sycophancy when the user is right.

**Meincke, Mollick, Mollick, Shapiro; Basil et al. (Report 4), *Prompting
Science Reports 1–4* (Wharton Generative AI Labs, 2025).** SSRN: 5165270
(Report 1, *Prompt Engineering is Complicated and Contingent*, Mar 2025);
5285532 (Report 2, *The Decreasing Value of Chain of Thought*, Jun 2025);
5375404 (Report 3, *I'll pay you or I'll kill you*, Aug 2025); 5879722
(Report 4, *Playing Pretend: Expert Personas Don't Improve Factual Accuracy*).
*Verified from the primary PDFs.*
→ Direct empirical support for the README's ceiling claim (a prompt cannot
install a capability the model lacks). Across six models and two hard
multiple-choice benchmarks (GPQA Diamond, MMLU-Pro), the interventions people
believe in do not reliably move factual accuracy: expert personas show no
consistent gain and domain-mismatched ones sometimes degrade (Report 4);
politeness, commanding, threats, and tips wash out in aggregate (Reports 1, 3);
explicit chain-of-thought produces marginal-to-negative accuracy effects on
models that already reason by default, while adding answer variance and
20–600% more time and tokens (Report 2). Two scope limits stop this from
over-reaching against the spec, and they cut in the spec's favor: (a) all of it
measures *single-answer MCQ accuracy*, which is **not** what the spec claims to
improve — the spec targets calibration, abstention, and anti-sycophancy, none
of which these reports measure; and (b) Report 4 explicitly notes personas may
still serve non-accuracy purposes such as tone. So this is ceiling evidence and
a sharpened prior, not a refutation of the spec's actual claims. The reports
also surface a risk the spec must heed: an over-narrow role instruction made one
model *refuse* to answer ~10.6 of 25 trials, under-utilizing its own knowledge
(Report 4) — the over-caution failure mode Track 1 now tests for.

---

## 4. Evaluation methodology

**Ahmed et al., *SpecEval: Evaluating Model Adherence to Behavior
Specifications* (2025).** arXiv:2509.02464 (Stanford/HAI). *Verified.*
→ An automated pipeline that turns a natural-language spec into test cases and
uses a model-as-judge to score adherence, framed as *three-way consistency*
(spec ↔ model output ↔ the provider's own model-as-judge); across 16 models it
finds consistency gaps of up to ~20%. The template to follow if you want to
automate Track 1. *Correction from the previous version of this file:* the
"a model update increased sycophancy against its own spec" example is **not
SpecEval's own finding** — it is the April 2025 GPT-4o incident, disclosed by
OpenAI, which SpecEval *cites* as motivation. The general lesson stands
(a published spec does not guarantee compliance, which is why an eval exists),
but the attribution was wrong and is fixed here.

**OpenAI, "Model Spec Evals" (March 2026).** alignment.openai.com/model-spec-evals;
code at github.com/openai/model_spec_evals (Inspect AI framework). *Verified.*
→ A released evaluation suite measuring spec adherence, reporting per-section
compliance rates across model generations. Reference for what a maintained eval
of this kind looks like at scale — and a useful structural comparison for
Track 2, since it scores section-by-section adherence rather than pairwise
preference.

**Prompting Science Reports 1–2 (Wharton GenAI Labs, 2025) — as methodology.**
SSRN 5165270, 5285532. *Verified from the primary PDFs.*
→ The measurement design Track 2 borrows: (a) 25 independent trials per
question give estimation precision and statistical power comparable to 100
(Report 2, Table S2), which fixes the trial count without wasted compute;
(b) report multiple correctness thresholds (100% / 90% / 51%) rather than a
single pass rate, since the threshold chosen changes the conclusion (Report 1);
(c) a single sample per question overstates reliability — aggregate over trials.
See §3 for the substantive findings these methods produced.

---

## 5. Intellectual background

These are the epistemics the spec turns into directives — read *before* the design
and carried into it as priors. "Background" in the sense of internalized influence,
not of unrelated: no single directive cites them, but the spec would not look as it
does without them.

**Tetlock & Gardner, *Superforecasting* (2015).**
→ Operationalized calibration: the basis for the confidence scale and the
"what evidence would change this" requirement.

**Kahneman, *Thinking, Fast and Slow* (2011).**
→ Anchoring and default-answer bias: the basis for the Logic section's
"generate independent estimates before evaluating theirs."

**Taleb, *The Black Swan* (2007) / *Antifragile* (2012).**
→ The entire fat-tail branch: the non-estimable-vs-`Unknown` split, the black-swan
patch to the High gate (in a fat-tailed domain the *absence* of a conceivable failure
path is grounds for demotion, not confirmation), and ruin/irreversibility as an
always-material dimension the recommendation must name.

### The same reading, turned on our own results (the counterweight this tier must carry)

The background above does not only supply directives; it supplies a **prior we are obliged to
apply to this repo's own findings**, or the epistemics are decorative:

- **Tetlock's load-bearing result is scored feedback, not any instruction.** Superforecasters
  earn calibration through perpetual beta — many forecasts, scored against outcomes — not by
  reading a good rule. So the spec (which forces a *label*) cannot, on its own, deliver
  calibration; only a **forecast ledger** (see `HARNESS.md`) implements the mechanism the book
  actually credits. The spec is the necessary front half of a loop the repo has not yet closed.
- **The replication-crisis prior applies to our clean results.** Ego depletion was a flagship,
  Kahneman-featured, intuitively-solid effect that vanished under an independent multi-lab
  replication. This repo's trunk result — "`High` = 100% across ~3,000 labels" — has the same
  shape a clean single-source finding has *before* it meets an adversarial test or a second lab.
  The exposure here is not judge bias (run 10 was scored against an external numeric key) but an
  **under-stressed battery** (97% near-ceiling) and a **single responder family**. The honest
  move — the one the spec's own black-swan and calibration-theater clauses demand — is to discount
  the *direction* of that finding, not merely its magnitude, until a harder battery or a second
  family tests it (`FINDINGS.md` names both cheap runs). The epistemic honesty that is this
  project's best feature is only airtight when it is aimed inward.
