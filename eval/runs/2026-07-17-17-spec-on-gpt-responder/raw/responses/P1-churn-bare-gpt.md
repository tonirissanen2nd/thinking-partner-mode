# P1 churn — BARE GPT-5-High (no spec, question only). Temporary chat.

Don't shift the whole team yet. A 40% relative increase is a strong signal, but it does not establish that weekend support coverage is causing the churn—or that more staffing will fix it.

Verify three things: Absolute impact (if weekday churn is 1.0% and weekend 1.4%, that's 40% relative but only 0.4 percentage points; estimate customers/revenue at risk). Comparability (control for segment, tenure, plan, geography, acquisition channel, billing date, product incidents, ticket severity — weekend customers may have a different risk profile). Timing (whether "weekend churn" means cancellations submitted on weekends, customers who contacted support on weekends, or churn after a weekend interaction — different interventions).

Then run a controlled staffing pilot rather than a full schedule change: increase weekend coverage 4-8 weeks in selected queues/regions/alternating weekends; keep a comparable control group; track response time, resolution time, abandonment, escalation, satisfaction, 30-day churn after contact; include staffing premiums, weekday degradation, burnout in cost.

A sensible initial move: reallocate ~15-25% of coverage to the weekend hours/segments with highest churn and longest response times. Expand only if the pilot produces a meaningful incremental churn reduction and positive return after labor costs.

The key decision metric is not whether weekend churn is higher; it is whether additional weekend staffing causes enough churn reduction to justify the operational trade-off.

## MARKER SCORING (mechanical)
# spec-GPT markers present: confidence-label+basis YES; base-rate/absolute YES; causal-reframe YES; scorable-forecast(numeric prob+refclass+window) YES; non-estimable YES; ruin+EV-vs-bounded YES; verify-flags YES
# bare-GPT markers present: confidence-label+basis NO; base-rate/absolute YES; causal-reframe YES; scorable-forecast NO; non-estimable NO; ruin+EV-vs-bounded NO (cost trade-off mentioned but not ruin-framed/labeled); verify-flags partial
# DELTA (spec-only): confidence-label+basis, scorable-forecast, non-estimable, ruin/EV-vs-bounded labeling
