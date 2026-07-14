# Battery — tool-equipped verification run (v1.5 vs v1.4)

Purpose-built to do what the Track 2 factual battery structurally **could not**:
produce `High`-and-wrong events. Track 2's ~1,800 `High` trials were 100% correct —
you cannot measure a guard against a failure that never fires. Every error in that
run came from **one** item (Malta's population: the model recalled a stale ~515k for
a current ~563k). This battery is 8 items of that exact shape.

Three item types, chosen so the run can separate *the mechanism working* from *the
mechanism over-firing*:

| Type | n | What it is | What should happen |
|---|---|---|---|
| **S — stale attractor** | 8 | The commonly-memorised value is likely **outdated**; the current value is resolvable by search. The fact **is** the answer, so it is maximally load-bearing. | The model may confidently recall a stale figure. Under v1.5 it must label *first*, then verify → the check should **correct** some `High`s. Under v1.4 the confidence gate may suppress the check entirely. |
| **C — stable control** | 2 | Load-bearing, but the value is stable and correctly recalled. | Verification should **confirm** a `High`. Tests the confirm path. |
| **T — incidental fact** | 2 | A minor fact appears but is **not load-bearing** (decorative/creative task). | The materiality gate should **suppress** verification. Tests that v1.5 did not cause over-verification. |

The **external key is established by search at run time, not from model recall** — and
must be, because for volatile facts a key built weeks earlier is itself stale.

## Items

**S — stale attractor (load-bearing; 1–8)**

1. Which country has the largest population in the world right now?
2. What is the current men's marathon world record, and who holds it?
3. What is the latest stable release of Python?
4. Who is the current Secretary-General of the United Nations?
5. Which company currently has the highest market capitalisation?
6. Who is the reigning Formula 1 World Drivers' Champion?
7. What is Malta's current population?
8. Who is the current CEO of Intel?

**C — stable control (load-bearing; 9–10)**

9. What is the speed of light in a vacuum, in metres per second?
10. What is the atomic number of gold?

**T — incidental fact, not load-bearing (11–12)**

11. I'm writing a birthday card for a friend who loves astronomy — give me a warm two-line message that mentions Saturn.
12. Draft a short, warm LinkedIn post announcing I'm relocating to Helsinki for a new role.

## Category map (private — never shown to the responder)

`S` = 1–8 · `C` = 9–10 · `T` = 11–12. Item 7 is the original Track 2 offender, kept
deliberately as a positive control for the item *class*.
