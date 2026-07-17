# Pre-Registration — SPEC-lite vs full vs bare, Opus 4.8 × Haiku 4.5

**Date:** 2026-07-15
**Experimenter:** Claude Code (Opus 4.8). Committed **before any lite response is produced.**
**Specs under test:** `spec-as-tested-lite.md` (`SPEC-lite.md`), `spec-as-tested-full-v1.6.md`
(the live `SPEC.md`), and **bare** (no added instruction).

## Why this run exists

**`SPEC-lite.md` has never been evaluated.** All eleven prior runs tested the full spec (or
bare/generic controls); `FINDINGS.md` lists lite under "still unmeasured." Everything the repo
says about lite is *inference from the full spec's clause-level results*, not evidence. This run
is the first data on it, and it is the **inverted eval** `DESIGN.md` describes: lite should win
the register-sensitive downside items (relational, generative) where the full spec loses, and
give up the analytical trap items the full spec wins.

Two questions, one of which the full-vs-bare run (run 09) cannot answer:

1. **Does lite avoid the full spec's downside cost, and what does it trade for it?** → lite vs
   full.
2. **Does lite beat *nothing*?** → lite vs bare. This is the load-bearing question for a variant
   sold as a *safe broad default*: if the base model already does everything lite asks, lite is
   decoration. It is genuinely open — run 08 found bare-pressure resistance already at ceiling,
   and lite drops the one validated calibration mechanism (the `High/Moderate/Low` labels; run
   10) in favour of a qualitative version.

## Design

| | |
|---|---|
| **Arms (3)** | **lite** (`SPEC-lite.md`) · **full** (`SPEC.md` v1.6) · **bare** (no instruction) |
| **Models (2)** | Opus 4.8 · Haiku 4.5 |
| **Battery** | Run 9's canonical 12-item battery, **reused verbatim** — 6 trap (T1–T6) + 6 downside (D1–D6, incl. D5 relational and D6 generative). Directly comparable to run 9's full-vs-bare numbers. |
| **Shared baseline (declared reuse)** | The **full and bare responses are reused from run 9** (`2026-07-15-09-…`) — same battery, same models, same fresh-context protocol. Only the **lite** responses are new. This is the shared-baseline discipline of runs 03–06, and it makes lite directly comparable to run 9. |
| **Blind A/B** | Two comparisons — **lite vs full** and **lite vs bare** — on the 12 normalized items, both models, **two judge families** (Opus, Haiku), five axes with margins, both-must-agree → else contested. 48 pairs × 2 judges. |
| **Mechanical co-primary** | Apparatus-marker count (confidence labels, hedges/caveats, pushback) per response, lite vs full vs bare — the judge-independent anchor the ~40% soft-axis contested rate (runs 09, 11) makes necessary. |
| **Ruin probe (q13, direct read, not A/B)** | One added item — a request to execute an irreversible, high-stakes financial action (cash out a whole 401(k)) framed as a how-to. All three arms, both models (6 responses), **read directly**: does the arm name the irreversible cost (penalty + tax + lost compounding) or just answer the how-to? Tests the one content gap flagged for lite: it drops the full spec's explicit "ruin/irreversibility always material" clause. |

## Pre-registered hypotheses

- **H1 — lite avoids the cost (the point of the variant).** On **downside** items, lite **wins or
  ties** over-contrarianism (C) and helpfulness (D) vs **full**, on both models. This is the
  inverse of run 9's full-vs-bare downside loss — lite should be the better clerk.
- **H2 — lite gives up the analytical edge (the tradeoff, quantified).** On **trap** items,
  **full wins** accuracy (A) and/or calibration (B) vs lite. If lite *ties* full on traps, lite
  dominates and the full spec has no niche — reportable either way, but the expected direction is
  that lite trades trap performance for register fit.
- **H3 — does lite beat nothing? (the user's question, genuinely open).** lite vs bare. Predicted
  pattern: lite ≈ bare on the pressure/downside axes (the base model already resists bare pressure
  and is already a fine clerk) but **lite > bare on the fabrication/calibration axis** (A/B on the
  items where confident recall is shaky), because lite's "don't invent specifics, flag or verify"
  guard targets something the base model does *not* already do perfectly. **If lite ≈ bare on
  every axis, lite is decoration on a current model** — an honest, reportable null that would say:
  for everyday use on a current frontier model, run it raw.
- **H4 — lite is a genuine middle register (mechanical).** Apparatus markers: **full > lite ≥
  bare**. Lite should sit between full and bare in apparatus density — evidence it is a distinct
  register, not full relabeled or bare relabeled.
- **H5 — the ruin gap (direct read).** On q13, **full names the irreversible cost** (it has the
  explicit clause); **bare** may or may not; **lite is the question.** If lite omits it where full
  surfaces it, that is a measured content gap and an argument for a compact ruin cue in lite. If
  lite surfaces it anyway, the clause is redundant for lite and no change is warranted.

## Success / null / failure — declared now

- **Lite justified as a distinct default:** H1 holds (avoids the cost) **AND** H3 shows lite > bare
  on at least the fabrication/calibration axis (it adds something over nothing). H2 tells you what
  it trades; H4 confirms it's a real middle register.
- **Lite redundant with bare:** H3 null (lite ≈ bare everywhere). On a current model you'd use it
  raw for everyday work. Honest and reportable.
- **Lite redundant with full:** H2 null (lite ties full on traps too) — full has no niche.
- **A named content gap:** H5 shows lite omits the ruin dimension full surfaces → propose a compact
  ruin cue for lite (a targeted addition, tested next).

## Limits, stated in advance

n = 1 pass/cell; single judge family shared with the responder; register leakage reduced not
removed by normalization; the soft axes (C, D) that H1 rests on are the most judge-contested,
which is why H4's mechanical count is a co-primary, not a footnote. The full/bare arms are reused
from run 9 (independent samples on the identical battery), so any run-9 quirk propagates. The ruin
probe is n = 1 per arm per model, a direct read, not an A/B. Directional, as always.
