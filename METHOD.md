# Method & Map

*What outlives the spec.*

This document is the part of the project that transfers. `SPEC.md` is one artifact; `FINDINGS.md`
records what nineteen runs established about *it*. This document abstracts away from the specific spec
and states the two things that generalize to **anyone evaluating any prompt-level behavioral
intervention**:

- **Part I — the method:** a discipline for measuring whether a prompt intervention actually *does*
  anything, and for not fooling yourself when it appears to.
- **Part II — the map:** where the prompt layer's power ends — what it installs reliably, what it
  installs only contingently, and what it cannot reach at all.

Both are distilled from a closed iterate-and-measure loop (19 pre-registered runs), and both are stated
so they apply to a *different* spec, prompt, or model than the ones here. Run numbers are cited as
evidence, not as required reading.

---

## Part I — The transferable method

Ten principles, each stated generally, with the run that taught it and how to apply it.

### 1. Pre-register before you run
Commit the hypotheses, the acceptance bands, **and the revert rule** to writing before the first
elicitation. Without this, every result becomes a story you tell afterward. Every run here has a
`PRE-REGISTRATION.md` written first; the discipline is what makes a null informative instead of
disappointing.

### 2. Prefer judge-independent anchors to LLM-judge preference
Score against something that cannot flatter you: an **external answer key** (deterministic grading), a
**mechanical marker count** (does the apparatus appear — regex, not opinion), or a **near-binary act**
(did it cave / correct the myth / demote the label). Reserve pairwise "which is better" judging for
what genuinely needs it, and know it is your softest instrument. In this project the findings that
survived contact with everything else are exactly the keyed ones; the pairwise-judged ones were the
ones that later moved.

### 3. Treat the LLM judge as a confound, not an oracle
A judge from the **same model family as the responder over-credits that family's house style.** Two
Claude judges disagreed on ~40% of soft-axis cells; a genuinely non-Claude judge did **not** reproduce
the flagship "better analyst" result and actively penalized the register as padding — and a *stronger*
non-Claude judge diverged *more*, not less (run 16). Rule: if you must use an LLM judge, use **≥2
families** and treat cross-family disagreement as the real uncertainty band. Never report single-family
A/B preference as ground truth. Its "quality" verdict is partly a taste verdict.

### 4. Turn the intervention's own skepticism on its own results
A clean, intuitive, single-source win — "100% across 3,000 labels" — has the exact shape of a result
that fails to replicate. Apply the **replication-crisis prior to your own headline**: discount its
*direction*, not just its magnitude, and name the cheapest run that would break it. Here that discount
was written down *before* the test, and the test (an adversarial battery) vindicated it — the 100%
cracked to 91% (run 14). If your result has no conceivable failure path, that is a reason to distrust
it, not to celebrate.

### 5. Separate "changes what it says" from "changes what it does"
The prompt layer reliably changes the model's **account of its reasoning** (labels, steelmen, apparatus
appear on cue) and only sometimes changes the **reasoning itself**. Measure both, separately:
**mechanical marker presence** (form) versus **keyed accuracy** (substance). The most common self-deception
is reading installed *form* as delivered *substance*. Form installed ≠ capability installed (the spec
made forecasts *scorable* but not *more accurate*, run 15; it installed the register on a second model
family, run 17, without installing the benefit, run 19).

### 6. Always run a bare / no-instruction arm — the ceiling check
"The intervention produced behavior X" is meaningless until you show the **base model didn't already
produce X**. Many plausible clauses are **inert because the base model already does the thing**:
resisting bare social pressure (run 08 on Claude, run 17 on GPT), demoting facts it can't know
(run 19). Inert is not harmful, but inert is not valuable either, and the two are invisible without the
bare arm. As base models improve, more of any spec drifts into this category — so re-run the ceiling
check over time, not once.

### 7. Build the battery to break your result, then report where it breaks
A **near-ceiling battery under-tests** and manufactures clean wins (run 10 was 97% — an under-stressed
instrument). Construct items *designed to produce the failure event you claim doesn't happen*
(run 14's adversarial battery; run 19's post-cutoff items). And **control the confounds explicitly**:
when testing recall, verify the model didn't secretly know or search — a battery of post-cutoff facts
is its own search-detector (runs 18–19). If the instrument can't break the claim, the instrument, not
the claim, is what you've measured.

### 8. Revert on the pre-registered trigger — even when the change feels good
A change with a real, visible benefit that trips its committed failure trigger **does not ship**
(frame-detection had a genuine benefit but regressed trap depth → reverted, run 11). Moving the
goalposts after seeing the result destroys the entire value of pre-registration. The discipline is only
worth anything at the exact moment it costs you something.

