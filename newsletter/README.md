# Prototype 4: events newsletter (preview only)

A static site that shows how a curated, multilingual events newsletter would work. No email is sent and no address is stored.

- **Pull:** browse and filter 46 upcoming events by topic, area and the language the event is given in; add one event, or the whole filtered list, to a calendar (.ics).
- **Push:** the same filters drive a live preview of the weekly digest and of the last-call reminder, in English, Vietnamese or Japanese.
- Settings live in the URL hash (the stand-in for a one-click preferences link) and nowhere else.

## Run

```bash
python3 -m http.server 8766 -d wenzao-masters-guide   # then open /newsletter/
```

## Data

| Source | Events | How |
|---|---|---|
| Wenzao announcement list (Prototype 3, `event-map/data/events.json`) | 31 | reused, then tagged and translated |
| National Taiwan University pages | 4 | `scripts/scrape.py` saves page text to `data/raw/`; fields read by hand |
| Academia Sinica (Institute of Economics seminars, Institute of Linguistics lectures and conferences) | 11 | same |

`scripts/build_events.py` merges everything into `data/events.json` (topic tags, delivery language, EN/VI/JA titles and summaries). Rebuild with `python3 newsletter/scripts/build_events.py`.

## Known limits

- Collected 15 and 17 Oct 2026; the preview treats 17 Oct as "today". Not independently verified.
- Vietnamese and Japanese text, topic tags and "inferred" language labels were written by Claude, not reviewed by native speakers.
- NTU's ELiD symposium page could not be opened, so only its title and date are known. Six Prototype 3 items without venue or date (PDF-only posts, competitions) are left out.
- Academia Sinica's institute list links for four Linguistics talks point to the institute home page, so the list page is linked instead.
- Coverage is two NTU-wide pages and two Academia Sinica institutes, not every department.
