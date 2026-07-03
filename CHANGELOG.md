# Changelog

## Revision — mid-2026 (expert-review pass)

This pass acted on a critique of the v5 package. It fixed what is fixable at the
document level and explicitly did **not** fabricate the one thing that isn't
(eval results — the protocol still has to be *run*).

### Added

- **`SPEC.md` — Verification section.** Closes a real omission: the spec was
  written as if the model were a closed parametric system. When verification
  tooling exists in-session (search, retrieval, code execution, connected
  sources), it now says *verify a load-bearing fact rather than flag it* — with
  two counterweights (materiality threshold; treat tool output as evidence, not
  ground truth). `SPEC-lite.md` gets the light version of the same.
  ⚠ **This is a new behavioral directive and is therefore unvalidated** — a
  candidate for the eval, not a proven improvement.
- **`eval/prompts/04-calibration.md` + `eval/calibration-scoresheet.csv` —
  Track 2.** A calibration-and-abstention measure that scores confidence labels
  against an *external* answer key. This measures the spec's central claim (are
  the forced labels actually calibrated?), which the blind A/B protocol
  (now Track 1) structurally cannot — a pairwise judge only sees whether a label
  *looks* justified, which is what calibration theater defeats. Includes the
  calibration-theater signature test (High-bin accuracy ≈ Moderate-bin accuracy).
  ⚠ **Designed, not run.**

### Changed

- **`DESIGN.md` — ceiling point 1** now states the sharper truth: the
  basis-anchoring guard is not merely *unmeasured*, it has a *plausible
  mechanism to worsen* calibration theater (a forced justification makes a wrong
  label read as more grounded). The "considered and rejected" verification item
  is split — parametric strengthening stays rejected; the tool-routing slice is
  now incorporated as the Verification section.
- **`README.md`** — the calibration-theater risk note is strengthened to match,
  and the repo-contents table now reflects the two eval tracks.
- **`eval/README.md`** — reframed as Track 1, with a header routing to Track 2.
- **`REFERENCES.md`** — most ⚠ flags resolved by checking primary sources this
  pass. Two substantive corrections:
  - The **OpenAI Model Spec** "current version 2025-10-27" note was already
    stale (a 2025-12-18 version exists); dates corrected.
  - The **SpecEval** entry wrongly attributed the "a model update increased
    sycophancy against its own spec" example to SpecEval's own findings. It is
    the April 2025 GPT-4o incident, disclosed by OpenAI, which SpecEval merely
    *cites*. Fixed.
  - Verified IDs/titles added for FaR (2402.17124), Sharma sycophancy
    (2310.13548), ELEPHANT (2505.13995, title corrected), "Sycophancy Is Not One
    Thing" (2509.21305), SpecEval (2509.02464), and Model Spec Evals (Mar 2026).

### Not addressed (cannot be, at the document level)

- **The spec is still unrun.** The most valuable next step is not another
  directive — it is one pass of *both* eval tracks (ideally in English and one
  other language). One measured result moves the package from "plausible" to
  "tested" more than any further editing. This revision deliberately did not
  add more machinery beyond the one omission-closing directive above.
