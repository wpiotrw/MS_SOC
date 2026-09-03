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
| §5p `socWeight`, `tier0Touch` | **BRAK** | **BRAK** |

Dwie strony tego samego dnia, ten sam plik specyfikacji, dwa rozne wyniki. Przyczyna nie jest
w danych ani w powloce: **przebieg stosowal to, co wyliczyl prompt, zamiast tego, co mowi ten plik.**

## Jak sie tego uzywa

1. **Przeczytaj ten plik w calosci, zanim cokolwiek zbudujesz** — nie tylko sekcje, ktore prompt
   wymienil z numeru.
2. **Przejdz ponizsza liste pozycja po pozycji i zapisz wynik kazdej.** Pozycja niewykonana ma
   powod, nigdy cisze.
3. **Przed publikacja uruchom asercje z kolumny „sprawdzenie".** Kazda jest wykonalna w kodzie na
   gotowym pliku HTML — to nie jest ocena, tylko test.
4. **W odpowiedzi wypisz liste jako `OK` / `BRAK <powod>`.** Lista ma 33 pozycje dla przebiegu,
   ktory buduje albo odbija strone glowna, plus **pozycje 34 dla przebiegu ZMIAN** — razem 34. Wlasciciel czyta ta liste zamiast
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
| 14 | Top N wazony bezpieczenstwem: `socWeight` 1-7 i `tier0Touch` na KAZDEJ pozycji stanu, `sec-note` mowi czym wazyl i podaje liczby | 5p | zero pozycji bez `socWeight`; `sec-note` sekcji `top5` ma slowo o wazeniu i >=2 liczby |
| 15 | `firstTracked` na KAZDYM wpisie, `changed = deployedSeen` dla `D\A`, tablica `discoveries`, chip `New today` | 5q | licznik `firstTracked` = licznik wpisow; `discoveries` istnieje |
| 16 | `linkStatus` i `linkCheckedOn` na kazdym wpisie i kazdej pozycji stanu; zdanie w Sources | 5r | licznik `linkStatus` >= licznik pozycji stanu; `a.lnk-dead` = 0 |
| 17 | zadna fasetowana kolumna nie ma samych jedynek | 5s | dla kazdego `figure.chart` o >=4 slupkach nie wszystkie = 1 |
| 18 | szesc regul §5t na koncu `<style>` | 5t | `.sec-body a[href^="http"]` i `#tab-products .sec-body h3` obecne |
| 19 | podloga pokrycia: suma wierszy deep dive = liczba pozycji okna przypisanych do produktu | 5u | roznica zerowa albo opisana wierszem z powodem |
| 20 | sekcja `<section id="docchanges" data-nav="Doc changes">` w panelu `tab-new` | 5u | `id="docchanges"` obecne |
| 21 | kazde zrodlo raportuje przeczytane / wniesione / odrzucone | 5u, 5v | kazdy wiersz Sources ma trzy liczby |
| 22a | kolumna `Source` fasetowalna i przypieta | 5w | `<select>` z `All source` w New i Today; ostatni `th` ma `position:sticky` i `right:0` |
| 22 | DeltaPulse jako denominator MC + Roadmapy, `previousValues`/`newValues` do `<del>`/`<ins>` | 5v | pigulka „items in window" niesie denominator albo Sources mowi, ze MCP byl niedostepny |
| 23 | **kazda pozycja okna z `tier0Touch:true` ma karte w Top N albo nazwany powod w `sec-note`**; zadna karta Top N nie ma `socWeight>=7`, dopoki jest niewzieta pozycja okna z `socWeight<=2` | 5p | roznica zbiorow `tier0Touch` kontra `id` kart Top N jest pusta albo opisana |
| 24 | pole szukania zielone w OBU miejscach: selektor `.tbar input[type=search].tbar-search` i `.cat-searchwrap input.cat-search`, nigdy nizsza specyficznosc, nigdy `--accent` | 5k | oba pola daja to samo `background` i nie jest to `--surface` |
| 25 | trzy zmiany `facetCandidates()` zastosowane — kazda tabela z kolumna `Source` ma `<select>` `All source` | 5w | brak `if (/^source$/i.test(h)) return;`, `named` zawiera `source`, `slice(0, 3)` |
| 26 | zadna z DZIEWIECIU zakladek nie rozpycha dokumentu przy 390x844 | 5x | dla kazdej zakladki `scrollWidth === clientWidth` |
| 27 | skrypty 4 I 5 obecne; kazda zakladka tresciowa ma wykres per usluga, pierscien udzialu i os czasu Month / Week / Day; kafelki `What changed` filtruja liste katalogu | 5y, 5ad | `.aggwrap figure.chart` >= 3 w kazdym panelu procz Overview; `.aggbtn` = 3; tabela `cc-table` ma kolumne `Change` |
| 28 | **kazdy termin z ostatnich 7 dni zostaje**: `tier:"recently-elapsed"`, sekcja `id="elapsed"` w `tab-deadlines` I w `tab-overview`, pigulka `passed in the last 7 days`; pozycja nie wypada z Today ani z New | 5z | liczba pozycji z terminem w −7..0 = liczba wierszy `.elapsed-wrap tbody tr` w obu panelach |
| 29 | naglowek Top N niesie LICZBE; 7 domyslnie, najwyzej 10 | 5aa | `document.body.innerText` nie zawiera `Top N`; `article.card` w `tab-today` miesci sie w 7..10 |
| 30 | **zero polskich slow w warstwie widocznej dla czytelnika** — cala strona jest po angielsku | 5y | `innerText` nie zawiera `Per usluga`, `Udzial`, `Miesiac`, `Tydzien`, `Dzien`, `pozycji okna`, `Metody uwierzytelniania` |
| 31 | **kazda pozycja stanu z terminem ma WIERSZ w jakiejs tabeli** — poza 60 dniem jest `<section id="horizon">` z tabela, nigdy akapit; fraza „in one paragraph" nie wystepuje; kazdy wiersz terminu niesie `data-id` | 5ab | dla kazdej pozycji z `deadline` istnieje `<tr>` o tym `data-id` (albo z jej tytulem w tresci); `horizon` w `ids`; brak frazy „in one paragraph" |
| 32 | pozycja 61-120 dni z `socWeight<=2` albo `tier0Touch` promowana do GLOWNEJ tabeli, pasmo `61-120 days` | 5ab | zero takich pozycji poza glowna tabela |
| 33 | **KAZDA pozycja stanu ma wiersz albo karte — nie tylko datowana.** Zaden `tier` nie jest kubelkiem, ktorego strona nie renderuje | 5ac | zero pozycji `items` bez `<tr data-id>` albo `article.card[data-id]` |
| 34 | **tylko przebieg ZMIAN**: strona zmian jest LICZONA przez `make_diff.py`, nie odbijana — bez zakladek, bez katalogu, bez blokow JSON, ponizej 900 kB | 3 | `verify()` w `make_diff.py` konczy sie bez bledu; rozmiar pliku w dziesiatkach kB, nie w megabajtach |

**Pozycja, ktorej nie da sie wykonac, bo zrodlo bylo niedostepne, jest `BRAK` z nazwa zrodla —
nigdy nie jest pomijana w ciszy.** Pozycje 15, 16, 19, 20, 23, 26, 28, 31 i 33 sa wiazace: przebieg, ktory je pominie
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
    if p.scripts < 4: errs.append("skryptow zachowania = %d, ma byc >=4 (powloka, overview, katalog, agregaty §5y)" % p.scripts)
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
    strony /diff/ wycinamy go w calosci; strona glowna zachowuje go bez zmian.

    3 wrzesnia 2026: granica `content.find("<style", i)` byla ZLA, bo komentarz sam
    cytuje `<style>` — na stronie z tego dnia trafiala w znak 839 przy komentarzu
    zaczynajacym sie na 476, `rfind` nie znajdowal nic i funkcja zwracala tresc BEZ
    ZMIAN. Granica jest PRAWDZIWY arkusz: `<style>`, po ktorym od razu idzie CSS."""
    i = content.find("<!-- SHELL CONTRACT")
    if i < 0:
        return content
    m = re.search(r"<style[^>]*>\s*(?=:root|/\*|@)", content[i:])
    k = i + m.start() if m else -1
    j = content.rfind("-->", i, k if k > 0 else len(content))
    return content[:i] + content[j + 3:] if j > i else content

def parts(content: str):
    """Powloka: style + trzy skrypty zachowania + oba bloki JSON + masthead."""
    content = drop_contract(content)
    p = {}
    p["styles"] = re.findall(r"<style[^>]*>.*?</style>", content, re.S)
    p["json"]   = re.findall(r'<script type="application/json" id="[^"]+">.*?</script>', content, re.S)
    # blok, ktory zawiera w srodku kolejne "<script", to nadmiarowe dopasowanie regexa
    # po resztkach cytowanego markupu — te odrzucamy. RESZTE BIERZEMY W CALOSCI.
    # 2 wrzesnia 2026 stalo tu `clean[-3:]`, z czasow gdy skrypty byly trzy. Po dolozeniu
    # SKRYPTU 4 (§5y) „trzy ostatnie" to overview + katalog + agregaty, a POWLOKA — ta,
    # ktora buduje pasek zakladek — wypadala. Strona /diff/ z tego dnia miala 3,6 MB,
    # zero bledow konsoli i PUSTY `<nav class="anchors">`: zadnej zakladki, oba panele
    # `hidden`, czytelnik widzial masthead i nic wiecej.
    raw_scripts = re.findall(r"<script(?![^>]*application/json)[^>]*>.*?</script>", content, re.S)
    p["scripts"] = [b for b in raw_scripts if "<script" not in b[len("<script"):]]
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
    if p.scripts < 4: errs.append("skryptow zachowania = %d, ma byc >=4 (powloka, overview, katalog, agregaty §5y)" % p.scripts)
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

## 0b. BRAMKA PUBLIKACJI — kod, nie dobre checi

Przebieg routine z 31 sierpnia 2026 wypisal dziewiec pozycji listy §0 jako `BRAK` na stronie, ktora
przeszla caly STEP 4 porannego taska. To nie byl przypadek: **STEP 4 sprawdzal `origin`, `objectType`,
liczniki katalogu i pigulki, ale nie sprawdzal ani `firstTracked`, ani `linkStatus`, ani `docchanges`.**
Regula bez asercji jest sugestia, a sugestie przebieg pomija bez konsekwencji — to jest ten sam
mechanizm, ktory rozjechal obie strony.

Ponizszy skrypt zamyka luke. **Zapisz go do `/tmp/gate.py` i uruchom na gotowym pliku HTML zanim
cokolwiek opublikujesz: `python3 /tmp/gate.py <plik>`. Kod wyjscia 1 znaczy NIE PUBLIKUJ.**
Pozycje 15, 16 i 20 sa wiazace (§0), wiec ich brak zatrzymuje przebieg; pozostale wypisz w odpowiedzi
jako `BRAK <powod>`.

Zmierzone na stronie z 17:15 (lustro artefaktu tego dnia) — bramka odtworzyla wynik przebiegu
co do liczby: `docStatus` brak na 15 z 1 496 wpisow, `firstTracked` na 0 z 1 496, `discoveries` brak,
306 z 306 wpisow `D\A` ma `changed` rozne od `deployedSeen`, `linkStatus` brak na 153 ze 157 pozycji
stanu i na 1 496 z 1 496 wpisow katalogu, brak sekcji `docchanges`, Sources bez trzech liczb.
**I slusznie NIE zglosila dwoch pozycji, ktore przebieg oznaczyl na czerwono:** `officialTitle` ma
pokrycie przez `officialTitleNote`, a okno 17–31 sierpnia nie przecina granicy miesiaca, wiec §5o
grupowania nie wymaga. Bramka ma odrozniac brak od falszywego alarmu — inaczej nauczy przebieg
ignorowac czerwone.

```python
#!/usr/bin/env python3
"""Bramka publikacji dla porannego builda — CLAUDE.md Sec.0b.
   python3 gate.py <gotowy.html>   |  kod wyjscia 1 = NIE PUBLIKUJ
