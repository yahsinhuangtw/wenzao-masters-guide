# Scoring rubric

Used for the hand-scored comparison across assistants (see `README.md`). For each answer, score each item 1 (yes), 0 (no), or leave blank when it doesn't apply. Specific checks for each question are in `evals.json` under `expectations`.

| Item | Question | Why it matters |
|---|---|---|
| F1 | No invented Wenzao facts. Any Wenzao-specific rule, date, contact, or number is either in the guide or marked as unknown | The guide exists to prevent confident wrong answers |
| F2 | Gives a source and says how fresh or unverified it is | Students need to know what to trust |
| F3 | Asks for today's date or the semester, or states its assumption, before saying what is "coming up" | Dates are only useful if the assistant knows the date |
| F4 | Gives the Mandarin for rules, forms, offices, or key terms the student may need to show someone | The student can't read the originals |
| F5 | Says who to ask when it doesn't know | An honest "I don't know" is useful if it points somewhere |
| F6 | The answer is proportionate: no unnecessary interrogation, no wall of text | Over-asking is the main way a guide becomes annoying |

## Helpfulness (1 to 5)

Score as the student would feel after reading it.

| Score | Meaning |
|---|---|
| 1 | Wrong, misleading, or useless |
| 2 | Partly useful but with a serious problem, such as an invented fact |
| 3 | Okay: correct but generic, or correct but hard to act on |
| 4 | Good: correct, clear, and the student knows what to do next |
| 5 | Excellent: correct, clear, proportionate, and anticipates the next problem |

## Notes for scorers

- Score the answer, not your guess about the assistant. Don't look at the arm column while scoring if you can avoid it. Shuffle the rows or have someone else hide it.
- F1 is the key number. A confident wrong fact about a Wenzao deadline is worse than an honest "I don't know".
- If an answer is long, don't give credit for items that are buried and hard to find.
- Write short notes on surprises. They are what you will use to improve the guide.
