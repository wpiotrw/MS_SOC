#!/usr/bin/env python3
"""§5cf (29 IX 2026): zakres wlasnej kopii stron Microsoft Learn.

Kopia obejmuje tylko strony, ktorych portal UZYWA — nie cale zestawy dokumentacji:
  * kazdy adres learn.microsoft.com w najnowszym pliku site/data/RRRR-MM-DD.json(.gz),
  * kazdy adres z microsoftlearn_sources.json (wlasciciel dopisuje obszary — wchodza same).
Strona raz zacytowana zostaje w kopii na stale: learn-mirror sprawdza w kazdym przebiegu
kazda strone, ktora juz zna, i usuwa ja tylko, gdy Learn odpowie 404 albo przekierowaniem.

Adresy sa grupowane po pierwszym segmencie sciezki (entra, intune, azure, graph...).
Kazda grupa to osobny katalog mirror/learn/<segment>/ z wlasna konfiguracja: sciezki plikow
zrodlowych z roznych repozytoriow koliduja (test 29 IX: Entra zapisala sie jako docs/...),
a w obrebie jednego segmentu pochodza z jednego zestawu dokumentacji.

Uzycie:
  python3 tools/mirror_scope.py [REPO]           # zapisuje konfiguracje i seed-urls.txt
  python3 tools/mirror_scope.py [REPO] --check   # po przebiegu: kolizje sciezek w stanie
"""
import glob, gzip, json, os, re, sys

LEARN = re.compile(r"https://learn\.microsoft\.com/[^\s\"'<>)\]\\]+")
LOCALE = re.compile(r"^[a-z]{2}(-[a-z]{2,4})?$")  # en-us, en, zh-hans — nie jest obszarem
# Adresy, ktore nie sa stronami dokumentacji albo nie oddaja Markdown
SKIP_SEG = {"answers", "training", "shows", "search", "api", "_themes", "media", "contribute",
            "legal", "previous-versions", "users", "credentials", "certifications", "samples"}
SKIP_EXT = re.compile(r"\.(png|jpe?g|gif|svg|json|xml|pdf|zip|yml|yaml|txt|csv)$", re.I)
# Mala mapa witryny spoza naszych obszarow: learn-mirror wymaga co najmniej jednej pasujacej
# mapy, a jej strony (/contribute/) nie pasuja do zadnego `include`, wiec zakres wyznaczaja
# wylacznie nasze dane (seed-urls.txt i strony juz znane).
SITEMAP = r"/_sitemaps/contribute_en-us_1\.xml$"
STATE_DAY = re.compile(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$")


def normalize(u):
    u = u.split("#", 1)[0].split("?", 1)[0].rstrip("/.,;")
    path = u[len("https://learn.microsoft.com/"):]
    parts = [p for p in path.split("/") if p]
    if parts and LOCALE.match(parts[0].lower()):
        parts = parts[1:]
    if not parts or parts[0].lower() in SKIP_SEG or SKIP_EXT.search(parts[-1]):
        return None, None
    seg = parts[0].lower()
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", seg):
        return None, None
    return seg, "https://learn.microsoft.com/en-us/" + "/".join(parts)


def newest_state(repo):
    days = sorted(f for f in os.listdir(os.path.join(repo, "site", "data")) if STATE_DAY.match(f))
    if not days:
        return None, ""
    f = os.path.join(repo, "site", "data", days[-1])
    raw = gzip.open(f, "rt", encoding="utf-8").read() if f.endswith(".gz") else open(f, encoding="utf-8").read()
    return days[-1], raw


def collect(repo):
    texts = []
    day, raw = newest_state(repo)
    texts.append(raw)
    src = os.path.join(repo, "microsoftlearn_sources.json")
    if os.path.exists(src):
        for e in json.load(open(src, encoding="utf-8-sig")):
            if isinstance(e, dict):
                texts.append(" ".join(str(v) for v in e.values()))
    groups = {}
    for t in texts:
        # adresy w JSON bywaja z ucieczka "\/" — zdejmujemy ja przed dopasowaniem
        for u in LEARN.findall(t.replace("\\/", "/")):
            seg, url = normalize(u)
            if seg:
                groups.setdefault(seg, set()).add(url)
    return day, groups


def write_if_changed(path, content):
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != content:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8", newline="\n").write(content)
        return True
    return False


def build(repo):
    day, groups = collect(repo)
    base = os.path.join(repo, "mirror", "learn")
    changed, total = 0, 0
    for seg, urls in sorted(groups.items()):
        d = os.path.join(base, seg)
        cfg = {
            "sitemaps": SITEMAP,
            "tocs": [],
            "extraUrls": [],
            "include": "^https://learn\\.microsoft\\.com/en-us/%s/" % re.escape(seg),
            "exclude": [],
            "trackedPaths": ".",
            "sourceRepos": [],
            "priority": "(whats-new|release-notes|what-s-new)",
            "concurrency": 4,
            "maxRequestsPerSecond": 8,
        }
        changed += write_if_changed(os.path.join(d, "learn-mirror.config.json"), json.dumps(cfg, indent=2) + "\n")
        # seed jest SUMA: dotychczasowe adresy zostaja, dochodza nowe
        seed = os.path.join(d, ".learn-mirror", "seed-urls.txt")
        old = set(open(seed, encoding="utf-8").read().split()) if os.path.exists(seed) else set()
        allu = sorted(old | urls)
        changed += write_if_changed(seed, "\n".join(allu) + "\n")
        total += len(allu)
    print("mirror_scope: state %s -> %d groups, %d seeded pages, %d files changed"
          % (day, len(groups), total, changed))
    for seg, urls in sorted(groups.items(), key=lambda kv: -len(kv[1]))[:12]:
        print("  %-36s %4d" % (seg, len(urls)))


def check(repo):
    """Kolizja = dwie strony zapisane pod ta sama sciezka w jednej grupie. Wtedy kopia jednej
    nadpisuje druga, wiec zglaszamy ja glosno (kod wyjscia 3) zamiast tracic tresc po cichu."""
    bad = 0
    for st in sorted(glob.glob(os.path.join(repo, "mirror", "learn", "*", ".learn-mirror", "state.json"))):
        pages = json.load(open(st, encoding="utf-8")).get("pages", {})
        by = {}
        for url, e in pages.items():
            if e.get("path"):
                by.setdefault(e["path"], []).append(url)
        for p, us in by.items():
            if len(us) > 1:
                bad += 1
                print("COLLISION %s: %s <- %s" % (st.split(os.sep)[-3], p, ", ".join(us)))
    print("mirror_scope --check: %d collisions" % bad)
    return 3 if bad else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    repo = os.path.abspath(args[0] if args else os.getcwd())
    sys.exit(check(repo) if "--check" in sys.argv else build(repo) or 0)
