# MS_SOC — instrukcja dla scheduled tasks (routines)

Repozytorium hostuje statyczna strone publikowana automatycznie do Azure Static Web Apps.
Kazdy push do `main`, ktory dotyka katalogu `site/`, uruchamia deploy.

# 0. LISTA KONTROLNA — wykonywana i sprawdzana w KAZDYM przebiegu

**Ta sekcja jest nadrzedna wobec promptu.** Prompt taska albo routine wymienia z nazwy tylko czesc
sekcji tego pliku; przebieg, ktory zrobil wylacznie to, co prompt wymienil, jest przebiegiem
NIEUDANYM. 31 sierpnia 2026 zmierzono to na dwoch stronach tego samego dnia:

| regula | strona SWA (routine, 15:22) | artefakt (scheduled task, 15:25) |
|---|---|---|
| §1 kolejnosc pigulek | OK | OK |
| §1a blok mobilny | OK | OK |
| §5e `b-undoc` / `b-elsewhere` | OK | OK |
| §5k `.card-title`, `.cat-changed` | **BRAK** | OK |
| §5l `site/kql/` | **BRAK** | n/d (artefakt nie ma repo) |
| §5n `officialTitle` | **BRAK (0)** | OK (156) |
| §5q `firstTracked`, `discoveries` | **BRAK** | **BRAK** |
| §5r `linkStatus` | **BRAK (0)** | tylko 3 wpisy |
| §5t chipy linkow, ramki `h3` | **BRAK** | OK |
| §5u sekcja `docchanges` | **BRAK** | **BRAK** |
| §5v denominator DeltaPulse | **BRAK** | OK |

Dwie strony tego samego dnia, ten sam plik specyfikacji, dwa rozne wyniki. Przyczyna nie jest
w danych ani w powloce: **przebieg stosowal to, co wyliczyl prompt, zamiast tego, co mowi ten plik.**

## Jak sie tego uzywa

1. **Przeczytaj ten plik w calosci, zanim cokolwiek zbudujesz** — nie tylko sekcje, ktore prompt
   wymienil z numeru.
2. **Przejdz ponizsza liste pozycja po pozycji i zapisz wynik kazdej.** Pozycja niewykonana ma
   powod, nigdy cisze.
3. **Przed publikacja uruchom asercje z kolumny „sprawdzenie".** Kazda jest wykonalna w kodzie na
   gotowym pliku HTML — to nie jest ocena, tylko test.
4. **W odpowiedzi wypisz liste jako `OK` / `BRAK <powod>`.** Wlasciciel czyta ta liste zamiast
   szukac braków na stronie.

## Lista

| # | co | sekcja | sprawdzenie na gotowym HTML |
|---|---|---|---|
| 0 | **routine odbija artefakt, nie buduje strony sam** | 0a | `verify()` w `mirror_artifact.py` konczy sie bez bledu; fallback opisany w odpowiedzi |
| 1 | siedem pigulek na stronie porannej, **osiem po passie popoludniowym** (ta dodatkowa to `since the morning pass`, §4d taska popoludniowego); pierwsze trzy zawsze: terminy, `undocumented at Microsoft`, `deployed, not in this tenant` | 1, 5e | pierwsze trzy `.counts a.count` w tej kolejnosci; licznik 7 albo 8, nigdy mniej |
| 2 | blok mobilny jako OSTATNI w `<style>` | 1a | `@media (max-width:760px)` wystepuje po ostatnim `.cat-controls{position:sticky` |
| 3 | dziewiec paneli `.tabpanel`, identyfikatory sekcji z §2 | 2 | licznik po usunieciu komentarza SHELL CONTRACT = 9 |
| 4 | znaczniki `<span class="badge b-…">` w kazdej tabeli, emoji 🔥/⚠️ w kazdej zakladce | 4 | `.badge` liczony w setkach, nie dziesiatkach |
| 5 | `KIND_BADGE` + `.badge.b-undoc` + `.badge.b-elsewhere` | 5e | wszystkie trzy obecne w pliku |
| 6 | `docStatus`, `docSource`, `docCheckedOn` na kazdym wpisie | 5e | zero wpisow bez `docStatus` |
| 7 | `descriptionByType` albo `descriptionSource:"none"` z data | 5j | zero wpisow bez jednego z dwoch |
| 8 | cztery reguly czytelnosci: `.cat-changed`, `summary` 14.5px, `.card-title`, zielone pola szukania | 5k | wszystkie cztery selektory w koncowym CSS |
| 9 | tresc pod `+` jako `<ul><li>`, nigdy proza | 5k | kazdy `details.foldnote` zawiera `<ul>` |
| 10 | pliki `site/kql/RRRR-MM-DD-<slug>.kql` + `index.json` | 5l | katalog istnieje i ma wpis na kazde opublikowane zapytanie |
| 11 | Today mowi, ze jest wyborem z N pozycji; kazdy wiersz Today ma `id` w New | 5m | zero wierszy Today bez pary w New |
| 12 | `officialTitle` i `reference` na kazdej pozycji stanu; kolumna `Reference` w New | 5n | licznik `officialTitle` = licznik pozycji stanu |
| 13 | grupowanie miesiacami w New i Deadlines | 5o | osobna tabela z `<caption>` na miesiac |
| 14 | Top N wazony bezpieczenstwem, `sec-note` mowi czym | 5p | `sec-note` sekcji `top5` zawiera zdanie o wazeniu |
| 15 | `firstTracked` na KAZDYM wpisie, `changed = deployedSeen` dla `D\A`, tablica `discoveries`, chip `New today` | 5q | licznik `firstTracked` = licznik wpisow; `discoveries` istnieje |
| 16 | `linkStatus` i `linkCheckedOn` na kazdym wpisie i kazdej pozycji stanu; zdanie w Sources | 5r | licznik `linkStatus` >= licznik pozycji stanu; `a.lnk-dead` = 0 |
| 17 | zadna fasetowana kolumna nie ma samych jedynek | 5s | dla kazdego `figure.chart` o >=4 slupkach nie wszystkie = 1 |
| 18 | szesc regul §5t na koncu `<style>` | 5t | `.sec-body a[href^="http"]` i `#tab-products .sec-body h3` obecne |
| 19 | podloga pokrycia: suma wierszy deep dive = liczba pozycji okna przypisanych do produktu | 5u | roznica zerowa albo opisana wierszem z powodem |
| 20 | sekcja `<section id="docchanges" data-nav="Doc changes">` w panelu `tab-new` | 5u | `id="docchanges"` obecne |
| 21 | kazde zrodlo raportuje przeczytane / wniesione / odrzucone | 5u, 5v | kazdy wiersz Sources ma trzy liczby |
| 22a | kolumna `Source` fasetowalna i przypieta | 5w | `<select>` z `All source` w New i Today; ostatni `th` ma `position:sticky` i `right:0` |
| 22 | DeltaPulse jako denominator MC + Roadmapy, `previousValues`/`newValues` do `<del>`/`<ins>` | 5v | pigulka „items in window" niesie denominator albo Sources mowi, ze MCP byl niedostepny |

**Pozycja, ktorej nie da sie wykonac, bo zrodlo bylo niedostepne, jest `BRAK` z nazwa zrodla —
nigdy nie jest pomijana w ciszy.** Pozycje 15, 16, 19, 20 sa wiazace: przebieg, ktory je pominie
bez powodu, nie publikuje.

## 0a. LUSTRO — artefakt jest zrodlem, SWA jest jego kopia

**Dwa przebiegi budujace niezaleznie te sama strone z tej samej specyfikacji NIE zbiegaja sie.**
Zmierzone 31 sierpnia 2026, dwie strony w odstepie trzech minut: artefakt mial 1 741 znacznikow,
380 chipow linkow (`border-radius: 999px`, niebieskie tlo) i 22 wykresy; strona SWA — 601 znacznikow,
354 kotwice bez ramki (`border-radius: 0px`, tlo przezroczyste) i 19 wykresow. Ten sam dzien,
ten sam plik regul, dwa rozne produkty. Roznicy nie da sie zamknac dopisywaniem regul, bo
przyczyna nie jest w regulach.

**Dlatego routine raportu porannego NIE BUDUJE juz strony. Kopiuje artefakt.**

### Kolejnosc dnia

| godzina (Warsaw) | co |
|---|---|
| 06:00 | scheduled task poranny buduje i publikuje artefakt `Microsoft SOC Brief <data>` |
| 07:00 | **routine czyta ten artefakt i odbija go do `site/index.html`** |
| 16:00 | scheduled task popoludniowy republikuje TEN SAM artefakt (sekcja `#pmdelta`) |
| 21:00 | routine zmian odbija artefakt `Microsoft SOC Delta <data>` do `site/diff/index.html` |

### Procedura, krok po kroku

1. `Artifact action:"list", scope:"mine", limit:20` — znajdz `Microsoft SOC Brief <dzisiejsza data>`.
2. `Artifact action:"read"` z jego `url`. Strona ma ~3,8 MB, wiec narzedzie **zapisze ja do pliku
   i poda sciezke w wyniku** — nie probuj jej czytac oczami, uzyj tej sciezki.
3. Zapisz ponizszy skrypt do `/tmp/mirror_artifact.py` i uruchom:
   `python3 /tmp/mirror_artifact.py <sciezka-z-kroku-2> site`
   Skrypt sam odrzuci przebieg, gdy czegos brakuje — **kod wyjscia 1 znaczy NIE PUBLIKUJ**.
4. Przenies poprzednia wersje do `site/history/RRRR-MM-DD-poranny.html` (zasada 2).
5. `git pull --rebase origin main`, commit, push, i udowodnij `BEFORE != AFTER` (zasada 7).

### Strona `/diff/` — ten sam skrypt, tryb `--diff`

`python3 /tmp/mirror_artifact.py <sciezka> site --diff` daje `site/diff/index.html`. Skrypt sam
rozpoznaje, co dostal:

- **artefakt `Microsoft SOC Delta <data>`** (dwa panele) — odbija go w calosci, podmieniajac tylko
  link w `dateline` na `/` (zasada 3);
- **artefakt `Microsoft SOC Brief <data>`** (dziewiec paneli) — wyjmuje z niego sekcje `#pmdelta`
  i sklada strone o DWOCH panelach, `tab-overview` i `tab-changed`, z ta sama powloka: ten sam
  `<style>`, te same trzy skrypty zachowania, ten sam masthead, oba bloki JSON;
- **brief bez `#pmdelta`** — pisze uczciwa strone „bez zmian" z godzina sprawdzenia, zamiast
  zostawic wczorajsza. Task 2 wymaga, zeby strona zawsze byla nadpisana.

Zmierzone 31 sierpnia 2026 na artefakcie 15:25 (ktory `#pmdelta` NIE mial): `diff/index.html`
3 626 297 B, render 1500x1000 — 2 zakladki `Overview` i `What changed`, 2 panele, jeden widoczny,
7 pigulek, 7 kafelkow Overview, sekcja `#delta` z data, link powrotny do `/`, zero kontenerow
katalogu, **zero bledow konsoli**, zero przewijania w poziomie.

Trzy pulapki, ktore skrypt obchodzi, bo kazda wywrocila go w tescie: komentarz `SHELL CONTRACT`
**cytuje** `<header class="top">`, `<style>` i `<script>`, a bywa przerwany wczesnym `-->`, wiec
jego resztki udaja markup — dlatego masthead bierzemy z OSTATNIEGO wystapienia, a przy skladaniu
`/diff/` caly komentarz wycinamy (`drop_contract`); z dopasowan `<script>` odrzucamy te, ktore
zawieraja w srodku kolejne `<script` i bierzemy trzy ostatnie; a liczenie elementow idzie przez
`html.parser`, nie przez wyrazenia regularne, bo powloka trzyma `class="tabpanel"` i
`data-catalog` takze w kodzie skryptow — zliczanie tekstem dawalo 12 paneli tam, gdzie sa 2.

**Fallback, i tylko on uruchamia stary tryb budowania:** artefaktu na dzisiaj nie ma, albo jego
`briefDate` nie jest dzisiejsza, albo skrypt zwrocil kod 1. Wtedy budujesz strone sam wedlug
STEP 2 i STEP 3 promptu — i **piszesz w odpowiedzi, ze lustro zawiodlo i z jakiego powodu**.
Cicha ucieczka do wlasnego budowania jest tym, przez co strony sie rozjechaly.

### Co robi transformacja — i czego NIE robi

Artefakt jest FRAGMENTEM: powloka `claude.ai` dokleja mu `<head>` z wlasnym runtime'em. Strona SWA
musi byc samodzielna. Skrypt wycina tresc od `<title>` do `</body>`, opakowuje ja w `<!DOCTYPE html>`
z `charset` i `viewport`, przenosi `<title>` i linki do fontow do `<head>`, i dopisuje do `dateline`
link do `/diff/` (zasada 3 — strona nie linkuje do samej siebie). Wyciaga tez oba bloki JSON do
`site/data/<data>.json`, bez ktorego task 2 nie ma punktu odniesienia.

**Skrypt nie dotyka tresci.** Nie przepisuje tabel, nie zmienia liczb, nie dodaje ani nie usuwa
sekcji. Gdyby dotykal, znowu mielibysmy dwie rozne strony.

Zmierzone na artefakcie z 31 sierpnia 2026: wejscie 3 843 497 znakow, wyjscie `index.html`
3 835 792 B, `data/2026-08-31.json` 3,4 MB. Render headless 1500x1000: 9 zakladek, 9 paneli,
jeden widoczny, 7 pigulek, 7 kafelkow Overview, 22 wykresy, 1 741 znacznikow, 380 chipow linkow
z `border-radius: 999px`, zero bledow konsoli i strony, zero przewijania w poziomie.

