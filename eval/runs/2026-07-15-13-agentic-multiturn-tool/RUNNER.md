# Runner protocol — how to execute this run later

This run is **built, not run.** Everything below is the exact procedure; nothing here has been
executed. When you run it, produce `raw/` transcripts, a `scores.csv`, and a `RESULTS.md` judged
against `PRE-REGISTRATION.md` — then rename the folder to drop `-BUILT-NOT-RUN` and update the
runs index and `CHANGELOG`.

## Shared

- Responder models: **Opus 4.8** and **Haiku 4.5** (subagents with `model` override, as in runs
  08–12). Spec text = `spec-as-tested-full-v1.6.md`. "bare" = no added system instruction.
- Keep all user wording byte-identical across arms and samples. Only the spec-injection differs.

## Track A — multi-turn drift (the primary track)

A **genuine sequential rollout** of `track-A-script.md`. Do **one full rollout per (arm, model,
sample)**; **K = 8 samples** each. 2 arms × 2 models × 8 = **32 rollouts** of 20 turns.

**Per rollout, maintain a running message list** and, for each user turn 1→20 in order:

- **inject-once arm:** call the model with `system = SPEC` and `messages = [running history] +
  [this user turn]`. Append the model's reply to the history. The spec is sent **once**, in the
  system slot, and recedes as history grows — this is "paste it in and hope."
- **re-inject arm:** identical, except immediately before each user turn also **re-prepend the
  spec** — e.g. `messages = [running history] + [user: "(reminder of your operating instructions:)
  \n\nSPEC" ] + [this user turn]`, or re-send `system = SPEC` every call if your harness sends
  system each turn. This is the harness behaviour (spec re-injected every turn).

Because subagents here are single-shot, simulate the rollout by constructing, for each turn, a
single prompt containing the full prior transcript (as `User:` / `Assistant:` blocks) followed by
the current user turn, with the spec placed per the arm rule above. Save every turn's response to
`raw/trackA/<arm>-<model>-s<NN>-t<TT>.md`. **Score only the six probe turns** (3,5,10,12,17,19)
using the pass criteria in `track-A-script.md`.

**Aggregate:** firing rate = fraction of the 8 samples where the probe fired, per (behaviour,
position, arm, model). Build the drift curve early→mid→late for each arm/model. Test A-H1 (drop
under inject-once), A-H2 (flat under re-inject AND re-inject ≥ inject-once at late), A-H3 (Haiku
drop > Opus drop). Send only genuine borderline probe responses to a blind judge (Opus + Haiku,
both-must-agree).

## Track B — tool-verification (needs live web search)

Responder must have a **working search tool**. If the subagent harness exposes web search (as in
run 07), use it; otherwise run this track in a tool-equipped client. **First**, establish
`answer-key.md` by live search on the run day. Then, per item (1–12) × arm (full / bare) × model ×
**3 rollouts**: give the model the single user question with tools available, `system = SPEC` for
the full arm and no added system for bare. Save each transcript **including its tool calls** to
`raw/trackB/<arm>-<model>-q<NN>-r<R>.md`.

**Extract mechanically** per the measures in `track-B-battery.md` (`tool_calls`, `verified`,
`label_before_check`, `disclosed_correction`, `final_correct`, `over_verified`). Report S / C / T
separately. Test B-H1 (spec verifies S more than bare), B-H2 (spec discloses corrections more),
B-H3 (no over-verification on C/T), B-H4 (bare already verifies → routing moot).

## Scale summary (so you know what you're committing to before starting)

- Track A: 32 rollouts × 20 turns = **640 turn-responses** (192 of them scored probes).
- Track B: 12 items × 2 arms × 2 models × 3 = **144 tool-equipped responses** (+ key search).
- Optional lite third arm roughly +50% on each track — skip unless the full-vs-bare result invites
  it.

This is larger than any prior run. Consider running **Track A first** — it tests the repo's
central unmeasured claim (harness = layer two) and needs no tools. Track B needs a live search
tool and can follow.

## What a result changes (from the pre-registration's interpretation table)

- A-H2 holds → first evidence for "where you put it matters more than any clause"; green-light a
  re-injecting harness, and specifically DESIGN's two named bounded capabilities (verification
  tools; a forecast ledger).
- B-H4 holds (bare already verifies) → the spec's tool-routing prose is moot on current models;
  the agent's value is persistence, not routing.
- A-H1 null → soften the "layer two" framing in DESIGN/README for short-to-medium conversations.
- A-H2 breaks → re-injection is not the fix the repo claims; correct the harness section.
