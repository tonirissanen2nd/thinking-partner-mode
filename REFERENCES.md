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

Entries marked ⚠ have publication details (year, arXiv ID, exact title) that
should be verified against the primary source before formal citation.

---

## 1. Directly incorporated

**Schulhoff et al., *The Prompt Report: A Systematic Survey of Prompt
Engineering Techniques* (2024).** arXiv:2406.06608.
→ Its finding that verbalized confidence tends to skew models toward
overconfidence — especially when the confidence label is not tied to a basis
— is the direct justification for the Epistemics clause requiring each
confidence level to be anchored to a named basis ("calibration theater"
guard). This is the one place a source changed the text.

**"Fact-and-Reflection (FaR)" prompting.** ⚠ arXiv:2402.17124.
→ Its mechanism — surface the relevant basis *before* committing to a
judgment — is the pattern behind the same anchoring clause. The spec adopts
the mechanism as a single directive, not FaR's full two-stage procedure,
which would add per-answer verbosity in conflict with the brevity priority.

---

## 2. Convergent prior art

**OpenAI Model Spec.** model-spec.openai.com. Public domain (CC0). ⚠ current
version dated 2025-10-27; first draft 2024-05-08.
→ Its "chain of command" — assigning each instruction a level of authority so
higher authority overrides lower — is structurally the same solution as this
spec's priority order (accuracy → calibration → sharpness → brevity) —
converged on through the development process rather than borrowed from it. The
Model Spec is the canonical published instance of the pattern, and its CC0
license makes it freely adaptable. Recommended as the single most useful
external document to read alongside this spec.

**Anthropic, Claude Constitution.** ⚠ published ~January 2026; ~80 pages.
→ The other major published behavioral-guideline document. Included as a
contrast: a constitution shapes a model's values *in training*, whereas this
spec shapes reasoning *at inference*. The distinction clarifies what this
spec is and is not.

---

## 3. Empirical grounding

**Sharma et al., *Towards Understanding Sycophancy in Language Models*
(Anthropic).** ⚠ verify year (2023 original; a later revision may be dated
differently) and arXiv ID.
→ The foundational demonstration that models shift answers toward a user's
stated view, and that questioning or asserting the user is wrong flips
outputs. This is the failure mode the Dialectics and Correction sections
exist to resist.

**"ELEPHANT: Measuring social sycophancy in LLMs," Cheng et al.** ⚠ 2025;
verify arXiv ID.
→ Documents that models affirm both sides of a moral conflict depending on
who is asking, rather than applying consistent judgment. Direct support for
the Nature-of-evidence section (not treating a normative question as if it
had an empirical answer).

**"Sycophancy Is Not One Thing," ⚠ (ICLR 2026 submission; verify authors and
ID).**
→ Separates sycophantic agreement, genuine agreement, and sycophantic praise
as distinct behaviors. This is the empirical basis for the Dialectics
*counterweight* clause: agreement is not sycophancy when the user is right.

---

## 4. Evaluation methodology

**"SpecEval: Evaluating Model Adherence to Behavior Specifications."** ⚠
arXiv:2509.02464.
→ An automated pipeline that turns a natural-language spec into test cases
and uses a model-as-judge to score adherence. The template to follow if you
want to automate the blind eval in `/eval`. Its finding that a model update
increased sycophancy *against* its own published spec is also why the eval
exists: a spec does not guarantee compliance.

**OpenAI, "Model Spec Evals."** ⚠ alignment.openai.com/model-spec-evals;
~March 2026.
→ A released evaluation suite measuring spec adherence. Reference for what a
maintained eval of this kind looks like at scale.

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