```python
#!/usr/bin/env python3
"""artifact -> site/index.html  (SWA mirror)
Wejscie : plik z pelnym HTML artefaktu (Artifact action:"read" zapisuje go na dysk)
Wyjscie : samodzielna strona dla Azure Static Web Apps + site/data/<date>.json
Transformacja jest deterministyczna: nic nie przepisuje tresci, tylko opakowuje.
"""
import re, sys, json, os, datetime

def extract_body(raw: str) -> str:
    """Artefakt to FRAGMENT: runtime ramki siedzi w <head>, tresc zaczyna sie od <title>."""
    start = raw.find("<title>")
    if start < 0:
        raise SystemExit("FAIL: brak <title> w artefakcie")
    end = raw.rfind("</body>")
    if end < 0:
        end = len(raw)
    return raw[start:end]

def build_page(content: str, diff_href: str = "/diff/") -> str:
    m = re.search(r"<title>(.*?)</title>", content, re.S)
    title = m.group(1).strip() if m else "Microsoft SOC Brief"
    content = content.replace(m.group(0), "", 1) if m else content

    # linki do fontow przenosimy do <head>; w body zostawiamy czysta tresc
    fonts = re.findall(r'<link[^>]+fonts\.(?:googleapis|gstatic)\.com[^>]*>', content)
    for f in fonts:
        content = content.replace(f, "", 1)
    head_links = "\n".join(fonts) if fonts else ""

    # Zasada 3 CLAUDE.md: index linkuje do /diff/, strona /diff/ do /, nigdy do siebie.
    # UWAGA: nie testuj `diff_href not in inner` — dla diff_href="/" to zawsze falsz,
    # bo KAZDY URL zawiera ukosnik. Sprawdzamy kotwice, nie podciag.
    label = "Back to the full brief" if diff_href == "/" else "Changes since this morning"
    dl = re.search(r'(<p class="dateline">)(.*?)(</p>)', content, re.S)
    if dl:
        inner = dl.group(2)
        # artefakt Delta linkuje do swojej PRYWATNEJ strony claude.ai — przekieruj ja
        inner = re.sub(r'href="https://claude\.ai/[^"]*"', 'href="%s"' % diff_href, inner)
        if not re.search(r'href="%s"' % re.escape(diff_href), inner):
            inner = inner.rstrip() + ' &middot; <a href="%s">%s</a>' % (diff_href, label)
        content = content.replace(dl.group(0), dl.group(1) + inner + dl.group(3), 1)

    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>%s</title>\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n"
        % (title, head_links, content.strip())
    )

def extract_state(content: str, require_catalog: bool = True):
    """Strona Delta (sekcja 3) nie ma przegladarki katalogu, wiec `soc-catalog`
    bywa jej obcy. Wymagamy go tylko dla briefu; brak w trybie --diff nie jest bledem."""
    out = {}
    need = ("soc-brief-state", "soc-catalog") if require_catalog else ("soc-brief-state",)
    for blk in ("soc-brief-state", "soc-catalog"):
        m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % blk, content, re.S)
        if not m:
            if blk in need:
                raise SystemExit("FAIL: brak bloku %s" % blk)
            continue
        out[blk] = json.loads(m.group(1))
    return out

from html.parser import HTMLParser

class _Scan(HTMLParser):
    """Liczy PRAWDZIWE elementy. HTMLParser sam ignoruje tresc <script>/<style>
    i komentarze, wiec cytaty markupu w SHELL CONTRACT nie zaklamuja wyniku."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tabpanels = 0; self.navanchors = 0; self.catalogs = set()
        self.ids = set(); self.scripts = 0; self.jsonblocks = 0; self.styles = 0; self.doctypes = 0
        self.hrefs = set()
    def handle_decl(self, decl):
        if decl.lower().startswith("doctype"): self.doctypes += 1
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if a.get("id"): self.ids.add(a["id"])
        if a.get("href"): self.hrefs.add(a["href"])
        if tag == "div" and "tabpanel" in cls: self.tabpanels += 1
        if tag == "nav" and "anchors" in cls: self.navanchors += 1
        if tag == "div" and a.get("data-catalog"): self.catalogs.add(a["data-catalog"])
        if tag == "style": self.styles += 1
        if tag == "script":
            if (a.get("type") or "").strip() == "application/json": self.jsonblocks += 1
            else: self.scripts += 1

def scan(page: str) -> _Scan:
    p = _Scan(); p.feed(page); return p

def verify(page: str) -> list:
    """Asercje strukturalne dla strony glownej. Pusta lista = mozna publikowac."""
    p = scan(page); errs = []
    if p.tabpanels != 9: errs.append("tabpanel = %d, ma byc 9" % p.tabpanels)
    if p.navanchors != 1: errs.append("nav.anchors = %d, ma byc 1" % p.navanchors)
    if p.catalogs != {"graph", "roles"}: errs.append("data-catalog = %s, ma byc graph+roles" % sorted(p.catalogs))
    for need in ("soc-brief-state", "soc-catalog"):
        if need not in p.ids: errs.append("brak bloku %s" % need)
    if p.jsonblocks != 2: errs.append("blokow JSON = %d, maja byc 2" % p.jsonblocks)
    if p.scripts < 3: errs.append("skryptow zachowania = %d, ma byc >=3" % p.scripts)
    if p.styles < 1: errs.append("brak <style>")
    if p.doctypes != 1: errs.append("DOCTYPE = %d, ma byc 1" % p.doctypes)
    if "/diff/" not in p.hrefs: errs.append("dateline nie linkuje do /diff/")
    return errs

DIFF_SHELL = """<div class="wrap">
<div class="tabpanel" data-tab="Overview" id="tab-overview" hidden></div>
<div class="tabpanel" data-tab="What changed" id="tab-changed" hidden>
%s
</div>
</div>
<footer><p>%s</p></footer>"""

def drop_contract(content: str) -> str:
    """Komentarz SHELL CONTRACT cytuje `<header>`, `<style>` i `<script>` i bywa
    przerwany wczesnym `-->`, przez co jego resztki udaja markup. Do skladania
    strony /diff/ wycinamy go w calosci; strona glowna zachowuje go bez zmian."""
    i = content.find("<!-- SHELL CONTRACT")
    if i < 0:
        return content
    k = content.find("<style", i)
    j = content.rfind("-->", i, k if k > 0 else len(content))
    return content[:i] + content[j + 3:] if j > i else content

def parts(content: str):
    """Powloka: style + trzy skrypty zachowania + oba bloki JSON + masthead."""
    content = drop_contract(content)
    p = {}
    p["styles"] = re.findall(r"<style[^>]*>.*?</style>", content, re.S)
    p["json"]   = re.findall(r'<script type="application/json" id="[^"]+">.*?</script>', content, re.S)
    # blok, ktory zawiera w srodku kolejne "<script", to nadmiarowe dopasowanie regexa
    # po resztkach cytowanego markupu; powloka ma DOKLADNIE trzy skrypty zachowania,
    # i sa to trzy ostatnie bloki na stronie.
    raw_scripts = re.findall(r"<script(?![^>]*application/json)[^>]*>.*?</script>", content, re.S)
    clean = [b for b in raw_scripts if "<script" not in b[len("<script"):]]
    p["scripts"] = clean[-3:]
    # SHELL CONTRACT cytuje `<header class="top">` w komentarzu — bierzemy OSTATNIE wystapienie
    i = content.rfind('<header class="top">')
    j = content.find("</header>", i) if i >= 0 else -1
    p["header"] = content[i:j + len("</header>")] if (i >= 0 and j > i) else ""
    m = re.search(r'<section id="pmdelta".*?</section>', content, re.S)
    p["pmdelta"] = m.group(0) if m else ""
    return p

def build_diff(content: str, date: str, when: str, home_href: str = "/") -> str:
    """Delta -> lustro 1:1. Brief bez #pmdelta -> uczciwa strona 'bez zmian', ta sama powloka."""
    p = parts(content)
    if scan(content).tabpanels <= 3:
        return build_page(content, diff_href=home_href)      # to juz jest strona Delta

    body = p["pmdelta"]
    if body:
        body = body.replace('id="pmdelta"', 'id="delta"', 1)
    else:
        body = ('<section id="delta" data-nav="What changed">'
                '<div class="sec-head"><h2>Section A</h2>'
                '<p class="sec-title">Changes since this morning</p></div>'
                '<div class="sec-body"><p class="sec-note">Re-checked ' + when +
                ' Warsaw. Today\'s brief carries no delta section, so this run has nothing '
                'from the afternoon pass to mirror. The morning page is unchanged.</p></div></section>')

    head = p["header"]
    dl = re.search(r'(<p class="dateline">)(.*?)(</p>)', head, re.S)
    if dl:
        inner = re.sub(r'\s*&middot;\s*<a href="/diff/">[^<]*</a>', "", dl.group(2)).rstrip()
        inner += ' &middot; <a href="%s">Back to the full brief</a>' % home_href
        head = head.replace(dl.group(0), dl.group(1) + inner + dl.group(3), 1)

    inner = DIFF_SHELL % (body, "Piotr Wisniewski &middot; " + date + " &middot; re-checked " + when)
    page = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "<title>Microsoft SOC Changes %s</title>\n%s\n</head>\n<body>\n%s\n%s\n%s\n%s\n</body>\n</html>\n"
            % (date, "\n".join(p["styles"]), head, inner,
               "\n".join(p["json"]), "\n".join(p["scripts"])))
    return page

def verify_diff(page: str) -> list:
    """Asercje strukturalne dla strony /diff/."""
    p = scan(page); errs = []
    if p.tabpanels != 2: errs.append("tabpanel = %d, strona diff ma miec 2" % p.tabpanels)
    if "delta" not in p.ids: errs.append("brak sekcji delta")
    if p.navanchors != 1: errs.append("nav.anchors = %d, ma byc 1" % p.navanchors)
    if p.catalogs: errs.append("strona diff nie ma katalogu, a ma %s" % sorted(p.catalogs))
    if p.scripts < 3: errs.append("skryptow zachowania = %d, ma byc >=3" % p.scripts)
    if p.styles < 1: errs.append("brak <style>")
    if p.doctypes != 1: errs.append("DOCTYPE = %d, ma byc 1" % p.doctypes)
    if "/" not in p.hrefs:
        errs.append("brak linku powrotnego do / — czy strona ma <p class=\"dateline\">?")
    return errs

if __name__ == "__main__":
    src, outdir = sys.argv[1], sys.argv[2]
    mode = "--diff" if "--diff" in sys.argv[3:] else "--brief"
    raw = open(src, encoding="utf-8").read()
    content = extract_body(raw)
    state = extract_state(content, require_catalog=(mode != "--diff"))
    date = state["soc-brief-state"].get("briefDate") or datetime.date.today().isoformat()

    if mode == "--diff":
        when = datetime.datetime.now().strftime("%H:%M")
        page = build_diff(content, date, when)
        errs = verify_diff(page)
        target = os.path.join(outdir, "diff", "index.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
    else:
        page = build_page(content)
        errs = verify(page)
        target = os.path.join(outdir, "index.html")

    if errs:
        print("PRZEBIEG NIEUDANY - nie publikuj:")
        for e in errs: print("   -", e)
        raise SystemExit(1)

    open(target, "w", encoding="utf-8").write(page)
    if mode == "--brief":
        os.makedirs(os.path.join(outdir, "data"), exist_ok=True)
        json.dump(state, open(os.path.join(outdir, "data", date + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False)
    print("OK  %s  %d B  (%s)" % (target, len(page.encode()), mode))
```

**Dwa bledy tego skryptu znalazl przebieg routine 31 sierpnia 2026, oba w trybie `--diff`, oba
zatrzymane przez bramke — i oba sa juz wyzej poprawione:**

- `extract_state()` zadalo `soc-catalog` bezwarunkowo, a strona Delta (sekcja 3) przegladarki
  katalogu nie ma, wiec `--diff` konczyl sie kodem 1. Teraz katalog jest wymagany **tylko dla
  briefu**; kontrola regresji: w trybie `--brief` jego brak nadal jest bledem.
- Test `diff_href not in dl.group(2)` byl zawsze falszywy dla `diff_href="/"`, bo **kazdy URL
  zawiera ukosnik**. Link powrotny nie powstawal i `verify_diff` odrzucal strone. Teraz sprawdzamy
  kotwice, nie podciag, a `href="https://claude.ai/…"` w dateline artefaktu Delta jest
  przekierowywany na `/`.

Zmierzone po poprawce na czterech wejsciach: brief (`--brief` 3 835 792 B, `--diff` 3 626 297 B),
prawdziwa Delta z 28 sierpnia (`--diff` 3 283 650 B), Delta pozbawiona `soc-catalog` i Delta
z linkiem do prywatnego artefaktu w dateline — wszystkie bez bledow.

**Asercje w `verify()` sa bramka publikacji**: dziewiec `.tabpanel` po usunieciu komentarza
SHELL CONTRACT (cytuje markup, ktory opisuje), oba bloki JSON, oba kontenery katalogu, pusty
`<nav class="anchors">`, co najmniej trzy skrypty zachowania, `<style>`, dokladnie jeden DOCTYPE
i link do `/diff/`. Kazda z nich broni bledu, ktory juz raz wystapil.

## Struktura

```
site/
  index.html            <- RAPORT PORANNY (strona glowna)
  diff/index.html       <- ZMIANY OD RANA (podstrona /diff/)
  history/YYYY-MM-DD-poranny.html
  history/YYYY-MM-DD-HHMM-diff.html
  data/YYYY-MM-DD.json  <- surowe dane, zeby diff mial z czym porownywac
```

## Zasady wspolne dla obu taskow

1. Piszesz WYLACZNIE do katalogu `site/`. Nic poza nim.
   Zmiana pliku spoza `site/` blokuje auto-merge i deploy nie ruszy.
2. Przed zapisem nowej wersji przenies poprzednia do `history/` pod nazwa z data.
3. Kazda strona ma w naglowku date i godzine generowania oraz JEDEN link nawigacyjny:
   `site/index.html` linkuje do `/diff/`, `site/diff/index.html` linkuje do `/`.
   Zadna strona nie linkuje do samej siebie.
4. Strony sa samodzielne: HTML + inline CSS, bez zewnetrznych zaleznosci i bez CDN.
5. Commit message: `content: <nazwa taska> <RRRR-MM-DD HH:MM>`.
6. Przed pushem zrob `git pull --rebase origin main`. Dwa taski pisza do tego samego
   repozytorium i moga sie minac.
7. Po pushu udowodnij, ze cos sie zmienilo: `BEFORE=$(git rev-parse origin/main)` przed
   pushem, `git fetch origin` i `AFTER=$(git rev-parse origin/main)` po. `AFTER` musi sie
   roznic od `BEFORE` i rownac twojemu `HEAD`. Rowne = przebieg NIEUDANY, napisz to wprost.

---

# LAYOUT STRONY — WIAZACE DLA OBU TASKOW

Ta sekcja opisuje markup, ktorego wymaga powloka (`<style>` + trzy skrypty wozone w stronie).
**Skrypty nie zglaszaja bledow — po cichu nie buduja tego, czego nie znalazly.** Kazda regula
ponizej zostala wyprowadzona z kodu tych skryptow, nie z upodoban.

## 1. Masthead — dokladnie ta struktura

```html
<header class="top"><div class="top-inner">
<div class="title-row"><h1>Microsoft SOC Brief</h1>
<p class="dateline">Saturday 29 August 2026 &middot; <b>published 07:12 Warsaw</b> &middot; window 15&ndash;29 August &middot; deadlines to 28 October &middot; Piotr Wisniewski &middot; <a href="/diff/">Changes since this morning</a></p>
<div class="hdr-tools"><button class="themebtn" type="button" onclick="__socToggleTheme()">Theme</button></div></div>
<div class="counts">
<a class="count crit" href="#deadlines"><b>34</b> deadlines in 60 days<span>&middot; 12 inside 30</span></a>
<a class="count" href="#graph"><b>28</b> undocumented at Microsoft<span>&middot; 25 permissions, 3 roles</span></a>
<a class="count" href="#graph"><b>306</b> deployed, not in this tenant<span>&middot; 20 visible, 286 hidden</span></a>
<a class="count chg" href="#delta"><b>58</b> changes since 27 Aug<span>&middot; 3 at source, 55 ours</span></a>
<a class="count" href="#new"><b>110</b> items in window<span>&middot; 14&ndash;28 August</span></a>
<a class="count" href="#graph"><b>1,020</b> permissions catalogued<span>&middot; 4 API surfaces</span></a>
<a class="count" href="#roles"><b>1,959</b> role actions<span>&middot; 135 built-in roles</span></a>
</div><nav class="anchors"></nav></div></header>
```

- `.hdr-tools` — skrypt 2 montuje tu globalny filtr produktow:
  `querySelector("header.top .hdr-tools")`. Brak elementu = brak filtra i brak przycisku Theme.
- `.counts` — skrypt 2 przepisuje te pigulki na duze kafelki w panelu Overview.
  Brak `.counts` = Overview bez kafelkow.
- `<nav class="anchors"></nav>` PUSTY, na koncu `.top-inner` — bez niego `buildTabs()` konczy
  dzialanie i nie powstaje pasek zakladek, a zaden panel nie zostaje odsloniety.
