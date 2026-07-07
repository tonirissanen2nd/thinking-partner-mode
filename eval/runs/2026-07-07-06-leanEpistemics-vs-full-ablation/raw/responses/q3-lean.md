The number depends entirely on what "significantly worse" means, so let me pin that first, then forecast.

**Resolution criterion I'll use:** a single pandemic between 2026 and 2046 causing **≥3× COVID-19's global excess mortality**. COVID's excess deaths are ~20 million (WHO put 2020–21 alone at ~14.8M; the Economist's through-2022 central estimate is ~18–27M), so the threshold is roughly **≥60 million excess deaths**. I'll flag where a different definition (higher case-fatality rate rather than total deaths, or economic/societal disruption) would move the answer.

## Outside view first

The best reference-class anchor is Marani et al. (2021, PNAS), which fit four centuries of epidemics to a generalized Pareto distribution with a **slowly decaying power-law tail** (intensity exponent ≈ −0.71). Two things matter from it:

1. Original headline: a COVID-scale-or-greater event has ~2%/year probability. **Important caveat:** the authors issued a 2023 correction — the code double-counted events across adjacent years, inflating probabilities and shortening recurrence intervals — so the true figure is **lower** than 2%/year. I can't recall the exact corrected value (Moderate confidence on the direction, Low on the magnitude of the revision).
2. The heavy tail means "much worse than COVID" is *not* dramatically rarer than COVID itself — the whole point of a slowly decaying tail is that large events aren't suppressed the way a thin-tailed (normal/exponential) model would predict.

## Decomposition

I'll split the hazard into three roughly independent channels, because they have very different estimability:

**1. Natural zoonotic spillover.** This is the estimable channel. Taking a corrected COVID-or-worse base rate of ~1%/year, and discounting modestly for the higher "≥3× COVID" bar (the fat tail keeps this discount small), I get ~0.5–1%/year. Over 20 years: 1 − (1 − 0.0075)²⁰ ≈ **~10–15%**. One real offset pulls this down: countermeasures have genuinely improved (mRNA platforms, genomic surveillance, compressed vaccine timelines), so a given pathogen kills fewer people now than the same pathogen would have in 1918 or 2020. That offset is weakest exactly where it matters most — a pathogen that is both highly transmissible and highly lethal, or one that spreads faster than countermeasures can be fielded. Confidence: **Moderate.**

**2. Laboratory accident.** Diffusion of high-consequence research and gain-of-function-adjacent work adds a non-trivial increment over a 20-year horizon. Poorly quantified; I'd treat it as adding low-single-digit percentage points, **Low confidence.**

**3. Deliberately engineered pathogen.** This is where a point estimate misleads, and I'll say so rather than fake precision. It is **genuinely fat-tailed and the reference class cannot contain it** — the historical record has no instance of a synthesized pathogen optimized past natural constraints on transmissibility/lethality, so there is no base rate to extrapolate. Advancing synthetic biology plus AI-assisted design raise the *ceiling* of what's possible over 20 years, and this channel dominates the extreme upper tail (an engineered agent can breach the natural trade-off between transmissibility and case-fatality that caps most zoonoses). I mark this component **non-estimable as a point probability.** The honest move here is to shift from "what's the number" to **exposure**: the mitigations that would make the forecast irrelevant are DNA-synthesis screening, lab-safety governance, and broad-spectrum medical countermeasures/surveillance — how fast those scale relative to capability diffusion is the actual lever, and it's more actionable than the probability.

## Combined forecast

Aggregating the estimable channels and adding a bounded allowance for the anthropogenic tail:

**~20% probability (plausible range 10–30%) that a pandemic causing ≥3× COVID-19's global excess mortality occurs between 2026 and 2046.** Confidence: **Low-to-Moderate** — Moderate on the natural component, Low on the total, because the upper tail is driven by the non-estimable engineered-pathogen channel, and the sign of the net trend is contested (countermeasures improving vs. spillover frequency and bio-capability both rising). The Marani result argues the increasing-risk direction; the correction and countermeasure gains argue the other way.

## What this answer leaves out (material omissions)

- **Definition sensitivity is the biggest driver.** If "worse" means *higher CFR* (e.g., a moderately transmissible pathogen at 10–30% lethality) rather than higher total deaths, the relevant probability and the risk profile change substantially. If it means economic/societal disruption, a less-deadly but more disruptive event could qualify and the number rises.
- **Single event vs. cumulative.** I estimated the probability of *at least one* qualifying pandemic, not the expected count.
- **Correlation across channels** (e.g., a natural outbreak that reveals or accelerates a capability) is ignored; the channels aren't perfectly independent.
- I have not independently reconstructed the corrected Marani figures — the base rate carries that uncertainty.

Sources:
- [Marani et al., "Intensity and frequency of extreme novel epidemics," PNAS 2021](https://www.pnas.org/doi/10.1073/pnas.2105482118)
- [Correction to Marani et al., PNAS 2023](https://www.pnas.org/doi/10.1073/pnas.2302169120)
- [WHO, global excess deaths associated with COVID-19](https://www.who.int/news-room/questions-and-answers/item/global-excess-deaths-associated-with-the-COVID-19-pandemic)
- [Our World in Data, excess mortality during COVID-19](https://ourworldindata.org/excess-mortality-covid)
