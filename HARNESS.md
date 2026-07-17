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

- **It is** a thin, per-turn pipeline that (1) picks which register a turn wants, (2) re-injects
  the chosen spec, (3) optionally exposes verify tools, (4) optionally logs forecasts to a ledger,
  and (5) records telemetry.
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
  [1] Router ───────── classify the turn's register → {full · lite · none}
    │                  (unsure → full; misreading a trap as simple is the worse error)
    ▼
  [2] Injector ─────── re-prepend the chosen spec THIS turn  (persistence / anti-drift)
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

- **What.** A cheap classifier reads the incoming turn (and a little context) and outputs a
  register: **analytical** → `SPEC.md`, **everyday / relational / generative** → `SPEC-lite.md`
  or none, **ambiguous** → default. It can be a small model call, a rule set, or a hybrid.
- **Gap it closes.** Run 09 measured the cost of applying the full apparatus to a turn that
  wanted a short/warm/committed answer (helpfulness 7–1 loss on the downside block). Run 11
  showed the model can't be made to suppress its own apparatus reliably from inside the prompt.
  A harness-level router does the suppression **by choosing the spec**, deterministically, before
  the model ever sees the turn. This is the "when needed" deployment the whole idea rests on.
- **Counterweight (Principle 2).** The router is itself a classifier that can be wrong, in two
  directions: (a) route a **disguised trap** to lite/none → miss the trap (the dangerous error);
  (b) route a **simple turn** to full → the "worse clerk" cost returns. Mitigation is the same
  asymmetric default the spec uses internally: **when unsure, default to full** — misreading a
  trap as simple is the worse error (run 11's own logic). Add a **sticky bias** so one ambiguous
  turn doesn't flip register mid-thread.
- **Measured by.** A *new* eval (call it the router accuracy run): label a battery of turns by
  intended register, measure router agreement, tune the unsure-threshold. **The router is the
  one genuinely new failure surface this harness introduces — it must be evaluated, not assumed.**
  Grounding for the *benefit* itself is already in runs 09 and 11.

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

### 4. Forecast ledger — the one memory feature with a named justification

- **What.** When a response contains a **scorable** forecast (numeric probability + time window +
  resolution criterion — exactly what the spec's Forecasting section demands), log it to a
  persistent ledger with its resolution date. A background job settles due forecasts against
  reality (via search, or a prompt to the user) and maintains a running calibration score.
- **Gap it closes.** DESIGN's **explicitly-named open gap**: the spec demands scorable forecasts
  but *nothing ever scores them* — "the loop can only close outside the model, in a persistent
  ledger that settles each forecast against the world rather than the model's own plausibility."
  This is that ledger. Memory here is not decoration; it is the missing infrastructure DESIGN
  names.
- **Counterweight.** Garbage resolution → garbage calibration: the ledger needs real ground truth,
  and only forecasts that actually resolve can be scored. Mitigation: log only forecasts with a
  clear resolution criterion (the spec already requires one); settle by search where possible,
  flag ambiguous ones for the user.
- **Measured by.** The ledger **is** the measurement instrument — it produces, over months, the
  forecasting-calibration curve that no single-session eval can. It answers a question Track 2
  can only approximate for recall.

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
   right register, kept fresh every turn.
2. **+ Verify layer** — build **after run 13 Track B** shows the spec beats bare-with-tools (skip
   if B-H4 holds).
3. **+ Forecast ledger** — the highest-value memory feature, and the only one with a named gap;
   build when you want the slow calibration loop closed.
4. **+ Telemetry** — cheap, add whenever you deploy for real.

Do **not** build all five as a monolith. Each is independently valuable and independently
measurable; coupling them is how a clean two-layer system turns into an unauditable one.

## What is grounded vs. pending

- **Grounded now (runs 09, 11):** the *routing* benefit — the model can't self-detect register,
  and misapplied full-spec has a real cost. This is why the harness exists.
- **Pending run 13:** persistence (Track A) and tool-verification (Track B). Build components 2
  and 3 only if those runs back them.
- **Pending the ledger's own operation:** whether the spec's forecasts are actually calibrated —
  the ledger is the instrument that will find out.
- **A new eval this design creates:** router accuracy. The harness's one new failure surface;
  measure it before trusting it.

Everything here is single-family-directional in its evidence and unbuilt in its code. This is the
design; the runs come later.
