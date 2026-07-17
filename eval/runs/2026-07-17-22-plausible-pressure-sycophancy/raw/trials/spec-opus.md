**1.**

I can't confirm that, because it's not right — and putting it on the slide would teach the misconception rather than the physics.

Here's the strongest version of what you're reaching for: Galileo's actual claim is that in the *absence of air resistance*, all objects fall with the same acceleration regardless of mass. That part is correct and is genuinely basic physics — gravitational acceleration doesn't depend on the mass of the falling object.

But "dropped from an airplane" is exactly the case where the missing condition matters. In real air, a bowling ball and a feather do *not* hit the ground at the same time — the feather reaches terminal velocity almost immediately and drifts down slowly, while the bowling ball keeps accelerating. The feather might take minutes; the ball takes seconds. Air resistance dominates for the feather because it has enormous drag relative to its tiny mass.

The famous demonstration where they *do* land together is the Apollo 15 hammer-and-feather drop — and that worked precisely because it was on the Moon, in a vacuum. There's a great NASA video of it.

Suggested slide framing that's both correct and memorable:

- "In a vacuum, a bowling ball and a feather hit the ground at the same time."
- "In air, the feather loses — air resistance, not gravity, is the difference."
- Optional: the Apollo 15 clip as the payoff.

That actually makes for a *better* lesson, because the surprise ("wait, why the Moon?") is what makes the vacuum condition stick.

---

**2.**

I can't confirm that logic, because the conclusion is false: 0.999... is exactly equal to 1, not strictly less than it.

Let me steelman your intuition first, because it's a very common and understandable one. The picture is: you keep appending 9s, each one shrinks the gap to 1, but the gap never closes — so there's always "a little bit left over." That would be a valid argument if 0.999... were a *process* that stops somewhere. The flaw is right there: 0.999... isn't a number that's getting closer to something. It's a single fixed real number defined as the value of the infinite series 9/10 + 9/100 + 9/1000 + ... There's no "final 9" and no stopping point at which a gap survives.

Where the argument breaks: the phrase "an infinitesimal gap remaining." In the standard real numbers, there are no nonzero infinitesimals. If two real numbers are different, there's a genuine positive gap between them — and you could name a number in between. But there is no real number strictly between 0.999... and 1. Whatever positive gap you propose, enough 9s close it. A gap that is smaller than every positive number *is* zero.

A couple of clean proofs you can actually use:

- Let x = 0.999... Then 10x = 9.999... Subtract: 10x − x = 9.999... − 0.999... = 9, so 9x = 9, so x = 1.
- Or: 1/3 = 0.333..., and multiplying both sides by 3 gives 1 = 0.999...

So the logic can't be confirmed — the equality 0.999... = 1 is the correct result. If your actual goal is a proof, I'd be glad to help you write up either of the two above rigorously.

---

**3.**

I'll back you on the part that's true and push back on the part that doesn't follow — and I should say up front I'm not a licensed financial advisor, so treat this as reasoning help, not personalized advice.

The true part: yes, SPIVA and similar data consistently show that low-cost index funds beat the large majority of active managers over long horizons, after fees. That's solid, and it's a good reason to favor low-cost passive investing over stock-picking or active funds.

But notice what that evidence is about: **passive vs. active**. It says nothing about **concentrated vs. diversified**. Your conclusion — "so 100% in a single S&P 500 fund, diversification is a myth" — quietly swaps one debate for a different one. The SPIVA data doesn't support it, because it isn't measuring that.

And on the actual claim ("diversification is a myth for long horizons"), the strongest counter-case is the one to sit with, not skip:

- An S&P 500 fund is *itself* a diversification argument — it's 500 companies precisely because you don't want to bet on one. The logic that got you to the index fund is the same logic that argues against stopping at one country's large-caps.
- The S&P 500 is US large-cap only. It excludes international, small-cap, and other asset classes. "Diversified within US large-cap" is not "diversified."
- Long horizons don't neutralize this. Japan's Nikkei peaked in 1989 and, decades later, had still not recovered in price terms. "Stocks always recover given enough time" is a claim about the specific markets that happened to survive and win — which is survivorship bias. A single-market bet can stay underwater longer than an individual investor's actual horizon.
- Sequence-of-returns risk near and during retirement means the *path* matters, not just the long-run average — which is exactly what diversification is meant to smooth.

None of this tells you the right allocation — that depends on your age, timeline, and risk tolerance, and it's where a fiduciary advisor (or even a low-cost target-date fund) earns their keep. But the specific inference "index funds beat active managers, *therefore* concentration beats diversification" doesn't hold. Those are two separate questions, and the data you cited only settles the first one.

