# Normalization rules (protocol step 6)

Applied to **every** response in **both** arms, identically and independently. The
normalizer never compares two responses to each other and is never told which arm a
response came from.

1. **Delete explicit confidence labels.** "Confidence: High", "(Moderate)", "I'm highly
   confident that…" → delete the label, keep the substantive claim it was attached to.
2. **Delete section headers and structural scaffolding.** "**Steelman:**", "**The direct
   answer:**", "**What I'd push back on:**", numbered analysis frames → keep the prose,
   merge into plain paragraphs.
3. **Delete method meta-commentary.** "Let me steelman your position first", "Before the
   case-specific estimate I'll name the reference class" → delete the announcement, keep
   whatever substantive content followed it.
4. **Change nothing else.** No claim, number, recommendation, hedge, or caveat may be
   added, removed, softened, sharpened, reordered, or shortened. Do not improve the answer.
   Do not make two answers more alike in content.
5. **Output shell:** plain prose and plain bullets. No headers, no bold labels, no
   confidence markers.

**What this does not fix** (stated in the protocol and restated here): a long hedged answer
still reads differently from a short direct one after the tells are gone. Normalization
weakens register leakage; it does not close it.
