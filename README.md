# Wenzao master's guide

A guide that any AI assistant can load to help master's students, especially international students, at Wenzao Ursuline University of Languages. It covers the GIES and DIA master's programs: thesis and advisor, research and library access, course selection, and the 2026-27 academic calendar.

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
| `tests/test-questions.md` | 17 questions to test the guide and compare AI assistants |

## How a student uses it

1. Load the guide into your AI assistant (see below).
2. Ask your question. The assistant first asks a few questions about you (department, semester, today's date, Mandarin level, what you need).
3. Import `dist/wenzao-115-masters.ics` into your phone's calendar so the key dates, with reminders for the important ones, arrive without asking.

## Loading it into an assistant

These are the general approaches. We haven't tested them on every assistant yet.

- **An assistant that supports skill folders:** copy the `wenzao-masters-guide` folder into its skills location.
- **An assistant with projects, custom GPTs, or Gems:** upload the files in `reference/` and `templates/` as knowledge, and paste `SKILL.md` as the instructions.
- **Any other assistant:** paste or attach `dist/wenzao-masters-guide-bundle.md` at the start of a conversation.

## Updating

```bash
python3 scripts/build.py
```

Run it after you change `data/calendar-115.json` or any reference file. It rewrites `reference/calendar-115.md`, the `.ics`, and the bundle, and it counts the `TODO(verify)` markers still open.

To fix a fact: edit the reference file, change its status, update `reference/sources.md`, run the build. To report a library login problem: add a row to the known-issues table in `reference/research-and-library.md`.

## What's still missing

- Verified details from the GIES and DIA study regulations, thesis exam guidelines, and forms.
- The exact JSTOR steps, and the other library systems and their logins.
- Office and library contacts.
- Which course-selection windows apply to master's students, and the procedure after a missed round.
- A person comparing the calendar dates with the PDF.
- Scholarships, visa and work rules, insurance, and campus life: not covered in this pilot.

## Testing

Run the questions in `tests/test-questions.md` with and without the guide on two or three different assistants, and record the results in the table at the bottom of that file.
