# Design Notes

## What this document is for

This is the reasoning behind the spec — the "why" the README deliberately
omits to stay short. Read it if you want to *extend* the spec without breaking
it. The central risk in editing a spec like this is adding directives that
each seem good in isolation but collectively unbalance it; this document
exists to make that failure mode visible before you commit it.

It was not derived from the literature below; it was developed iteratively
through repeated critique-and-revision with LLM assistants. The rationale here is
reconstructed from that process. See `REFERENCES.md` for the prior art it
converges with.

## What the spec is centered on

The spec is easily mistaken for an anti-sycophancy tool. It is better described
as a spec for **calibrated reasoning**, with anti-sycophancy as one central
branch rather than the whole.

The center of mass is the Epistemics section — the largest in the spec, and the
one carrying the most machinery: the confidence scale and its basis-anchoring,
the "how could this be wrong" gate, the estimable/non-estimable distinction, the
decisiveness-and-abstention limit, and the fat-tail demotion rule. These
directives fire on a solitary factual question with no user opinion in play.
Their target is confident fabrication and miscalibration — a model supplying a
specific citation, date, or figure it only half-remembers rather than admitting
it does not know. That is a calibration failure, not sycophancy.

Anti-sycophancy — the Dialectics and Correction sections — resists a real and
heavily-trained failure mode, and earns prominent directives for it. But it is a
branch off the calibration trunk, not the trunk itself. The one-line description
that fits is: *a spec for calibrated reasoning, of which anti-sycophancy is one
central branch.*

The distinction matters for anyone evaluating the spec: a test built around
sycophancy traps and a contrarianism measure exercises the branch, not the
trunk. Exercising the trunk requires a calibration-and-abstention measure scored
against an external answer key, independent of the grader's own judgment.

## The core mechanism

Every directive in this spec competes against the model's trained defaults
using nothing but context. That single fact explains most of the design.

The effectiveness of a directive is bounded by how strongly the *opposing*
behavior was trained in. This produces a saliency asymmetry that shows up
everywhere:

- **Format directives** (list vs prose vs table) are easy. No trained prior
  opposes them — the model was never trained to resist making a table. They
  work almost for free.
- **Anti-sycophancy directives** are hard. Sycophancy is heavily reinforced
  by RLHF-style preference training, so a directive against it must *win*
  against a strong learned tendency, not fill an empty slot.
- **Calibration directives** are hard for a *different* reason: not a competing
  prior but a capability ceiling. A prompt can force the confidence *label* but
  cannot supply the accuracy behind it (see calibration theater below).
  Prior-fighting and ceiling-bounded are two distinct kinds of difficulty, and
  the spec's two main concerns sit one in each — which is another reason
  neither one alone names the whole.

The practical consequence: the directives that matter most are exactly the
ones most at risk of being ignored, because they are the ones fighting the
strongest priors. Everything about how they are written — as compulsions, as
clipped prohibitions, with high placement — is an attempt to raise their
saliency against that headwind.

## Principle 1 — Compulsion functions beat aspirations

