# Harness — a reference design for the second layer

## What this document is

`DESIGN.md` and `README.md` describe the spec as **layer one of a two-layer system: the spec
supplies the behaviour, the harness supplies the persistence** — and repeat that *where you put
the spec matters more than any clause in it*. They never specify that second layer. This
document sketches it.

**It is a design sketch, not shipped code.** Its status is the same as run 13's: committed so
the design is fixed and auditable *before* it is built, not because it exists. It follows the
spec's own discipline — every component fixes a **named** gap the eval program found, each
carries a Principle-2 counterweight, and **the spec files are never touched**: the harness reads
`SPEC.md` / `SPEC-lite.md` as swappable config, so layer one keeps its whole value —
portability, model-independence, editing in seconds.

## What the harness is, and isn't

- **It is** a thin, per-turn pipeline that (1) picks which register — and, optionally, which model
  *tier* — a turn wants, (2) re-injects the chosen spec on the chosen model, (3) optionally exposes
  verify tools, (4) optionally logs forecasts to a ledger, and (5) records telemetry.
- **It is not** a fusion of spec-and-agent. The spec stays a portable file you can drop into any
  harness; this is separate infrastructure that runs *around* a model. **Disable any component
  and it degrades gracefully** — the injector alone (persistence) is already useful; the router
  alone is already useful.
- **The design payoff it targets** is the eval program's single clearest finding: the full spec
  is *a better analyst and a worse clerk* (run 09), and the model **cannot reliably self-detect
  which register a turn wants at the prompt layer** (run 11 tried, and over-trimmed the traps).
  The harness moves that detection **outside the model**, where it can be deterministic and
  measured.

## The per-turn pipeline

```
  incoming user turn
    │
    ▼
  [1] Router ───────── classify the turn → (register, tier)
    │                  register: {full · lite · none}   tier: {cheap · strong}
    │                  (unsure → strong + full; misreading a trap as simple is the worse error)
    ▼
  [2] Injector ─────── re-prepend the chosen spec, on the chosen model, THIS turn
    │                  (persistence / anti-drift)
    │                  ── cheap model may escalate mid-turn: a Low/Unknown label on a
    │                     load-bearing point re-runs the turn on the strong model
    ▼-- (escalation)
    │
    ▼
  [3] Verify layer ─── if the turn is factual & load-bearing, expose a search/retrieval tool
    │                  (activates the spec's Verification section, inert without tools)
    ▼
  model generates the response  (may call tools → verify-before-answer → disclose corrections)
    │
    ├─[4] Ledger ───── if the response contains a scorable forecast, log it + resolution date
    │                  (a background job settles due forecasts against reality later)
    │
    └─[5] Telemetry ── log which spec fired, labels emitted, tools used, corrections disclosed
    │
    ▼
  response to user
```

## Components

Each: **what it does · the named gap it closes · its Principle-2 counterweight · which run
measures it.**

### 1. Router — the core, and the best-grounded

- **What.** A cheap classifier reads the incoming turn (and a little context) and outputs a pair:
  **(register, tier).** The *same* "is this a load-bearing analytical turn?" decision drives both
  — which spec, and which model. So the two collapse into one classifier:
  - **everyday / relational / generative / simple factual** → `SPEC-lite.md` (or none) on a
    **cheap, token-light model**;
  - **high-stakes analytical / contested / subtle-reasoning** → `SPEC.md` on a **strong model**;
  - **ambiguous** → strong + full (the asymmetric default, below).
- **Gap it closes.** Two, from one classifier. *Register:* run 09 measured the cost of applying
  the full apparatus to a turn that wanted a short/warm/committed answer (helpfulness 7–1 on the
  downside block), and run 11 showed the model can't suppress its own apparatus reliably from
  inside the prompt — so the harness suppresses it by *choosing the spec*. *Tier:* the eval gives
  a usable map of where the raw capability gap actually bites — the cheap model is fine (with the
  spec) on the everyday majority (run 10: Haiku's `High` labels are as reliable as Opus's; run 12:
  lite improves Haiku's calibration *more* than Opus's), but the strong model is needed on subtle
  reasoning (run 08 q08: Haiku caved to a false premise hidden among true ones; **Opus caught it**
  — a capability limit, not a prompt one). Cheap-by-default with escalation is the token-cheap
  deployment the question asks for.
- **Why this is the theoretically correct fix, not just an engineering convenience.** It converges
  (structurally, not as literal identity) with the dual-process account the spec's background
  reading rests on: the full spec is *System-2-in-a-box*, and applying it to a fast-answer turn is
  the same error as engaging deliberate reasoning where intuition suffices — which is what run 09's
  helpfulness 7–1 cost *is*. Run 11's finding that the model can't self-detect its register from
  inside the prompt is the analogue of WYSIATI: the model does not notice it is in a slow-thinking
  situation. A system that cannot see it should be in System 2 cannot be trusted to switch itself
  into it — so the switch belongs to a deterministic **outer** layer. That is the router.
