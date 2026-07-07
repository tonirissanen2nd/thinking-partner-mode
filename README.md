# Thinking Partner Mode

A behavioral specification for LLM assistants that prioritizes calibrated
reasoning over agreeableness. It instructs the model to assign explicit
confidence levels, steelman counter-arguments, reject misframed questions,
distinguish empirical from normative claims, and flag what it left out —
instead of defaulting to fluent, confident, user-pleasing answers.

This is a **system prompt / custom instruction**, not a tool or a model. You
paste it into the custom-instructions field of an assistant (or prepend it to
a conversation) and it shapes how that model reasons and answers.

## What it is and isn't

It is an **inference-time behavioral spec**: a set of directives that compete
against a model's trained defaults using nothing but context. Its whole value
proposition is flexibility — you can edit it in seconds — not power.

It is **not** training, fine-tuning, or any weight-level intervention. That
sets its ceiling: a directive can force the model to *label* its confidence,
but cannot make a poorly-calibrated model well-calibrated. It changes
behavior within the model's existing repertoire; it does not expand that
repertoire. Expect it to surface uncertainty and catch framing errors more
reliably; do not expect it to make the model know things it doesn't.

## Status: honest

This spec is a **well-reasoned design, not a validated tool.** It was
developed iteratively through repeated critique-and-revision with LLM
assistants — not derived from the research literature (most of which surfaced
late; see `REFERENCES.md`).

It has now been run through the blind A/B protocol — but only *directionally*,
within a single model family, in English (see `eval/runs/`). That is weaker than
the mandated three-family design, and a single pass proves little: treat the runs
as suggestive, not validating. Its specific claims — that it reduces sycophancy,
that the counterweight clause prevents over-contrarianism, that it works as well
in one language as another (untested — the runs are English only) — are plausible
and grounded in the sycophancy literature, but not established here. If you want
confidence in the effect size, run the three-family protocol in `/eval`. Treat the
directives as informed design choices, not proven results.

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
what `eval` Track 2 does. It has now been run once (single-family): it found no
calibration theater, but on a thin base — the error spread came from essentially
one item — so treat that as directional, not settled. Treat the confidence labels
as a discipline that surfaces reasoning, not as proof the reasoning is
calibrated.

## Repository contents

| Path | What it is |
|---|---|
| `SPEC.md` | The full spec (English). The calibration-first version — paste into your assistant for analytical work. |
| `SPEC-lite.md` | The lightweight overlay — honest and calibrated without the sharpness. A safer broad default across mixed tasks. |
| `SPEC.<lang>.md` | Translated version(s), if present. Behavior may differ by language — test the one you use. |
| `DESIGN.md` | The reasoning behind the spec — mechanism, principles, limits, and how to extend it without breaking it. |
| `eval/` | Two-track evaluation: blind A/B (branch) + calibration (trunk), with prompts and scoresheets. |
| `eval/README.md` | Track 1 — the blind A/B test that removes the obvious biases; routes to Track 2. |
| `eval/prompts/04-calibration.md` | Track 2 — calibration & abstention scored against an external key (measures the claim Track 1 can't). |
| `eval/runs/` | Completed eval runs — one folder each (pre-registration + results + raw artifacts). Directional and single-family so far; not yet three-family. |
| `REFERENCES.md` | Prior art, empirical grounding, and where to verify claims — tiered by actual relationship to the spec. |
| `LICENSE` | MIT. |

## When to use it — and which variant

Two variants, chosen by task type:

**Full (`SPEC.md`)** — for quantitative analysis, contested-evidence questions,
and strategic decisions, where surfacing uncertainty and resisting your own
framing has real value. A known cost: it makes the model blunter and more
willing to push back. That is the point, not a bug — but it is the wrong
default for warm or creative work.

**Lite (`SPEC-lite.md`)** — a safer broad default for mixed, everyday use:
honest and calibrated without the sharpness. It keeps the anti-sycophancy and
calibration core but drops the immediate misframe rejection, the mandatory
steelman, and the forecasting/tail-risk machinery — the directives that make
the full spec a poor fit for generative or relational tasks.

If in doubt, start with Lite. Reach for Full when the work is analytical and
the overhead earns its cost. The full spec's priority order (accuracy →
calibration → sharpness → brevity) arbitrates its internal conflicts, but you
will still feel the overhead on easy questions — which is the reason Lite
exists.

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
`REFERENCES.md`.

## License

MIT — see [`LICENSE`](LICENSE). Copy, adapt, and redistribute freely, including
commercially; the only condition is that the copyright notice travels with it.
