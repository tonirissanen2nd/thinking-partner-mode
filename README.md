# Thinking Partner Mode

A behavioral specification for LLM assistants that prioritizes calibrated
reasoning over agreeableness. It instructs the model to assign explicit
confidence levels, steelman counter-arguments, reject misframed questions,
distinguish empirical from normative claims, and flag what it left out —
instead of defaulting to fluent, confident, user-pleasing answers.

**Get the spec:** [`SPEC.md`](SPEC.md) — the full version, for analytical work — or
[`SPEC-lite.md`](SPEC-lite.md), a calmer, better-calibrated everyday register. (Which one,
and why, is in *When to use it* below.)

This is a **system prompt / custom instruction**, not a tool or a model. Put it
wherever your tool **re-injects it** — a custom-instructions or project-instructions
field, a `CLAUDE.md`, a system prompt your client re-sends each turn. That re-injecting
layer is your **harness**, and it is the half of the system most people skip: paste the
spec once into a chat and it works for a one-off, but it decays as the conversation
grows, so **where you put it matters more than any clause in it** (see *What it is and
isn't* for the two-layer picture).

**What twelve evaluation runs found, in one line:** the spec is a **purposeful analytical
register — "a better analyst and a worse clerk"** — whose confidence labels are honest
and whose value is roughly **independent of model size** (it scales with *what you ask*,
not *what you run it on*). Its calibration trunk is validated on two models; its
anti-sycophancy branch mostly guards against a failure current frontier models no longer
commit. Use it for analytical work, not to "stop the model being sycophantic." The full
story is in [`FINDINGS.md`](FINDINGS.md).

## What it is and isn't

It is an **inference-time behavioral spec**: directives that compete against a
model's trained defaults using nothing but context. Against the alternatives you
actually have — nothing, or a generic "be thorough and honest" instruction — what
it buys is measured: a decisive edge on analytical questions and confidence labels
that carry information (see [`FINDINGS.md`](FINDINGS.md)). What it cannot do is
exceed the model's underlying capability, persist on its own, or survive long-context
drift — those need a training-level intervention, which is a different thing built by
different people.

That ceiling is worth being concrete about: a directive can force the model to
*label* its confidence, but cannot make a poorly-calibrated model well-calibrated.
It changes behavior within the model's existing repertoire; it does not expand that
repertoire. Expect it to surface uncertainty and catch framing errors more
reliably; do not expect it to make the model know things it doesn't.

**Where to put it — and why that matters more than any directive in it.** The spec
lives in context, so its influence weakens as a conversation lengthens: a good result
on turn one says little about turn forty. That drift is real, but it is a **harness**
limit, not a prompt limit, and the fix is one layer up. Put the spec somewhere your
tool **re-injects** — a `CLAUDE.md`, a project-instructions file, a system prompt your
client re-sends every turn — rather than pasting it once into a chat and hoping. Treat
this as **layer one of a two-layer system**: the spec supplies the behavior, the
harness supplies the persistence. No clause inside the spec can substitute for the
second layer, and adding more clauses to compensate for its absence is the classic way
to make a long instruction file worse. [`HARNESS.md`](HARNESS.md) sketches what that
second layer could be — a thin per-turn harness that also picks *which* register a turn
wants (the eval's clearest finding is that the model can't do that reliably itself).

## Status: honest

This spec is a **well-reasoned design, not a validated tool.** It was
developed iteratively through repeated critique-and-revision with LLM
assistants, not by translating the research literature into directives (the
empirical sources mostly surfaced late). But not on a blank slate: the author
had read Kahneman, Tetlock, and Taleb, so those frameworks were internalized
priors behind the design — the convergence with them is partly recall, not pure
independent re-derivation (see [`REFERENCES.md`](REFERENCES.md)).

It has now been through **twelve pre-registered runs** — including two-model runs and a
calibration track scored against an external key — but all of it is **single model family
(Claude judging Claude) and directional**, never the mandated three-family design (see
`eval/runs/` and [`FINDINGS.md`](FINDINGS.md)). What that program found is more useful, and
more complicated, than "we haven't tested it":

- Its calibration claim is **validated on two models** — the confidence labels carry real
  information and show no calibration theater (run 10).
- Its **"reduces sycophancy" claim is largely moot** on a current frontier model: the base
  model already resists bare pressure unprompted, weak model included (run 08).
- Its **over-contrarianism cost is real** — measured, not just feared, on simple and
  relational questions (run 09).
- Whether it **works across languages is still untested** — the runs are English only.

If you want confidence in the effect size, run the three-family protocol in `/eval`. The spec
is revised through an iterate-and-measure loop: each change is A/B-tested against the version
before it and reverted if the eval doesn't back it (three changes have been reverted or
withheld on that rule). That loop is directional — better-motivated design, not proven results.
For the current version and what each change rests on, see `CHANGELOG.md`; for the synthesis,
`FINDINGS.md`; for the runs themselves, `eval/runs/`.

One documented risk worth knowing before you rely on it: verbalized
confidence labels can *increase* overconfidence rather than fix it
(calibration theater). The spec guards against this by requiring each label
to be anchored to a named basis — but that guard is weaker than it looks.
Forcing the model to state a basis makes it *generate a justification* for
whatever label it was already going to emit, which can make a wrong label read
as *more* grounded, not less. The guard plausibly still helps by making a
*missing* basis visible, but it cannot close the gap between a plausible-sounding
basis and a genuinely calibrated one at the prompt layer. The only way to tell
those apart is to score labels against an external answer key — which is exactly
what `eval` Track 2 does. It has now been run on **two models** with deterministic
grading (run 10): it found **no calibration theater — `High` was 100% accurate across
~3,000 labels, the weak model included** — with a monotone curve, and the spec ordered
its labels better than a plain one-liner. Two honest asterisks: the battery is
near-ceiling (97%), so it stresses the claim only lightly, and the labels lean slightly
*under*-confident. Still single-family, so directional — but a far stronger base than the
first pass. Treat the confidence labels as trustworthy where they say `High`, and as a
discipline that surfaces reasoning elsewhere.

