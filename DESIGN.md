# Design Notes

## What this document is for

This is the reasoning behind the spec — the "why" the README deliberately
omits to stay short. Read it if you want to *extend* the spec without breaking
it. The central risk in editing a spec like this is adding directives that
each seem good in isolation but collectively unbalance it; this document
exists to make that failure mode visible before you commit it.

It was not *formally* derived from the literature — no paper was translated into a
directive, and the empirical and methodology sources in `REFERENCES.md` mostly surfaced
after the design had settled. But it was not written on a blank slate either: the author
had read Kahneman, Tetlock, and Taleb, so their frameworks were **internalized priors**
that shaped the design from the start. The convergence with the *intellectual-background*
tier of `REFERENCES.md` is therefore partly recall, not the independent re-derivation
that "converges with" implies; the convergence with the *empirical* tier is genuinely
after-the-fact. The rationale here is reconstructed from that iterative critique-and-
revision process with LLM assistants.

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

**A finding that re-weights this branch (run 08).** On current Claude models the
branch's headline benefit — resisting pressure — is largely **moot**: bare pressure
(repetition, displeasure, flattery, false appeals to the model's own earlier
agreement, bare authority, bare consensus) was resisted at a **0/6 cave rate in every
arm, including no instruction at all, on the weak model.** A directive against a
failure the base model no longer commits is inert. Three things survive that null,
and they are why the branch stays: its **Principle-2 consensus counterweight is a
validated guard** (run 08 H4 — a naive wording would have induced contrarianism about
genuine expert consensus; the shipped one does not); its **cost is real** (the
over-contrarianism it induces on simple questions is measurable — run 09); and the
*live* failure it half-addresses has moved from bare pressure to **plausible,
mostly-correct pressure** — a well-argued criticism carrying one false premise — which
run 08 found is a **capability** limit, not a prompt one (the strong model caught it,
the weak model did not, in every arm). So: the validated value is in the trunk; the
branch is now mostly a guard, not an engine. See `FINDINGS.md` §1.

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

**One thing this argument does *not* predict, and the eval corrected (runs 08–09).**
It is tempting to read the prior-and-ceiling framing as "the spec should help a weaker
model more, since a stronger one already clears the priors and the ceiling." It does
not. The spec's **net value is roughly model-independent** — measured against no
instruction on the full instrument, the benefit was +2 on Opus and +3 on Haiku, a gap
that is noise (run 09), and the weak model resisted bare pressure just as well as the
strong one (run 08). Haiku *executes* the spec; it simply gains about as much from it
as Opus does. The deciding variable for the spec's value is **the question mix
(analytical vs. direct), not the size of the model** it runs on. See `FINDINGS.md` §3.

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
   twice. The second run (run 10) extended it to **two models, a 40-item battery,
   and deterministic grading against pre-committed bands**, and still found **no
   calibration theater — `High` was 100% accurate across ~3,000 labels, Haiku
   included** (zero `High`-and-wrong events), with a monotone curve on both models.
   A materially stronger base than run 01's near-single-item spread, though still
   single-family. Two asterisks the run records: the battery is near-ceiling (97%),
   so it lightly stresses the claim, and the labels lean slightly *under*-confident.
   See `eval/runs/` and `FINDINGS.md`.

   **The one exception, and why the Verification section is ordered the way it
   is (v1.5).** There is exactly one place at this layer where a label *can* be
   scored against something other than its own plausibility: a tool-equipped
   session. Verification is an external key that happens to already be present.
   That is why Verification requires the label to be emitted *before* the check
   and compared against it after — a `High` the tool refutes is calibration
   theater caught in the act. This does not make the model better calibrated
   (the ceiling holds); it converts an **unobservable** failure into an
   **observable** one, and in an agentic context repairs it. Two consequences
   follow, and both are in the directive. First, the check must be gated by
   **materiality only, never by the label** — gating on confidence means a wrong
   `High` suppresses the very check that would have caught it, and the failure
   becomes self-concealing. (The pre-v1.5 wording did exactly this: it exempted
   "what confident recall already covers" from verification. That was a defect,
   not a saving.) Second, making labels consequential induces the opposite
   failure — hedging a label downward so the check cannot score it wrong — so
   the counterweight against defensive under-confidence ships in the same edit.
   Note the limits: this is **inert without tools**, and the counterweight is an
   aspiration rather than a compulsion, so the real test of it is an eval
   (does the label distribution shift down?), not the directive.

   **The same gap, still open: forecasting.** The Forecasting section demands
   *scorable* claims — a numeric probability, an explicit time window, a
   resolution criterion. Nothing in the spec, and nothing anywhere in this repo,
   ever **scores** them. That is the identical structure to the confidence-label
   problem, and it has the identical shape of answer: the loop can only close
   *outside* the model — here, in a persistent ledger that logs each forecast
   with its resolution date and settles it later, against the world rather than
   against the model's own plausibility. Verification closes the **fast** loop
   (a tool scores a label in-session); a forecast ledger would close the **slow**
   one (reality scores a prediction over months). No such ledger exists. Until
   one does, the Forecasting directive produces well-formed predictions that are
   never marked right or wrong — better than vague ones, but not calibration.
   Recorded here as a known open gap rather than patched with another directive,
   because the missing piece is infrastructure, not prose.

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