### 9. Reuse a shared baseline for comparability and cost
Freeze one set of responses and reuse it across variants, so runs are **directly comparable** and each
new arm is cheap (runs 03–06 reused a baseline; runs 12 and 16 re-scored existing responses). This also
isolates the variable you actually changed.

### 10. Record the inert, the moot, and the compromised — prominently
Honesty over promotion is not a virtue signal; it is the highest-information output. The clauses that
turned out inert, the benefits that are moot on current models, the null that was **compromised by your
own probe design** (recorded, not buried — run 13) — these are precisely what other people hide, which
makes them the most valuable thing you can publish. A program that only reports its wins has told you
almost nothing.

**The method in one line:** *pre-register, anchor to something that can't flatter you, ceiling-check
against bare, build the battery to break your own result, discount your clean wins, revert on your own
trigger, and publish the inert.*

---

## Part II — The map: where the prompt layer stops

A behavioral spec's reach has four layers. The generalizable finding is that they are very different in
how far a prompt can push them.

### Layer 0 — Installable, portable, cheap: **form**
Register, confidence labels, the outside-view apparatus (reference class, base rate, non-estimable),
steelman, sequencing, apparatus suppression on cue. A prompt installs these **reliably**, and — the
part that surprised us — **across model families**: a non-Claude model executed the same directives and
produced the same register (run 17). This is real, and it is the cheap, dependable product of a prompt.
It is also the *least* of what you probably wanted.

### Layer 1 — Contingent: **benefit is base-model-relative**
Whether the installed form *helps* is not a property of the spec. It is a property of **(spec × base
model × task)**. The same calibration clause **cut confidently-wrong on one model** (Claude 4.x, which
lacked enough volatile-fact humility — run 14) and was **inert on another** (GPT-5-High, which already
self-hedges what it can't know — run 19). The anti-sycophancy branch is inert on every current frontier
model tested. Consequence: **the benefit shrinks as base models improve**, and "does this spec help?"
has no model-independent answer. Design for the model you have, and expect the answer to expire.

### Layer 2 — Judge-relative: **the *appearance* of benefit**
On the soft, quality-of-answer axes, measured "betterness" is partly the **judge's house-style
preference**, not a fact about the answer. A same-family judge over-credits the register; a cross-family
judge discounts or penalizes it (run 16). So any A/B "this spec makes better answers" claim is, on the
soft axes, entangled with who is scoring. Only keyed substance escapes this. Treat pairwise "quality"
wins as taste-contaminated until a second family confirms them.

### Layer 3 — Out of reach of the prompt entirely: **accuracy and judgment**
Some things a prompt **cannot install**, no matter the wording:
- **Forecast accuracy.** The spec makes forecasts *well-formed and scorable* — numeric probability,
  reference class, resolution criterion — but *not more correct* (run 15). Form is prompt-reachable;
  prescience is not.
- **Calibration over time.** Tetlock's result is earned by *scored feedback over many forecasts*, not
  by reading a good rule. A prompt forces a label; only outcomes force calibration.
- **The fat-tail / black-swan branch.** Validated by mechanism and argument, but its *outcome* is
  unscoreable by any battery (a non-estimable claim has no key). It lives in a different epistemic
  category from the trunk.

Everything in Layer 3 requires a **real-world feedback loop** — a persistent ledger that logs
predictions and scores them against reality (the "layer two" the prompt is only the front half of). The
prompt is necessary and insufficient; the loop is the part you cannot skip and have not built until you
build it.

**The map in one line:** *the prompt layer installs legible reasoning — portable, cheap, and real; it
does not install accuracy or judgment — those are base-model-bounded, task- and judge-relative, and for
the parts that matter most, reachable only by a real-world feedback loop the prompt cannot substitute
for.*

---

## Coda — using this on your own intervention

If you are evaluating a prompt, a system message, a "mode," or a behavioral spec of your own, the method
compresses to a checklist:

1. Pre-register hypotheses, bands, and the revert rule — before running.
2. Anchor to a key, a marker count, or a binary act; use A/B preference last and least.
3. Run a **bare arm** every time; "it did X" is meaningless if bare also did X.
4. If you use an LLM judge, use **two families**; treat their disagreement as your error bar.
5. Build the battery to **produce the failure you claim doesn't happen**; control for the model already
   knowing or searching.
6. **Discount your own clean wins** and name the cheap run that would break them; then run it.
7. Separate **form installed** from **substance delivered** — measure them apart.
8. **Revert on your committed trigger**, especially when the change looks good.
9. **Publish the inert and the compromised**, prominently.

And set expectations from the map: **expect to install form; expect the benefit to be contingent and
shrinking as models improve; expect the appearance of benefit to be partly your judge's taste; and
expect the part you actually wanted — accuracy, calibration over time, the tail — to require a loop the
prompt cannot reach.** A behavioral spec is a real but narrow instrument. Knowing exactly how narrow,
and why, is worth more than one more polished clause.