## Repository contents

| Path | What it is |
|---|---|
| [`SPEC.md`](SPEC.md) | The full spec (English). The calibration-first version — paste into your assistant for analytical work. |
| [`SPEC-lite.md`](SPEC-lite.md) | The lightweight overlay — the calibration/anti-sycophancy core without the sharpness. Better-calibrated than the raw model, at some cost in directness (run 12). |
| [`DESIGN.md`](DESIGN.md) | The reasoning behind the spec — mechanism, principles, limits, and how to extend it without breaking it. |
| [`FINDINGS.md`](FINDINGS.md) | Top-level synthesis of what the twelve eval runs established — read this before adopting or extending. |
| [`HARNESS.md`](HARNESS.md) | A reference design for the *second* layer — a thin per-turn harness that deploys the spec conditionally. A sketch, not shipped code. |
| [`eval/`](eval/) | Two-track evaluation: blind A/B (branch) + calibration (trunk), with prompts and scoresheets. |
| [`eval/README.md`](eval/README.md) | Track 1 — the blind A/B test that removes the obvious biases; routes to Track 2. |
| [`eval/prompts/04-calibration.md`](eval/prompts/04-calibration.md) | Track 2 — calibration & abstention scored against an external key (measures the claim Track 1 can't). |
| [`eval/runs/`](eval/runs/) | Completed eval runs — one folder each (pre-registration + results + raw artifacts). Directional and single-family so far; not yet three-family. |
| [`REFERENCES.md`](REFERENCES.md) | Prior art, empirical grounding, and where to verify claims — tiered by actual relationship to the spec. |
| [`LICENSE`](LICENSE) | MIT. |

## When to use it — and which variant

Two variants, chosen by task type:

**Full (`SPEC.md`)** — for quantitative analysis, contested-evidence questions,
and strategic decisions, where surfacing uncertainty and resisting your own
framing has real value. A known cost: it makes the model blunter and more
willing to push back. That is the point, not a bug — but it is the wrong
default for warm or creative work.

**Lite (`SPEC-lite.md`)** — a calmer everyday register: honest and calibrated
without the sharpness. It keeps the anti-sycophancy and calibration core but drops
the immediate misframe rejection, the mandatory steelman, and the forecasting/tail-risk
machinery — the directives that make the full spec a poor fit for generative or
relational tasks.

Reach for Full when the work is analytical and the overhead earns its cost. The full
spec's priority order (accuracy → calibration → sharpness → brevity) arbitrates its
internal conflicts, but you will still feel the overhead on easy questions — which is
the reason Lite exists.

**The eval backs the routing, and pins down what Lite actually is (runs 09, 12).** Run 09
located the full spec's cost precisely where this split predicts it: against no instruction,
the full spec won analytical questions decisively (accuracy 12–0 on traps) but lost
helpfulness and over-contrarianism on the direct/relational/generative block. Run 12 then
measured Lite directly, and the honest picture is narrower than "safe broad default": against
the full spec, Lite is the **better clerk** (wins helpfulness on everyday turns) and the
**worse analyst** (full wins trap accuracy 8–1); against *nothing*, Lite is **not**
decoration — it is **better calibrated** than the raw model (the one thing the base model
doesn't already do) — but it **costs some directness** (the raw model is more helpful and less
cautious on analytical items). So **Lite trades directness for calibration.** Pick Lite if you
value a better-calibrated everyday assistant; if you'd rather have raw directness, the model
without any spec is a defensible everyday choice too.

## Design notes

Two ideas drive most of the spec, if you want to adapt it:

1. **Compulsion functions beat aspirations.** "Focus on truth" is a wish a
   model can satisfy vacuously. "Assign a confidence label on this scale,
   anchored to its basis" is a procedure that forces a checkable artifact.
   The spec favors the latter throughout, because a forced visible step
   competes against trained defaults better than a stated intention does.

2. **Optimizing against one failure mode creates others.** Any directive that
   pushes behavior one way creates pressure toward an opposite failure mode,
   and this operates on each of the spec's pushes: the anti-sycophancy push
   induces contrarianism, the calibration push induces calibration theater, and
   stacking directives induces conflict between them. Several clauses (the
   counterweight, the priority order, the "how could this be wrong" check) exist
   as counterweights, not as more directives in the same direction. If you
   extend the spec, add counterweights — not just more rules in one direction.

A structural parallel worth knowing: frontier labs solve the directive-
conflict problem the same way this spec does. OpenAI's Model Spec assigns
each instruction a "level of authority" so higher overrides lower; this
spec's priority order is the same mechanism at a personal scale. The Model
Spec is public domain (CC0) and worth reading alongside this. See
[`REFERENCES.md`](REFERENCES.md).

The full reasoning — the mechanism, the ceiling, the fat-tail branch, and a
checklist for extending the spec without breaking it — is in
[`DESIGN.md`](DESIGN.md).

## License

MIT — see [`LICENSE`](LICENSE). Copy, adapt, and redistribute freely, including
commercially; the only condition is that the copyright notice travels with it.
