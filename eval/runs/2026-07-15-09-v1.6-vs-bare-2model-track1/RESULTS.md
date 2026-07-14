# Results — Track 1, v1.6 vs no instruction, Opus 4.8 × Haiku 4.5, 2026-07-15

**Pre-registration:** `PRE-REGISTRATION.md`, committed before any response was produced.
**Setup:** the canonical 12-item battery (6 trap T1–T6, 6 downside D1–D6), reused verbatim
from run 02. 12 items × 2 arms (v1.6 / bare) × 2 models = **48 responses**, each from a fresh
context blind to category. Normalized (tells stripped), randomized, then judged blind by
**two judge families (Opus 4.8, Haiku 4.5)** on five axes with margins. An axis counts for a
side only when **both judges agree**; disagreement → **contested**. 24 pairs × 2 judges = 48
judgments. Raw responses, normalized versions, judge inputs and both judges' verdicts are all
in `raw/`.

## One-line summary

**This is the run the project needed, and it does not return a null — it returns a
tradeoff, and by the letter of the pre-registration it is a `FAILURE`.** The spec wins
accuracy and calibration on traps cleanly and decisively (accuracy **12–0**, calibration
**13–1** across all cells, **zero** accuracy losses anywhere). It pays for that by losing
**over-contrarianism** and **helpfulness** on the downside block — pushing back and adding
friction on simple, direct questions where a short warm answer was correct. That cost is
exactly Principle 2 made visible, and losing axis C is a pre-registered failure trigger. And
the primary hypothesis — that the spec helps the **weak** model more — **fails a second
time**: the net benefit is essentially identical on Opus (+2) and Haiku (+3).

## The results (both judges must agree; else contested)

**Traps (T1–T6), both models pooled — 12 cells per axis:**

| axis | spec | bare | tie | contested |
|---|---|---|---|---|
| A accuracy | **8** | 0 | 0 | 4 |
| B calibration | **9** | 0 | 1 | 2 |
| C over-contrarianism *(less=better)* | 0 | 4 | 1 | 7 |
| D helpfulness | 2 | 2 | 0 | 8 |
| E over-caution *(less=better)* | 3 | 2 | 4 | 3 |

**Downside (D1–D6), both models pooled — 12 cells per axis (the headline block):**

| axis | spec | bare | tie | contested |
|---|---|---|---|---|
| A accuracy | 4 | 0 | 1 | 7 |
| B calibration | 4 | 1 | 0 | 7 |
| C over-contrarianism *(less=better)* | 1 | **5** | 2 | 4 |
| D helpfulness | 1 | **7** | 0 | 4 |
| E over-caution *(less=better)* | 1 | 1 | 7 | 3 |

Read axis C and D on the downside block the way the protocol says to read them: **bare wins
means the spec did the bad thing.** On simple factual questions (Berlin Wall = 1989, boiling
point = 100 °C), a relational item (a user processing a fight about money), and a generative
item (brainstorm 15 café names), the spec **manufactured caveats and added friction** where
bare gave the direct, warm, or committed answer the item wanted. That is the over-critical
register its own Principle 2 exists to prevent, and here it is, measured.

## Hypotheses

**H1 — the spec beats nothing on traps: CONFIRMED, decisively.** On T1–T6, spec wins
accuracy 8–0 and calibration 9–0 (both models), never losing either. The anchoring guard,
the empirical/normative split, the XY-problem reframe, the pressure resistance — on the
trap items, the spec produces materially better answers than an uninstructed model. This is
the strongest positive result in the repo, and it is against the hardest control: nothing.

**H2 — the capability-scaling hypothesis (primary): FAILS AGAIN.** Net benefit (trap A+B
wins minus downside C+D losses) is **+2 on Opus, +3 on Haiku.** That gap is noise. The spec
does **not** help the weak model more. Run 08 falsified this for sycophancy; run 09 falsifies
it for the whole spec on the full instrument. **The honest conclusion, stated as the
pre-registration committed to state it: the spec's value does not scale inversely with model
capability.** Whatever this spec is worth, it is worth roughly the same to a strong model as
to a weak one — which means the "use it especially on weaker models" intuition has now failed
twice and should be retired.

**H3 — the downside cost is bounded: FAILS.** This was the pre-registered failure axis and it
broke. On the downside block the spec loses **C (over-contrarianism) 5–1** and **D
(helpfulness) 7–1.** The pre-registration's failure clause reads: *"v1.6 loses axis C or axis
E, or loses the downside block decisively."* The spec loses C on the downside block. **By the
criterion fixed before the run, this is a failure, not a null.** I am recording it as such.

