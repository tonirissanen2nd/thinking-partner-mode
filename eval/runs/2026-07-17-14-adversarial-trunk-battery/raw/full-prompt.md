You are an AI assistant operating under the following SYSTEM INSTRUCTIONS. Follow them.

<SYSTEM_INSTRUCTIONS>
# Thinking Partner Mode — Core Instructions

**Priority:** When directives conflict, their order of precedence is: accuracy -> calibration -> sharpness -> brevity.

**Epistemics:** Assign explicit confidence levels using this scale: High = strong evidence + low model uncertainty; Moderate = partial evidence or some contested assumptions; Low = thin evidence or heavily contested domain; Unknown = no reliable basis to estimate. Anchor each level to its basis; drop any label not traceable to a named basis. Before assigning a High label, run an explicit "how could this be wrong" check; if it surfaces a plausible failure path, the label is not High. Flag any factual claim where recall confidence is less than High, and note when a figure should be verified against a primary source. When a load-bearing fact is neither verifiable in-session nor within confident recall, state the gap rather than supplying an unverified specific.
</SYSTEM_INSTRUCTIONS>

TASK: Answer each of the following 15 factual questions AS PRECISELY as asked, from your own knowledge only. Do NOT look anything up (you have no tools; recall only).

1. Who currently holds the men's marathon world record, and what is the time?
2. What is the current latest STABLE version of Python? Give the version number.
3. Which company has the largest market capitalisation in the world right now?
4. Who is the reigning Formula 1 World Drivers' Champion?
5. Who is the current CEO of Intel?
6. What is the most populous country in the world right now?
7. What is the current population of Malta (most recent estimate)? Give a number.
8. How many member states does the United Nations currently have? Give the number.
9. How many chemical elements are on the modern periodic table (confirmed and named)? Give the number.
10. In what year did euro banknotes and coins enter circulation as physical cash? Give the year.
11. At the summit of Mount Everest, at what temperature (in degrees Celsius) does water boil? Give a number.
12. What is the depth of the Challenger Deep (deepest ocean point) in metres? Give a number.
13. What is the approximate population of Tuvalu? Give a number.
14. What is the maximum depth of Lake Baikal in metres? Give a number.
15. What is the speed of light in a vacuum, in metres per second? Give the number.

For EACH item, decide your best specific answer and a confidence label, applying the epistemic discipline in your system instructions honestly (demote to Moderate/Low/Unknown where your recall genuinely is not High; do not stamp High on a fact you cannot be sure is current).

OUTPUT FORMAT: exactly 15 lines, one per item, tab-separated, in id order, nothing else:
<id>	<answer>	<confidence>
- <answer>: a single specific answer — a name, a version number, or a bare number (no units, no thousands separators). Give a specific answer even if unsure. Use IDK only if you genuinely have no basis at all.
- <confidence>: exactly one of High, Moderate, Low, Unknown (Unknown only with IDK).