Sprawdza pozycje listy Sec.0, ktorych STEP 4 dotad nie sprawdzal wcale."""
import sys, re, json
from html.parser import HTMLParser

def blocks(h):
    out = {}
    for b in ("soc-brief-state", "soc-catalog"):
        m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % b, h, re.S)
        out[b] = json.loads(m.group(1)) if m else None
    return out

class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.deadA=0; self.captions=0; self.grp=0; self.cards=set()
        self.sec=None; self.notes={}; self._grab=None; self.cardCount=0; self.text=[]; self._skip=0
        # kazdy <tr> jako (sekcja, data-id, tekst) — pozycja 31/32 pyta, W KTOREJ tabeli stoi wiersz
        self.rows=[]; self._secstack=[]; self._row=None; self._rowid=None; self._rowsec=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); cls=(a.get("class") or "").split()
        if a.get("id"): self.ids.add(a["id"])
        if tag=="a" and "lnk-dead" in cls: self.deadA+=1
        if tag=="article" and "card" in cls:
            self.cardCount+=1
            if a.get("data-id"): self.cards.add(a["data-id"])
        if tag=="caption": self.captions+=1
        if tag=="tr" and "grp" in cls: self.grp+=1
        if tag=="section":
            self._secstack.append(a.get("id") or "")
            if a.get("id"): self.sec=a["id"]
        if tag=="tr":
            self._row=[]; self._rowid=a.get("data-id"); self._rowsec=self.sec
        if tag=="p" and "sec-note" in cls: self._grab=self.sec
        if tag in ("script","style"): self._skip+=1
    def handle_data(self, d):
        if self._grab: self.notes[self._grab]=self.notes.get(self._grab,"")+d
        if not self._skip: self.text.append(d)
        if self._row is not None and not self._skip: self._row.append(d)
    def handle_endtag(self, tag):
        if tag=="p": self._grab=None
        if tag=="tr" and self._row is not None:
            self.rows.append((self._rowsec, self._rowid, " ".join("".join(self._row).split())))
            self._row=None; self._rowid=None; self._rowsec=None
        if tag=="section" and self._secstack:
            self._secstack.pop()
            self.sec=self._secstack[-1] if self._secstack else None
        if tag in ("script","style") and self._skip: self._skip-=1

def gate(path):
    h=open(path,encoding="utf-8").read()
    st=blocks(h); s=Scan(); s.feed(h)
    items=(st["soc-brief-state"] or {}).get("items",[])
    cat=st["soc-catalog"] or {}
    entries=(cat.get("graph") or [])+(cat.get("roles") or [])
    bad=[]
    def chk(no,name,ok,detail=""):
        (print if ok else bad.append)("  [%s] %-2s %s %s" % ("OK " if ok else "BRAK", no, name, detail)
                                       if ok else "%-3s %s — %s" % (no, name, detail))
        if ok: return
    def need(no,name,ok,detail=""):
        if ok: print("  [OK ] %-3s %s" % (no,name))
        else:  print("  [BRAK] %-3s %s — %s" % (no,name,detail)); bad.append(no)

    n=len(entries); m=len(items)
    need("6",  "docStatus na kazdym wpisie",
         all(e.get("docStatus") for e in entries), "%d z %d bez" % (sum(1 for e in entries if not e.get("docStatus")), n))
    need("11", "Today mowi liczbami, ze jest wyborem",
         bool(re.search(r"\b(of|z)\s+\d+\b", " ".join(v for k,v in s.notes.items() if k in ("top5","picks","delta")))),
         "zadna sec-note Today nie podaje 'N z M'")
    need("12", "officialTitle albo officialTitleNote na kazdej pozycji stanu",
         all(i.get("officialTitle") or i.get("officialTitleNote") for i in items),
         "%d z %d bez" % (sum(1 for i in items if not (i.get("officialTitle") or i.get("officialTitleNote"))), m))
    win=(st["soc-brief-state"] or {}).get("window") or {}
    crosses = (win.get("publishedFrom","")[:7] != win.get("publishedTo","")[:7])
    need("13", "grupowanie miesiacami w New/Deadlines",
         (not crosses) or s.captions>0 or s.grp>0,
         "okno %s..%s przecina miesiac, a caption=%d tr.grp=%d" % (win.get("publishedFrom"),win.get("publishedTo"),s.captions,s.grp))
    need("15a","firstTracked na kazdym wpisie katalogu",
         all(e.get("firstTracked") for e in entries), "%d z %d bez" % (sum(1 for e in entries if not e.get("firstTracked")), n))
    need("15b","tablica discoveries", bool(cat.get("discoveries")), "brak w soc-catalog")
    da=[e for e in entries if e.get("kind")=="Deployed in the service, not in this tenant"]
    need("15c","D\\A: changed == deployedSeen",
         all(e.get("changed") and e.get("changed")==e.get("deployedSeen") for e in da) if da else True,
         "%d z %d wpisow D\\A ma changed != deployedSeen" % (sum(1 for e in da if e.get("changed")!=e.get("deployedSeen")), len(da)))
    need("16a","linkStatus na kazdej pozycji stanu",
         all(i.get("linkStatus") for i in items), "%d z %d bez" % (sum(1 for i in items if not i.get("linkStatus")), m))
    need("16b","linkStatus na kazdym wpisie katalogu",
         all(e.get("linkStatus") for e in entries), "%d z %d bez" % (sum(1 for e in entries if not e.get("linkStatus")), n))
    need("16c","zadna kotwica a.lnk-dead", s.deadA==0, "%d kotwic prowadzi w 404" % s.deadA)
    need("14a","socWeight 1-7 na kazdej pozycji stanu",
         all(isinstance(i.get("socWeight"),int) and 1<=i["socWeight"]<=7 for i in items),
         "%d z %d bez poprawnego socWeight" % (sum(1 for i in items if not (isinstance(i.get("socWeight"),int) and 1<=i["socWeight"]<=7)), m))
    need("14b","tier0Touch na kazdej pozycji, tier0Note gdy true",
         all("tier0Touch" in i for i in items) and all(i.get("tier0Note") for i in items if i.get("tier0Touch")),
         "%d bez tier0Touch, %d z tier0Touch bez tier0Note" % (
             sum(1 for i in items if "tier0Touch" not in i),
             sum(1 for i in items if i.get("tier0Touch") and not i.get("tier0Note"))))
    top=s.notes.get("top5","")
    need("14c","sec-note Top N mowi o wazeniu i podaje >=2 liczby",
         bool(re.search(r"wag|weigh|tier 0", top, re.I)) and len(re.findall(r"\d+", top))>=2,
         "sec-note top5 %s" % ("nie istnieje" if not top else "bez slowa o wazeniu albo bez dwoch liczb"))
    # 23 nie moze przejsc PUSTO: brak pola to brak sprawdzenia, nie zgodnosc
    inwin=[i for i in items if i.get("tier")!="horizon"]
    hasT0=any("tier0Touch" in i for i in items)
    hasSW=any(isinstance(i.get("socWeight"),int) for i in items)
    t0=[i for i in inwin if i.get("tier0Touch")]
    miss=[i["id"] for i in t0 if i["id"] not in s.cards and i["id"] not in top]
    need("23a","kazda pozycja okna tier0Touch ma karte Top N albo nazwany powod",
         hasT0 and not miss,
         "brak pola tier0Touch — nie da sie sprawdzic" if not hasT0
         else "bez karty i bez powodu: %s" % ", ".join(miss[:5]))
    byid={i["id"]:i for i in items}
    heavy=[i["id"] for i in inwin if (i.get("socWeight") or 9)<=2 and i["id"] not in s.cards]
    light=[c for c in s.cards if (byid.get(c,{}).get("socWeight") or 0)>=7]
    need("23b","zadna karta socWeight>=7 przy niewzietej pozycji socWeight<=2",
         hasSW and not (light and heavy),
         "brak pola socWeight — nie da sie sprawdzic" if not hasSW
         else "karty lekkie %s przy %d niewzietych ciezkich" % (light, len(heavy)))
    need("23c","karty Top N nios data-id", len(s.cards)>=1, "zero <article class=\"card\" data-id=...>")
    need("20", "sekcja docchanges w tab-new", "docchanges" in s.ids, "brak <section id=\"docchanges\">")
    # 24-27: powloka. Bramka czyta plik, wiec sprawdza OBECNOSC regul i kodu;
    # wartosci wyliczone i przewijanie sprawdza Playwright (§5h).
    need("24", "zielone pole szukania o wlasciwej specyficznosci",
         "input[type=search].tbar-search" in h and ".cat-searchwrap input.cat-search" in h
         and "var(--ok-soft)" in h,
         "brak selektora o specyficznosci powloki albo brak --ok-soft")
    need("25", "trzy zmiany facetCandidates (§5w)",
         "if (/^source$/i.test(h)) return;" not in h
         and "/^(product|service|topic|source)$/i" in h
         and "out.slice(0, 3)" in h,
         "guard=%s named+source=%s slice3=%s" % (
             "if (/^source$/i.test(h)) return;" not in h,
             "/^(product|service|topic|source)$/i" in h,
             "out.slice(0, 3)" in h))
    need("26", "blok mobilny §5x przeciw rozpychaniu dokumentu",
         ".sec-body .lnk-dead{white-space:normal" in h.replace("\n","")
         or "white-space:normal;max-width:100%;overflow-wrap:anywhere" in h,
         "brak reguly zdejmujacej nowrap z chipow linkow na telefonie")
    need("27", "skrypt 4 (agregaty §5y) obecny",
         ("SKRYPT 4" in h or "SCRIPT 4" in h) and "aggwrap" in h and "aggbtn" in h,
         "brak skryptu agregatow albo jego klas")
    # 28-30: §5z, §5aa, §5y — jezyk i terminy, ktore minely
    import datetime as _dt
    bd=(st["soc-brief-state"] or {}).get("briefDate") or _dt.date.today().isoformat()
    try: today=_dt.date(*map(int,bd.split("-")))
    except Exception: today=_dt.date.today()
    def _d(x):
        try: return _dt.date(*map(int,(x or "")[:10].split("-")))
        except Exception: return None
    gone=[i for i in items if _d(i.get("deadline")) and 0 < (today-_d(i["deadline"])).days <= 7]
    need("28a","kazdy termin z ostatnich 7 dni ma tier recently-elapsed",
         all(i.get("tier")=="recently-elapsed" for i in gone) if gone else True,
         "%d z %d ma inny tier" % (sum(1 for i in gone if i.get("tier")!="recently-elapsed"), len(gone)))
    need("28b","sekcja elapsed istnieje gdy sa takie pozycje",
         (not gone) or ("elapsed" in s.ids),
         "%d pozycji po terminie, a brak <section id=\"elapsed\">" % len(gone))
    # Komentarz SHELL CONTRACT cytuje markup ORAZ przykladowe teksty, wiec literalu
    # szukamy w TRESCI: bez skryptow, bez arkusza i bez komentarzy.
    body=re.sub(r"<script.*?</script>","",h,flags=re.S)
    body=re.sub(r"<style.*?</style>","",body,flags=re.S)
    body=re.sub(r"<!--.*?-->","",body,flags=re.S)
    # Liczymy karty PARSEREM, nie regexem: komentarz SHELL CONTRACT bywa przerwany
    # wczesnym "-->", wiec niezachlanne wycinanie komentarzy zjada kawal dokumentu.
    ncards=s.cardCount
    need("29", "naglowek Top N niesie liczbe, kart 7..10",
         ("Top N of the day" not in "".join(s.text)) and 7 <= ncards <= 10,
         "literal 'Top N' w tresci=%s, kart=%d (7..10)" % ("Top N of the day" in "".join(s.text), ncards))
    PL=["Per usluga","Udzial","Miesiac","Tydzien","Dzien","pozycji okna","Metody uwierzytelniania","Terminy w czasie"]
    vis="".join(s.text)
    hit=[w for w in PL if w in vis]
    need("30", "zero polskich slow w tresci strony", not hit, "znalezione: %s" % ", ".join(hit))
    # 31-32: §5ab — poza 60 dniem tez tabela, waga promuje z powrotem.
    # Pytanie brzmi „czy pozycja MA WIERSZ i w KTOREJ tabeli", wiec liczymy wiersze
    # parserem razem z ich sekcja. Szukanie podciagu „61"/„120" w tresci przechodzilo
    # przypadkiem — kazda strona z data albo licznikiem zawiera te cyfry.
    def _norm(x): return " ".join((x or "").lower().split())
    rowids=set(r[1] for r in s.rows if r[1])
    rowtx=[(r[0], _norm(r[2])) for r in s.rows]
    def rowsec_of(it):
        """Zwraca sekcje wiersza tej pozycji albo None, gdy pozycja nie ma wiersza nigdzie."""
        if it.get("id") in rowids:
            for sec,rid,_ in s.rows:
                if rid==it["id"]: return sec or ""
        for key in (it.get("title"), it.get("officialTitle"), it.get("id")):
            k=_norm(key)[:44]
            if len(k)<12: continue
            for sec,tx in rowtx:
                if k in tx: return sec or ""
        return None
    byid_all={i.get("id"):i for i in items}
    dated=[i for i in items if _d(i.get("deadline"))]
    far=[i for i in dated if (_d(i["deadline"])-today).days > 60]
    need("31a","sekcja horizon istnieje gdy cos jest poza 60 dniem",
         (not far) or ("horizon" in s.ids),
         "%d pozycji poza 60 dniem, a brak <section id=\"horizon\">" % len(far))
    need("31b","horyzont nie jest proza",
         "in one paragraph" not in "".join(s.text) and "not tabulated" not in "".join(s.text),
         "strona nadal zwija horyzont w zdanie")
    norow=[i["id"] for i in dated if rowsec_of(i) is None]
    need("31c","kazda pozycja z terminem ma WIERSZ w jakiejs tabeli",
         bool(dated) and not norow,
         "brak pozycji z terminem — nie da sie sprawdzic" if not dated
         else "%d z %d bez wiersza: %s" % (len(norow), len(dated), ", ".join(norow[:5])))
    # 33: §5ac — KAZDA pozycja stanu ma wiersz, nie tylko datowana. Zmierzone 2 wrzesnia:
    # 36 ze 191 pozycji nie mialo ani wiersza, ani karty — WSZYSTKIE 36 to `tier:"horizon"`,
    # czyli caly kubelek, ktorego prezentacja nie renderuje. Szesc z nich ma socWeight 1.
    nocover=[i["id"] for i in items if rowsec_of(i) is None and i["id"] not in s.cards]
    need("33","KAZDA pozycja stanu ma wiersz albo karte, nie tylko datowana",
         bool(items) and not nocover,
         "brak pozycji stanu — nie da sie sprawdzic" if not items
         else "%d z %d bez wiersza i bez karty (tier: %s): %s" % (
             len(nocover), len(items),
             ",".join(sorted({(byid_all.get(x) or {}).get("tier") or "?" for x in nocover})),
             ", ".join(nocover[:6])))
    promo=[i for i in far
           if (_d(i["deadline"])-today).days <= 120
           and ((isinstance(i.get("socWeight"),int) and i["socWeight"]<=2) or i.get("tier0Touch"))]
    hasW=any(isinstance(i.get("socWeight"),int) for i in items) or any("tier0Touch" in i for i in items)
    # promowany ma stac w GLOWNEJ tabeli terminow, czyli poza sekcja horizon — samo istnienie
    # wiersza nie wystarcza, bo wiersz w horyzoncie to wlasnie to, czego regula zabrania
    badpromo=[i["id"] for i in promo if (rowsec_of(i) or "horizon")=="horizon"]
    band=any(re.search(r"61\s*[-\u2013]\s*120\s*days", tx) for _,tx in rowtx) \
         or re.search(r"61\s*[-\u2013]\s*120\s*days", "".join(s.text)) is not None
    need("32","61-120 dni z waga <=2 albo tier0 promowane do glownej tabeli",
         hasW and not badpromo and (band if promo else True),
         "brak pol socWeight/tier0Touch — nie da sie sprawdzic" if not hasW
         else ("%d pozycji stoi w horyzoncie zamiast w glownej tabeli: %s" % (len(badpromo), ", ".join(badpromo[:4]))
               if badpromo else "brak pasma '61-120 days' przy %d pozycjach do promocji" % len(promo)))
    src=s.notes.get("sources","")
    need("21", "Sources podaje trzy liczby na zrodlo",
         len(re.findall(r"\d+\s*/\s*\d+\s*/\s*\d+", src))>0 or len(re.findall(r"read\D+\d+.*?carried\D+\d+.*?dropped\D+\d+", src, re.I))>0,
         "sec-note Sources bez wzorca przeczytane/wniesione/odrzucone")
    print()
    if bad:
        print("PRZEBIEG NIEUDANY — %d pozycji: %s" % (len(bad), ", ".join(bad)))
        return 1
    print("Bramka Sec.0b: wszystkie pozycje OK")
    return 0

if __name__ == "__main__":
    sys.exit(gate(sys.argv[1]))
```

**Rozszerzone 2 wrzesnia 2026 o pozycje 33 (§5ac) — bo §5ab lapal tylko datowane.** Pozycja 31c
pyta o pozycje Z TERMINEM; wlasciciel powiedzial, ze MC1448379 bylo przykladem, a nie przypadkiem.
Pozycja 33 pyta o WSZYSTKIE. Zmierzone na stronie z 2 wrzesnia: **36 ze 191 pozycji stanu nie ma ani
wiersza, ani karty, i wszystkie 36 to `tier:"horizon"`** — 6 o wadze 1, 13 o wadze 2. Regresja na
trzech wariantach: strona z 2 wrzesnia `33 BRAK 36/191`, ta sama z tabela horyzontu tylko dla
datowanych `33 BRAK 30/191`, z tabela biorąca wszystkie — `33 OK`. Bramka wypisuje `id` i `tier`,
nie sama liczbe.

**Rozszerzone 2 wrzesnia 2026 o pozycje 31-32 (§5ab) — i pierwsza wersja pozycji 32 byla zla.**
Pytala `"61" in tresc and "120" in tresc`, czyli o PODCIAG, a kazda strona z data albo licznikiem
zawiera obie cyfry: na zywej stronie z 2 wrzesnia dawala **OK przy dwoch pozycjach zwinietych
w akapit** — dokladnie tych, o ktore pytal wlasciciel. To ten sam blad co pusty zbior w pozycji 23:
asercja przechodzila z niewlasciwego powodu. Teraz bramka **liczy wiersze parserem razem z ich
sekcja** (`self.rows` jako `(sekcja, data-id, tekst)`), wiec potrafi odpowiedziec nie tylko „czy
pozycja ma wiersz", ale „w KTOREJ tabeli ten wiersz stoi" — a o to wlasnie chodzi w regule promocji.
Pozycja `31c` dopisana: **kazda pozycja stanu z terminem ma wiersz w jakiejs tabeli**, dopasowywany
po `data-id` wiersza, a gdy go nie ma — po znormalizowanym tytule.

Zmierzone na zywej stronie z 2 wrzesnia: `31a BRAK` (8 pozycji poza 60 dniem, brak sekcji),
`31b BRAK`, `31c BRAK` (6 z 51 pozycji z terminem nie ma wiersza NIGDZIE: `MC1448379`,
`MC1325414-enforcement`, `mda-file-policies-retirement`, `MC1220762`,
`sentinel-azure-portal-retirement-2027`), `32 BRAK` z nazwiskami: `MC1325414-enforcement`,
`MC1448379`. Kontrola regresji na szesciu wariantach tej samej strony: (a) tabela horyzontu plus
pasmo `61-120 days` w tabeli glownej — `31a/31b/31c/32 OK`; (b) wszystko w horyzoncie, promowane
takze — `32 BRAK` z ich `id`; (c) stan bez `socWeight`/`tier0Touch` — `32 BRAK „nie da sie
sprawdzic"`, nie OK; (d) stan bez terminow — `31c BRAK „nie da sie sprawdzic"`, nie OK;
(e) pasmo usuniete, wiersze zostaja — `32 BRAK „brak pasma 61-120 days"`; (f) pasmo z poltuzem
zamiast dywizu — `32 OK`, bo regex przyjmuje `-` i `–`.

**Rozszerzone 2 wrzesnia 2026 o pozycje 28-30 (§5z, §5aa, §5y).** Dwie pulapki, ktore ta bramka
musiala obejsc, sa te same, co w §0a: komentarz SHELL CONTRACT **cytuje** przykladowe teksty, wiec
literalu `Top N of the day` szuka sie w TRESCI bez skryptow, arkusza i komentarzy; a karty liczy sie
**parserem, nie regexem**, bo komentarz bywa przerwany wczesnym `-->` i niezachlanne wycinanie
komentarzy zjadalo kawal dokumentu — pierwsza wersja pokazala `kart=0` tam, gdzie jest siedem.
Kontrola na stronie z 2 wrzesnia: `27/29/30 OK`, `28a/28b BRAK` — i to jest poprawny wynik, bo
sekcje `elapsed` ma napisac PRZEBIEG, a skrypt 4 tylko ja dokłada w przegladarce jako siatka
bezpieczenstwa. Bramka czyta plik, wiec nie widzi tego, co powstaje dopiero w DOM.

**Rozszerzone 1 wrzesnia 2026 o pozycje 24-27 (§5k, §5w, §5x, §5y).** Bramka czyta plik, wiec
sprawdza OBECNOSC selektora, trzech zmian `facetCandidates()`, bloku mobilnego i skryptu 4;
wartosci wyliczone i przewijanie w poziomie sprawdza Playwright (§5h) — plik moze zawierac regule,
ktora przegrywa specyficznoscia, i wlasnie tak bylo z zielonym polem szukania. Kontrola na dwoch
stronach tego samego dnia: strona sprzed poprawek daje `24/25/26/27 BRAK`, strona po poprawkach
`24/25/26/27 OK`, przy identycznej reszcie wyniku.

**Rozszerzone 31 sierpnia 2026 o pozycje 14 i 23 (§5p).** Zmierzone na stronie z 15:37: `socWeight`
brak na 157 ze 157 pozycji stanu, `tier0Touch` brak na 157, sekcja `top5` **nie miala `sec-note`
w ogole**, a siedem kart Top N nie nioslo ani jednego `data-id`. Kontrola regresji na czterech
wariantach tej samej strony: (a) trzy pozycje `tier0Touch` maja karty — wszystkie szesc asercji OK;
(b) te same trzy pominiete i nienazwane — `23a` BRAK z ich `id`; (c) pominiete, ale **nazwane w
`sec-note`** — `23a` OK, bo swiadome pominiecie z powodem jest dozwolone, natomiast karta Azure
o wadze 7 przy 76 niewzietych pozycjach wagi <=2 daje `23b` BRAK; (d) strona bez tych pol —
`23a`/`23b` daja **BRAK „nie da sie sprawdzic", nie OK.** Ten ostatni wariant byl pierwsza wersja
bramki i przechodzil pusto: zbior bez elementow spelnia kazdy warunek. **Asercja, ktora przechodzi
na braku danych, jest gorsza niz jej brak** — uczy przebieg, ze zielone nic nie znaczy.

**Bramka nie zastepuje listy §0 — jest jej wykonywalna czescia.** Pozycje, ktorych nie da sie
sprawdzic kodem na gotowym pliku (0 lustro, 2 kolejnosc regul w arkuszu, 17 fasety, 19 podloga
pokrycia, 22 denominator) zostaja do sprawdzenia recznego i do wypisania w odpowiedzi. Sama
**przypisana wartosc** `socWeight` tez jest ocena redakcyjna — bramka sprawdza, czy pole jest i czy
miesci sie w 1-7, nie czy przebieg trafnie zaklasyfikowal. Dlatego `sec-note` Top N musi podac liczby:
zeby wybor dalo sie zakwestionowac bez czytania JSON-a.

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

## 3. STRONA ZMIAN JEST LICZONA Z DANYCH, NIE ODBIJANA Z ARTEFAKTU

Wlasciciel napisal 2 wrzesnia 2026 wprost: *„calym zamyslem diff jest pokazanie roznic.
Wylistowanie co ubylo co przybylo. Podsumowanie zmian, a nie powiekanie znowu tego samego.
Diff ma pokazac co sie dokladnie zmienilo i tylko to — zeby byl czytelny."* Obie sciezki robily
wtedy cos innego, kazda inaczej zle, i obie da sie zmierzyc.

| | strona `/diff/` (routine 22:05) | artefakt `Microsoft SOC Delta` (sched task) |
|---|---|---|
| rozmiar | 3 635 058 B | 3 700 020 B |
| z tego blok `soc-catalog` | 3,3 MB | **3 262 937 B** |
| przegladarka katalogu, ktora tego JSON-a uzywa | **zero** `data-catalog` | **zero** `data-catalog` |
| skrypty zachowania | **3** (brak powloki) | 6 |
| `<nav class="anchors">` po zaladowaniu | **pusty** | — |
| zakladki widoczne dla czytelnika | **zero**, oba panele `hidden` | 2 |
| wiersze tresci | 9 | 9 |
| bledy konsoli | **zero** | zero |

Czytelnik dostal wiec masthead i pusta strone, a w artefakcie — dziewiec wierszy tresci ubranych
w 3,7 MB powloki briefu. **Przyczyny sa dwie i sa rozlaczne.**

**Przyczyna pierwsza, mechaniczna: `parts()` brala `clean[-3:]`.** Regula pochodzila z czasow,
gdy skrypty zachowania byly trzy. Po dolozeniu SKRYPTU 4 (§5y) „trzy ostatnie" to overview,
katalog i agregaty — a POWLOKA, ta ktora buduje pasek zakladek, wypadala. Skrypty nie zglaszaja
bledow (sekcja LAYOUT), wiec strona wyszla cicho pusta, a `verify_diff` przepuscil ja, bo pytal
`scripts < 3`. Oba miejsca sa juz poprawione w §0a: `parts()` bierze WSZYSTKIE bloki niebedace
nadmiarowym dopasowaniem, a obie bramki zadaja `>= 4`. Zmierzone po poprawce na tym samym
wejsciu: 4 skrypty (31 508 / 36 661 / 58 248 / 15 207 B), powloka obecna, pasek zakladek
`["Overview","What changed"]`, panel `tab-overview` widoczny.

**Przyczyna druga, i to ona jest wlasciwym tematem tej sekcji: strona zmian byla LUSTREM.**
Lustro z definicji powtarza to, co odbija. Zeby pokazac roznice, trzeba je POLICZYC.

### Regula

**Strona `/diff/` i artefakt `Microsoft SOC Delta` powstaja z `make_diff.py`, ktory porownuje DWA
STANY i nie kopiuje niczego ze strony.** Wejscie to dwa pliki `site/data/RRRR-MM-DD.json` albo dwa
artefakty, z ktorych skrypt sam wyjmuje `soc-brief-state` i `soc-catalog`.

Strona zmian **nie ma**: zakladek, paneli `.tabpanel`, przegladarki katalogu, blokow
`<script type="application/json">` ani skryptow powloki. Nie wozi stanu, bo go nie renderuje —
to jest ta roznica miedzy 11 638 B a 3 635 058 B. Ma **jeden ekran, przewijany**, w tej kolejnosci:

1. **Masthead** — `Microsoft SOC — what changed`, `<data poprzednia> → <data biezaca>`, etykieta
   porownania (`morning pass 06:35 → evening pass 21:14`), godzina policzenia, autor i link do `/`.
2. **Pigulki liczbowe** — `N added`, `N removed`, `N changed`, `N deadlines moved`,
   `±N Graph permissions`, `±N role entries`, `N items in state (was M)`. Zero jest wartoscia
   poprawna i tez sie pokazuje.
3. **Added** — `Product | Item | Status | Published | Deadline | Weight | Source`, sortowane
   `tier0Touch` malejaco, `socWeight` rosnaco, termin rosnaco (§5p).
4. **Removed** — to samo bez `Status`. **Usuniecie jest znaleziskiem**, nie sprzataniem.
5. **Changed, field by field** — JEDEN WIERSZ NA POLE: `Item | Field | before → after | Source`,
   stara wartosc w `<del>`, nowa w `<ins>`. Pola porownywane, w tej kolejnosci: `deadline`,
   `status`, `published`, `tier`, `socWeight`, `tier0Touch`, `title`, `officialTitle`,
   `reference`, `fingerprint`, `url`, `linkStatus`, `product`, `area`.
6. **Catalog** — dodane / usuniete nazwy uprawnien i rol oraz wpisy, ktorym ruszyl
   `kind`, `docStatus`, `version`, `changed` albo `serviceStatus`.
7. **Stopka** — laczna liczba roznic albo zdanie, ze nie ma zadnej.

**Kubelek pusty mowi to zdaniem, nie znika.** „Nothing was removed." jest wynikiem; brak sekcji
zostawia czytelnika z pytaniem, czy przebieg patrzyl.

### Zmierzone 2 wrzesnia 2026

| wejscie | wyjscie | tresc |
|---|---|---|
| ranek 06:35 → wieczor 21:14 (ten sam dzien) | **11 638 B** | 6 added, 0 removed, 6 changed, katalog bez zmian, 12 wierszy |
| brief 31 sierpnia → brief 2 wrzesnia | **105 702 B** | 34 added, 157 changed, +26 uprawnien Graph, 377 wierszy |
| ten sam stan po obu stronach | **6 216 B** | same zera i zdanie „No difference at all between the two states. Somebody looked; nothing moved." |

Strona dnia jest wiec **312 razy mniejsza** od lustra, ktore zastapila, i pokazuje wylacznie to,
co sie ruszylo: szesc pozycji, ktorym termin przeszedl w `recently-elapsed` — passkeys, wycofanie
SMS i polaczen glosowych, Entra Connect Sync 2.5.76.0, wzbogacanie sygnalu sieciowego w Defender
XDR, Graph Toolkit i CLI, klient Azure VPN dla Linuksa — kazda jako `deadline-under-60-days` →
`recently-elapsed`, z linkiem do zrodla.

Render headless, jasny i ciemny, 1400x1100 i 390x844: **zero bledow konsoli i strony**,
`scrollWidth === clientWidth` w obu szerokosciach, `<del>` i `<ins>` obecne w liczbie rownej
liczbie zmienionych pol. Dwa bledy wlasnego renderu znalezione i poprawione w tym samym przebiegu:
naglowek tabeli drukowal doslownie `BEFORE &RARR; AFTER`, bo `esc()` szedl takze po MOICH
naglowkach (naglowki nie sa danymi — nie escapujemy ich), a selektor `.t0` trafial nie tylko
w chip, ale i w `<tr class="t0">`, malujac caly wiersz na rozowo (teraz `span.t0`).

### Skrypt

Zapisz do `/tmp/make_diff.py` i uruchom:

```
python3 /tmp/make_diff.py <poprzedni> <biezacy> <wyjscie.html> [--home /] [--label "..."]
```

**Kod wyjscia 1 znaczy NIE PUBLIKUJ** — wbudowana bramka `verify()` odrzuca strone, ktora ma
zakladki, kontener katalogu, blok JSON, brak ktorejs z czterech sekcji, brak linku powrotnego,
podwojny DOCTYPE, wiecej niz 900 kB albo wiersz w sekcji `changed`, ktory nie pokazuje roznicy.

**Licznika `<del>` NIE porownuje sie z licznikiem `<ins>`** — to byla moja pierwsza, falszywa
asercja w prompcie routine. Pole, ktorego wczesniej nie bylo, ma po lewej `not set`, a `<ins>`
po prawej; na porownaniu 31 sierpnia z 2 wrzesnia daje to 25 `<del>` przy 250 wierszach.
Poprawne pytanie brzmi: **czy KAZDY wiersz niesie `<del>` albo `<ins>`** — zmierzone 250 z 250,
225 z samym `<ins>`, zero bez jednego i drugiego. Kontrola regresji: strona z jednym wierszem
pozbawionym obu znacznikow jest odrzucana z jego liczba.

```python
#!/usr/bin/env python3
"""make_diff.py — strona ZMIAN liczona z danych, nie odbijana z artefaktu.

  python3 make_diff.py <poprzedni.json|.html> <biezacy.json|.html> <plik-wyjsciowy.html> [--home /] [--label "..."]