- **Escalation — two triggers, because one has a blind spot.** The cheap model runs the spec, so
  **its own confidence labels become an escalation signal**: a `Low`/`Unknown` on a load-bearing
  point re-runs the turn on the strong model. Run 10 validated those labels, so this reliably
  catches the *known* unknowns. But it **cannot** catch the dangerous case — a cheap model that is
  *confidently wrong* on a subtle trap does not emit `Low`; it caves with a `High` (run 08 q08).
  So the router's **pre-classification** is the second, necessary trigger: a turn tagged
  high-stakes-analytical goes straight to the strong model, catching exactly the confidently-wrong
  case the label signal misses. Belt and suspenders.
- **Counterweight (Principle 2).** Adding the tier decision **raises the cost of a misrouting.**
  Register-only, sending a disguised trap to lite costs some trap accuracy — bad but bounded.
  With tiers, sending a disguised trap to the *cheap model* costs the capability itself: run 08
  showed the cheap model **misses the subtle trap entirely.** So the same two error directions
  apply, but the trap-as-simple error is now worse. Mitigation is the spec's own asymmetric
  default, hardened: **when unsure, strong + full** — misreading a trap as simple is the worse
  error (run 11's logic), and now more so. Add a **sticky bias** so one ambiguous turn doesn't
  flip register/tier mid-thread. And note the honest limit of the token-saving: it is real **only
  if the traffic is mostly everyday** — a workload dominated by hard analysis routes to the strong
  model anyway and saves little.
- **Measured by.** Two new evals, both this design's own failure surfaces, neither assumed:
  (i) **router accuracy** — label a battery of turns by intended (register, tier), measure the
  classifier's agreement, tune the unsure-threshold; (ii) **cheap+escalate vs strong-always** —
  does the cheap-default pipeline match a strong-model-always baseline on answer quality, at lower
  cost? (A relative of run 13 Track A: switching tiers mid-conversation is a cousin of the drift
  question.) Grounding for the *routing benefit* and the *tier map* is already in runs 08, 09, 10,
  11, 12; the *policy* is not — build it behind these two measurements.

### 2. Injector — persistence / anti-drift

- **What.** Re-prepends the chosen spec into context **every turn** (system slot re-sent, or spec
  re-injected before the latest user turn), and handles a clean switch when the router changes
  register.
- **Gap it closes.** Long-context drift — "a good result on turn one says little about turn
  forty." Re-injection is the layer-two mechanism the repo names but has never demonstrated.
- **Counterweight.** Re-injecting a large spec every turn costs tokens; a mid-conversation
  register switch can feel abrupt (apparatus appears, then vanishes). Mitigation: switch only on
  a clear register change; prefer `SPEC-lite`'s smaller footprint for the default register.
- **Measured by.** **Run 13, Track A** (inject-once vs re-inject). Build this component only after
  Track A shows re-injection actually cures drift; if it doesn't, the whole layer-two claim is
  wrong and the harness loses its persistence rationale.

### 3. Verify layer — activates the inert Verification section

- **What.** Exposes a search/retrieval tool when the turn makes a load-bearing factual claim, so
  the spec's Verification directive can fire: emit the label, verify, report whether the check
  confirmed, corrected, or couldn't resolve it.
- **Gap it closes.** Verification is **inert without tools** (DESIGN). Run 07 showed that with
  tools it converts an unobservable miscalibration into an observable, repaired one (the
  disclosure effect).
- **Counterweight.** Over-verification (the spec's materiality gate must hold — run 07 confirmed
  it doesn't verify decorative facts); and tool output can be stale/wrong/adversarial (the spec's
  own "evidence, not ground truth" clause). Plus the **named null risk**: a raw tool-equipped
  model may already verify, making the routing moot (run 13 B-H4).
- **Measured by.** **Run 13, Track B** (full spec vs bare-with-tools). Build only if it beats bare.

### 4. Forecast ledger — the thesis-completing component (listed last, not least)

*Ordered fourth for build-readiness, not importance. On importance it is the center of gravity:
it is the only component that turns "the spec **forces a label**" into "the harness **forces
calibration**" — and calibration-by-scored-feedback is the load-bearing empirical result of the
literature the spec converges with (Tetlock's superforecasters got their edge from perpetual beta
— scored feedback over many forecasts — not from any single instruction; Duke's poker argument is
identical). Every other component shapes a single response; this one closes the loop across
months. Read it as the thesis, not an accessory.*

- **What.** When a response contains a **scorable** forecast (numeric probability + time window +
  resolution criterion — exactly what the spec's Forecasting section demands), log it to a
  persistent ledger with its resolution date. A background job settles due forecasts against
  reality (via search, or a prompt to the user) and maintains a running calibration score.
- **Gap it closes.** DESIGN's **explicitly-named open gap**: the spec demands scorable forecasts
  but *nothing ever scores them* — "the loop can only close outside the model, in a persistent
  ledger that settles each forecast against the world rather than the model's own plausibility."
  This is that ledger. Memory here is not decoration; it is the missing infrastructure DESIGN
  names — and it is the **only** instrument that can reach the fat-tail / judgment domain the
  spec's machinery exists for, which a keyed single-session battery structurally cannot (see
  `FINDINGS.md`, "the fat-tail branch is a different epistemic category").
- **Counterweight.** Garbage resolution → garbage calibration: the ledger needs real ground truth,
  and only forecasts that actually resolve can be scored. Mitigation: log only forecasts with a
  clear resolution criterion (the spec already requires one); settle by search where possible,
  flag ambiguous ones for the user.
- **Why it is not built first, despite being the thesis.** It would sit on an **unmeasured
  foundation**: the spec's Forecasting directives themselves are unvalidated — run 10 measured
  calibration on *factual recall*, never on *judgment/prediction*. Building an elaborate scoring
  loop on top of directives that may not even produce well-formed, calibrated forecasts is the
  scope-creep the whole method warns against. **The prerequisite is one cheap, now-runnable
  measurement:** a Track-2-style run that scores *forecasts* (post-cutoff/withheld resolvable
  items, scored against the known outcome) rather than recall — the rung between run 10 and the
  ledger. Do that first; it de-risks the whole thesis-component for the cost of one run.
- **Measured by.** The ledger **is** the measurement instrument — it produces, over months, the
  forecasting-calibration curve that no single-session eval can. The forecast-quality run above
  is the finite proxy that earns it the build.

### 5. Telemetry — deployment as an ongoing eval

- **What.** Per turn, log which spec fired, confidence labels emitted, tools called, corrections
  disclosed, forecasts logged.
- **Gap it closes.** Everything in the repo is measured on synthetic batteries; nobody knows if
  TPM helps a **real** workload. Telemetry closes that — and tells you whether the *router* is
  choosing well in the wild.
- **Counterweight.** It measures *process* (did the label appear) not *outcome* (was it right);
  outcome still needs the ledger or explicit user feedback. And it is logging — mind privacy and
  cost.

## Build order — MVP first, each addition gated on a measurement

The spec's extender rule applies to the harness too: *one measured result is worth more than
another component.*

1. **MVP — Router + Injector.** The two best-grounded pieces: they address the measured findings
   (worse-clerk cost, drift) and need no tools or memory. This alone is a useful harness: the
   right register — and, if you want the token saving, the right *tier* — kept fresh every turn.
   Add the tier split only once the router-accuracy eval shows the classifier is good enough that
   a misroute-to-cheap on a hidden trap is rare; the asymmetric default (unsure → strong + full)
   covers the rest.
2. **+ Verify layer** — build **after run 13 Track B** shows the spec beats bare-with-tools (skip
   if B-H4 holds).
3. **+ Forecast ledger** — the thesis-completing component, not a late accessory. But gate it on
   its prerequisite: **first run the forecast-quality eval** (score *predictions*, not recall — the
   rung between run 10 and the ledger) to confirm the spec even produces well-formed, calibrated
   forecasts. Build the ledger once that de-risks its foundation; don't build a scoring loop on
   unvalidated Forecasting directives.
4. **+ Telemetry** — cheap, add whenever you deploy for real.

Do **not** build all five as a monolith. Each is independently valuable and independently
measurable; coupling them is how a clean two-layer system turns into an unauditable one.

## What is grounded vs. pending

- **Grounded now (runs 09, 11):** the *routing* benefit — the model can't self-detect register,
  and misapplied full-spec has a real cost. This is why the harness exists.
- **Grounded now (runs 08, 10, 12):** the *tier map* — where the raw capability gap bites (subtle
  reasoning → strong; everyday calibrated assistance → cheap suffices with the spec). This tells
  you *how* to route across model tiers, but not that the cheap-default *policy* works as a system.
- **Pending run 13:** persistence (Track A) and tool-verification (Track B). Build components 2
  and 3 only if those runs back them.
- **Pending two new evals this design creates:** *router accuracy* (does the classifier pick the
  right (register, tier)?) and *cheap+escalate vs strong-always* (does the token-cheap pipeline
  match a strong-always baseline on quality?). The tier split is only as safe as the first, and
  only worth it if the second holds.
- **Pending the ledger's own operation:** whether the spec's forecasts are actually calibrated —
  the ledger is the instrument that will find out.
- **A new eval this design creates:** router accuracy. The harness's one new failure surface;
  measure it before trusting it.

Everything here is single-family-directional in its evidence and unbuilt in its code. This is the
design; the runs come later.
