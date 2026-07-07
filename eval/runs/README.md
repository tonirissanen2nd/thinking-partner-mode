# Eval runs

One folder per run. Each run is self-contained: its own pre-registration, its
results writeup, and its raw artifacts — so a run can be read, audited, or
reproduced without reference to any other. This is the convention; keep it when
adding runs.

Each run folder contains:

- `PRE-REGISTRATION.md` — committed **before** any result (removes researcher
  degrees of freedom).
- `RESULTS.md` — the writeup, judged against the pre-registration.
- `spec-as-tested-vN.md` — the exact `SPEC.md` this run evaluated, archived
  verbatim, so the tested spec version is preserved with the run even as the live
  `SPEC.md` evolves. **Version numbering:** `v1` is the first tested spec (SHA
  `f68f436`); the next modified spec that gets re-run is `v1.1`, then `v1.2`, and
  so on — stamped into the filename. Both runs to date tested `v1` (byte-identical).
- the run's data (scores CSVs, workflow scripts, battery, answer key, …).
- optionally `raw/` — the process intermediates (per-question responses,
  normalized answers, blind judge inputs, individual judgments). Committed for
  auditability: you can see exactly what each judge saw and said. Skip it if a
  run is script-driven and the script + CSVs already reproduce it.

The protocol these runs implement lives one level up: `../README.md` (Track 1),
`../prompts/` (the role prompts), `../scoring/` (the scoresheet tools).

## Runs to date

| Run | Roles | What it is |
|---|---|---|
| `2026-07-07-single-family/` | all roles Claude Opus 4.8 | The first pass. Both tracks (blind A/B + calibration). Directional, single-family — the weakest role separation. |
| `2026-07-07-hetero-claude/` | responder Opus · judges Haiku · generator Sonnet | Track 1 only, re-run with a *different Claude model* judging than responding. Reduces (does not remove) same-model preference bias; still one family. |
| `2026-07-07-v1.1-vs-v1-ablation/` | responder Opus · judges Haiku | Direct A/B of the spec against itself: `v1` vs `v1.1`. Isolates the two v1.1 counterweights. Result: v1.1 less contrarian / more helpful, but at a small accuracy cost — Principle 2 live; motivates a v1.2. |
| `2026-07-07-v1.2-vs-v1-ablation/` | responder Opus · judges Haiku | `v1` vs `v1.2` (shared v1 baseline, so directly comparable to the v1.1 run). Result: the sequencing counterweight recovered the q3 accuracy while keeping the gains — a keeper; the triviality gate is a wash. |
| `2026-07-07-v1.3-vs-v1-ablation/` | responder Opus · judges Haiku | `v1` vs `v1.3` (narrowed triviality gate; same v1 baseline). Result: narrowing did NOT recover q7 — v1 wins its accuracy for the 3rd straight run regardless of gate wording → the gate is at the prompt-layer ceiling; drop it. Also a vivid n=1-noise demo (identical sequencing wording, helpfulness swung 4-0→2-1 on resampling). |
| `2026-07-07-leanEpistemics-vs-full-ablation/` | responder Opus · judges Haiku | `full` (v1) vs `lean` (Epistemics machinery cut), on a purpose-built fat-tail / ruin / hidden-failure / control battery. Result: full beats lean on the stress items (accuracy 5-2, calibration 4-2; fat-tail group 2-0/2-0), even on controls → the dense Epistemics earns its keep on the tail. Reconciles the Track-2 ordinary-facts null: redundant on ordinary facts, not on the tail. Keep it. |

None of these is the mandated **three-family** run (generator, responder, judge
from three different model families). All are directional. See each run's
`RESULTS.md` for what it can and cannot establish.
