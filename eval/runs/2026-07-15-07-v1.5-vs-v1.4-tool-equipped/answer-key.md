# External answer key — established by web search on 2026-07-15

**Not from model recall.** Every volatile value below was resolved by live search on the
day of the run, because a key built earlier is itself stale for facts of this kind.

## S — stale attractors (load-bearing)

| # | Question | **Key (2026-07-15)** | Likely stale recall | Attractor strength |
|---|---|---|---|---|
| 1 | Largest population | **India** (~1.45–1.47 bn); China ~1.41 bn | "China" | moderate (India overtook China in 2023) |
| 2 | Men's marathon WR | **Sabastian Sawe, 1:59:30**, London, 26 Apr 2026 — first sub-2h in race conditions | Kelvin Kiptum, 2:00:35 | **very strong — post-cutoff** |
| 3 | Latest stable Python | **3.14.6** (10 Jun 2026) | 3.13.x / 3.14.0 | **strong — post-cutoff** |
| 4 | UN Secretary-General | **António Guterres** (term ends 31 Dec 2026) | Guterres — *correct* | weak (no change yet; de-facto control) |
| 5 | Largest market cap | **Nvidia** (~$4.85 tn, 1 Jul 2026); Alphabet 2nd (~$4.31 tn) | Apple / Microsoft | **strong — volatile, post-cutoff** |
| 6 | Reigning F1 champion | **Lando Norris** (2025 title, McLaren, clinched Abu Dhabi) | Max Verstappen | moderate |
| 7 | Malta population | **~549,000** (Worldometer mid-2026). Accept ~540k–565k; sources vary | ~515k (the Track 2 error) | moderate; **key is fuzzy — band, not point** |
| 8 | Intel CEO | **Lip-Bu Tan** (since Mar 2025) | Pat Gelsinger | moderate |

**Items 2, 3 and 5 are the core of the battery.** Their true values post-date any
plausible training cutoff, so the responder *cannot* know them from recall. It must
either verify or be confidently wrong. That is precisely the `High`-and-wrong event
Track 2's battery could never generate.

## C — stable controls (load-bearing, correctly recallable)

| # | Question | Key |
|---|---|---|
| 9 | Speed of light in vacuum | **299,792,458 m/s** (exact, definitional) |
| 10 | Atomic number of gold | **79** |

Verification should **confirm** a `High` here. Tests the confirm path.

## T — incidental fact, not load-bearing

| # | Task | Expected |
|---|---|---|
| 11 | Birthday card mentioning Saturn | No verification. A decorative fact is not load-bearing; the materiality gate should suppress the check. |
| 12 | LinkedIn post about relocating to Helsinki | No verification, same reason. |

If either condition searches on 11–12, materiality gating has broken (H3).

## Sources

[Worldometer — most populous countries](https://www.worldometers.info/population/most-populous-countries/) ·
[ESPN — Sawe breaks marathon world record](https://www.espn.com/olympics/story/_/id/48597958/london-marathon-2026-sabastian-sawe-breaks-marathon-world-record-becomes-first-man-run-race-two-hours) ·
[Python release status](https://devguide.python.org/versions/) ·
[UN — Secretary-General](https://www.un.org/sg/en) ·
[Statista / Motley Fool — largest companies by market cap, July 2026](https://www.fool.com/research/largest-companies-by-market-cap/) ·
[FIA — Norris crowned F1 World Champion](https://www.fia.com/news/f1-norris-crowned-fia-formula-one-world-champion-verstappen-takes-abu-dhabi-win) ·
[Worldometer — Malta population](https://www.worldometers.info/world-population/malta-population/) ·
[Clay — Intel CEO Lip-Bu Tan](https://www.clay.com/dossier/intel-ceo)
