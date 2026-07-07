Two questions are bundled here, and they have different answers: "Is the 15% lift real?" and "Should I roll out?" Separating them is the whole game, because the second can be yes even when the first is only moderately supported — a checkout button is cheap to ship and cheap to revert.

Is the effect real? It depends on details p<0.05 doesn't tell you. The single number you quoted can't carry the conclusion. The load-bearing unknowns:

- **Was significance the stopping rule?** If you watched the dashboard and ended the test when it crossed p<0.05 ("peeking" / optional stopping), the true false-positive rate is far above 5% — commonly 20-30%+ with daily looks. This is the single most common way A/B tests lie. If the two-week duration and sample size were fixed *in advance* and you looked once at the end, 5% stands. If not, discount heavily. (can't assess your case without knowing your process.)
- **How many things were you testing?** One button vs. twenty metrics/variants is a different p-value. If this was the only comparison, fine. If it's the one winner among many, you've got a multiple-comparisons problem and the nominal p<0.05 is optimistic.
- **What's the confidence interval, not the point estimate?** "15%" is the center of a range. If the 95% CI is [2%, 28%], the real effect could be small; if it's [12%, 18%], you have a tight estimate. p<0.05 only tells you the interval excludes zero — it says nothing about whether the lift is large enough to matter. Ask for the interval.
- **Novelty effect.** A visually new button can lift conversion transiently because it draws attention; the effect can decay as users habituate. Two weeks may not distinguish a durable lift from a novelty spike. This biases the two-week number *upward* as an estimate of steady-state.
- **Cycle coverage.** Two weeks captures two of each weekday but zero monthly cycle (paydays, billing dates, month-end). Probably minor for checkout; flagging it as an unmeasured dimension.

Note the category: "is it real" is an empirical claim, and you've shown *evidence against the null*, not *confidence in a 15% durable lift*. Those are not the same thing, and p<0.05 is routinely misread as the second.

Should you roll out? Probably yes — but the reason is the downside profile, not the p-value. This is the part the significance framing obscures. A checkout-button change is reversible and low-cost: if the lift is illusory or decays, you revert and you've lost little. That asymmetry — bounded, recoverable downside vs. a plausible real gain — makes rollout a reasonable EV-positive move *even at moderate confidence that the effect is real*. You do not need certainty to justify a reversible action. Contingent on the change genuinely being easy to revert and not coupled to anything hard to unwind (pricing, contracts, data migrations). If it is coupled to something irreversible, raise the evidence bar first.

A scorable version of the forecast, so this isn't just vibes: conditional on the test having a pre-registered fixed sample/duration and a single primary metric, I'd put ~70% that a true lift of at least 5% (relative) persists over the next 90 days; if instead the test was peeked-at or cherry-picked from many metrics, drop that to ~40-45%. Resolution: measured conversion in a held-back or post-rollout comparison window at 90 days.

What actually moves your confidence, in order:
1. Confirm the stopping rule and metric count — this alone can swing "real" from Moderate to Low or up to High.
2. Get the confidence interval on the lift, not just the p-value.
3. If you can, keep a small holdout (e.g., 5-10%) on the old button post-rollout for a few weeks. This directly tests novelty decay and costs you almost nothing — it's a strictly better path than "roll to 100% and hope," and it's the move I'd push for.

Don't say "confident this is real" — say "evidence is positive, downside is bounded and reversible, so I'll ship it with a holdout to confirm the effect persists." The holdout is what lets you claim it's real later.
