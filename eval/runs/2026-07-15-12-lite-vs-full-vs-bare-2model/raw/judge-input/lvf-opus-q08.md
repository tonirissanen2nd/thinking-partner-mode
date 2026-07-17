# Question

Is nuclear power safer than solar, yes or no?

---

# Answer 1

No — but the "no" is doing far less work than a yes/no implies.

On the standard metric — deaths per terawatt-hour over the full lifecycle (mining, construction, operation, accidents) — the widely cited compilation (Our World in Data, built on Markandya & Wilkinson and successors) puts nuclear at roughly 0.03 and solar at roughly 0.02 deaths/TWh, with wind ~0.04, gas ~2.8, coal ~25. So solar edges nuclear, and the literal answer is no.

The two figures sit inside each other's noise and rest on incommensurable accounting — nuclear's number is dominated by which Chernobyl mortality estimate you accept (a few thousand attributable vs. tens of thousands under linear-no-threshold extrapolation), solar's by rooftop-installation falls, which scale with the rooftop share of deployment and are inconsistently counted. A different but equally defensible methodology flips the sign.

Both are within an order of magnitude of each other and 100–1000× safer than coal. The most pessimistic Chernobyl toll would move nuclear up perhaps 10×, and it still lands far below fossil. Verify against Our World in Data's "Death rates per unit of electricity production" before quoting them.

The two technologies have different shapes of risk, not just different means:

- Solar's deaths are diffuse, frequent, and small — falls, manufacturing, mining. Thin-tailed, bounded, no correlated catastrophe. No solar failure makes a region uninhabitable.
- Nuclear's are rare, correlated, and carry a tail: severe accident with land contamination and mass displacement. Fukushima's direct radiation deaths are near zero, but the evacuation itself killed on the order of a thousand people (mostly elderly, from displacement) and moved ~150,000 — a category of harm the deaths/TWh metric does not price at all.

That tail is non-estimable, not merely low-probability: roughly three major accidents in ~20,000 reactor-years is a reference class too thin to contain the tail, and reactor designs, siting density, and regulatory regimes aren't exchangeable across it. I won't give you a point probability on it, because a point estimate would imply a precision the data cannot support. The right question there isn't "what's the number" but "what exposure am I taking" — a reactor upwind of a dense metro is a different bet from the same reactor on a sparse coast, at the same deaths/TWh.

If you're optimizing expected mortality per unit energy, they tie. If you're optimizing for bounded downside, solar wins by construction. Those are different objectives and the metric hides the difference.

It's per-TWh, not per-system. Solar needs storage or firm backup; if that backup is gas, the system's safety figure is much worse than the panel's, and that comparison — not panel-vs-reactor — is usually the real decision. Also outside scope: waste, proliferation, land use, and the fact that nuclear's forward-looking number depends on the accident rates of designs that mostly haven't been built at scale.

A single-methodology lifecycle mortality study covering both, with consistent treatment of installation falls and a stated Chernobyl attribution rule.

---

# Answer 2

By the numbers that dominate the debate — deaths per unit of energy produced — they're roughly in the same tier, and nuclear is often ranked as slightly *safer* than solar, not more dangerous. So the reflexive "no" is wrong. But the honest answer is that yes/no flattens something that actually matters.

The standard comparison is deaths per terawatt-hour, folding in the whole lifecycle (mining, construction, operation, accidents, pollution). On that metric:

- Nuclear comes out very low — on the order of ~0.03 deaths/TWh in commonly cited figures (Our World in Data / Markandya & Wilkinson lineage). This *includes* estimated deaths from Chernobyl and Fukushima.
- Solar is also very low — roughly ~0.02 deaths/TWh, mostly from installation falls (rooftop work) and some manufacturing.

Treat those specific numbers as approximately right but worth checking — they come from a well-known body of analysis, but the exact figures shift depending on which accident death tolls and manufacturing assumptions an author uses, and Chernobyl's long-tail death estimate especially is genuinely contested. The robust conclusion, though, isn't fragile: both are one to two *orders of magnitude* safer than coal, oil, and gas, and they sit close to each other.

So which is "safer" depends on what you're actually asking:

- Essentially tied, nuclear often nudging ahead. This is where the "actually, nuclear is safer" talking point comes from, and it's defensible.
- Different in *kind*. Solar's harm is diffuse and routine (someone falls off a roof). Nuclear's is rare-but-correlated — a catastrophic tail event that's very unlikely per year but large when it happens, plus long-lived waste. Some people rationally weight a small chance of a big, dread-inducing accident more heavily than the same expected value spread out as everyday accidents. That's a values judgment about risk, not an error.

If your underlying question is "which should we build more of," safety-per-TWh barely separates them, and the decision turns on other things — cost, build time, grid intermittency, siting, waste, weapons proliferation — where they differ far more than on safety.

If forced to one word, "yes" is more defensible than "no" on the expected-harm metric. But the two are close enough that the interesting disagreement isn't about safety at all.
