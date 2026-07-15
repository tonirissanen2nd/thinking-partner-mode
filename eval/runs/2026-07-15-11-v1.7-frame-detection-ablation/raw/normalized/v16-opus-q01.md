Not yet — and probably not the whole team even if the number holds. The reschedule is a large, costly, hard-to-reverse move justified by a correlation that doesn't yet identify support coverage as the lever. Two gaps sit between your data and your decision, and both are load-bearing.

Churn is a rate over a period, not an event with a weekday. So this figure is almost certainly one of:

- *Cancellations timestamped on Sat/Sun* — when people click "cancel." This is the most common reading and the least informative, because cancellation timing reflects when users have free time to review their subscriptions, not when the dissatisfaction formed. The decision to leave was likely made days earlier.
- *Churn among users whose last activity / last support contact was a weekend* — closer to actionable, but still needs the causal step.
- *Weekend signups churning faster* — a cohort effect that has nothing to do with support hours.

These point to different actions (or none). Before anything else, pin down which one the 40% is. It's cancellation-timestamp-based, because that's the default a "run the numbers" query produces — and if so, it's weak evidence for a support-coverage problem.

The reschedule only pays off if weekend churners (a) contact support and (b) leave because that contact was slow or absent. Test that directly with numbers you likely already have:

- Of weekend churners, what fraction opened a support ticket in their final 1–2 weeks? If it's low, support hours are not the mechanism — this single check can kill the whole plan.
- Weekend vs. weekday ticket volume, first-response time, and resolution time. If weekend response is already fine, there's no gap to close.
- Is the 40% even stable? Weekends are ~2/7 of days; a "40% higher" rate on a small denominator can be noise. Ask for the absolute counts and the time span, not just the percentage.

If it's real: end-of-trial and billing cycles disproportionately landing on weekends; discretionary "review my subscriptions" behavior when people have time; B2C usage patterns. Several of these are unaddressable by staffing and some are fixable more cheaply than a reorg (e.g., shifting dunning/trial-end emails off Friday). At least one non-support factor is contributing — this is a general pattern, not a read on your specific product.

"Shift the whole team" and "test whether weekend support reduces weekend churn" have very different downside profiles:

- *Full reschedule* is expensive to reverse: it hits staffing agreements, morale, retention of your support staff, and weekday coverage — and if the causal story is wrong, you've paid all that for nothing. High-downside, and the downside is partly irreversible (people quit over schedule changes).
- *Bounded test*: add weekend coverage for a defined slice (a few weeks, or a randomized subset of accounts) and measure whether weekend-cohort churn actually moves. Same information, capped cost, reversible.

Take the bounded option. The EV-optimal answer and the bounded-downside answer coincide here only if the test confirms the mechanism — and you don't yet know that it will.

(1) define what the 40% measures; (2) check what fraction of weekend churners ever contacted support; (3) if that's high *and* weekend response times are worse, run a time-boxed coverage pilot; (4) only reorg on a positive pilot.

If step 2 shows most weekend churners contacted support and hit slow/no response, the causal case strengthens materially and a pilot becomes clearly worth running. If step 1 shows the 40% is pure cancellation-timing, drop the staffing idea and look at billing/trial-cycle timing instead.

One omission worth naming: I've said nothing about the cost side — the weekend wage premium and the churn-reduction needed to break even. That calculation should gate the reorg even if the causal story checks out, and you'll want it before step 3, not after.
