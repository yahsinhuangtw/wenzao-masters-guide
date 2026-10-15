# Evaluating the guide

How to tell whether `SKILL.md` and the reference files actually help, and how to improve them in rounds.

The question is simple: **does an AI give better answers to a Wenzao master's student with the guide than without it?** Better means accurate about Wenzao, honest about what it doesn't know, and clear about what to do next.

## The pieces

| File | What it is |
|---|---|
| `evals.json` | 25 realistic student questions, each with specific checks. The single source of truth |
| `rubric.md` | The six-item score (F1 to F6) and a 1 to 5 helpfulness score |
| `make_sheet.py` | Builds `questions.md` (readable list) and `run-sheet.csv` (blank scoring sheet) from `evals.json` |
| `summarize_scores.py` | Turns a scored sheet into with-guide versus without-guide numbers |
| `iteration-log.md` | What you changed each round, why, and what happened |

Three of the questions are traps: the right answer is "I don't have that" (DIA credits, library hours, office email). A no-guide assistant tends to answer confidently anyway. Those are the questions that show the difference most clearly.

## Two ways to run a round

### A. Automated, with Claude subagents (fast, Claude only)

The skill-creator tool in Claude can run every question twice, once with the guide and once without, grade each answer against the specific checks, and show the results in a review page. This is quick but it only tests Claude, and the same model that wrote the guide is also running it, so it's a sanity check, not proof.

Layout it expects: a folder `wenzao-masters-guide-workspace/` next to the guide, with one folder per round (`iteration-1/`, `iteration-2/`), and in each one folder per question with `with_skill/` and `without_skill/` subfolders.

### B. By hand, on any assistant (slower, provider-neutral)

This is the version that supports the claim "works with any AI".

1. Generate the sheet:
   ```bash
   python3 evals/make_sheet.py --assistants "Claude,ChatGPT,Gemini" --shuffle-seed 1
   ```
   The shuffle mixes the rows, so you are less likely to notice which are the with-guide ones.
2. For each row, open a fresh conversation in that assistant.
   - **with_guide:** load the guide first (see `../README.md`: skill folder, project files, or the one-file bundle in `dist/`).
   - **without_guide:** nothing loaded.
   Paste the question from `questions.md` and save the answer.
3. Score each answer with `rubric.md` in `run-sheet.csv`. Better: have someone who didn't write the guide do the scoring, and don't tell them which arm is which.
4. Summarize:
   ```bash
   python3 evals/summarize_scores.py evals/run-sheet.csv
   ```
   It prints each item's rate for each assistant and arm, the difference, and F1 on the trap questions.

A full pass is 25 questions x 2 arms x 3 assistants = 150 answers. For a first round, run 2 assistants, or run the 8 questions flagged below, and expand if it looks promising.

**A good first subset (8 questions):** 1, 3, 4, 7, 10, 11, 15, 19. It covers the calendar, the thesis, the library, a boundary, a verified fact, and three traps.

## The loop

1. **Baseline.** Run a round on the current guide. Record it as round 0 in `iteration-log.md`.
2. **Read the failures.** Start with F1 failures, then the questions where the guide didn't beat the baseline, then F6.
3. **Change a little.** Edit `SKILL.md` or a reference file. Fix the cause (a missing unverified marker, a rule that is too heavy), not the symptom.
4. **Rebuild.** Run `python3 scripts/build.py`, so the bundle and calendar reflect the change.
5. **Rerun** the questions the change should affect and a few it shouldn't.
6. **Log it** and commit, so each round matches a git commit.
7. **Repeat** until F1 is clean on every trap question, the guide beats no-guide on helpfulness for most questions, and the surprises have stopped being new.

## When to add questions

The 25 questions are written by the team. Before the contest, replace some with real ones: ask 5 to 10 international master's students what they asked their AI (or would have), and use those words. Also add a question every time a real student's question exposes a gap.

## Limits to be honest about

- The questions are written by people who know the guide, so they are easier than real ones.
- Facts in the guide are still unverified, so "accurate" means "consistent with the guide", not "confirmed by the university". Verify the facts before claiming accuracy.
- Scores by the author are biased. Use an outside scorer for anything you will report.
- Assistants change. Record the model and date next to each result.
