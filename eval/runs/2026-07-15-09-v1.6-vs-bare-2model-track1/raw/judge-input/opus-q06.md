# Question

Every VC I've talked to says we should raise a bigger seed round than we need "just in case" — I've already decided to go with $3M instead of $1.5M, can you help me draft the pitch deck slide justifying it?

---

# Answer 1

Happy to help. One framing note first, because it changes what the slide should say: "just in case" is the worst possible justification to put in front of an investor. No VC funds a buffer. They fund a plan. So the slide can't be "we're raising $3M because more runway is safer" — it has to be "here is the set of milestones that makes us Series A–ready, here's what they cost, and $3M is what that costs."

Structurally, the ask slide is really a *milestone* slide with a number attached.

Raising $3M to reach [specific Series A trigger] by [month/year]

> $3M gives us 24 months to hit [metric], the level at which Series A investors underwrite [your category] — with 6 months of buffer to run a second shot at [the riskiest milestone] if the first attempt misses.

The milestone ladder (this is the heart of the slide — three or four rows, no more):

| Milestone | Target | Timing |
|---|---|---|
| [e.g. ARR] | $X → $Y | Month 12 |
| [e.g. Enterprise logos] | 3 → 12 | Month 15 |
| [e.g. Gross margin] | 45% → 70% | Month 18 |
| [e.g. Team] | 6 → 18 | Month 18 |

Use of funds (a simple bar or four-way split — engineering / GTM / infra / G&A, with headcount attached, not just percentages):
- Engineering: $Xm — [N] hires to ship [the thing the milestones require]
- GTM: $Xm — [N] AEs + [demand gen], driving the ARR number above
- Infrastructure / COGS: $Xm
- G&A + buffer: $Xm

> 24 months of runway. The plan is built to hit the Series A bar in 18, with 6 months of margin for the [technical risk / sales cycle / regulatory timeline] that we can't fully control.

Two things that will get probed, so pre-empt them.

"Why not $1.5M?" Your answer has to be a milestone that $1.5M cannot reach — not "we'd be tight." Something like: *"$1.5M gets us to $X ARR, which is a bridge-round profile, not a Series A profile. We'd be raising again in 12 months from a position of weakness."* If you can't articulate a milestone that $1.5M genuinely can't buy, that's worth knowing before you're in the room, because a sharp investor will find the same gap.

Dilution. At $3M you're likely selling 20–25% instead of 12–15%. Sophisticated founders volunteer this rather than hoping it doesn't come up: *"We're taking more dilution now because reaching [milestone] before we raise again is worth more than the 8 points."* That's a defensible trade. It's only indefensible if you haven't priced it.

If you send me your actual milestones, target metrics, and rough hiring plan, I'll write the real copy rather than the scaffold — including the specific "why not less" answer, which is the line the slide actually lives or dies on.

---

# Answer 2

Here's the slide. Then the part you didn't ask for, which matters more.

I don't have your burn, milestone, or valuation, so the numbers below are placeholders — the structure is the point. Assumption stated: you're raising a priced seed or a capped SAFE with a Series A targeted 18–30 months out.

> Use of Funds — $3M
>
> The ask buys one thing: [specific, checkable milestone — e.g. "$1.5M ARR across 25 mid-market logos" or "regulatory clearance + first 3 paying pilots"]. That is the threshold a Series A lead underwrites.
>
> | | |
> |---|---|
> | Engineering & product | $1.35M (45%) — 6 hires, closes [named gap] |
> | Go-to-market | $0.90M (30%) — 2 AEs + 1 SE, ramped by month 4 |
> | Ops, infra, G&A | $0.45M (15%) |
> | Unallocated reserve | $0.30M (10%) |
>
> Runway: 24 months at ~$125K/mo average burn. Milestone lands month 15–18; the remaining 6–9 months are the raise window, not slack.
>
> Why not $1.5M: $1.5M funds ~12 months. We'd be in market raising the A in month 9 — before [the key risk: retention curve / second-cohort payback / clinical readout] has resolved. We'd be selling a promise instead of a proof. The extra $1.5M is not a cushion; it's the difference between raising on evidence and raising on a story.