- Nigdy nie wymyslaj wlasnych klas `.inner`, `.meta` ani wlasnego `<nav>`.
- **`dateline` zawsze niesie godzine generowania i autora.** `published HH:MM Warsaw` na stronie
  porannej, `re-checked HH:MM Warsaw` dopisywane przez kazdy przebieg diff — nigdy zastepowane.
  Autor: `Piotr Wisniewski`. Ta sama para wraca w `<footer>`: autor, data i godzina, commit.
  Strona bez godziny nie mowi czytelnikowi, czy patrzy na dzisiejszy przebieg czy na wczorajszy.
- Pigulek jest teraz siedem. Kazda `.counts a.count` staje sie kafelkiem w Overview, wiec licznik
  dodajesz przez dopisanie pigulki, nigdy przez pisanie `.stat` recznie.
- **Kolejnosc pigulek jest wiazaca: terminy, `undocumented at Microsoft`, `deployed, not in this
  tenant`, dopiero potem reszta.** Na telefonie pasek jedzie poziomo (sekcja 1a), wiec szosta
  i siodma pigulka sa poza ekranem. 30 sierpnia 2026 obie byly na stronie i wlasciciel nie zobaczyl
  zadnej. Pigulka, ktorej nie widac bez przewijania w bok, nie liczy sie jako kafelek.

## 1a. Naglowek MUSI dac sie przewinac na telefonie

`header.top` ma w powloce `position:sticky;top:0`, a `.counts` ma `flex-wrap:wrap`. Na telefonie
siedem pigulek lamie sie na siedem wierszy i przyklejony naglowek zjada caly ekran — nie da sie go
przewinac, zostaje kilka linii tresci.

**Blok mobilny dopisujesz na SAMYM KONCU `<style>`, nigdy do istniejacego bloku `@media`.**
Zmierzone w arkuszu strony z 30 sierpnia 2026: `header.top{position:sticky}` stoi na pozycji ~19 950,
wlasny blok `@media (max-width:760px)` powloki na ~35 500, ale `.cat-controls{position:sticky}` jest
redefiniowane DWA RAZY pozniej — na ~54 050 i ~56 690. Specyficznosc jest ta sama, wiec wygrywa
regula pozniejsza: naglowek posluchal, a pasek szukania katalogu nie. Zostal przypiety i na telefonie
zaslanial wyniki w zakladkach Roles i Graph API, dokladnie tak jak zglosil wlasciciel. Blok na koncu
arkusza wygrywa z obiema redefinicjami:

```css
@media (max-width:760px){
  header.top{position:static}
  .counts{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .counts .count{flex:0 0 auto}
  .cat-controls{position:static}
}
```

Domyslnie wiec naglowek **przewija sie razem ze strona**, a pigulki jada w jednym poziomym pasku.
`@media print` juz teraz robi `header.top{position:static}`, wiec powloka to znosi. `--hdr-h:112px`
jest stala i na telefonie i tak klamie — dlatego `.cat-controls` tez przestaje byc sticky.
**Na desktopie `.cat-controls` zostaje sticky** — sekcja 5c tego broni i nie odpinasz go tam.
Playwright sprawdza przy 390x844: `getComputedStyle(header).position === "static"`, `.counts`
miesci sie w jednym wierszu, po przewinieciu o 600 px naglowek jest poza widokiem,
`getComputedStyle(document.querySelector(".cat-controls")).position === "static"`, a po przewinieciu
listy katalogu jej pierwszy wiersz nie jest zaslaniany przez pasek szukania (prostokat wiersza nie
przecina sie z prostokatem `.cat-controls`).

## 2. Ktora sekcja w ktorym panelu — raport poranny

| panel | `data-tab` | sekcje, w tej kolejnosci |
|---|---|---|
| `tab-overview` | `Overview` | *(pusty — wypelnia skrypt 2)* |
| `tab-today` | `Today` | `top5` (Top N) · `picks` · `delta` |
| `tab-new` | `New` | `new` |
| `tab-deadlines` | `Deadlines` | `deadlines` |
| `tab-products` | `Products` | `exec` · `deep` · `auth` |
| `tab-roles` | `Roles` | `roles` |
| `tab-graph` | `Graph API` | `graph` |
| `tab-hunting` | `Hunting & actions` | `kql` · `actions` · `strategic` |
| `tab-sources` | `Sources` | `sources` |

**Identyfikatory sekcji sa kanoniczne — skrypty pytaja o nie po nazwie:**

- `querySelector("#delta table")` buduje wykres Overview *Changes since the last brief*.
  Sekcja nazwana `changes` zamiast `delta` = wykresu nie ma.
- slupki wykresow skacza do `#new` i `#deadlines`. Sekcja `newwindow` zamiast `new` = kazdy
  slupek produktu to martwe klikniecie.
- pigulki naglowka linkuja do `#deadlines`, `#delta`, `#new`, `#graph`, `#roles`.

`top5` jako jedyna sekcja **nie dostaje `data-nav`**. Kazda inna ma.
Panele `tab-roles` i `tab-graph` nie zawieraja tabel — tylko pusty
`<div class="catalog" data-catalog="roles">` i `…="graph"`, ktore wypelnia skrypt 3.

## 3. Ktora sekcja w ktorym panelu — diff

| panel | `data-tab` | sekcje |
|---|---|---|
| `tab-overview` | `Overview` | *(pusty)* |
| `tab-changed` | `What changed` | `delta` · `act` · `sources` |

Dwa panele, nigdy wiecej. Zadnego `<div class="catalog">` — strona diff nie ma przegladarki
katalogu. Liczniki w `.counts` mowia o TYM przebiegu: `0 source-side changes`,
`0 brief-side changes`, `31 sources re-checked`, `1009 Graph permissions re-counted, unchanged`,
`137 Entra roles re-counted, unchanged`.

## 4. Tabele — powloka nie pokoloruje niczego, czego nie oznaczyles

- **Kazda komorka statusu to `<span class="badge b-…">`, nigdy goly tekst.**
  `b-new` nowe u zrodla · `b-upd` zmienione, poprawione, przesuniety termin ·
  `b-dep` wycofywane, usuniete · `b-own` ruch tego raportu, nie Microsoftu.
  Wzorzec z 28 sierpnia: 184 takie znaczniki na stronie (Today 74, New 110).
  Przebieg, ktory pisal golym tekstem, mial 14 i zadnego w New — wszystkie tabele wyszly szare.
- **`🔥` w wierszu, ktorego termin miesci sie w 30 dniach, `⚠️` w 60 — w KAZDEJ zakladce,
  ktora ten wiersz pokazuje, nie tylko w Deadlines.** Skrypt 1 (`markRows()`) czyta emoji
  i nadaje klasy `rowhot`/`rowwarm`; skrypt 2 robi z nich chipy `🔥 under 30 days`
  i `⚠️ 30–60 days` oraz kafelki paska zakladki. Brak emoji = tylko szare `rows in this tab`.
- **Nigdy nie pisz recznie `.panelhead`.** Pasek statystyk buduje skrypt 2 i pomija panel,
  ktory juz taki element ma jako bezposrednie dziecko. We wzorcu jest ich zero.
- **Kolumna faset nazywa sie `Product`** (albo Change type / Status / Priority / Area / Kind /
  Service) — `sectionSummaries()` czyta ja, zeby zbudowac chipy `21 Entra`, `10 Purview`.
- **Kolumna okna czasowego jest obowiazkowa w kazdej datowanej tabeli:** SOC actions
  `Do it before`, tabela zmian `When`, deep dive `Published`.
- Struktura sekcji: `<section id="…" data-nav="…">` › `.sec-head` (`<h2>` litera +
  `<p class="sec-title">`) › `.sec-body`. Tabele w `<div class="tw"><table>…</table></div>`,
  kolumna `Source` zawsze ostatnia.
- Roznice pokazuj, nie opisuj: `<del>` stara wartosc, `<ins>` nowa.

## 5. Stan uslugi bije dokumentacje

Hierarchia zrodel dla uprawnien Graph, od najmocniejszego. **Nigdy nie odwracaj tej kolejnosci.**

0. **Mapa wdrozen Microsoftu — `permissions/new/provisioningInfo.json` w repo
   `microsoftgraph/microsoft-graph-devx-content`.** Najwczesniejszy sygnal, globalny, obejmuje
   uprawnienia ukryte i PPE. Mowi, co ISTNIEJE — nie mowi, co mozesz nadac. Szczegoly: sekcja 5d.
1. **Service principal Graph — stan uslugi w naszym tenancie.** Dokumentacja Microsoftu sama go wskazuje:
   `GET /v1.0/servicePrincipals(appId='00000003-0000-0000-c000-000000000000')`
   `?$select=appRoles,oauth2PermissionScopes,resourceSpecificApplicationPermissions`
2. **`learn.microsoft.com/graph/permissions-reference` — dokumentacja.** Spoznia sie za usluga,
   czasem o tygodnie. Sluzy do opisow, `adminConsent`, `descriptionByType` — nie do rozstrzygania,
   czy uprawnienie istnieje.
3. **Trackery** (msgraphpermissions.com, graphpermissions.merill.net) — pochodne punktu 1, nie 2.

### Dlaczego ta sekcja istnieje

Odczyt service principala z 29 sierpnia 2026 (app-only, `Directory.Read.All`):
**729 `appRoles` · 807 `oauth2PermissionScopes` · 58 RSC = 1 022 unikalne nazwy.**
Katalog mial wtedy 1 028 wpisow i brakowalo w nim **13 zywych uprawnien** (`isEnabled: true`),
wszystkich do KASOWANIA cudzych metod uwierzytelniania:

```
UserAuthenticationMethod.Delete.All          712f5e0d-bc8d-4ae5-8242-cfb9a4921ed3
UserAuthMethod-Email.Delete.All              f0e9adfd-ed6b-45f5-b969-324a75286a39
UserAuthMethod-External.Delete.All           7fa6d39e-1e4e-44be-bf9c-e8260b12e1f5
UserAuthMethod-HardwareOATH.Delete.All       9d8eb432-7ea3-491a-9ed7-e6361b308f08
UserAuthMethod-MicrosoftAuthApp.Delete.All   ae494ca6-9612-417a-972a-ef52efaf2de3
UserAuthMethod-Passkey.Delete.All            9563fbd0-03a7-466e-8042-63d668b7d1a3
UserAuthMethod-Phone.Delete.All              59f17651-8b6c-494e-a269-4ac582fbbca0
UserAuthMethod-PlatformCred.Delete.All       bd760918-651f-4e67-b66f-8f614384dec2
UserAuthMethod-QR.Delete.All                 e1c34213-26ac-400b-9548-a749f1b1a4e0
UserAuthMethod-ResourceKey.Delete.All        a71aecaf-82f1-47c5-ad0a-5e63503b928f
UserAuthMethod-SoftwareOATH.Delete.All       e5676e10-1a16-452b-ad10-71f54b755852
UserAuthMethod-TAP.Delete.All                4f872e9d-d232-4ecd-ab9c-337cbdb184e5
UserAuthMethod-WindowsHello.Delete.All       f3197110-aa7f-4acd-a0fd-71981ad68d42
```

Zadnego nie ma w permissions-reference. Tracker zglosil `UserAuthenticationMethod.Delete.All`
22 sierpnia 2026; przebieg odrzucil je jako „zmyslone", bo dokumentacja go nie miala, i ten blad
trafil do promptu jako regula. **To byl falszywy negatyw, nie ochrona przed halucynacja.**
Uprawnienie do kasowania cudzego passkeya wypadlo z raportu dla SOC, bo Microsoft nie zdazyl
opisac go na Learn.

### Jak przebieg czyta stan uslugi

a. **Lokka**, gdy pulpit wlasciciela jest podlaczony
   (`mcp__remote-devices__Lokka-Microsoft__Lokka-Microsoft`, apiType `graph`, method `get`) —
   odpytaj SP wprost, po jednej kolekcji na wywolanie, i **zapisz surowa odpowiedz do pliku**
   zanim cokolwiek policzysz. To zrodlo pierwsze.
b. **Bez pulpitu** — zrzuty Merilla z tego samego service principala, bez tokenu, odswiezane
   codziennie, pobieralne server-side:
   `https://raw.githubusercontent.com/merill/microsoft-info/main/_info/GraphAppRoles.csv`
   (`"Id","Value","DisplayName","Description"`) i
   `https://raw.githubusercontent.com/merill/microsoft-info/main/_info/GraphDelegateRoles.csv`
   (`"Id","Value","AdminConsentDisplayName","AdminConsentDescription"`).
c. Dopiero potem dokumentacja — po opisy i po to, co Microsoft o uprawnieniu napisal.

**Nie odrzucaj nazwy dlatego, ze nie ma jej w permissions-reference.** Odrzuc ja, gdy nie ma jej
w stanie uslugi. Wpis obecny w stanie uslugi, a nieobecny w dokumentacji, publikujesz oznaczony:

```json
{"kind":"New in service, not yet documented", "origin":"microsoft",
 "published":null, "dateLabel":"Seen in the service",
 "serviceSeen":"2026-08-29", "docsChecked":"2026-08-29",
 "ids":{"application":"712f5e0d-bc8d-4ae5-8242-cfb9a4921ed3"},
 "originNote":"Present in the Graph service principal on 2026-08-29 with isEnabled true; absent from Microsoft's permissions reference the same day."}
```

GUID bierzesz z pola `id` w odpowiedzi service principala albo z kolumny `Id` u Merilla — to jest
odczyt u zrodla, wiec wolno. **Nigdy nie przepisuj GUID-a z ekranu trackera i nigdy go nie zgaduj.**
Gdy zadnego z zrodel 1 nie udalo sie odczytac, nie kasuj nic z katalogu i napisz na stronie, ze
stan uslugi nie byl sprawdzony w tym przebiegu.

**Service principal w tenancie to replika, nie globalny rejestr.** Microsoft wdraza uprawnienia
pierscieniami: to samo uprawnienie bywa juz w jednym tenancie, a w drugim jeszcze nie. Dlatego
„nie ma tego w naszym SP" znaczy „nie da sie tego u nas nadac", a nie „nie istnieje".

