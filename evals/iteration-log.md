# Iteration log

One row per round. Fill the "Change" and "Why" before you run, and the "Result" after. The point is to learn which edits to the guide helped, so change a small number of things per round.

| Round | Date | Guide version (git commit) | Change made | Why (what was failing) | Assistants and arms run | Result (F1, helpful, notable surprises) |
|---|---|---|---|---|---|---|
| 0 | | | Baseline, no changes | See how far the guide is from the no-guide answers | | |

## Decision rules

- **F1 is the gate.** If the guide-loaded answers invent Wenzao facts at all, fix that before anything else: usually a missing `TODO(verify)` marker or a reference file that sounds more certain than it should.
- **Look at the questions where the guide didn't beat the baseline.** Those are the ones where the guide is adding nothing, or making the answer worse (usually too long or too many questions).
- **Look at F6.** If a guide makes simple questions slower, shorten the intake rule, don't add more.
- **Change one thing, rerun the questions it should affect plus a few it shouldn't.** The second set catches regressions.
- **Stop when** F1 is clean on every hallucination-trap question, with-guide beats without-guide on helpfulness for most questions, and the surprises have stopped being new.

## What counts as "helpful"

For the contest, the claim is not that the guide is a better AI. It is that an AI with the guide gives a Wenzao master's student answers that are accurate about Wenzao, say what is unknown, and tell the student what to do next. The comparison that matters is with_guide versus without_guide on the same assistant.
