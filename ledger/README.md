# Forecast ledger — the measurement instrument

This is "layer two" from `HARNESS.md`, built for real as a **measurement instrument** — the part with
*certain* value (`METHOD.md`, Part II, Layer 3). A prompt can make a forecast *scorable* (run 15); only
a persistent, resolved-against-reality ledger makes it *scored*. This turns a model's forecasts from
ephemeral, confident-sounding claims into an auditable track record.

It deliberately does **not** try to make the model forecast better. Whether feeding the scored track
record back improves calibration is the *improvement bet*, pre-registered separately in
[`PRE-REGISTRATION-improvement-bet.md`](PRE-REGISTRATION-improvement-bet.md) and **not assumed** by this
tool. Build and trust the measurement first; test the improvement second.

## What it delivers (the certain benefits)

1. **A real calibration score over time** — Brier, ECE, and a reliability curve: when the model says
   70%, how often does it actually happen?
2. **Auditable, user-correctable judgment** — you can see *where* it is miscalibrated (which reference
   classes it low- or over-balls) and discount accordingly, even if the model never changes.
3. **A judge-free way to compare specs / models on forecast quality** — scored against *outcomes*, not a
   taste-contaminated LLM judge (the failure run 16 exposed).

## Seeded with real data

`forecasts.jsonl` is seeded with **264 real, resolved forecasts** from run 15 (the spec's Forecasting
section producing numeric probabilities on resolvable items, scored against known outcomes). Run:

```
python ledger/ledger.py report
```

produces (today, on the seed data):

```
Brier score: 0.192            (0 = perfect, 0.25 = always-50%)
ECE:         0.149
Discrimination (top-half minus bottom-half resolve rate): +0.36   (good: high-prob forecasts resolve TRUE more)

Reliability curve:            every bin resolves HIGHER than forecast -> the model is systematically UNDERCONFIDENT
  [0.0,0.1) n=15  mean 0.04  resolved 1.00   (+0.96)   <- lowballed the "surprise" events badly
  ...
  [0.9,1.0) n=72  mean 0.96  resolved 1.00   (+0.04 ok)

Worst reference class: sports-record   Brier 0.812   (the marathon WR it forecast at ~4% and which happened)
Best:                  software-release Brier 0.013   (annual release cadence -> outside view nails it)

Per arm (judge-free spec-vs-bare):  bare Brier 0.181  <  full Brier 0.202   (reproduces run 15's finding)
```

That single report is the whole point: it **scores** the forecasts, **localises** the miscalibration
(great on base-rate items, terrible on genuine surprises), and **compares** arms without a judge — none
of which a prompt or a single session can do.

## Usage

```
# log a forecast the model just made (probability in [0,1])
python ledger/ledger.py log --q "Will X happen by 2027-01-01?" --prob 0.35 \
    --due 2027-01-01 --crit "resolves TRUE if ..." --refclass geopolitics --arm spec --source "gpt5 spec"

# list what's open and past due (the resolution work queue)
python ledger/ledger.py open

# when the outcome is known, resolve it
python ledger/ledger.py resolve --id f0007 --outcome 1

# score the whole track record (optionally one arm)
python ledger/ledger.py report [--arm spec]
```

Store is `forecasts.jsonl` (one JSON record per line; schema documented at the top of `ledger.py`).
No dependencies beyond the Python standard library.

## Where it sits

- `HARNESS.md` — the full second-layer design; this implements its Ledger component as a measurement tool.
- `METHOD.md` — why this is the only instrument that reaches "Layer 3" (accuracy / calibration over time).
- `PRE-REGISTRATION-improvement-bet.md` — the open question: does the *feedback* improve the model, or
  hit the same say-vs-do ceiling the prompt layer did?
