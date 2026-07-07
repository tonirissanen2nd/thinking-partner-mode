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

Neither is the mandated **three-family** run (generator, responder, judge from
three different model families). Both are directional. See each run's
`RESULTS.md` for what it can and cannot establish.
