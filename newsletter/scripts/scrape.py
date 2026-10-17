#!/usr/bin/env python3
"""Collect raw event pages from NTU and Academia Sinica (public pages only).

Writes data/raw/<source>-<n>.txt (plain text of each event page) and
data/raw/index.json (url, source, list title). Structuring into events.json is
done by hand afterwards, as in the event-map prototype, so every field can be
checked against the page text.
"""
import html, json, re, time, urllib.request
from pathlib import Path
from urllib.parse import urljoin

OUT = Path(__file__).resolve().parent.parent / "data" / "raw"
UA = {"User-Agent": "Mozilla/5.0 (campus-ai-contest student prototype)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=25).read().decode("utf8", "ignore")


def text(h):
    h = re.sub(r"<(script|style|nav|footer|header)[^>]*>.*?</\1>", "", h, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", h))
    return re.sub(r"\n\s*\n+", "\n", re.sub(r"[ \t]+", " ", t)).strip()


def anchors(h, base):
    for m in re.finditer(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        label = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))).strip()
        yield urljoin(base, html.unescape(m.group(1))), label


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items = []

    # NTU homepage "活動快報": titles end with ~YYYY/MM/DD
    base = "https://www.ntu.edu.tw/"
    h = get(base)
    for m in re.finditer(r'title="([^"]+~20\d\d/\d\d/\d\d)[^"]*"[^>]*href="([^"]+)"', h):
        items.append(("ntu", html.unescape(m.group(2)), html.unescape(m.group(1))))

    # Academia Sinica, Institute of Economics seminars
    base = "https://www.econ.sinica.edu.tw/4d49b1b1-d551-4956-84a5-6bbf392d8417/pages/29?online=29"
    for u, label in anchors(get(base), base):
        if "/posts/" in u and label and "TBA" not in label and len(label) > 12:
            items.append(("sinica-ieas", u, label))

    # Academia Sinica, Institute of Linguistics lectures and conferences
    for typ in (1, 2):
        base = f"https://www.ling.sinica.edu.tw/main/zh-tw?act=activity_list&c=list&type={typ}"
        h = get(base)
        for m in re.finditer(r'<a href="([^"]+)"[^>]*title="([^"]+?)\(另開新視窗\)"', h):
            u = urljoin("https://www.ling.sinica.edu.tw/main/", html.unescape(m.group(1)))
            items.append(("sinica-ling", u, html.unescape(m.group(2))))

    seen, index = set(), []
    for src, url, label in items:
        if url in seen:
            continue
        seen.add(url)
        n = sum(1 for i in index if i["source"] == src) + 1
        name = f"{src}-{n:02d}.txt"
        try:
            body = text(get(url))
        except Exception as e:  # keep going; record the failure
            body = f"FETCH FAILED: {e}"
        (OUT / name).write_text(f"URL: {url}\nLIST TITLE: {label}\n\n{body[:6000]}\n", encoding="utf8")
        index.append({"file": name, "source": src, "url": url, "list_title": label})
        time.sleep(0.5)
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf8")
    print(len(index), "pages saved to", OUT)


if __name__ == "__main__":
    main()
