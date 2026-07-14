Before you move the whole team, I'd want to close the gap between "churn is higher on weekends" and "weekend support coverage is the cause." Those are very different claims, and only the second one justifies the reschedule.

**Some things worth checking first:**

*What does "weekend churn" actually mean?* Churn events usually get timestamped when something fires — a subscription lapses, a card fails, a cancel button gets clicked. If billing runs on a weekly cycle that lands Saturday, or if dunning retries cluster on certain days, you can get a big weekend spike that has nothing to do with customer behavior at all. Check whether the timestamp is the customer's decision or your system's bookkeeping.

*Who churns on weekends?* If weekend churners are disproportionately consumer/self-serve users and your weekday churners are B2B, you may just be looking at two different populations with different rhythms, not a coverage problem. Segment before you act.

*Did those churned users actually contact support?* This is the big one. If most weekend churners never opened a ticket, then support coverage isn't the lever — no amount of staffing helps people who were never going to reach out. Pull the subset who did contact support before churning and look at their wait times versus weekday contacts. That's the number that would actually justify the change.

*Is 40% a lot?* Relative lifts sound dramatic at low base rates. 40% higher than 0.5% is 0.7%. Also worth knowing: what's the confidence interval, and how many weekends are in the sample? Weekly seasonality is noisy, and a few weeks of data can easily produce a 40% swing that regresses away.

**On the decision itself:** even if weekend support turns out to be the cause, "shift the whole team" is the most expensive and least reversible version of the intervention. Cheaper tests that would give you the same information:

- Staff one or two extra weekend shifts for a month and see whether weekend churn moves.
- Look at whether weekend *response times* are actually degraded. If they're fine, coverage isn't the bottleneck.
- Consider whether the fix is asynchronous — better self-serve docs, a "we'll get back to you Monday" autoresponder that actually sets expectations, a save-offer flow on the cancel page.

There's also a real cost on the other side: weekend-heavy schedules hurt retention and morale on the support team itself, and that's a slow, hard-to-reverse expense.

**What I'd do:** run the "did they contact support?" analysis first. It's cheap and it either kills the hypothesis or makes it much stronger. If it holds up, pilot extra weekend coverage before restructuring anyone's schedule permanently.

Happy to help think through the query if you want to share how churn is being defined in your data.
