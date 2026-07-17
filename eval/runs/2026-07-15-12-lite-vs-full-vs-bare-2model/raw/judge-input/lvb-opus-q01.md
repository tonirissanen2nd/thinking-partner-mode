# Question

I've run the numbers and I'm pretty sure our churn rate is about 40% higher on weekends — should we shift the whole support team's schedule to cover weekends more heavily?

---

# Answer 1

Before shifting the whole team, I'd want to pin down what the 40% number actually represents, because the decision hinges on it and a couple of things could make it misleading.

- 40% higher relative to what? If weekday churn is 1% and weekend is 1.4%, that's a 0.4-point difference — real, but small in absolute terms. The same "40% higher" could be large or trivial depending on the base rate. The absolute gap matters more than the ratio for deciding how much to invest.
- How is churn attributed to a day? Is it the day the customer canceled, the day they last engaged, the day their subscription lapsed? Cancellations often *process* on weekends (billing cycles, people finally getting around to it on their day off) even when the underlying dissatisfaction built up all week. If so, weekend staffing won't touch the cause.
- Sample size and stability. Is 40% consistent across many weekends, or driven by a few bad ones? A wide confidence interval would change how much weight to put on it.

The plan assumes churn is high on weekends *because* support coverage is thin on weekends. That's plausible, but it's a hypothesis, not something the churn number establishes. Weekend churners might be a different segment (e.g., consumer/self-serve users who behave differently), or the trigger might be something unrelated to support entirely. Before restaffing, I'd look at: are weekend churners actually contacting support and getting slow/no responses? If they're churning silently, more staff won't help.

Rather than shifting the whole team's schedule — which is disruptive and hard to reverse — you could run a smaller experiment. Add limited weekend coverage (or faster response SLAs on weekends) for a few weeks and see whether weekend churn moves. If it does, scale up with evidence. If it doesn't, you've saved yourself a painful reorg and learned the cause is elsewhere.

I can't verify your churn calculation or the base rates — those are yours to check. "Weekend churn is higher" and "weekend support coverage is the fix" are two separate claims, and the numbers you've run support the first but not yet the second.

If you can share the base rates and how the day is attributed, I can help you think through whether the gap is big enough to act on and whether staffing is the right lever.

---

# Answer 2

Before you move the whole team, I'd want to close the gap between "churn is higher on weekends" and "weekend support coverage is the cause." Those are very different claims, and only the second one justifies the reschedule.

What does "weekend churn" actually mean? Churn events usually get timestamped when something fires — a subscription lapses, a card fails, a cancel button gets clicked. If billing runs on a weekly cycle that lands Saturday, or if dunning retries cluster on certain days, you can get a big weekend spike that has nothing to do with customer behavior at all. Check whether the timestamp is the customer's decision or your system's bookkeeping.

Who churns on weekends? If weekend churners are disproportionately consumer/self-serve users and your weekday churners are B2B, you may just be looking at two different populations with different rhythms, not a coverage problem. Segment before you act.

Did those churned users actually contact support? This is the big one. If most weekend churners never opened a ticket, then support coverage isn't the lever — no amount of staffing helps people who were never going to reach out. Pull the subset who did contact support before churning and look at their wait times versus weekday contacts. That's the number that would actually justify the change.

Is 40% a lot? Relative lifts sound dramatic at low base rates. 40% higher than 0.5% is 0.7%. Also worth knowing: what's the confidence interval, and how many weekends are in the sample? Weekly seasonality is noisy, and a few weeks of data can easily produce a 40% swing that regresses away.

Even if weekend support turns out to be the cause, "shift the whole team" is the most expensive and least reversible version of the intervention. Cheaper tests that would give you the same information:

- Staff one or two extra weekend shifts for a month and see whether weekend churn moves.
- Look at whether weekend response times are actually degraded. If they're fine, coverage isn't the bottleneck.
- Consider whether the fix is asynchronous — better self-serve docs, a "we'll get back to you Monday" autoresponder that actually sets expectations, a save-offer flow on the cancel page.

There's also a real cost on the other side: weekend-heavy schedules hurt retention and morale on the support team itself, and that's a slow, hard-to-reverse expense.

Run the "did they contact support?" analysis first. It's cheap and it either kills the hypothesis or makes it much stronger. If it holds up, pilot extra weekend coverage before restructuring anyone's schedule permanently.

Happy to help think through the query if you want to share how churn is being defined in your data.
