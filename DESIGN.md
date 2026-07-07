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
against an external answer key, independent of the grader's own judgment — which
the blind A/B protocol (Track 1) does *not* provide, and which `eval`'s Track 2
(`prompts/04-calibration.md`) exists to supply. Running only the A/B track tests
only the branch.

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

   Worse than merely unmeasured: the basis-anchoring guard has a *plausible
   mechanism to run the wrong way.* The empirical finding it rests on (the
   Prompt Report; FaR) is that requiring verbalized confidence skews models
   toward overconfidence on some instances. The guard's response — "state the
   basis before the label" — forces the model to *generate a justification* for
   whatever label it was going to emit. A required justification is easy to
   produce and makes the label read as *more* grounded, which is the exact
   surface of convincing calibration theater, not a defense against it. The
   guard may still help by making a *missing* basis visible (a label with no
   producible reason is a flag). But "anchor the label to a basis" cannot, at
   the prompt layer, close the gap between a plausible-sounding basis and a
   truly calibrated one — and by the ceiling argument above, probably nothing
   at this layer can. This is why Track 2 of the eval scores labels against an
   external key: it is the only way to tell the two apart. It has now been run
   once (single-family, directional): it found no calibration theater on that
   battery — but the result rests on a thin base (near-single-item error spread)
   and one model family, so it is suggestive, not settled (see `eval/runs/`).

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
- **The Chain-of-thought directive earns its place through auditability, not
  accuracy.** The Wharton Prompting Science series (Report 2; see REFERENCES)
  finds that on current models — which frequently produce a reasoning trace by
  default — an explicit CoT instruction yields marginal-to-negative accuracy
  effects and adds answer variance and cost. If the directive's job were to
  raise correctness, that evidence would argue for dropping it. Its job here is
  different: it forces the reasoning into the open so confidence labels can be
  anchored to a visible basis (Epistemics) and framing errors caught before the
  conclusion (Logic). That function is not what Report 2 measures. The directive
  stays — but the honest reason is auditability; anyone porting the spec to a
  strong reasoning model should read the CoT line as serving the confidence
  machinery, not as a performance booster.
- **Expert tone is a register, not an accuracy lever.** The spec sets an expert
  tone and is framed as a thinking *partner*. Report 4 (Wharton) tests the
  adjacent belief directly: assigning an expert persona ("you are a world-class
  expert in X") does not reliably improve factual accuracy across six models and
  two benchmarks, and a domain-mismatched or over-narrow role can *degrade* it
  or trigger refusals. The implication is scoped, not fatal — what Report 4
  kills is the *accuracy* rationale for an expert framing, which the spec does
  not rely on (the ceiling already denies the spec improves raw correctness).
  The expert *tone* — as register, vocabulary, and default depth — is a tone
  choice, which Report 4 notes personas legitimately serve. The framing stays,
  stripped of any implicit claim that "thinking partner" makes the model know
  more.

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
- **Strengthening the verification sentence (parametric)** — rejected. A prompt
  cannot make parametric memory more reliable by insisting; that half is at the
  ceiling of what prose can do.
- **The tool-routing half — now incorporated (Verification section).** The
  rejection above conceded that "a prompt *can* route to tools." The original
  spec left that latent, which is a real omission for tool-equipped
  deployments (agentic contexts, connected sources): "flag it for checking" is
  the wrong move when a check is one tool call away. The Verification directive
  makes the routing explicit — verify rather than defer when tooling exists —
  and carries its own counterweights (materiality threshold; treat tool output
  as evidence, not ground truth). Convergent support: FaR (see REFERENCES)
  finds that eliciting low-confidence expression itself helps *trigger*
  retrieval on hard instances — the same low-confidence → verify coupling. Note
  this is a *new behavioral directive* and therefore unvalidated; it is a
  candidate for the eval, not a proven improvement.

## Two variants

The full spec is not universally appropriate. Its sharpness directives and its
misframe-rejection actively *harm* generative and relational tasks — creative
drafting, brainstorming, emotional-support-adjacent conversation — where
committing hard and rejecting framings is the wrong register.

This is why the repo ships two artifacts, selected by different criteria:

- **`SPEC-lite.md`** — a lightweight overlay (anti-sycophancy + calibration
  with a materiality threshold + verification routing), chosen for *value
  density*: safe as a broad default across mixed tasks. It keeps the core and
  drops what carries a downside cost — the immediate misframe rejection, the
  mandatory steelman, and the forecasting/tail-risk machinery.
- **`SPEC.md`** — the full spec, chosen for *truth-tracking analytical work*
  (quantitative analysis, contested evidence, strategic decisions), where the
  overhead earns its cost.

The README routes the reader between them. Do not present the full spec as a
universal default; it isn't one. A note on status: the eval to date targets the
full spec — the lite variant is even less tested, and its downside categories
(D5 relational, D6 generative) run inverted, since that is where lite should
win and full should lose.

## For extenders — a checklist

1. Does the addition fix a *named* failure mode? If your justification is "it
   makes the spec more thorough," stop — that is the over-optimization signal,
   not a reason.
2. Does it push an existing tendency further? If so, add the counterweight in
   the same edit.
3. Does it belong in the spec at all, or in the operator's governance layer
   (like convexity)? Keep decision architecture out.
4. Is it a compulsion or a wish? Prefer the compulsion.
5. Is it an absolute command where a conditional trigger belongs? A directive
   phrased as an unconditional action ("reject immediately," "do not praise,"
   "avoid typical answers") fires even where the action is wrong, and rewards
   *performing* the directive over serving its purpose. Prefer "when X, do Y"
   so the action triggers on the need, not on every turn. This is the spec's
   most common self-inflicted failure — most of its contrarianism risk traces
   to absolute phrasing. The 2026-07-07 eval runs confirmed this empirically: the
   spec's frame-rejection register drew a measurable contrarianism/over-caution
   cost on *answerable* XY questions (a different-model judge scored the
   critique-first answer as more contrarian). The spec's sequencing counterweight in
   *Goal vs. solution* — lead with the deliverable, attach the critique — is the
   response. See `CHANGELOG` and `eval/runs/`.
6. Have you validated it? The spec is unvalidated (see `/eval`). Before adding
   the next directive, consider running the blind test on what you already
   have — one measured result is worth more than another design iteration.
