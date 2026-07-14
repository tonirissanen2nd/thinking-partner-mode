# Changelog

## 2026-07-15 — SPEC v1.6 (name the persuasion vectors — **unrun**)

**Dialectics** replaces the vague *"social pressure alone is never a sufficient
reason"* with an enumerated list of what does **not** count as evidence: repetition,
insistence, expressed displeasure, flattery or rapport, appeal to your own earlier
agreement, or the bare assertion of authority or consensus without the argument or
data behind it. Rationale: "don't cave to pressure" is an *aspiration* — it names no
checkable surface. An enumeration is a compulsion in the spec's own sense.

**Two honest qualifications, because the case for this is weaker than it first looks:**

1. **The evidence cited for it does not target this failure mode.** The suggestion
   came with a persuasion study showing Cialdini-style vectors moving LLM compliance
   35.3% → 51.3%. But that study is about persuading a model to comply with
   *objectionable requests* — a safety/compliance target. Dialectics is about
   *sycophantic position-change in an analytical disagreement*. The vectors plausibly
   transfer; the effect size does not. This edit rests on the argument, not on that
   number.
2. **A Principle-2 trap was in the proposed wording and is corrected here.** Listing
   "claims of consensus" flatly as non-evidence would induce the opposite failure —
   contrarianism about genuine expert consensus, which *is* evidence (weak, but real).
   The clause therefore distinguishes the **bare, unsupported claim** of consensus
   (not evidence) from consensus itself (weak evidence), and says so explicitly so a
   future editor cannot re-collapse them.

**Unrun.** Candidate for the eval, not an improvement. The existing Track 1 battery
has one pressure item (T6) and no items that apply flattery, reciprocity, or false
consensus — testing this properly needs a battery built for it.

## 2026-07-15 — SPEC v1.5 (verification as calibration scoring — **unrun**)

Reworks the **Verification** section. Prompted by an external critique that found a
real defect, not just a missed improvement.

- **Fixed a defect.** The old wording exempted "what confident recall already covers"
  from verification. That is a **confidence gate on the check** — and it inverts the
  whole point: a wrong `High` suppresses the very check that would have caught it, so
  miscalibration becomes self-concealing. Verification is now gated by **materiality
  only, never by the label**. This half is a bug fix by the spec's own logic.
- **Added ordering.** Emit the confidence label *before* verifying, then verify, then
  state whether the check confirmed, corrected, or could not resolve it. The label
  becomes a prediction; the check scores it. This is the only point in the spec where
  a label is tested against something other than its own plausibility — `DESIGN`'s
  ceiling argument concedes nothing at the prompt layer can close that gap, and a
  tool-equipped session is the one place an external key is already present. It does
  not make the model better calibrated; it makes miscalibration **observable**.
- **Counterweight, same edit.** Consequential labels induce the opposite failure —
  hedging downward so the check cannot score you wrong. So: *do not lower a label to
  protect it from the check.*
- **Conflict handling.** Where the check and confident recall disagree and cannot be
  reconciled in-session, name the conflict rather than silently adopting the tool's
  answer (silent adoption destroys the calibration signal — you never see that the
  prior label was wrong).

**Scope and status.** This is **inert without tools** — in a plain chat it changes
nothing. And it is **unrun**: by the spec's own extender rule, that makes it a
candidate for the eval, not an improvement. It also cannot be tested by the existing
Track 1 battery, which has no tool-use condition; testing it needs a tool-equipped run
on a battery that can actually produce `High`-and-wrong events (stale/superseded facts
— the "Malta-like" items that drove every error in Track 2).

## 2026-07-07 — SPEC v1.4 (distilled: keep the sequencing change, drop the triviality gate)

The end state of the v1.1→v1.3 loop plus the lean-Epistemics ablation. Three
decisions, each eval-backed (`eval/runs/`):

- **Kept — the sequencing change** (Goal vs. solution: lead with the deliverable,
  full critique after). Validated across the v1.1 and v1.2 ablations — helpfulness /
  anti-contrarianism / anti-over-caution gains, and v1.2 recovered its one accuracy
  cost. This is the single change the whole loop validated.