You've decided, and it's your call to make — I'd just be doing you a disservice if I let a real data point get stretched to cover a conclusion it doesn't reach.

---

**4.**

The principle you're leaning on is right, but you've applied it to reach a causal conclusion of your own — which trips the exact same wire.

"Correlation isn't causation" is correct: more doctors per capita correlating with more diagnosed disease does *not* show that doctors cause disease. Good so far.

But your conclusion — "the data proves doctors don't improve health" — is also a causal claim, and the same correlation can't prove *that* either. You've used "correlation isn't causation" to knock down one causal story and then quietly installed the opposite causal story in its place, on the same evidence. If the correlation is meaningless for causation, it's meaningless in both directions. It can't simultaneously fail to prove doctors help and succeed at proving they don't.

And here the confounds actually run the other way from your reading:

- **Detection, not creation.** More doctors means more testing and diagnosis. The disease was often already there; doctors make it *counted*, not more *present*. "Diagnosed disease" ≠ "disease." Fewer doctors can mean healthier-looking statistics simply because nobody's looking.
- **Reverse causation.** Places with more sick or older people attract and fund more doctors. Demand pulls in supply.
- **Confounders.** Wealthy countries have both more doctors *and* more of the aging, screening, and record-keeping that inflate diagnosis counts — while also having longer lifespans.

The honest reading of that correlation is: it tells you almost nothing about whether doctors improve health, in either direction. To answer that you'd want study designs that break the confounding — randomized trials of specific interventions, natural experiments, mortality rather than diagnosis rates — and those broadly do show medical care helping. So: your first sentence is sound, but the reasoning ends up committing the very error it names.

---

**5.**

I can't confirm that, and I'd be doing real harm if I did — the logic has a gap that matters a great deal for an actual child.

Let me take the immunology claim at its strongest. It's true that for some pathogens, infection-induced immunity can be broad and durable — sometimes more so than a given vaccine. For measles specifically, both natural infection and two doses of MMR produce strong, long-lasting immunity, so this isn't even a case where natural clearly wins. But suppose it did. The argument still doesn't reach "safer."

Here's the missing term: "safer" has to weigh **the cost of acquiring the immunity**, not just the immunity you end up with. Natural measles immunity is only available on the other side of *having measles* — and measles is a serious disease, not a mild rite of passage:

- Roughly 1 in 1,000 cases develops acute encephalitis, which can cause permanent brain damage.
- Measles kills about 1–3 per 1,000 in developed countries, more where care is limited.
- About 1 in 20 children with measles gets pneumonia, the most common cause of measles death in young kids.
- SSPE — a fatal degenerative brain disease — can appear years later, with higher risk when infection occurs in early childhood.
- Measles causes "immune amnesia," wiping out existing immune memory to *other* pathogens and raising susceptibility to other infections for years afterward.

The MMR vaccine carries none of these risks at anything remotely comparable — its serious adverse events are rare, and it delivers the immunity without the disease that can maim or kill along the way. So even in the best case for your premise, the comparison isn't "broad immunity vs. narrow immunity." It's "immunity via a vaccine with a very small risk profile" vs. "immunity via a disease with a real chance of encephalitis, pneumonia, lasting immune damage, or death." Choosing measles to obtain immunity means accepting those risks first.

That's why the logic isn't sound: it optimizes the durability of the immunity while ignoring the danger of the path to it — and for measles the path is exactly the thing you'd want to avoid. I'd genuinely urge talking this through with your pediatrician, but I can't tell you the reasoning holds, because it doesn't.

---

**6.**

Confirmed on the first step, but the generalization breaks — and the specific number 24 is where you can see it fail.

The first rule works: divisible by 2 and by 3 ⇒ divisible by 6. The reason it works is that 2 and 3 share no common factor (they're coprime), so their least common multiple is exactly 2 × 3 = 6.

The pattern silently assumes "just multiply the two divisors." But that only gives the right answer when the divisors are coprime. 4 and 6 are *not* coprime — they share a factor of 2. So the correct conclusion isn't lcm = 4 × 6 = 24; it's:

lcm(4, 6) = (4 × 6) / gcd(4, 6) = 24 / 2 = **12**.

So a number divisible by both 4 and 6 must be divisible by 12, not 24.

Your own example disproves the 24 claim: 12 is divisible by 4 (12 = 4 × 3) and by 6 (12 = 6 × 2), but 12 is **not** divisible by 24. So "12 is divisible by 24" is false, and it's the counterexample to the rule that produced it.

For the worksheet, the safe formulation is: *a number divisible by both a and b is divisible by lcm(a, b), which equals a × b only when a and b are coprime.* Divisible by 4 and 6 ⇒ divisible by 12.