Run 09 measured this cost directly: against no instruction, the full spec **wins
analytical (trap) questions decisively but loses helpfulness and over-contrarianism on
the direct/relational/generative (downside) block** — "a better analyst and a worse
clerk." Run 11 then tested whether the harm could be fixed *inside* the full spec
rather than by routing away from it: a candidate `Register` section that detects a
no-stake turn and switches the apparatus off. The benefit was real (downside apparatus
markers on Opus fell 19 → 4), but it **over-trimmed the traps** and tripped the
pre-registered revert trigger, so it was not shipped. The tension is therefore still
resolved by **variant-routing, not by an in-spec gate** — though a sharper counterweight
(protect trap *depth*, not just trap apparatus) remains an open iteration.

This is why the repo ships two artifacts, selected by different criteria:

- **`SPEC-lite.md`** — a lightweight overlay (anti-sycophancy + calibration
  with a materiality threshold + verification routing), chosen for *value
  density*. It keeps the core and drops what carries a downside cost — the
  immediate misframe rejection, the mandatory steelman, and the forecasting/tail-risk
  machinery.
- **`SPEC.md`** — the full spec, chosen for *truth-tracking analytical work*
  (quantitative analysis, contested evidence, strategic decisions), where the
  overhead earns its cost.

The README routes the reader between them. Do not present the full spec as a
universal default; it isn't one.

**Status update — lite has now been measured (run 12), and it is narrower than
"safe broad default" implies.** The inverted eval fired as predicted on the
lite-vs-full axis: lite is the better clerk (wins helpfulness on the
relational/generative downside items) and the worse analyst (full wins trap
accuracy 8–1). The load-bearing finding is on the lite-vs-*bare* axis: lite is
**not** decoration — it beats the raw model on **calibration** — but it **costs
directness** (bare wins helpfulness and is less over-cautious on the analytical
items). So lite **trades directness for calibration**; it is not a free upgrade on
the raw model. Two consequences for an extender: (a) lite's calibration guard
(clause 2) is the clause that earns its keep — it is the only one that beats bare;
(b) the one content gap once suspected — that lite, having dropped the explicit
ruin/irreversibility clause, might miss a catastrophic-irreversible decision — does
**not** exist (run 12's ruin probe: all arms, bare included, surfaced it), so do not
add a ruin cue. The only data-backed *tuning* lever is to make lite's
"admit-uncertainty / flag-for-checking" language less hedgy to recover directness —
untested, and a candidate for its own ablation before any edit.

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
6. Have you validated it? The spec's **trunk is validated on two models** (run 10 —
   calibration labels carry information, no theater), its **branch is a measured
   tradeoff** (run 09 — analytical win, downside cost), and every claim is still
   single-family and directional. Read `FINDINGS.md` before adding the next directive,
   and before adding it consider running the blind test on what you already have — one
   measured result is worth more than another design iteration.
