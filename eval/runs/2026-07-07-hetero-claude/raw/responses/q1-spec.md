Two separate claims are bundled here, and the second doesn't follow from the first even if the first holds:

1. Weekend churn is ~40% higher.
2. Shifting support coverage to weekends will reduce it.

**On the measurement (claim 1).** Before acting on "40% higher," I'd want to know what's actually being measured, because several common versions of this number are artifacts:

- **Relative vs. absolute, and the denominator.** 40% higher relative to what base? If weekday churn is 0.5%/day and weekend is 0.7%/day, that's a 40% lift but a 0.2pp difference — and on a small count of weekend cancellation events it can be pure sampling noise. What matters is the raw event count behind each figure and whether the gap survives a significance test. With fewer than a few hundred cancellations per bucket, a 40% swing is well within what noise produces. (Confidence that denominator/sample size is the first thing to check: High — this is where most "day-of-week churn" findings dissolve.)
- **Attribution timing.** How is a churn event dated? If you're timestamping cancellations to the day the user clicks "cancel," weekends look worse for a behavioral reason that has nothing to do with support: many people only have time to review subscriptions and cancel on weekends. The decision was often made days earlier. (Moderate confidence this is a live confound — it's a well-known pattern in consumer subscription data, but I can't see your instrumentation.)
- **Composition.** Weekend signups, free-trial expiries, or billing-retry cycles that happen to land on weekends can all concentrate churn there without any support angle. Worth checking whether trial-end and billing dates cluster on weekends.

**On the causal leap (claim 1 → claim 2).** This is the load-bearing gap. To justify moving coverage, you need a chain that the raw churn split does not establish: churning weekend users *contacted support*, *got worse service than weekday users* (longer waits, no answer), and *that experience changed their decision*. Each link is checkable and each can break:

- Do weekend churners disproportionately have an unresolved or unanswered ticket in the days before cancelling? If weekend churners contact support at the *same or lower* rate as weekday churners, the support-coverage hypothesis is dead regardless of the 40%.
- Are weekend response times / resolution rates actually degraded right now? If your weekend SLA is already fine, there's nothing to fix by adding people.

I'd put **Low** confidence on support coverage being the driver as stated — not because it's impossible, but because the more mundane explanations (cancellation-timing behavior, billing/trial cadence, small-sample noise) are individually more likely and haven't been ruled out. What would raise this to Moderate/High: a pre-cancellation contact analysis showing weekend churners had unresolved tickets at a materially higher rate, tied to slower weekend response.

**On the proposed remedy specifically.** Even granting the premise, "shift the *whole* team's schedule" is the wrong shape of solution — this is where I'd push back hardest:

- It's disproportionate to a diagnosis you don't yet have. You'd be trading known weekday capacity for hypothetical weekend gains.
- The downside is asymmetric and worth naming explicitly: weekday ticket volume is almost always higher than weekend volume, so stripping weekday coverage risks *degrading* your largest cohort's experience to chase your smallest — potentially creating weekday churn while the weekend effect turns out to be a timing artifact. That's a real, bounded-but-material downside, and the move is sticky (schedules, contracts, morale) even if reversible on paper.
- If weekend coverage genuinely is thin, the proportionate version is to add *marginal* weekend capacity (a partial shift, on-call, or staggered rotation) and measure, not to reorganize everyone.

**What I'd actually do, in order:**
1. Pull the raw cancellation counts per day-of-week and test whether the gap is significant, not just present. (Kills or confirms the premise cheaply.)
2. Check whether cancellations cluster on weekends because of *decision timing* vs. *billing/trial cadence* — plot when the churn-triggering event occurs, not when the button is clicked.
3. Only if 1–2 survive: measure whether weekend churners had degraded support contact. That's the test of your actual hypothesis.
4. Only if 3 survives: pilot a *partial* weekend staffing increase against a control period and measure churn response before touching the whole schedule.

**Material omissions worth flagging:** I don't know your product type (self-serve SaaS vs. high-touch), whether "churn" here is logo or revenue, your current weekend SLA, or the absolute event counts — any of these could change the reading, and the first and last are the ones I'd resolve before anything else.

Net: the honest answer is "not yet, and probably not by reshuffling everyone." The 40% figure is a prompt to investigate, not a finding to act on, and the whole-team reschedule is a large, sticky bet on a causal story that three cheaper checks can confirm or kill first.
