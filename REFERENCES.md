# References & Prior Art

## How to read this list

This spec was developed iteratively, through repeated critique-and-revision
with LLM assistants. The sources below were, for the most part, found **after**
the design was largely settled — so this is not a citation chain. Presenting it
as one would be inaccurate.

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

---

## 5. Intellectual background

These are the epistemics the spec turns into directives. Background, not
sources.

**Tetlock & Gardner, *Superforecasting* (2015).**
→ Operationalized calibration: the basis for the confidence scale and the
"what evidence would change this" requirement.

**Kahneman, *Thinking, Fast and Slow* (2011).**
→ Anchoring and default-answer bias: the basis for the Logic section's
"generate independent estimates before evaluating theirs."