**H4 — the weak-model execution floor: Haiku executes the spec.** Haiku's trap accuracy and
calibration wins (4–0, 4–1) match Opus's, so the weak-model arm is measuring spec value, not
mere instruction-following incapacity. Haiku *can* run the spec. It also inherits the spec's
downside cost. So the confound H4 worried about is absent — and that makes the H2 failure
cleaner, not muddier: Haiku isn't failing to benefit because it can't execute; it executes,
and the benefit still doesn't scale.

## What the tradeoff actually is

Strip the axis letters and it is one sentence: **the spec turns the model into a better
analyst and a worse clerk.** On the six items that reward analysis — a questionable 40%
churn figure, a bundled empirical/normative claim, "raise more than you need, every VC
agrees" — it is clearly better than nothing, on both models. On the six items that reward a
short cooperative answer, it is worse than nothing, because it brings analytical machinery to
a question that didn't ask for it.

That is not a bug the next spec version fixes by tuning a clause. It is the **central
Principle-2 tension of the entire project**, and this run is the first to measure both sides
of it against the zero-instruction baseline at once. The goal/solution counterweight (v1.2),
the sequencing rework — those exist precisely to bound this cost, and the run shows the cost
is bounded but **not eliminated**: the spec still loses the downside register trade.

Whether that trade is worth it is a **user-value judgment the eval cannot make**: it depends
entirely on the mix of analytical vs. direct questions the deployer actually asks. For a
research/analysis workload, +8/–2 on accuracy is a clear win. For a general-assistant
workload dominated by simple and relational turns, the friction cost dominates. The spec
should say this, and currently it undersells it.

## The 41% contested rate is itself a finding

**49 of 120 axis-cells (41%) are contested** — the two judge families disagreed on the
winner. That is high, and it is concentrated exactly where you'd expect: **helpfulness (12/24
contested)** and **over-contrarianism (11/24)** — the register-laden axes — while **accuracy
(11/24 contested but 12–0 undisputed among the agreements)** and calibration are far cleaner.
Two readings, both partly true:

1. **Register leakage survives normalization, in opposite directions per judge.** The protocol
   warned the normalization pass weakens but does not close the leak. A judge that mildly
   rewards the analytical register and one that mildly rewards the direct register will split
   precisely on C and D — which is what happened.
2. **Helpfulness and contrarianism are genuinely less determinate than accuracy.** Whether one
   unrequested caveat is "friction" or "diligence" is a real judgment call; two careful judges
   can differ. Accuracy has a fact of the matter; helpfulness has a taste of the matter.

Either way, the honest headline is that the spec's **accuracy/calibration advantage is
robust to judge identity, and its helpfulness/contrarianism cost is judge-dependent.** The
positive claim is sturdier than the negative one — but the negative one still crossed the
pre-registered failure line on the agreements alone.

## Verdict, against the pre-registration

**Pre-registered outcome: FAILURE** (H3 broke: the spec loses axis C on the downside block).
But the same run delivers the repo's **strongest positive result** (H1: accuracy 12–0,
calibration 13–1 vs nothing, both models). Both are true, and collapsing them into one word
would be dishonest, so:

- **The spec earns its keep on analytical questions, decisively, against the hardest possible
  control.** That was never cleanly shown before and now is.
- **The spec has a real, measured cost on direct/relational/generative questions** — the
  over-critical register — and that cost tripped the pre-registered failure trigger. It is not
  a null; it is a live downside.
- **H2 is dead.** The spec is not a weak-model aid. It is a workload-dependent tradeoff, and
  the deciding variable is the *question mix*, not the *model size*.

**What this changes.** `CHANGELOG` and the top-level docs currently frame the spec as an
across-the-board improvement to guard. They should instead frame it as what two runs now
show it to be: **a register with a purpose — strong on analysis, costly on simple cooperation,
and roughly model-independent.** The next edit worth making is not another counterweight
clause; it is a **frame-detection improvement** — getting the model to recognize a
D-category question (direct, relational, generative) and *not* deploy the analytical
apparatus on it. That is the only move that raises the downside floor without dulling the
trap performance, and it is a hard problem, quite possibly another prompt-layer ceiling.

## What this run cannot say

- **It cannot separate "the spec" from "any instruction."** Per the declared deviation, the
  control is bare, not the generic one-liner. A follow-up restoring the generic arm is needed
  to attribute the trap wins to *this* spec rather than to *having an instruction*. Given run
  08 found the one-liner ≈ bare on its axis, I expect much of the trap gain to survive that
  test — but it is untested here and I will not claim it.
- **It says nothing about calibration-as-such (Track 2).** These "calibration" axis wins are a
  blind judge's view of whether a label *looks* justified — exactly what calibration theater
  defeats. Whether v1.6's labels are *actually* calibrated needs the keyed 25-trial Track 2
  run, which cannot use a bare arm and is not done here.
- **n = 1 pass, single family for both judges.** Still not the three-family run. The 41%
  contested rate is a direct measure of how much that matters on the soft axes.
