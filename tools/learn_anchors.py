#!/usr/bin/env python3
"""learn_anchors.py - point every Microsoft Learn link of the portal at the SECTION it is about (CLAUDE.md 5fl).

Owner, 26 X 2026: "the Microsoft Learn link of the Play Integrity item opens the top of the Intune in-development
page; I had to scroll and did not know it was important. Every Microsoft link should land on its section."

Reads our own Markdown copy of the Learn pages (mirror/learn, workflow learn-mirror.yml: canonicalUrl + headings),
the newest state site/data/<date>.json, and writes site/data/learn-anchors.json:
  {"items": {"<item id>": "<url>#<anchor>"}, "titles": {"<page url>": {"<normalised heading>": "<anchor>"}}, ...}
 - items: an item of the brief whose url is a Learn page gets the heading that matches its own words best
   (title, Microsoft's title, fingerprint), only above a clear threshold - a wrong anchor is worse than none;
 - titles: for the pages the portal links to, every heading, so a link whose TEXT is a heading (what's new entries)
   finds its anchor in the browser.
Learn builds anchors from the heading: lower case, everything but letters, digits, spaces and hyphens dropped,
spaces to hyphens ("Plan for Change: Google Play strong ... above" -> "plan-for-change-google-play-strong-...-above").
Never fails the job: a missing mirror or state writes nothing and exits 0.
"""
import glob, json, os, re, sys

STOP = set("a an and are as at be by for from has have in into is it its of on or that the this to with will your you "
           "new now microsoft update updates change changes support "
           # product names match every heading of a product page - they never decide a section
           "defender entra azure intune office 365 windows sentinel purview teams exchange".split())


def slug(h):
    """Learn's own rule, checked against live pages 26 X 2026: lower case, '?' becomes '-', other punctuation is
    dropped, EVERY space becomes '-' (so "Android | Oct 2026" -> "android--oct-2026"), nothing is trimmed."""
    h = re.sub(r"`|\*\*|\*|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", h)
    h = h.strip().lower().replace("?", "-")
    h = re.sub(r"[^\w\s-]", "", h, flags=re.U)
    return re.sub(r"\s", "-", h)


def textfrag(h):
    """a text fragment (#:~:text=) for browsers that support it - it finds the heading even if Learn ever changes
    its id rule; the id before it serves the others"""
    from urllib.parse import quote
    t = re.sub(r"`|\*\*|\*|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", h).strip()
    w = t.split()
    return quote(" ".join(w[:8]), safe="")


def norm_url(u):
    u = str(u or "").split("#")[0].split("?")[0].rstrip("/").lower()
    u = re.sub(r"^https?://learn\.microsoft\.com/(?:[a-z]{2}-[a-z]{2}/)?", "https://learn.microsoft.com/", u)
    return u


def words(t):
    return [w for w in re.findall(r"[a-z0-9]+", str(t or "").lower()) if len(w) > 2 and w not in STOP]


def pages(root):
    out = {}
    for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        try:
            txt = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = re.search(r"^canonicalUrl:\s*(\S+)", txt, re.M)
        if not m:
            continue
        hs, seen = [], {}
        for h in re.findall(r"^#{2,4}\s+(.+?)\s*#*\s*$", txt, re.M):
            s = slug(h)
            if not s:
                continue
            n = seen.get(s, 0); seen[s] = n + 1
            hs.append((h, (s if n == 0 else "%s-%d" % (s, n)) + ":~:text=" + textfrag(h)))
        out[norm_url(m.group(1))] = hs
    # a page moved inside Learn keeps its old address as a redirect: index both the canonical url and the
    # intune-service form the state still carries (urlBefore)
    return out


def best(item, heads):
    """the heading this item is about, or None. Measured 26 X 2026 on 107 Learn items: a plain overlap score sent
    "EmailPostDeliveryEvents gains ApproverUpn" to "Defender for Office 365 Plan 1 and Plan 2" and missed the Play
    Integrity entry (4 of 8 heading words) - so a heading wins when it is covered (4+ shared words, 80%+ of the
    heading) or CLEARLY ahead of the next heading on the same page; a permission name as heading only on an exact
    mention."""
    txt = " ".join(str(item.get(k) or "") for k in ("title", "officialTitle", "fingerprint"))
    ws = set(words(" ".join(str(item.get(k) or "") for k in ("title", "officialTitle"))))
    if not ws:
        return None
    sc = []
    for h, a in heads:
        hw = set(words(h))
        if not hw:
            continue
        if "." in h and " " not in h.strip():
            if h.strip().lower() in txt.lower():
                return a
            continue
        hit = len(ws & hw)
        sc.append((hit + hit / float(len(hw)), hit, hit / float(len(hw)), a))
    if not sc:
        return None
    sc.sort(reverse=True)
    b, s2 = sc[0], (sc[1][0] if len(sc) > 1 else 0)
    if b[1] >= 4 and b[2] >= 0.8:
        return b[3]
    if b[1] >= 3 and b[0] - s2 >= 1.5:
        return b[3]
    return None


def main(site, mirror):
    states = sorted(glob.glob(os.path.join(site, "data", "20??-??-??.json")))
    P = pages(os.path.join(mirror, "learn"))
    if not states or not P:
        print("learn_anchors: nothing to do (states %d, pages %d)" % (len(states), len(P)))
        return 0
    st = json.load(open(states[-1], encoding="utf-8")).get("soc-brief-state", {})
    out, used = {"items": {}, "titles": {}}, set()
    for it in st.get("items", []):
        # only when the item's own link IS the Learn page (an item that moved to a blog keeps its blog link)
        u = norm_url(it.get("url"))
        if u in P and "#" not in str(it.get("url")):
            a = best(it, P[u])
            if a:
                out["items"][it["id"]] = str(it.get("url")) + "#" + a
                used.add(u)
    links = set(norm_url(it.get("url")) for it in st.get("items", []))
    for x in (st.get("nt") or {}).get("items", []) or []:
        links.add(norm_url(x.get("link") or x.get("url")))
    for u in links:
        if u in P:
            out["titles"][u] = dict((" ".join(words(h)), a) for h, a in P[u])
    out["state"] = os.path.basename(states[-1])
    out["pages"] = len(P)
    path = os.path.join(site, "data", "learn-anchors.json")
    new = json.dumps(out, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    if new != old:
        open(path, "w", encoding="utf-8").write(new)
        print("learn_anchors: wrote %s - %d items anchored, %d pages with headings, %d kB"
              % (path, len(out["items"]), len(out["titles"]), len(new) // 1024))
    else:
        print("learn_anchors: no change - %d items anchored" % len(out["items"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "site", sys.argv[2] if len(sys.argv) > 2 else "mirror"))
