# Run 13 — agentic eval (BUILT, NOT RUN)

The first design that tests whether the spec survives **as an agent** — two things every prior
run (all one or two turns) left unmeasured:

- **Track A — long-context drift** and whether **re-injection cures it**. Tests the repo's single
  most-repeated practical claim: *where you put the spec matters more than any clause in it*
  ("layer one, the spec; layer two, the harness"). Never measured until this runs.
- **Track B — tool-verification vs a raw tool-equipped model.** Does the spec's Verification
  section — inert without tools — actually fire and beat bare-with-tools? Run 07 showed the
  disclosure mechanism once; this pits it against bare.

**Nothing here has been executed.** Contents:

- `PRE-REGISTRATION.md` — hypotheses, fixed in advance.
- `track-A-script.md` — the 20-turn conversation with 6 probes and pass criteria.
- `track-B-battery.md` — the tool-verification battery (key established at run time).
- `RUNNER.md` — the exact procedure, arm construction, scale, and what each result changes.
- `spec-as-tested-*.md` — archived specs.

To run it: follow `RUNNER.md`, produce `raw/` + `scores.csv` + `RESULTS.md` judged against the
pre-registration, then drop `-BUILT-NOT-RUN` from the folder name and update the runs index and
`CHANGELOG`.
