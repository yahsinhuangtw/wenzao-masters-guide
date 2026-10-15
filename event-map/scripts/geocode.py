#!/usr/bin/env python3
"""Geocode data/events.source.json -> data/events.json (Nominatim, cached, 1 req/s)."""
import json, re, time, urllib.parse, urllib.request, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "events.source.json"
OUT = ROOT / "data" / "events.json"
CACHE = ROOT / "data" / "geocode-cache.json"
UA = "wenzao-event-map-prototype (student project)"
BBOX = (21.8, 25.4, 119.3, 122.1)  # lat_min, lat_max, lon_min, lon_max


def norm(s):
    return (s or "").replace("台", "臺")


def name_ok(q, hit):
    """Reject fuzzy matches: the hit's own name must contain the query's name (addresses are exempt)."""
    if any(ch.isdigit() for ch in q) or not re.search(r"[\u4e00-\u9fff]", q):
        return True
    first = norm(hit["display_name"].split(",")[0])
    core = norm(q.split()[0]).replace("國立", "")
    return core in first or first in norm(q)


def lookup(q, cache):
    if q in cache:
        return cache[q]
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "format": "json", "limit": 1, "countrycodes": "tw", "accept-language": "zh-TW"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        res = json.load(r)
    time.sleep(1.1)
    cache[q] = res[0] if res else None
    return cache[q]


def main():
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    data = json.loads(SRC.read_text())
    stats = {"ok": 0, "city_mismatch": 0, "failed": 0}
    for ev in data["events"]:
        for s in ev["sessions"]:
            s["geo"] = None
            for qi, q in enumerate(s["queries"]):
                hit = lookup(q, cache)
                if not hit:
                    continue
                lat, lon = float(hit["lat"]), float(hit["lon"])
                inside = BBOX[0] <= lat <= BBOX[1] and BBOX[2] <= lon <= BBOX[3]
                city_ok = norm(s["city"]).rstrip("市縣") in norm(hit["display_name"])
                if not inside or not name_ok(q, hit) or not city_ok:
                    continue
                s["geo"] = {"lat": lat, "lon": lon, "query": q, "display_name": hit["display_name"],
                            "precision": "address" if re.search(r"\d+號", q) else ("venue-or-campus" if qi == 0 else "institution"),
                            "city_check": "ok" if city_ok else "MISMATCH"}
                break
            key = "failed" if not s["geo"] else ("ok" if s["geo"]["city_check"] == "ok" else "city_mismatch")
            stats[key] += 1
            print(f'{ev["id"]} {s["venue_zh"][:22]:<24} ->', s["geo"] and (s["geo"]["city_check"], s["geo"]["query"], round(s["geo"]["lat"], 4), round(s["geo"]["lon"], 4)), file=sys.stderr)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1))
    print(stats, file=sys.stderr)


if __name__ == "__main__":
    main()
