# Sources and verification

Every Wenzao-specific fact in this guide should trace to a line below. "Checked" says how the source was read. Nothing here has been checked by university staff.

| Source | What it supports | Checked how | Date | Status |
|---|---|---|---|---|
| `schday_c_115.pdf`, 115 academic year daytime-division calendar (approved 2026-05-21) | `calendar-115.md`, the calendar file | Text extracted from the PDF by a script, not compared with the printed grid | 2026-10-14 | Needs a person to compare 5 to 10 dates with the PDF |
| GIES curriculum design page, https://c052.wzu.edu.tw/category/149868 | GIES graduation requirements, site structure | Page summary | 2026-10-14 | Needs a person to read it |
| DIA regulations page, https://c030.wzu.edu.tw/category/143040 | DIA site structure, link list | Page summary | 2026-10-14 | Needs a person to read it |
| DIA homepage, https://c030.wzu.edu.tw/ | DIA announcement lists, office contact | Page summary | 2026-10-15 | Needs a person to read it |
| GIES homepage, https://c052.wzu.edu.tw/ | GIES news lists, office contact | Page summary | 2026-10-15 | Needs a person to read it |
| Registration Section site, https://d001.wzu.edu.tw/ | Registration news list address | Page summary | 2026-10-15 | Needs a person to read it |
| School-wide news list, https://a001.wzu.edu.tw/list/147031 | School-wide announcement list and related links | Page summary | 2026-10-15 | Needs a person to read it |
| Project proposal draft (`proposal.md`) | Library description | Proposal text, which cites official university pages | 2026-10-14 | Needs a check against the library site |
| A GIES master's student's experience | Advisor choice at GIES, the missed selection round, the JSTOR login issue | Told to the team | 2026-10-14 | Needs a second student, and the JSTOR steps tested |

## Rules for updating

- When you verify a fact, change its status in the file and the row here, and put the date and your initials.
- When you add a fact, add a row here at the same time.
- If a source changes, search the guide for the old fact and fix every place.
- Every few months (or at the start of a semester) re-read the calendar and the department pages, and run `python3 scripts/build.py` again if the dates change.