- **Dropped — the triviality gate.** Three wordings (v1.1/v1.2/v1.3) all lost the q7
  trivial-fact accuracy; narrowing did not help → a prompt-layer ceiling, not a
  wording problem. The Epistemics addition is reverted entirely — Epistemics is now
  byte-identical to v1.
- **Kept unchanged — the dense Epistemics machinery.** The lean-Epistemics ablation
  showed it earns its keep on fat-tail / ruin / hidden-failure items (full beat a lean
  core 5–2 on accuracy, 4–2 on calibration), reconciling the Track-2 ordinary-facts
  null (redundant on ordinary facts, not on the tail). Do not lean it.

Net: **v1.4 = v1 + the sequencing counterweight, and nothing else.** Still directional
(single-family, n=1, Haiku judge) — a candidate for the mandated three-family run, not
a proven result.

## 2026-07-07 — SPEC v1.3 (narrow the triviality gate; wording-vs-ceiling test)

The v1.2 ablation left the triviality gate a wash: even with the "keep context"
clause, the model over-trimmed trivial-fact answers (q7, downside completeness lost
to v1). v1.3 narrows the gate as far as wording can go — it now governs *only* the
confidence phrase, and explicitly forbids shortening the answer or dropping context.
Everything else (the sequencing change) is unchanged from v1.2.

This is a deliberate **wording-vs-ceiling probe**, A/B'd against v1 in
`eval/runs/2026-07-07-05-v1.3-vs-v1-ablation/` (same v1 baseline as the v1.1 and v1.2
runs, so the three are directly comparable). If the narrowing recovers the downside
completeness v1.2 lost, the gate was a wording problem. If it does not move, the gate
is at the prompt-layer ceiling (the model won't reliably hold "drop the label, not
the substance" however it's phrased) — and should be dropped rather than re-worded.

## 2026-07-07 — SPEC v1.2 (counter-counterweights for v1.1's induced cost)

The v1.1 ablation (`eval/runs/2026-07-07-03-v1.1-vs-v1-ablation/`) found v1.1's two
counterweights worked — less contrarian, less over-cautious, more helpful — but
induced a small **accuracy** cost, a live instance of Principle 2 (optimizing one
failure mode induces its opposite). v1.2 adds the counterweight v1.1 should have
carried in the same edit:

- **Sequencing:** leading with the deliverable must not abbreviate the critique —
  surface the load-bearing failure mode with full weight, *after* the deliverable,
  not before. (Targets the q3 accuracy loss: v1.1 led with the script but caught
  the structural failure mode less fully.)
- **Triviality gate:** dropping the confidence *label* must not drop *substance* —
  if the question carries a genuine ambiguity a brief clarification resolves, still
  give it. (Targets the q7 accuracy loss: v1.1's bare "1989." dropped the useful
  "what does 'the fall' mean" context.)

Each is a bound on the v1.1 edit it sits next to, added in the same revision — the
discipline v1.1 skipped. **v1.2 is being A/B'd against v1** in
`eval/runs/2026-07-07-04-v1.2-vs-v1-ablation/` to check it closes the accuracy cost
without losing v1.1's gains.

## 2026-07-07 — SPEC v1.1 (two eval-driven counterweights, unrun)

Two narrow changes to `SPEC.md`, each a *counterweight* to a cost the eval runs
located (see `eval/runs/`) — not a new push in an existing direction. **v1.1 is
modified but not yet re-run**: treat these as candidate improvements, not validated
ones. When v1.1 is run, its run folder gets `spec-as-tested-v1.1.md`, diffable
against v1. `SPEC-lite.md` is unchanged — its lighter framing already sidesteps
both issues.

- **Sequencing on the XY case (Goal vs. solution).** Both runs charged the spec a
  cost for leading with a framing critique before delivering an *answerable*
  request (single-family axis E on the XY item; hetero axis C on the cron item,
  where a different-model judge scored the critique-first answer as more
  contrarian). v1.1: when the means is suboptimal but the request is answerable,
  lead with the usable answer and attach the better path, rather than gating the
  deliverable behind the critique. Rejection-first stays scoped to genuinely
  misframed questions. This bounds the contrarianism the reframe register induces.
- **Triviality gate on confidence labels (Epistemics).** The hetero run flagged a
  `High`/"well-documented fact" assertion on a settled question (the Berlin Wall
  year) as uninformative — calibration theater from the trivial-fact side. v1.1
  extends the existing theater guard: drop the label on settled, uncontested
  facts; reserve labels for uncertainty that is contestable or decision-relevant.

Deliberately **not** folded into v1.1: the Track 2 null (the dense Epistemics
machinery did not beat a generic "be honest" instruction on a well-calibrated
model) argues for *subtracting*, not adding — a leaner-Epistemics variant to A/B
against v1. That is a measurement to run, not a directive to write, so it is left
for a future run.

## 2026-07-07 — first eval runs (directional)

The eval is no longer only *designed* — it has been **run**, though only
directionally. Entries below that call the spec "unrun" record the state at their
date; they are superseded by this one, not by a rewrite.

- **`eval/runs/2026-07-07-01-single-family/`** — both tracks, all roles Claude Opus
  4.8 (a single family). Track 1: the spec wins calibration on analytical traps,
  the contrarianism counterweight holds, and the cost concentrates on
  warm/brief/creative asks (exactly the Full-vs-Lite split the README predicts).
  Track 2: no calibration theater, but no measurable gain over a generic "be
  honest" control on an already-well-calibrated base model.
- **`eval/runs/2026-07-07-02-hetero-claude/`** — Track 1 re-run with a *different
  Claude model* judging (Haiku) than responding (Opus). The calibration win
  replicates; a mild trap-contrarianism cost that same-model judging missed does
  show up.

Both are **single-family, single-pass, small-n** — suggestive, not validating.
The mandated **three-family** run (generator, responder, judge from three
different model families) is still not done and remains the next step. The spec
is now best described as **run directionally, not validated** — "run" and
"validated" are not the same claim.

## Revision — mid-2026 (empirical-integration pass)

Integrated the Wharton *Prompting Science* series (Reports 1–4, SSRN 5165270 /
5285532 / 5375404 / 5879722) after reviewing the primary PDFs. The reports
measure single-answer MCQ accuracy — **not** the spec's targets (calibration,
abstention, anti-sycophancy) — so they are ceiling evidence and a sharpened
prior, not a refutation. Five changes:

1. **`REFERENCES.md`** — added the series to §3 (empirical grounding, for the
   ceiling claim) and §4 (methodology, for the eval design), with scope limits
   stated so it is not over-read as testing the spec's actual claims.
2. **`DESIGN.md`** — recorded that the Chain-of-thought directive is mandated
   for *auditability*, not accuracy (Report 2 finds explicit CoT marginal-to-
   negative on models that already reason, and variance-adding); the directive
   serves the confidence machinery, not correctness.
3. **`DESIGN.md`** — buried the expert-persona *accuracy* assumption: Report 4
   shows expert personas don't reliably improve factual accuracy (and mismatched
   ones can degrade or cause refusals). The expert *tone* stays as a register
   choice, which Report 4 notes personas legitimately serve.
4. **`eval/prompts/04-calibration.md` + `eval/scoring/calibration-scoresheet.csv`** — Track 2
   now requires **25 trials per item** (Report 2 Table S2: 25 ≈ 100 for
   precision/power), scored at **three correctness thresholds** (25/25, 23/25,
   13/25), and adds **per-item reliability** (compare the emitted label to the
   item's empirical success rate — a `High` on a 60%-correct item is
   miscalibrated even above chance) alongside the trial-level calibration curve.
5. **`eval/prompts/03-judge.md` + `README.md` + both scoresheets** — added
   Track 1 **axis E: over-caution / under-utilization** (refusing or
   under-committing on answerable questions), distinct from axis C
   (manufacturing objections). Motivated by Report 4's refusal mode (an
   over-narrow role made one model decline ~10.6/25 answerable trials). Added to
   the judge, pre-registration success/failure, red flags, and the CSV + xlsx
   summary blocks (ALL / trap / downside).

⚠ Unchanged: none of the additions are themselves validated, and the eval
remains **unrun**. These sharpen the design and the measurement; they do not
substitute for running it. `SPEC.md` was not touched.

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
- **`eval/prompts/04-calibration.md` + `eval/scoring/calibration-scoresheet.csv` —
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