Zmierzone 29 sierpnia 2026: msgraphpermissions.com pokazuje `IdentityDiagnostic.Read`
(delegowane, `3839e465-e636-4c8e-b959-340182fb0567`, opis „Allows the app to read own identity
diagnostics information…"). Odczyt SP tego tenanta — `v1.0` i `beta`, `appRoles` 729,
`oauth2PermissionScopes`/`publishedPermissionScopes` 807, RSC 58 — **nie ma tego GUID-a ani slowa
`Diagnostic` nigdzie w surowych plikach**. Tak samo dokumentacja i zrzuty Merilla. Autor trackera
czyta wiec service principala ze SWOJEGO tenanta, ktory dostal wdrozenie wczesniej; opis, ktory
cytuje, to `adminConsentDescription` z obiektu SP, a nie proza z dokumentacji.

Taki wpis ma wlasny stan — nie kasujesz go i nie publikujesz jako naszego:

```json
{"kind":"In the service elsewhere, not in this tenant", "origin":"microsoft",
 "published":null, "dateLabel":"Seen by a tracker, absent from our tenant",
 "trackerSeen":"2026-08-27", "tenantChecked":"2026-08-29",
 "ids":{"delegated":"3839e465-e636-4c8e-b959-340182fb0567"},
 "originNote":"Listed by msgraphpermissions.com; absent from this tenant's Graph service principal on v1.0 and beta on 2026-08-29."}
```

Trzyma sie go w `notPublished` z data sprawdzenia i wraca sie do niego kazdego dnia — az pojawi sie
w naszym SP, i wtedy dostaje `b-new`. GUID przepisujesz tylko wtedy, gdy podal go czlowiek albo
przeczytales go u zrodla; nigdy z ekranu trackera.

## 5a. Zeby „NEW" cokolwiek znaczylo

`firstSeen` mowi, kiedy TEN raport zobaczyl wpis po raz pierwszy — nie kiedy Microsoft go wydal.
Po zasianiu katalogu 27 sierpnia 1 019 z 1 031 wpisow ma `firstSeen: 2026-08-27` i
`kind: "Newly inventoried"`, wiec „nowe" nie odroznia niczego od niczego.

Kazdy wpis niesie wiec drugie pole: **`sourceChanged`** — data po stronie Microsoftu, wzieta
z kolumny `LAST CHANGED` trackera albo z daty publikacji w dokumentacji, `null` gdy nieznana.

- Znacznik `<span class="badge b-new">NEW</span>` dostaje wpis, ktorego `sourceChanged` miesci sie
  w oknie raportu. Nigdy nie nadawaj go na podstawie `firstSeen`.
- `b-upd` dostaje wpis, ktorego `sourceChanged` sie przesunal wzgledem poprzedniego przebiegu.
- Katalog pokazuje oba pola osobno: „w katalogu od <firstSeen>", „zmienione u zrodla <sourceChanged>".

**Dla uprawnien Graph `sourceChanged` liczysz, nie zgadujesz.** Odczyt service principala z sekcji 5
daje zbior nazw w usludze. Roznica zbiorow wzgledem wczorajszego katalogu jest deterministyczna:

- nazwa w dzisiejszym odczycie, ktorej nie bylo wczoraj → `serviceSeen` = dzis, `sourceChanged` = dzis,
  `b-new`. To jest jedyne prawdziwe „NEW" dla uprawnien i nie wymaga zadnej daty od Microsoftu.
- nazwa wczoraj obecna, dzis nieobecna → `b-dep`, `No longer in the service`, z data odczytu.
- odczyt sie nie udal → nie ruszasz katalogu, nie nadajesz zadnych znacznikow i piszesz na stronie,
  ze stan uslugi nie byl sprawdzony. Milczenie udajace „bez zmian" jest gorsze niz przyznanie sie.

Zapisuj przy katalogu `serviceRead`: `{"date":…, "source":"lokka"|"merill"|"none", "appRoles":N,
"delegated":N, "rsc":N}`. Bez tego nastepny przebieg nie ma z czym porownac i „NEW" znowu przestaje
cokolwiek znaczyc.

## 5b. Parsowanie permissions-reference i to, czego Microsoft nie publikuje

`microsoft_docs_fetch` na `https://learn.microsoft.com/graph/permissions-reference` zwraca calosc
(~565 KB). Zapisz i sparsuj skryptem — nigdy nie czytaj oczami. Struktura jest maszynowo regularna:

```
### <PermissionName>
| Category | Application | Delegated |
| --- | --- | --- |
| Identifier | <GUID albo -> | <GUID albo -> |
| DisplayText | … | … |
| Description | … | … |
| AdminConsentRequired | Yes/No | Yes/No |
```

RSC to plaska tabela: `| Name | ID | Display text | Description |`.

Trackery pokazuja „Privilege level — Level 2 · Moderate" i „Roles that support this permission".
**Microsoft nie publikuje ani jednego, ani drugiego** — to wlasna pochodna trackera. Katalog wozi
`notPublished` i renderuje je w kazdym panelu szczegolow, zeby brak byl powiedziany, a nie zgadniety:

```json
"notPublished":{"graph":[["Privilege level","Microsoft publishes no severity or privilege tier …"],
  ["Roles that support this permission","Microsoft publishes no permission-to-role mapping …"],
  ["Request samples","documented on each API method page, not the permissions reference …"]]}
```

Nigdy nie drukuj zmyslonej severity z trackera obok pol Microsoftu — czyta sie ja wtedy jak jego.

## 5c. Katalog: klikalnosc i pasek wyszukiwania

- **Kazdy wiersz tabeli zmian jest linkiem do swojego wpisu.** Klikniecie czysci filtr, ktory by go
  ukryl, zaznacza wpis i przewija liste. Oba katalogi.
- **Szukajka i filtry w jednym przypietym pasku** (`.cat-controls`, `position:sticky`) tuz nad lista.
  Gdy pole szukania siedzialo na gorze panelu, a lista dwa ekrany nizej, odjezdzalo dokladnie wtedy,
  kiedy bylo potrzebne. Nie odpinaj go.
- **`.filterbanner[hidden]` musi dawac `display:none`** — `.filterbanner{display:flex}` wygrywa
  z atrybutem `hidden`, przez co nad lista wisial na stale pusty niebieski pasek.

## 5d. Cztery zbiory. Mapa wdrozen Microsoftu jest najwczesniejszym sygnalem

Odczyt naszego service principala mowi, co MOZNA u nas nadac — nie mowi, co istnieje w usludze.
Microsoft publikuje wlasna, globalna mape wdrozen uprawnien w publicznym repozytorium i to ona
wyprzedza wszystko inne, lacznie z trackerami.

| zbior | co to jest | jak sie go czyta |
|---|---|---|
| **D — mapa wdrozen Microsoftu** | co Microsoft zdefiniowal i wdrozyl gdziekolwiek, **razem z ukrytymi i PPE** | `git clone --depth 1 https://github.com/microsoftgraph/microsoft-graph-devx-content` › `permissions/new/provisioningInfo.json` (3,0 MB) |
| **A — nasz tenant** | co mozemy nadac dzisiaj | Lokka, SP Graph, `appRoles` + `oauth2PermissionScopes` + RSC |
| **C — dokumentacja** | co Microsoft opisal | sparse clone `microsoftgraph/microsoft-graph-docs-contrib` › `concepts/permissions-reference.md` |
| **B — drugi tenant** | tania kontrola krzyzowa | `merill/microsoft-info` › `_info/GraphAppRoles.csv`, `GraphDelegateRoles.csv` |

**Klonuj, nie pobieraj fetchem.** Pliki maja 180 KB – 3 MB. Narzedzie pobierajace strone streszcza
i ucina: 29 sierpnia 2026 zapytane o `UserAuthMethod-*.Delete.All` w CSV Merilla odpowiedzialo
„nie ma zadnego" — a pelny plik ma wszystkie trzynascie.

### Schemat D

```json
"permissionDeployments": {
  "IdentityDiagnostic.Read": [
    {"id":"f5b84bd9-6ffb-41bf-a2d2-644bcb35a835","scheme":"DelegatedWork",
     "environment":"PPE;public","isHidden":true,"isEnabled":true,
     "resourceAppId":"a57aca87-cbc0-4f3c-8b9e-dc095fdc8978"}
  ]
}
```

`scheme` — `DelegatedWork` / `Application` / `DelegatedPersonal`. `environment` — `public`, `PPE`,
`PPE;public`, `public;FairFax`, czasem puste. `isHidden` — uprawnienie wdrozone, ale nie pokazywane
w portalu. `id` bywa pustym stringiem, wtedy GUID-a stamtad nie bierzesz.
Opisy i czesc GUID-ow: `permissions/permissions-descriptions.json` w tym samym repo.

### Zmierzone 29 sierpnia 2026

- D: **1 885 nazw**, z tego **1 288** `isEnabled` w `public`; **953 widoczne**, **335 tylko ukrytych**.
- A: **1 022** · C: **939** · B: **964** (identyczne z A co do nazwy).
- **D \ A = 306** — tyle Microsoft wdrozyl, a nasz tenant tego nie wystawia. **20 widocznych**
  (m.in. `Zone.Read.All`, `AuditActivity.Read.All`, `Group.Selected`,
  `Policy.ReadWrite.HybridAuthentication`, `AppRegistration.Create`) i **286 ukrytych**.
- `IdentityDiagnostic.Read/.Read.All/.StartDiagnosis/.StartDiagnosis.All` — wszystkie
  `isHidden: true`, `environment: "PPE;public"`, `resourceAppId` = `a57aca87-cbc0-4f3c-8b9e-dc095fdc8978`
  („IAM Supportability").

### Data pojawienia sie liczona z historii gita — to jest `sourceChanged`

Plik dostaje commity „Weekly Permissions sync". `git log -S "<nazwa>" -- permissions/new/provisioningInfo.json`
podaje commit, w ktorym nazwa pojawila sie pierwszy raz. Zmierzone:

- `IdentityDiagnostic` — **2026-02-21**, szesc miesiecy przed tym, jak zglosil to tracker.
- `UserAuthenticationMethod.Delete.All` — **2026-07-17**, miesiac przed trackerem.

To jest data po stronie Microsoftu, wyliczona, nie zgadnieta. Uzywaj jej jako `sourceChanged`
dla wpisow ze zbioru D. Uwaga na opoznienie samego pliku: najnowszy sync z 12 sierpnia 2026 przy
odczycie 29 sierpnia, wiec **D bywa o dwa–trzy tygodnie z tylu wzgledem wlasnego zrodla** — zapisuj
date ostatniego commita razem z danymi.

### Co ktora roznica znaczy

- **D \ A** — wdrozone gdzies w usludze, u nas jeszcze nie. Wpis dostaje
  `kind:"Deployed in the service, not in this tenant"`, `origin:"microsoft"`, `published:null`,
  `dateLabel:"Deployed in the service"`, `deployedSeen` = data z gita, plus `isHidden`,
  `environment`, `schemes`. **Nie liczy sie do „permissions in the catalog"** — tego nie nadasz.
  Dzien, w ktorym nazwa wejdzie do A, jest dniem `b-new`.

  **ALE MUSI ZNALEZC SIE W KATALOGU — to blad, ktory juz raz kosztowal cala funkcje.**
  29 sierpnia 2026 przebieg policzyl `D \ A` = 306, wykluczyl je z licznika „1 037 permissions
  catalogued" — i **nie dopisal ich nigdzie**, bo regula mowila tylko, czym NIE sa. Na stronie
  nie bylo ani jednego `IdentityDiagnostic`, a szukajka w katalogu zwracala `0 of 15`.
  Kazdy wpis `D \ A` idzie do tablicy `graph` z `inInventory:false`, `tracked:true` — dzieki temu
  jest w wyszukiwarce, w filtrze typu zmiany i w trybie *Microsoft changes*, a `inInventory:false`
  trzyma go poza licznikiem katalogu. **Nieobecnosc w tablicy nie jest wykluczeniem z licznika,
  tylko zgubieniem znaleziska.** Licznik ma wlasna, siodma pigulke: `306 deployed, not in this
  tenant`.

  Sprawdzian, ktory ma to lapac: jesli `len(D \ A) > 0`, a zero wpisow w `graph` ma
  `kind:"Deployed in the service, not in this tenant"` — **przebieg NIEUDANY, nie publikuj**.
  Kanarek do recznego sprawdzenia: `IdentityDiagnostic.Read`, `IdentityDiagnostic.Read.All`,
  `IdentityDiagnostic.StartDiagnosis`, `IdentityDiagnostic.StartDiagnosis.All` musza byc
  w katalogu, z `isHidden:true`, `environment:"PPE;public"`, `deployedSeen:"2026-02-21"`
  i GUID-ami z pola `id` mapy D (`f5b84bd9-6ffb-41bf-a2d2-644bcb35a835` dla `.Read`).
- **C \ A** — udokumentowane, nie ma u nas (0 dnia 29 sierpnia).
- **A \ C** — mamy, Microsoft nie opisal (25 dnia 29 sierpnia).
- **B \ A** — inny tenant ma, my nie (0 dnia 29 sierpnia; B odpowiadalo A nazwa w nazwe).

### Czego dalej nie widzimy — i tego nie zmyslaj

Nazwa, ktorej nie ma w zadnym z D, A, B, C, jest poza zasiegiem tego raportu. Trafia do
`notPublished.watchlist` z `trackerSeen`, `checkedIn:["D","A","B","C"]` i data. **GUID-a nie
przepisujesz z ekranu trackera.** 29 sierpnia 2026 tracker podawal dla `IdentityDiagnostic.Read`
delegowane `3839e465-e636-4c8e-b959-340182fb0567`; tego GUID-a **nie ma nigdzie w repozytoriach
Microsoftu** — `provisioningInfo.json` podaje dla tej nazwy `f5b84bd9-6ffb-41bf-a2d2-644bcb35a835`.
Bierz `id` z D albo z odczytu SP; gdy `id` jest puste, zostaw pole i napisz dlaczego.

Sekcja Sources niesie jedno zdanie z data: *„Mapa wdrozen Microsoftu (sync <data commita>): D=1885,
z tego 1288 wlaczonych w public. Nasz tenant: A=1022. Dokumentacja: C=939. Roznica D\A = 306, w tym
20 widocznych."* Katalog, ktory nie mowi, czego nie widzi, klamie cisza.

## 5e. „Nieudokumentowane u Microsoftu" — znacznik, filtr i kafelek

To dotyczy TAK SAMO uprawnien jak i rol. Zmierzone 29 sierpnia 2026:

| obiekt | w usludze | udokumentowane | **nieudokumentowane** |
|---|---|---|---|
| uprawnienia Graph | A = 1 022 | C = 939 | **25** |
| role katalogowe Entra | 145 (`roleDefinitions`, v1.0 i beta identycznie) | 138 naglowkow `##` | **3** |

Te trzy role to `Entra SOC Identity Responder`, `Entra Customer Lockbox Approver`
i `On Premises Directory Sync Account` — zadna nie wystepuje w pliku dokumentacji ani razu.

### Ktory dokument jest oficjalny — na obiekt, nie na raport

| `objectType` | oficjalne zrodlo dokumentacji | plik do sparsowania |
|---|---|---|
| `Permission`, `Permission scope`, `Endpoint` (Graph) | `learn.microsoft.com/graph/permissions-reference` | `microsoftgraph/microsoft-graph-docs-contrib` › `concepts/permissions-reference.md` |
| `Role`, `scope: "Entra directory role"` | `learn.microsoft.com/entra/identity/role-based-access-control/permissions-reference` | `MicrosoftDocs/entra-docs` › `docs/identity/role-based-access-control/permissions-reference.md` |
| `Role`, `scope: "Azure RBAC"` | `learn.microsoft.com/azure/role-based-access-control/built-in-roles` | ta sama strona, pobrana i sparsowana |

Stan uslugi dla rol czytasz z `GET /v1.0/roleManagement/directory/roleDefinitions`
(`$select=displayName,description,isBuiltIn,isEnabled,templateId`, **bez `fetchAll`** — z nim Lokka
zwraca `Invalid array length`). To jest zbior A dla rol. **`description` jest obowiazkowe w `$select`**:
31 sierpnia 2026 odczyt mial zero opisow na 145 rolach wylacznie dlatego, ze pola nie zazadano,
a dla roli nieobecnej w dokumentacji to zdanie jest jedynym tekstem, jaki Microsoft o niej publikuje.

### Jak sprawdzasz, zeby nie klamac

**Szukaj w calym pliku dokumentacji, nie w naglowkach.** Naglowki `##` daja 138 rol, ale sekcja
`Roles not shown in the portal` opisuje kolejne w tabeli, bez wlasnego naglowka. Liczenie po
naglowkach dawalo **12** rzekomo nieudokumentowanych; po calym pliku zostaja **3**.

**Normalizuj nazwe przed werdyktem** — bez tego zglosisz zmiane nazwy jako nowosc:
porownanie bez rozroznienia wielkosci liter (`Customer LockBox` = `Customer Lockbox`) plus mapa
aliasow, dzis jeden wpis: `Azure AD Joined Device Local Administrator` =
`Microsoft Entra Joined Device Local Administrator`. Kazdy nowy alias dopisujesz do
`docAliases` w katalogu razem z data i powodem.

### Pola, ktore to niosa

Kazdy wpis inwentarza — uprawnienie i rola — dostaje:

```json
"docStatus": "documented | undocumented | not-in-tenant",
"docSource": "<URL oficjalnej strony dla tego objectType>",
"docCheckedOn": "YYYY-MM-DD",
"serviceStatus": "in-tenant | deployed-elsewhere"
```

`docStatus: "undocumented"` = jest w usludze u nas, nie ma w oficjalnym dokumencie.
`"not-in-tenant"` = zbior `D \ A` z sekcji 5d, wiec i tak nieudokumentowane, ale niedostepne.

### Znacznik, filtr i kafelek — bez przerabiania powloki

1. **Znacznik w katalogu i filtr dostajesz z `kind`.** Katalog renderuje `kind` jako chip i ma
   filtr po typie zmiany, wiec dwie nowe wartosci daja jedno i drugie za darmo:
   `New in service, not yet documented` oraz `Deployed in the service, not in this tenant`.
   **Nie dopisuj wlasnego `<select>`** — skrypt 3 buduje liste filtra z wartosci, ktore zastanie.
2. **Kafelek liczy pigulka w naglowku — pozycja DRUGA i TRZECIA**, sekcja 1:
   `<a class="count" href="#graph"><b>28</b> undocumented at Microsoft<span>&middot; 25 permissions, 3 roles</span></a>`
   oraz `<a class="count" href="#graph"><b>364</b> deployed, not in this tenant<span>&middot; 73 visible, 291 hidden</span></a>`.
   Licznik sumaryczny, rozbicie w `<span>`. Zero to poprawna wartosc i tez sie pokazuje.
   **Dodatkowo `<p class="sec-note">` sekcji `graph` i `roles` otwiera sie tymi samymi liczbami** —
   kafelek siedzi w Overview, a czytelnik patrzy na panel katalogu i tam ma je zobaczyc.
3. **Kolor chipa bierze sie z mapy w skrypcie, nie z CSS.** `badge(text, cls)` w skrypcie 3 czyta
   `KIND_BADGE[text]`, a przy braku klucza spada na `"b-prod"` — zwykly szary. 30 sierpnia 2026
   wszystkie 364 wpisy `Deployed in the service, not in this tenant` i 16 `New in service, not yet
   documented` byly szare wylacznie z tego powodu. **Dopisz do `KIND_BADGE` szesc kluczy. Tylko
   klucze: nie zmieniasz istniejacego wpisu i nie ruszasz zadnej innej linii tego skryptu.**

   ```js
   "New in service, not yet documented": "b-undoc", "Undocumented at Microsoft": "b-undoc",
   "No longer documented": "b-undoc", "Deployed in the service, not in this tenant": "b-elsewhere",
   "No longer in the service": "b-dep", "Documented at Microsoft": "b-upd"
   ```

   To jedna z DWOCH dozwolonych zmian w skryptach powloki (druga sa trzy linie `facetCandidates()` z §5w) i jest to zmiana danych, nie logiki.
4. **Dwie klasy znacznikow dopisujesz na koncu `<style>`** — razem z blokiem mobilnym z sekcji 1a
   sa to jedyne dozwolone dopisane reguly CSS. Zbudowane ze zmiennych, ktore arkusz juz ma
   (`--warn`, `--warn-soft`, `--accent`, `--accent-soft`), wiec oba motywy dzialaja same:

   ```css
   .badge.b-undoc{background:var(--warn-soft);color:var(--warn);border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--warn)}
   .badge.b-elsewhere{background:var(--accent-soft);color:var(--accent);border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--accent)}
   .cc-row:has(.badge.b-undoc){box-shadow:inset 3px 0 0 var(--warn)}
   .cc-row:has(.badge.b-elsewhere){box-shadow:inset 3px 0 0 var(--accent)}
   ```

   Szesc istniejacych znacznikow to prostokaty bez obwodki — zaokraglenie i obwodka sa jedynym, co
   odroznia te dwa na pierwszy rzut oka, i o to prosil wlasciciel. `:has()` daje jeszcze kolorowy
   pasek na krawedzi wiersza listy; w przegladarce bez `:has()` paska po prostu nie ma, reszta dziala.
5. **Rola nieudokumentowana ma `kind:"Undocumented at Microsoft"`.** 30 sierpnia 2026 trzy takie role
   dostaly `New in service, not yet documented` — wartosc Graphowa — i filtr w katalogu rol nie mial
   pozycji, ktorej wlasciciel szukal. Wartosci graphowe zostaja przy Graphie.
6. **Wykresu nie musisz dotykac.** Skrypt 2 buduje `By change type` z `msChanged` grupowanego po
   `kind`, wiec kazda nowa wartosc jest slupkiem sama z siebie. 30 sierpnia 2026 slupkow bylo
   384 = 364 + 13 + 5 + 2 i zgadzalo sie to z pigulka. Nie dopisuj wlasnego wykresu.

### Kiedy ramka znika

Sama, w przebiegu, w ktorym nazwa pojawi sie w oficjalnym dokumencie. `docStatus` przechodzi na
`documented`, wpis dostaje rekord zmiany `kind:"Documented at Microsoft"`, `origin:"microsoft"`,
`changed` = data tego przebiegu, i wchodzi do `changeSummary.modified`. **To jest ruch Microsoftu,
nie nasz** — nigdy `origin:"brief"`. Odwrotnie tez: nazwa, ktora znika z dokumentacji, wraca na
`undocumented` z rekordem `No longer documented`.

Sekcja Sources niesie zdanie: *„Nieudokumentowane u Microsoftu: 25 uprawnien z 1 022 w usludze
(dokumentacja: 939) i 3 role ze 145 (dokumentacja: 138), sprawdzone <data>."*

## 5f. Inne API i statystyki na powierzchnie

Graph to nie cala powierzchnia uprawnien. Blada *Request API permissions* w portalu wymienia
kilkanascie innych resource API; nadanie na ktorymkolwiek siega danych tenanta i **nie widac go
w raporcie uprawnien Graph**. Katalog wozi tablice `apis` — po jednym wpisie na powierzchnie:
`name`, `description`, `status` (`inventoried`/`queued`), `permissions`, `url`, `socNote`, a przy
`queued` takze `queuePosition` i `targetDate`.

Kolejnosc: **Office 365 Management APIs** (powierzchnia logow audytu dla SOC), **Exchange Online**
(`full_access_as_app` = odczyt wszystkich skrzynek), **Azure Service Management**
(`user_impersonation` na plaszczyznie sterowania), **SharePoint** (stare nadania ACS app-only sa
poza raportowaniem zgod Graph), dalej Intune, Power BI, Dynamics CRM, Azure DevOps, Purview,
Power Automate, Azure Storage, Azure RMS, Azure Data Explorer.

**Jedno API z kolejki na przebieg, a „scheduled" musi nazwac dzien.** Pozycja N jest na N-ty dzien
roboczy po dacie raportu; powloka renderuje **scheduled · #N in the queue · due 26 Aug**, nigdy
golego myslnika. Kazdy przebieg bierze #1, inwentaryzuje, ustawia `status:"inventoried"` z realna
liczba w `permissions`, dopisuje jego uprawnienia do tablicy `graph` z `surface` nazywajacym API
i przelicza pozostale terminy. **Te wpisy sa `origin:"catalog"`, `kind:"Newly inventoried"`,
`published:null` — nigdy nowe u Microsoftu.** Do czasu inwentaryzacji zostaje `queued`: uczciwa
kolejka bije zmyslona liste, i **nigdy nie wymyslasz nazwy uprawnienia dla powierzchni, ktorej
nie przeczytales**. Powierzchnia stojaca na #1 po terminie pokazuje, ze przebieg obiecal date
i jej nie dotrzymal — i tak ma byc.

Kazda `inventoried` powierzchnia wozi `counts` (`total`, `delegated`, `application`, `both`, `rsc`),
poprzedni odczyt w `previous`/`previousChecked` i `delta`. Kazdy przebieg: przelicz od nowa;
przepisz `counts`→`previous` i `checked`→`previousChecked` PRZED nadpisaniem; ustaw `checked` na
dzis; policz `delta` pole po polu. **Niezerowa delta to znalezisko, nie statystyka** — zrob roznice
zbiorow nazw i napisz rekord `New at source` albo `No longer listed at source` dla kazdej.
Przesuniety total bez rekordu zmiany znaczy, ze przebieg zrobil arytmetyke i pominal robote.
Bez zmian → same zera i „no change", co warto opublikowac: to datowane stwierdzenie, ze ktos
sprawdzil. Pierwszy przebieg dla powierzchni: `previous` null, „baseline", poprawne dokladnie raz.

**Nigdy nie ustawiaj `complete:true` dla listy, ktorej nie przeczytales w calosci**, i nie pozwol
`published` odjechac od liczby Microsoftu. Niepelny inwentarz, ktory to mowi, jest uzyteczny;
taki, ktory udaje komplet, kaze czytelnikowi wywnioskowac, ze uprawnienie nie istnieje.

## 5g. Wersjonowanie wpisow katalogu

Versioning rules, every run:

- **Unchanged entry** — copy forward byte for byte. Do not touch `version`, `lastChanged`, `history`.
- **Changed entry** — bump `version`, `lastChanged` = today, append `{"v":<new>,"date":"<today>","note":"<what changed, concretely>"}` to `history`, old value into `before`/`privilegedBefore` so the UI strikes it through.
- **New entry** — `version:1`, `firstSeen`/`lastChanged` today, one history line.
- **`rolesVersion`/`graphVersion`** — bump by 1 when any entry in that list was added or bumped this run, else leave alone. `baselineDate` never changes after the first run.
- `apiVersion` is Microsoft's surface (`beta` / `v1.0`), stated only when the page states it; `version` is this catalog's item revision. Never conflate them.
- **`kind` must be actionable without explanation.** Listed values only; never coin metaphorical jargon ("blast radius grew" is unlookuppable). `Existing permission gained reach` = an already-consented permission that can now do something new — no consent prompt fires, so nothing in the audit trail marks it. Say so in the section's `<p class="sec-note">`.
- `kind` names WHAT changed, never whether it is dated. A role on the reference but absent from every what's-new log gets `kind:"Undated at source"`, `changed:null`, a `dateNote`. Never "New role" on a guess.
- Never bump a version to look busy. A quiet catalog is a correct result and the UI says so.

Message Center: your tenant's own MC is unreachable here. Use https://mc.merill.net (RSS https://mc.merill.net/rss.xml) and footnote MC items "vary by tenant — confirm in your own tenant".

Slownik `kind` jest ZAMKNIETY, a walidator przebiegu odrzuca wartosc spoza listy — dlatego nowe
stany musza byc w nim wymienione, inaczej znalezisko wypada po cichu. Graph dokladamy:
`New in service, not yet documented`, `Deployed in the service, not in this tenant`,
`No longer in the service`, `Documented at Microsoft`, `No longer documented`.
Role dokladamy: `Undocumented at Microsoft`, `Documented at Microsoft`, `No longer documented`.
**Oba katalogi musza je przyjmowac** — chip przy wpisie i filtr typu zmiany powstaja z zastanych
wartosci `kind`, wiec to stad bierze sie filtr „nieudokumentowane" i „wdrozone gdzie indziej",
dla rol tak samo jak dla uprawnien.

## 5h. Kontrola Playwright — pelna lista asercji

Render headless at 1500x1000 in light AND dark and assert — every one of these has caught a real regression: no console or page errors; exactly one visible `.tabpanel`; `nav.anchors .tab` is 9, labels human, strip not overflowing, also at 1280px; **`header.top .hdr-tools` holds the Theme button and a `select.globalfilter` whose first option is `All products`, and every `header.top .counts a.count` is mirrored into a `#tab-overview .stat` tile**; **every panel except Overview and Sources has exactly one `.panelhead`, built by the script, carrying ≥1 `.stat` and ≥1 `figure.chart`**; **every panel that lists a deadline inside 60 days shows a `🔥 under 30 days` or `⚠️ 30–60 days` chip — absent means the rows lack the emoji**; **`.badge` count across the page is in the hundreds, not the tens**; a picks product chip leaves only that product's rows, raises a `.filterbanner`, Clear filter restores them; **`.filterbanner[hidden]` computes to `display:none`, and with a filter active the banner is visible with a non-empty `.fb-msg`**; **`.cat-controls` is `position:sticky` at desktop width and the search input stays in the viewport after scrolling `.cat-split` into view**; both catalogs render a non-zero count and three modes — Microsoft changes / Catalog notes / All — defaulting to the first with no `catalog`/`brief` entry in it; **`.badge.b-undoc` and `.badge.b-elsewhere` both have a non-transparent background and a non-zero `border-radius` in both themes, and each is carried by at least one rendered chip**; **every `input.tbar-search` and `.cat-searchwrap .cat-search` has a non-transparent, non-`--surface` background in both themes; `.cat-changed` scrollHeight may exceed its clientHeight but `.cat-searchrow` is within 480 px of the panel top; `details.foldnote>summary` computes a font-size of at least 14 px; `.card-title` has a non-transparent background and a non-zero border-radius; every open `details.foldnote` body contains a `ul` and no bare `p` over 40 words**; `scrollWidth` never exceeds client width; **open a role with actions: the action table holds exactly as many rows as `actionsFull`, the count line carries the provenance sentence, `.cp-privbtn` filters to privileged-only with `aria-pressed="true"` and toggles back, and `.cp-verify` links a real `entra-docs/blob/main/.../includes/<slug>.md` URL**. Skip this step rather than failing the run if Playwright is missing.

Nowe od 31 sierpnia 2026, kazda z nich lapie realny blad z tego dnia: **zaden `figure.chart`
o co najmniej czterech slupkach nie ma wszystkich slupkow rownych 1** (wykres „By topic" mial ich
dziesiec i wlasciciel nie mial z niego nic); **kazdy `.sec-body a[href^="http"]` ma niezerowy
`border-radius` i nieprzezroczyste tlo w obu motywach, i takich kotwic jest co najmniej sto**;
**zaden `.lnk-dead` nie jest kotwica** (`querySelectorAll("a.lnk-dead").length === 0`);
**kazdy `#tab-products .sec-body h3` ma nieprzezroczyste tlo i `border-radius` niezerowy**;
**suma wierszy tabel deep dive rowna sie liczbie z jego `sec-note`**, a `sec-note` kazdej tabeli
produktu zawiera liczbe pozycji okna (sekcja 5u).

Dodatkowo przy **390x844** (telefon): `getComputedStyle(document.querySelector("header.top")).position`
zwraca `static`; `.counts` miesci sie w jednym wierszu; po `window.scrollBy(0,600)` naglowek jest
poza widokiem (`getBoundingClientRect().bottom < 0`); **`.cat-controls` ma `position:static`, a po
przewinieciu listy katalogu prostokat paska szukania nie przecina sie z prostokatem pierwszego
wiersza wynikow** — to jest asercja, ktorej brak przepuscil blad kaskady z sekcji 1a; **pierwsze trzy
`.counts a.count` to kolejno terminy, `undocumented at Microsoft` i `deployed, not in this tenant`**.
I jeszcze: wpisanie `IdentityDiagnostic` w szukajke katalogu Graph w trybie **All** zwraca co
najmniej cztery wiersze — zero znaczy, ze mapa wdrozen nie trafila do danych.

## 5i. Weryfikacja licznika akcji roli — zrodlo i przeliczenie

Ta sekcja jest wiazaca dla obu taskow i obu routines; prompty na nia wskazuja zamiast ja powtarzac.

Learn builds each role's Actions table from one file per role in Microsoft's public docs repo.
**Clone it, do not fetch it:** `git clone --depth 1 --filter=blob:none --sparse
https://github.com/MicrosoftDocs/entra-docs` then `git sparse-checkout set
docs/identity/role-based-access-control` gives `permissions-reference.md` and the `includes/` files
as plain files. A `microsoft_docs_fetch` of that ~400 KB page spills its oversized result into a file
under `/root/.claude/`, and every later shell command naming that path raises its own approval
prompt, which a scheduled run has nobody to answer. Print every `## <Role>` heading with the
`[!INCLUDE …]` path under it — Microsoft's own name-to-file mapping, 132 files on 27 Aug 2026, and
the source of `actionsSource.github`. **Never construct that path from a guessed slug**; a 404 in the
verify box is worse than no verify box. For at least one role each run, diff the include file's table
against your parse and set `checked` only where that diff ran and came back empty.

**Do not "fix" the count to match a third-party site.** Microsoft prints what it prints — Agent ID
Administrator, 64 rows on 27 Aug 2026, matching its source file row for row; 66 is 64 plus the
markdown header and separator lines, so drop them. Where a third-party figure is higher, name the
reason in `actionsProvenance` and add the live `roleDefinition` to `notPublished.roles`.
**Count in code, never trust a summary's arithmetic** — one pass reported 57 rows for a 64-row file.

On 27 Aug 2026: 133 `##` sections, 1,992 rows — one section, `Roles not shown in the portal`, is a
page note, not a role: **exclude it**, leaving 132 roles, 1,959 actions, 33 PRIVILEGED, 5 with an
`appliesTo` table.

**What Microsoft does NOT publish for a role, and what this brief therefore does not print:** a
role-to-Graph-permission mapping, an attack-path narrative, and an assignment mode for every role.
Sites showing those compiled them by hand and say so. Carry them in `notPublished.roles` and render
them, so the absence is stated rather than left for the reader to guess at.

## 5j. Opis kazdego wpisu — albo zdanie, dlaczego go nie ma

31 sierpnia 2026 panel `IdentityDiagnostic.Read.All` pokazywal identyfikator uprawnienia i nic wiecej:
zadnego display text, zadnego opisu. Tak samo nowe role. Puste pole nie mowi czytelnikowi, czy Microsoft
nic nie napisal, czy przebieg nie zajrzal.

**Zrodla opisu dla uprawnienia, w tej kolejnosci:**

| zrodlo | pola |
|---|---|
| **A — service principal / CSV Merilla** | `appRoles`: `displayName`, `description`; `oauth2PermissionScopes`: `adminConsentDisplayName`, `adminConsentDescription`, `userConsentDisplayName`, `userConsentDescription` |
| **C — dokumentacja** | `DisplayText` i `Description` per typ, z tabeli permissions-reference |
| **D — mapa wdrozen** | `permissions/permissions-descriptions.json` w repo devx: `delegatedScopesList` (598 wpisow) i `applicationScopesList` (534), pola `adminConsentDisplayName`, `adminConsentDescription`, `consentDisplayName`, `consentDescription`, `id`, `isEnabled`, `value` |

Zmierzone 31 sierpnia 2026: plik opisow zna **716 unikalnych nazw**; z 1 885 nazw zbioru D **708 ma opis,
a 1 177 nie ma** — i wszystkie cztery `IdentityDiagnostic.*` sa w tych 1 177. Czyli akurat tam pustka byla
uczciwa, ale strona musi to powiedziec.

Kazdy wpis niesie `displayText`, `descriptionByType` oraz `descriptionSource`:
`service` | `docs` | `deployment-map` | `none`. Przy `none` panel drukuje zdanie, nigdy puste pole:
*„Microsoft nie publikuje opisu tego uprawnienia — sprawdzone w service principalu, w permissions-reference
i w permissions-descriptions.json dnia <data>."* Rola bierze opis z `description` w `roleDefinitions`
(sekcja 5e — pole musi byc w `$select`).

Walidator odrzuca przebieg, w ktorym wpis nie ma ani niepustego `descriptionByType`, ani
`descriptionSource:"none"` z data `docsChecked`.

## 5k. Czytelnosc — cztery reguly CSS i jedna redakcyjna

Zmierzone w arkuszu z 31 sierpnia 2026: `details.foldnote>summary` ma 13 px i `var(--muted)`, a plusik
`::before` 17 px — wlasciciel zglosil, ze nie da sie tego dostrzec. `.card-title` to goly tekst 15,5 px
bez ramki. `.cat-changed` renderuje cala tabele zmian NAD paskiem szukania, wiec w zakladce Graph API
trzeba przewinac ~25 wierszy, zeby dojsc do wyszukiwarki.

Cztery reguly dopisujesz na koncu `<style>`, razem z blokiem mobilnym z sekcji 1a i znacznikami
z sekcji 5e. Wygrywaja, bo sa ostatnie — ta sama zasada kaskady:

```css
.cat-changed{max-height:min(58vh,430px);overflow:auto;overscroll-behavior:contain}
details.foldnote>summary,details.cb-more>summary,details.cov-more>summary{font-size:14.5px;font-weight:600;color:var(--text)}
details.foldnote>summary::before,details.cb-more>summary::before,details.cov-more>summary::before{width:22px;height:22px;flex-basis:22px;font-size:15px;background:var(--accent-soft);border-color:var(--accent)}
.card-title{display:inline-block;background:var(--accent-soft);color:var(--text);border:1px solid var(--accent);border-radius:10px;padding:6px 11px}
.tbar-search,.cat-searchwrap .cat-search{background:var(--ok-soft);border-color:var(--ok);border-width:1.5px;font-weight:500}
.tbar-search::placeholder,.cat-searchwrap .cat-search::placeholder{color:var(--muted);font-weight:400}
.tbar input.tbar-search:focus,.cat-searchwrap .cat-search:focus{background:var(--surface);box-shadow:0 0 0 3px var(--ok-soft)}
.cat-searchicon{color:var(--ok)}
```

**Pole szukania ma byc zielone i wygladac tak samo wszedzie.** Powloka daje katalogowi `.cat-search`
z akcentem i lupka, ale tabelom `.tbar-search` na zwyklym `--surface` — i wlasnie ono ginie na stronie,
co zglosil wlasciciel 31 sierpnia 2026. Cztery reguly wyzej robia z obu pol jeden system: zielone tlo
`--ok-soft`, obwodka `--ok`, po kliknieciu tlo wraca na `--surface` z zielonym pierscieniem. Zielen jest
w arkuszu (`--ok`, `--ok-soft`) i dziala w obu motywach, wiec nie dodajesz zadnej nowej zmiennej.

`.cat-changed` nie traci ani jednego wiersza — przewija sie we wlasnym pudelku zamiast spychac pasek
szukania poza ekran. Prawdziwe zwijanie pod `+` wymagaloby dopisania kodu budujacego DOM do skryptu 3,
a tego przebieg bez nadzoru robic nie powinien: dozwolona zmiana w skryptach zostaje jedna, mapa
`KIND_BADGE` z sekcji 5e.

**To, co siedzi pod `+`, jest lista punktowana, nigdy proza.** Cialo kazdego `details.foldnote` to
`<ul><li>`, jeden fakt na punkt, ponizej ~25 slow, najwyzej siedem punktow. Tak samo `sec-note` dluzszy
niz dwa zdania i karta, ktorej What / Why / Action przekracza trzy linijki. Rozwijany akapit jest
najczestsza skarga na te strone: czytelnik otwiera go po fakt, a dostaje wypracowanie.

## 5l. Historia KQL zyje w repozytorium, nie na stronie

Zapytania z sekcji Hunting rosna z kazdym dniem i strona nie jest miejscem na ich archiwum. Kazdy
przebieg zapisuje kazde opublikowane zapytanie jako osobny plik:

```
site/kql/RRRR-MM-DD-<slug>.kql
site/kql/index.json
```

Naglowek pliku `.kql` to komentarze `//`: `title`, `date`, `product`, `tables` (lista tabel, ktore
zapytanie rusza), `purpose` (jedno zdanie), `source` (URL strony ze schematem). `index.json` to tablica
`{file, title, date, product, tables, purpose}` — po to, zeby dalo sie szukac po tytule i po tabeli bez
otwierania plikow. Sekcja Hunting linkuje kazde zapytanie do jego pliku, a naglowek sekcji do
`index.json`.

Zapytanie identyczne z wczorajszym **nie dostaje nowego pliku** — dopisujesz mu w `index.json` date
w polu `reused` i tyle. Inaczej katalog w tydzien zamieni sie w kopie tego samego zapytania.
Tytul jest zdaniem, ktore mozna wyszukac: `Sign-ins from a new ASN for privileged roles`, nigdy
`Query 3`. Katalog `site/kql/` mieści sie w `site/`, wiec nie lamie zasady 1.

## 5m. Today i New to DWA ROZNE ZBIORY, nie dwie kopie tego samego

31 sierpnia 2026 wlasciciel wpisal `account` w wyszukiwarke w zakladce **Today** i dostal jeden wiersz
(Teams), a ten sam wpis — MC o przeniesieniu My Account na `myaccount.cloud.microsoft` — byl w zakladce
**New**. Wyglada to na zgubiony rekord, a nie jest: pole szukania w Today stalo w sekcji *Pick of the day*,
ktora z definicji ma **jeden wiersz na produkt**, wiec przeszukiwal 19 wierszy, nie 105. Strona tego nie
mowila, wiec czytelnik ma prawo sadzic, ze czegos brakuje.

**Definicje, ktore obie zakladki musza wypowiedziec wprost:**

| zakladka | populacja | ile | czym jest |
|---|---|---|---|
| **Today** | wybor redakcyjny z dzisiejszego przebiegu | Top N (7) + jeden wiersz na produkt + lista zmian | „co bym dzis podniosl" — zawsze podzbior |
| **New** | KOMPLET okna 14 dni | wszystko, jeden wiersz na pozycje | rejestr, nic nie jest wycinane |

Zasady:

1. **Kazda sekcja Today otwiera sie zdaniem, ktore nazywa podzbior**: *„Wybor 19 z 105 pozycji okna —
   pelna lista jest w zakladce New."* Liczby prawdziwe, nie okragle.
2. **Kazda pozycja w Today istnieje w New z tym samym `id`.** Wpis w Today, ktorego nie ma w New, to blad
   danych i STEP 4 go odrzuca.
3. **Duplikat to nie problem, ukryty duplikat jest.** Ten sam element MOZE byc w Top N, w Pick of the day
   i w New — to trzy rozne pytania o ten sam fakt. Ale wiersz Today linkuje do swojego wiersza w New
   (`href="#new"` plus `id` pozycji), zeby czytelnik mial dojscie do pelnego rekordu.
4. **Okna czasu znacza co innego w kazdej z nich i tak sa opisane.** Pick of the day ma kolumne `Deadline`,
   wiec powloka daje mu okno „Due in" — to jest termin, nie data publikacji. New ma `Published`, wiec
   dostaje okno publikacji. Zdanie sekcji mowi ktore to okno; bez tego dwa identycznie wygladajace paski
   sugeruja, ze jedna zakladka jest niepelna kopia drugiej.

## 5n. Tytul Microsoftu zostaje na stronie, razem z numerem MC

Nasze naglowki sa przepisywane na „co sie zmienilo" — `My Account and identity self-service move to
myaccount.cloud.microsoft` zamiast oryginalnego `Microsoft Entra: Domain update for My Account and identity
self-service experiences`. Dla skanowania to lepsze i zostaje. Ale czytelnik, ktory chce znalezc ten sam
wpis w Message Center albo u agregatora, nie ma czego wyszukac.

Dlatego kazda pozycja stanu niesie OBA pola:

- `title` — nasz naglowek, czasownikowy, mowiacy co sie zmienia;
- `officialTitle` — **tytul Microsoftu przepisany co do znaku**, nigdy skrocony i nigdy przeredagowany;
- `reference` — `MC…` / `RM…`, albo doslowne `no MC/RM post — Learn only`.

Render: w komorce nazwy nasz tytul pogrubiony, a pod nim `officialTitle` mniejszym, wyciszonym tekstem —
to samo miejsce, gdzie dzis stoi obszar (`Entra Connect / Cloud Sync`). **Tabela New dostaje kolumne
`Reference` z numerem MC/RM**; 31 sierpnia 2026 jej nie miala, przez co jedynym miejscem z numerem byla
zakladka Today. Nigdy nie wymyslasz numeru: brak posta to `no MC/RM post — Learn only`, nie puste pole.

## 5o. Podzial na miesiace tam, gdzie ma sens

Wlasciciel wskazal `updates.getcurrent.cloud/by-service`, gdzie lista jest grupowana naglowkami
miesiecy z licznikiem. Robimy to samo, ale tylko tam, gdzie zakres naprawde obejmuje wiecej niz jeden
miesiac:

- **New** — okno ma 14 dni, wiec zwykle sa to dwa miesiace na przelomie. Grupuj naglowkiem
  `<tr class="grp"><td colspan="N"><b>Sierpien 2026</b> (10)</td></tr>` tylko wtedy, gdy okno przecina
  granice miesiaca; w przeciwnym razie zadnych naglowkow.
- **Deadlines** — zakres 60 dni zawsze przecina co najmniej dwa miesiace, wiec grupowanie jest tu stale.
- Naglowek grupy to zwykly wiersz tabeli, wiec sortowanie kolumny go rozsypie. **Dlatego grupy dodajesz
  tylko do tabel, ktore nie maja `th.sortable`**, albo — prosciej i bezpieczniej — dajesz kazdemu miesiacowi
  osobne `<div class="tw"><table>` z wlasnym `<caption>`. Druga droga jest domyslna: nie psuje sortowania,
  nie wymaga zmian w skryptach i wyglada dokladnie jak wzor.

## 5p. Top N wazy sie bezpieczenstwem, nie funkcjonalnoscia chmury

31 sierpnia 2026 w Top 7 trafil element o funkcji sieciowej Azure. Wazny, ale nie dla SOC-a, ktory
czyta te strone rano. Kolejnosc wagi, od najwyzszej:

1. **Tozsamosc** — Entra ID, Conditional Access, metody uwierzytelniania, PIM, Identity Protection, role.
2. **Wykrywanie i reakcja** — Defender XDR, MDE, MDI, MDO, MDCA, Sentinel: nowe detekcje, zmiany schematu
   hunting, retencja, zmiany w alertach.
3. **Dane i zgodnosc** — Purview: DLP, audyt, retencja, Insider Risk.
4. **Zarzadzanie punktem koncowym** — Intune: baseline'y, compliance, ASR, szyfrowanie.
5. **Powierzchnia dzierzawy** — M365 admin, Exchange Online, SharePoint, Teams: zgody, uprawnienia,
   udostepnianie zewnetrzne, przeplyw poczty.
6. **Windows i cykl zycia** — konce wsparcia, wymuszone upgrade'y.
7. **Azure** — **tylko wtedy**, gdy zmiana rusza kontrole bezpieczenstwa, zrodlo logow albo granice
   tozsamosci. Sama funkcja platformy (nowy SKU zapory, region, opcja wydajnosci) nie jest materialem
   na Top N, choc moze byc w New.

Kryterium rozstrzygajace, gdy dwa elementy waza podobnie: **czy SOC musi cos zrobic albo cos przeoczy?**
Termin w 30 dniach, wymagana akcja administratora, zmiana domyslna wlaczana bez zgody, nowe uprawnienie
o zasiegu dzierzawy, wycofanie zrodla logow — to bije kazda nowosc funkcjonalna. Sekcja Top N mowi w
`sec-note`, wedlug czego wazyla, zeby wybor dalo sie zakwestionowac.

## 5q. „Znalezione dzis" musi dac sie odroznic od „znalezionego dwa dni temu"

31 sierpnia 2026 wlasciciel otworzyl `IdentityDiagnostic.Read` i zobaczyl `PUBLISHED BY MICROSOFT:
not dated by Microsoft` oraz `FIRST TRACKED: 31 Aug 2026`. Cztery wpisy wygladaly identycznie jak 364
znalezione dzien wczesniej. **Pytanie „co przybylo dzisiaj" nie ma w tym UI odpowiedzi** — i to nie jest
kwestia wygladu, tylko dat w danych.

**Przyczyna: selektor okresu filtruje po dacie Microsoftu, a ta jest `null`.** Przy `changed: null`
wpis wypada z kazdego okna procz `ALL` i laduje na koncu sortowania. 364 + 16 wpisow bez daty to jeden
nierozroznialny blok.

**Naprawa jest po stronie danych, nie skryptu.** Kazdy wpis niesie trzy rozne daty i zadna nie zastepuje
pozostalych:

| pole | co znaczy | skad |
|---|---|---|
| `changed` / `published` | data Microsoftu | tylko to, co Microsoft wydrukowal |
| `deployedSeen` | kiedy Microsoft wdrozyl nazwe | `git log -S` w mapie wdrozen — **to JEST data Microsoftu**, wyliczona, nie zgadnieta |
| `firstTracked` | kiedy TEN raport zobaczyl wpis pierwszy raz | data przebiegu |

1. **Dla wpisow `D\A` ustaw `changed = deployedSeen`.** To data po stronie Microsoftu, wiec wolno ja tam
   wpisac — i dopiero wtedy selektor okresu, sortowanie i wykres zaczynaja dzialac dla tych 364 pozycji.
   Bez tego caly zbior jest „nie datowany" i nie da sie go przefiltrowac. Panel szczegolow pokazuje obie:
   *„Wdrozone u Microsoftu 21 lutego 2026 · po raz pierwszy w tym katalogu 31 sierpnia 2026."*
2. **`firstTracked` jest obowiazkowe na kazdym wpisie** i nigdy sie nie zmienia po pierwszym zapisie.
3. **Katalog wozi `discoveries`** — tablica `{date, graphNew, graphDeployed, rolesNew, rolesUndocumented,
   note}`, jeden wpis na przebieg, ktory cos znalazl. Sekcje `graph` i `roles` otwieraja `sec-note`
   ostatnimi trzema wierszami tej tablicy: *„31 sierpnia: 4 nowe wdrozone gdzie indziej, 13 nowych
   w usludze. 30 sierpnia: 364 wdrozone gdzie indziej, 16 nowych w usludze. 29 sierpnia: baseline."*
   To jest jedyne miejsce, ktore odpowiada na pytanie „co przybylo dzis" bez klikania w filtry.
4. **Chip `NEW TODAY`** przy wpisie, ktorego `firstTracked` = data dzisiejszego przebiegu. Klasa
   `b-new` juz istnieje i jest zielona, wiec nie dodajesz CSS — dopisujesz tylko drugi znacznik obok
   znacznika `kind`, tekstem `New today`.
5. **Sortowanie listy katalogu:** najpierw `firstTracked` malejaco, potem `changed` malejaco. Dzisiejsze
   znaleziska sa na gorze, zawsze, niezaleznie od tego jak stara jest data Microsoftu.

Walidator: kazdy wpis ma `firstTracked`; kazdy wpis `kind:"Deployed in the service, not in this tenant"`
ma niepuste `deployedSeen` ORAZ `changed` rowne `deployedSeen`; `discoveries` ma wpis z data dzisiejszego
przebiegu, gdy cokolwiek doszlo, i nie ma go, gdy nic nie doszlo.

## 5r. Kazdy link jest sprawdzany w kazdym przebiegu

Zmierzone 31 sierpnia 2026 na `site/index.html` (commit `83ff391`): **342 atrybuty `href`,
333 zewnetrzne, 159 unikalnych adresow**. Rozklad: `learn.microsoft.com` 194, `mc.merill.net` 93,
`daily.entra.news` 15, `azure.microsoft.com` 8, `www.microsoft.com` 5, `thehackernews.com` 4,
`entra.news` 4, `techcommunity.microsoft.com` 4, `developer.microsoft.com` 2, `www.neowin.net` 1.
**Zaden przebieg nie sprawdzil ani jednego z nich.** Brief, ktory linkuje w ciemno, jest tak
wiarygodny jak najgorszy ze swoich 159 linkow, a Microsoft przenosi artykuly co tydzien — na tym
wlasnie zyje `daily.entra.news`.

### Krok 1 — offline, prawie za darmo, dla wszystkiego z Learn

Lista plikow calego repozytorium dokumentacji kosztuje mniej niz jedna pobrana strona:

```
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/MicrosoftDocs/entra-docs
git -C entra-docs ls-tree -r --name-only HEAD > entra-files.txt
```

Zmierzone 31 sierpnia 2026: **15 893 sciezki, `.git` 912 KB, bez ani jednego bloba**. Mapowanie:

| URL | repozytorium | sciezka w repo |
|---|---|---|
| `learn.microsoft.com/<locale>?/entra/<X>` | `MicrosoftDocs/entra-docs` | `docs/<X>.md` |
| `…/graph/<X>` | `microsoftgraph/microsoft-graph-docs-contrib` | `concepts/<X>.md` |
| `…/defender-xdr/<X>`, `…/defender-for-identity/<X>`, `…/defender-endpoint/<X>` | `MicrosoftDocs/defender-docs` | `<produkt>/<X>.md` |
| `…/mem/<X>`, `…/intune/<X>` | `MicrosoftDocs/memdocs` | `memdocs/<X>.md` |

Segment jezyka (`/en-us/`), kotwice i `?…` obcinasz przed mapowaniem. Plik jest → `linkStatus:"ok"`,
zero zapytan sieciowych.

### Krok 2 — mapa przekierowan mowi, DOKAD artykul poszedl

`.openpublishing.redirection.json` w tym samym repo: **732 wpisy** 31 sierpnia 2026, kazdy w postaci
`{"source_path":"docs/…md","redirect_url":"/entra/…","redirect_document_id":false}`. Link, ktorego
pliku nie ma, ale ktory stoi w `source_path`, **nie jest martwy — jest przeniesiony**. Podmieniasz
`href` na `redirect_url`, zapisujesz `urlBefore` i dopisujesz rekord zmiany `kind:"Doc moved"`,
`origin:"microsoft"`. Przeniesienie linku jest ZNALEZISKIEM, nie sprzataniem: to znaczy, ze
Microsoft przepisal artykul, ktory cytujemy.

### Krok 3 — brak w repozytorium NIE jest dowodem smierci

Wlasciciel zglosil 31 sierpnia 2026, ze nie otwiera mu sie
`learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-provisioning-to-active-directory-works`.
Zmierzone tego samego dnia: tego sluga **nie ma wsrod 15 893 plikow entra-docs ani wsrod 732
przekierowan**, a mimo to Learn go serwuje — tytul „Microsoft Entra provisioning behavior (Preview)",
naglowek „How provisioning from Microsoft Entra ID to Active Directory works (preview)". Artykuly
w preview publikuja sie z galezi, ktorej publiczne lustro nie wozi. Kontrola na zmyslonym slugu
w tym samym katalogu: twarde `404 client error`, wiec narzedzie odroznia jedno od drugiego.

**Wniosek wiazacy: brak w repo → sprawdzenie na zywo. Nigdy brak w repo → „martwy".**
Odwrotny blad kosztowalby wiecej niz brak sprawdzania: skasowalibysmy prawdziwy artykul o preview.

### Krok 4 — sprawdzenie na zywo, z budzetem

Tylko dla adresow, ktorych kroki 1–2 nie rozstrzygnely. Learn przez
`mcp__Microsoft_Learn__microsoft_docs_fetch`, reszta przez WebFetch. **Najwyzej 40 zapytan na
przebieg**, w kolejnosci: Today, Top N, Deadlines, deep dive, reszta. Czego nie zmiescisz, zostaje
`unchecked` — i mowisz ile. `mc.merill.net` sprawdzasz obecnoscia numeru MC w kanale, nie
pobieraniem 93 stron.

### Pola i render

Kazdy element stanu i kazdy wpis katalogu niesie `linkStatus` (`ok` | `moved` | `dead` |
`unchecked`), `linkCheckedOn`, a przy `moved` takze `urlBefore`.

- `moved` — kotwica prowadzi do NOWEGO adresu, z klasa `lnk-moved` i tytulem `moved <data>`.
- `dead` — **tresci nie kasujesz.** Zrodlo renderuje sie jako
  `<span class="lnk-dead">link dead <data></span>`, a ostatni znany URL jako zwykly tekst.
  Kotwica prowadzaca w 404 klamie bardziej niz jej brak.
- `unchecked` — bez znacznika przy wierszu, ale policzona w Sources.

Sekcja Sources niesie jedno zdanie z data: *„159 unikalnych linkow: 147 rozstrzygnietych offline
w repozytoriach dokumentacji Microsoftu, 11 pobranych, 1 przeniesiony (podmieniony), 0 martwych,
0 niesprawdzonych — stan na <data>."* Zero martwych jest wynikiem i tez sie publikuje.

## 5s. Wykres samych jedynek nie jest raportem

31 sierpnia 2026 zakladka Products rysowala wykres **„By topic" z dziesiecioma slupkami, kazdy
rowny 1**: Passkeys, Passwordless, FIDO2, Authentication Methods policy, Temporary Access Pass,
Conditional Access, Authentication Strength, MFA enforcement, SMS, Voice. Wlasciciel napisal, ze
kompletnie go nie rozumie — i nie ma tam czego rozumiec. Wykres, w ktorym kazdy slupek ma 1, to ta
sama tabela obrocona o cwierc obrotu.

Przyczyna siedzi w danych, nie w powloce. `sectionSummaries()` fasetuje pierwsza rozpoznana kolumne,
a rozpoznaje co najmniej: `Product`, `Change type`, `Status`, `Priority`, `Area`, `Kind`, `Service`,
`Topic`. Tabela Authentication watchlist miala 12 wierszy i 10 roznych wartosci `Topic`, wiec faseta
nie grupowala niczego.

1. **Kolumna fasetowana jest slownikiem zamknietym, nie polem tekstowym.** Dozwolone wartosci
   `Product`: Entra · Intune · Defender XDR · Defender for Endpoint · Defender for Identity ·
   Defender for Cloud Apps · Purview · Sentinel · Exchange · Teams · SharePoint · Windows · Azure ·
   Graph · Copilot Studio.
2. **Temat wiersza idzie do tresci wiersza**, nie do naglowka kolumny. „Passkeys" opisuje jeden
   wiersz i nalezy do komorki `Change`.
3. **Policz fasete przed publikacja.** Dla kazdej rozpoznanej kolumny w panelu: jesli
   `max(licznosc) == 1` przy co najmniej czterech wierszach, albo roznych wartosci jest wiecej niz
   12 — kolumna jest zla. Przemianuj ja na nazwe, ktorej powloka nie fasetuje (`Scope`, `Feature`,
   `Capability`), a fasetowanie zostaw kolumnie `Product`.
4. Faseta, ktora dziala, wyglada jak pasek chipow z artefaktu z tego samego dnia:
   `2 Entra Connect · 2 Provisioning · 2 Authentication Methods · 1 Cloud Sync` — sa dwojki, wiec
   grupowanie cos znaczy.

## 5t. Linki i sekcje produktow w ramkach

Zmierzone w arkuszu z 31 sierpnia 2026 (60 879 znakow CSS, 32 zadeklarowane zmienne):
`a{color:var(--accent);text-decoration:none}` — link rozni sie od tekstu wylacznie kolorem. `.tw`
jest pozniej redefiniowane na `{overflow:visible;border:none}`, wiec tabele nie maja ramki.
Naglowki produktow w panelu `tab-products` to `<h3>` (7 sztuk: Entra, Sentinel, Defender XDR, MDE,
MDI, Purview, Intune) i sa golym tekstem.

**`--line` NIE ISTNIEJE w tym arkuszu.** Ramke rysuje sie `var(--border)`. Regula uzywajaca
niezadeklarowanej zmiennej jest niepoprawna przy wyliczaniu wartosci i potrafi zgasic tekst —
nie wymyslaj nazw zmiennych, sprawdz je w `<style>` przed uzyciem. Zadeklarowane sa: `--accent`,
`--accent-line`, `--accent-soft`, `--bad`, `--bad-soft`, `--bg`, `--border`, `--border-soft`,
`--code-bg`, `--cond`, `--del-bg`, `--del-fg`, `--faint`, `--grey`, `--grey-soft`, `--hdr-h`,
`--info`, `--info-soft`, `--ins-bg`, `--ins-fg`, `--mono`, `--muted`, `--ok`, `--ok-soft`,
`--on-accent`, `--sans`, `--surface`, `--surface-2`, `--surface-3`, `--text`, `--warn`,
`--warn-soft`.

Szesc regul dopisujesz na koncu `<style>`, razem z blokiem mobilnym (1a), znacznikami (5e)
i czytelnoscia (5k). Z nimi razem to sa JEDYNE dozwolone dopisane reguly CSS.

```css
.sec-body a[href^="http"]{display:inline-block;padding:1px 8px;border-radius:999px;background:var(--info-soft);color:var(--info);border:1px solid var(--info);font-weight:600;line-height:1.6;white-space:nowrap}
.sec-body a[href^="http"]:hover{background:var(--info);color:var(--on-accent);text-decoration:none}
.sec-body a.lnk-moved{background:var(--warn-soft);color:var(--warn);border-color:var(--warn)}
.sec-body .lnk-dead{display:inline-block;padding:1px 8px;border-radius:999px;background:var(--bad-soft);color:var(--bad);border:1px solid var(--bad);font-weight:600;white-space:nowrap}
#tab-products .sec-body h3{display:block;background:var(--accent-soft);color:var(--text);border:1px solid var(--accent);border-left:4px solid var(--accent);border-radius:10px;padding:8px 12px;margin:24px 0 12px}
#tab-products .sec-body .tw{border:1px solid var(--border);border-radius:12px}
```

`white-space:nowrap` jest konieczne: etykiety linkow sa krotkie („Microsoft Learn", „Message
Center", „Entra doc change") i zawiniety chip czyta sie jak dwa osobne. Selektor celuje wylacznie
w `.sec-body`, wiec masthead, pasek zakladek i klikalne wiersze katalogu (`href="#…"`, nie `http`)
zostaja nietkniete.

## 5u. Dwie sciezki publikacji, jeden brief — i podloga pokrycia

Ten sam dzien, 31 sierpnia 2026, ten sam temat, dwa przebiegi:

| licznik | strona SWA (routine, 07:32) | artefakt (scheduled task, 06:40 / 11:35) |
|---|---|---|
| items in window | 111 | 105 |
| permissions catalogued | 1 048 | 1 038 |
| role actions | 1 996 / 140 rol | 1 959 / 137 rol |
| deadlines in 60 days | 39 (15 inside 30) | 36 (22 inside 30) |
| undocumented at Microsoft | 28 (25 + 3) | 26 (25 + 1) |
| deployed, not in this tenant | 364 | 306 |
| Today / New / Products / Sources | 18 / 113 / **22** / 40 | 31 / 105 / **48** / 9 |
| kolejnosc pigulek | terminy, changes, items, permissions, roles, **undocumented 6., deployed 7.** | terminy, **undocumented 2., deployed 3.** — zgodnie z sekcja 1 |

Liczby nie musza byc rowne: dwa przebiegi dzieli szesc godzin, a zrodlo sie rusza. **Rowne musza byc
cztery rzeczy: zestaw i kolejnosc pigulek, zestaw zakladek i identyfikatory sekcji, procedura budowy
katalogu, oraz podloga pokrycia.** Strona SWA lamala 31 sierpnia pierwsza i czwarta.

### Podloga pokrycia — to ona zgubila Cloud Sync

Artefakt mial w deep dive dla Entry **13 wierszy**, w tym „Entra ID provisions users, groups and
group memberships into on-premises AD DS through the Cloud Sync agent, with the SID preserved"
(`Published 2026-08-19`, tier-0 skutek: chmura staje sie zapisujacym do AD). Strona SWA miala
**6 wierszy** i tego wiersza nie miala nigdzie — ani w deep dive, ani w exec summary. Przy
113 pozycjach w New i 22 wierszach w deep dive **91 pozycji wypadlo po cichu**.

**Regula: kazda pozycja z okna nalezy do dokladnie jednej tabeli produktu w deep dive.**
`suma wierszy deep dive` = `liczba pozycji okna przypisanych do produktu`. Naglowek kazdej tabeli
produktu mowi to liczba: *„13 z 113 pozycji okna nalezy do Entry; wszystkie 13 sa ponizej."*
Pozycja swiadomie pominieta nie znika — dostaje wiersz z powodem w kolumnie `Change`. Roznica
miedzy suma deep dive a liczba pozycji okna, ktora jest niezerowa i nieopisana, to **przebieg
NIEUDANY, nie publikuj**.

### Podloga zrodel

Kazde zrodlo w sekcji Sources raportuje trzy liczby — **przeczytane / wniesione / odrzucone** —
i jedno zdanie powodu odrzucenia. Zrodlo, ktore zwrocilo 40 pozycji, a wnioslo 3, jest poprawne
tylko wtedy, gdy strona mowi, co sie stalo z pozostalymi 37. Ciche odrzucanie jest dokladnie tym
mechanizmem, przez ktory historia o Cloud Sync zniknela z jednej z dwoch stron.

### Zmiany w dokumentacji sa pierwszoklasowym zrodlem

`daily.entra.news/changes/…` oraz git-log repozytoriow dokumentacji z sekcji 5r maja te sama range
co Message Center. Dostaja **wlasna sekcje `docchanges` w panelu `tab-new`**
(`<section id="docchanges" data-nav="Doc changes">`), z kolumnami `Article`, `What changed`,
`Lines`, `Security impact`, `Product`, `Source`. Roznice bierzesz z gita, nie z oka:
`git log --since=<okno> --numstat -- <sciezka>` daje `+143/-319` na plik, a `git log -p` daje tresc
zmiany. **Nie dodajemy dziesiatej zakladki** — pasek przy 1280 px jest juz pelny (sekcja 5h),
a kontrakt mowi o dziewieciu panelach.

## 5v. Zrodla i MCP — ktore po co, i ktore daje gotowy diff

Wlasciciel wskazal cztery serwisy i kilka MCP. Zadne z nich nie zastepuje tej strony — one dostarczaja
dane, my robimy z nich brief dla SOC. Ale **jeden z nich daje to, czego dotad recznie nie umielismy
zrobic: gotowa roznice pole po polu.**

### DeltaPulse — sprawdzone 31 sierpnia 2026, to jest podloga pokrycia dla MC i Roadmapy

MCP `mcp__DeltaPulse_-_track_M365_world__*` (zaladuj przez ToolSearch). Zmierzone tego dnia:

| wywolanie | wynik |
|---|---|
| `list_new_items(dateRange:"last_7_days", source:"both")` | `total_count: 47` |
| `list_change_history(days:3, changeType:"changed")` | `total: 21` |

`list_new_items` zwraca na wpis: `id` (`MC1464712` albo numer Roadmapy `569608`), `title` —
**naglowek Microsoftu slowo w slowo, czyli gotowy `officialTitle` z sekcji 5n** — `publishedDate`,
`service[]`, `category` (`planForChange` / `stayInformed` / `preventOrFixIssue`), `severity`,
`isMajorChange`, `actionRequiredByDateTime`, `tags`, `url`.

`list_change_history` zwraca na zmiane: `itemId`, `itemType`, `changeDate`, **`changedFields`**
(np. `["releaseDate","modifiedDate"]`, `["summary","lastUpdatedDate","bodyContent"]`),
**`previousValues` i `newValues` — pelne, obie strony**. Zmierzony przyklad:
Roadmap `396782` „Universal Print: Logs and alerts", `releaseDate` `December CY2026` → `January CY2027`.

**To jest dokladnie material na `<del>`/`<ins>`.** Regula sekcji 4 („roznice pokazuj, nie opisuj")
i wartosc `Revised at source`, ktora wymaga zacytowania obu stron, przestaja byc recznym wysilkiem:
`previousValues[pole]` idzie do `<del>`, `newValues[pole]` do `<ins>`, `changedFields` nazywa kolumne.
`releaseDate`, ktory sie przesunal, to `Deadline moved` z obiema datami wprost z danych.

**Czego DeltaPulse NIE obejmuje** — i dlatego nie zastepuje niczego: Roadmapa i Message Center, nic
poza tym. Zadnych uprawnien Graph, zadnych rol Entra, zadnych stron `learn.microsoft.com`
what's-new dla Defendera, Sentinela czy Intune, zadnej mapy wdrozen. Zbior D/A/B/C z sekcji 5d
i klony repozytoriow dokumentacji z sekcji 5r zostaja bez zmian.
**I jest halasliwy**: w probce z 31 sierpnia wiekszosc pozycji dotyczyla Dynamics, Teams i Vivy.
Wazenie bezpieczenstwem z sekcji 5p obowiazuje tak samo jak dla kazdego innego zrodla —
DeltaPulse podaje denominator („47 pozycji w oknie"), nie liste do przepisania.

### Jak uzywac ich razem

| zrodlo | do czego jest wiarygodne | czego z niego NIE bierzesz |
|---|---|---|
| **DeltaPulse MCP** | denominator MC + Roadmapy, `officialTitle`, ID, kategoria, `previousValues`/`newValues` | uprawnien, rol, tresci z Learn |
| **`mc.merill.net`** (RSS `/rss.xml`) | Message Center bez dostepu do tenanta; kontrola krzyzowa dla DeltaPulse | niczego o tenancie — kazdy wpis MC nosi przypis „vary by tenant" |
| **`daily.entra.news`** + MCP `mcp__remote-devices__entra-news-mcp__*` | zmiany w artykulach Entry, dzien po dniu — zrodlo sekcji `docchanges` | uprawnien Graph; MCP siedzi na pulpicie i w przebiegu chmurowym zwykle go nie ma |
| **`msmessagecenter.com`, `updates.getcurrent.cloud`** | trop i inspiracja UI (podzial na miesiace z sekcji 5o pochodzi stad) | zadnego faktu bez potwierdzenia u Microsoftu — to nie sa zrodla pierwotne |
| **`mcp__KQL_Search__*`** | przyklady zapytan i nazwy tabel do sprawdzenia | zadnego zapytania bez weryfikacji schematu na Learn (sekcja I) |
| **`mcp__Microsoft_Learn__*`** | kazdy URL `learn.microsoft.com` | niczego, co lepiej wziac z klona repo (sekcje 5b, 5i, 5r) |

**Kolejnosc jest odwrotna do wygody.** Klon repozytorium bije MCP, MCP bije stronę, strona bije
tracker. Serwis trzeciej strony nigdy nie jest cytowany jako zrodlo faktu — jest cytowany jako to,
czym jest: *„zglosil to <serwis> <data>; potwierdzone u Microsoftu <gdzie> <data>"*, albo wedruje do
`notPublished.watchlist`, gdy potwierdzenia nie ma.

**Kazde uzyte zrodlo raportuje w Sources trzy liczby — przeczytane / wniesione / odrzucone** —
zgodnie z sekcja 5u. Dla DeltaPulse to jest dokladnie `total_count` z `list_new_items` kontra liczba
wierszy, ktore trafily do New. Zrodlo niedostepne w przebiegu wymienia sie z nazwy jako niesprawdzone;
**MCP, ktorego nie ma, jest zrodlem zdegradowanym, nigdy powodem zatrzymania przebiegu.**

## 5w. Kolumna Source — faseta i przypiecie

Wlasciciel zglosil dwie rzeczy o kolumnie `Source`: nie miesci sie na ekranie i nie da sie po niej
filtrowac. Obie maja jedna, konkretna przyczyne w powloce i obie sa zmierzone.

### Dlaczego nie ma filtra — jedna linia

`facetCandidates()` w skrypcie 1 zaczyna od jawnego wykluczenia:

```js
if (/^source$/i.test(h)) return;
```

Kolumna `Source` nigdy nie trafia do kandydatow, wiec zaden `<select>` dla niej nie powstaje.
Do tego funkcja konczy sie `return out.slice(0, 2);` — **powloka buduje najwyzej DWA selecty**,
a w tabeli New zajmuja je `Product` i `Status`, w Today `Product` i `Change type`. Nawet po
odblokowaniu Source nie byloby dla niego miejsca.

**Trzy zmiany, dokladnie te i zadnych innych** (przed → po, do wklejenia bez interpretacji):

| # | przed | po |
|---|---|---|
| 1 | `      if (/^source$/i.test(h)) return;` | usun te linie (mozna zostawic komentarz w jej miejscu) |
| 2 | `var named = /^(product|service|topic)$/i.test(h);` | `var named = /^(product|service|topic|source)$/i.test(h);` |
| 3 | `return out.slice(0, 2);` | `return out.slice(0, 3);` |

Zmiana 2 czyni Source kolumna tozsamosciowa: podnosi limit dlugosci wartosci z 34 do 60 znakow
i liczbe roznych wartosci z 14 do 30, a `out.sort` stawia ja przed kolumnami nietozsamosciowymi.
Zmiana 3 daje trzecie miejsce, zeby Source nie wypchnal `Status` ani `Change type`.

Zmierzone 31 sierpnia 2026 na artefakcie 15:25, render 1500x1000:

| tabela | przed | po |
|---|---|---|
| New (108 wierszy) | `All product`, `All status` | `All product`, **`All source`**, `All status` |
| Today — zmiany (16 wierszy) | `All product`, `All change type` | `All product`, **`All source`**, `All change type` |

Zero bledow konsoli i strony w obu motywach.

### Dlaczego „nie miesci sie" — i czego to NIE jest

Zmierzone: **chipy w komorce `Source` nie wychodza poza nia ani o piksel** (0 wierszy z
przekroczeniem, maksimum 0 px). To nie jest przycinanie tekstu. Tabela New ma siedem kolumn
i **1 576 px szerokosci przy kontenerze 1 460 px**, wiec ostatnia kolumna po prostu stoi poza
ekranem i trzeba przewinac w bok, zeby ja zobaczyc. Pierwsza kolumna jest juz przypieta
(`stickyfirst` przy >=6 kolumnach), wiec czytelnik widzi `Product` i traci `Source` — czyli
dokladnie to, po czym chcialby filtrowac.

**Przypinamy ostatnia kolumne tak samo jak pierwsza.** Trzy reguly na koniec `<style>`, razem
z blokiem z §1a, §5e, §5k i §5t:

```css
.sec-body table col:last-child{width:172px!important}
.sec-body th:last-child,.sec-body td:last-child{position:sticky;right:0;background:var(--surface);box-shadow:inset 1px 0 0 var(--border);white-space:nowrap}
.sec-body thead th:last-child{background:var(--surface-2)}
```

`width` musi byc `!important`, bo `sizeTable()` wpisuje szerokosc kolumny stylem inline
(`col.style.width`), a `Source` dostaje tam 150 px z tablicy `WIDTHS` — za malo na chip
„Microsoft deployment map". Tlo jest obowiazkowe: bez niego przypieta komorka jest przezroczysta
i tresc przejezdza pod nia. `--surface` i `--surface-2` sa zadeklarowane (§5t).

Zmierzone po zmianie: w tabeli New `Source` jest widoczne **bez przewijania w bok**
(`visibleAtScroll0` z `false` na `true`), tabela nadal 1 576 px, kontener 1 460 px, zero bledow.

### To rozszerza liste dozwolonych zmian w skryptach

Do 31 sierpnia 2026 jedyna dozwolona zmiana w skryptach powloki byla mapa `KIND_BADGE` (§5e).
**Teraz sa dwie pozycje: `KIND_BADGE` oraz trzy zmiany `facetCandidates()` wypisane wyzej.**
Obie sa wymienione co do znaku i obie zostaly przetestowane renderem. Nic poza nimi w tych
trzech skryptach nie jest ruszane, a przebieg, ktory chce zmienic cokolwiek innego, tego nie
robi i pisze o tym w odpowiedzi.

**Na sciezce lustra (§0a) routine nie robi zadnej z tych zmian** — dostaje je gotowe razem
z odbita strona. Obowiazuja przy budowaniu, czyli w scheduled taskach i w fallbacku routine.

### Asercje Playwright

- w panelu `tab-new` i `tab-today` pasek narzedzi tabeli zawiera `<select>`, ktorego pierwsza
  opcja brzmi `All source`;
- `getComputedStyle(th_ostatni).position === "sticky"` i `right === "0px"`;
- tlo ostatniej komorki nie jest przezroczyste w obu motywach;
- przy `scrollLeft = 0` prostokat ostatniego `th` miesci sie w prostokacie `.tw`;
- zaden chip w ostatniej kolumnie nie wystaje poza swoja komorke.

## 6. Kontrakt w stronie

Kazda strona niesie komentarz `<!-- SHELL CONTRACT v1 ... -->` tuz po `<title>`. To pelna
specyfikacja UI, wozona razem z powloka, ktora opisuje. Kopiuj go dalej bez zmian.
**Gdy prompt i ten plik zdaja sie roznic co do markupu — wygrywa ten plik i kontrakt.**

---

## Task 1 — raport poranny

- Plik docelowy: `site/index.html`
- Dodatkowo zapisz surowe dane do `site/data/RRRR-MM-DD.json`.
  Bez tego pliku task 2 nie ma punktu odniesienia.
- Poprzednia wersje przenies do `site/history/RRRR-MM-DD-poranny.html`.

## Task 2 — diff (zmiany od rana)

- Plik docelowy: `site/diff/index.html`. **Nigdy nie dotykaj `site/index.html`** — to plik
  taska 1, a dwa przebiegi piszace do jednego pliku gubia strone.
- Punkt odniesienia: najnowszy `site/data/*.json` z dnia biezacego.
- Jesli nie ma zmian, i tak nadpisz strone, z wyrazna informacja
  "Brak zmian od <godzina porannego uruchomienia>". Pusta strona jest mylaca,
  bo nie wiadomo czy task w ogole wystartowal.
- Poprzednia wersje przenies do `site/history/RRRR-MM-DD-HHMM-diff.html`.

## Czego nie robic

- Nie modyfikuj `.github/workflows/*` ani `staticwebapp.config.json`.
- Nie usuwaj plikow z `history/`.
- Nie dodawaj sekretow, tokenow ani kluczy do repozytorium.
- Nie oddawaj calego zadania podagentowi w tle. Streszczenie od delegata to twierdzenie,
  nie wynik.