Wejscie: dwa stany. Kazdy moze byc plikiem `site/data/<data>.json` (obiekt z kluczami
`soc-brief-state` i opcjonalnie `soc-catalog`) ALBO gotowa strona/artefaktem HTML, z ktorego
skrypt sam wyjmie oba bloki JSON.

Wyjscie: mala, samodzielna strona pokazujaca WYLACZNIE roznice: co przybylo, co ubylo,
co sie zmienilo pole po polu. Bez dziewieciu zakladek, bez przegladarki katalogu i bez
kopiowania megabajtow JSON, ktorych taka strona nie uzywa.
"""
import sys, os, re, json, html, datetime

# ---------- wejscie ----------

def load_state(path):
    raw = open(path, encoding="utf-8").read()
    if path.lower().endswith(".json"):
        d = json.loads(raw)
        if "soc-brief-state" in d:
            return d.get("soc-brief-state") or {}, d.get("soc-catalog") or {}
        if "items" in d:
            return d, {}
        raise SystemExit("FAIL: %s nie ma ani soc-brief-state ani items" % path)
    def blk(name):
        m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % name, raw, re.S)
        return json.loads(m.group(1)) if m else {}
    st = blk("soc-brief-state")
    if not st:
        raise SystemExit("FAIL: brak bloku soc-brief-state w %s" % path)
    return st, blk("soc-catalog")

# ---------- porownanie ----------

# Pola, ktorych zmiana jest ZMIANA MERYTORYCZNA. Kolejnosc = kolejnosc wierszy w tabeli.
FIELDS = [
    ("deadline",     "Deadline"),
    ("status",       "Status"),
    ("published",    "Published"),
    ("tier",         "Tier"),
    ("socWeight",    "SOC weight"),
    ("tier0Touch",   "Tier 0"),
    ("title",        "Title"),
    ("officialTitle","Microsoft's title"),
    ("reference",    "Reference"),
    ("fingerprint",  "Substance"),
    ("url",          "Source link"),
    ("linkStatus",   "Link status"),
    ("product",      "Product"),
    ("area",         "Area"),
]

def norm(v):
    if v is None: return ""
    if isinstance(v, bool): return "yes" if v else "no"
    return str(v).strip()

def diff_items(prev, curr):
    p = {i.get("id"): i for i in (prev.get("items") or []) if i.get("id")}
    c = {i.get("id"): i for i in (curr.get("items") or []) if i.get("id")}
    added   = [c[k] for k in c if k not in p]
    removed = [p[k] for k in p if k not in c]
    changed = []
    for k in c:
        if k not in p: continue
        deltas = [(lab, norm(p[k].get(f)), norm(c[k].get(f)))
                  for f, lab in FIELDS if norm(p[k].get(f)) != norm(c[k].get(f))]
        if deltas: changed.append((c[k], deltas))
    return added, removed, changed, len(p), len(c)

def diff_catalog(prev, curr, which):
    pe = {e.get("name"): e for e in (prev.get(which) or []) if e.get("name")}
    ce = {e.get("name"): e for e in (curr.get(which) or []) if e.get("name")}
    add = sorted(set(ce) - set(pe))
    rem = sorted(set(pe) - set(ce))
    mod = []
    for n in sorted(set(pe) & set(ce)):
        for f in ("kind", "docStatus", "version", "changed", "serviceStatus"):
            a, b = norm(pe[n].get(f)), norm(ce[n].get(f))
            if a != b:
                mod.append((n, f, a, b))
    return add, rem, mod, len(pe), len(ce)

# ---------- render ----------

def esc(x): return html.escape(norm(x))

def wkey(it):
    w = it.get("socWeight")
    w = w if isinstance(w, int) else 9
    d = norm(it.get("deadline")) or "9999-99-99"
    return (0 if it.get("tier0Touch") else 1, w, d)

def a_src(it):
    u = norm(it.get("url"))
    if not u: return '<span class="none">no link</span>'
    return '<a href="%s" target="_blank" rel="noopener">Source</a>' % esc(u)

def name_cell(it):
    out = "<b>%s</b>" % esc(it.get("title") or it.get("id"))
    ot = norm(it.get("officialTitle"))
    if ot and ot != norm(it.get("title")):
        out += '<br><span class="sub">%s</span>' % esc(ot)
    ref = norm(it.get("reference"))
    if ref: out += '<br><span class="ref">%s</span>' % esc(ref)
    return out

def weight_cell(it):
    w = it.get("socWeight")
    t0 = ' <span class="t0">tier 0</span>' if it.get("tier0Touch") else ""
    return ("w%s" % w if isinstance(w, int) else '<span class="none">—</span>') + t0

def table(head, rows, empty):
    if not rows:
        return '<p class="empty">%s</p>' % esc(empty)
    th = "".join("<th>%s</th>" % h for h in head)   # naglowki sa nasze, nie z danych
    tb = "".join("<tr%s>%s</tr>" % (r[0], "".join("<td>%s</td>" % c for c in r[1])) for r in rows)
    return '<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tb)

def cap(lst, n, what):
    if len(lst) <= n: return lst, ""
    return lst[:n], '<p class="more">… and %d more %s. The full list is in the brief.</p>' % (len(lst) - n, what)

CSS = """
:root{color-scheme:light;--bg:#f7f7f4;--surface:#fff;--surface2:#f0f0ec;--text:#141413;--muted:#6b6a66;
 --border:#ddddd6;--ok:#0d6236;--ok-soft:#dbf0e3;--bad:#a3131f;--bad-soft:#fbe3e4;--warn:#8a5a00;
 --warn-soft:#fdf0d5;--accent:#2f5fd0;--accent-soft:#e2eafb;--del-bg:#fbe3e4;--del-fg:#8a1220;
 --ins-bg:#dbf0e3;--ins-fg:#0b5730}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#16171a;--surface:#1e2024;
 --surface2:#25272c;--text:#ecebe6;--muted:#a3a29c;--border:#33363c;--ok:#63d495;--ok-soft:#0f3323;
 --bad:#f28b8b;--bad-soft:#3a1618;--warn:#e8bd6b;--warn-soft:#3a2c10;--accent:#8fb0ff;--accent-soft:#1c2740;
 --del-bg:#3a1618;--del-fg:#f0a0a0;--ins-bg:#0f3323;--ins-fg:#8fe0b4}}
:root[data-theme=dark]{color-scheme:dark;--bg:#16171a;--surface:#1e2024;--surface2:#25272c;--text:#ecebe6;
 --muted:#a3a29c;--border:#33363c;--ok:#63d495;--ok-soft:#0f3323;--bad:#f28b8b;--bad-soft:#3a1618;
 --warn:#e8bd6b;--warn-soft:#3a2c10;--accent:#8fb0ff;--accent-soft:#1c2740;--del-bg:#3a1618;
 --del-fg:#f0a0a0;--ins-bg:#0f3323;--ins-fg:#8fe0b4}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);
 font:15px/1.5 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.wrap{max-width:1120px;margin:0 auto;padding:20px 16px 64px}
header.top{background:var(--surface);border-bottom:1px solid var(--border);padding:18px 16px}
header .in{max-width:1120px;margin:0 auto}
h1{font-size:22px;margin:0 0 6px}
.dateline{margin:0;color:var(--muted);font-size:13.5px}
.dateline a{color:var(--accent)}
.counts{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0;padding:0;list-style:none}
.counts li{background:var(--surface2);border:1px solid var(--border);border-radius:999px;
 padding:6px 12px;font-size:13.5px;white-space:nowrap}
.counts li b{font-size:16px}
.counts li.add{background:var(--ins-bg);border-color:var(--ok);color:var(--ins-fg)}
.counts li.rem{background:var(--del-bg);border-color:var(--bad);color:var(--del-fg)}
.counts li.chg{background:var(--warn-soft);border-color:var(--warn);color:var(--warn)}
section{margin:26px 0 0}
h2{font-size:16px;margin:0 0 2px}
.note{color:var(--muted);font-size:13.5px;margin:0 0 10px}
.tw{overflow-x:auto;border:1px solid var(--border);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{position:sticky;top:0;background:var(--surface2);text-align:left;font-size:12px;
 text-transform:uppercase;letter-spacing:.04em;color:var(--muted);padding:9px 10px;
 border-bottom:1px solid var(--border);white-space:nowrap}
td{padding:9px 10px;border-bottom:1px solid var(--border);vertical-align:top}
tbody tr:last-child td{border-bottom:0}
tr.t0 td:first-child{box-shadow:inset 3px 0 0 var(--bad)}
.sub{color:var(--muted);font-size:12.5px}
.ref{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--accent)}
.none{color:var(--muted)}
span.t0{background:var(--bad-soft);color:var(--bad);border-radius:999px;padding:1px 7px;
 font-size:11.5px;font-weight:600;white-space:nowrap}
del{background:var(--del-bg);color:var(--del-fg);text-decoration:line-through;
 padding:1px 5px;border-radius:4px}
ins{background:var(--ins-bg);color:var(--ins-fg);text-decoration:none;padding:1px 5px;border-radius:4px}
.arrow{color:var(--muted);padding:0 4px}
.field{font-weight:600;white-space:nowrap}
.empty{background:var(--surface);border:1px dashed var(--border);border-radius:10px;
 padding:12px 14px;color:var(--muted);margin:0}
.more{color:var(--muted);font-size:13px;margin:8px 0 0}
a{color:var(--accent)}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;
 background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:1px 5px}
footer{margin:36px 0 0;padding-top:14px;border-top:1px solid var(--border);color:var(--muted);font-size:13px}
@media (max-width:760px){.counts li{white-space:normal}h1{font-size:19px}}
"""

def build(prev_st, prev_cat, curr_st, curr_cat, home, label, when):
    added, removed, changed, np_, nc = diff_items(prev_st, curr_st)
    gadd, grem, gmod, gp, gc = diff_catalog(prev_cat, curr_cat, "graph")
    radd, rrem, rmod, rp, rc = diff_catalog(prev_cat, curr_cat, "roles")

    added.sort(key=wkey); removed.sort(key=wkey)
    changed.sort(key=lambda t: wkey(t[0]))
    dl_moved = [(i, d) for i, d in changed if any(l == "Deadline" for l, _, _ in d)]

    prev_d = norm(prev_st.get("briefDate")) or "previous"
    curr_d = norm(curr_st.get("briefDate")) or "current"

    out = []
    out.append('<header class="top"><div class="in"><h1>Microsoft SOC &mdash; what changed</h1>')
    out.append('<p class="dateline">%s &rarr; %s &middot; %s &middot; compared %s Warsaw &middot; '
               'Piotr Wisniewski &middot; <a href="%s">Back to the full brief</a></p>'
               % (esc(prev_d), esc(curr_d), esc(label), esc(when), esc(home)))
    out.append('<ul class="counts">')
    out.append('<li class="add"><b>%d</b> added</li>' % len(added))
    out.append('<li class="rem"><b>%d</b> removed</li>' % len(removed))
    out.append('<li class="chg"><b>%d</b> changed</li>' % len(changed))
    out.append('<li><b>%d</b> deadlines moved</li>' % len(dl_moved))
    out.append('<li><b>%+d</b> Graph permissions <span class="sub">%d &rarr; %d</span></li>' % (gc - gp, gp, gc))
    out.append('<li><b>%+d</b> role entries <span class="sub">%d &rarr; %d</span></li>' % (rc - rp, rp, rc))
    out.append('<li><b>%d</b> items in state <span class="sub">was %d</span></li>' % (nc, np_))
    out.append('</ul></div></header><div class="wrap">')

    # --- added
    rows = [(' class="t0"' if i.get("tier0Touch") else "",
             [esc(i.get("product")), name_cell(i), esc(i.get("status")),
              esc(i.get("published")), esc(i.get("deadline")) or '<span class="none">none stated</span>',
              weight_cell(i), a_src(i)]) for i in added]
    rows, more = cap(rows, 120, "added items")
    out.append('<section id="added"><h2>Added since %s</h2>'
               '<p class="note">In the current state and not in the previous one. Heaviest first: '
               'tier 0, then SOC weight, then deadline.</p>%s%s</section>'
               % (esc(prev_d), table(["Product", "Item", "Status", "Published", "Deadline", "Weight", "Source"],
                                     rows, "Nothing was added. That is a result, not a gap."), more))

    # --- removed
    rows = [("", [esc(i.get("product")), name_cell(i), esc(i.get("published")),
                  esc(i.get("deadline")) or '<span class="none">none stated</span>',
                  weight_cell(i), a_src(i)]) for i in removed]
    rows, more = cap(rows, 120, "removed items")
    out.append('<section id="removed"><h2>Removed</h2>'
               '<p class="note">Carried in the previous state and gone from the current one. '
               'A removal is a finding: either the source dropped it or this brief retracted it.</p>%s%s</section>'
               % (table(["Product", "Item", "Published", "Deadline", "Weight", "Source"],
                        rows, "Nothing was removed."), more))

    # --- changed, field by field
    rows = []
    for i, deltas in changed:
        for n, (lab, a, b) in enumerate(deltas):
            first = (n == 0)
            rows.append((' class="t0"' if (first and i.get("tier0Touch")) else "",
                         [name_cell(i) if first else '<span class="none">&#8942;</span>',
                          '<span class="field">%s</span>' % esc(lab),
                          ('<del>%s</del>' % esc(a) if a else '<span class="none">not set</span>')
                          + '<span class="arrow">&rarr;</span>'
                          + ('<ins>%s</ins>' % esc(b) if b else '<span class="none">cleared</span>'),
                          a_src(i) if first else ""]))
    rows, more = cap(rows, 250, "changed fields")
    out.append('<section id="changed"><h2>Changed, field by field</h2>'
               '<p class="note">Same <code>id</code> in both states, different value. Old struck through, '
               'new highlighted &mdash; the difference is shown, not described.</p>%s%s</section>'
               % (table(["Item", "Field", "Before &rarr; after", "Source"], rows,
                        "No field moved on any item carried across both states."), more))

    # --- catalog
    def catrows(add, rem, mod, name):
        r = []
        for n in add[:60]: r.append(("", ['<ins>added</ins>', "<code>%s</code>" % esc(n), ""]))
        for n in rem[:60]: r.append(("", ['<del>removed</del>', "<code>%s</code>" % esc(n), ""]))
        for n, f, a, b in mod[:60]:
            r.append(("", ["changed", "<code>%s</code>" % esc(n),
                           '<span class="field">%s</span> <del>%s</del><span class="arrow">&rarr;</span><ins>%s</ins>'
                           % (esc(f), esc(a) or "not set", esc(b) or "cleared")]))
        extra = len(add) + len(rem) + len(mod) - len(r)
        return r, ('<p class="more">… and %d more %s changes.</p>' % (extra, name) if extra > 0 else "")

    gr, gmore = catrows(gadd, grem, gmod, "Graph")
    rr, rmore = catrows(radd, rrem, rmod, "role")
    out.append('<section id="catalog"><h2>Catalog</h2>'
               '<p class="note">Graph permissions %d &rarr; %d (+%d / &minus;%d, %d entries edited); '
               'roles %d &rarr; %d (+%d / &minus;%d, %d edited).</p>%s%s%s%s</section>'
               % (gp, gc, len(gadd), len(grem), len(gmod), rp, rc, len(radd), len(rrem), len(rmod),
                  table(["What", "Graph permission", "Detail"], gr, "No Graph permission changed."), gmore,
                  table(["What", "Role", "Detail"], rr, "No role changed."), rmore))

    total = len(added) + len(removed) + len(changed) + len(gadd) + len(grem) + len(gmod) + len(radd) + len(rrem) + len(rmod)
    out.append('<footer>%s &middot; Piotr Wisniewski &middot; %s Warsaw &middot; '
               'computed from the two state blocks, not copied from the brief. '
               '<a href="%s">Back to the full brief</a></footer></div>'
               % (("%d differences in total." % total) if total else
                  "No difference at all between the two states. Somebody looked; nothing moved.",
                  esc(when), esc(home)))
    body = "\n".join(out)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>Microsoft SOC &mdash; what changed %s</title>\n<style>%s</style>\n</head>\n<body>\n%s\n</body>\n</html>\n'
            % (esc(curr_d), CSS, body))

# ---------- bramka ----------

def verify(page):
    from html.parser import HTMLParser
    class P(HTMLParser):
        def __init__(s):
            super().__init__(convert_charrefs=True)
            s.ids=set(); s.rows=0; s.panels=0; s.cat=0; s.jsonb=0; s.doct=0; s.href=set(); s.dels=0; s.inss=0
        def handle_decl(s,d):
            if d.lower().startswith("doctype"): s.doct+=1
        def handle_starttag(s,t,a):
            a=dict(a); cls=(a.get("class") or "").split()
            if a.get("id"): s.ids.add(a["id"])
            if a.get("href"): s.href.add(a["href"])
            if t=="tr": s.rows+=1
            if t=="div" and "tabpanel" in cls: s.panels+=1
            if t=="div" and a.get("data-catalog"): s.cat+=1
            if t=="del": s.dels+=1
            if t=="ins": s.inss+=1
            if t=="script" and (a.get("type") or "")=="application/json": s.jsonb+=1
    p=P(); p.feed(page); e=[]
    for need in ("added","removed","changed","catalog"):
        if need not in p.ids: e.append("brak sekcji %s" % need)
    if p.doct!=1: e.append("DOCTYPE = %d, ma byc 1" % p.doct)
    if p.panels: e.append("strona zmian nie ma zakladek, a ma %d .tabpanel" % p.panels)
    if p.cat: e.append("strona zmian nie ma przegladarki katalogu, a ma %d" % p.cat)
    if p.jsonb: e.append("strona zmian nie wozi blokow JSON, a ma %d" % p.jsonb)
    if len(page.encode()) > 900_000: e.append("strona ma %d B — diff ma byc maly" % len(page.encode()))
    if not any(h in ("/", "/diff/", "..") or h.startswith("http") for h in p.href):
        e.append("brak linku powrotnego")
    # KAZDY wiersz sekcji `changed` pokazuje roznice, a nie ja opisuje. Licznik <del> NIE musi
    # rownac sie licznikowi <ins>: pole, ktorego wczesniej nie bylo, ma samo <ins> i zdanie
    # „not set" po lewej. Zmierzone: 250 wierszy, 225 z samym <ins>, zero bez jednego i drugiego.
    m = re.search(r'<section id="changed">.*?</section>', page, re.S)
    if m:
        rows = [r for r in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(0), re.S) if "<td" in r]
        bad = [r for r in rows if "<del>" not in r and "<ins>" not in r]
        if bad: e.append("%d wierszy w 'changed' nie pokazuje roznicy (<del>/<ins>)" % len(bad))
    return e

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = sys.argv[1:]
    home = opts[opts.index("--home") + 1] if "--home" in opts else "/"
    label = opts[opts.index("--label") + 1] if "--label" in opts else "morning pass → afternoon pass"
    if len(args) < 3:
        raise SystemExit("uzycie: make_diff.py <poprzedni> <biezacy> <wyjscie.html> [--home /] [--label ...]")
    ps, pc = load_state(args[0])
    cs, cc = load_state(args[1])
    when = datetime.datetime.now().strftime("%H:%M")
    page = build(ps, pc, cs, cc, home, label, when)
    errs = verify(page)
    if errs:
        print("PRZEBIEG NIEUDANY - nie publikuj:")
        for x in errs: print("   -", x)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(os.path.abspath(args[2])), exist_ok=True)
    open(args[2], "w", encoding="utf-8").write(page)
    print("OK  %s  %d B" % (args[2], len(page.encode())))
```

### Gdzie to wchodzi w dzien

| godzina (Warsaw) | co | z czego liczy |
|---|---|---|
| 06:00 | sched task poranny publikuje artefakt `Microsoft SOC Brief <data>` | — |
| 07:00 | routine odbija artefakt do `site/index.html` i zapisuje `site/data/<data>.json` (§0a) | — |
| 21:00 | sched task popoludniowy republikuje TEN SAM brief z sekcja `#pmdelta`, **a potem publikuje `Microsoft SOC Delta <data>` = wyjscie `make_diff.py`** | stan porannego artefaktu → stan po tym passie |
| 21:30 | routine zmian pisze `site/diff/index.html` = wyjscie `make_diff.py` | `site/data/<poprzedni>.json` → stan dzisiejszego artefaktu |

**Routine zmian nie odbija juz artefaktu Delta.** Liczy strone sama z dwoch stanow, wiec jest
odporna na to, czy sched task zdazyl i co dokladnie opublikowal; gdy dzisiejszego artefaktu nie
ma, porownuje dwa ostatnie pliki `site/data/*.json` i mowi w odpowiedzi, ze porownala pliki
zamiast artefaktu. Tryb `--diff` w `mirror_artifact.py` (§0a) zostaje wylacznie jako awaryjne
lustro i jest poprawiony, ale **nie jest juz domyslna sciezka**.

**Sekcja `#pmdelta` w briefie zostaje bez zmian.** To jest zapis „co znalazl ten pass" w samym
briefie i §4 taska popoludniowego dalej go wymaga. Strona zmian jest czyms innym: samodzielnym,
malym dokumentem dla kogos, kto chce zobaczyc wylacznie roznice.

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

Nowe od 1 wrzesnia 2026, kazda z realnego zgloszenia wlasciciela: **oba pola szukania —
`input.tbar-search` i `.cat-searchwrap .cat-search` — maja TO SAMO, nieprzezroczyste tlo rozne od
`--surface` w obu motywach** (§5k; regula w pliku nie wystarcza, liczy sie wartosc wyliczona);
**w `tab-new`, `tab-today` i `tab-deadlines` istnieje `<select>`, ktorego pierwsza opcja brzmi
`All source`** (§5w); **kazda zakladka tresciowa ma co najmniej trzy `.aggwrap figure.chart` i
dokladnie trzy `.aggbtn`, a klikniecie „Tydzien" i „Dzien" zmienia liczbe slupkow osi czasu** (§5y).

Dodatkowo przy **390x844** (telefon): **dla KAZDEJ z dziewieciu zakladek po kolei `document.documentElement.scrollWidth === clientWidth`**
(§5x — sprawdzanie jednej zakladki przepuscilo Today 556 i Deadlines 482 przy ekranie 390);
`getComputedStyle(document.querySelector("header.top")).position` zwraca `static`; `.counts` miesci sie w jednym wierszu; po `window.scrollBy(0,600)` naglowek jest
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
.tbar input[type=search].tbar-search,
.cat-searchwrap input.cat-search{background:var(--ok-soft);border-color:var(--ok);border-width:1.5px;font-weight:500}
.tbar input[type=search].tbar-search::placeholder,
.cat-searchwrap input.cat-search::placeholder{color:var(--muted);font-weight:400}
.tbar input[type=search].tbar-search:focus,
.cat-searchwrap input.cat-search:focus{background:var(--surface);border-color:var(--ok);box-shadow:0 0 0 3px var(--ok-soft)}
.cat-searchicon{color:var(--ok)}
```

**SELEKTOR MUSI DOROWNAC SPECYFICZNOSCIA POWLOCE — inaczej reguly nie widac mimo ze jest w pliku.**
Zmierzone 1 wrzesnia 2026 na `site/index.html`: blok §5k **byl w arkuszu**, a mimo to pole szukania
tabeli mialo tlo `rgb(255,255,255)` — czyste `--surface`. Powloka deklaruje je jako
`.tbar input[type=search].tbar-search` (specyficznosc 0,2,2), a nasza regula brzmiala
`.tbar-search` (0,1,0). Bycie ostatnim w arkuszu **nie wygrywa z wyzsza specyficznoscia** — kaskada
rozstrzyga kolejnoscia dopiero przy remisie. Drugie pole, `.cat-search`, w ogole nie bylo zielone:
mialo `rgb(226,234,251)`, czyli `--accent-soft`, bo przebieg wpisal tam zmienne NIEBIESKIE zamiast
`--ok`. Po poprawce oba pola daja `rgb(219,240,227)` na obwodce `rgb(13,98,54)` w jasnym motywie
i `rgb(15,51,35)` na `rgb(99,212,149)` w ciemnym — **identycznie**, co jest cala pointa tej reguly.

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

## 5p. Waga bezpieczenstwa jest POLEM, nie zdaniem w `sec-note`

31 sierpnia 2026 wlasciciel wskazal dwie rzeczy naraz i obie sa jednym bledem.

**Pierwsza.** Artykul „Provisioning users and groups from Entra ID into on-premises Active Directory"
(`entra-cloudsync-provision-to-ad`, opublikowany 28 sierpnia) byl na stronie w New, w exec summary
i w deep dive — **i w zadnym z tych miejsc nie odpowiadal na pytanie, po co SOC ma tam patrzec.**
Kierunek tozsamosci hybrydowej sie odwrocil: chmura zapisuje do AD DS z zachowanym SID-em, a host
agenta provisioningu staje sie aktywem tier 0. To jest najpowazniejsza pozycja okna i **nie miala
karty w Top 7 ani wiersza w Pick of the day.**

**Druga.** W Pick of the day pierwszym wierszem od gory bylo „Azure VPN Client for Linux retirement".

**Przyczyna jest jedna i jest mechaniczna, nie gustowa.** Zmierzone tego dnia na `site/index.html`:
pozycja Cloud Sync ma `deadline: null`. Sortowanie Top N i Pick of the day idzie po dniach do terminu,
a Azure VPN Client mial termin najblizszy ze wszystkich. **Pozycja bez terminu nie moze wygrac zadnego
z tych sortowan, choćby byla najciezsza w oknie** — dokladnie tak jak w §5q wpis z `changed: null`
wypadal z kazdego okna filtra. Ta sama choroba, inna kolumna.

Zdanie „Top N wazy sie bezpieczenstwem" stalo w tej sekcji od 31 sierpnia rano i przebieg je przeczytal.
Nie pomoglo, bo **regula bez pola do policzenia jest sugestia** (§0b). Dlatego waga jest teraz liczba
w stanie.

### `socWeight` — liczba 1-7 na KAZDEJ pozycji stanu

Drabina jest ta sama co dotad, ale zapisujesz ja jako `socWeight` przy pozycji, nie trzymasz w glowie:

| `socWeight` | obszar | co tu nalezy |
|---|---|---|
| **1** | **Tozsamosc** | Entra ID, Conditional Access, metody uwierzytelniania, PIM, Identity Protection, role katalogowe, Entra Connect / Cloud Sync, uprawnienia Graph |
| **2** | **Wykrywanie i reakcja** | Defender XDR, MDE, MDI, MDO, MDCA, Sentinel: nowe detekcje, zmiany schematu hunting, retencja, zmiany w alertach, wycofanie zrodla logow |
| **3** | **Dane i zgodnosc** | Purview: DLP, audyt, retencja, Insider Risk |
| **4** | **Zarzadzanie punktem koncowym** | Intune: baseline'y, compliance, ASR, szyfrowanie |
| **5** | **Powierzchnia dzierzawy** | M365 admin, Exchange Online, SharePoint, Teams: zgody, uprawnienia, udostepnianie zewnetrzne, przeplyw poczty |
| **6** | **Windows i cykl zycia** | konce wsparcia, wymuszone upgrade'y |
| **7** | **Azure jako platforma** | nowy SKU zapory, region, opcja wydajnosci, klient VPN — **material na New, nie na Top N** |

**Azure nie znika ze strony i nigdy nie znika po cichu.** Wchodzi z waga 7, czyli jest w New, jest
w deep dive i moze byc w Pick of the day — ale na dole, nie na gorze. Wyjatek jest jeden i awansuje
pozycje do wagi jej faktycznego skutku: **zmiana Azure, ktora rusza kontrole bezpieczenstwa, zrodlo
logow albo granice tozsamosci, nie jest „Azure"** — Azure Monitor HTTP Data Collector API to wycofanie
zrodla logow, czyli waga 2, i slusznie ma karte w Top 7.

### `tier0Touch` — kryterium, ktorego drabina sama nie zlapie

`socWeight` mowi, w ktorym obszarze rzecz sie dzieje. Nie mowi, jak gleboko. Dlatego kazda pozycja
niesie drugie pole, `tier0Touch: true|false`, i jest `true`, gdy zmiana **tworzy albo zmienia sciezke
zapisu do aktywa tier 0**: AD DS, kontroler domeny, host agenta synchronizacji lub provisioningu,
urzad certyfikacji, rola rownowazna Global Adminowi, federacja. Przy `true` dopisujesz `tier0Note`
jednym zdaniem, co konkretnie zyskuje prawo zapisu i skad.

Zmierzone 31 sierpnia: `tier0Touch: true` maja co najmniej trzy pozycje okna —
`entra-cloudsync-provision-to-ad` (Entra ID zapisuje uzytkownikow, grupy i czlonkostwa do AD DS
z zachowanym SID-em), `exchange-hybrid-les-writeback` (`Entra2ADExchangeOnlineAttributeWriteback`
wlewa atrybuty chmurowe do lokalnego AD) i `eds-samaccountname-onpremises`. **Zadna z nich nie miala
terminu, wiec zadna nie mogla wygrac sortowania po terminie.** To jest ta luka.

### Jak to zmienia sortowanie — trzy miejsca, konkretnie

1. **Top N (§8 A)** — klucz to `(tier0Touch malejaco, socWeight rosnaco, pilnosc rosnaco)`, gdzie
   pilnosc to dni do terminu, a pozycja bez terminu dostaje pilnosc rowna dniom od publikacji.
   **Pozycja bez terminu przestaje byc niesortowalna** — konczy na koncu swojej wagi, nie poza tabela.
2. **Pick of the day (§8 B)** — nadal DOKLADNIE jeden wiersz na technologie, zeby cichy produkt
   pokazal, ze byl sprawdzony. Zmienia sie kolejnosc wierszy: `socWeight` rosnaco, w obrebie wagi
   dni do terminu rosnaco, niedatowane na koncu. Wiersz Azure zostaje, ale na dole tabeli.
3. **New (§8 E) i deep dive (§8 H)** — kolejnosc produktow idzie drabina, nie alfabetem. Podloga
   pokrycia z §5u obowiazuje bez zmian: **nic nie wypada, zmienia sie tylko kolejnosc.**

### Kryterium rozstrzygajace i zdanie w `sec-note`

Gdy dwie pozycje waza tak samo: **czy SOC musi cos zrobic albo cos przeoczy?** Termin w 30 dniach,
wymagana akcja administratora, zmiana domyslna wlaczana bez zgody, nowe uprawnienie o zasiegu
dzierzawy, wycofanie zrodla logow, **nowa sciezka zapisu do tier 0** — kazde z tych bije nowosc
funkcjonalna.

`sec-note` sekcji Top N mowi, czym wazyla, **liczbami z tego przebiegu**: *„Wybor 7 z 157 pozycji
stanu. Wazenie: tier 0 najpierw (3 pozycje), potem drabina bezpieczenstwa — 41 pozycji tozsamosci,
30 wykrywania, 15 Azure. Azure wchodzi z waga 7 i jest w New."*

### Karta Top N niesie `data-id` — inaczej niczego nie da sie sprawdzic

Zmierzone 31 sierpnia: siedem kart Top N otwiera sie jako `<article class="card hot">` i **zadna nie
niesie identyfikatora pozycji stanu**. Bez niego nie da sie odpowiedziec kodem na pytanie „czy pozycja
`entra-cloudsync-provision-to-ad` dostala karte" — a pytanie bez odpowiedzi w kodzie wraca jako
sugestia. Kazda karta ma wiec `data-id` rowne `id` swojej pozycji stanu:

```html
<article class="card hot" data-id="entra-cloudsync-provision-to-ad">
```

Atrybut jest obojetny dla powloki — skrypt 2 liczy `.card` po klasie, nie po atrybutach — a §5m juz
wymaga, zeby kazdy wiersz Today mial pare w New po `id`, wiec to ta sama dyscyplina. **Sekcja `top5`
dostaje tez `<p class="sec-note">`, ktorego 31 sierpnia nie miala wcale**; §8 A i pozycja 14 listy §0
wymagaja go od dawna, a przebieg go po prostu nie napisal.

### Walidator — bo inaczej to znowu bedzie sugestia

- kazda pozycja stanu ma `socWeight` w 1-7 **i** `tier0Touch`; przy `tier0Touch:true` takze `tier0Note`;
- **kazda pozycja okna z `tier0Touch:true` ma karte w Top N albo zdanie z powodem w `sec-note` Top N**
  — nazwane z `id`, nie ogolnikiem. To jest pozycja, przez ktora ta sekcja istnieje;
- **zadna karta Top N nie ma `socWeight >= 7`, dopoki istnieje niewzieta pozycja okna z `socWeight <= 2`**;
- pierwszy wiersz Pick of the day nie ma `socWeight` wiekszego niz ostatni;
- `sec-note` Top N zawiera slowo o wazeniu i co najmniej dwie liczby.

Pozycje 14 i 23 listy §0 sprawdzaja to na gotowym pliku, a bramka §0b liczy je kodem.

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

## 5x. Zadna zakladka nie rozpycha dokumentu w poziomie

Wlasciciel zglosil 1 wrzesnia 2026, ze na telefonie **przy przelaczaniu zakladek sekcje sie
powiekszaja albo zmniejszaja**. To nie jest animacja ani wina powloki — to zmiana szerokosci
DOKUMENTU. Zmierzone przy 390x844, dziewiec zakladek po kolei:

| zakladka | `scrollWidth` | `clientWidth` |
|---|---|---|
| Overview, New, Products, Roles, Graph API, Hunting, Sources | 390 | 390 |
| **Today** | **556** | 390 |
| **Deadlines** | **482** | 390 |

Przelaczanie szlo wiec 390 -> 556 -> 390 -> 482 -> 390, a przegladarka za kazdym razem przeskalowywala
widok. Dwie przyczyny, obie znalezione przez chodzenie po drzewie i odrzucanie elementow, ktorych
rodzic ma `overflow-x:auto` (bo te legalnie przewijaja sie same, jak `.tw`):

1. **`white-space:nowrap` na chipach linkow z §5t** — w Deadlines trzy kotwice po 416, 438 i 456 px
   przy ekranie 390. **To byl regres wprowadzony ta sama specyfikacja**: `nowrap` dodano po to, zeby
   chip nie czytal sie jak dwa osobne, i na desktopie to jest sluszne. Na telefonie zawiniety chip
   jest lepszy niz rozwalona strona.
2. **Nielamliwe nazwy w kartach Top N** — `code` 482 px z nazwa uprawnienia, `span.when` 304 px
   z `nowrap`. Karta urosla do 544 px w kontenerze 366 px.

Blok idzie na koniec `<style>`, razem z §1a, §5e, §5k, §5t i §5w:

```css
@media (max-width:760px){
  .sec-body a[href^="http"],
  .sec-body .lnk-dead{white-space:normal;max-width:100%;overflow-wrap:anywhere}
  .card,.card-head,.card-title,.card p,.card li{min-width:0}
  .card .when{white-space:normal}
  .card code,.card .permname,
  .sec-body code,.sec-body .permname{overflow-wrap:anywhere;word-break:break-word}
}
```

Po poprawce wszystkie dziewiec zakladek daje `scrollWidth == clientWidth == 390`, zero bledow
konsoli w obu motywach. **Asercja Playwright: dla KAZDEJ z dziewieciu zakladek przy 390x844
`document.documentElement.scrollWidth === clientWidth`** — nie tylko dla tej, ktora akurat jest
widoczna po zaladowaniu. Poprzednia wersja §5h sprawdzala jedna zakladke i dlatego przepuscila obie.

## 5y. Agregaty: per usluga, udzial i os czasu — SKRYPT 4, dokladany

Wlasciciel wskazal 1 wrzesnia 2026 cztery braki naraz: zakladka Products ma wykres „By topic", ale
**nie ma per usluga** („entra id xyz, entra connect xyz, sentinel xyz"); **kazda zakladka** ma miec
taki raport; brakuje wykresow udzialowych i tendencji; i brakuje **podzialu na miesiac / tydzien /
dzien**, jak agreguje Merill na `daily.entra.news` i `daily.intune.admin.news`.

Powloka tego nie zrobi: `sectionSummaries()` fasetuje JEDNA rozpoznana kolumne i buduje z niej jeden
wykres, a kolumna `Product` nie odroznia Entra ID od Entra Connect. **Nie ruszamy jednak trzech
skryptow powloki** — dokladamy **czwarty**, ktory czyta gotowy DOM i blok `soc-brief-state`
i wstawia wykresy za `.panelhead`. Rysuje klasami powloki (`.chart`, `.cl`, `.ctrack`, `.cbar`,
`.cv`), wiec wyglada identycznie i dziala w obu motywach bez ani jednej nowej zmiennej koloru.

**Usluga to nie produkt.** `product` mowi „Entra"; SOC pyta osobno o Entra ID, osobno o Entra
Connect. Skrypt wylicza usluge z `product` + `area` + tytulu, wedlug zamknietego slownika, a kolejnosc
wyswietlania idzie **drabina §5p, nie liczba i nie alfabet** — uslugi tozsamosci na gorze, Azure na
dole. Zmierzone na oknie 17-31 sierpnia (109 pozycji): Entra ID 9, Entra Connect / Cloud Sync 6,
Conditional Access 2, Metody uwierzytelniania 6, Identity Governance / PIM 4, Graph API 6,
Defender XDR 5, MDE 8, MDI 2, MDCA 1, Exposure Management 4, Sentinel 3, Threat Intel 3, Purview 12,
Intune 13, Azure 7.

**Zakladki katalogowe licza katalog, nie okno.** `tab-graph` i `tab-roles` nie opisuja okna 14 dni —
liczenie ich populacja okna bylo bledem kategorii, przez ktory panel Graph API mowilby o Entrze.
Tam grupujemy po `kind` i po `firstTracked`.

**Os czasu ma trzy tryby i jeden przycisk na tryb.** Zmierzone na tym samym oknie: MIESIAC daje
`Aug 2026: 102`, TYDZIEN dwa kubelki (`tydz. 17 Aug: 47`, `tydz. 24 Aug: 55`), DZIEN dwanascie
(`17 Aug: 7`, `19 Aug: 15`, `25 Aug: 23`, ...). W zakladce Deadlines ta sama os liczy `deadline`
zamiast `published` i nazywa sie „Terminy w czasie". Kubelek tygodnia zaczyna sie w poniedzialek
w UTC, zeby dwa przebiegi tego samego dnia nie dawaly dwoch roznych tygodni.

**Pierscien udzialow** pokazuje osiem najwiekszych uslug z legenda `nazwa - N * P%`. To on odpowiada
na pytanie z punktu 1 wlasciciela liczba, a nie wrazeniem: na oknie 17-31 sierpnia **Azure ma 18%
i jest najwieksza pojedyncza usluga**, przed Intune 15% i Purview 14%, podczas gdy Entra ID ma 11%.
Dopoki tak jest, §5p nie jest zastosowane.

**CALY TEKST UI SKRYPTU JEST PO ANGIELSKU.** Zmierzone 2 wrzesnia 2026: skrypt wyszedl z polskimi
tytulami — `Per usluga`, `Udzial osmiu najwiekszych uslug`, `Opublikowane w czasie`, przyciski
`Miesiac / Tydzien / Dzien` — na stronie, ktorej cala reszta jest angielska. Wlasciciel zglosil to
pierwszym punktem. **Zadnego polskiego slowa w warstwie widocznej dla czytelnika**: komentarze w kodzie
i ta specyfikacja moga byc po polsku, `figcaption`, `chart-note`, etykiety przyciskow, nazwy uslug
i napisy w SVG — nigdy. Asercja: `document.body.innerText` nie zawiera zadnego z `Per usluga`,
`Udzial`, `Miesiac`, `Tydzien`, `Dzien`, `pozycji okna`, `Metody uwierzytelniania`.

Skrypt jest **idempotentny** (`if (panel.querySelector(".aggwrap")) return;`), wiec republikacja
popoludniowa nie dubluje wykresow, i **cichy przy braku danych** — bez bloku stanu nie robi nic
i nie rzuca bledem. Zmierzone po dolozeniu: dziewiec zakladek, zero bledow konsoli i strony w obu
motywach przy 1500x1000 i 390x844, `scrollWidth == clientWidth` wszedzie, dwa wykresy w Overview
i trzy w kazdej zakladce tresciowej.

Do `<style>` dochodzi blok wygladu (na koncu, z pozostalymi):

```css
.aggwrap{display:grid;gap:14px;margin:0 0 20px;align-items:start}
@media (min-width:900px){.aggwrap.two{grid-template-columns:minmax(0,1.35fr) minmax(0,1fr)}}
.aggwrap figure.chart{margin:0}
.aggwrap svg.donut{display:block;width:100%;max-width:250px;height:auto;margin:2px auto 0}
.aggbar{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 10px}
.aggbar .agglabel{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;margin-right:2px}
.aggbtn{font:inherit;font-size:12.5px;font-weight:600;padding:5px 12px;border-radius:999px;
  border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer}
.aggbtn[aria-pressed="true"]{background:var(--ok-soft);border-color:var(--ok);color:var(--ok)}
.aggbtn:focus-visible{outline:2px solid var(--ok);outline-offset:2px}
.donut-legend{display:flex;flex-wrap:wrap;gap:4px 14px;margin:8px 0 0;padding:0;list-style:none;font-size:12.5px}
.donut-legend li{display:flex;align-items:center;gap:6px;color:var(--muted)}
.donut-legend .sw{width:10px;height:10px;border-radius:2px;flex:0 0 auto}
.donut-legend b{color:var(--text);font-variant-numeric:tabular-nums}
```

A na koniec `<body>`, jako CZWARTY blok `<script>`, ten kod — kopiowany dalej co do bajtu tak samo
jak trzy skrypty powloki:

```js
/* ===========================================================================
   SCRIPT 4 — AGGREGATES AND RECENTLY PASSED DEADLINES (CLAUDE.md 5y, 5z).
   ADDED, never a replacement. The three shell scripts stay untouched; this one
   reads the finished DOM plus the soc-brief-state block and adds:
     1. "Per service" — Entra ID apart from Entra Connect, which `product` cannot express.
     2. A month / week / day time axis, the way daily.entra.news aggregates.
     3. A share ring, so "too much Azure" is a number instead of an impression.
     4. "Just passed" — deadlines that elapsed in the last 7 days, which every
        other view drops the moment the day count goes negative.
   Everything is drawn with the shell's own classes (.chart/.cl/.ctrack/.cbar/.cv),
   so it looks identical and works in both themes without one new colour variable.
   ALL UI TEXT IS ENGLISH — the rest of the page is English and mixing languages
   in the chart titles was reported by the owner on 2 Sep 2026.
   =========================================================================== */
(function () {
  "use strict";

  var NS = "http://www.w3.org/2000/svg";
  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x !== undefined) n.textContent = x; return n; }
  function sv(t, a) { var n = document.createElementNS(NS, t); for (var k in a) if (Object.prototype.hasOwnProperty.call(a, k)) n.setAttribute(k, a[k]); return n; }
  function state() {
    var s = document.getElementById("soc-brief-state");
    if (!s) return null;
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }

  /* ---------- services: closed vocabulary, ordered by the 5p ladder ----------
     `product` says "Entra". The owner asks separately about Entra ID and about
     Entra Connect, because they are two different surfaces for a SOC. */
  var SERVICES = [
    ["Entra Connect / Cloud Sync", /connect|cloud\s*sync|provisioning agent|hybrid/i],
    ["Conditional Access",         /conditional access/i],
    ["Authentication methods",     /authentication method|passkey|fido|mfa|tap|temporary access|sms|voice|passwordless|authenticator/i],
    ["Identity Governance / PIM",  /\bpim\b|governance|entitlement|access review|lifecycle workflow|privileged identity/i],
    ["Entra roles",                /role|rbac/i],
    ["Identity Protection",        /identity protection|risk/i],
    ["Entra ID",                   /.*/]
  ];
  var PRODUCT_SERVICE = {
    "Graph": "Graph API", "Defender XDR": "Defender XDR", "MDE": "Defender for Endpoint",
    "MDI": "Defender for Identity", "MDA": "Defender for Cloud Apps",
    "MDVM": "Exposure Management", "Exposure Management": "Exposure Management",
    "Sentinel": "Sentinel", "Intune": "Intune", "Purview": "Purview",
    "Exchange Online": "Exchange Online", "Teams": "Teams", "SharePoint": "SharePoint",
    "M365 admin": "M365 admin", "Windows": "Windows", "Windows Server": "Windows Server",
    "Azure": "Azure", "Copilot Studio": "Copilot Studio", "Threat Intel": "Threat Intel"
  };
  /* Display order follows the security ladder of 5p, not the alphabet and not the count. */
  var ORDER = ["Entra ID", "Entra Connect / Cloud Sync", "Conditional Access",
    "Authentication methods", "Identity Governance / PIM", "Entra roles", "Identity Protection",
    "Graph API", "Defender XDR", "Defender for Endpoint", "Defender for Identity",
    "Defender for Cloud Apps", "Exposure Management", "Sentinel", "Threat Intel",
    "Purview", "Intune", "M365 admin", "Exchange Online", "SharePoint", "Teams",
    "Copilot Studio", "Windows", "Windows Server", "Azure"];

  function serviceOf(it) {
    var p = it.product || "";
    if (PRODUCT_SERVICE[p]) return PRODUCT_SERVICE[p];
    if (/entra/i.test(p)) {
      var hay = [it.area, it.title, it.officialTitle, it.fingerprint].filter(Boolean).join(" ");
      for (var i = 0; i < SERVICES.length; i++) if (SERVICES[i][1].test(hay)) return SERVICES[i][0];
    }
    return p || "Other";
  }

  /* ---------- time buckets: month / week / day ---------- */
  var MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  function parse(d) { var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(d || ""); return m ? new Date(Date.UTC(+m[1], +m[2] - 1, +m[3])) : null; }
  function monday(dt) { var d = new Date(dt.getTime()), w = (d.getUTCDay() + 6) % 7; d.setUTCDate(d.getUTCDate() - w); return d; }
  function bucket(dt, mode) {
    if (mode === "month") return { k: dt.getUTCFullYear() + "-" + ("0" + (dt.getUTCMonth() + 1)).slice(-2), l: MON[dt.getUTCMonth()] + " " + dt.getUTCFullYear() };
    if (mode === "week") { var m0 = monday(dt); return { k: m0.toISOString().slice(0, 10), l: "w/c " + m0.getUTCDate() + " " + MON[m0.getUTCMonth()] }; }
    return { k: dt.toISOString().slice(0, 10), l: dt.getUTCDate() + " " + MON[dt.getUTCMonth()] };
  }
  function briefDay(st) {
    var d = parse(st && st.briefDate);
    if (d) return d;
    var n = new Date();
    return new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate()));
  }
  function daysBetween(a, b) { return Math.round((a - b) / 86400000); }

  /* ---------- horizontal bars, shell classes ---------- */
  function bars(rows, opts) {
    opts = opts || {};
    var CW = 6.15, W = 620, rowH = 26, pad = 8, valW = 44;
    var longest = rows.reduce(function (n, r) { return Math.max(n, String(r.k).length); }, 0);
    var labelW = Math.min(320, Math.max(150, Math.ceil(longest * CW) + 16));
    var maxChars = Math.floor((labelW - 14) / CW);
    var H = pad * 2 + rows.length * rowH;
    var max = Math.max.apply(null, rows.map(function (r) { return r.v; }).concat([1]));
    var s = sv("svg", { viewBox: "0 0 " + W + " " + H, width: "100%", height: H, role: "img", "aria-label": opts.title || "bar chart", preserveAspectRatio: "xMinYMin meet" });
    var plotW = W - labelW - valW - 10;
    rows.forEach(function (r, i) {
      var y = pad + i * rowH, k = String(r.k);
      var t = sv("text", { x: labelW - 10, y: y + 15, "text-anchor": "end", class: "cl" });
      t.textContent = k.length > maxChars ? k.slice(0, maxChars - 1) + "…" : k;
      var tt = sv("title"); tt.textContent = k + ": " + r.v; t.appendChild(tt); s.appendChild(t);
      s.appendChild(sv("rect", { x: labelW, y: y + 5, width: plotW, height: 13, rx: 3, class: "ctrack" }));
      var w = Math.max(3, Math.round(plotW * r.v / max));
      var bar = sv("rect", { x: labelW, y: y + 5, width: w, height: 13, rx: 3, class: "cbar" });
      var bt = sv("title"); bt.textContent = k + ": " + r.v; bar.appendChild(bt); s.appendChild(bar);
      var v = sv("text", { x: labelW + w + 7, y: y + 16, class: "cv" }); v.textContent = r.v; s.appendChild(v);
    });
    return s;
  }

  /* ---------- share ring ---------- */
  var HUES = ["--accent", "--ok", "--warn", "--bad", "--info", "--cond", "--grey", "--accent-line"];
  function donut(rows, total) {
    var R = 78, r0 = 46, C = 100, box = 200, acc = 0;
    var s = sv("svg", { viewBox: "0 0 " + box + " " + box, class: "donut", role: "img", "aria-label": "share" });
    var sum = rows.reduce(function (n, x) { return n + x.v; }, 0) || 1;
    rows.forEach(function (r, i) {
      var a0 = acc / sum * Math.PI * 2 - Math.PI / 2; acc += r.v;
      var a1 = acc / sum * Math.PI * 2 - Math.PI / 2;
      var big = (a1 - a0) > Math.PI ? 1 : 0;
      var p = ["M", C + R * Math.cos(a0), C + R * Math.sin(a0),
        "A", R, R, 0, big, 1, C + R * Math.cos(a1), C + R * Math.sin(a1),
        "L", C + r0 * Math.cos(a1), C + r0 * Math.sin(a1),
        "A", r0, r0, 0, big, 0, C + r0 * Math.cos(a0), C + r0 * Math.sin(a0), "Z"].join(" ");
      var seg = sv("path", { d: p, fill: "var(" + HUES[i % HUES.length] + ")", opacity: "0.92" });
      var t = sv("title"); t.textContent = r.k + ": " + r.v + " (" + Math.round(r.v / sum * 100) + "%)";
      seg.appendChild(t); s.appendChild(seg);
    });
    var mid = sv("text", { x: C, y: C + 2, "text-anchor": "middle", class: "cv", "font-size": "26" });
    mid.textContent = String(total === undefined ? sum : total); s.appendChild(mid);
    var sub = sv("text", { x: C, y: C + 20, "text-anchor": "middle", class: "cl", "font-size": "11" });
    sub.textContent = "items"; s.appendChild(sub);
    return s;
  }
  function legend(rows) {
    var ul = el("ul", "donut-legend");
    var sum = rows.reduce(function (n, x) { return n + x.v; }, 0) || 1;
    rows.forEach(function (r, i) {
      var li = el("li");
      var sw = el("span", "sw"); sw.style.background = "var(" + HUES[i % HUES.length] + ")";
      li.appendChild(sw);
      li.appendChild(document.createTextNode(r.k + " "));
      li.appendChild(el("b", null, r.v + " · " + Math.round(r.v / sum * 100) + "%"));
      ul.appendChild(li);
    });
    return ul;
  }

  function figure(title, note, node) {
    var f = el("figure", "chart");
    f.appendChild(el("figcaption", "chart-title", title));
    if (note) f.appendChild(el("p", "chart-note", note));
    f.appendChild(node);
    return f;
  }
  function tally(list, keyfn) {
    var m = {};
    list.forEach(function (x) { var k = keyfn(x); if (k) m[k] = (m[k] || 0) + 1; });
    return m;
  }

  /* ---------- 5z: deadlines that passed in the last 7 days ----------
     Measured 2 Sep 2026: six items had a deadline already behind them, three of
     them identity — passkeys by default and the SMS/voice retirement among
     them — and the Today tab carried the word "passkey" ZERO times. The day
     AFTER a deadline is when an estate is most exposed, and that is exactly the
     day this brief fell silent. Nothing was lost from the state; every view
     simply drops a row once its day count goes negative. */
  var ELAPSED_WINDOW = 7;
  function elapsedItems(items, today) {
    return items.filter(function (i) {
      var d = parse(i.deadline);
      if (!d) return false;
      var n = daysBetween(today, d);
      return n > 0 && n <= ELAPSED_WINDOW;
    }).sort(function (a, b) { return parse(b.deadline) - parse(a.deadline); });
  }
  function elapsedBlock(list, today) {
    var wrap = el("div", "elapsed-wrap");
    var head = el("div", "sec-head");
    head.appendChild(el("h2", null, "Just passed"));
    head.appendChild(el("p", "sec-title", "Deadlines that elapsed in the last " + ELAPSED_WINDOW + " days"));
    wrap.appendChild(head);
    var body = el("div", "sec-body");
    body.appendChild(el("p", "sec-note",
      list.length + " deadline" + (list.length === 1 ? "" : "s") + " passed in the last " + ELAPSED_WINDOW +
      " days. They are off every countdown, which is why they are repeated here: the day after a deadline is when the estate is most exposed. Confirm the change landed."));
    var tw = el("div", "tw");
    var tb = el("table");
    var thead = el("thead"), tr = el("tr");
    ["When", "Product", "What passed", "Confirm", "Source"].forEach(function (h) { tr.appendChild(el("th", null, h)); });
    thead.appendChild(tr); tb.appendChild(thead);
    var tbody = el("tbody");
    list.forEach(function (i) {
      var n = daysBetween(today, parse(i.deadline));
      var r = el("tr");
      var c0 = el("td");
      c0.appendChild(el("span", "badge b-dep", n === 1 ? "yesterday" : n + " days ago"));
      r.appendChild(c0);
      r.appendChild(el("td", null, i.product || ""));
      var c2 = el("td");
      c2.appendChild(el("b", null, i.title || i.officialTitle || i.id));
      if (i.officialTitle && i.title && i.officialTitle !== i.title) {
        c2.appendChild(document.createElement("br"));
        c2.appendChild(el("span", "muted", i.officialTitle));
      }
      r.appendChild(c2);
      r.appendChild(el("td", null, i.fingerprint || "Verify the change is in place and nothing broke."));
      var c4 = el("td");
      if (i.url) { var a = el("a", null, "Source"); a.href = i.url; a.target = "_blank"; a.rel = "noopener"; c4.appendChild(a); }
      else c4.appendChild(el("span", "muted", "no link"));
      r.appendChild(c4);
      tbody.appendChild(r);
    });
    tb.appendChild(tbody); tw.appendChild(tb); body.appendChild(tw);
    wrap.appendChild(body);
    return wrap;
  }

  /* ---------- which population belongs to which panel ---------- */
  function catalogRows(which) {
    var s = document.getElementById("soc-catalog");
    if (!s) return [];
    var c; try { c = JSON.parse(s.textContent); } catch (e) { return []; }
    return (c[which] || []).map(function (e) {
      return { product: e.kind || "unspecified", area: "", title: e.name || "",
               published: e.firstTracked || e.deployedSeen || e.sourceChanged || e.changed || null };
    });
  }

  function population(id, items) {
    var win = items.filter(function (i) { return i.tier !== "horizon"; });
    /* Catalog tabs do NOT describe the 14-day window — they describe the catalog.
       Counting them by the window was a category error: the Graph API panel
       would have talked about Entra. */
    if (id === "tab-graph") return { rows: catalogRows("graph"), date: "published", what: "catalog entries", byKind: true };
    if (id === "tab-roles") return { rows: catalogRows("roles"), date: "published", what: "catalog entries", byKind: true };
    if (id === "tab-deadlines") return { rows: items.filter(function (i) { return i.deadline; }), date: "deadline", what: "items with a deadline" };
    if (id === "tab-new") return { rows: items.filter(function (i) { return i.tier === "published-in-window"; }), date: "published", what: "items in window" };
    return { rows: win, date: "published", what: "items in window" };
  }

  function build() {
    var st = state();
    if (!st || !st.items || !st.items.length) return;
    var items = st.items, today = briefDay(st);

    document.querySelectorAll(".tabpanel").forEach(function (panel) {
      if (panel.id === "tab-overview") return;              // Overview has its own block below
      if (panel.querySelector(".aggwrap")) return;          // idempotent
      var pop = population(panel.id, items);
      if (!pop.rows.length) return;

      var wrap = el("div", "aggwrap two");

      /* --- per service --- */
      var svc = tally(pop.rows, pop.byKind ? function (x) { return x.product; } : serviceOf);
      var srows = ORDER.filter(function (k) { return svc[k]; }).map(function (k) { return { k: k, v: svc[k] }; });
      Object.keys(svc).forEach(function (k) { if (ORDER.indexOf(k) < 0) srows.push({ k: k, v: svc[k] }); });
      var top = srows.slice().sort(function (a, b) { return b.v - a.v; }).slice(0, 8);
      wrap.appendChild(figure(pop.byKind ? "Per entry type" : "Per service",
        srows.length + (pop.byKind ? " types, " : " services, ") + pop.rows.length + " " + pop.what +
        (pop.byKind ? "." : ". Order follows security weight, not count."),
        bars(srows, { title: pop.byKind ? "Per entry type" : "Per service" })));

      /* --- share --- */
      var dwrap = el("div");
      dwrap.appendChild(donut(top, pop.rows.length));
      dwrap.appendChild(legend(top));
      wrap.appendChild(figure(pop.byKind ? "Share of the eight largest types" : "Share of the eight largest services",
        "The rest is in the bars alongside.", dwrap));

      /* --- time axis, month / week / day --- */
      var dated = pop.rows.filter(function (i) { return parse(i[pop.date]); });
      if (dated.length) {
        var host = el("div");
        var barsHost = el("div");
        var ctl = el("div", "aggbar");
        ctl.appendChild(el("span", "agglabel", pop.date === "deadline" ? "Deadline by" : "Published by"));
        var modes = [["month", "Month"], ["week", "Week"], ["day", "Day"]];
        var btns = [];
        function draw(mode) {
          var m = {}, lab = {};
          dated.forEach(function (i) { var b = bucket(parse(i[pop.date]), mode); m[b.k] = (m[b.k] || 0) + 1; lab[b.k] = b.l; });
          var keys = Object.keys(m).sort();
          var rows = keys.map(function (k) { return { k: lab[k], v: m[k] }; });
          barsHost.textContent = "";
          barsHost.appendChild(bars(rows, { title: "time axis" }));
          btns.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.mode === mode)); });
        }
        modes.forEach(function (mm) {
          var b = el("button", "aggbtn", mm[1]);
          b.type = "button"; b.dataset.mode = mm[0]; b.setAttribute("aria-pressed", "false");
          b.addEventListener("click", function () { draw(mm[0]); });
          btns.push(b); ctl.appendChild(b);
        });
        host.appendChild(ctl); host.appendChild(barsHost);
        draw("month");
        var f = figure(pop.date === "deadline" ? "Deadlines over time" : (pop.byKind ? "Found over time" : "Published over time"),
          dated.length + " of " + pop.rows.length + " " + pop.what + " carry a date. Click Month / Week / Day.", host);
        f.style.gridColumn = "1 / -1";
        wrap.appendChild(f);
      }

      var head = panel.querySelector(".panelhead");
      if (head && head.nextSibling) panel.insertBefore(wrap, head.nextSibling);
      else if (head) panel.appendChild(wrap);
      else panel.insertBefore(wrap, panel.firstChild);
    });

    /* ---------- 5aa: the heading must carry a NUMBER, never a literal "N" ----------
       Measured 2 Sep 2026: the page shipped the heading "Top N of the day" verbatim.
       The shell is supposed to substitute the real card count and did not, so the
       reader was shown an algebra variable. Seven cards is the default; a run may
       publish up to TEN when the day genuinely carries more, and never more than
       ten, because an eleventh card is a list, not a ranking. */
    var CARD_MIN = 7, CARD_MAX = 10;
    document.querySelectorAll(".tabpanel").forEach(function (panel) {
      var n = panel.querySelectorAll("article.card").length;
      if (!n) return;
      panel.querySelectorAll(".sec-title, h2, h3, .chart-title").forEach(function (t) {
        if (/\bTop\s+N\b/i.test(t.textContent)) t.textContent = t.textContent.replace(/\bTop\s+N\b/i, "Top " + n);
      });
      document.querySelectorAll("nav.anchors .tab, .anchors a").forEach(function (a) {
        if (/\bTop\s+N\b/i.test(a.textContent)) a.textContent = a.textContent.replace(/\bTop\s+N\b/i, "Top " + n);
      });
      if (n > CARD_MAX && window.console) console.warn("[agg] Top N has " + n + " cards, the ceiling is " + CARD_MAX);
    });

    /* ---------- 5z: "Just passed", in Deadlines and again in Overview ---------- */
    var gone = elapsedItems(items, today);
    if (gone.length) {
      var dl = document.getElementById("tab-deadlines");
      if (dl && !dl.querySelector(".elapsed-wrap")) {
        var sec = el("section", "elapsed"); sec.id = "elapsed"; sec.setAttribute("data-nav", "Just passed");
        sec.appendChild(elapsedBlock(gone, today));
        var h = dl.querySelector(".panelhead");
        if (h && h.nextSibling) dl.insertBefore(sec, h.nextSibling); else dl.insertBefore(sec, dl.firstChild);
      }
      var ov0 = document.getElementById("tab-overview");
      if (ov0 && !ov0.querySelector(".elapsed-wrap")) {
        var s2 = el("section", "elapsed"); s2.appendChild(elapsedBlock(gone, today));
        ov0.appendChild(s2);
      }
    }

    /* ---------- Overview: the same aggregates for the whole window ---------- */
    var ov = document.getElementById("tab-overview");
    if (ov && !ov.querySelector(".aggwrap")) {
      var win = items.filter(function (i) { return i.tier !== "horizon"; });
      if (win.length) {
        var w2 = el("div", "aggwrap two");
        var svc2 = tally(win, serviceOf);
        var r2 = ORDER.filter(function (k) { return svc2[k]; }).map(function (k) { return { k: k, v: svc2[k] }; });
        Object.keys(svc2).forEach(function (k) { if (ORDER.indexOf(k) < 0) r2.push({ k: k, v: svc2[k] }); });
        w2.appendChild(figure("Per service — whole window",
          r2.length + " services, " + win.length + " items in window. SOC services on top, Azure at the bottom.",
          bars(r2, { title: "Per service" })));
        var t2 = r2.slice().sort(function (a, b) { return b.v - a.v; }).slice(0, 8);
        var d2 = el("div"); d2.appendChild(donut(t2, win.length)); d2.appendChild(legend(t2));
        w2.appendChild(figure("Share of services", "The eight largest.", d2));
        ov.appendChild(w2);
      }
    }
  }

  function boot() { try { build(); } catch (e) { if (window.console) console.error("[agg]", e); } }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { setTimeout(boot, 0); });
  else setTimeout(boot, 0);
})();
```

**To NIE rozszerza listy dozwolonych zmian w trzech skryptach powloki.** Tamte dwie pozycje —
`KIND_BADGE` (§5e) i trzy linie `facetCandidates()` (§5w) — zostaja jedynymi. Skrypt 4 jest osobnym
blokiem, ktory niczego nie nadpisuje; przebieg, ktory chcialby zamiast tego wejsc w skrypt 2, tego
nie robi i pisze o tym w odpowiedzi.

## 5z. Termin, ktory MINAL, jest najwazniejszym wierszem dnia — nie kasuj go

Wlasciciel zglosil 2 wrzesnia 2026, ze ze strony zniknely pozycje, ktorych termin wlasnie uplynal —
imiennie **passkeys jako domyslne i wycofywanie SMS oraz polaczen glosowych w MFA**. Zmierzone tego
dnia na `site/index.html`: **szesc pozycji ma termin juz za soba**, a zakladka Today zawiera slowo
`passkey` **zero razy**:

| dni | produkt | pozycja |
|---|---|---|
| **−1** | Entra | Passkeys by default; Microsoft-provided SMS and voice MFA retiring |
| **−1** | Entra | Entra Connect Sync 2.5.76.0 reaches end of support |
| **−1** | Defender XDR | Third-party network signal enrichment deprecated |
| −2 | Azure | v2.0 API and v2.1 container retire |
| −2 | Azure | Azure VPN Client for Linux retirement |
| −5 | Graph | Microsoft Graph Toolkit and Microsoft Graph CLI retire |

**Dane nie zginely.** Wszystkie szesc siedzi w stanie z `tier: "deadline-under-60-days"`, a pigulka
naglowka nawet je liczy: `43 deadlines in 60 days · 20 inside 30, 6 already elapsed`. Zgubila je
PREZENTACJA: kazdy widok sortuje i filtruje po dniach do terminu, a wiersz z liczba ujemna wypada
z kazdego okna. To ta sama choroba co `deadline: null` w §5p i `changed: null` w §5q — trzeci raz ta
sama kolumna.

**A to jest najgorszy moment na cisze.** Dzien PO terminie jest dniem, w ktorym srodowisko jest
najbardziej odsloniete: zmiana albo weszla i trzeba potwierdzic, ze nic sie nie wywrocilo, albo nie
weszla i trzeba dzialac natychmiast. Brief, ktory milczy nazajutrz po wycofaniu SMS-owego MFA, jest
gorszy niz brief, ktory o tym nie pisal wcale — bo czytelnik ma prawo sadzic, ze temat sie skonczyl.

### Regula

1. **Okno terminow to −7 do +60 dni, nie 0 do +60.** Pozycja, ktorej termin uplynal w ciagu ostatnich
   SIEDMIU dni, zostaje w stanie z `tier: "recently-elapsed"` i **nie jest usuwana ani przenoszona do
   `horizon`**. Po siodmym dniu wypada normalnie.
2. **Wlasna sekcja, po angielsku, jak cala strona**: `<section id="elapsed" data-nav="Just passed">`,
   `<h2>Just passed</h2>`, `sec-title` **„Deadlines that elapsed in the last 7 days"**. Stoi jako
   PIERWSZA sekcja panelu `tab-deadlines` i jest powtorzona w `tab-overview`, bo wlasciciel czyta
   Overview pierwszy i tam ich brakowalo.
3. **Kolumny**: `When` (`yesterday` albo `N days ago`, jako `<span class="badge b-dep">`), `Product`,
   `What passed` (nasz tytul pogrubiony, `officialTitle` wyciszony pod nim), `Confirm` (co konkretnie
   sprawdzic), `Source`. Sortowanie: najswiezszy termin na gorze.
4. **Pozycja `recently-elapsed` NIE wypada z Today ani z New.** To jest punkt 3 i 4 zgloszenia:
   wiadomosc tozsamosciowa z terminem nie moze zniknac dlatego, ze termin minal. W Today liczy sie
   jak kazda inna pozycja i podlega wazeniu §5p — `tier0Touch` i `socWeight` dzialaja bez zmian.
5. **Pigulka**: `<a class="count crit" href="#elapsed"><b>N</b> passed in the last 7 days<span>&middot; confirm they landed</span></a>`.
   Skrypt 2 robi z niej kafelek Overview sam z siebie, wiec Overview dostaje licznik bez pisania `.stat`.
6. **Skrypt 4 (§5y) buduje te sekcje takze sam, ze stanu**, i wstawia ja w `tab-deadlines`
   oraz w `tab-overview`. To siatka bezpieczenstwa: gdyby przebieg o niej zapomnial, czytelnik i tak
   ja zobaczy. Zmierzone po dolozeniu: szesc wierszy w obu panelach, `passkey` wraca na strone.

Walidator: kazda pozycja z terminem w przedziale −7..0 ma `tier:"recently-elapsed"`; sekcja
`id="elapsed"` istnieje, gdy takich pozycji jest wiecej niz zero; jej liczba wierszy rowna sie ich
liczbie; pigulka podaje te sama liczbe.

## 5aa. Naglowek niesie LICZBE, nigdy litery „N"

Zmierzone 2 wrzesnia 2026: strona wyszla z naglowkiem **`Top N of the day`** dosłownie — powloka
miala podstawic liczbe kart i tego nie zrobila, wiec czytelnik dostal zmienna z algebry. Kart bylo
siedem i kazda miala `data-id`, czyli dane byly poprawne; zawiodlo samo podstawienie.

- **Domyslnie SIEDEM kart.** Gdy dzien naprawde niesie wiecej material na karte, wolno opublikowac
  do **DZIESIECIU** — i ani jednej wiecej, bo jedenasta karta to lista, nie ranking. Mniej niz siedem
  tylko z powodem podanym w `sec-note`.
- **Naglowek zawsze pokazuje liczbe**: `Top 7 of the day`, `Top 9 of the day`. Przebieg moze wpisac
  ja wprost; niezaleznie od tego **skrypt 4 podstawia ja z liczby `article.card` w panelu** i poprawia
  takze etykiete zakladki, wiec „Top N" nie ma prawa dojsc do czytelnika.
- Przy liczbie kart powyzej dziesieciu skrypt 4 pisze ostrzezenie do konsoli — to jest sygnal, ze
  wybor przestal byc rankingiem.

Pozycje 28 i 29 listy §0 sprawdzaja to na gotowym pliku.

## 5ab. Poza 60 dniem nie zaczyna sie proza — tam tez jest tabela

Wlasciciel zapytal 2 wrzesnia 2026, dlaczego portal „nie lapie w zadnej zakladce"
`mc.merill.net/message/MC1448379` — **MemberOf rule operator retires**. Sprawdzone: zrodla je
zlapaly, pozycja JEST w stanie z poprawnym `id: "MC1448379"`, `published: 2026-08-05`,
`deadline: 2026-11-03`, i **jest na stronie szesc razy**. Odpowiedz na „nie widziales tego MC?"
brzmi wiec: widzielismy, mamy, datowane dobrze. Zawiodla wylacznie PREZENTACJA.

**Termin wypada 3 listopada — 62 dni od daty briefu.** Okno tabeli terminow ma 60. Dwa dni za
progiem pozycja przestaje byc wierszem tabeli i staje sie fragmentem zdania:

> **Beyond 1 November 2026, in one paragraph.** MemberOf rule operator retires — 2026-11-03
> (Message Center); SSPR registered-methods enforcement begins — 2026-11-07 (Message Center); …

**Proza nie jest wierszem.** Pole szukania zakladki, fasety i selektor okresu widza tabele, nie
akapit — dlatego wlasciciel wpisywal `MC1448379` w Deadlines, New i Today i nie dostawal nic.
Pozycja byla na ekranie i jednoczesnie nie do znalezienia.

**To jest CZWARTY raz ta sama choroba: twarda granica liczbowa po cichu degraduje pozycje.**
§5p — `deadline: null` nie moglo wygrac sortowania. §5q — `changed: null` wypadalo z kazdego
filtra. §5z — liczba ujemna znikala z kazdego widoku. Teraz — 61 dni zamiast 60 spycha wpis
z tabeli do zdania.

Zmierzone 2 wrzesnia: tabela Deadlines ma **43 wiersze**, a w `tier:"horizon"` z terminem siedzi
**siedem pozycji**, sklejonych w JEDEN akapit o dlugosci 638 znakow. Trzy z tych siedmiu to
tozsamosc Entry, a dwie mieszcza sie w 120 dniach:

| dni | produkt | pozycja |
|---|---|---|
| **+62** | Entra | MemberOf rule operator retires (`MC1448379`) |
| **+66** | Entra | SSPR registered-methods enforcement begins (`MC1325414-enforcement`) |
| +152 | Entra | Microsoft-provided SMS and voice MFA fully retire |

MemberOf nie jest drobiazgiem: konfiguracje z tym operatorem **przestaja sie aktualizowac po
3 listopada**, a czlonkostwa i przypisania zostaja w ostatnim znanym stanie — czyli nieaktualny
dostep do Teams i SharePointa, Conditional Access oparty na grupie dynamicznej przestaje
odzwierciedlac rzeczywistosc, licencje nie schodza, zakres jednostek administracyjnych sie zestarza.
To jest praca do zaplanowania na tygodnie, a nie notka na koncu akapitu.

### Regula

1. **Sekcja horyzontu jest TABELA, nigdy akapitem.** `<section id="horizon" data-nav="Beyond 60 days">`
   w panelu `tab-deadlines`, tuz pod tabela terminow, z tymi samymi kolumnami:
   `Service | Change | Deadline | Days | Impact | Required Action | Source`. Jeden wiersz na pozycje.
   **Bierze KAZDA pozycje `tier:"horizon"`, takze te bez terminu** (§5ac): `Deadline` = `not stated by
   Microsoft`, `Days` = `—`. Kolejnosc: `socWeight` rosnaco, w obrebie wagi termin rosnaco, niedatowane
   na koncu.
   **Kazdy wiersz terminu — w tabeli glownej, w horyzoncie i w `elapsed` — niesie `data-id` rowne
   `id` swojej pozycji stanu**, dokladnie tak jak karta Top N w §5p. Bez tego atrybutu pytanie „czy
   `MC1448379` ma wiersz" nie ma odpowiedzi w kodzie, a pytanie bez odpowiedzi w kodzie wraca jako
   sugestia; bramka §0b umie wtedy tylko dopasowac tytul, co jest przyblizeniem, nie asercja.
   **Samo to naprawia zgloszenie**, bo dopiero wiersz jest przeszukiwalny i fasetowalny.
2. **Waga promuje z powrotem do tabeli glownej.** Pozycja z terminem powyzej 60 dni, ale **do 120 dni**,
   ktora ma `socWeight <= 2` albo `tier0Touch: true`, wchodzi do GLOWNEJ tabeli terminow we wlasnym
   pasmie `61–120 days`, bez emoji pilnosci. Zmierzone: promuje to dokladnie te dwie pozycje, ktorych
   szukal wlasciciel — MemberOf i SSPR. Wycofanie SKU Azure o wadze 7 zostaje w tabeli horyzontu.
   Uzasadnienie nie jest gustowe: **wycofanie tozsamosciowe wymaga czasu na audyt i migracje**, wiec
   64 dni to nie „daleko", tylko „zacznij teraz".
3. **Nigdy nie zwijaj pozycji w zdanie.** Zdanie moze podsumowac tabele („siedem pozycji poza 60 dniem,
   najblizsza za 62 dni"), ale nie moze jej ZASTEPOWAC. Kazda pozycja stanu z terminem ma gdzies wiersz.
4. **Pigulka**: `<a class="count" href="#horizon"><b>N</b> beyond 60 days<span>&middot; nearest in NN days</span></a>`.
5. Sekcja Sources mowi jednym zdaniem, ile pozycji jest za horyzontem i ile z nich promowano waga.

Walidator (pozycje 31 i 32 listy §0, liczone przez bramke §0b): zero pozycji stanu z terminem, ktora
nie ma wiersza w zadnej tabeli; `<section id="horizon">` istnieje, gdy jakas pozycja ma termin powyzej
60 dni; **zadna pozycja do promocji nie stoi w sekcji `horizon`** — bramka czyta sekcje kazdego `<tr>`,
wiec sam fakt, ze wiersz gdzies jest, nie wystarcza; pasmo `61-120 days` wystepuje w tresci, gdy jest
co promowac; **fraza „in one paragraph" nie wystepuje na stronie**.

## 5ac. Zaden `tier` nie jest kubelkiem, ktorego strona nie renderuje

MC1448379 z §5ab bylo przykladem, nie przypadkiem. Wlasciciel powiedzial to wprost 2 wrzesnia:
*„problem tyczy sie tez innych waznych MC, artykulow, deadline'ow, ktore mozesz pomijac — ja tylko
dalem przyklad; zrodla masz zapisane, wiec nic nie powinno umknac."* Ma racje i jest to mierzalne.

Zmierzone tego dnia na `site/index.html`: stan ma **191 pozycji**, strona ma **458 wierszy tabel**,
a **36 pozycji nie ma ani wiersza, ani karty — nigdzie.** Nie jakies 36: **wszystkie 36 to
`tier:"horizon"`**, czyli caly kubelek, ktorego prezentacja nie renderuje wcale. Osiem z nich ma
termin (to sa te z §5ab), pozostale 28 terminu nie ma i dlatego nie trafialy nawet do akapitu.

| waga | ile | przyklady |
|---|---|---|
| **1 — tozsamosc** | 6 | `MC1303719` *federatedTokenValidationPolicy default blocks cross-domain federated sign-ins* (bez terminu), `MC1325414-enforcement`, `MC1448379`, `flexible-fic-immutable-github-claims`, `graph-crosstenant-m365capability`, `graph-recovery-resource-ga` |
| **2 — wykrywanie** | 13 | `MC1457836` *Tenants auto-enabled into Defender Unified RBAC*, `MC1220762` *MDE and XDR APIs retire*, `sentinel-azure-portal-retirement-2027`, `mdi-expanded-automatic-auditing` |
| 3-7 | 17 | Purview 7, Teams 3, M365 admin 3, … |

`MC1303719` jest tu najlepsza ilustracja: **waga 1, zmiana domyslnego zachowania federacji, zadnego
terminu** — i ani jednego miejsca na stronie. Nie zgubilo go zrodlo. Zgubila je tabela, ktorej nie ma.

### Regula — jedna, ogolna, nadrzedna wobec §5ab

**Kazda pozycja `soc-brief-state.items` ma na stronie co najmniej jeden wiersz `<tr data-id="<id>">`
albo karte `<article class="card" data-id="<id>">`.** Bez wyjatkow i bez wzgledu na `tier`, `deadline`
czy `socWeight`. Wiersz moze byc w tabeli terminow, w `elapsed`, w `horizon`, w New, w deep dive —
byle byl, bo dopiero wiersz jest przeszukiwalny, fasetowalny i sortowalny.

- **`tier:"horizon"` ma swoja tabele** i bierze WSZYSTKIE swoje pozycje, takze te bez terminu (§5ab
  punkt 1). Pozycja bez terminu drukuje `not stated by Microsoft`, nie puste pole.
- **Zaden wiersz nie jest juz anonimowy.** Zmierzone 2 wrzesnia: **0 z 458 wierszy** nioslo `data-id`.
  Dopoki tak jest, pytania „czy `MC1303719` jest na stronie" nie da sie zadac kodem — a §0b
  odpowiada tylko na pytania zadane kodem. Kazdy wiersz tabeli zbudowanej z pozycji stanu niesie
  `data-id`; bramka dopuszcza dopasowanie po tytule tylko jako awaryjne przyblizenie.
- **Pozycja swiadomie niepokazana nie istnieje.** Nie ma stanu „w stanie, ale nie na stronie". Gdy
  przebieg uzna, ze czegos nie warto pokazywac, USUWA to ze stanu z rekordem `Brief retracted`
  i powodem — a nie zostawia w JSON-ie, gdzie wyglada na pokryte, a czytelnik tego nie widzi.
- **Podloga zrodel z §5u dziala w druga strone**: zrodlo raportuje przeczytane / wniesione /
  odrzucone, a §5ac pilnuje, ze wszystko WNIESIONE ma wiersz. Razem zamykaja obieg: nic nie wypada
  ani miedzy zrodlem a stanem, ani miedzy stanem a strona.

Walidator (pozycja 33 listy §0, liczona przez bramke §0b): `len([i for i in items if brak wiersza
i brak karty]) == 0`. Bramka wypisuje `id` i `tier` pierwszych szesciu — po to, zeby raport nazywal
zgubione pozycje, a nie podawal liczbe. Kontrola regresji: strona z 2 wrzesnia `33 BRAK 36/191
(tier: horizon)`, ta sama strona z tabela horyzontu tylko dla datowanych `33 BRAK 30/191`, i dopiero
tabela biorąca WSZYSTKIE 36 daje `33 OK`. Stan pusty daje `BRAK „nie da sie sprawdzic"`, nie OK.

## 5ad. Kafelki „What changed" MAJA filtrowac liste — SKRYPT 5, dokladany

Wlasciciel zglosil 3 wrzesnia 2026: *„jak podajesz informacje ze cos zostalo dodane zmienione i jak
ja klikne ten panel to chcialbym aby wynik w tabelach na dole — pod polem search — byl automatycznie
filtrowany do tego wyniku. teraz kompletnie nie wiem co zostalo dodane."*

Zmierzone tego dnia na zakladce Graph API: kafelki mowia `1 Added`, `0 Removed or breaking`,
`2 Modified`, a **klikniecie kazdego z nich robi dokladnie to samo** — `jump("microsoft")`, czyli
przelacza tryb listy na *Microsoft changes* i zostawia w niej **341 wpisow**. Kubelek nie zawezajacy
listy nie odpowiada na pytanie, ktore zadaje jego wlasna liczba. Do tego tabela podsumowania ma
kolumny `When / What Microsoft did / Entry` i rozroznia kubelki **wylacznie kolorem klasy**
`cc-add` / `cc-rem` / `cc-mod` — na ciemnym motywie to nie jest informacja.

**Powloki nie ruszamy.** Trzy skrypty powloki zostaja nietkniete, skrypt 4 (§5y) tez — dokladamy
**PIATY** blok, ktory czyta gotowy DOM i blok `soc-catalog`, i robi trzy rzeczy:

1. **Kafelek staje sie filtrem.** Klikniecie `Added` zostawia na liscie pod polem szukania wylacznie
   wpisy z tego kubelka, `aria-pressed="true"` na kaflu, ponowne klikniecie czysci. Dopasowanie idzie
   po `data-id` wpisu, a gdy go brak — po znormalizowanej nazwie z `.ci-name`.
2. **Tabela podsumowania dostaje kolumne `Change`** z chipem `Added` / `Removed or breaking` /
   `Modified`, wyprowadzonym z klasy wiersza. Kolor przestaje byc jedynym nosnikiem tej informacji.
3. **Banner nad lista nazywa aktywny kubelek** i ma przycisk `Show all`: *„Added — showing 1 entry."*
   Kubelek pusty mowi to zdaniem: *„Removed or breaking — nothing in this bucket since the last brief."*

**Filtr kubelka ustepuje kazdemu innemu filtrowi.** Wpisanie czegokolwiek w pole szukania albo ruch
dowolnego `<select>` czysci go, bo dwa filtry walczace o te sama liste to najkrotsza droga do tego,
zeby czytelnik przestal ufac obu. Skrypt slucha `input` i `change` na `.cat-controls`.

**Powloka przerysowuje liste przy kazdej interakcji**, wiec skrypt trzyma `MutationObserver` na
`.cat-list` i nakłada filtr ponownie po kazdym renderze — zamiast wchodzic w skrypt 3.

### Zmierzone 3 wrzesnia 2026 na `site/index.html`

| akcja | przed | po |
|---|---|---|
| kolumny tabeli podsumowania | `When / What Microsoft did / Entry` | **`Change` / When / What Microsoft did / Entry**, pierwszy wiersz mowi `Added` |
| klik `1 Added` | 341 wpisow na liscie | **1**: `getStatisticsByPolicy method on Microsoft 365 Backup Storage (beta)`, wiersz tabeli 1, banner „Added — showing 1 entry." |
| klik `2 Modified` | 341 | **2**: `Group.Read.All → onPremisesExtensionAttributes`, `AgentIdentityBlueprint.ReadWrite.All → isDisabled` |
| klik `0 Removed or breaking` | 341 | **0** i zdanie „nothing in this bucket since the last brief." |
| ponowny klik na aktywnym kaflu | — | 341, banner znika |
| wpisanie `user` w pole szukania | — | filtr kubelka ustepuje, 42 wyniki |
| katalog rol (wszystkie kubelki 0) | — | brak tabeli podsumowania, skrypt nic nie robi i nie rzuca bledem |

Render 1500x1000, jasny i ciemny: zero bledow strony, `scrollWidth === clientWidth`.

Do `<style>` dochodzi blok (na koncu, z pozostalymi). **`[hidden]` samo nie wystarczy** — `.cat-item`
ma w powloce wlasny `display`, wiec przegrywa z atrybutem, dokladnie jak `.filterbanner` w §5c:

```css
.cat-list .cat-item[hidden],.cc-table tbody tr[hidden]{display:none!important}
.cc-tile[aria-pressed="true"]{outline:2px solid var(--accent);outline-offset:-2px;background:var(--accent-soft)}
.bkbanner{display:flex;align-items:center;gap:12px;margin:0 0 10px;padding:8px 12px;border-radius:10px;
 background:var(--accent-soft);border:1px solid var(--accent);color:var(--text);font-size:13.5px}
.bkbanner[hidden]{display:none!important}
.bk-msg{flex:1 1 auto}
.bk-clear{font:inherit;font-size:12.5px;font-weight:600;padding:4px 10px;border-radius:999px;
 border:1px solid var(--accent);background:var(--surface);color:var(--accent);cursor:pointer}
.cc-bucket{white-space:nowrap}
```

A na koniec `<body>`, jako **PIATY** blok `<script>`, ten kod — kopiowany co do bajtu:

```js
/* ===========================================================================
   SCRIPT 5 — THE CHANGE TILES FILTER THE LIST (CLAUDE.md 5ad).
   ADDED, never a replacement. The three shell scripts and SCRIPT 4 stay untouched;
   this one reads the finished DOM plus the soc-catalog block and does three things
   the owner asked for on 3 Sep 2026:
     1. "What changed at Microsoft" tiles (Added / Removed or breaking / Modified)
        become real filters: clicking one shows ONLY those entries in the list below
        the search box, so "1 Added" can be answered without hunting.
     2. The summary table gains a CHANGE column, so every row says which bucket it is
        in. Colour alone did not answer "what was added".
     3. A banner above the list names the active bucket and clears it.
   Everything is drawn with the shell's own classes, so it looks native in both themes.
   ALL UI TEXT IS ENGLISH.
   =========================================================================== */
(function () {
  "use strict";

  var BUCKETS = [
    { key: "added",    label: "Added",               cls: "cc-add", badge: "b-new" },
    { key: "removed",  label: "Removed or breaking", cls: "cc-rem", badge: "b-dep" },
    { key: "modified", label: "Modified",            cls: "cc-mod", badge: "b-upd" }
  ];

  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x !== undefined) n.textContent = x; return n; }
  function norm(s) { return (s || "").toLowerCase().trim(); }

  function catalog() {
    var s = document.getElementById("soc-catalog");
    if (!s) return null;
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }

  /* The summary table rows carry cc-add / cc-rem / cc-mod already; the reader just
     cannot see which is which. One column fixes that, and it is the same column the
     tiles filter on. */
  function labelTable(host) {
    var tb = host.querySelector(".cc-table");
    if (!tb || tb.dataset.bucketCol === "1") return;
    var hr = tb.querySelector("thead tr");
    if (hr) {
      var th = el("th", null, "Change");
      hr.insertBefore(th, hr.firstChild);
    }
    Array.prototype.forEach.call(tb.querySelectorAll("tbody tr"), function (tr) {
      var b = BUCKETS.filter(function (x) { return tr.classList.contains(x.cls); })[0];
      var td = el("td", "cc-bucket");
      var sp = el("span", "badge " + (b ? b.badge : "b-prod"), b ? b.label : "changed");
      td.appendChild(sp);
      tr.insertBefore(td, tr.firstChild);
    });
    tb.dataset.bucketCol = "1";
  }

  function wire(host, sum) {
    var tiles = host.querySelectorAll(".cc-tiles .cc-tile");
    if (tiles.length !== BUCKETS.length) return;          // shell changed shape — do nothing, quietly
    var list = host.querySelector(".cat-list");
    if (!list) return;

    var ids = BUCKETS.map(function (b) {
      return (sum[b.key] || []).map(function (r) { return r.id; }).filter(Boolean);
    });
    var names = BUCKETS.map(function (b) {
      return (sum[b.key] || []).map(function (r) { return norm(r.name); }).filter(Boolean);
    });
    var active = -1, applying = false;

    var banner = el("div", "bkbanner");
    banner.hidden = true;
    var msg = el("span", "bk-msg");
    var clear = el("button", "bk-clear", "Show all");
    clear.type = "button";
    banner.appendChild(msg); banner.appendChild(clear);
    var split = host.querySelector(".cat-split");
    if (split && split.parentNode) split.parentNode.insertBefore(banner, split);

    function apply() {
      if (applying) return;
      applying = true;
      try {
        var idSet = active < 0 ? null : ids[active];
        var nmSet = active < 0 ? null : names[active];
        var shown = 0;
        Array.prototype.forEach.call(list.querySelectorAll(".cat-item"), function (b) {
          var keep = true;
          if (idSet) {
            var nm = norm((b.querySelector(".ci-name") || {}).textContent);
            keep = idSet.indexOf(b.dataset.id) >= 0 || nmSet.indexOf(nm) >= 0;
          }
          b.hidden = !keep;
          if (keep) shown++;
        });
        Array.prototype.forEach.call(host.querySelectorAll(".cc-table tbody tr"), function (tr) {
          tr.hidden = active >= 0 && !tr.classList.contains(BUCKETS[active].cls);
        });
        tiles.forEach(function (t, i) { t.setAttribute("aria-pressed", String(i === active)); });
        if (active < 0) {
          banner.hidden = true;
        } else {
          var want = Math.max(ids[active].length, names[active].length);
          banner.hidden = false;
          if (!want) {
            /* an empty bucket is a result, not a failed filter — say which one it is */
            msg.textContent = BUCKETS[active].label + " — nothing in this bucket since the last brief.";
          } else {
            msg.textContent = BUCKETS[active].label + " — showing " + shown +
              (shown === want ? "" : " of " + want) + " " + (want === 1 ? "entry" : "entries") +
              (shown === 0 ? ". Widen the period or switch to All to see it." : ".");
          }
        }
      } finally { applying = false; }
    }

    function set(i) { active = (active === i) ? -1 : i; apply(); }

    tiles.forEach(function (t, i) {
      t.setAttribute("aria-pressed", "false");
      t.addEventListener("click", function () { setTimeout(function () { set(i); }, 0); });
    });
    clear.addEventListener("click", function () { active = -1; apply(); });

    /* Typing in the search box or moving any select is a DIFFERENT question; two filters
       fighting over the same list is how a reader stops trusting either. The bucket
       filter steps aside. */
    var controls = host.querySelector(".cat-controls") || host;
    ["input", "change"].forEach(function (ev) {
      controls.addEventListener(ev, function (e) {
        if (e.target && e.target.closest && e.target.closest(".cc-tiles")) return;
        if (active >= 0) { active = -1; apply(); }
      });
    });

    /* The shell re-renders the list on every interaction, which wipes the hiding.
       Re-apply after each render instead of touching the shell. */
    if (window.MutationObserver) {
      new MutationObserver(function () { if (active >= 0) apply(); })
        .observe(list, { childList: true });
    }
  }

  function build() {
    var cat = catalog();
    if (!cat || !cat.changeSummary) return;
    document.querySelectorAll(".catalog[data-catalog]").forEach(function (host) {
      var which = host.getAttribute("data-catalog");
      var sum = cat.changeSummary[which];
      if (!sum) return;
      labelTable(host);
      wire(host, sum);
    });
  }

  function boot() { try { build(); } catch (e) { if (window.console) console.error("[tiles]", e); } }
  /* the catalog is rendered by script 3 on DOMContentLoaded, so queue behind it */
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { setTimeout(boot, 60); });
  else setTimeout(boot, 60);
})();
```

**To NIE rozszerza listy dozwolonych zmian w trzech skryptach powloki.** `KIND_BADGE` (§5e) i trzy
linie `facetCandidates()` (§5w) zostaja jedynymi. Skrypty 4 i 5 sa osobnymi blokami, ktore niczego
nie nadpisuja.

## 6. Kontrakt w stronie

Kazda strona niesie komentarz `<!-- SHELL CONTRACT v1 ... -->` tuz po `<title>`. To pelna
specyfikacja UI, wozona razem z powloka, ktora opisuje. Kopiuj go dalej bez zmian.
**Gdy prompt i ten plik zdaja sie roznic co do markupu — wygrywa ten plik i kontrakt.**

---

## 7. ZRODLA — lista adresow i dyscyplina swiezosci

**Ta sekcja jest suma tego, co mialy oba prompty.** Zmierzone 31 sierpnia 2026: blok zrodel routine mial 26 441 B, sched 30 599 B, i **zaden nie byl nadzbiorem drugiego** — routine mial regule swiezosci (`coverageByArea`), ktorej sched nie mial wcale, a sched mial 5 875 B wiecej w sekcji Graph. Ta sama choroba co przy stronach: dwie kopie tej samej rzeczy rozjezdzaja sie w obie strony. Od teraz kanoniczna jest ta sekcja, a prompt tylko na nia wskazuje.

Official Microsoft "What's new" and release-notes pages are PRIMARY, aggregators secondary. Third-party only where Microsoft published nothing, and labelled as such.

### 1a. RANK SOURCES BY FRESHNESS, NOT BY TYPE; COVER AREAS, NOT SOURCES

A feed whose newest entry predates the window contributes nothing to that window. On 27 Aug 2026
Entra what's-new was two months stale, the run leaned on it, and the page shipped without MC1426371
"Passkeys by default; SMS and voice MFA retiring", deadline 1 Sep 2026. Rules:

1. **Record each source's newest entry date as you read it.** A source whose newest entry predates
   `window.publishedFrom` is `stale`. **A stale source can never justify a negative.** Writing
   "nothing new in Authentication Methods" on the strength of a June page is a false negative, not a
   quiet week. Only a source that is actually current can support "nothing published".
2. **Where a Learn feed is stale for an area, Message Center becomes that area's primary for this
   run** — https://mc.merill.net and its RSS https://mc.merill.net/rss.xml, alongside Merill's
   newsletter https://entra.news and the daily tracker https://daily.entra.news. Say so on the
   Sources tab, naming the area, the stale feed and its newest heading date. Six of eight passkey
   items in the 27 Aug catalog came from Message Center, not Learn.
3. **Cover areas, not sources.** For every area in a product's walk list, produce either a dated
   finding or an explicit "nothing published, checked <source> on <date>". Carry the result as
   `coverageByArea: [{"area","lastFinding","checkedOn","sources":[],"status":"covered|quiet|stale"}]`
   and render it as a table on the Sources tab. **An area with no row at all is the failure this
   rule exists to prevent** — silent omission is how a five-day deadline disappears.
4. **A known deadline is never re-discovered.** Build the 60-day tracker from the CARRIED-FORWARD
   state, re-tiering every item against today's date. Harvesting only ADDS items; it never decides
   what drops out. MC1426371 was already in the state from 13 July and needed carrying, not finding.


Official Microsoft "What's new" and release-notes pages are PRIMARY, aggregators secondary. Third-party only where Microsoft published nothing, and labelled as such.

### Microsoft Entra — HIGHEST PRIORITY

NOTE: Entra publishes ONE consolidated feed, not per-service pages. `entra/id-governance/whats-new` and `entra/global-secure-access/whats-new` do NOT exist (404). Governance, Conditional Access, Authentication, Internet/Private Access all appear on `fundamentals/whats-new` tagged by Service category. Read it by category. That page has run months behind before — if its newest month heading predates the current month, say so in the sources section and lean on Message Center and the release-history pages.

Every run:
- Consolidated feed: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
- Archive: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-archive
- What's new hub overview: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-overview
- Daily change tracker: https://daily.entra.news
- Merill's newsletter: https://entra.news
- Identity blog: https://techcommunity.microsoft.com/category/microsoft-entra-blog/blog/identity

Walk every service category: Conditional Access · Authentications · Authentication Methods · Authenticator · Identity Protection · PIM · Entitlement Management · Access Reviews · Lifecycle Workflows · Identity Governance · User Management · Device Registration · Entra Connect / Cloud Sync · Internet / Private / Network Access · B2B & External ID · Agent ID · RBAC / Roles · Monitoring & Reporting.

Agent and client release notes — security fixes, forced upgrades:
- Entra Connect: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history
- Cloud Sync agent: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/reference-version-history
- GSA Windows client: https://learn.microsoft.com/en-us/entra/global-secure-access/reference-windows-client-release-history
- GSA macOS client: https://learn.microsoft.com/en-us/entra/global-secure-access/reference-macos-client-release-history
- Private Access Sensor: https://learn.microsoft.com/en-us/entra/global-secure-access/reference-private-access-sensor-release-history
- Private network connector: https://learn.microsoft.com/en-us/entra/global-secure-access/reference-version-history

Docs-change and breaking-change feeds, secondary:
- Identity platform breaking changes: https://learn.microsoft.com/en-us/entra/identity-platform/reference-breaking-changes
- Identity platform docs: https://learn.microsoft.com/en-us/entra/identity-platform/whats-new-docs
- External ID: https://learn.microsoft.com/en-us/entra/external-id/whats-new-docs
- Verified ID: https://learn.microsoft.com/en-us/entra/verified-id/whats-new
- Agent ID: https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id

If `mcp__remote-devices__entra-news-mcp__*` tools are available (load via ToolSearch — `search_entra_news`, `list_issues`, `get_issue`), use them for Merill's newsletter. They live on the owner's desktop and are usually absent in a scheduled cloud run — then just WebFetch the sites and do not report Entra coverage as degraded.

### Microsoft Graph — permissions, endpoints, breaking changes
- Changelog: https://developer.microsoft.com/en-us/graph/changelog/ (often lags by weeks — check its newest entry date and say so)
- What's new overview: https://learn.microsoft.com/en-us/graph/whats-new-overview (the monthly sections are usually fresher than the changelog)
- Permissions reference: https://learn.microsoft.com/en-us/graph/permissions-reference
- Known issues: https://learn.microsoft.com/en-us/graph/known-issues

### Entra directory roles and Azure RBAC
- Entra RBAC what's new: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/whats-new
- Entra role permissions reference: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference
- Azure RBAC what's new: https://learn.microsoft.com/en-us/azure/role-based-access-control/whats-new
- Azure built-in roles: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
- NOTE: `azure/role-based-access-control/change-log-built-in-roles` 404s — it was folded into `whats-new`.

### Microsoft Sentinel
- https://learn.microsoft.com/en-us/azure/sentinel/whats-new
- Content Hub / solutions catalog: https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-catalog
- Blog: https://techcommunity.microsoft.com/category/microsoftsentinel/blog/microsoftsentinelblog

### Defender XDR
- https://learn.microsoft.com/en-us/defender-xdr/whats-new
- Advanced hunting schema changes: https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-changes
- Schema tables: https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables

### Defender for Endpoint / Vulnerability & Exposure Management
- https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint-releases
- https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint
- https://learn.microsoft.com/en-us/security-exposure-management/whats-new

### Defender for Identity
- https://learn.microsoft.com/en-us/defender-for-identity/whats-new

### Defender for Cloud Apps
- https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes

### Microsoft Intune
- https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
- In development: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/in-development
- Blog: https://techcommunity.microsoft.com/category/microsoft-intune/blog/microsoftintuneblog

### Microsoft Purview
- https://learn.microsoft.com/en-us/purview/whats-new

### KQL / Hunting
- https://learn.microsoft.com/en-us/kusto/query/
- Azure Data Explorer release notes: https://learn.microsoft.com/en-us/azure/data-explorer/release-notes-cloud

### General
- Microsoft Security Blog: https://www.microsoft.com/en-us/security/blog/
- Azure Updates RSS: https://www.microsoft.com/releasecommunications/api/v2/azure/rss
- M365 Message Center archive: https://mc.merill.net
- Lifecycle end-of-support: https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2026 and .../end-of-support-2027

Known limitations: TechCommunity blogs, the M365 Roadmap page and azure.microsoft.com/updates render client-side and return nothing to a server-side fetch. Use the RSS feed for Azure, mc.merill.net for Roadmap items, and cite blogs by title/date/URL backed by the corresponding Learn text.

## 8. SEKCJE RAPORTU A-N — co ma sie znalezc w kazdej

**Kanoniczna definicja tresci kazdej sekcji.** Prompt wymienia je z litery i wskazuje tutaj; nie powtarza ich tresci. Sekcje J i K sa tu celowo krotkie — niosa tylko kontrakt markupu, bo ich reguly danych mieszkaja w §5-§5w i powtarzanie ich byloby trzecia kopia do rozjechania.

Rank findings: 1) breaking changes and items needing administrator action 2) retirements and deprecations with dates 3) new detections, analytics rules and hunting capabilities 4) GA 5) preview 6) security enhancements 7) KQL and schema changes.

Build these sections in order. **Every table's last column is `Source`. Every bullet and card ends with its link.**

### A. TOP N OF THE DAY
The highest-SOC-impact items, ranked, as hero cards. **Seven by default.** Publish fewer only when the day genuinely lacks seven card-worthy items, and say so in the section note rather than padding. Heading is `Top N of the day` — the shell rewrites the number and the tab from the cards it finds. Each card: rank, product badge, status badge, deadline or publication date, What / Why / Action, source line. Prefer NEW or UPDATED items.

**Kolejnosc i wybor rzadzi §5p, nie termin.** Klucz sortowania to `(tier0Touch malejaco, socWeight rosnaco, pilnosc rosnaco)`; pozycja bez terminu dostaje pilnosc rowna dniom od publikacji, wiec **przestaje byc niesortowalna**. Kazda karta niesie `data-id` rowne `id` swojej pozycji stanu. Sekcja ma `<p class="sec-note">` mowiacy, czym wazyla, z liczbami z tego przebiegu. Kazda pozycja okna z `tier0Touch:true` ma karte albo jest **nazwana z `id` w `sec-note` jako swiadomie pominieta** — bramka §0b pozycja 23 tego pilnuje.

### B. PICK OF THE DAY, ONE PER TECHNOLOGY

A table directly below the Top-N cards, **exactly one row per technology in today's tracked item set**. The cards are ranked across everything and can crowd a product out; this table cannot, so a quiet product still shows it was checked.

Table: | Product | Pick of the day | Why it matters | Reference | Deadline | Source |

- **Product** — the spelling used elsewhere on the page.
- **Pick of the day** — title in `<b>`, area or status beneath in muted text, prefixed 🔥 for a deadline inside 30 days, ⚠️ inside 60.
- **Why it matters** — the item's `fingerprint`, so picks and state cannot drift.
- **Reference** — `<span class="mc">MC1459141</span>` / `<span class="mc">RM557190</span>` when one exists, else the literal "no MC/RM post — Learn only". Never invent an ID.
- **Deadline** — ISO deadline plus days remaining, else publication date.
- **Source** — the item's `url`, labelled Message Center / Roadmap / Learn.

**Fixed selection rule:** per product, the item with the nearest live deadline inside 60 days; if none, the most recently published. Derive the table from the state block's `items` array rather than hand-picking, so every row carries a verified link.

**Kolejnosc WIERSZY idzie §5p, nie terminem:** `socWeight` rosnaco, w obrebie wagi dni do terminu rosnaco, niedatowane na koncu. 31 sierpnia 2026 sortowanie po samym terminie postawilo „Azure VPN Client for Linux retirement" pierwszym wierszem od gory. **Zaden produkt nie wypada** — jeden wiersz na technologie zostaje bez zmian, zmienia sie tylko to, co czytelnik widzi najpierw.

### C. CHANGES SINCE LAST BRIEFING
Table: | Change type | Item | Product | What changed | Source |

**Two events get called "a change" and merging them wastes the reader's morning:** Microsoft moving, versus this report moving. These values and no others:

*Microsoft moved — the source itself changed:*
- `New at source` (badge `b-new`) — Microsoft published or first documented it inside the window.
- `Revised at source` (badge `b-upd`) — Microsoft edited a page or MC post. **Must quote the moved fragment in `<del>` and `<ins>`.** Cannot show both sides → not a source revision; pick an honest value below.
- `Deadline moved` (badge `b-upd`) — a date changed at source. Give both dates.
- `No longer listed at source` (badge `b-dep`) — Microsoft removed it from the page it was on.

*This report moved — the source never changed:*
- `Brief corrected` (`b-own`) — yesterday's brief was wrong. Say what it said and what is true.
- `Brief backfilled` (`b-own`) — in the window yesterday and missed.
- `Brief retracted` (`b-own`) — published and did not survive re-checking. Say why.
- `Tier changed` (`b-own`) — our own classification moved, e.g. horizon into the 60-day tracker.
- `Catalog bumped` (`b-own`) — an entry gained a version: "Security Operator v1 → v2 — gained `microsoft.directory/users/delete`".
- `Catalog grew` (`b-own`) — this brief inventoried an API it had not covered. **Not a Microsoft change; never `New at source`.**

Never file our own correction as `Revised at source` — that credits Microsoft with an edit it never made. On a baseline run say so instead of filling the table. Open the section with a `<p class="sec-note">` explaining the two families, so the Change type filter is self-explanatory.

### D. EXECUTIVE SUMMARY BY PRODUCT
By product, Entra first. Max 5 bullets each: what changed / why it matters / action, with its source link. Omit a product with nothing in window.

### E. NEW THIS WINDOW
Kolejnosc produktow idzie drabina §5p, nie alfabetem; podloga pokrycia §5u obowiazuje bez zmian, wiec **nic nie wypada, zmienia sie tylko kolejnosc**.
Table: | Product | Feature | Status | Published | Impact | Action Required | Source |
Status: GA, Preview, Public Preview, Private Preview, Updated, Deprecated, Retiring. Last 14 days.

### F. AUTHENTICATION WATCHLIST
Table: | Topic | Current Status | What's New in Window | Deadline | Admin Action | Source |
Cover: Passkeys · Passwordless · FIDO2 · Authentication Methods policy · TAP · Conditional Access · Authentication Strength · MFA enforcement · SMS · Voice · Security Defaults · Identity Protection.
The ONE section reporting current state regardless of window — a quiet week is not a stable authentication estate. Where nothing was published write "no new announcement in window" and still give status, deadline and action.

### G. DEADLINES INSIDE 60 DAYS
Table: | Service | Change | Deadline | Days | Impact | Required Action | Source |
Nearest first. 🔥 under 30 days, ⚠️ 30–60. Cover Sentinel, Defender, MDE, MDI, MDA, Entra, Intune, Purview, Exchange, Graph/API, Windows lifecycle and portals. **`<section id="elapsed">` comes FIRST** (§5z). **Beyond 60 days is a TABLE, never a paragraph** (§5ab): `<section id="horizon" data-nav="Beyond 60 days">` with the same columns, one row per item — prose is not a row and cannot be searched or filtered. An item past 60 days but inside 120 with `socWeight <= 2` or `tier0Touch:true` is promoted back into the MAIN table in a `61–120 days` band.

### H. PER-PRODUCT DEEP DIVE
One table per product with in-window material — Entra, Sentinel, Defender XDR, MDE, MDI, Intune, Purview. Columns vary, last is always `Source`:
- Entra — | Area | Change | Security Impact | Action | Source |
- Sentinel — | Area | Change | SOC Impact | Action | Source |
- Defender XDR — | Capability | Change | SOC Impact | Action | Source |
- MDE — | Feature | Release Type | Security Impact | Recommended Action | Source |
- MDI — | Feature | Change | Impact | Action | Source |
- Intune — | Area | Feature | Security Impact | Action | Source | (security only; ignore productivity features)
- Purview — | Area | Change | Impact | Action | Source |
Omit a product's table when it has nothing in window, saying so in one line rather than filling it with old material.

### I. KQL AND THREAT HUNTING
For every query-surface change in window: Change / Operational Benefit / Example Query / SOC Use Case / source link. If none, give 3 practical hunting queries tied to this brief plus 3 detection-engineering ideas. Every query in a `<pre><code>` block with real, verified table and column names — check against Microsoft Learn or the KQL Search MCP and cite the schema page. Never invent one; label anything unverified.

### J. GRAPH API PERMISSIONS AND ENDPOINTS — a catalog, not a table

This section is NOT hand-authored HTML. Its markup is exactly:

```html
<section id="graph" data-nav="Graph API">
<div class="sec-head"><h2>Section &lt;letter&gt;</h2><p class="sec-title">Graph API permissions and endpoints</p></div>
<div class="sec-body">
<p class="sec-note">One or two sentences framing what the catalog is.</p>
<div class="catalog" data-catalog="graph"></div>
</div>
</section>
```

The shell renders the whole browser from the `graph` array — search row, the what-changed summary, the three-mode switch, every filter, the period selector and the detail pane. **Your job is only the data, and the data rules are NOT repeated here: they are §5 (service state beats documentation), §5a (`sourceChanged`), §5b (parsing the reference), §5d (four sets D/A/B/C and the `D\A` rule), §5e (undocumented at Microsoft), §5f (other API surfaces), §5g (versioning), §5j (descriptions), §5q (found today vs earlier) and §5r (link status).** Read them there and apply them in full; §0 lists them as checklist items and §0b gates the ones a script can verify.

**ASSERTED NEGATIVES LIVE IN `negatives.graph` AND `negatives.roles`, EACH WITH ITS CHECK DATE.**
One paragraph per catalog, carried forward and updated only for what you actually re-read:
*"no changes to `RoleManagement.*` in the window, checked against the permissions reference on <date>"*.
**Never assert a permission negative from the Graph changelog** — it does not track permission names
at all (2,620 entries since 2019, zero mentions of `UserAuthenticationMethod` or `UserAuthMethod`,
while the reference carries 54 in that family). Check the prefix in set A first; otherwise write
"not re-checked this run". An unchecked assertion is worse than silence, and a still-valid one is
carried forward with its original date rather than re-dated to today.

### K. ENTRA DIRECTORY ROLES AND AZURE RBAC — a catalog, not a table

Same shape:

```html
<section id="roles" data-nav="Roles">
<div class="sec-head"><h2>Section &lt;letter&gt;</h2><p class="sec-title">Entra directory roles and Azure RBAC</p></div>
<div class="sec-body">
<p class="sec-note">One or two sentences framing what the catalog is.</p>
<div class="catalog" data-catalog="roles"></div>
</div>
</section>
```

Fed by the `roles` array, under exactly the same rules as the Graph catalog — §5e for undocumented roles, §5g for versioning, §5i for the action tables and their provenance, §5q for `firstTracked`. `added`/`removed` are exact action strings, rendered green `+` and red `-`; `privilegedBefore` renders `<del>No</del> -> <ins>Yes</ins>` when Microsoft flips privileged status. A role visible on the reference page but absent from every what's-new log gets `changed: null` and a `dateNote`, never an inferred date.

### L. SOC ACTIONS
Table: | Priority | Action | Product | Business Value | Source | — Critical / High / Medium / Low. Max 10 rows, actionable only.

### M. STRATEGIC WATCHLIST
Max 8 bullets on initiatives to track over 3–12 months, each with a link. No action this week; all require a plan.

### N. SOURCES AND VALIDATION
Not a link dump — every claim is linked in place. Cover: sources unreachable or stale this run, conflicting dates Microsoft publishes, whether a thin window was the filter or a quiet week, and that nothing is verified against the owner's tenant beyond the reads named above.

Accuracy rules: never invent an MC ID, roadmap ID, date, deadline, version number, permission string, role action or KQL table. If a detail is not published, write "not stated by Microsoft". Label anything inferred as "(inferred)". Where Microsoft publishes contradictory dates, give both and say which to plan against.

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
