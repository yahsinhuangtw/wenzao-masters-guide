# Research and library access

Status of this file: the known-issues entry comes from one master's student's experience and has not been tested again. The general explanation of institutional access is general knowledge, not Wenzao-verified. The library description comes from the project proposal, which cites official university pages.

## Known issues

Add new entries at the end. Never delete an entry without noting why.

| ID | System | What happens | Likely cause (a guess) | What to try | Status | Last checked |
|---|---|---|---|---|---|---|
| KI-001 | JSTOR | Opening JSTOR directly fails. Opening it through the library's proxy link lets you in, but the page still shows a "Log in" button, so you can't tell whether you are in. | JSTOR doesn't know you belong to the university unless you arrive through the library. The "Log in" button is probably JSTOR's personal-account login, not the university's. | Go to the library website, find JSTOR in the database list, and open it from there. Then try opening and downloading a full-text article that is not marked free. If it opens, you are in. | Reported by a master's student. Steps `TODO(verify)`: exact library path, which credentials, and whether the "Log in" button explanation is right | not yet checked |

Entry template:

```
| KI-00N | System name | What the student sees | Best guess at the cause | Steps that work | Who reported it, and whether steps were tested | date |
```

If the library's own login instructions are outdated, say so plainly ("the official instructions may be out of date") and give the contact (`TODO(verify)`: library help contact).

## How institutional access works (general)

This is general knowledge about academic databases and is not specific to Wenzao.

- A university pays for access. Publishers recognize you either by the campus network or by a login that goes through the library.
- If you visit the publisher's site directly from home, it may not know you are a student, so it blocks you. Going through the library's link (often a proxy) is what proves you belong.
- Many sites keep showing their own "Log in" or "Sign in" button even when you have institutional access, because that button is for a personal account. The reliable test is whether you can open or download full text.
- If you are asked for a personal account or a payment, you probably did not arrive through the library. Close the tab and start again from the library site.

Students from other countries may expect a different login system. Say that it is normal for it to feel confusing.

## Wenzao library (from the project proposal, to verify)

- Physical holdings across seven floors, with foreign-language collections in English, Japanese, French, German, Spanish, and Vietnamese, and specialized collections such as the English Foundation Collection.
- Digital platforms including iVideo, Vision Media, and BBC audio-visual learning portals. These suit language learning more than thesis research.
- Library site: https://lib.wzu.edu.tw/ (linked from the school's news site on 2026-10-15, not opened by us yet).
- `TODO(verify)`: the list of research databases, the proxy or login method, opening hours, interlibrary loan, how to ask a librarian, and the contact.

## Finding literature for a thesis

1. Start from the topic worksheet's keywords, in the languages the student can read.
2. Use the library's database list to find the databases that cover the field (`TODO(verify)`: which databases the library offers).
3. Look at the department's past theses for their reference lists, they show which sources your supervisors consider standard.
4. Keep every source in a citation manager from day one (Zotero is free), and write down where you got it.
5. If you can't get a paper, ask the library about interlibrary loan before paying for it (`TODO(verify)`: whether the library offers it).

## What the agent should do

- If a login problem is described, check the known-issues table first and say whether the entry is tested.
- If it isn't in the table, give the general explanation, then tell the student to contact the library and offer to note the problem as a new known issue.
- Never ask for or store a student's password.