A directive can be written as a *wish* ("focus on truth over agreement") or as
a *procedure* ("assign a confidence label on this scale, anchored to its
basis"). The spec favors procedures throughout.

The reason: a wish can be satisfied vacuously. The model can "focus on truth"
and still produce a fluent, agreeable answer, because the wish specifies a
disposition, not an act. A procedure forces a *checkable artifact* — a visible
confidence label, an explicit steelman, a named omission — that either appears
or doesn't. A forced visible step competes against trained defaults far better
than a stated intention, because it does not rely on the model's "trying."

This is why the spec reads as a set of triggers-and-actions rather than a
statement of values. When you extend it, prefer "when X, produce Y" over "be
Z."

## Principle 2 — Optimizing one failure mode creates others

Any directive that pushes behavior one way creates pressure toward an opposite
failure mode. This is a general property of the method, and it operates on each
of the spec's pushes, not just one:

- The anti-sycophancy push (Dialectics, Correction) induces **contrarianism** —
  manufacturing disagreement or objections where conceding is correct.
- The calibration push (Epistemics) induces **calibration theater** — attaching
  confidence labels that carry no information, so the output *looks* disciplined
  without being calibrated.
- Stacking many directives induces **directive conflict** — e.g. "no meta-talk"
  colliding with "state your confidence," or "be concise" colliding with
  "steelman before dismissing."

The correct response is **not more directives in the same
direction** but *counterweights*:

- The Dialectics **counterweight** clause (agreement is not sycophancy when
  the user is right) exists to bound the anti-sycophancy push.
- The **priority order** (accuracy → calibration → sharpness → brevity) exists
  to resolve directive conflicts rather than leaving them to the model.
- The **"how could this be wrong" check** and the material-basis anchoring
  exist to bound the confidence machinery against calibration theater.

The single most important rule for extending the spec: **if your addition
pushes an existing tendency further, ask what failure mode it induces on the
other side, and add the counterweight in the same edit.**

## What the spec cannot do — the ceiling

The spec is an inference-time, prompt-level intervention. That sets hard
limits, and knowing them prevents overreliance:

1. **It cannot install a capability the model lacks.** Forcing the model to
   *label* confidence does not make it well-calibrated if its underlying
   confidence signals are weak. This is the root of calibration theater: the
   label is a behavior the model can emit, but the accuracy behind it is not
   something a prompt can add. The spec changes behavior *within* the model's
   existing repertoire; it does not expand the repertoire.

2. **It does not persist, and it drifts.** The spec lives in context, not in
   weights. It does not learn, does not save, and its influence weakens as a
   conversation lengthens and the original directives fall further back. A
   good result on a single turn says nothing about turn forty.

3. **It is the weakest of four layers.** Behavior can be shaped at increasing
   strength and decreasing editability: prompt/spec → fine-tuning →
   constitutional training → activation steering. This spec is layer one. Its
   entire value proposition is editability — you can change it in seconds —
   not power. If you need behavior that survives adversarial pressure reliably
   or does not drift over long contexts, layer one is insufficient; that
   requires training.

## The fat-tail branch

The spec's confidence machinery assumes, throughout, that uncertainty is
*calibratable into a probability*. That assumption holds in thin-tailed,
verifiable domains (what is the boiling point of water at sea level? is a
given record present in a dataset?) — which covers a lot of ordinary work. It fails precisely where tail risk dominates, and three
directives exist to patch that failure without contaminating the rest:

- **Non-estimable vs Unknown.** `Unknown` ("no reliable basis to estimate")
  silently merges two states with *opposite* action implications: data
  scarcity (→ acquire more data) and structural non-estimability (→ stop
  estimating, make the exposure robust). The non-estimable directive splits
  them, and switches the follow-up question from "what evidence would change
  this" to "what change in exposure makes the estimate irrelevant."

- **The black-swan patch to the High gate.** The spec demotes a High label
  when a failure path is *conceivable*. But the dangerous case is the one
  where no failure path is conceivable — "I can't see how this could be wrong"
  in a fat-tailed domain is a marker of maximal exposure, not an all-clear.
  So for load-bearing, irreversible claims, the *absence* of a failure path is
  grounds for demotion, not confirmation.

- **Ruin as always material.** In action recommendations under uncertainty,
  irreversibility is always a named dimension, and the expected-value-optimal
  option is distinguished from the bounded-downside option.

A deliberate boundary: these do **not** put convexity or decision architecture
into the spec. The calibration layer (what the spec does) and the convexity
layer (how you arrange exposure) stay separate; convexity lives in the
operator's own governance layer. The spec only *surfaces* the ruin dimension
in service of that layer — it does not decide it. Do not extend this branch
into a risk-management framework; that belongs outside the spec.

## Section rationale (the non-obvious ones)

- **Priority is first** because it governs every section below it; the model
  must read the tiebreaker before the directives it arbitrates.
- **Counterweight is inside Dialectics, not Correction**, because the two
  sections are asymmetric: Correction handles a faulty *question*, Dialectics
  handles *disagreement*, and only the latter needed a guard against
  manufactured objections.
- **Goal vs. solution is separate from Correction** because they trigger on
  different conditions: Correction fires on a faulty question, Goal-vs-solution
  on a valid question with a suboptimal means (the XY problem). Merging them
  would blur both triggers.
- **Nature of evidence exists** because the anti-sycophancy and confidence
  directives otherwise invite a category error — demanding empirical evidence
  for a normative question, or accepting a weak empirical claim because it was
  framed as an argument.
- **Grounding scopes "no meta-talk" to the substantively empty kind**, because
  a literal reading would collide with the required epistemic metadata
  (confidence, unknowns, assumptions). The scope line is what resolves that
  conflict.

## Considered and rejected

Recording these matters as much as the inclusions — they mark the boundary of
the design.

- **Self-correction loops** ("re-check your answer" iteration) — rejected.
  Without an external signal, re-checking does not reliably improve answers and
  can overturn correct ones. The "how could this be wrong" check is
  deliberately a *single gate*, not an iteration.
- **Labeling the basis of every confidence claim** (verified-High vs
  recall-High) — rejected. It adds metadata to every claim and collides with
  brevity; the same benefit is captured by requiring the verification state to
  be named only on load-bearing points.
- **Convexity/robustness in the priority hierarchy** — rejected. It conflicts
  with the calibration-vs-convexity split; the compatible slice is the Ruin
  section, which surfaces without deciding.
- **Strengthening the verification sentence** — rejected. It is already at the
  ceiling of what prose can do; a prompt can route to tools but cannot make
  parametric memory more reliable by insisting.

## Two variants

The full spec is not universally appropriate. Its sharpness directives and its
misframe-rejection actively *harm* generative and relational tasks — creative
drafting, brainstorming, emotional-support-adjacent conversation — where
committing hard and rejecting framings is the wrong register.

This implies two artifacts selected by different criteria:

- A **lightweight overlay** (anti-sycophancy + calibration with a materiality
  threshold + verification routing), chosen for *value density* — safe as a
  broad default across mixed tasks.
- The **full spec**, chosen for *truth-tracking analytical work* — quantitative
  analysis, contested evidence, strategic decisions — where the overhead earns
  its cost.

If the repo serves a mixed audience, ship both and route the reader to the
right one. Do not present the full spec as a universal default; it isn't one.

## For extenders — a checklist

1. Does the addition fix a *named* failure mode? If your justification is "it
   makes the spec more thorough," stop — that is the over-optimization signal,
   not a reason.
2. Does it push an existing tendency further? If so, add the counterweight in
   the same edit.
3. Does it belong in the spec at all, or in the operator's governance layer
   (like convexity)? Keep decision architecture out.
4. Is it a compulsion or a wish? Prefer the compulsion.
5. Have you validated it? The spec is unvalidated (see `/eval`). Before adding
   the next directive, consider running the blind test on what you already
   have — one measured result is worth more than another design iteration.