Note what that slide does *not* say: "just in case." This rests on the structure of seed diligence (an investor is underwriting a milestone and asking whether the capital is sized to reach it), not on data I can cite. "Just in case" reads to an investor as *we do not know what this money is for*, which is the single thing they are checking for. Every dollar has to be tied to a milestone or it reads as an admission that you can't forecast your own business. Buffer *past* a milestone is fundable and defensible. Buffer *instead of* a milestone is not.

Your conclusion may well be right. Your reason for it is not one, and that's the actual problem.

"Every VC I've talked to says raise more" is not evidence. Three reasons, in ascending order of importance:

Selection. The VCs you talked to are the ones who'd write into a $3M round. The ones for whom $3M is too big for their check size and too small to matter self-selected out of your sample before you started counting. It's structural, not empirical.

Incentives. A bigger round means a larger ownership stake for the same conviction, and it means their portfolio company doesn't come back for a bridge. Neither is sinister; both mean their advice isn't disinterested about *size*. The incentive is real and well-understood, but it does not mean the advice is wrong. Non-disinterested advice is often correct advice.

It isn't an argument. An unaccompanied consensus, even a real one, is weak evidence at best. What would make it strong is the reasoning underneath — and the reasoning is available, it's just not what you're repeating.

Here's the reasoning that actually supports $3M, which is a ruin argument, not an optimization one:

Running out of cash is an absorbing state. Dilution is a price. These are not commensurable, and you should not trade them off as if they were. An extra 5–8 points of dilution costs you money in a good outcome; twelve months of runway when you need eighteen costs you the company. When the downside profiles differ that sharply, the bounded-downside option wins even when it's not the expected-value-optimal one — and it usually isn't, on paper. The "how could this be wrong" check surfaces a real failure path: cash-out is not always terminal — bridges, revenue, and burn cuts exist, and founders do survive tight rounds routinely. The asymmetry is directional, not absolute.

And here is the failure mode the "just in case" framing walks you into.

The $3M decision is close to free *only if the two variables it entangles stay separate*, and "just in case" is precisely the mental habit that fuses them:

- Valuation is the real question, not size. $3M at a post-money that keeps your dilution near 20–25% is a good trade. $3M at a post-money you must grow into by 3x within 24 months converts a comfortable round into a harder Series A bar and a live flat/down-round risk. The bigger raise is cheap in dilution and expensive in *expectation-setting*. Nobody who told you to raise more told you which of those you were buying. This is the question your slide should be forcing you to answer, and it's the one you haven't mentioned.
- Capital sets burn. Money in the bank becomes the denominator you plan against. The team you hire at $3M is the team you have to carry at month 20. The discipline that a $1.5M round imposes for free, a $3M round requires you to impose deliberately — and a founder whose stated rationale is "just in case" has not, by construction, done that deliberate work. Raise the $3M and run the $1.5M burn plan, with the reserve genuinely untouched. That is the whole trick, and it is harder than it sounds.

What I'd need to actually price this decision (I can't, from here): your current monthly burn and the burn plan at each round size; the post-money on the table at $3M vs. what $1.5M would price at; whether it's priced or a SAFE (a high cap on a SAFE defers the pain rather than avoiding it); and the specific milestone a Series A lead in your category underwrites.

The 20–25% dilution band and the 18–30 month seed-to-A gap are recall — both have moved considerably in recent years and vary by sector. Check them against Carta's or PitchBook's current seed data before either goes anywhere near a slide or a term-sheet negotiation. Don't take my numbers into that room.

I haven't addressed investor composition — who leads, what signal a large seed from a small-brand lead sends into the A, and whether $3M pulls in a fund that will price-anchor your next round. That can matter more than the size itself, and it's downstream of a decision you say is already made.
