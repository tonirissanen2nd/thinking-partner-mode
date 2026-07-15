# Pre-Registration — v1.7 (frame-detection) vs v1.6 ablation, Opus 4.8 × Haiku 4.5

**Date:** 2026-07-15
**Experimenter:** Claude Code (Opus 4.8). Committed **before any response is produced.**
**Isolated change:** v1.7 = v1.6 **+ one new section, `Register`.** Nothing else differs
(`diff` is a single insertion; both specs archived here). This is a clean one-section ablation.

## Why this run exists

Run 9 measured the whole spec against nothing and found a **directional tradeoff**: v1.6 wins
accuracy/calibration on trap questions decisively but **loses over-contrarianism (C 5–1) and
helpfulness (D 7–1) on the downside block** — it brings the analytical apparatus (confidence
labels, steelmanning, caveats, pushback) to simple, relational, and generative questions that
wanted a short, warm, or committed answer. Run 9's verdict named the fix precisely: **make the
model detect a direct/relational/generative turn and *not* deploy the apparatus on it** — a
Principle-2 counterweight to the analytical push. `Register` is that section. This run tests
whether it works, or whether it is another prompt-layer ceiling.

## The change under test

`Register` instructs: before deploying the apparatus, classify the turn's stake. Apparatus is
**off by default** on (a) simple factual questions, (b) relational/emotionally-loaded turns,
(c) generative/creative requests, (d) sound-premise/uncontested questions. **Counterweight
(Principle 2):** a turn that *looks* simple but hides a trap (false premise, anchoring figure,
ruinous downside, XY problem) keeps the full apparatus; warmth never extends to endorsing a
false claim; when register is genuinely ambiguous, default to the apparatus — misreading a
trap as simple is the worse error.

## Design

| | |
|---|---|
| **Battery** | Run 9's canonical 12-item battery, verbatim: **6 trap (T1–T6)** + **6 downside (D1–D6)**. The traps test the counterweight (no regression); the downside items test the benefit. |
| **Arms (2)** | **v1.7** (v1.6 + Register) · **v1.6** (live spec) |
| **Models (2)** | **Opus 4.8** · **Haiku 4.5** (run 9 found the tradeoff on both) |
| **Cells** | 12 × 2 × 2 = **48 responses**, each from a fresh context blind to category |
| **Blind A/B** | Within each model, 12 normalized pairs, **two judge families (Opus, Haiku)**, five axes with margins, both-must-agree → else contested. 24 pairs × 2 = 48 judgments. |
| **Mechanical measure (judge-independent)** | On the **downside** responses, count apparatus markers directly — explicit confidence labels, hedge/caveat phrases, and pushback/"however"-style reversals. Run 9's 41% contested rate on the soft axes (C, D) makes a judge-only read fragile on exactly the axes this edit targets; the marker count is a direct behavioural check that does not depend on a judge. |

## Pre-registered hypotheses

- **H1 — the benefit (the point of the edit).** On **downside** items (D1–D6), v1.7 **wins or
  ties** axis **C** (over-contrarianism, less=better) and axis **D** (helpfulness) against v1.6,
  on both models. I.e. v1.7 pushes back less and adds less friction on questions that wanted a
  direct/warm/committed answer.
- **H2 — no trap regression (the counterweight test, primary).** On **trap** items (T1–T6),
  v1.7 **ties** v1.6 on axis **A** (accuracy) and axis **B** (calibration), on both models. If
  v1.7 *loses* traps, the `Register` gate misfired — it classified genuine traps as simple and
  suppressed the apparatus where it was needed. That is the exact failure mode of the dropped
  triviality gate (run 5): a well-meant suppressor that a wording cannot make safe. **If H2
  breaks, `Register` is a prompt-layer ceiling and is reverted, not shipped.**
- **H3 — the mechanism, measured directly.** On downside responses, v1.7 emits **fewer
  apparatus markers** (confidence labels + caveats + pushback phrases) than v1.6, on both
  models. This is the behavioural signature of the gate firing, independent of any judge.
- **H4 — the disguised-trap check.** The apparatus stays ON where it must: D1 (item 9, washing
  chicken — the user is *right*) is still confirmed, not hedged into false balance; and any
  trap that superficially resembles a simple question (T-items) is not stripped of the
  apparatus. Read from the trap responses and D1 directly.

## Success / null / failure — declared now, with the promotion rule

- **Promote to live SPEC v1.7:** H1 holds (downside C and D improve or tie) **AND** H2 holds
  (no trap accuracy/calibration regression). The edit buys back downside friction at no cost to
  trap performance — the counterweight worked.
- **Inert — do not ship:** H1 null (downside C/D ≈ tie both ways) while H2 holds. `Register`
  changed nothing measurable; shipping it is bloat. Revert.
- **Failure — revert:** H2 breaks (v1.7 loses trap A or B). The gate cannot be made safe at the
  prompt layer; it trades trap rigor for downside comfort. Revert, and record the ceiling —
  as run 5 did for the triviality gate.

The live `SPEC.md` stays at v1.6 until this run decides. v1.7 exists only as
`spec-as-tested-v1.7.md` here; it is promoted to `SPEC.md` **only** on the success condition.

## Limits, stated in advance

n = 1 pass/cell; single judge family shared with the responder; register leakage reduced not
removed by normalization; the soft axes (C, D) that H1 rests on are the ones run 9 found most
judge-contested — which is exactly why H3's mechanical marker count is pre-registered as a
co-primary read, not a footnote. Directional, as always.
