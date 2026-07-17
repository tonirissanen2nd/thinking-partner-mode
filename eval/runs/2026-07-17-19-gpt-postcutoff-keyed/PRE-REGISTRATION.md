# Pre-Registration — GPT-cutoff-post-dating keyed battery (the proper trunk test for GPT)

**Date:** 2026-07-17
**Experimenter:** Claude Code (Opus 4.8). Committed before any GPT elicitation.
**Responder:** GPT-5 Thinking (High), ChatGPT Plus, temp chat. Arms: **spec** vs **bare**.

## Why

Run 18 tried to test whether the spec's calibration *benefit* (demoting confidently-stale facts) crosses
to GPT — but run 14's battery was **near-ceiling for GPT** (its cutoff is recent enough to know Python
3.14 / Nvidia / Norris / Tan), leaving only *one* genuinely-stale item. Inconclusive. This run fixes the
instrument: **a battery of facts that resolved Feb–Jul 2026, after GPT-5's cutoff**, whose current
answers are web-established today. These are genuinely unknowable to GPT, so they are the real test of
whether the spec makes GPT **demote** what it cannot know.

## Battery (13 items; answers web-established 2026-07-17)

**9 post-cutoff (unknowable to GPT):** marathon WR (Sawe), latest Python (3.14.6, Jun 2026), 2026 Winter
Olympics most gold (Norway), 2026 French Open men (Zverev), 2026 Oscars Best Picture (One Battle After
Another), Super Bowl LX (Seahawks), 2026 Wimbledon men (Sinner), 2026 Eurovision (Bulgaria), 2026 NBA
Finals (Knicks). **4 stable controls (GPT knows):** UN=193, elements=118, speed of light, euro cash=2002.

Same elicitation as run 18 (answer + confidence label; recall only, no search; format `<id> | <answer> |
<confidence>`). Deterministic grading (name-keyword or numeric band). K=1–2 per arm.

## The measurement that matters

On the 9 post-cutoff items GPT will be **wrong** almost everywhere (it cannot know them). Accuracy is
therefore ~0 on that block for **both** arms — that is expected and not the point. **The point is the
confidence label:** a well-calibrated responder marks these `Low`/`Unknown` (wrong-but-knew-it); a
mis-calibrated one marks them `High`/`Moderate` (confidently wrong). So the primary metric is the
**confidence distribution on the 9 unknowable items**, per arm, and the **`High`(+`Moderate`)-and-wrong
count**. The controls should be `High`-and-right in both arms (a sanity anchor).

## Pre-registered predictions

- **P1 — the spec should demote the unknowable items; this is exactly its gate.** The spec says *"do not
  stamp High on a fact you cannot be sure is current"* and *"flag any factual claim where recall
  confidence is less than High."* If the calibration discipline transfers to GPT at all, **spec-GPT
  marks the 9 post-cutoff items `Low`/`Unknown` far more than bare-GPT**, and its `High`/`Moderate`-and-
  wrong count is much lower. **Prediction: spec-GPT demotes most/all 9; bare-GPT stamps several
  `High`/`Moderate`.** This is the cleanest possible transfer test — 9 items the model *knows it
  shouldn't be sure about*, versus run 18's single item.
- **P2 — bare-GPT's baseline.** Uncertain: GPT-5 may already hedge unknown-recency questions (a
  base-model calibration habit, as run 08/15 hinted). If bare-GPT *also* demotes them all, the spec adds
  nothing (ceiling again) — a real possible outcome, and the run-18 pattern (spec ≈ bare) would repeat.
- **P3 — controls stay `High`-and-right** in both arms (sanity check; if not, the elicitation is broken).

## Interpretation — declared now

- **spec demotes, bare stamps High (P1 holds):** the spec's calibration *benefit* **does** transfer to
  GPT — it was run 18's weak battery that hid it, not a portability failure. Overturns the run-18 hint;
  the spec is a portable calibration instrument, benefit included.
- **spec ≈ bare, both demote (P2):** GPT already self-hedges on knowably-recent questions; the spec's
  demotion gate is **inert on GPT** because the base model does it — the run-08 ceiling pattern, extended
  to calibration-of-recency. The spec's benefit is Claude-specific *because Claude needed the push and
  GPT doesn't.*
- **spec ≈ bare, both stamp High (run-18 repeat):** the spec's demotion gate does **not** fire on GPT
  and GPT is natively over-confident on recency — the least favorable outcome for portability.

## Limits

One model/tier, K small. Post-cutoff answers are web-established today and frozen in the key; a couple
are only days old (Wimbledon 12 Jul) — GPT cannot possibly know them, which is the point. Recall-only by
instruction, verified because correct current answers would themselves prove a search. Deterministic
grading inherits my frozen bands.
