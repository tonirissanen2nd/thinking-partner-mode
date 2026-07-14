# Eval runs

One folder per run, named `YYYY-MM-DD-NN-slug` where `NN` is the run's sequence
number — so a directory listing sorts in **run order**. Each run is self-contained:
its own pre-registration, results writeup, and raw artifacts, so a run can be read,
audited, or reproduced without reference to any other. Keep both conventions when
adding a run (next index, self-contained).

**Run folders are immutable historical records.** A run's `RESULTS.md` reports what
*that* run found against the spec version *it* tested; it is **not** updated later to
reflect newer versions — that would corrupt the record, and duplicated across N
folders it would inevitably go stale. The only place that tracks the *current*
picture is **this index** plus the top of `../../CHANGELOG.md`. Only those two are
updated per push; the run folders never are.

Each run folder contains:

- `PRE-REGISTRATION.md` — committed **before** any result (removes researcher
  degrees of freedom).
- `RESULTS.md` — the writeup, judged against the pre-registration.
- `spec-as-tested-vN.md` — the exact spec this run evaluated, archived verbatim, so
  the tested version is preserved even as the live `SPEC.md` evolves. `v1` is the
  first tested spec (SHA `f68f436`); later modified specs are `v1.1`, `v1.2`, …
  stamped into the filename. (The lean-Epistemics run archives `spec-full-v1.md` and
  `spec-lean.md` instead — it tests a fork, not a version bump.)
- the run's data (scores CSV, battery, answer key, workflow scripts where used, …).
- optionally `raw/` — the process intermediates (per-question responses, normalized
  answers, blind judge inputs, individual judgments), committed for auditability.

The protocol these runs implement lives one level up: `../README.md` (Track 1),
`../prompts/` (the role prompts), `../scoring/` (the scoresheet tools).

## Runs to date (newest first)

| # | Run | What it found |
|---|---|---|
| 7 | `2026-07-15-07-v1.5-vs-v1.4-tool-equipped/` | First **tool-equipped** run (live web search). `v1.4` vs `v1.5` on a purpose-built stale-fact battery — the one thing Track 2's battery structurally could not do: produce `High`-and-wrong events. Result: the confidence-gate *bug fix* is weakly supported (v1.4 verified 7/8 anyway), but the **disclosure effect is strong** — on the same items, with the same correct final answers, v1.4 concealed that its unaided recall had been confidently wrong and v1.5 reported it. No over-verification, no defensive hedging. **Keep v1.5** — the mechanism makes miscalibration *observable*, exactly as `DESIGN` claims, without improving calibration. **Scope:** isolates the Verification change only. The live spec is `v1.6`, whose Dialectics change (persuasion vectors) is orthogonal to this battery and **remains untested**. |
| 6 | `2026-07-07-06-leanEpistemics-vs-full-ablation/` | `full` (v1) vs `lean` (Epistemics machinery cut), on a purpose-built fat-tail / ruin / hidden-failure / control battery. Full beats lean on the stress items (accuracy 5–2, calibration 4–2; fat-tail group 2–0/2–0), even on controls → the dense Epistemics earns its keep on the tail. Reconciles the Track-2 ordinary-facts null. **Keep the dense Epistemics.** |
| 5 | `2026-07-07-05-v1.3-vs-v1-ablation/` | `v1` vs `v1.3` (narrowed triviality gate). Narrowing did NOT recover q7 — v1 wins its accuracy the 3rd straight run regardless of wording → the gate is a prompt-layer ceiling. **Drop the gate.** Also a vivid n=1-noise demo (same sequencing wording, helpfulness swung 4–0→2–1 on resampling). |
| 4 | `2026-07-07-04-v1.2-vs-v1-ablation/` | `v1` vs `v1.2` (shared v1 baseline). The sequencing counter-counterweight recovered the q3 accuracy while keeping the gains → **sequencing is a keeper**; the triviality gate still a wash. |
| 3 | `2026-07-07-03-v1.1-vs-v1-ablation/` | `v1` vs `v1.1`. Isolates the two v1.1 counterweights: less contrarian / more helpful, but a small accuracy cost (Principle 2 live) → motivates v1.2. |
| 2 | `2026-07-07-02-hetero-claude/` | Track 1 re-run with a *different Claude model* judging (Haiku) than responding (Opus). Calibration win replicates; a mild trap-contrarianism cost same-model judging missed shows up. |
| 1 | `2026-07-07-01-single-family/` | The first pass. Both tracks (blind A/B + calibration), all roles Opus 4.8. Directional, single-family — the weakest role separation. |

**Net across the loop:** the sequencing counterweight was validated (kept), the
triviality gate hit a prompt-layer ceiling (dropped), and the dense Epistemics was
shown to earn its keep on tail risk (kept) — distilled into `v1.4` (see `CHANGELOG`).

None of these is the mandated **three-family** run (generator, responder, judge from
three different model families). All are directional. See each run's `RESULTS.md`
for what it can and cannot establish.
