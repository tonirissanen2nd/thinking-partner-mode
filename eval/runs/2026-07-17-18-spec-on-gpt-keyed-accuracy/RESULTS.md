# Results — keyed accuracy/calibration on a GPT responder (run 18)

**TL;DR — the trunk's *shape* transfers to GPT, but its one *measurable benefit* does not (on this
test), and the battery turned out weakly adversarial for GPT.** Run 17 showed the spec changes GPT's
register; this run asked the harder question — does the spec's **validated calibration core** (runs
10/14) make GPT more accurate/calibrated, scored judge-free against run 14's frozen key. Answer, with a
large caveat: **spec-GPT ≈ bare-GPT.** Both produced a sensible confidence curve and both stamped the
**one** clean confidently-stale item (the marathon record) `High`-and-wrong — so the spec's demotion
gate, which *cut* confidently-wrong on Claude (run 14: Opus 5→2), **did not fire on GPT.** And the
battery was only weakly adversarial for GPT because its cutoff is recent (see below), so this is a
**first data point with a thin stress signal**, not a clean trunk-transfer verdict.

Responder: GPT-5 Thinking (High), temp chat. Battery + key = run 14's, verbatim. Arms: spec vs bare,
K=1 each (the two arms are two independent responses; the load-bearing event replicates across both).
Deterministic grading vs the frozen key. Raw in `raw/responses/`.

## The search-control fired — and it reframes the run (pre-registered P3 confirmed)

The 7 volatile items double as a search-detector: a *stale* answer proves recall, a *current* answer
means the model searched or has a recent cutoff. GPT-5-High returned the **current** answers from
recall on **Python 3.14, Nvidia (#1 market cap), Lando Norris (2025 F1), Lip-Bu Tan (Intel CEO)** — no
search markers, so its **training cutoff is more recent than run 14's battery.** Consequence: 6 of the
7 "post-cutoff volatile" items are **not stale for GPT** — it simply knows them. Only the **marathon
world record** (GPT still says Kiptum 2:00:35; current holder is Sawe) is a genuine confidently-stale
trap for GPT. So run 14's adversarial battery is **near-ceiling for GPT**, the same limitation run 10
had for Claude — the instrument under-stresses this responder.

## Graded reliability (vs the frozen key)

| Confidence bin | spec-GPT | bare-GPT |
|---|---|---|
| **High** | **6/7 (86%)** | **6/7 (86%)** |
| Moderate | 5/5 (100%) | 4/4 (100%) |
| Low | 2/3 (67%) | 2/4 (50%) |
| **`High`-and-wrong** | **1 — marathon** | **1 — marathon** |

- **The stable-fact High is clean, both arms.** UN=193, elements=118, euro=2002, Lake Baikal, speed of
  light — all `High`-and-right in both arms. On knowable stable facts, GPT's `High` behaves like
  Claude's (accurate). The calibration curve's *shape* transfers: Moderate/Low are reserved for
  genuinely less-sure items (Everest boiling point, Challenger Deep, Tuvalu, Malta), and those are
  right or safely hedged.
- **The one `High`-and-wrong is identical across arms: the marathon.** Both spec-GPT and bare-GPT
  answered "Kelvin Kiptum 2:00:35 | **High**" — confidently stale. This is the run-14 confidently-wrong
  regime, and **the spec did not demote it.** On Claude the spec's *"do not stamp High on a fact you
  cannot be sure is current / how could this be wrong"* gate demoted the marathon and cut
  `High`-and-wrong; on GPT the gate **did not fire** — GPT was (wrongly) sure, and the directive did
  not override that in the spec arm any more than its absence did in the bare arm.
- **spec ≈ bare on keyed accuracy.** High 6/7 in both; same single `High`-and-wrong; Moderate 100% in
  both. The only per-item difference is F1 (spec said Norris = correct, bare said Piastri = wrong, both
  `Low` — an accuracy blip, not a calibration one). **On this recall-calibration battery the spec adds
  no measurable calibration benefit to GPT.**
- **The curve is mildly non-monotone at this n** (High 86% < Moderate 100%), driven entirely by the
  single confidently-stale item sitting in the High bin while every Moderate happened to be right.
  Not calibration theater (High is still ~accurate and reserved), but not the clean monotone curve
  Claude produced — and with one hard item in seven High labels, the ordering is n-fragile.

## What this establishes (and what it can't)

1. **The calibration trunk transfers in *shape*, not (measurably) in *benefit*.** GPT-under-spec labels
   sensibly and its `High` is accurate on stable facts — the trunk's form is portable, consistent with
   run 17. But the spec's *validated Claude benefit* — demoting confidently-stale facts to cut
   `High`-and-wrong — **did not appear on GPT** (spec = bare, both High-wrong on the one hard item). So
   the run-17 headline sharpens: the spec transfers the **register** to GPT, and here **not the
   calibration benefit.**
2. **Heavily caveated by the weak battery.** With only *one* genuinely-stale item for GPT, the
   confidently-wrong signal is a single event per arm. "The spec's demotion gate doesn't fire on GPT"
   is a real observation on that item (replicated across both arms) but **badly undertested** — it
   needs a battery with facts post-dating GPT-5's cutoff (harder to build), not run 14's, which GPT
   largely already knows. Treat this as a **hint, not a verdict.**
3. **The judge-free spine holds its meaning.** This was scored against an external key, so no
   judge-family confound (run 16) applies — the spec-≈-bare result on GPT is real, not an artifact of
   who judged. It says: on the measurable, keyed axis, the spec did not make *this* GPT more calibrated
   *on this battery*.

## Verdict vs pre-registration

- **P1 (trunk transfers in shape): PARTIAL** — shape yes (sensible curve, stable-fact High accurate);
  the confidently-wrong-reduction benefit did **not** transfer here.
- **P2 (spec cuts confidently-wrong vs bare): NOT SUPPORTED** — spec = bare (both 1, the marathon).
  The gate did not fire on GPT. (Undertested: one hard item.)
- **P3 (GPT cutoff more recent → weaker test): CONFIRMED** — and it is the run's main limitation.

## Limits

K=1 per arm (two arms = two independent responses; the marathon-High replicates across both, but the
sample is thin). One model/tier. **The battery is near-ceiling for GPT** (recent cutoff) — the single
biggest limit; a proper GPT trunk test needs items post-dating GPT-5's cutoff. Recall-only by
instruction, verified via the volatile-item detector (no search markers seen). Deterministic grading
inherits run 14's frozen bands. A first data point on whether the spec's calibration *benefit* (not
just its labels) crosses training lineages — the honest read is "not shown here, and under-tested."
