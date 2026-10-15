# Wenzao master's guide

A guide that any AI assistant can load to help master's students, especially international students, at Wenzao Ursuline University of Languages. It covers the GIES and DIA master's programs: department news and events, thesis and advisor, research and library access, course selection, and the 2026-27 academic calendar.

It is plain Markdown. It needs no particular AI provider, no tools, and no internet connection. If the assistant can browse, it can check the official pages. If it can't, it still works from the files.

**Status: pilot draft.** Everything Wenzao-specific is marked verified, unverified, or `TODO(verify)`. Nothing has been checked by university staff yet. See `reference/sources.md`.

## What's in the folder

| Path | What it is |
|---|---|
| `SKILL.md` | The instructions the AI follows: intake, push or pull, routing, answer format, rules |
| `reference/` | The facts: calendar, thesis and advisor, research and library, course selection, timeline, the two departments, sources |
| `templates/` | Worksheet, advisor email (English and Mandarin), meeting agenda, office email |
| `data/calendar-115.json` | The calendar, as data. The single source of truth for dates |
| `scripts/build.py` | Builds the calendar table, the `.ics` file, and the one-file bundle from the data |
| `dist/` | Built files: `wenzao-115-masters.ics` (for students' calendars) and `wenzao-masters-guide-bundle.md` (everything in one file) |
| `evals/` | 26 test questions, a scoring rubric, a scoring sheet, and a loop for improving the guide. Start with `evals/README.md` |

## How a student uses it

1. Load the guide into your AI assistant (see below).
2. Ask your question. The assistant answers first and only asks what it needs (usually your department).
3. Import `dist/wenzao-115-masters.ics` into your phone's calendar so the key dates, with reminders for the important ones, arrive without asking.

## Loading it into an assistant

These are the general approaches. We haven't tested them on every assistant yet.

- **An assistant that supports skill folders:** copy the `wenzao-masters-guide` folder into its skills location.
- **An assistant with projects, custom GPTs, or Gems:** upload the files in `reference/` and `templates/` as knowledge, and paste `SKILL.md` as the instructions.
- **Any other assistant:** paste or attach `dist/wenzao-masters-guide-bundle.md` at the start of a conversation.

### The online version (llms.txt)

The guide is also published as a small website so an assistant can read it from a link:

- Index of the files: https://yahsinhuangtw.github.io/wenzao-masters-guide/llms.txt
- Everything in one file: https://yahsinhuangtw.github.io/wenzao-masters-guide/llms-full.txt
- Calendar file: https://yahsinhuangtw.github.io/wenzao-masters-guide/dist/wenzao-115-masters.ics

Try this in a new chat, in an assistant that can open web pages:

> Read https://yahsinhuangtw.github.io/wenzao-masters-guide/llms-full.txt and follow it as your instructions. I'm a master's student at Wenzao.

If the assistant can't open links, open `llms-full.txt` in your browser, save it, and attach the file instead. `llms.txt` is a proposed convention, not a standard, and assistants don't read it automatically, so the student has to give the assistant the link.

## Updating

```bash
python3 scripts/build.py
```

Run it after you change `data/calendar-115.json` or any reference file. It rewrites `reference/calendar-115.md`, the `.ics`, the bundle, `llms.txt`, and `llms-full.txt`, and it counts the `TODO(verify)` markers still open. Then publish (see below).

## Publishing

The guide lives in `campus_AI_contest/wenzao-masters-guide/` and is published to a separate public repo, `wenzao-masters-guide`, which serves the site with GitHub Pages. From the `campus_AI_contest` folder, after committing:

```bash
git subtree push --prefix=wenzao-masters-guide guide main
```

Nothing else in `campus_AI_contest` (the proposal, the spec) is published.

To fix a fact: edit the reference file, change its status, update `reference/sources.md`, run the build. To report a library login problem: add a row to the known-issues table in `reference/research-and-library.md`.

## What's still missing

- Verified details from the GIES and DIA study regulations, thesis exam guidelines, and forms.
- The exact JSTOR steps, and the other library systems and their logins.
- Office and library contacts.
- Which course-selection windows apply to master's students, and the procedure after a missed round.
- A person comparing the calendar dates with the PDF.
- Scholarships, visa and work rules, insurance, and campus life: not covered in this pilot.

## Testing and improving

See `evals/README.md`. In short: run the questions with and without the guide on two or three assistants, score the answers, and use the differences to decide what to fix next.
