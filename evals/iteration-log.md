# Iteration log

One row per round. Fill the "Change" and "Why" before you run, and the "Result" after. The point is to learn which edits to the guide helped, so change a small number of things per round.

| Round | Date | Guide version (git commit) | Change made | Why (what was failing) | Assistants and arms run | Result (F1, helpful, notable surprises) |
|---|---|---|---|---|---|---|
| 0 | 2026-10-15 | `77dce42` (guide v1) | Baseline, no changes | See how far the guide is from the no-guide answers | Claude subagents, with and without the guide, 19 questions, web off | Guide 97% of checks, no guide 58%. The gain comes from Wenzao facts (calendar, GIES credits, DIA AI guidelines), Mandarin terms, and templates. Behavior checks (honesty, not inventing) mostly passed without the guide too. Guide over-asked: 4 to 5 intake questions on questions 6, 13, 18 |
| 1 | 2026-10-15 | uncommitted work after `ec10235` (guide v2) | Intake cut to one question and answer first; new `notices.md` and `weekly-notices-prompt.md`; calendar items only when relevant (max 3); DIA and GIES office contacts added | A first test by a Vietnamese master's student: five questions up front, a headline list she couldn't use, unrelated calendar items appended, and she said a LINE bot would be better | Claude subagents: v2, v1, and no guide on 25 questions (6 new: news, events, first hello, office phone, weekly check). Web allowed only on the three news and events questions | All 25: v2 94%, v1 79%, no guide 55%. Old questions 1-19: v2 94%, v1 95% (no regression). New questions 20-25: v2 94%, v1 42%, no guide 45%. First hello went from 151 words to 23. Open: question 6 still asks three questions; question 14 dropped the 2027-01-08 thesis deadline (the "max 3 items" rule); question 24 reply too long (116 words); checks on questions 19 and 20 were outdated or vacuous and were fixed afterward |
| 2 | 2026-10-15 | guide v3 (commit after `79e7dd8`) | Ask the department only when the answer depends on it; coaching asks at most two things per turn, first reply asks interests and languages; list the next three `dont_miss` items by date (max 5); simple lookups give just the thing plus one freshness line | Round 1 open items: question 6 asked three questions, question 14 dropped the 2027-01-08 thesis deadline, question 24 reply was 116 words | Claude subagents: v3 vs v2 on 10 questions (6, 14, 24 targeted; 1, 2, 3, 10, 13, 20, 22 as regression checks) | v3 43/48 (90%), v2 42/48 (88%). Fixed: 6 now asks two questions and no department first (4/5, was 3/5), 14 now includes the 2027-01-08 deadline (5/5, was 4/5), 24 shortened from 116 to 65 words. Not fixed or new: 6 never mentions past theses, 22 lists example topics (44 words), 24 still adds an address, an email fallback, and an offer, 20 shows about 7 items and doesn't state eligibility for headline-only items. Differences of one check are within noise at one run per question |

## Decision rules

- **F1 is the gate.** If the guide-loaded answers invent Wenzao facts at all, fix that before anything else: usually a missing `TODO(verify)` marker or a reference file that sounds more certain than it should.
- **Look at the questions where the guide didn't beat the baseline.** Those are the ones where the guide is adding nothing, or making the answer worse (usually too long or too many questions).
- **Look at F6.** If a guide makes simple questions slower, shorten the intake rule, don't add more.
- **Change one thing, rerun the questions it should affect plus a few it shouldn't.** The second set catches regressions.
- **Stop when** F1 is clean on every hallucination-trap question, with-guide beats without-guide on helpfulness for most questions, and the surprises have stopped being new.

## What counts as "helpful"

For the contest, the claim is not that the guide is a better AI. It is that an AI with the guide gives a Wenzao master's student answers that are accurate about Wenzao, say what is unknown, and tell the student what to do next. The comparison that matters is with_guide versus without_guide on the same assistant.
