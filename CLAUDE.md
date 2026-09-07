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
   gotowym pliku HTML — to nie jest ocena, tylko test. **Pozycje, ktorych bramka nie umie sprawdzic
   z pliku, bo powstaja dopiero w przegladarce (49, 51, 52), sprawdza Playwright z §5h** — i to
   rozroznienie jest tu istotne, bo 7 wrzesnia 2026 bramka dala 45/46 na stronie, ktorej panel
   uprawnienia byl pusty.
4. **W odpowiedzi wypisz liste jako `OK` / `BRAK <powod>`.** Lista ma 52 pozycje dla przebiegu,
   ktory buduje albo odbija strone glowna (0-33, 35-52), plus **pozycje 34 dla przebiegu ZMIAN** — razem 53.
   (Poprzednie wydania mowily „47 … razem 48"; 0-33 to 34 pozycje, a nie 33, wiec liczba byla o jedna za mala.
   Liczbe w kazdej asercji sprawdza sie tak samo jak kazda inna — §0a: **kazda liczba zapisana w asercji ma date waznosci**.) Wlasciciel czyta ta liste zamiast
   szukac braków na stronie.

## Lista

| # | co | sekcja | sprawdzenie na gotowym HTML |
|---|---|---|---|
| 0 | **routine odbija artefakt, nie buduje strony sam** | 0a | `verify()` w `mirror_artifact.py` konczy sie bez bledu; fallback opisany w odpowiedzi |
| 1 | siedem pigulek na stronie porannej, **osiem po passie popoludniowym** (ta dodatkowa to `since the morning pass`, §4d taska popoludniowego); pierwsze trzy zawsze: terminy, `undocumented at Microsoft`, `deployed, not in this tenant` | 1, 5e | pierwsze trzy `.counts a.count` w tej kolejnosci; licznik 7 albo 8, nigdy mniej |
| 2 | blok mobilny jako OSTATNI w `<style>` | 1a | `@media (max-width:760px)` wystepuje po ostatnim `.cat-controls{position:sticky` |
| 3 | **dziesiec** paneli `.tabpanel`, identyfikatory sekcji z §2 (od 6 wrzesnia 2026 dochodzi `tab-components`, §5ag) | 2, 5ag | licznik po usunieciu komentarza SHELL CONTRACT = 10 |
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
| 26 | zadna z DZIESIECIU zakladek nie rozpycha dokumentu przy 390x844; kazdy `.navrow` przewija sie sam, dokument NIE | 5x, 5ae | dla kazdej zakladki `scrollWidth === clientWidth` na `documentElement` |
| 27 | skrypty 4 I 5 obecne; kazda zakladka tresciowa ma wykres per usluga, pierscien udzialu i os czasu Month / Week / Day; kafelki `What changed` filtruja liste katalogu | 5y, 5ad | `.aggwrap figure.chart` >= 3 w kazdym panelu procz Overview; `.aggbtn` = 3; tabela `cc-table` ma kolumne `Change` |
| 28 | **kazdy termin z ostatnich 7 dni zostaje**: `tier:"recently-elapsed"`, sekcja `id="elapsed"` w `tab-deadlines` I w `tab-overview`, pigulka `passed in the last 7 days`; pozycja nie wypada z Today ani z New | 5z | liczba pozycji z terminem w −7..0 = liczba wierszy `.elapsed-wrap tbody tr` w obu panelach |
| 29 | naglowek Top N niesie LICZBE; 7 domyslnie, najwyzej 10 | 5aa | `document.body.innerText` nie zawiera `Top N`; `article.card` w `tab-today` miesci sie w 7..10 |
| 30 | **zero polskich slow w warstwie widocznej dla czytelnika** — cala strona jest po angielsku | 5y | `innerText` nie zawiera `Per usluga`, `Udzial`, `Miesiac`, `Tydzien`, `Dzien`, `pozycji okna`, `Metody uwierzytelniania` |
| 31 | **kazda pozycja stanu z terminem ma WIERSZ w jakiejs tabeli** — poza 60 dniem jest `<section id="horizon">` z tabela, nigdy akapit; fraza „in one paragraph" nie wystepuje; kazdy wiersz terminu niesie `data-id` | 5ab | dla kazdej pozycji z `deadline` istnieje `<tr>` o tym `data-id` (albo z jej tytulem w tresci); `horizon` w `ids`; brak frazy „in one paragraph" |
| 32 | pozycja 61-120 dni z `socWeight<=2` albo `tier0Touch` promowana do GLOWNEJ tabeli, pasmo `61-120 days` | 5ab | zero takich pozycji poza glowna tabela |
| 33 | **KAZDA pozycja stanu ma wiersz albo karte — nie tylko datowana.** Zaden `tier` nie jest kubelkiem, ktorego strona nie renderuje | 5ac | zero pozycji `items` bez `<tr data-id>` albo `article.card[data-id]` |
| 35 | **pasek ma wlasny, grafitowy kolor na `.navstack`, ten sam w obu motywach, DWA opisane rzedy (`Daily`, `Reference`) i ramke na kazdej zakladce** | 5ae | `--nav-bg` i `--nav-tab-line` zadeklarowane; `.navstack` niesie `background`; `nav.anchors .tab` niesie `border`; render: tlo `.navstack` identyczne w obu motywach i rozne od `--surface`; dwa `.navrow`, razem 10 zakladek |
| 36 | **kazdy `<li>` ma JEDEN temat i konczy sie linkiem** — ksztalt punktu z zakladki Products obowiazuje na calej stronie | 5af | zaden `<li>` nie ma naraz >=2 `<b>` i >=3 srednikow, liczone `html.parser`; punkty `sec-note` sekcji `top5` otwieraja sie `<b>` i niosa link (to drugie okiem, §5af) |
| 37 | **zakladka Component versions**: kazdy komponent ma `versions[]` z platforma ze slownika, `provenance`, `state`, `checkedOn` i zrodlo; kazda wersja ma wlasny `.vbox` z chipem platformy | 5ag | licznik `.vbox` = licznik wpisow `versions[]`; zero platform spoza slownika |
| 38 | **nic nie zostalo wyciete**: liczba `li.relitem` na stronie rowna sie liczbie punktow `releases[].groups[].items[]` w bloku stanu | 5ag | roznica zerowa; zaden `details.rest` nie ma podpisu `N of N` |
| 39 | **reguła wyboru jest opublikowana i stosowana**: `div.rulebox` na stronie, kazdy wypromowany punkt niesie etykiete `.rcat`, odsetek wypromowanych w 30-70% | 5ag | `.rulebox` obecny; `li.promoted` bez `.rcat` = 0; `promoted/total` w pasmie |
| 40 | **kafelki nawigacji**: kazdy `a.jtile` wskazuje istniejacy `article.cmp[id]`, kafelkow tyle co komponentow, panel `What this page tracks` podaje liczby zgodne ze stanem | 5ag | zero kotwic bez sekcji; `a.jtile` = liczba `components`; liczba w panelu = policzona ze stanu |
| 34 | **tylko przebieg ZMIAN**: strona zmian jest LICZONA przez `make_diff.py`, nie odbijana — bez zakladek, bez katalogu, bez blokow JSON, ponizej 900 kB; **sekcja `bytab` z SZESCIOMA wierszami i jedna tabela na zakladke w Added / Removed / Changed**, plus sekcje `components` (§5ag) i `endpoints` (§5ah), oraz rejestr dopisany przez `--ledger` (§5aj) | 3, 3a | `verify()` w `make_diff.py` konczy sie bez bledu; rozmiar pliku w dziesiatkach kB, nie w megabajtach |
| 41 | **`graphMap` w bloku `soc-brief-state`**: `commit`, `readOn`, slownik sciezek `p`, tablica metod `m`; blokow JSON na stronie nadal DWA | 5ah | `graphMap` obecne z czterema polami; `<script type="application/json">` = 2 |
| 42 | **nic nie obciete z mapy endpointow**: suma par po dekodowaniu `eps` rowna sie liczbie par metoda-sciezka w pliku Microsoftu | 5ah | roznica zerowa (zmierzone 24 099 przy klonie `ec959bb`) |
| 43 | `privilegeLevel` i `requiresAdminConsent` na kazdym schemacie, ktory ma je w pliku; chip zgody CZERWONY przy `required`, ZIELONY przy `not required` | 5ah | zero schematow bez `l`/`c`; oba kolory obecne i rozne |
| 44 | **derywacja rola-uprawnienie ma opublikowana regule i kolumne glebokosci**: `div.rulebox` w zakladce Graph API, `Depth` w kazdym wierszu, mianownik rowny liczbie endpointow z naglowka panelu | 5ah | zaden wiersz nie ma pokrycia >100%; mapa bez `roles` daje `BRAK „nie da sie sprawdzic"`, nie OK |
| 45 | **rejestr zmian dopisany**: `site/data/changelog.json` ma wpis w `runs` na DZISIEJSZY przebieg, takze przy zerze zmian; zaden wpis nie starszy niz `retentionDays` | 5aj | `runs[-1].date` = data przebiegu; `min(seen)` w oknie |
| 46 | **kazda zakladka tresciowa ma `details.chg14`**, licznik w podpisie rowny liczbie wierszy w srodku; zakladka bez zmian ma zdanie z liczba przebiegow, nie pusty element | 5aj | licznik = wiersze dla kazdej zakladki |
| 47 | **rejestr NIE zostal przepisany**: wpisy starsze niz dzisiaj sa identyczne z poprzednim przebiegiem | 5aj | roznica pusta; pierwszy przebieg daje `BRAK „brak punktu odniesienia"`, nie OK |
| 48 | **SKRYPT 6 buduje KAZDY panel uprawnienia w ukladzie v13**: `.v13pane` z `At a glance`, kartami schematow, zwinieta lista endpointow i tabela rol, plus `Exact match` przy szukajce katalogu; `Worked example` ukryty | 5ak | `v13pane`, `epsinject`, `s6exact` i `SCRIPT 6` w pliku; render: trzy rozne uprawnienia daja trzy ROZNE liczby endpointow |
| 49 | **SKRYPT 7 buduje panel roli w tym samym ukladzie**, a pierwsze dwie sekcje OBU paneli to `At a glance` i `What changed … in the last 14 days` | 5al | `SCRIPT 7`, `v13role`, `actinject`, `__socOpenRole` w pliku; render: panel roli ma te dwie sekcje w tej kolejnosci |
| 50 | **`ledger14` w bloku stanu**: `runs` i `entries`, blokow JSON nadal DWA, zaden wpis bez `tab`, zaden z encja HTML ani ze zdaniem w polu `id` | 5al, 5aj | `ledger14` obecne; `<script type="application/json">` = 2; zero wpisow z `&…;` i z `→` w `id` |
| 51 | **kazda zakladka tresciowa ma `details.chg14` z SKRYPTU 8**: obie osie wykresu podpisane, licznik rowny liczbie wierszy, kazdy wiersz z przedmiotem ma `+` albo `↗` | 5al | `SCRIPT 8`, `chg14`, `axt`, `howto` w pliku; render: licznik = wiersze, oba podpisy osi obecne |
| 52 | **`+` w wierszu historii otwiera panel katalogu**, a klon nie ma wlasnej sekcji 14 dni | 5al | `__socOpenPerm` i `__socOpenRole` w pliku; render: trzy rozne wiersze daja trzy ROZNE panele, `[data-hist]` w klonie = 0 |

**Pozycja, ktorej nie da sie wykonac, bo zrodlo bylo niedostepne, jest `BRAK` z nazwa zrodla —
nigdy nie jest pomijana w ciszy.** Pozycje 15, 16, 19, 20, 23, 26, 28, 31, 33, 42, 45, 47, 48, 49, 51 i 52 sa wiazace: przebieg, ktory je pominie
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
- **artefakt `Microsoft SOC Brief <data>`** (dziewiec albo dziesiec paneli) — wyjmuje z niego sekcje `#pmdelta`
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

**Bramka lustra sama byla o krok od wywalenia przebiegu 7 wrzesnia 2026.** `verify()` mial zaszyte
`tabpanels != 9` i `navanchors != 1` — liczby prawdziwe w dniu, w ktorym je napisano. Po §5ag paneli
jest dziesiec, a po §5ae wariancie B pasek ma DWA `nav.anchors`, po jednym na rzad. Lustro odrzucilo
by wiec poprawny artefakt, routine uciekl by w fallback i **zbudowal strone po swojemu** — czyli
dokladnie ta rozbieznosc, przed ktora ta sekcja istnieje. Zmierzone na szesciu wejsciach po
poprawce: 10 paneli / 2 rzedy `OK`; 9 paneli / 1 rzad `OK` z ostrzezeniem; 9 paneli / 2 rzedy `OK`
z ostrzezeniem; 12 paneli, 2 panele i 3 rzedy — `ODRZUCONE` z liczba. Prog jest przedzialem,
bo zadaniem lustra jest wierna kopia, a ten test lapie ZEPSUTA EKSTRAKCJE, nie brakujaca zakladke.
**Kazda liczba zapisana w asercji ma date waznosci** — dopisujac panel, zakladke albo skrypt
przeszukaj plik za twardymi licznikami, zanim opublikujesz.

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
    # 6 wrzesnia 2026: paneli jest DZIESIEC (§5ag dokłada `tab-components`), a pasek ma DWA
    # `nav.anchors`, po jednym na rzad (§5ae wariant B). Zaszyte `!= 9` i `!= 1` odrzucilyby
    # jutrzejszy artefakt i zepchnelyby routine w fallback, czyli w budowanie strony po swojemu —
    # a to jest ta sama rozbieznosc, przed ktora §0a istnieje.
    # Prog jest przedzialem, nie liczba, i to jest swiadome: zadaniem lustra jest WIERNA kopia,
    # a ten test lapie ZEPSUTA EKSTRAKCJE (0, 2, 12 paneli), nie brakujaca zakladke. Artefakt
    # o dziewieciu panelach przechodzi, ale przebieg MUSI to zglosic w odpowiedzi.
    if p.tabpanels not in (9, 10):
        errs.append("tabpanel = %d, ma byc 10 (9 dopuszczalne przejsciowo)" % p.tabpanels)
    elif p.tabpanels == 9:
        print("UWAGA: artefakt ma 9 paneli — brakuje zakladki Component versions (§5ag). "
              "Lustro publikuje, ale napisz o tym w odpowiedzi jako pozycja 3 BRAK.")
    if p.navanchors not in (1, 2):
        errs.append("nav.anchors = %d, ma byc 2 (jeden na rzad, §5ae) albo 1 przed przejsciem"
                    % p.navanchors)
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
    # `build_diff` bierze masthead Z BRIEFU, a ten od §5ae wariantu B wozi `.navstack`
    # z DWOMA `nav.anchors`, po jednym na rzad. Zaszyte `!= 1` odrzucaloby wiec poprawna
    # strone awaryjna. Ten sam blad, ta sama rodzina, znaleziony przy przeszukiwaniu pliku
    # za twardymi licznikami — i to jest dowod, ze ta regula z §0a byla potrzebna.
    if p.navanchors not in (1, 2):
        errs.append("nav.anchors = %d, ma byc 2 (jeden na rzad, §5ae) albo 1 przed przejsciem"
                    % p.navanchors)
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

**Asercje w `verify()` sa bramka publikacji**: dziesiec `.tabpanel` po usunieciu komentarza
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
        # §5af: kazdy <li> jako (tekst, liczba <b>, liczba <a>) — kryterium to liczba TEMATOW
        self.listitems=[]; self._li=None; self._lib=0; self._lia=0
        # §5ag: zakladka Component versions
        self.vboxes=0; self.vboxPchips=0; self._invbox=False
        self.pchips=[]; self.relitems=0; self.promoted=0; self.rcats=0
        self._inpromoted=False; self.rulebox=0; self.navstack=0; self.navrows=0
        self.restsummaries=[]; self._insummary=False; self._sumbuf=[]
        # §5ag nawigacja: kotwice kafelkow, id sekcji, liczby panelu
        self.jtiles=[]; self.cmpids=set(); self.rbnums=[]
        self._innum=False; self._numbuf=[]
        # §5ah / §5aj: bloki JSON musza zostac DWA, a pasek 14 dni ma miec prawdziwy licznik
        self.jsonblocks=0; self._intb=False
        self.chg14=[]; self._in14=0; self._c14=None; self._r14=0; self._insum14=False; self._sum14=[]; self._badge14=False
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
        if tag=="li": self._li=[]; self._lib=0; self._lia=0
        elif self._li is not None and tag=="b": self._lib+=1
        elif self._li is not None and tag=="a": self._lia+=1
        # --- §5ag ---
        if tag=="div" and "vbox" in cls: self.vboxes+=1; self._invbox=True
        if tag=="div" and "rulebox" in cls: self.rulebox+=1
        if tag=="div" and "navstack" in cls: self.navstack+=1
        if tag=="div" and "navrow" in cls: self.navrows+=1
        if tag=="span" and "pchip" in cls:
            self.pchips.append(" ".join(c for c in cls if c.startswith("p-")))
            if self._invbox: self.vboxPchips+=1
        if tag=="span" and "rcat" in cls:
            self.rcats+=1
            if self._inpromoted: pass
        if tag=="li" and "relitem" in cls:
            self.relitems+=1
            if "promoted" in cls: self.promoted+=1; self._inpromoted=True
        if tag=="summary": self._insummary=True; self._sumbuf=[]
        if tag=="a" and "jtile" in cls: self.jtiles.append(a.get("href") or "")
        if tag=="article" and "cmp" in cls and a.get("id"): self.cmpids.add(a["id"])
        if tag=="span" and "rb-num" in cls: self._innum=True; self._numbuf=[]
        if tag=="script" and (a.get("type") or "").strip()=="application/json": self.jsonblocks+=1
        if tag=="details" and "chg14" in cls:
            self._in14+=1; self._c14=None; self._r14=0
        elif self._in14 and tag=="details": self._in14+=1
        if self._in14 and tag=="summary" and self._c14 is None: self._insum14=True
        if self._insum14 and tag=="span" and "badge" in cls: self._badge14=True; self._sum14=[]
        if self._in14 and tag=="tr" and self._intb: self._r14+=1
        if tag=="tbody": self._intb=True
        if tag=="p" and "sec-note" in cls: self._grab=self.sec
        if tag in ("script","style"): self._skip+=1
    def handle_data(self, d):
        if getattr(self,"_badge14",False): self._sum14.append(d)
        if self._insummary: self._sumbuf.append(d)
        if self._innum: self._numbuf.append(d)
        if self._grab: self.notes[self._grab]=self.notes.get(self._grab,"")+d
        if not self._skip: self.text.append(d)
        if self._row is not None and not self._skip: self._row.append(d)
        if self._li is not None and not self._skip: self._li.append(d)
    def handle_endtag(self, tag):
        if tag=="p": self._grab=None
        if tag=="tr" and self._row is not None:
            self.rows.append((self._rowsec, self._rowid, " ".join("".join(self._row).split())))
            self._row=None; self._rowid=None; self._rowsec=None
        if tag=="li" and self._li is not None:
            self.listitems.append((" ".join("".join(self._li).split()), self._lib, self._lia))
            self._li=None
        if tag=="li": self._inpromoted=False
        if tag=="div" and self._invbox: self._invbox=False
        if tag=="summary" and self._insummary:
            self.restsummaries.append(" ".join("".join(self._sumbuf).split())); self._insummary=False
        if tag=="span" and self._innum:
            self.rbnums.append("".join(self._numbuf).strip()); self._innum=False
        if tag=="tbody": self._intb=False
        if tag=="span" and getattr(self,"_badge14",False):
            m=re.search(r"\d+", "".join(self._sum14))
            if m and self._c14 is None: self._c14=int(m.group(0))
            self._badge14=False
        if tag=="summary" and self._insum14:
            if self._c14 is None: self._c14=-1
            self._insum14=False
        if tag=="details" and self._in14:
            self._in14-=1
            if self._in14==0:
                self.chg14.append((self._c14 if self._c14 is not None else -1, self._r14))
        if tag=="section" and self._secstack:
            self._secstack.pop()
            self.sec=self._secstack[-1] if self._secstack else None
        if tag in ("script","style") and self._skip: self._skip-=1

def gate(path, site=None):
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
    need("27", "skrypty 4 (agregaty §5y) i 5 (filtr kafelkow §5ad) obecne",
         ("SKRYPT 4" in h or "SCRIPT 4" in h) and "aggwrap" in h and "aggbtn" in h
         and "SCRIPT 5" in h and "bkbanner" in h and "cc-tile" in h,
         "brak: %s" % ", ".join(
             [n for n,ok in (("skrypt 4", ("SKRYPT 4" in h or "SCRIPT 4" in h)),
                             ("klasy agregatow", "aggwrap" in h and "aggbtn" in h),
                             ("skrypt 5", "SCRIPT 5" in h),
                             ("banner kubelka", "bkbanner" in h),
                             ("kafelki cc-tile", "cc-tile" in h)) if not ok]))
    # 35: §5ae — pasek zakladek ma wlasny kolor i ramke. Bramka czyta plik, wiec sprawdza
    # OBECNOSC zmiennych i reguly; wartosci wyliczone i rownosc obu motywow sprawdza Playwright.
    flat=h.replace("\n","").replace("\r","")
    need("35","pasek zakladek ma wlasny kolor i ramke na zakladce (§5ae)",
         "--nav-bg" in h and "--nav-tab-line" in h
         and re.search(r"nav\.anchors\s*\{[^}]*background", flat) is not None
         and re.search(r"nav\.anchors\s+\.tab\s*\{[^}]*border", flat) is not None,
         "zmienne=%s, tlo paska=%s, ramka zakladki=%s" % (
             "--nav-bg" in h and "--nav-tab-line" in h,
             re.search(r"nav\.anchors\s*\{[^}]*background", flat) is not None,
             re.search(r"nav\.anchors\s+\.tab\s*\{[^}]*border", flat) is not None))
    # 36: §5af — punkt listy ma JEDEN temat. Liczymy PARSEREM: komentarz SHELL CONTRACT ma
    # wczesny "-->", wiec niezachlanne wycinanie komentarzy zjada kawal dokumentu i daje 0 punktow
    # tam, gdzie jest 98. Kryterium to liczba TEMATOW, nie slow: punkt o 123 slowach opisujacy jedna
    # rzecz jest poprawny, punkt o 113 slowach opisujacy dziewiec — nie.
    packed=[t for t,nb,na in s.listitems if nb>=2 and t.count(";")>=3]
    need("36","kazdy punkt listy ma jeden temat (§5af)",
         bool(s.listitems) and not packed,
         "brak punktow listy — nie da sie sprawdzic" if not s.listitems
         else "%d z %d punktow upycha kilka tematow w jeden: %s" % (
             len(packed), len(s.listitems), " | ".join(x[:60] for x in packed[:2])))
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
    # 37-39: §5ag zakladka Component versions. Bramka czyta plik, wiec liczy elementy i porownuje
    # je ze stanem; wartosci wyliczone (kolory chipow) sprawdza Playwright.
    comps=(st["soc-brief-state"] or {}).get("components") or []
    PLATS={"windows","windows-server","macos","ios","ipados","android","cross","apple"}
    if comps:
        nver=sum(len(c.get("versions") or []) for c in comps)
        badplat=[v.get("platform") for c in comps for v in (c.get("versions") or [])
                 if v.get("platform") not in PLATS]
        nofield=[c.get("id") for c in comps
                 if not (c.get("versions") and c.get("provenance") and c.get("state")
                         and c.get("checkedOn") and c.get("sources"))]
        need("37","kazdy komponent kompletny, kazda wersja ma wlasny .vbox z chipem",
             not badplat and not nofield and s.vboxes==nver and s.vboxPchips>=s.vboxes,
             "platformy spoza slownika %s; niekompletne %s; vbox=%d przy %d wersjach, chipow w vbox=%d"
             % (badplat[:3], nofield[:3], s.vboxes, nver, s.vboxPchips))
        nitems=sum(len(g.get("items") or []) for c in comps
                   for r in (c.get("releases") or []) for g in (r.get("groups") or []))
        degen=[x for x in s.restsummaries
               if re.search(r"remaining\s+(\d+)\s+of\s+\1\b", x)]
        need("38","nic nie wyciete: li.relitem = liczba punktow w stanie",
             s.relitems==nitems and not degen,
             "wyrenderowane %d, w stanie %d; podpisy 'N of N': %s" % (s.relitems, nitems, degen[:2]))
        band = (100.0*s.promoted/s.relitems) if s.relitems else 0
        need("39","regula wyboru opublikowana i stosowana",
             s.rulebox>=1 and s.rcats>=s.promoted and 30 <= band <= 70,
             "rulebox=%d, etykiet %d przy %d wypromowanych, odsetek %.0f%% (ma byc 30-70)"
             % (s.rulebox, s.rcats, s.promoted, band))
        # 40: kafelek prowadzacy donikad jest gorszy niz brak kafelka — obiecuje i nie dowozi.
        dead=[h for h in s.jtiles if not (h.startswith("#") and h[1:] in s.cmpids)]
        nums=[int(x) for x in s.rbnums if x.isdigit()]
        # POZYCYJNIE, nie `w in nums`: pierwsza wersja pytala, czy liczba gdziekolwiek wystepuje,
        # i przechodzila na stronie z blednym licznikiem komponentow, bo ta sama cyfra stala
        # w wierszu obok. Asercja, ktora przechodzi z niewlasciwego powodu, jest gorsza niz jej brak.
        want=[len(comps), sum(len(c.get("versions") or []) for c in comps)]
        need("40","kafelki nawigacji celuja w istniejace sekcje, liczby panelu zgodne ze stanem",
             bool(s.jtiles) and not dead and len(s.jtiles)==len(comps)
             and nums[:len(want)]==want,
             "brak kafelkow — nie da sie sprawdzic" if not s.jtiles
             else "martwe kotwice %s; kafelkow %d przy %d komponentach; w panelu %s, oczekiwano %s"
                  % (dead[:3], len(s.jtiles), len(comps), nums[:len(want)], want))
    else:
        need("37","zakladka Component versions ma dane", False, "brak tablicy components w stanie")
        need("40","kafelki nawigacji", False, "brak tablicy components w stanie")
    # 35 (wariant B §5ae): plaszczyzna siedzi na .navstack, nie na nav.anchors
    need("35b","pasek ma dwa opisane rzedy w jednej ramce .navstack",
         s.navstack==1 and s.navrows==2,
         "navstack=%d (ma byc 1), navrow=%d (ma byc 2)" % (s.navstack, s.navrows))

    # ---- 41-44: mapa Graph API (§5ah). Bramka czyta plik, wiec sprawdza, czy strona NIESIE
    # to, co przebieg twierdzi, ze przeczytal. Liczbe par podaje sam przebieg w `pairs`;
    # asercja pyta, czy tyle samo da sie z niej odczytac. Mapa bez `pairs` to brak sprawdzenia.
    gm=(st["soc-brief-state"] or {}).get("graphMap") or {}
    need("41","graphMap w bloku stanu, blokow JSON nadal dwa",
         bool(gm) and all(k in gm for k in ("commit","readOn","p","m")) and s.jsonblocks==2,
         "brak graphMap" if not gm else "brakuje pol %s; blokow JSON %d" % (
             [k for k in ("commit","readOn","p","m") if k not in gm], s.jsonblocks))
    if gm:
        def dec(txt):
            n=0
            for grp in (txt or "").split(";"):
                if not grp or ":" not in grp: continue
                for part in grp.split(":",1)[1].split(","):
                    if "-" in part:
                        a,b=part.split("-",1); n+=int(b)-int(a)+1
                    elif part: n+=1
            return n
        gp=gm.get("perms") or {}
        got=sum(dec(v.get("eps")) for v in gp.values())
        want=gm.get("pairs")
        need("42","nic nie obciete z mapy endpointow",
             isinstance(want,int) and got==want,
             "brak pola pairs — nie da sie sprawdzic" if not isinstance(want,int)
             else "zdekodowano %d par, przebieg przeczytal %d" % (got,want))
        noschema=[k for k,v in gp.items()
                  if not all(isinstance(x,dict) and "l" in x and "c" in x for x in (v.get("s") or {}).values())]
        need("43","privilegeLevel i zgoda na kazdym schemacie, chip zgody w dwoch kolorach",
             not noschema and "admin consent required" in h and "no admin consent" in h
             and "t-bad" in h and "t-ok" in h,
             "bez pol l/c: %s; czerwony=%s zielony=%s" % (
                 noschema[:3], "admin consent required" in h, "no admin consent" in h))
        withroles={k:v for k,v in gp.items() if v.get("roles")}
        over=[k for k,v in withroles.items() if any((r[1] if len(r)>1 else 0)>100 for r in v["roles"])]
        need("44","derywacja rol ma regule, glebokosc i sensowne pokrycie",
             bool(withroles) and not over and s.rulebox>=1
             and ("whole resource" in h and "selected properties only" in h),
             "zadne uprawnienie nie ma tablicy roles — nie da sie sprawdzic" if not withroles
             else "pokrycie >100%% w %s; rulebox=%d; kolumna Depth=%s" % (
                 over[:3], s.rulebox,
                 "whole resource" in h and "selected properties only" in h))
    else:
        for no,name in (("42","mapa endpointow"),("43","privilegeLevel i zgoda"),("44","derywacja rol")):
            need(no,name,False,"brak graphMap — nie da sie sprawdzic")
    # ---- 45-47: rejestr 14 dni (§5aj). Potrzebuje katalogu site/, wiec bez niego
    # pozycje sa BRAKIEM z powodem, nigdy cicho pominiete.
    import datetime as _d2, os as _os
    if site:
        cl_p=_os.path.join(site,"data","changelog.json")
        prev_p=_os.path.join(site,"data","changelog.prev.json")
        if not _os.path.exists(cl_p):
            need("45","rejestr zmian dopisany",False,"brak %s" % cl_p)
            need("47","rejestr nie przepisany",False,"brak rejestru")
        else:
            cl=json.load(open(cl_p,encoding="utf-8"))
            runs=cl.get("runs") or []; ent=cl.get("entries") or []
            ret=cl.get("retentionDays") or 90
            today=(st["soc-brief-state"] or {}).get("briefDate") or _d2.date.today().isoformat()
            oldest=min((e.get("seen","") for e in ent), default=today)
            too_old=(_d2.date.fromisoformat(today)-_d2.date.fromisoformat(oldest)).days > ret if oldest else False
            need("45","rejestr zmian dopisany, wpis runs na dzis, nic starszego niz retencja",
                 any(r.get("date")==today for r in runs) and not too_old,
                 "runs bez dzisiejszej daty %s" % today if not any(r.get("date")==today for r in runs)
                 else "najstarszy wpis %s przy retencji %d dni" % (oldest,ret))
            if not _os.path.exists(prev_p):
                need("47","rejestr nie przepisany",False,
                     "brak changelog.prev.json — brak punktu odniesienia, nie da sie sprawdzic")
            else:
                prev=json.load(open(prev_p,encoding="utf-8"))
                key=lambda e:(e.get("seen"),e.get("tab"),e.get("kind"),e.get("id"),e.get("field"))
                old_before={key(e):e for e in (prev.get("entries") or []) if e.get("seen","")<today}
                new_before={key(e):e for e in ent if e.get("seen","")<today}
                changed=[k for k,v in old_before.items() if new_before.get(k)!=v]
                need("47","rejestr nie przepisany — wpisy sprzed dzis identyczne",
                     not changed, "%d wpisow z przeszlosci zmieniono albo usunieto" % len(changed))
    else:
        need("45","rejestr zmian dopisany",False,"nie podano katalogu site/ — uruchom gate.py <html> <site>")
        need("47","rejestr nie przepisany",False,"nie podano katalogu site/")
    need("46","kazda zakladka tresciowa ma pasek 14 dni z prawdziwym licznikiem",
         bool(s.chg14) and all(c==r for c,r in s.chg14),
         "brak details.chg14" if not s.chg14
         else "licznik rozny od liczby wierszy w %d zakladkach" % sum(1 for c,r in s.chg14 if c!=r))

    # 48: §5ak — dane w bloku stanu nie sa renderem. Zmierzone 7 wrzesnia 2026: mapa kompletna,
    # bramka 45/46, a `details.eps` wyrenderowany RAZ poza panelem, wiec zaden z 1 076 wpisow
    # katalogu go nie pokazywal. Bramka czyta plik, wiec pyta o OBECNOSC skryptu i jego zaczepy;
    # to, czy panel sie wypelnia, sprawdza Playwright (§5h) — i to rozroznienie jest tu cala pointa.
    hasmap = bool((st["soc-brief-state"] or {}).get("graphMap", {}).get("perms"))
    s6 = all(k in h for k in ("v13pane", "epsinject", "s6exact", "cat-detail-inner")) and "SCRIPT 6" in h
    # Bez mapy pozycja NIE moze dac OK — pusty zbior spelnia kazdy warunek, a 41 juz wtedy krzyczy.
    need("48","SKRYPT 6 wypelnia kazdy panel uprawnienia (§5ak)",
         hasmap and s6,
         "brak graphMap — nie da sie sprawdzic" if not hasmap
         else "graphMap jest, a skryptu 6 nie ma — dane sa w stanie, czytelnik ich nie zobaczy: %s" % (
             ", ".join(k for k in ("SCRIPT 6","v13pane","epsinject","s6exact","cat-detail-inner") if k not in h)))
    # ---- 49-52: uklad v16 w obu zakladkach (§5al). Bramka czyta PLIK, wiec pyta
    # o obecnosc skryptow i o ksztalt danych; to, czy panel sie wypelnia i czy `+`
    # otwiera go naprawde, sprawdza Playwright (§5h). To rozroznienie jest cala
    # pointa pozycji 48 i powtarza sie tutaj.
    K49 = ("SCRIPT 7","v13role","actinject","__socOpenRole","s7exact","s7tips","rolerank")
    need("49","SKRYPT 7 buduje panel roli w ukladzie v16 (§5al)",
         all(k in h for k in K49) and "el(\"details\", \"rank\")" not in h,
         "brak: %s" % ", ".join(k for k in K49 if k not in h))
    led=(st["soc-brief-state"] or {}).get("ledger14") or {}
    lent=led.get("entries") or []
    ents=[e for e in lent if any(isinstance(v,str) and re.search(r"&(?:mdash|rarr|minus|middot);",v)
                                 for v in e.values())]
    packed=[e for e in lent if isinstance(e.get("id"),str) and ("\u2192" in e["id"] or "->" in e["id"])]
    notab=[e for e in lent if not e.get("tab")]
    need("50","ledger14 w bloku stanu, bez encji i bez zdan w polu id",
         bool(led) and bool(led.get("runs")) and s.jsonblocks==2
         and not ents and not packed and not notab,
         "brak ledger14 — nie da sie sprawdzic" if not led
         else "runs=%s, blokow JSON=%d, wpisow z encja=%d, z pakietem w id=%d, bez tab=%d"
              % (bool(led.get("runs")), s.jsonblocks, len(ents), len(packed), len(notab)))
    need("51","SKRYPT 8 buduje gore zakladki i rejestr 14 dni z opisanymi osiami",
         all(k in h for k in ("SCRIPT 8","chg14","axt","howto","How to read this")),
         "brak: %s" % ", ".join(k for k in ("SCRIPT 8","chg14","axt","howto","How to read this") if k not in h))
    need("52","`+` w wierszu historii otwiera panel katalogu",
         all(k in h for k in ("__socOpenPerm","__socOpenRole","__socHistSection","hd-in","data-hist")),
         "brak: %s" % ", ".join(k for k in ("__socOpenPerm","__socOpenRole","__socHistSection","hd-in","data-hist") if k not in h))
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
    sys.exit(gate(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
```

**Rozszerzone 6 wrzesnia 2026 o pozycje 41-47 (§5ah mapa Graph API, §5aj rejestr 14 dni).**
Bramka przyjmuje teraz drugi argument: `python3 gate.py <gotowy.html> <katalog site/>`. Bez niego
pozycje 45 i 47 daja `BRAK „nie podano katalogu site/"` — **nie sa pomijane w ciszy**, bo to ten sam
blad co asercja przechodzaca na pustych danych. Pozycja 42 jest tu najwazniejsza i odpowiada na
pytanie „czy przebieg przepisal cala mape": **dekoduje `eps` na gotowej stronie i porownuje z liczba
par, ktora przebieg sam zapisal w `pairs`.** Roznica znaczy, ze cos obcial, i nie da sie jej
wytlumaczyc gustem. Kontrola regresji na osmiu wariantach: (a) poprawna strona i poprawny rejestr —
`41-47 OK`; (b) `pairs` 9 przy piu zdekodowanych — `42 BRAK` z obiema liczbami; (c) chip mowi
7 zmian przy trzech wierszach — `46 BRAK`; (d) mapa bez tablicy `roles` — `44 BRAK „nie da sie
sprawdzic"`, nie OK; (e) stan bez `graphMap` — `41` BRAK plus `42-44 BRAK „nie da sie sprawdzic"`;
(f) rejestr z przepisanym wpisem z przeszlosci — `47 BRAK` z liczba; (g) rejestr bez dzisiejszego
wpisu w `runs` — `45 BRAK`; (h) wpis starszy niz retencja — `45 BRAK` z data. Pozycje 0-40 daja
przy tym **identyczne werdykty co przed zmiana** — sprawdzone diffem calego wyjscia.

Licznik paska 14 dni czyta sie **z chipa w podpisie, nie z calego podpisu**: pierwsza wersja brala
pierwsza liczbe z tekstu i trafiala w „last **14** days" zamiast w liczbe zmian. To ta sama rodzina
bledow co podciag „61"/„120" w pozycji 32 — asercja, ktora patrzy na zla liczbe, przechodzi albo
zapala sie z niewlasciwego powodu.

**Rozszerzone 6 wrzesnia 2026 o pozycje 40 (§5ag, kafelki nawigacji) — i pierwsza wersja tej asercji
byla zla.** Pytala `all(w in nums for w in want)`, czyli czy liczba GDZIEKOLWIEK wystepuje w panelu,
i przechodzila na stronie z blednym licznikiem komponentow, bo ta sama cyfra stala w wierszu obok.
To ten sam blad co podciag „61"/„120" w pozycji 32: asercja przechodzaca z niewlasciwego powodu.
Teraz porownanie jest POZYCYJNE. Kontrola regresji na czterech wariantach (3 komponenty, 4 wersje):
(p) poprawna — `40 OK`; (q) jeden kafelek celujacy w nieistniejaca sekcje — `40 BRAK` z nazwa martwej
kotwicy; (r) panel podaje 5 komponentow zamiast 3 — `40 BRAK [5, 4] przy [3, 4]`; (s) jeden kafelek
mniej niz komponentow — `40 BRAK 2 przy 3`. Wariant bez tablicy `components` daje `40 BRAK
„nie da sie sprawdzic"`, nie OK.

**Rozszerzone 6 wrzesnia 2026 o pozycje 37-39 (§5ag) i o wariant B pozycji 35 (§5ae).** Pozycja 38
jest tu najwazniejsza i jest odpowiedzia na pytanie wlasciciela „na jakiej podstawie wybrales te
trzy poprawki": **bramka liczy `li.relitem` na gotowej stronie i porownuje z liczba punktow
`releases[].groups[].items[]` w bloku stanu.** Roznica znaczy, ze przebieg cos wyciol, i nie da sie
jej wytlumaczyc gustem. Kontrola regresji na dziesieciu wariantach tej samej strony: (a) poprawna —
`37/38/39/35b OK`; (b) dwa punkty niewyrenderowane — `38 BRAK 4 przy 6`, a przy okazji `39 BRAK`,
bo odsetek wypromowanych skoczyl do 75%; (c) podpis `Show the remaining 3 of 3` — `38 BRAK`
z cytatem podpisu; (d) platforma `win-typo` spoza slownika — `37 BRAK` z nazwa; (e) brak
`div.rulebox` — `39 BRAK`; (f) jeden wypromowany punkt bez etykiety `.rcat` — `39 BRAK 2 przy 3`;
(g) wszystko wypromowane — `39 BRAK 100%`; (h) jeden `.navrow` zamiast dwoch — `35b BRAK`;
(i) brak `.vbox` przy istniejacej wersji — `37 BRAK 0 przy 1`; (j) stan bez tablicy `components` —
`37 BRAK „brak tablicy components"`, **nie OK**. Ten ostatni wariant jest ta sama pulapka co przy
pozycjach 23 i 32: zbior pusty spelnia kazdy warunek, wiec asercja musi odroznic „sprawdzone
i zgodne" od „nie bylo czego sprawdzac".

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
| `tab-components` | `Component versions` | `components` |
| `tab-hunting` | `Hunting & actions` | `kql` · `actions` · `strategic` |
| `tab-sources` | `Sources` | `sources` |

**Paneli jest DZIESIEC od 6 wrzesnia 2026.** `tab-components` dolozony wraz z §5ag; pasek zakladek przechodzi wtedy na dwa opisane rzedy (§5ae, wariant B). Kazda asercja liczaca panele albo zakladki mowi 10, nie 9 — pozycje 3 i 26 listy §0 sa juz poprawione.

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
to jest ta roznica miedzy 11 638 B a 3 635 058 B.

**Jedyny wyjatek od „bez skryptow" to przelacznik motywu, i jest nim z powodu.** Wlasciciel zglosil
3 wrzesnia 2026: *„ten html z diff nie ma przelacznika do motywu"*. Arkusz tej strony wozi OBA
motywy — `prefers-color-scheme` plus `[data-theme]` — wiec bez przycisku czytelnik jest zamkniety
w tym, co narzucil mu system, podczas gdy brief obok ma `Theme` od poczatku. Dwa male bloki:
w `<head>` przywrocenie zapamietanego wyboru przed pierwszym malowaniem (bez tego strona mruga),
na koncu `<body>` obsluga klikniecia. Zachowanie **identyczne z przyciskiem w briefie** — przerzuca
jasny/ciemny wzgledem tego, co widac teraz — plus zapamietanie w `localStorage` w `try/catch`,
bo strone zmian sie odswieza, a wracanie do motywu systemu przy kazdym odswiezeniu bylo by tym
samym co brak przycisku. `verify()` zada `id="themebtn"` i klucza `soc-diff-theme`: regula bez
asercji jest sugestia, a sugestie przebieg pomija.

Ma **jeden ekran, przewijany**, w tej kolejnosci:

1. **Masthead** — `Microsoft SOC — what changed`, `<data poprzednia> → <data biezaca>`, etykieta
   porownania (`morning pass 06:35 → evening pass 21:14`), godzina policzenia, autor i link do `/`,
   a po prawej stronie **przycisk `Theme`** (`.hdr-tools > button#themebtn`, jak w briefie).
2. **Pigulki liczbowe** — `N added`, `N removed`, `N changed`, `N deadlines moved`,
   `±N Graph permissions`, `±N role entries`, `N items in state (was M)`. Zero jest wartoscia
   poprawna i tez sie pokazuje.
3. **`What changed, by tab`** — sekcja `id="bytab"`, tabela `Tab | Added | Removed | Changed |
   Areas touched`, jeden wiersz na zakladke, **ZAWSZE SZESC wierszy** (§3a).
4. **Added** — `Product | Item | Status | Published | Deadline | Weight | Source`, **jedna tabela
   na zakladke**, z `<caption class="tabcap">` niosacym nazwe zakladki, licznik i obszary;
   sortowane `tier0Touch` malejaco, `socWeight` rosnaco, termin rosnaco (§5p).
5. **Removed** — to samo bez `Status`, tak samo grupowane. **Usuniecie jest znaleziskiem**,
   nie sprzataniem.
6. **Changed, field by field** — grupowane po zakladce, JEDEN WIERSZ NA POLE:
   `Item | Field | before → after | Source`,
   stara wartosc w `<del>`, nowa w `<ins>`. Pola porownywane, w tej kolejnosci: `deadline`,
   `status`, `published`, `tier`, `socWeight`, `tier0Touch`, `title`, `officialTitle`,
   `reference`, `fingerprint`, `url`, `linkStatus`, `product`, `area`.
7. **Component versions** — sekcja `id="components"`. Tabela roznic pole po polu: `Version on <platforma>`
   ze stara wartoscia w `<del>` i nowa w `<ins>`, dalej `State`, `Deadline`, `Provenance`, `Checked on`.
   **Porownanie idzie PER PLATFORMA**: Authenticator, ktory ruszyl sie na iOS a nie na Androidzie, daje
   jeden wiersz, nie dwa. Pod tabela, dla kazdego komponentu ktoremu ruszyla wersja, **blok
   `<div class="relnew">` z trescia NOWEGO wydania** — grupy i punkty wydawcy, limit 20 punktow
   i licznik „and N more in this release". Nowe wydanie nie istnialo w poprzednim stanie, wiec jest
   roznica, a nie powtorzeniem briefu; to ono odpowiada na pytanie „co ta nowa wersja wnosi".
   **Reguly promocji z §5ag tu sie NIE powtarza** — dwie kopie jednej reguly rozjezdzaja sie, wiec
   zamiast wybierac, pokazuje sie cale wydanie z twardym limitem.

8. **Catalog — zakladki Graph API i Roles** — dodane / usuniete nazwy uprawnien i rol oraz wpisy,
   ktorym ruszyl `kind`, `docStatus`, `version`, `changed` albo `serviceStatus`. Dwie tabele,
   kazda z podpisem nazywajacym swoja zakladke. **Kazda nazwa, ktora nadal istnieje w katalogu,
   niesie kotwice `↗` do swojego panelu w briefie** (`/#graph:perm=…`, `/#roles:role=…`, §5al):
   ta strona z zalozenia nie ma katalogu, wiec nie otworzy panelu u siebie, ale ma w niego wskazac.
   `verify()` odrzuca strone, na ktorej wiersz katalogu takiej kotwicy nie ma.
9. **Graph endpoints** — sekcja `id="endpoints"` (§5ah). Porownanie `graphMap` PARA PO PARZE:
   endpointy, ktore uprawnienie zyskalo, ktore stracilo, oraz ruch `privilegeLevel`
   i `requiresAdminConsent`. **To sa endpointy, nie pozycje**, i dlatego maja WLASNY, szosty wiersz
   w podsumowaniu — doliczenie ich do wiersza `Graph API` zmieszaloby dwie rozne jednostki.
   Nota sekcji mowi to, co czyni ja wazna dla SOC: **endpoint dopisany do juz nadanej zgody nie
   wywoluje zadnego promptu, wiec nie ma go w sladzie audytowym** (to jest `Existing permission
   gained reach` z §5g, tylko policzone).
10. **Stopka** — laczna liczba roznic albo zdanie, ze nie ma zadnej.

**Kubelek pusty mowi to zdaniem, nie znika.** „Nothing was removed." jest wynikiem; brak sekcji
zostawia czytelnika z pytaniem, czy przebieg patrzyl.

### 3a. KAZDA ZMIANA STOI W SWOJEJ ZAKLADCE — i jest podsumowanie, ktore to zbiera

Wlasciciel zglosil 3 wrzesnia 2026, po pierwszym przebiegu na policzonej stronie zmian:
*„kazda zakladka powinna pokazac tylko roznice od rana. Jakies podsumowanie tez zbiorcze, co
w jakich zakladkach i obszarach sie zmienilo — np. co zostalo usuniete, co dodane; jak zostalo
dodane nowe api albo rola, to powinno sie tylko to wyswietlac w zakladce, do ktorej przynalezy."*

Plaska lista „7 added" odpowiada na pytanie ILE, nie na pytanie GDZIE. Czytelnik, ktory rano
patrzyl na dziewiec zakladek, wieczorem pyta o te same dziewiec — a nie o jeden wor.

1. **Kazda pozycja ma DOM i jest liczona dokladnie raz.** Dom wyliczasz z `tier`, bo to jedyne
   pole mowiace, gdzie brief ja renderuje: `published-in-window` → **New**; `deadline-under-60-days`,
   `recently-elapsed`, `horizon` → **Deadlines**; wpis katalogu `graph` → **Graph API**; wpis
   katalogu `roles` → **Roles**; wpis tablicy `components` → **Component versions**. Pozycja bez
   `tier`, ale z terminem, idzie do Deadlines.
2. **Today i Products nie sa niczyim domem.** Today jest wyborem z tych samych pozycji (§5m),
   a Products drugim widokiem okna — liczenie ich osobno podwoiloby kazda zmiane. Nota sekcji
   mowi to wprost, zeby czytelnik nie szukal ich w tabeli.
3. **Podsumowanie ma SZESC wierszy zawsze**, takze z samymi zerami. `New | 0 | 0 | 0 | —` znaczy
   „sprawdzone, nic sie nie ruszylo" i jest wynikiem; brak wiersza znaczy „nie wiadomo".
   **Od 6 wrzesnia 2026 wierszy jest szesc** — dochodzi `Component versions` (§5ag) oraz
   `Graph endpoints` (§5ah, jednostka to endpoint, nie pozycja), ktorej domem jest
   tablica `components` w bloku stanu, porownywana PER PLATFORMA: Authenticator, ktory ruszyl sie na
   iOS a nie na Androidzie, daje jeden wiersz roznicy, nie dwa.
4. **Kolumna `Areas touched`** wymienia wartosci `product` dotkniete w tej zakladce, do osmiu, potem
   wielokropek. To jest „w jakich obszarach" ze zgloszenia.
5. **Kubelek pusty zachowuje SWOJ PODPIS.** `<p class="emptycap">` z nazwa zakladki stoi nad zdaniem
   „No role changed." — samo zdanie bez nazwy nie mowi, ktora zakladka jest cicha.

### Zmierzone 3 wrzesnia 2026 — trzy wejscia, ta sama bramka

| wejscie | rozmiar | podsumowanie per zakladka |
|---|---|---|
| ranek 07:14 → wieczor 21:15 (ten sam dzien) | **17 052 B** | New +7 (Entra · M365 admin · Dynamics 365), Deadlines 0/0/0, Graph API +35, Roles 0/0/0 |
| brief 31 sierpnia → wieczor 3 wrzesnia | **186 418 B** | New +59 / 71 zmienionych, Deadlines +10 / 86, Graph API +69 / 331, Roles 0 / 0 / 7 |
| ten sam stan po obu stronach | **9 899 B** | cztery wiersze samych zer |

Przelacznik motywu zmierzony na wszystkich trzech wejsciach, w czterech kombinacjach (system jasny
i ciemny, 1400 i 390 px): start bez atrybutu `data-theme` czyli na motywie systemu, **pierwszy klik
przerzuca na przeciwny** (`rgb(247,247,244)` ↔ `rgb(22,23,26)` na `body`), drugi wraca, a po
`reload` wybor **zostaje**. Przycisk stoi w gornym wierszu na prawo od tytulu, ma nieprzezroczyste
tlo w obu motywach (`rgb(240,240,236)` / `rgb(37,39,44)`), zero bledow konsoli i strony,
`scrollWidth === clientWidth` przy 390 i 1400.

Render headless, jasny i ciemny, 1400x1100 i 390x844, wszystkie trzy wejscia: **zero bledow konsoli
i strony**, `scrollWidth === clientWidth` w obu szerokosciach, `#bytab` obecne z czterema wierszami,
link powrotny w stopce. Dwa bledy wlasnego renderu znalezione i poprawione w tym samym przebiegu:
tabela pusta **gubila podpis** (`table()` zwracalo samo zdanie, wiec „No role changed." wisialo bez
nazwy zakladki), a podsumowanie **pokazywalo tylko zakladki, ktore sie ruszyly** — czyli dokladnie
nie odpowiadalo na pytanie „ktora byla cicha".

`verify()` zyskal asercje: sekcja `bytab` istnieje, a **kazda zakladka z niezerowym licznikiem
w podsumowaniu ma na dole tabele z tym podpisem**. Bez niej podsumowanie moglo by podac liczbe,
ktorej nic nie pokrywa — a ono jest cala tresc tej strony.

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
python3 /tmp/make_diff.py <poprzedni> <biezacy> <wyjscie.html> [--home /] [--label "..."] [--ledger site/data/changelog.json]
```

**`--ledger` jest OBOWIAZKOWA w obu przebiegach dnia** (§5aj). Ta sama funkcja, ktora liczy strone,
dopisuje rejestr 14-dniowy; przed dopisaniem kopiuje `changelog.json` do `changelog.prev.json`,
zeby pozycja 47 listy §0 miala z czym porownac. Zmierzone: dopisanie tych samych dwoch stanow
drugi raz tego samego dnia daje **+0 wpisow** (deduplikacja po `(seen, tab, kind, id, field)`),
a pusty rejestr powstaje sam przy pierwszym uruchomieniu.

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
co sie zmienilo pole po polu. Bez dziesieciu zakladek, bez przegladarki katalogu i bez
kopiowania megabajtow JSON, ktorych taka strona nie uzywa.
"""
import sys, os, re, json, html, datetime
from urllib.parse import quote as _q

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

# ---------- ktora zakladka briefu jest DOMEM tej pozycji ----------
# Wlasciciel, 3 wrzesnia 2026: „kazda zakladka powinna pokazac tylko roznice od rana …
# jak zostalo dodane nowe api albo rola, to powinno sie to wyswietlac w zakladce, do ktorej
# przynalezy." Dom pozycji wyliczamy z `tier`, bo to jedyne pole, ktore mowi, gdzie brief ja
# renderuje. Today jest WYBOREM z tych samych pozycji (§5m), wiec nie jest niczyim domem —
# inaczej ta sama zmiana stanelaby w dwoch miejscach i licznik klamalby.
TIER_TAB = {
    "published-in-window":    "New",
    "deadline-under-60-days": "Deadlines",
    "recently-elapsed":       "Deadlines",
    "horizon":                "Deadlines",
}
TAB_ORDER = ["New", "Deadlines", "Graph API", "Graph endpoints", "Roles", "Component versions"]
# Zakladki, ktore ta strona potrafi zliczyc, i ktore dostaja wiersz ZAWSZE — takze z trzema zerami.
# Today i Products nie sa niczyim domem: Today jest wyborem (§5m), a Products drugim widokiem tych
# samych pozycji okna, wiec ich ruch jest juz policzony w New i Deadlines. Liczenie ich osobno
# podwoiloby kazda zmiane.
SUMMARY_TABS = ["New", "Deadlines", "Graph API", "Graph endpoints", "Roles", "Component versions"]

def tab_of(it):
    t = TIER_TAB.get(norm(it.get("tier")))
    if t: return t
    return "Deadlines" if norm(it.get("deadline")) else "New"

def group(rows, keyfn):
    """Zwraca [(zakladka, [wiersze])] w kolejnosci TAB_ORDER; nieznane zakladki na koncu."""
    g = {}
    for r in rows: g.setdefault(keyfn(r), []).append(r)
    known = [(t, g.pop(t)) for t in TAB_ORDER if t in g]
    return known + sorted(g.items())

def areas(items):
    """Obszary (product) dotkniete w tej zakladce — odpowiedz na 'w jakich obszarach'."""
    seen = []
    for i in items:
        a = norm(i.get("product")) or "unspecified"
        if a not in seen: seen.append(a)
    return seen

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

# Pola komponentu, ktorych ruch jest ZMIANA. §5ag: wersja, stan wydania i termin.
COMPONENT_FIELDS = [("state","State"),("deadline","Deadline"),("provenance","Provenance"),
                    ("checkedOn","Checked on")]

def comp_versions(c):
    """Wersje jako {platforma: numer} — porownanie idzie per platforma, bo komponent
    o dwoch platformach (Authenticator) rusza sie na kazdej osobno."""
    return {norm(v.get("platform")): norm(v.get("version")) for v in (c.get("versions") or [])}

def diff_components(prev, curr):
    p = {c.get("id"): c for c in (prev.get("components") or []) if c.get("id")}
    c = {x.get("id"): x for x in (curr.get("components") or []) if x.get("id")}
    added   = [c[k] for k in c if k not in p]
    removed = [p[k] for k in p if k not in c]
    changed = []
    for k in c:
        if k not in p: continue
        deltas = []
        pv, cv = comp_versions(p[k]), comp_versions(c[k])
        for plat in sorted(set(pv) | set(cv)):
            if pv.get(plat, "") != cv.get(plat, ""):
                deltas.append(("Version on " + (plat or "unspecified"), pv.get(plat, ""), cv.get(plat, "")))
        for f, lab in COMPONENT_FIELDS:
            if norm(p[k].get(f)) != norm(c[k].get(f)):
                deltas.append((lab, norm(p[k].get(f)), norm(c[k].get(f))))
        if deltas: changed.append((c[k], deltas))
    return added, removed, changed, len(p), len(c)

# ---------- mapa Graph API (§5ah) ----------

def gm_paths(st):
    """{uprawnienie: {(metoda, sciezka)}} — dekoduje `eps` ze slownika i przedzialow."""
    gm = (st or {}).get("graphMap") or {}
    M, P = gm.get("m") or [], gm.get("p") or []
    out = {}
    for name, d in (gm.get("perms") or {}).items():
        s_ = set()
        for grp in (d.get("eps") or "").split(";"):
            if not grp or ":" not in grp: continue
            mi, body = grp.split(":", 1)
            try: meth = M[int(mi)]
            except Exception: continue
            for part in body.split(","):
                if not part: continue
                if "-" in part:
                    a, b = part.split("-", 1)
                    rng = range(int(a), int(b) + 1)
                else:
                    rng = [int(part)]
                for i in rng:
                    if 0 <= i < len(P): s_.add((meth, P[i]))
        out[name] = s_
    return out

def gm_schemes(st):
    gm = (st or {}).get("graphMap") or {}
    return {n: (d.get("s") or {}) for n, d in (gm.get("perms") or {}).items()}

def diff_graphmap(prev_st, curr_st):
    """Zwraca (wiersze, liczniki). Wiersz = (uprawnienie, rodzaj, tekst przed, tekst po).

    PIERWSZY PRZEBIEG PO WPROWADZENIU MAPY: wczorajszy plik danych jej nie ma. Bez tego
    warunku porownanie zbioru pustego z pelnym oglasza KAZDY endpoint jako dodany dzisiaj —
    zmierzone 7 wrzesnia 2026 na prawdziwych danych: **9 736 wierszy i „24 099 added"**,
    strona nie do przeczytania, a rejestr §5aj dostalby tyle samo falszywych wpisow.
    Brak punktu odniesienia nie jest zmiana. To ta sama zasada co `state:"baseline"` w §5ag
    i `BRAK „nie da sie sprawdzic"` w §0b: pusty zbior spelnia kazdy warunek, wiec trzeba
    odroznic „sprawdzone i zgodne" od „nie bylo z czym porownac"."""
    prev_has = bool(((prev_st or {}).get("graphMap") or {}).get("perms"))
    curr_has = bool(((curr_st or {}).get("graphMap") or {}).get("perms"))
    if curr_has and not prev_has:
        n = len((curr_st["graphMap"] or {}).get("perms") or {})
        return ([("\u2014", "baseline", "",
                  "First run carrying graphMap: %d permissions recorded. The previous state has no "
                  "endpoint map, so there is nothing to compare against and nothing here is a change. "
                  "Tomorrow's run reports real differences." % n)], 0, 0, 0)
    pp, cp = gm_paths(prev_st), gm_paths(curr_st)
    ps, cs = gm_schemes(prev_st), gm_schemes(curr_st)
    rows, add, rem, chg = [], 0, 0, 0
    for name in sorted(set(pp) | set(cp)):
        a, b = pp.get(name, set()), cp.get(name, set())
        gained, lost = sorted(b - a), sorted(a - b)
        for m, p in gained[:40]:
            rows.append((name, "endpoint added", "", "%s %s" % (m, p))); add += 1
        if len(gained) > 40:
            rows.append((name, "endpoint added", "", "\u2026 and %d more" % (len(gained) - 40)))
        add += max(0, len(gained) - 40)
        for m, p in lost[:40]:
            rows.append((name, "endpoint removed", "%s %s" % (m, p), "")); rem += 1
        rem += max(0, len(lost) - 40)
        for k in sorted(set(ps.get(name, {})) | set(cs.get(name, {}))):
            o, n = (ps.get(name) or {}).get(k) or {}, (cs.get(name) or {}).get(k) or {}
            if norm(o.get("l")) != norm(n.get("l")):
                rows.append((name, "privilege level \u00b7 " + k, norm(o.get("l")), norm(n.get("l")))); chg += 1
            if norm(o.get("c")) != norm(n.get("c")):
                rows.append((name, "admin consent \u00b7 " + k,
                             "required" if o.get("c") else "not required",
                             "required" if n.get("c") else "not required")); chg += 1
    return rows, add, rem, chg

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

def deep_link(tab, key, home="/"):
    """Strona zmian nie ma katalogu (§3), wiec nie otworzy panelu u siebie —
    ale moze w niego wskazac. Skrypty 6 i 7 czytaja te kotwice (§5al)."""
    if not key: return ""
    frag = ("graph:perm=" if tab == "Graph API" else "roles:role=") + key
    # spacja w nazwie roli musi byc zakodowana, inaczej kotwica jest niepoprawnym URL-em
    return (' <a class="deep" href="%s#%s" title="Open the full panel in the brief">\u2197</a>'
            % (esc(home), esc(_q(frag, safe="=:/."))))

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

def table(head, rows, empty, caption=None):
    if not rows:
        # Kubelek pusty mowi to zdaniem — ale musi tez powiedziec, KTORY kubelek jest pusty,
        # inaczej „No role changed." wisi bez nazwy zakladki, ktorej dotyczy.
        lead = ('<p class="emptycap">%s</p>' % caption) if caption else ""
        return lead + '<p class="empty">%s</p>' % esc(empty)
    th = "".join("<th>%s</th>" % h for h in head)   # naglowki sa nasze, nie z danych
    tb = "".join("<tr%s>%s</tr>" % (r[0], "".join("<td>%s</td>" % c for c in r[1])) for r in rows)
    cap = ('<caption class="tabcap">%s</caption>' % caption) if caption else ""
    return ('<div class="tw"><table>%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (cap, th, tb))

def num(n, kind):
    """Licznik w podsumowaniu. ZERO tez sie pokazuje — to wynik, nie brak."""
    if not n: return '<span class="none">0</span>'
    if kind == "add": return '<b class="nadd">+%d</b>' % n
    if kind == "rem": return '<b class="nrem">&minus;%d</b>' % n
    return '<b class="nchg">%d</b>' % n

def tabcap(tab, n, word, items):
    """Podpis tabeli zakladki: nazwa, licznik i obszary — jednym zdaniem."""
    a = [esc(x) for x in areas(items)]
    more = " &middot; …" if len(a) > 8 else ""
    return ('<b>%s</b> &middot; %d %s <span class="capareas">%s%s</span>'
            % (esc(tab), n, esc(word if n != 1 else word.rstrip("s")),
               " &middot; ".join(a[:8]), more))

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
.title-row{display:flex;align-items:flex-start;gap:16px;flex-wrap:wrap}
.title-row>div:first-child{flex:1 1 320px;min-width:0}
.hdr-tools{flex:0 0 auto;margin-left:auto}
.themebtn{background:var(--surface2);border:1px solid var(--border);color:var(--text);border-radius:6px;
 padding:7px 14px;font:inherit;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap}
.themebtn:hover{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
.themebtn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
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
.relnew{border:1px solid var(--border);border-radius:10px;background:var(--surface);
 padding:11px 13px;margin:10px 0 0}
.relnew h3{font-size:13.5px;margin:0 0 2px}
.relnew h3 .rv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ins-fg);
 background:var(--ins-bg);border-radius:6px;padding:1px 7px;margin-left:7px;font-size:12.5px}
.relnew .grp{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);
 font-weight:700;margin:9px 0 4px}
.relnew ul{margin:0;padding-left:19px;font-size:13px}
.relnew li{margin:0 0 5px}
.relnew li:last-child{margin-bottom:0}
caption.tabcap{caption-side:top;text-align:left;padding:9px 10px;background:var(--surface2);
 border-bottom:1px solid var(--border);font-size:13px;color:var(--text)}
caption.tabcap .capareas{color:var(--muted);font-size:12.5px;margin-left:6px}
.emptycap{margin:0 0 4px;font-size:13px;color:var(--text)}
.emptycap .capareas{color:var(--muted);font-size:12.5px;margin-left:6px}
.tw+.tw{margin-top:12px}
b.nadd{color:var(--ins-fg)}b.nrem{color:var(--del-fg)}b.nchg{color:var(--warn)}
tr.quiet td{color:var(--muted)}
.more{color:var(--muted);font-size:13px;margin:8px 0 0}
a{color:var(--accent)}
a.deep{text-decoration:none;font-weight:700;padding:0 5px;border-radius:6px;
 background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent);font-size:11.5px}
a.deep:hover{background:var(--accent);color:var(--surface)}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;
 background:var(--surface2);border:1px solid var(--border);border-radius:5px;padding:1px 5px}
footer{margin:36px 0 0;padding-top:14px;border-top:1px solid var(--border);color:var(--muted);font-size:13px}
@media (max-width:760px){.counts li{white-space:normal}h1{font-size:19px}}
"""

# Strona zmian NIE ma skryptow powloki (§3) — te dwa to jedyny wyjatek i sa nim z powodu:
# arkusz wozi oba motywy, a bez przelacznika czytelnik nie ma czym ich zmienic. Zachowanie jest
# TAKIE SAMO jak przycisk `Theme` w briefie: przerzuca jasny/ciemny wzgledem tego, co widac teraz.
# Dochodzi pamiec wyboru — strona zmian jest odswiezana, a wracanie do motywu systemu przy kazdym
# odswiezeniu bylo by tym samym co brak przycisku.
THEME_HEAD = """<script>
/* przywroc zapamietany motyw PRZED pierwszym malowaniem, zeby nie bylo mrugniecia */
(function(){try{var v=localStorage.getItem('soc-diff-theme');
if(v==='light'||v==='dark')document.documentElement.setAttribute('data-theme',v);}catch(e){}})();
</script>"""

THEME_BODY = """<script>
(function(){
  "use strict";
  var r=document.documentElement, b=document.getElementById('themebtn');
  if(!b) return;
  b.addEventListener('click', function(){
    try{
      var explicit=r.getAttribute('data-theme');
      var dark = explicit==='dark' ||
                 (!explicit && window.matchMedia('(prefers-color-scheme:dark)').matches);
      var next = dark ? 'light' : 'dark';
      r.setAttribute('data-theme', next);
      try{ localStorage.setItem('soc-diff-theme', next); }catch(e){}
    }catch(e){}
  });
})();
</script>"""

def build(prev_st, prev_cat, curr_st, curr_cat, home, label, when):
    added, removed, changed, np_, nc = diff_items(prev_st, curr_st)
    gadd, grem, gmod, gp, gc = diff_catalog(prev_cat, curr_cat, "graph")
    radd, rrem, rmod, rp, rc = diff_catalog(prev_cat, curr_cat, "roles")
    cadd, crem, cmod, cp, cc_ = diff_components(prev_st, curr_st)

    added.sort(key=wkey); removed.sort(key=wkey)
    changed.sort(key=lambda t: wkey(t[0]))
    dl_moved = [(i, d) for i, d in changed if any(l == "Deadline" for l, _, _ in d)]

    prev_d = norm(prev_st.get("briefDate")) or "previous"
    curr_d = norm(curr_st.get("briefDate")) or "current"

    out = []
    out.append('<header class="top"><div class="in"><div class="title-row"><div>'
               '<h1>Microsoft SOC &mdash; what changed</h1>')
    out.append('<p class="dateline">%s &rarr; %s &middot; %s &middot; compared %s Warsaw &middot; '
               'Piotr Wisniewski &middot; <a href="%s">Back to the full brief</a></p></div>'
               '<div class="hdr-tools"><button class="themebtn" id="themebtn" type="button">Theme</button>'
               '</div></div>'
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

    ge_rows, ge_add, ge_rem, ge_chg = diff_graphmap(prev_st, curr_st)

    # --- podsumowanie zbiorcze: co w ktorej zakladce i w jakich obszarach
    # To jest odpowiedz na „jakies podsumowanie tez zbiorcze, co w jakich zakladkach
    # i obszarach sie zmienilo". Zero jest wartoscia i tez ma wiersz.
    tally = {}
    for i_ in added:              tally.setdefault(tab_of(i_), {"a": [], "r": [], "c": []})["a"].append(i_)
    for i_ in removed:            tally.setdefault(tab_of(i_), {"a": [], "r": [], "c": []})["r"].append(i_)
    for i_, _d in changed:        tally.setdefault(tab_of(i_), {"a": [], "r": [], "c": []})["c"].append(i_)
    for tab in SUMMARY_TABS:      tally.setdefault(tab, {"a": [], "r": [], "c": []})

    srows = []
    for tab in SUMMARY_TABS + sorted(k for k in tally if k not in SUMMARY_TABS):
        if tab not in tally: continue
        t = tally[tab]
        if tab == "Graph API":
            na, nr, nc = len(gadd), len(grem), len(gmod)
            ar = "Graph permissions"
        elif tab == "Roles":
            na, nr, nc = len(radd), len(rrem), len(rmod)
            ar = "Entra directory roles"
        elif tab == "Graph endpoints":
            na, nr, nc = ge_add, ge_rem, ge_chg
            ar = "what already-consented permissions can call"
        elif tab == "Component versions":
            na, nr, nc = len(cadd), len(crem), len(cmod)
            ar = " &middot; ".join(esc(x.get("name") or x.get("id"))
                                   for x in (cadd + crem + [t[0] for t in cmod])[:8]) or "&mdash;"
        else:
            na, nr, nc = len(t["a"]), len(t["r"]), len(t["c"])
            ar = " &middot; ".join(esc(x) for x in areas(t["a"] + t["r"] + t["c"])[:8]) or "&mdash;"
        srows.append((' class="quiet"' if not (na or nr or nc) else "",
                      ["<b>%s</b>" % esc(tab), num(na, "add"), num(nr, "rem"), num(nc, "chg"), ar]))
    out.append('<section id="bytab"><h2>What changed, by tab</h2>'
               '<p class="note">What moved since %s, tab by tab, and which areas it touched. '
               'A row of three zeros means that tab was checked and did not move. Each item is counted '
               'in the ONE tab that is its home &mdash; New for the published window, Deadlines for '
               'anything dated, Graph API and Roles for the two catalogs &mdash; so nothing is counted '
               'twice. Today is a selection from New and Deadlines and Products is a second view of the '
               'same items, so their changes are already in these rows.</p>%s</section>'
               % (esc(prev_d),
                  table(["Tab", "Added", "Removed", "Changed", "Areas touched"], srows,
                        "No tab moved at all.")))

    # --- added, grouped by tab
    body = []
    for tab, items_ in group(added, tab_of):
        rows = [(' class="t0"' if i_.get("tier0Touch") else "",
                 [esc(i_.get("product")), name_cell(i_), esc(i_.get("status")),
                  esc(i_.get("published")), esc(i_.get("deadline")) or '<span class="none">none stated</span>',
                  weight_cell(i_), a_src(i_)]) for i_ in items_]
        rows, more = cap(rows, 120, "added items")
        body.append(table(["Product", "Item", "Status", "Published", "Deadline", "Weight", "Source"],
                          rows, "", tabcap(tab, len(items_), "items", items_)) + more)
    out.append('<section id="added"><h2>Added since %s</h2>'
               '<p class="note">In the current state and not in the previous one, one table per tab of '
               'the brief. Heaviest first: tier 0, then SOC weight, then deadline.</p>%s</section>'
               % (esc(prev_d), "".join(body) or
                  '<p class="empty">Nothing was added. That is a result, not a gap.</p>'))

    # --- removed, grouped by tab
    body = []
    for tab, items_ in group(removed, tab_of):
        rows = [("", [esc(i_.get("product")), name_cell(i_), esc(i_.get("published")),
                      esc(i_.get("deadline")) or '<span class="none">none stated</span>',
                      weight_cell(i_), a_src(i_)]) for i_ in items_]
        rows, more = cap(rows, 120, "removed items")
        body.append(table(["Product", "Item", "Published", "Deadline", "Weight", "Source"],
                          rows, "", tabcap(tab, len(items_), "items", items_)) + more)
    out.append('<section id="removed"><h2>Removed</h2>'
               '<p class="note">Carried in the previous state and gone from the current one, by tab. '
               'A removal is a finding: either the source dropped it or this brief retracted it.</p>%s</section>'
               % ("".join(body) or '<p class="empty">Nothing was removed.</p>'))

    # --- changed, field by field, grouped by tab
    body = []
    for tab, pairs in group(changed, lambda t: tab_of(t[0])):
        rows = []
        for i_, deltas in pairs:
            for n, (lab, a, b) in enumerate(deltas):
                first = (n == 0)
                rows.append((' class="t0"' if (first and i_.get("tier0Touch")) else "",
                             [name_cell(i_) if first else '<span class="none">&#8942;</span>',
                              '<span class="field">%s</span>' % esc(lab),
                              ('<del>%s</del>' % esc(a) if a else '<span class="none">not set</span>')
                              + '<span class="arrow">&rarr;</span>'
                              + ('<ins>%s</ins>' % esc(b) if b else '<span class="none">cleared</span>'),
                              a_src(i_) if first else ""]))
        rows, more = cap(rows, 250, "changed fields")
        body.append(table(["Item", "Field", "Before &rarr; after", "Source"], rows, "",
                          tabcap(tab, len(pairs), "items", [x[0] for x in pairs])) + more)
    out.append('<section id="changed"><h2>Changed, field by field</h2>'
               '<p class="note">Same <code>id</code> in both states, different value, by tab. Old struck '
               'through, new highlighted &mdash; the difference is shown, not described.</p>%s</section>'
               % ("".join(body) or
                  '<p class="empty">No field moved on any item carried across both states.</p>'))

    # --- component versions (§5ag): wersja, stan i termin, pole po polu
    crows = []
    for c_, deltas in cmod:
        for n, (lab, aa, bb) in enumerate(deltas):
            first = (n == 0)
            crows.append(("", [("<b>%s</b>" % esc(c_.get("name") or c_.get("id"))) if first
                               else '<span class="none">&#8942;</span>',
                               '<span class="field">%s</span>' % esc(lab),
                               ('<del>%s</del>' % esc(aa) if aa else '<span class="none">not set</span>')
                               + '<span class="arrow">&rarr;</span>'
                               + ('<ins>%s</ins>' % esc(bb) if bb else '<span class="none">cleared</span>'),
                               a_src(c_) if first else ""]))
    for c_ in cadd:
        crows.append(("", ["<b>%s</b>" % esc(c_.get("name") or c_.get("id")),
                           '<span class="field">Tracked</span>',
                           '<span class="none">not tracked</span><span class="arrow">&rarr;</span>'
                           + "<ins>%s</ins>" % esc(", ".join("%s %s" % (k, v) for k, v in
                                                             sorted(comp_versions(c_).items()))),
                           a_src(c_)]))
    for c_ in crem:
        crows.append(("", ["<b>%s</b>" % esc(c_.get("name") or c_.get("id")),
                           '<span class="field">Tracked</span>',
                           "<del>%s</del>" % esc(", ".join("%s %s" % (k, v) for k, v in
                                                           sorted(comp_versions(c_).items())))
                           + '<span class="arrow">&rarr;</span><span class="none">no longer tracked</span>',
                           a_src(c_)]))
    # Wersja, ktora sie ruszyla, ma TRESC — i to jest ta czesc, na ktorej czytelnik dziala.
    # Nowe wydanie nie istnialo w poprzednim stanie, wiec jest roznica, nie powtorzeniem briefu.
    # Reguly promocji z §5ag tu NIE powtarzamy: dwie kopie jednej reguly rozjezdzaja sie
    # (to jest lekcja §0a). Zamiast tego pokazujemy CALE wydanie z twardym limitem i licznikiem.
    REL_CAP = 20
    def new_release(cur, prev_c):
        # zwraca wydanie obecne w biezacym stanie, ktorego nie bylo w poprzednim
        seen = {norm(r.get("version")) for r in ((prev_c or {}).get("releases") or [])}
        for r in (cur.get("releases") or []):
            if norm(r.get("version")) not in seen:
                return r
        return None

    def relblock(c_, rel):
        if not rel: return ""
        o = ['<div class="relnew"><h3>%s<span class="rv">%s</span></h3>'
             % (esc(c_.get("name") or c_.get("id")), esc(rel.get("version")))]
        if rel.get("date"): o.append('<p class="note">%s</p>' % esc(rel.get("date")))
        shown = 0
        for g in (rel.get("groups") or []):
            items = g.get("items") or []
            if not items: continue
            room = REL_CAP - shown
            if room <= 0: break
            if g.get("title"): o.append('<p class="grp">%s</p>' % esc(g["title"]))
            o.append("<ul>%s</ul>" % "".join(
                "<li>%s%s</li>" % (esc(i.get("text")),
                                   (" " + '<a href="%s" target="_blank" rel="noopener">%s</a>'
                                    % (esc(i.get("url")), esc(i.get("label") or "Source")))
                                   if i.get("url") else "")
                for i in items[:room]))
            shown += min(len(items), room)
        total = sum(len(g.get("items") or []) for g in (rel.get("groups") or []))
        if total > shown:
            o.append('<p class="more">… and %d more in this release. The full list is in the brief.</p>'
                     % (total - shown))
        o.append("</div>")
        return "".join(o)

    prevc = {c_.get("id"): c_ for c_ in (prev_st.get("components") or []) if c_.get("id")}
    relblocks = []
    for c_, deltas in cmod:
        if any(l.startswith("Version on") for l, _, _ in deltas):
            relblocks.append(relblock(c_, new_release(c_, prevc.get(c_.get("id")))))
    for c_ in cadd:
        rels = c_.get("releases") or []
        if rels: relblocks.append(relblock(c_, rels[0]))
    relblocks = [x for x in relblocks if x]

    out.append('<section id="components"><h2>Component versions</h2>'
               '<p class="note">Versions %d &rarr; %d tracked components. A component moves when a version '
               'changes on any platform, when its release state changes, or when a deadline moves. '
               '<b>Where a version moved, what the new release contains is printed below the table</b> '
               '&mdash; that release did not exist in the previous state, so it is a difference and not a '
               'repeat of the brief.</p>%s</section>'
               % (cp, cc_, table(["Component", "Field", "Before &rarr; after", "Source"], crows,
                                 "No tracked component moved.")
                  + ("".join(relblocks) if relblocks else "")))

    # --- Graph endpoints (§5ah): co uprawnienie potrafi wywolac, pole po polu
    erows = []
    for nm, what, before, after in ge_rows[:250]:
        erows.append(("", ["<b>%s</b>" % esc(nm), '<span class="field">%s</span>' % esc(what),
                           ("<del>%s</del>" % esc(before) if before else '<span class="none">not there</span>')
                           + '<span class="arrow">&rarr;</span>'
                           + ("<ins>%s</ins>" % esc(after) if after else '<span class="none">gone</span>')]))
    emore = ('<p class="more">… and %d more endpoint rows.</p>' % (len(ge_rows) - 250)) if len(ge_rows) > 250 else ""
    pn = len((prev_st.get("graphMap") or {}).get("perms") or {})
    cn2 = len((curr_st.get("graphMap") or {}).get("perms") or {})
    out.append('<section id="endpoints"><h2>Graph endpoints</h2>'
               '<p class="note">What each permission can call, compared pair by pair from '
               '<span class="mono">graphMap</span> in the two state blocks: %d &rarr; %d permissions carrying a '
               'path set. An endpoint appearing here means Microsoft widened or narrowed what an already-granted '
               'consent reaches &mdash; no consent prompt fires for that, so nothing in the audit trail marks it. '
               'These are endpoints, not items, which is why they have their own row in the summary above.</p>%s%s</section>'
               % (pn, cn2,
                  table(["Permission", "What", "Before &rarr; after"], erows,
                        "No permission gained or lost an endpoint, and no privilege level moved.",
                        '<b>Graph endpoints</b> &middot; +%d / &minus;%d / %d edited' % (ge_add, ge_rem, ge_chg)),
                  emore))

    # --- catalog
    def catrows(add, rem, mod, name, tab=None, home_="/"):
        r = []
        for n in add[:60]: r.append(("", ['<ins>added</ins>', "<code>%s</code>%s" % (esc(n), deep_link(tab, n, home_)), ""]))
        for n in rem[:60]: r.append(("", ['<del>removed</del>', "<code>%s</code>" % esc(n), ""]))
        for n, f, a, b in mod[:60]:
            r.append(("", ["changed", "<code>%s</code>%s" % (esc(n), deep_link(tab, n, home_)),
                           '<span class="field">%s</span> <del>%s</del><span class="arrow">&rarr;</span><ins>%s</ins>'
                           % (esc(f), esc(a) or "not set", esc(b) or "cleared")]))
        extra = len(add) + len(rem) + len(mod) - len(r)
        return r, ('<p class="more">… and %d more %s changes.</p>' % (extra, name) if extra > 0 else "")

    gr, gmore = catrows(gadd, grem, gmod, "Graph", "Graph API", home)
    rr, rmore = catrows(radd, rrem, rmod, "role", "Roles", home)
    # Katalog jest domem DWOCH zakladek — kazda dostaje wlasny podpis, zeby wiersz
    # podsumowania „Graph API / Roles" mial na dole odpowiadajaca mu tabele.
    out.append('<section id="catalog"><h2>Catalog &mdash; Graph API and Roles tabs</h2>'
               '<p class="note">Graph permissions %d &rarr; %d (+%d / &minus;%d, %d entries edited); '
               'roles %d &rarr; %d (+%d / &minus;%d, %d edited). These two tables are the whole of what '
               'moved in those two tabs.</p>%s%s%s%s</section>'
               % (gp, gc, len(gadd), len(grem), len(gmod), rp, rc, len(radd), len(rrem), len(rmod),
                  table(["What", "Graph permission", "Detail"], gr, "No Graph permission changed.",
                        '<b>Graph API</b> &middot; +%d / &minus;%d / %d edited' % (len(gadd), len(grem), len(gmod))),
                  gmore,
                  table(["What", "Role", "Detail"], rr, "No role changed.",
                        '<b>Roles</b> &middot; +%d / &minus;%d / %d edited' % (len(radd), len(rrem), len(rmod))),
                  rmore))

    total = (len(added) + len(removed) + len(changed) + len(gadd) + len(grem) + len(gmod)
             + len(radd) + len(rrem) + len(rmod) + len(cadd) + len(crem) + len(cmod))
    out.append('<footer>%s &middot; Piotr Wisniewski &middot; %s Warsaw &middot; '
               'computed from the two state blocks, not copied from the brief. '
               '<a href="%s">Back to the full brief</a></footer></div>'
               % (("%d differences in total." % total) if total else
                  "No difference at all between the two states. Somebody looked; nothing moved.",
                  esc(when), esc(home)))
    body = "\n".join(out)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>Microsoft SOC &mdash; what changed %s</title>\n<style>%s</style>\n%s\n</head>\n'
            '<body>\n%s\n%s\n</body>\n</html>\n'
            % (esc(curr_d), CSS, THEME_HEAD, body, THEME_BODY))

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
    for need in ("bytab","added","removed","changed","components","endpoints","catalog"):
        if need not in p.ids: e.append("brak sekcji %s" % need)
    # KAZDA zakladka z niezerowym licznikiem w podsumowaniu ma na dole tabele z tym podpisem.
    # Bez tego „podsumowanie per zakladka" moglo by klamac, a to jest cala tresc tej strony.
    m0 = re.search(r'<section id="bytab">.*?</section>', page, re.S)
    if m0:
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", m0.group(0), re.S):
            cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
            if len(cells) < 4: continue
            tab = re.sub(r"<[^>]+>", "", cells[0]).strip()
            nums = [re.sub(r"[^0-9]", "", re.sub(r"<[^>]+>", "", c)) or "0" for c in cells[1:4]]
            if all(n == "0" for n in nums): continue
            if ("<b>%s</b>" % tab) not in page:
                e.append("zakladka %s ma licznik w podsumowaniu, a nie ma tabeli" % tab)
    if p.doct!=1: e.append("DOCTYPE = %d, ma byc 1" % p.doct)
    # Przelacznik motywu: arkusz wozi oba motywy, wiec strona bez przycisku zostawia czytelnika
    # z tym, co narzucil system. Regula bez asercji jest sugestia (§0b) — wiec asercja.
    if 'id="themebtn"' not in page: e.append("brak przycisku motywu (#themebtn)")
    # §5al: wiersz zakladki katalogowej ma prowadzic do panelu w briefie — inaczej
    # czytelnik strony zmian widzi nazwe i nie ma jak zobaczyc, czego dotyczy.
    m3 = re.search(r'<section id="catalog">.*?</section>', page, re.S)
    if m3:
        rows3 = [r for r in re.findall(r"<tr[^>]*>(.*?)</tr>", m3.group(0), re.S) if "<code" in r]
        nolink = [r for r in rows3 if "removed" not in r and 'class="deep"' not in r]
        if nolink: e.append("%d wierszy katalogu bez kotwicy do panelu w briefie" % len(nolink))
    if "soc-diff-theme" not in page: e.append("brak skryptu przelacznika motywu")
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

def ledger(path, prev_st, prev_cat, curr_st, curr_cat, when, kind="morning"):
    """§5aj — rejestr DOPISYWANY. Ta sama funkcja, ktora liczy strone, pisze rejestr:
    dwa niezalezne liczenia tej samej rzeczy rozjezdzaja sie (§0a)."""
    today = norm(curr_st.get("briefDate")) or datetime.date.today().isoformat()
    if os.path.exists(path):
        cl = json.load(open(path, encoding="utf-8"))
        # kopia odniesienia dla pozycji 47 listy §0 — bez niej nie da sie sprawdzic,
        # czy przebieg nie przepisal historii
        json.dump(cl, open(os.path.join(os.path.dirname(path), "changelog.prev.json"),
                           "w", encoding="utf-8"), ensure_ascii=False)
    else:
        cl = {"retentionDays": 90, "pageWindowDays": 14, "runs": [], "entries": []}
    seen = {(e.get("seen"), e.get("tab"), e.get("kind"), e.get("id"), e.get("field"))
            for e in cl.get("entries") or []}
    new = []
    def clean(x):
        """Rejestr trzyma ZNAKI, nie encje. Encja w danych wraca potem w kazdym
        widoku, ktory je czyta — na stronie, w panelu i w `+` wiersza historii."""
        if not isinstance(x, str): return x
        for a, b in (("&mdash;", "\u2014"), ("&rarr;", "\u2192"), ("&minus;", "\u2212"),
                     ("&middot;", "\u00b7"), ("&amp;", "&")):
            x = x.replace(a, b)
        return x

    def put(tab, kind_, iid, field, before, after, it=None):
        iid, field, before, after = clean(iid), clean(field), clean(before), clean(after)
        k = (today, tab, kind_, iid, field)
        if k in seen: return
        seen.add(k)
        it = it or {}
        new.append({"seen": today, "tab": tab, "kind": kind_, "id": iid, "field": field,
                    "before": before or None, "after": after or None,
                    "product": norm(it.get("product")) or None,
                    "weight": it.get("socWeight"), "tier0": bool(it.get("tier0Touch")),
                    "msDate": norm(it.get("published")) or norm(it.get("changed")) or None,
                    "url": norm(it.get("url")) or None})
    added, removed, changed, _, _ = diff_items(prev_st, curr_st)
    for i in added:   put(tab_of(i), "added", i.get("id"), None, None, None, i)
    for i in removed: put(tab_of(i), "removed", i.get("id"), None, None, None, i)
    for i, deltas in changed:
        for lab, a, b in deltas: put(tab_of(i), "changed", i.get("id"), lab, a, b, i)
    pc, cc = prev_cat or {}, curr_cat or {}
    for which, tab in (("graph", "Graph API"), ("roles", "Roles")):
        a, r, m, _, _ = diff_catalog(pc, cc, which)
        for n in a: put(tab, "added", n, None, None, None)
        for n in r: put(tab, "removed", n, None, None, None)
        for n, f, o, v in m: put(tab, "changed", n, f, o, v)
    # Ruch endpointow dopisujemy PER UPRAWNIENIE. Jeden wpis na endpoint dawal
    # 9 736 wierszy pierwszego dnia z mapa (zmierzone 7 wrzesnia 2026) i rejestr
    # przestawal byc czytelny; liczba plus trzy przyklady odpowiadaja na to samo
    # pytanie, a panel uprawnienia i tak wymienia wszystkie endpointy.
    agg = {}
    for nm, what, before, after in diff_graphmap(prev_st, curr_st)[0]:
        if what in ("endpoint added", "endpoint removed"):
            a = agg.setdefault((nm, what), {"n": 0, "ex": []})
            a["n"] += 1
            if len(a["ex"]) < 3: a["ex"].append(after or before)
        else:
            put("Graph API", "changed", nm, what, before, after)
    for (nm, what), a in sorted(agg.items()):
        sign = "+" if what == "endpoint added" else "\u2212"
        e = {"seen": today, "tab": "Graph API", "kind": "changed", "id": nm,
             "field": "endpoints", "before": None, "after": "%s%d" % (sign, a["n"]),
             "detail": "%s: %s%s" % (what, ", ".join(a["ex"]),
                                     ", \u2026" if a["n"] > len(a["ex"]) else ""),
             "product": None, "weight": None, "tier0": False, "msDate": None, "url": None}
        k = (today, e["tab"], e["kind"], e["id"], e["field"])
        if k not in seen:
            seen.add(k); new.append(e)
    cl["entries"] = (cl.get("entries") or []) + new
    keep = datetime.date.today() - datetime.timedelta(days=cl.get("retentionDays", 90))
    cl["entries"] = [e for e in cl["entries"] if (e.get("seen") or "9999") >= keep.isoformat()]
    cl["runs"] = [r for r in (cl.get("runs") or []) if not (r.get("date") == today and r.get("kind") == kind)]
    cl["runs"].append({"date": today, "kind": kind, "at": when, "entries": len(new)})
    cl["runs"] = sorted(cl["runs"], key=lambda r: (r.get("date"), r.get("at") or ""))[-200:]
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    json.dump(cl, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    return len(new), len(cl["entries"])

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = sys.argv[1:]
    home = opts[opts.index("--home") + 1] if "--home" in opts else "/"
    label = opts[opts.index("--label") + 1] if "--label" in opts else "morning pass → afternoon pass"
    if len(args) < 3:
        raise SystemExit("uzycie: make_diff.py <poprzedni> <biezacy> <wyjscie.html> [--home /] [--label ...] [--ledger site/data/changelog.json]")
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
    if "--ledger" in opts:
        lp = opts[opts.index("--ledger") + 1]
        n, tot = ledger(lp, ps, pc, cs, cc, when,
                        "diff" if "--home" in opts and home == "/" else "morning")
        print("OK  %s  +%d wpisow, razem %d" % (lp, n, tot))
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

Trackery pokazuja „Privilege level — Level 2 · Moderate", „Roles that support this permission"
i „Request samples". **Ta sekcja twierdzila do 6 wrzesnia 2026, ze Microsoft nie publikuje ZADNEGO
z tych trzech. Dwa z tych trzech twierdzen byly falszywe** — i to jest dokladnie ten sam blad co
falszywy negatyw z sekcji 5 (`UserAuthMethod-*.Delete.All` odrzucone jako „zmyslone", bo nie bylo
ich na Learn). Nie ma ich w `permissions-reference`, ale sa w `permissions/new/permissions.json`
w repo `microsoftgraph/microsoft-graph-devx-content`, ktore i tak klonujemy (§5d).

Zmierzone 6 wrzesnia 2026 na klonie `ec959bb` z 4 wrzesnia — 923 uprawnienia:

| co tracker pokazuje | czy Microsoft to publikuje | gdzie |
|---|---|---|
| **Privilege level 1-4** | **TAK** — `schemes[<typ>].privilegeLevel` na **903 z 923** uprawnien; rozklad per schemat: 8 razy 1, 236 razy 2, 1 132 razy 3, 84 razy 4 | `permissions.json` |
| **Request samples** (co uprawnienie moze wywolac) | **TAK** — `pathSets[]` z `methods`, `paths` i `schemeKeys`; **24 180 par metoda-sciezka** na **7 430** roznych sciezkach | `permissions.json` |
| **Roles that support this permission** | **NIE** — pole roli nie istnieje nigdzie w tym pliku | — |

Trzeci wiersz jest jedynym prawdziwym brakiem i zostaje w `notPublished`. Sprawdzone tego dnia
takze po drugiej stronie: **139 plikow rol w `MicrosoftDocs/entra-docs` nie wymienia ani jednego
uprawnienia Graph**, a dokumentacja API Graph nazywa role na **104 z 11 937 stron (0,9%)**.

```json
"notPublished":{"graph":[["Roles that support this permission",
  "Microsoft publishes no permission-to-role mapping: no role field in permissions.json, no Graph permission named in any of the 139 Entra role files, and a role named on 104 of 11 937 API reference pages. This brief derives a candidate list and says so; see the rule printed in the tab."]]}
```

**Privilege level i lista endpointow przestaja wiec byc „pochodna trackera" — sa danymi Microsoftu
i renderuje sie je jak kazde inne** (§5ah). Nigdy natomiast nie drukuj severity, ktorej Microsoft
nie wydal, obok jego pol — czyta sie ja wtedy jak jego.

**Nauka ogolna, wazniejsza niz same trzy wiersze: „Microsoft tego nie publikuje" jest TWIERDZENIEM
i wymaga daty oraz nazwy sprawdzonego pliku, tak samo jak kazde inne.** Zapisane bez sprawdzenia,
zyje w tym pliku miesiacami i kaze kolejnym przebiegom nie szukac.

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

Render headless at 1500x1000 in light AND dark and assert — every one of these has caught a real regression: no console or page errors; exactly one visible `.tabpanel`; **the two `.navrow` strips carry 10 `.tab` between them** (§5ae wariant B), labels human, neither row overflowing, also at 1280px; **`header.top .hdr-tools` holds the Theme button and a `select.globalfilter` whose first option is `All products`, and every `header.top .counts a.count` is mirrored into a `#tab-overview .stat` tile**; **every panel except Overview and Sources has exactly one `.panelhead`, built by the script, carrying ≥1 `.stat` and ≥1 `figure.chart`**; **every panel that lists a deadline inside 60 days shows a `🔥 under 30 days` or `⚠️ 30–60 days` chip — absent means the rows lack the emoji**; **`.badge` count across the page is in the hundreds, not the tens**; a picks product chip leaves only that product's rows, raises a `.filterbanner`, Clear filter restores them; **`.filterbanner[hidden]` computes to `display:none`, and with a filter active the banner is visible with a non-empty `.fb-msg`**; **`.cat-controls` is `position:sticky` at desktop width and the search input stays in the viewport after scrolling `.cat-split` into view**; both catalogs render a non-zero count and three modes — Microsoft changes / Catalog notes / All — defaulting to the first with no `catalog`/`brief` entry in it; **`.badge.b-undoc` and `.badge.b-elsewhere` both have a non-transparent background and a non-zero `border-radius` in both themes, and each is carried by at least one rendered chip**; **every `input.tbar-search` and `.cat-searchwrap .cat-search` has a non-transparent, non-`--surface` background in both themes; `.cat-changed` scrollHeight may exceed its clientHeight but `.cat-searchrow` is within 480 px of the panel top; `details.foldnote>summary` computes a font-size of at least 14 px; `.card-title` has a non-transparent background and a non-zero border-radius; every open `details.foldnote` body contains a `ul` and no bare `p` over 40 words**; `scrollWidth` never exceeds client width; **open a role with actions: the action table holds exactly as many rows as `actionsFull`, the count line carries the provenance sentence, `.cp-privbtn` filters to privileged-only with `aria-pressed="true"` and toggles back, and `.cp-verify` links a real `entra-docs/blob/main/.../includes/<slug>.md` URL**. Skip this step rather than failing the run if Playwright is missing.

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

Nowe od 7 wrzesnia 2026 wieczorem (§5al), i kazda odpowiada jednemu punktowi wlasciciela z tego dnia:
**kazdy `details.chg14` ma DWA elementy `text.axt`** — jeden z tekstem konczacym sie na `per day`,
drugi zaczynajacym sie od `day of month` — a jego `svg` nie ma `preserveAspectRatio="none"`;
**sekcja 14 dni stoi w KAZDEJ zakladce tresciowej bezposrednio po `.panelhead`**, a jej `offsetTop`
wzgledem panelu rozni sie miedzy Roles i Graph API o mniej niz 60 px; **panel roli i panel uprawnienia
maja te same dwie pierwsze sekcje**, w kolejnosci `At a glance`, `What changed … in the last 14 days`;
**klikniecie `+` na TRZECH roznych wierszach historii w kazdej z dwoch zakladek daje trzy `.v13pane`
o ROZNYCH licznikach** (zmierzone: Graph 28 / 85 / 179 endpointow, Roles 1 / 81 / 99 akcji), a w kazdym
klonie `[data-hist]` = 0; **cztery przelaczenia tego samego `+` daja jeden panel** (idempotencja);
**wiersz, ktorego katalog nie ma, pokazuje ZDANIE, nie pusty box**; **`Exact match` w Roles zwezasa
liste regula w arkuszu, a nie atrybutem** — `administrator` 96 wpisow i 0 z zaznaczonym Exact match,
`User Administrator` 2 → 1; **akcja katalogowa daje note z przyciskami nazywajacymi role**, a klikniecie
przycisku otwiera panel i przywraca pelna liste; **kotwice `#graph:perm=…` i `#roles:role=…` zaznaczaja
wpis** po zaladowaniu i przy `hashchange`.

Nowe od 7 wrzesnia 2026 (§5ak), i to one lapia blad, ktory bramka przepuscila: **klikniecie TRZECH
roznych uprawnien w katalogu Graph daje za kazdym razem `details.epsinject` w `.cat-detail-inner`,
a liczby endpointow w podpisach sa ROZNE** (zmierzone: 2, 1, 14, 5); **pasek chipow zmienia liczbe
widocznych wierszy** (14 -> GET 5 -> Least privilege 12); **uprawnienie bez pasujacej roli pokazuje
ZDANIE, nie pusta tabele**; po czterech przelaczeniach tam i z powrotem `.epsinject` i `.rolesinject`
wystepuja po RAZ jeden (idempotencja).

Nowe od 3 wrzesnia 2026, oba ze zgloszenia wlasciciela z tego dnia: **kliknieciecie kafelka
`Added` / `Removed or breaking` / `Modified` w kazdym katalogu zostawia na liscie pod polem szukania
wylacznie wpisy tego kubelka** (`.cat-item:not([hidden])` rowna sie liczbie z kafelka albo zero
z bannerem mowiacym, ze kubelek jest pusty), kafelek dostaje `aria-pressed="true"`, ponowne
klikniecie przywraca pelna liste, a wpisanie czegokolwiek w pole szukania czysci filtr kubelka;
**tabela `.cc-table` ma kolumne `Change` z chipem `.badge` w kazdym wierszu** (§5ad).
I kolor paska (§5ae): **`getComputedStyle(nav.anchors).backgroundColor` jest nieprzezroczyste,
IDENTYCZNE w obu motywach i rozne od tla `header.top` oraz od `--surface`**; kazda `nav.anchors .tab`
ma niezerowa `borderTopWidth` i `borderTopColor` rozny od wlasnego tla; zakladka z
`aria-selected="true"` ma tlo rozne od nieaktywnych; licznik `.navcount` ma nieprzezroczyste tlo
w obu motywach — te same wartosci, nie tylko „jakies".

Dodatkowo przy **390x844** (telefon): **dla KAZDEJ z DZIESIECIU zakladek po kolei `document.documentElement.scrollWidth === clientWidth`**
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
a kontrakt mowil wtedy o dziewieciu panelach. **Od 6 wrzesnia 2026 panele sa dwa razy piec i pasek ma dwa rzedy (§5ae), wiec ten argument nie blokuje juz nowej zakladki** — blokuje natomiast dokladanie zakladki, ktora nie ma wlasnego domu w diffie (§3a). `docchanges` zostaje sekcja panelu `tab-new`.

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
konsoli w obu motywach. **Asercja Playwright: dla KAZDEJ z DZIESIECIU zakladek przy 390x844
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

## 5ae. Pasek zakladek ma WLASNY kolor — grafit z ramka na kazdej zakladce

Wlasciciel zglosil 3 wrzesnia 2026: *„pasek z zakladkami prawie ginie w gaszczu tych naszych
informacji"*, a po pierwszej probie: *„niech sie zakladki odrozniaja, maja jakas ramke, bo teraz
wszystko sie zlewa"*.

Przyczyna jest mierzalna, nie gustowa. Zmierzone tego dnia na `site/index.html`: `nav.anchors` nie
ma wlasnego tla (`rgba(0,0,0,0)`), a kazda `.tab` stoi na `--surface`, czyli **na tym samym kolorze,
co siedem pigulek nad nia i cala tresc pod nia**. Trzy warstwy tego samego bialego prostokata jedna
pod druga: pasek nie jest wtedy elementem nawigacji, tylko trzecim rzedem kafelkow.

### Regula

Pasek dostaje **wlasna plaszczyzne, ktorej nie ma zadna inna czesc strony**, i jest ona **identyczna
w obu motywach**. To jest cel, a nie niedopatrzenie: pasek ma byc punktem odniesienia, ktory nie
zmienia sie razem z motywem. Dlatego szesc grafitowych wartosci wchodzi jako **osobne zmienne
`--nav-*` deklarowane raz na `:root`** i nieprzedefiniowane w bloku ciemnym — **to jedyny w arkuszu
wyjatek od §5t** („nie wymyslaj nazw zmiennych") i ma powod: grafit jest celowo poza paleta motywu,
bo pigulki uzywaja czerwieni, niebieskiego i szarosci powierzchni, a pasek musi byc plaszczyzna,
ktorej zaden licznik nie ma.

**Kazda zakladka ma ramke.** Bez niej dziewiec etykiet na jednolitym grafitze zlewa sie dokladnie
tak, jak zglosil wlasciciel — plaszczyzna sama nie wystarcza, bo rozdziela pasek od strony, ale nie
zakladki od siebie. Aktywna jest biala z bialym pierscieniem, wiec czytelnik widzi ja katem oka.

Blok idzie na koniec `<style>`, razem z §1a, §5e, §5k, §5t, §5w, §5x, §5y i §5ad — to sa JEDYNE
dozwolone dopisane reguly CSS.

```css
/* §5ae — pasek zakladek ma WLASNY kolor, staly w obu motywach. */
:root{--nav-bg:#2b3140;--nav-line:#3d4557;--nav-tab:#323949;--nav-tab-line:#6d7891;
 --nav-fg:#cfd5e2;--nav-hover:#3e4759;--nav-hover-line:#8b95ab;--nav-on:#1b2030;--nav-rowlab:#98a2b8}
/* WARIANT B (6 wrzesnia 2026): plaszczyzna przenosi sie na .navstack, bo pasek ma teraz DWA
   opisane rzedy. `nav.anchors` samo w sobie jest odtad przezroczyste — asercja §5h celuje
   w .navstack, nie w nav.anchors. To jedyna zmiana asercji, ktora ten wariant kosztuje. */
.navstack{background:var(--nav-bg);border:1px solid var(--nav-line);border-radius:12px;
 padding:8px 10px;display:grid;gap:8px}
.navstack nav.anchors{background:none;border:0;border-radius:0;padding:0;margin:0;
 flex-wrap:wrap;overflow-x:visible;row-gap:8px;align-items:center;gap:10px}
.navrow{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.navrow+.navrow{padding-top:8px;border-top:1px solid var(--nav-line)}
.navrow .rowlab{flex:0 0 auto;font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
 font-weight:700;color:var(--nav-rowlab);min-width:74px}
nav.anchors .tab{background:var(--nav-tab);border:1.5px solid var(--nav-tab-line);border-radius:9px;
 color:var(--nav-fg);padding:8px 13px}
nav.anchors .tab:hover{background:var(--nav-hover);border-color:var(--nav-hover-line);color:#fff}
nav.anchors .tab[aria-selected="true"]{background:#fff;border-color:#fff;color:var(--nav-on);
 font-weight:700;box-shadow:0 0 0 3px rgba(255,255,255,.16)}
.navrow.ref .tab{background:transparent;border-color:#4b5568;color:#aab3c6;font-weight:600}
.navrow.ref .tab:hover{background:var(--nav-hover);border-color:var(--nav-hover-line);color:#fff}
nav.anchors .tab .navcount{background:rgba(255,255,255,.18);color:#e6eaf2}
nav.anchors .tab:hover .navcount{background:rgba(255,255,255,.26);color:#fff}
nav.anchors .tab[aria-selected="true"] .navcount{background:var(--nav-bg);color:#fff}
@media (max-width:760px){
  /* zawiniecie dwunastu zakladek kosztuje na telefonie SIEDEM rzedow i 295-358 px ekranu —
     zmierzone 6 wrzesnia 2026 na wszystkich czterech wariantach. Dlatego na telefonie kazdy
     rzad wraca do JEDNEGO paska przewijanego w poziomie. */
  .navstack{gap:7px;padding:7px 8px}
  .navrow{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .navrow .rowlab{min-width:0}
  .navstack nav.anchors{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch}
  nav.anchors .tab{flex:0 0 auto;padding:8px 12px}
}
```

`--nav-*` sa deklarowane, wiec §5t jest spelnione co do litery: **zadna regula nie uzywa zmiennej,
ktorej arkusz nie zna**. Surowy `#fff` przy zakladce aktywnej i `rgba(255,255,255,.18)` przy liczniku
sa swiadome — maja byc biale takze w motywie jasnym, gdzie `--surface` jest bialy i pierscien by zginal.

**Licznik przy nazwie zakladki nazywa sie `.navcount`, nie `.tabn`.** Pierwsza wersja tego bloku
celowala w `.tabn` i **byla cicha**: klasy o tej nazwie nie ma w powloce ani razu, wiec obie reguly
nie robily nic, a licznik zostawal przy regulach powloki — `color:var(--faint)` na grafitze i
`background:var(--on-accent)`, ktore w motywie jasnym jest biale, a w ciemnym prawie czarne. Pasek
mial wiec wygladac tak samo w obu motywach i **wlasnie w liczniku wygladal inaczej**. Regula CSS
celujaca w nieistniejaca klase nie zglasza bledu — to ta sama choroba co skrypty z sekcji LAYOUT.
Selektor sprawdzasz w `<style>` powloki, zanim go napiszesz.

### Zmierzone 3 wrzesnia 2026 (render headless na kopii zywej strony)

| | motyw ciemny | motyw jasny |
|---|---|---|
| tlo paska | `rgb(43,49,64)` | `rgb(43,49,64)` |
| tlo zakladki | `rgb(50,57,73)` | `rgb(50,57,73)` |
| ramka zakladki | `rgb(109,120,145)` | `rgb(109,120,145)` |
| zakladka aktywna | `rgb(255,255,255)` na `rgb(27,32,48)` | identycznie |
| licznik nieaktywny | `rgba(255,255,255,.18)` / `rgb(230,234,242)` | identycznie |
| licznik aktywny | `rgb(43,49,64)` / `rgb(255,255,255)` | identycznie |
| tlo `header.top` | `rgb(22,27,34)` | `rgb(255,255,255)` — pasek rozni sie od naglowka w OBU |
| zakladek | 9 | 9 |
| bledy strony | 0 | 0 |

Telefon 390x844, wszystkie dziewiec zakladek po kolei: `scrollWidth === clientWidth === 390`,
czyli §5x nie jest zlamane.

### Dwa opisane rzedy — wariant B, przyjety 6 wrzesnia 2026

Dziesiata zakladka (§5ag) nie miesci sie w jednym pasku i **nie jest to kwestia gustu, tylko pomiaru**.
Zmierzone na zywej stronie: dziewiec zakladek zajmuje **1238 z 1238 px przy szerokosci 1280** — pasek
jest dokladnie pelny, wiec dziesiata juz przewija sie w bok. Skrocenie etykiet nie ratuje: „Hunting",
„Graph", „Lifecycle" daja 1261 px przy tych samych 1238 dostepnych.

Pasek ma wiec **dwa opisane rzedy w jednej grafitowej ramce**:

| rzad | etykieta | zakladki |
|---|---|---|
| gorny | `Daily` | Overview · Today · New · Deadlines · Products · Hunting & actions |
| dolny | `Reference` | Component versions · Roles · Graph API · Sources |

Podzial nie jest wymyslony na potrzeby paska. **§5y stawia go w danych**: „zakladki katalogowe licza
katalog, nie okno". Rzedy nazywaja rozroznienie, ktore prezentacja i tak robi, a zakladki referencyjne
sa ciszej (sama obwodka, bez wypelnienia), zeby oko trafialo najpierw w rzad dzienny.

Markup: `<div class="navstack"><div class="navrow daily"><span class="rowlab">Daily</span><nav
class="anchors"></nav></div><div class="navrow ref"><span class="rowlab">Reference</span><nav
class="anchors"></nav></div></div>`. **Powloka buduje zakladki do PIERWSZEGO pustego `nav.anchors`**,
wiec drugi rzad wypelnia skrypt 4 przenoszac do niego zakladki referencyjne po `buildTabs()`.
Bez tego przeniesienia wszystkie dziesiec zostaje w gornym rzedzie i wariant B nie rozni sie od A.

Zmierzone na czterech wariantach, oba motywy, 24 rendery: **desktop dwa rzedy, 101 px wysokosci przy
1500 i przy 1280; telefon dwa rzedy po 101 px, kazdy przewijany osobno; zero bledow konsoli;
`scrollWidth === clientWidth` w kazdej komorce.** Bez reguly telefonowej wszystkie cztery warianty
zawijaly sie do **siedmiu rzedow i 295-358 px** — gorzej niz dzisiejsze przewijanie w bok.

### Asercje Playwright (dochodza do §5h)

**Uwaga na przeniesiona asercje.** Wariant B przenosi plaszczyzne z `nav.anchors` na `.navstack`,
wiec `getComputedStyle(nav.anchors).backgroundColor` zwraca odtad `rgba(0,0,0,0)`. Asercja, ktora
tego nie uwzglednia, **zapala sie na poprawnej stronie** — a to jest ten sam blad co asercja
przechodzaca na pustych danych (§0b). Dlatego:

- `getComputedStyle(document.querySelector(".navstack")).backgroundColor` **nie jest przezroczyste
  i jest TAKIE SAMO w obu motywach**;
- **sa DWA elementy `.navrow`**, gorny ma etykiete `Daily`, dolny `Reference`, i kazdy niesie
  `<nav class="anchors">` z co najmniej jedna zakladka;
- suma zakladek w obu rzedach wynosi **10**, a `Component versions` stoi w rzedzie `Reference`;
- kazda `nav.anchors .tab` ma `borderTopWidth` niezerowa i `borderTopColor` rozny od tla zakladki;
- zakladka z `aria-selected="true"` ma tlo rozne od zakladek nieaktywnych;
- tlo `.navstack` jest rozne od tla `header.top` i od `--surface`;
- przy 390x844 **kazdy `.navrow` ma `scrollWidth > clientWidth`** (przewija sie sam) a dokument
  NIE — `document.documentElement.scrollWidth === clientWidth`.

## 5af. Punkt listy ma JEDEN temat — ksztalt punktu z zakladki Products jest wzorcem dla calej strony

Wlasciciel zglosil 5 wrzesnia 2026, pokazujac dwa zrzuty obok siebie: *„zakladka Today — kompletnie
nieczytelne, trudno cos znalezc, wychwycic. Zakladka Products — tu dane sa usystematyzowane, ladnie
poukladane. Czy mozesz w Today rowniez tak przedstawic te dane i upewnic sie, ze jesli w innych
zakladkach cos podajesz w bullet points, to zrobisz to tak samo jak w Products?"*

Roznica jest mierzalna, nie estetyczna. Zmierzone tego dnia na `site/index.html` — **98 punktow
`<li>` w calej tresci**, liczonych `html.parser`, nie wyrazeniem regularnym (§0a: komentarz
SHELL CONTRACT ma wczesny `-->`, wiec niezachlanne wycinanie komentarzy zjada kawal dokumentu
i daje 0 punktow zamiast 98):

| | zakladka Products (`#exec`) | zakladka Today (`sec-note` sekcji `top5`) |
|---|---|---|
| punktow | 60 | 4 |
| zaczyna sie od `<b>` | **60 z 60** | 0 z 4 |
| konczy sie linkiem | **60 z 60** | 0 z 4 |
| tematow w JEDNYM punkcie | 1 | **9** |
| `<b>` w jednym punkcie | 1 | **9** |
| srednikow w jednym punkcie | 0 | **8** |
| slow w tym punkcie | mediana 42 | **113** |

Czwarty punkt Today upycha **dziewiec pozycji tier 0 w jeden akapit** rozdzielony srednikami —
`MC1456735`, `MC1458947`, `eds-samaccountname-onpremises`, `entra-cloudsync-provision-to-ad`,
`entra-connect-2-5-79-0-end-of-support`, `entra-security-admin-identity-response`,
`exchange-hybrid-les-writeback`, `gsa-tls-inspection-managed-certificate`,
`reference-connect-version-history` — i **ani jednego linku do zrodla**. To sa dokladnie te pozycje,
ktore §5p kaze NAZWAC z `id`, gdy nie dostaly karty. Zostaly nazwane i jednoczesnie sa nie do
przeczytania.

**To nie jest nowa regula, tylko regula, ktorej nikt nie mierzyl.** §5k mowi od 31 sierpnia:
„tresc pod `+` jest lista punktowana, nigdy proza — jeden fakt na punkt". Punkt z dziewiecioma
`<b>` jest proza w przebraniu punktu. Regula bez asercji jest sugestia (§0b) — i tak samo tu.

### Ksztalt punktu — jeden, dla KAZDEGO `<li>` na stronie

```html
<li><b>Naglowek nazywajacy JEDNA rzecz</b> &mdash; zdanie albo dwa, co to jest i co z tego wynika. <a href="https://…">Source</a></li>
```

1. **Jeden temat na punkt.** Lista dziewieciu pozycji to DZIEWIEC punktow, nigdy jeden punkt
   z dziewiecioma `<b>`. Kazdy dostaje wlasny naglowek i wlasny link.
2. **Punkt otwiera `<b>`**, po nim `&mdash;`, po nim wyjasnienie. Tak wygladaja wszystkie 60
   punktow, ktore wlasciciel wskazal jako czytelne.
3. **Punkt konczy sie swoim linkiem.** To jest regula 1 obu promptow („SOURCE LINK ON EVERY CLAIM"),
   i punkt bez linku lamie ja tak samo jak wiersz tabeli bez kolumny `Source`. Pozycja, ktora
   naprawde nie ma URL-a, dostaje `<span class="lnk-dead">` albo doslowne `no MC/RM post — Learn
   only` (§5n) — nigdy puste miejsce.
4. **Dlugosc NIE jest kryterium.** Punkt o 123 slowach opisujacy JEDNA rzecz jest poprawny —
   taki jest na stronie i wlasciciel wskazal go jako dobry. Punkt o 113 slowach opisujacy DZIEWIEC
   rzeczy jest bledem. Liczy sie liczba tematow, nie liczba slow.
5. **Siedem punktow to sufit dla listy NARRACYJNEJ** (§5k) — dla wyliczenia nazwanych pozycji sufitu
   nie ma, bo kazda pozycja musi byc widoczna. Wyliczenie idzie wtedy do wlasnej, zagniezdzonej
   `<ul>` pod punktem, ktory je zapowiada.

### Gdzie to obowiazuje

Wszedzie, gdzie strona uzywa `<li>`: `sec-note` sekcji `top5`, exec summary, `details.foldnote`,
strategic watchlist, Sources. **Jedna strona, jeden ksztalt punktu** — czytelnik nie ma sie uczyc
dwoch konwencji, przechodzac miedzy zakladkami.

Walidator (pozycja 36 listy §0, liczona przez bramke §0b): **zaden `<li>` nie ma naraz co najmniej
dwoch `<b>` i co najmniej trzech srednikow.** Zmierzone na stronie z 5 wrzesnia: ten warunek lapie
**dokladnie jeden** punkt — ten z Today — i **nie lapie** punktu z Sources, ktory ma dwa `<b>`, zero
srednikow i 49 slow, bo tamten opisuje jedna rzecz i jest poprawny. Asercja, ktora lapie oba, byla by
tak samo bezuzyteczna jak asercja, ktora nie lapie zadnego.

**Reguly 3 (link w kazdym punkcie) bramka NIE sprawdza kodem, i to jest swiadome.** Pierwsza wersja
tej pozycji zadala linku od kazdego punktu z `<b>` i zmierzone tego dnia zapalila sie na
**jedenastu** punktach, z ktorych zaden nie byl bledem: to punkty `sec-note` objasniajace, co znaczy
kolumna `Reference` albo czym roznia sie rodziny `Change type`. One nie stawiaja tezy o Microsofcie,
wiec nie maja czego cytowac. **Asercja, ktora zapala sie na poprawnej stronie, uczy przebieg, ze
czerwone nic nie znaczy** — dokladnie tak samo jak asercja przechodzaca na pustych danych (§0b).
Link w punkcie NIOSACYM TEZE zostaje regula redakcyjna, sprawdzana okiem przy pozycji 21.

## 5ag. Zakladka Component versions — wersje komponentow i TRESC kazdego wydania

Wlasciciel poprosil 6 wrzesnia 2026 o zbieranie wersji komponentow bezpieczenstwa: Authenticator na
iOS i Androida, sensory MDI i MDE, GSA, Entra Connect, najnowsze systemy Apple, wersja poprzednia
i koniec wsparcia. Po trzech iteracjach widoku (v1-v4, wszystkie zmierzone) reguly ponizej sa tym,
co z tego zostalo. **Numer wersji sam w sobie nikomu nie mowi, czy trzeba dzialac** — dlatego ta
zakladka nie jest tabela numerow, tylko numerem plus trescia wydania.

Panel `tab-components`, sekcja `<section id="components" data-nav="Component versions">`, rzad
`Reference` paska (§5ae).

### Kontrakt danych — `components` w bloku `soc-brief-state`

```json
"components":[{
  "id":"entra-connect-sync",
  "name":"Entra Connect Sync",
  "scope":"Directory synchronization service",
  "versions":[{"platform":"windows-server","version":"2.6.84.0","released":"2026-07-07",
               "releaseLabel":"Released 7 July 2026"}],
  "provenance":"vendor",
  "state":"baseline",
  "deadline":"2026-09-30",
  "deadlineNote":"Synchronization stops on any server below 2.5.79.0.",
  "releases":[{"version":"2.6.84.0","date":"Released 7 July 2026","current":true,
    "groups":[{"title":"Added","items":[
      {"text":"<doslownie z release notes>","url":"…","label":"Passwordless setup"}]}]}],
  "sources":[{"url":"…","label":"Entra Connect version history"}],
  "checkedOn":"2026-09-06"
}]
```

- **`platform`** jest slownikiem ZAMKNIETYM: `windows`, `windows-server`, `macos`, `ios`, `ipados`,
  `android`, `cross`, `apple`. Kolor chipa bierze sie z tej wartosci i jest **ten sam na calej
  stronie** — takze w tabelach. Wartosc spoza listy = przebieg NIEUDANY.
- **`provenance`**: `vendor` | `mirror` | `blog`. Nigdy nie mieszasz ich w jednym polu — komponent
  o dwoch platformach i dwoch pochodzeniach niesie obie wartosci, jak Authenticator.
- **`state`**: `baseline` | `no-change` | `new-version` | `backfilled` | `corrected`. `baseline`
  jest poprawne WYLACZNIE w przebiegu, ktory nie ma z czym porownac. Przebieg z wczorajszym
  `site/data/*.json` i stanem `baseline` na wszystkich komponentach jest przebiegiem NIEUDANYM:
  to znaczy, ze porownania nie zrobil.
- **`releases[].items[].text` jest DOSLOWNY** z release notes wydawcy, w JEGO kolejnosci i w JEGO
  grupach (`Added` / `Changed` / `Fixed`, `Functional changes` / `Other changes`). Nie streszczasz,
  nie laczysz dwoch punktow w jeden i nie zmieniasz kolejnosci wewnatrz grupy.

### Reguła wyboru — bo „wybralem te trzy" nie jest regula

Pierwsza wersja tej zakladki pisala pod lista *„Three of the nine listed fixes are shown."* i nie
mowila, na jakiej podstawie. Wlasciciel zapytal wprost i mial racje: **wybor bez kryterium jest
sugestia, a sugestii nie da sie sprawdzic** — to ten sam mechanizm co regula bez asercji (§0b).

**Nic nie jest wycinane.** Kazdy punkt, ktory wydawca opublikowal, jest na stronie. Zmienia sie
wylacznie kolejnosc: punkt idzie na przod i dostaje etykiete, gdy jego tekst pasuje do jednej
z osmiu kategorii ponizej. Reszta zostaje w kolejnosci wydawcy pod `<details class="rest">`
z podpisem **`Show the remaining N of M`** — licznik zawsze widoczny.

```python
RULES = [
 ("credentials & sign-in", r"passkey|fido2|authentication|sign[- ]?in\b|sign[- ]?out\b|credential|"
                           r"certificate|\btpm\b|\bmsal\b|password"),
 ("audit & logging",       r"\baudit|event log|windows event|traffic log|log collection|"
                           r"event tracing|\betw\b|event collection"),
 ("privilege & directory", r"administrator|\badmin\b|privilege|\brole\b|directory synchronization|"
                           r"active directory|domain controller|\bad cs\b|\bad fs\b|cross-tenant|tenant id"),
 ("detection & visibility",r"\bdetect|discover|visibilit|hunting"),
 ("data protection",       r"\bdlp\b|data loss|classification"),
 ("control changed",       r"no longer|removed|remove[sd]?\b|disabled|self-healing|falls back|"
                           r"silently|by default"),
 ("lifecycle",             r"migration|generally available|end of support|retire|deprecat"),
 ("vulnerability",         r"vulnerabilit|\bcve\b"),
]
def classify(text):
    t = text.lower()
    return [name for name, pat in RULES if re.search(pat, t)]
```

Trzy rzeczy sa w tej regule wiazace i kazda ma powod:

1. **Etykieta na punkcie nazywa kategorie, ktora go zlapala.** Czytelnik sprawdza wybor punkt po
   punkcie, zamiast brac go na wiare. To jest cala odpowiedz na pytanie „na jakiej podstawie".
2. **Regula jest wypisana na stronie w `<div class="rulebox">`**, tym samym tekstem co w kodzie.
   Regula stosowana, ale nieopublikowana, jest z punktu widzenia czytelnika gustem.
3. **Grupa, w ktorej NIC nie pasuje, pokazuje wszystko od razu** i mowi jednym zdaniem dlaczego.
   Pierwsza wersja dawala tam `Show the remaining 1 of 1`, co jest absurdem, i `6 of 6`, co jest
   zwykla lista schowana bez powodu.

Zmierzone 6 wrzesnia 2026 na piu komponentach: **67 punktow zrodlowych, 38 wypromowanych (57%),
21 pod rozwijaniem, 8 w grupach bez dopasowania — razem 67.** To, co zostaje niewypromowane, to
wersje .NET Runtime, accessibility, telemetria, kolejnosc kanalow w UI i „miscellaneous fixes".
**Regula promujaca 90% jest bezuzyteczna tak samo jak promujaca 5%** — pierwsza nie wybiera,
druga chowa tresc. Gdy pomiar wyjdzie poza pasmo 30-70%, poprawiasz regule i zapisujesz nowy pomiar.

### MDE ma TRZY strumienie wersji i nigdy nie zwijasz ich w jeden

Wlasciciel zglosil to wprost: przy jednej wartosci nie wiadomo, czy to sensor, silnik, czy
sygnatury. Strona pokazuje cztery wiersze, bo cztery odpowiadaja na rozne pytania:

| strumien | zmierzone 6 wrzesnia 2026 | co to jest |
|---|---|---|
| Platform | `4.18.26080.3` | binarka klienta antywirusa |
| Engine | `1.1.26080.3` | silnik skanujacy |
| Security intelligence, **wysylana z wydaniem** | `1.159.11.0` | zestaw definicji z sierpniowej platformy |
| Security intelligence, **zywa** | `1.459.66.0`, 5 wrzesnia 18:59:01 | to, co endpoint faktycznie pobiera |

**Dwie ostatnie sie nie zgadzaja i obie sie publikuje.** Lipcowe wydanie podaje `1.457.11.0`, czyli
WIECEJ niz sierpniowe `1.159.11.0`. Planuje sie wzgledem zywego feedu, a strona mowi to zdaniem —
§8 N wymaga podania obu wartosci tam, gdzie Microsoft publikuje sprzeczne.

Serwisowanie: *„After a new package version is released, support for the previous two versions is
reduced to technical upgrade support only"* — model N−2, cytowany doslownie.

Lista wykrytych zagrozen z kazdej definicji **jest linkowana, nigdy przepisywana**: to setki
pozycji dziennie i zasypalyby zakladke. Link do `wdsi/definitions/antimalware-definition-release-notes`
wystarczy.

### Zrodla — kazde sprawdzone, wynik negatywny tez zapisany

Pelna tabela z werdyktem per adres jest w §7 („Wersje komponentow — co da sie zrodlowac, a czego
NIE"). Tu tylko to, co rozstrzyga codzienny przebieg:

- **Authenticator iOS** — `itunes.apple.com/lookup?id=983156458`, oficjalne API Apple, `version`
  i `currentVersionReleaseDate` z sekundami. **Nie uzywasz strony App Store do daty** — ona podaje
  `5d ago`, a data wzgledna nie jest data.
- **Authenticator Android** — Google Play nie wystawia numeru przy odczycie server-side, a Microsoft
  nie publikuje historii wersji tej aplikacji wcale. Numer powstaje przez **zgodnosc co najmniej
  dwoch niezaleznych luster**, data pochodzi WYLACZNIE z `Updated on` Google Play, a wpis jest
  oznaczony `provenance:"mirror"`. Szczegoly i pulapki parsowania: §7.
- **MDE, MDI, GSA, Entra Connect** — strony Learn wymienione w §7, kazda z kotwica na konkretne
  wydanie. Kotwica jest czescia rekordu, nie ozdoba: `#26840` dla Entra Connect,
  `#windows-antivirus--august-2026--…` i `#macos--august-2026--…` dla MDE.
- **Apple** — `support.apple.com/en-us/100100` na wszystkie systemy i Safari,
  `support.apple.com/en-us/109033` na galezie macOS, czyli na „wersje −1". Wiersze niosa
  `platform:"apple"`, zeby nikt nie wzial ich za komunikat Microsoftu.
- **Blog niezalezny** (np. Richard M. Hicks o GSA) wchodzi jako `provenance:"blog"`, we WLASNEJ
  sekcji `Independent commentary`, nigdy wymieszany z punktami wydawcy. 6 wrzesnia dolozyl fakt,
  ktorego release history nie ma: integracja z Windows Update od listopada 2026.

**Pomylka, ktora ta sekcja ma powstrzymac, zdarzyla sie w tym samym dniu:** przebieg zapisal
`101.26071.0005 (wrzesien 2026)` jako najnowszy build MDE na macOS, bo odczyt zlapal sekcje
o Linuksie. Prawidlowa wartosc, po odczycie kotwicy `#macos--august-2026--101260620012`, to
**`101.26062.0012`, release `20.126062.12.0`, sierpien 2026**. Dlatego kazdy build MDE bierze sie
z KOTWICY konkretnego wydania, nie z tabeli zbiorczej i nie z wyszukiwania po nazwie systemu.

### Markup — szyna i panel

Kazdy komponent to jeden `<article class="cmp">`: szyna `<div class="rail">` po lewej i panel
`<div class="pane">` po prawej, rozdzielone od 900 px w gore, zlozone ponizej.

- **Kazda wersja siedzi we wlasnej zaokraglonej ramce `<div class="vbox">`** z chipem platformy nad
  numerem i data pod nim. Komponent o dwoch platformach ma DWIE ramki — `6.8.54 / 6.2608.5658`
  w jednym wierszu nie mowi, co jest czym, i zostalo z tego powodu odrzucone.
- **Chip platformy `<span class="pchip p-…">` niesie kolor** i powtarza sie wszedzie, gdzie ta
  platforma wystepuje, takze w komorkach tabel.
- **Kazde wydanie — biezace I poprzednie — ma te sama strukture**: `<div class="relhead">` z numerem
  i data, potem grupy wydawcy i punkty. **Poprzednie wydania NIE sa proza.** Wersja, ktora zwijala
  siedem punktow GSA w jedno zdanie rozdzielone srednikami, zostala odrzucona z tego samego powodu
  co §5af: sklejone punkty sa nie do przeczytania i nie do przeszukania.
- `<details class="rest">` nigdy nie ma podpisu `N of N`.

### Nawigacja i panel liczb — kontrakt, nie ozdoba

Wlasciciel zglosil 6 wrzesnia 2026, ze do kazdego komponentu trzeba przewijac cala strone recznie.
Nad sekcja komponentow stoi wiec **siatka kafelkow**, a kafelek jest jednoczesnie nawigacja
i podsumowaniem — pasek nawigacji, ktory nic nie mowi, marnuje najlepsze miejsce na stronie.

- Kazdy `article.cmp` niesie `id="cmp-<id komponentu>"` i `scroll-margin-top`, zeby naglowek sekcji
  nie chowal sie pod gorna krawedzia.
- Kafelek to **zwykla kotwica** `<a class="jtile" href="#cmp-…">`, nie `onclick`. Dziala bez
  JavaScriptu, otwiera sie w nowej karcie i zostawia adres w pasku, wiec da sie wyslac komus link
  prosto do jednego komponentu.
- Kafelek niesie: chipy platform, nazwe, **numer wersji z etykieta** (`Platform 4.18.26080.3`), stan
  i date. Komponent o dwoch platformach ma dwie linie, nie sklejone `6.8.54 / 6.2608.5658`.
- **Skrypt tylko podswietla.** `IntersectionObserver` zaznacza kafelek sekcji, ktora jest w polu
  widzenia (`aria-current="true"`). Brak obserwatora nie psuje niczego.
- `scroll-behavior:smooth` **tylko** w `@media (prefers-reduced-motion:no-preference)`.
- Komponent z terminem ma kafelek z czerwona ramka. Zmierzone: jeden na siedem.

**Panel `What this page tracks` opisuje KOMPONENTY, nie mechanike reguly.** Pierwsza wersja podawala
tam „38 z 67 punktow", czyli stronę mówiącą o sobie samej; liczby reguly przeniesione sa do zdania
o regule w lewej kolumnie. Panel podaje cztery liczby, kazda **wyliczona ze stanu**, nigdy wpisana:
komponenty, wersje wraz z liczba platform, wydania z trescia, punkty wydawcow.

**Rozbicia na „tyle poprawek, tyle nowosci" NIE ma i to jest swiadome.** Nazwy grup sa u kazdego
wydawcy inne: Entra Connect ma `Added` / `Changed` / `Fixed`, GSA `Functional changes` /
`Other changes`, MDE nazwy obszarow (`Data Loss Prevention`, `Identity`), a MDI i MDE na macOS nie
maja grup wcale. Jedna liczba „poprawek" wymagalaby wspolnej taksonomii, ktorej ci wydawcy nie maja —
czyli tego samego bledu co „wybralem te trzy poprawki", tylko w skali strony. Strona podaje wiec
liczbe, ktora jest prawdziwa: **ile punktow siedzi w grupie nazwanej `Fixed` przez samego wydawce**,
i mowi wprost, ze pozostali grupuja inaczej. Gdyby to rozbicie bylo potrzebne, droga bez zmyslania
jest jedna: `releases[].groups[].kind` ze slownika `added|changed|fixed|other`, przypisywany przy
odczycie zrodla, z jawna regula mapowania nazwy grupy wydawcy.

**Kolor liczby tez cos znaczy i nie wprowadza nowego odcienia do palety**: `--accent` inwentarz,
`--info` wersje, `--cond` wydania, `--ok` „nic nie wypadlo", `--bad` termin, `--warn` wartosc
z luster, `--grey` zastrzezenie. Wszystkie siedem liczb — cztery statystyki i trzy flagi — stoi
w **jednej kolumnie**, w ramkach o tej samej szerokosci. Wiersz z twardym terminem ma wlasne tlo
i pasek na lewej krawedzi; jest jedynym takim wierszem.

**Pulapka zmierzona przy tej zmianie:** pierwsza wersja dawala temu wierszowi ujemny margines, zeby
tlo siegalo krawedzi panelu. Wygladalo dobrze i **lamalo wlasna regule §5x** — element byl szerszy
od rodzica. Wciecie przeniesione na wszystkie wiersze, kolumna liczb sie zgadza, nic nie wystaje.

### Walidator — pozycje 37, 38 i 39 listy §0

- **37** — kazdy komponent ma `versions[]` z platforma ze slownika, `provenance`, `state`,
  `checkedOn` i co najmniej jedno zrodlo; kazda wersja ma wlasny `vbox` z chipem.
- **38** — **suma punktow wyrenderowanych rowna sie sumie punktow w danych.** To jest asercja,
  przez ktora ta sekcja istnieje: liczba `li.relitem` na stronie musi rownac sie liczbie
  `releases[].groups[].items[]` w bloku stanu. Roznica znaczy, ze przebieg cos wyciol.
- **39** — reguła wyboru jest opublikowana (`div.rulebox`), kazdy wypromowany punkt niesie co
  najmniej jedna etykiete `.rcat`, i odsetek wypromowanych miesci sie w 30-70%.
- **40** — kazdy `a.jtile` ma `href="#cmp-…"` wskazujacy **istniejacy** `article.cmp`; kafelkow jest
  tyle co komponentow; a liczby w `What this page tracks` rownaja sie policzonym ze stanu. Kafelek
  prowadzacy donikad jest gorszy niz brak kafelka, bo obiecuje i nie dowozi.

## 5ah. Zakladka Graph API — co uprawnienie POTRAFI WYWOLAC, i ktora rola to pokrywa

Wlasciciel zglosil 6 wrzesnia 2026 szesc rzeczy naraz, pokazujac obok naszej zakladki strone
`msgraphpermissions.com`: szczegoly rol renderuja sie rozstrzelone albo nachodza na siebie; nie ma
dopasowania doslownego; **nie widac, na jakie GET / POST / PATCH pozwala uprawnienie**; nie widac,
ktore role je maja; wejscie w zakladke od razu wlacza filtr `Microsoft changes` zamiast `All`.
I zdanie, ktore jest tresc tej sekcji: **„najwazniejsze — znajdz to, czego nie umiemy wyswietlic"**.

Odpowiedz nie byla w powloce ani w CSS. **Byla w pliku, ktory klonujemy od 29 sierpnia i z ktorego
czytalismy jedno pole.** `permissions/new/permissions.json` w `microsoftgraph/microsoft-graph-devx-content`
niesie na kazde uprawnienie pelna liste endpointow z metodami, poziom uprawnienia i flage zgody
administratora. §5b twierdzila, ze Microsoft tego nie publikuje — i to twierdzenie bylo falszywe
przez tydzien, bo nikt go nie sprawdzil.

Zmierzone 6 wrzesnia 2026 na klonie `ec959bb` z 4 wrzesnia:

| co | ile |
|---|---|
| uprawnien w pliku | **923** |
| uprawnien z `pathSets` | 879 |
| par metoda-sciezka | **24 099** |
| roznych sciezek | **7 430** |
| par oznaczonych `isLeastPrivilege` | 11 098 |
| rozklad metod | GET 13 832 · POST 5 781 · PATCH 2 187 · DELETE 2 131 · PUT 249 |
| uprawnien z `privilegeLevel` | **903 z 923**; poziomow per schemat: 8 razy 1, 236 razy 2, 1 132 razy 3, 84 razy 4 |
| identyfikatorow uprawnien (GUID) | 1 979 |

Kontrola trafnosci: `User.Read` daje **205 par** — tyle samo, ile tracker nazywa „205 samples".
Cztery endpointy `User.Read` weszly do pliku **14 sierpnia 2026, commitem `3f8f987`** (`git log -S`),
wiec `sourceChanged` dla nich jest data Microsoftu, a nie data naszego odczytu (§5q).

### Kontrakt danych — `graphMap` W BLOKU `soc-brief-state`

**Nie dokladasz trzeciego bloku `<script type="application/json">`.** Bramka lustra (§0a) zada
DOKLADNIE dwoch i trzeci wywraca caly przebieg — sprawdzone. Mapa jest wiec kluczem w istniejacym
bloku stanu.

```json
"graphMap":{
  "commit":"ec959bb (2026-09-04)", "readOn":"2026-09-06",
  "m":["GET","POST","PATCH","DELETE","PUT"],
  "p":["/accessreviews","/accessreviews/{id}", "…7430 sciezek, slownik"],
  "perms":{
    "User.Read":{
      "eps":"0:142-154,156,158-159,164-174;1:3206,3208",
      "least":"0:142-154,164-174",
      "s":{"DelegatedWork":{"l":2,"c":0},"DelegatedPersonal":{"l":2,"c":0}},
      "ids":{"DelegatedWork":"e1fe6dd8-ba31-4d61-89e7-88639da4683d"},
      "new":{"3206":"2026-08-14"},
      "roles":[["Global Administrator",96,1],["User Administrator",90,1],["Global Reader",84,1]]
    }
  }
}
```

- **`eps` i `least` to lancuchy `<indeks metody>:<przedzialy indeksow sciezek>`**, przedzialy
  rozdzielone przecinkiem, grupy metod srednikiem. `142-154` znaczy trzynascie kolejnych sciezek.
- **`s`** — schemat: `l` to `privilegeLevel` 1-4, `c` to `requiresAdminConsent` jako 0/1.
- **`new`** — indeks sciezki na date wejscia do pliku, wyliczona `git log -S` (§5d), **data
  Microsoftu, nie nasza**.
- **`roles`** — wynik derywacji nizej: `[nazwa, pokrycie w procentach, 1 gdy caly zasob]`, najwyzej
  dziesiec pozycji na uprawnienie.

**Kodowanie mierzone, nie wybrane z gustu** — cztery warianty tej samej mapy, ten sam dzien:

| wariant | surowo | gzip |
|---|---|---|
| naiwnie, `{"m":"GET","p":"/users"}` na pare | 1,77 MB | 101 kB |
| slownik sciezek + listy indeksow | 0,67 MB | 83 kB |
| **slownik sciezek + przedzialy indeksow** | **0,60 MB** | **67 kB** |
| tylko `isLeastPrivilege` | 0,58 MB | 86 kB |

Wariant trzeci jest kanoniczny. Ostatni odrzucony nie dla rozmiaru, tylko dlatego, ze **traci
odpowiedz na pytanie „co ta zgoda faktycznie otwiera"** — a to jest cale pytanie SOC.

Koszt calej strony: 5,65 MB / 433 kB gzip przed, **6,32 MB / 537 kB gzip po** (+12% surowo,
+24% gzip). W przegladarce `JSON.parse` 1,6 ms, rozwiniecie jednego uprawnienia 0,8 ms. Budowa:
sparse clone devx 1,9 s, parsowanie 0,02 s, derywacja rol **0,4 s**. Bramka §0b 0,29 → 0,30 s,
lustro §0a 0,59 → 0,47 s, `make_diff.py` 0,03 → 0,04 s.

### Co panel uprawnienia pokazuje, w tej kolejnosci

1. **At a glance** — `objectType`, API, **privilege level per schemat**, **admin consent per
   schemat**, liczba endpointow z rozbiciem na metody, liczba `isLeastPrivilege`, kazdy GUID.
2. **Published by Microsoft** — na schemat: display name i opis, dokladnie jak w pliku.
3. **What this permission can call** — `<details class="eps">`, **domyslnie ZWINIETE**, w podpisie
   liczba endpointow. W srodku pasek filtrow metod (`All 205`, `GET 179`, `POST 18`, `PATCH 4`,
   `DELETE 4`, `Least privilege 163`) i tabela `Method | Endpoint | Privilege | Change`.
4. **Entra roles that can do this** — derywacja z regula wypisana na stronie (nizej).
5. **APIs an app registration can be granted permissions on** — sekcja istniejaca, bez zmian.
6. **What Microsoft changed** — sekcja istniejaca, bez zmian.

**Kolejnosc jest wiazaca. Sekcje 3 i 4 wstawia SKRYPT 6 (§5ak), nie przebieg** — panel buduje
skrypt 3 powloki, ktorego nie wolno edytowac, wiec bez szostego skryptu dane siedza w bloku stanu,
a czytelnik ich nie widzi. Zmierzone 7 wrzesnia 2026: mapa kompletna, bramka 45/46, a lista
endpointow wyrenderowana RAZ, poza panelem. Lista jest zwinieta i stoi NAD dwiema starymi sekcjami,
zeby nie konkurowaly o gore panelu; wlasciciel poprosil o to wprost. Sekcja 3 rozwinieta ma ~7 400 px
wysokosci, zwinieta 44 px — pomiar, bo pierwsza wersja tego bloku **nie zwijala sie wcale** i test
tego nie zlapal, mierzac wysokosc tabeli w srodku (`content-visibility:hidden` zachowuje ostatni
layout potomkow, wiec tabela raportowala 7 236 px takze zwinieta). **Wysokosc mierzy sie na samym
`<details>`.**

### Cztery rodzaje zapytania w JEDNYM polu

Pole rozpoznaje, co wpisano, i **mowi o tym chipem `matched by …`** zamiast udawac, ze wszystko jest
jedna przestrzenia nazw:

| co wpisano | rozpoznanie | wynik |
|---|---|---|
| `e1fe6dd8-ba31-4d61-89e7-88639da4683d` | GUID | uprawnienie o tym `id`, nota „GUID belongs to User.Read" |
| `/drives/{id}/items/{id}/invite` | zaczyna sie od `/` | uprawnienia nadajace ta sciezke; nota nazywa je z imienia |
| `microsoft.directory/users/inviteGuest` | zaczyna sie od `microsoft.` | **akcja katalogowa, nie endpoint Graph** — nota mowi to wprost i wymienia role, ktore ja niosa |
| `User.Read` | reszta | nazwa uprawnienia, z `Exact match` albo bez |

**Nota przy sciezce i przy akcji NAZYWA znalezione uprawnienia, nie tylko je liczy.** Sama liczba
przy pustej liscie kart czyta sie jak porazka, a jest poprawnym wynikiem.

**`Exact match` jest polem wyboru obok szukajki**, nie trybem. Bez niego `User.Read` daje trzy
wyniki, z nim jeden — zmierzone.

**Tryb domyslny to `All`, nie `Microsoft changes`.** Wejscie w zakladke z wlaczonym filtrem zmian
pokazuje ulamek katalogu i wyglada na pusta zakladke; wlasciciel zglosil to jako nieintuicyjne
i ma racje. `Microsoft changes` zostaje jako drugi przycisk.

**Nad polem stoi rzad KLIKALNYCH podpowiedzi** — `name` / `endpoint` / `permission ID` /
`directory action` — kazda wpisuje swoj przyklad i od razu pokazuje wynik. Podpowiedz, ktora trzeba
przeczytac, przegrywa z podpowiedzia, ktora sie klika; a placeholder z czterema mozliwosciami
i tak nie miesci sie na telefonie (zmierzone: obcinany przy 390 px).

### Rola, ktora pokrywa uprawnienie — DERYWACJA, i strona to mowi

To jest odpowiedz na „w jakie role ma zdefiniowane dane uprawnienie". **Zaczyna sie od sprawdzenia,
czy Microsoft to publikuje. Nie publikuje** — zmierzone 6 wrzesnia 2026 w trzech miejscach:

- `permissions.json` niesie `authorizationType`, `ownerInfo`, `pathSets`, `schemes` — **zero pola roli**;
- **139 plikow rol** w `MicrosoftDocs/entra-docs` nie wymienia **ani jednego** uprawnienia Graph;
- dokumentacja API Graph nazywa role na **104 z 11 937 stron (0,9%)**, a akcje `microsoft.directory/…`
  na **33 stronach**.

Lista „Roles that support this permission" u kazdego trackera jest wiec **czyjas derywacja**.
Nasza tez jest — i dlatego **regula jest wydrukowana na stronie**, tak samo jak regula wyboru
punktow w §5ag. Regula bez asercji jest sugestia; regula stosowana, ale nieopublikowana, jest gustem.

```python
VERB={"GET":"read","POST":"create","PATCH":"update","PUT":"update","DELETE":"delete"}
# zasob = pierwszy segment sciezki bez parametru; `/me/...` liczy sie jako `users`
# akcja katalogowa microsoft.directory/<zasob>[/<wlasciwosc>]/<operacja>; `.unified`/`.security` -> baza
# rola POKRYWA endpoint, gdy ma akcje na tym samym zasobie z ta sama operacja albo `allTasks`
# pokrycie = udzial ENDPOINTOW uprawnienia, nie liczba akcji roli
```

**Dwie pulapki, obie zmierzone, obie sa czescia reguly:**

1. **Liczenie akcji zamiast endpointow odwraca ranking.** Pierwsza wersja postawila **Guest Inviter
   nad Global Readerem** dla `User.Read.All` — bo Guest Inviter ma szesnascie waskich odczytow
   wlasciwosci, a Global Reader jedna akcje `users/allProperties/read`, ktora pokrywa wiecej.
   Wazenie liczba endpointow to naprawia.
2. **Sama liczba nadal klamie, wiec kazdy wiersz niesie kolumne `Depth`**: `whole resource` albo
   `selected properties only`, i przy rownym pokryciu pierwsza bije druga. W panelu Roles ten sam
   podzial stoi przy liczniku: **Guest Inviter pokrywa 140 uprawnien na >=50%, z tego 0 na caly
   zasob i 140 tylko na wybrane wlasciwosci**; Global Reader 187, z tego **185 na caly zasob**.
   Bez tej kolumny obie liczby wygladaja tak samo.

Zmierzone dla `User.Read.All` (215 endpointow, 36 rol pasuje w ogole):

| rola | pokrycie | glebokosc |
|---|---|---|
| Global Administrator | 96% | caly zasob |
| User Administrator | 90% | caly zasob |
| Privileged Authentication Administrator | 88% | caly zasob |
| AI Reader | 84% | caly zasob |
| Global Reader | 84% | caly zasob |
| Directory Readers | 84% | tylko wybrane wlasciwosci |

Kazdy wiersz pokazuje **dopasowane akcje katalogowe** (do czterech, potem licznik) i linkuje do
sekcji tej roli w `permissions-reference`. Nota pod tabela mowi, ile rol pasuje w ogole, ile
pokazano, z ilu endpointow liczone jest pokrycie i **`Derived by this brief, not published by
Microsoft`** — pelnym zdaniem, nie gwiazdka.

**Mianownik derywacji bierze sie z TEJ SAMEJ listy endpointow, ktora panel pokazuje wyzej.**
Pierwsza wersja liczyla z surowego pliku i dawala 202 przy 205 w naglowku — dwie rozne liczby
o tym samym na jednej stronie sa gorsze niz jedna niedokladna.

**`34 ze 137 rol nie publikuje zadnej akcji katalogowej`** — role Exchange, Defender i DevOps
miedzy nimi. Nigdy sie tu nie pojawia i **strona mowi to wprost**, zeby ich nieobecnosc nie byla
czytana jako dowod. To ta sama dyscyplina co `notPublished` w §5b.

### Panel Roles — to samo pole, druga przestrzen nazw

`<input id="rq">` przyjmuje **akcje katalogowa** (`microsoft.directory/users/inviteGuest` -> trzy
role: Directory Writers, Guest Inviter, User Administrator) albo **nazwe roli** (-> jej akcje plus
liczba uprawnien Graph, ktore pokrywa, z podzialem na glebokosc). Wlasciciel poprosil o „ta sama
logike co w wyszukiwarce uprawnien" i to jest ona: jedno pole, rozpoznanie wejscia, jawna nota
o tym, ktora przestrzen nazw zostala dopasowana.

### Ile to kosztuje i skad sie bierze

| krok | zrodlo | czas |
|---|---|---|
| mapa endpointow | `microsoftgraph/microsoft-graph-devx-content` -> `permissions/new/permissions.json` | 1,9 s klon + 0,02 s parsowanie |
| daty wejscia endpointow | `git log -S` w tym samym repo | w klonie |
| akcje rol | `MicrosoftDocs/entra-docs` -> `permissions-reference.md` + 139 plikow `includes/` | w klonie §5i |
| derywacja rola-uprawnienie | powyzsze dwa, 879 uprawnien x 103 role | **0,4 s** |

**Klonuj sparse i blobless** (§5ai) — pelny klon devx zaciaga cala historie, sparse blobless daje `permissions/` w **8,4 MB i 2,0 s** (1,3 s klon + 0,7 s `sparse-checkout set permissions`).

### Co z tego idzie do strony zmian

`make_diff.py` (§3) porownuje `graphMap` pole po polu, PER UPRAWNIENIE: endpointy dodane, endpointy
usuniete, zmiana `privilegeLevel`, zmiana `requiresAdminConsent`. To jest przycisk „co sie zmienilo
od ostatniego uruchomienia", o ktory pytal wlasciciel — z ta roznica, ze u nas jest to sekcja
`id="endpoints"` na stronie `/diff/`, a nie przycisk w katalogu.

### Walidator — pozycje 41-44 listy §0

- **41** — `graphMap` istnieje w `soc-brief-state`, ma `commit`, `readOn`, slownik `p` i tablice
  metod `m`; blokow JSON na stronie jest nadal DWA.
- **42** — kazde uprawnienie z `pathSets` w pliku ma `eps` w mapie; suma par po dekodowaniu rowna
  sie liczbie par w pliku (zmierzone 24 099). **Roznica znaczy, ze przebieg cos obcial.**
- **43** — `privilegeLevel` i `requiresAdminConsent` sa na kazdym schemacie, ktory ma je w pliku;
  chip zgody jest CZERWONY przy `required` i ZIELONY przy `not required` — kolor niesie tresc.
- **44** — kazde uprawnienie z niepusta tablica `roles` niesie regule (`div.rulebox`) i kolumne
  `Depth`; zaden wiersz derywacji nie ma pokrycia >100%; mianownik rowna sie liczbie endpointow
  z naglowka panelu. **Mapa bez `roles` daje `BRAK „nie da sie sprawdzic"`, nie OK.**

## 5ak. Panel uprawnienia — UKLAD z v13, wypelniany przez SKRYPT 6

Wlasciciel zobaczyl 7 wrzesnia 2026 opublikowana strone i napisal: *„nowy artefakt powstal, ale
z calym szacunkiem — co to jest? Proponowales html v13, co sie z tym stalo? Nie zostalo uzyte…
caly layout jest zupelnie inny."* Potem trzy konkretne objawy: sekcja `Entra roles that can do this`
*„cos pokazuje, ale nie wiadomo, z czym to jest zwiazane"*; szukanie `User.Read.All` *„i nie mam
endpointow, ktore to uprawnienie uzywa"*; *„nie ma przycisku exact match"*.

**Mial racje we wszystkich trzech, a przyczyna byla po mojej stronie, nie po stronie przebiegu.**

### Co zmierzone na tamtej stronie

| co | wynik |
|---|---|
| `graphMap` w bloku stanu | **kompletna**: 923 uprawnienia, 24 099 par, 7 430 sciezek, 363 derywacje rol |
| bramka §0b | **45 z 46 OK** |
| `details.eps` w calym dokumencie | **jeden**, w `section#graph > .sec-body`, pod naglowkiem `Worked example — User.Read.All` |
| panel po kliknieciu w ktorekolwiek z **1 076** uprawnien | bez endpointow, bez rol |
| `Exact match` przy szukajce katalogu | **nie bylo go tam** — istnial w osobnym widgecie `div.gq` NAD katalogiem |

**Dwie porazki, obie moje.** Pierwsza: dane byly, renderu nie bylo, bo panel buduje SKRYPT 3
powloki, a §5w pozwala ruszyc w skryptach powloki dokladnie dwie rzeczy. Przebieg zrobil jedyna
rzecz, ktora mu zostawala — jeden przyklad server-side — **i uczciwie go tak podpisal**.
Druga, powazniejsza: **wlasciciel zatwierdzil UKLAD (makieta v13), a do §5ah wpisalem OPIS.**
Obrazek i proza to dwa rozne artefakty; przebieg zastosowal proze w ksztalcie powloki i strona
nie przypominala tego, co zostalo zatwierdzone. To jest §0a o jeden poziom wyzej: nie dwa przebiegi
sie rozjechaly, tylko makieta ze specyfikacja.

**I bramka to przepuscila**, bo pozycje 41-44 pytaly o blok stanu i o obecnosc napisow w pliku,
a nie o to, czy panel je pokazuje. Asercja przechodzaca z niewlasciwego powodu — moj wlasny zarzut
z §0b, popelniony w mojej wlasnej bramce.

### Regula

**Panel uprawnienia Graph ma uklad v13 i buduje go SKRYPT 6**, dokladany tak samo jak skrypt 4
(§5y) i skrypt 5 (§5ad).

> **Poprawka z 7 wrzesnia 2026 wieczorem (§5al).** SKRYPT 6 ma od tego dnia trzy zmiany i tylko trzy:
> sekcja `What changed on this permission in the last 14 days` stoi **DRUGA**, zaraz po `At a glance`
> (buduje ja `window.__socHistSection` ze SKRYPTU 8); skrypt wystawia `window.__socOpenPerm(nazwa)`,
> zeby `+` w wierszu historii mogl poprosic katalog o panel; i czyta kotwice `#graph:perm=<nazwa>`,
> zeby wiersz strony `/diff/` mogl w ten panel wskazac. Pelny kod obu skryptow jest w §5al. **Lista dozwolonych zmian w trzech skryptach powloki sie NIE zmienia.**
Skrypt obserwuje `.cat-detail`, czyta nazwe z `h3.cat-title` i sklada panel w tej kolejnosci:

1. **Naglowek** — nazwa monospace i chipy przepisane z `.cat-badges` powloki.
2. **At a glance** — `dl.kv` z: `Kind`, `Object type`, `API`, `Entity` (czytane z tego, co powloka
   juz wyrenderowala), a dalej **z mapy**: `Privilege level` per schemat jako chip 1-4,
   `Admin consent` per schemat **czerwony przy `required`, zielony przy `not required`**,
   `Endpoints` z rozbiciem na metody, `Least privilege`, `Published by Microsoft`, `First tracked`
   i **kazdy `Permission ID` osobno**.
3. **Published by Microsoft** — powloka drukuje jedna KOLUMNE na schemat, v13 jedna KARTE; skrypt
   **transponuje** tabele `proptable` na karty `.scheme` z chipem poziomu i zgody w naglowku.
4. **What this permission can call** — `details.eps`, **zwiniete**, licznik w podpisie, pasek
   `All / GET / POST / … / Least privilege` filtrujacy wiersze, tabela
   `Method | Endpoint | Privilege | Change | Source`, gdzie `Change` niesie date wejscia endpointu
   do pliku Microsoftu, a `Source` linkuje do pliku w KONKRETNYM commicie.
5. **Entra roles that can do this** — `div.rulebox` z `graphMap.rule` i `ruleNote`, potem tabela
   `Entra role | Coverage | Depth | Matched directory actions | Endpoints covered | Source`.
   **Uprawnienie bez pasujacej roli dostaje ZDANIE, nie pusty element.**

Dwa panele powloki, ktore ten uklad zastepuje (`At a glance`, `Published by Microsoft`), skrypt
**ukrywa, nigdy nie usuwa** — nalezą do skryptu 3. Pozostale panele zostaja pod spodem nietkniete.

Skrypt robi jeszcze dwie rzeczy, obie ze zgloszenia:

- **Ukrywa `Worked example`** i wstawia w jego miejsce jedno zdanie, ze przyklad jest teraz
  w kazdym panelu. Blok bez zaznaczonego uprawnienia jest dokladnie tym, co wlasciciel opisal
  jako „cos pokazuje, ale nie wiadomo z czym zwiazane".
- **Dokłada `Exact match` DO SZUKAJKI KATALOGU**, a nie obok niej. Pole ma stac tam, gdzie
  czytelnik pisze; osobny widget nad katalogiem nie odpowiada na pytanie zadane w zielonym polu.

### Dwie pulapki, obie zmierzone i obie sa czescia reguly

1. **`data-id` jest PREFIKSOWANE.** Wpis katalogu ma `data-id="perm-User.Read.All"`, a nazwa siedzi
   w `.ci-name`. Pierwsza wersja `Exact match` porownywala `data-id` z zapytaniem i dawala **zero
   wynikow dla `User.Read.All`** — asercja, ktora nie zapala sie nigdy, jest tak samo bezuzyteczna
   jak ta, ktora zapala sie zawsze.
2. **Ta sama nazwa istnieje na DWOCH powierzchniach.** Katalog wozi `perm-User.Read.All` (Graph)
   i `spo-User.Read.All` (SharePoint). Budowanie panelu po samej nazwie pokazywaloby endpointy
   Grapha przy uprawnieniu SharePointa — ciche pomieszanie dwoch przestrzeni, przed ktorym broni
   §5c. Skrypt sprawdza prefiks zaznaczonego wpisu i **przy innej powierzchni nie robi nic**.

### Zmierzone po dolozeniu, na PRAWDZIWEJ stronie z 7 wrzesnia

Skrypt i arkusz wstrzykniete w opublikowany plik, render headless, oba motywy, 1500 i 390 px,
**zero bledow strony i `scrollWidth === clientWidth` wszedzie**:

| scenariusz wlasciciela | wynik |
|---|---|
| `Worked example` bez zaznaczenia | ukryty, zastapiony jednym zdaniem |
| `Exact match` przy szukajce katalogu | jest; `User.Read.All` daje **2 z 1076** (Graph i SharePoint), licznik `2 exact` |
| Graph `User.Read.All` | panel v13, **215 endpointow**, 10 wierszy rol, GA 97% caly zasob |
| SharePoint `User.Read.All` | **brak panelu Graph** — poprawnie, inna powierzchnia |
| `SecurityAlert.Create.All` / `EntraBackup.ReadWrite.Preview` / `AccessReview.ReadWrite.Membership` | 2 / 1 / 14 endpointow, role: zdanie / zdanie / **6 wierszy** |
| filtr metod | 215 → GET 175 → Least privilege 75 |
| cztery przelaczenia tam i z powrotem | `.v13pane` = 1, bez duplikatow |

**Kazde uprawnienie ma wlasna liczbe** — to jest cala roznica wzgledem jednego przykladu.

### Walidator — pozycja 48 listy §0

Bramka czyta plik, wiec sprawdza, ze skrypt jest i celuje w istniejace klasy; to, czy panel
naprawde sie wypelnia, sprawdza Playwright (§5h) — **i to rozroznienie jest tu cala pointa**,
bo poprzednia wersja bramki dala 45/46 na stronie, ktorej panel byl pusty.

Do `<style>` dochodzi blok wygladu (na koncu, z pozostalymi z §1a, §5e, §5k, §5t, §5w,
§5x, §5y, §5ad i §5ae). Kazdy selektor zaczyna sie od `.v13pane` albo od klasy, ktora tworzy
wylacznie skrypt 6, wiec nic stad nie wycieka na reszte strony. **`--surface2` NIE ISTNIEJE
w tym arkuszu — nazywa sie `--surface-2`** (§5t: sprawdz zmienna, zanim jej uzyjesz):

```css
/* §5ak — panel uprawnienia w ukladzie v13. Kazdy selektor zaczyna sie od .v13pane
   albo od klasy, ktora tworzy wylacznie skrypt 6, wiec nic tu nie wycieka na reszte
   strony. Zmienne sa TE, ktore arkusz juz deklaruje (§5t): `--surface2` nie istnieje,
   nazywa sie `--surface-2`. */
.v13pane{margin:0 0 14px}
.v13pane>header{padding:0 0 10px;border-bottom:1px solid var(--border);margin:0 0 12px}
.v13pane h2{font-family:var(--mono);font-size:17px;margin:0 0 7px}
.v13pane .chips{display:flex;flex-wrap:wrap;gap:6px}
.v13pane .sec{padding:0 0 14px;margin:0 0 14px;border-bottom:1px solid var(--border)}
.v13pane .sec:last-child{border-bottom:0;margin-bottom:0;padding-bottom:0}
.v13pane .sec h3{font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin:0 0 9px}
.v13pane dl.kv{display:grid;grid-template-columns:minmax(120px,190px) minmax(0,1fr);gap:7px 16px;margin:0;font-size:13.5px}
.v13pane dl.kv dt{color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.04em;font-weight:700}
.v13pane dl.kv dd{margin:0;min-width:0;overflow-wrap:anywhere}
.v13pane .scheme{border:1px solid var(--border);border-radius:10px;background:var(--surface-2);padding:11px 13px;margin:0 0 10px}
.v13pane .scheme:last-child{margin-bottom:0}
.v13pane .scheme .sh{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:0 0 8px}
.v13pane .scheme .nm{font-weight:700;font-size:13.5px}
.v13pane .mono{font-family:var(--mono);font-size:12.5px}
.v13pane .note{color:var(--muted);font-size:12.5px;margin:8px 0 0}
.v13pane .empty{background:var(--surface-2);border:1px dashed var(--border);border-radius:10px;padding:11px 13px;color:var(--muted);margin:0;font-size:13px}
.v13pane .rulebox{border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:10px;
 background:var(--surface-2);padding:10px 13px;margin:0 0 11px;font-size:13px}
.v13pane .actlist{font-size:12px}
.v13pane .rname{font-family:var(--sans);font-weight:600;min-width:150px}
.v13pane .badge.t-ok{background:var(--ok-soft);color:var(--ok);box-shadow:inset 0 0 0 1.5px var(--ok);border-radius:999px}
.v13pane .badge.t-bad{background:var(--bad-soft);color:var(--bad);box-shadow:inset 0 0 0 1.5px var(--bad);border-radius:999px}
.v13pane .badge.t-warn{background:var(--warn-soft);color:var(--warn);box-shadow:inset 0 0 0 1.5px var(--warn);border-radius:999px}
.v13pane .badge.t-acc{background:var(--accent-soft);color:var(--accent);box-shadow:inset 0 0 0 1.5px var(--accent);border-radius:999px}
.v13pane .badge.t-grey{background:var(--grey-soft);color:var(--grey);box-shadow:inset 0 0 0 1.5px var(--border);border-radius:999px}
.v13pane .m{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:700;padding:1px 7px;border-radius:5px;background:var(--surface-2);color:var(--muted)}
.v13pane .m-GET{background:var(--ok-soft);color:var(--ok)}
.v13pane .m-POST{background:var(--accent-soft);color:var(--accent)}
.v13pane .m-PATCH{background:var(--warn-soft);color:var(--warn)}
.v13pane .m-DELETE{background:var(--bad-soft);color:var(--bad)}
.v13pane .m-PUT{background:var(--info-soft);color:var(--info)}
.v13pane details.eps{border:1px solid var(--border);border-radius:10px;background:var(--surface-2)}
.v13pane details.eps>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:11px 13px}
.v13pane details.eps>summary::-webkit-details-marker{display:none}
.v13pane details.eps>summary::before{content:"+";font-family:var(--mono);font-size:15px;font-weight:700;
 width:22px;height:22px;flex:0 0 22px;display:inline-flex;align-items:center;justify-content:center;
 border-radius:6px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
.v13pane details.eps[open]>summary::before{content:"\2212"}
.v13pane details.eps>summary .sm-t{flex:1 1 auto;font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;font-weight:700;color:var(--muted)}
.v13pane .mf{display:flex;flex-wrap:wrap;gap:6px;margin:0 13px 10px}
.v13pane .mf button{font:inherit;font-size:12px;font-weight:600;padding:4px 11px;border-radius:999px;
 border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer}
.v13pane .mf button[aria-pressed="true"]{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
.v13pane details.eps>.tw,.v13pane details.eps>.note{margin:0 13px 12px}
label.s6exact{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:600;
 color:var(--text);white-space:nowrap;margin-left:10px;cursor:pointer}
p.s6note{color:var(--muted);font-size:13px;margin:0 0 12px}
@media (max-width:760px){
  .v13pane dl.kv{grid-template-columns:1fr;gap:3px 0}
  .v13pane dl.kv dt{padding-top:7px}
  .v13pane .badge{white-space:normal;overflow-wrap:anywhere}
}
```

A na koniec `<body>`, jako **SZOSTY** blok `<script>`, ten kod — kopiowany co do bajtu:

```js
/* ===========================================================================
   SCRIPT 6 — THE GRAPH PERMISSION PANEL, IN THE APPROVED v13 LAYOUT
   (CLAUDE.md 5ak). ADDED, never a replacement: shell scripts 1-3 and the added
   scripts 4 (§5y) and 5 (§5ad) are untouched.

   Two failures on the 7 Sep 2026 page, and both were mine, not the run's:
   1. `graphMap` carried all 923 permissions, 24,099 pairs and 363 role
      derivations, and the gate passed 45 of 46 — yet `details.eps` was rendered
      ONCE, statically, outside the panel. All 1,076 catalog entries opened
      without endpoints and without roles. The data was complete; the render was
      missing, because the panel is built by shell script 3 and §5w forbids
      editing it.
   2. The owner approved a LAYOUT (the v13 mock) and §5ah carried a DESCRIPTION.
      The run applied the description inside the shell's own panel shape, so the
      page bore no resemblance to what was approved. A picture and prose are not
      the same artefact — that is §0a, one level up.

   This script rebuilds the permission panel in the approved order and shape,
   from the state block and from what the shell already rendered. It hides the
   shell's own "At a glance" and "Published by Microsoft" panels rather than
   deleting them, and leaves every other panel below untouched.
   ALL UI TEXT IS ENGLISH.
   =========================================================================== */
(function () {
  "use strict";
  var SRC = "https://github.com/microsoftgraph/microsoft-graph-devx-content/blob/%C/permissions/new/permissions.json";
  var ROLEREF = "https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#";
  var LVL = { 1: ["Level 1", "Low"], 2: ["Level 2", "Moderate"], 3: ["Level 3", "High"], 4: ["Level 4", "Critical"] };

  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x !== undefined) n.textContent = x; return n; }
  function state() {
    var s = document.getElementById("soc-brief-state");
    if (!s) return null;
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }
  var ST = state(), GM = (ST && ST.graphMap) || null;

  /* `eps` is "<method index>:<index ranges>", ranges comma-separated, method groups
     semicolon-separated. 142-154 means thirteen consecutive paths. */
  function decode(txt) {
    var out = [], M = (GM && GM.m) || [], P = (GM && GM.p) || [];
    (txt || "").split(";").forEach(function (grp) {
      if (!grp || grp.indexOf(":") < 0) return;
      var bits = grp.split(":"), meth = M[parseInt(bits[0], 10)];
      bits[1].split(",").forEach(function (part) {
        if (!part) return;
        var a, b;
        if (part.indexOf("-") > 0) { var t = part.split("-"); a = +t[0]; b = +t[1]; } else { a = b = +part; }
        for (var i = a; i <= b; i++) if (P[i] !== undefined) out.push({ m: meth, p: P[i], i: i });
      });
    });
    return out;
  }
  function keyset(list) { var s = {}; list.forEach(function (x) { s[x.m + " " + x.p] = 1; }); return s; }
  function srcLink(label) {
    var a = el("a", "lnk", label || "Source file");
    a.href = SRC.replace("%C", ((GM && GM.commit) || "dev").split(" ")[0]);
    a.target = "_blank"; a.rel = "noopener";
    return a;
  }
  function lvlChip(n) {
    if (!n || !LVL[n]) return el("span", "badge t-grey", "not stated");
    var c = n <= 2 ? "t-ok" : (n === 3 ? "t-warn" : "t-bad");
    return el("span", "badge " + c, LVL[n][0] + " · " + LVL[n][1]);
  }
  function consentChip(c, prefix) {
    return el("span", "badge " + (c ? "t-bad" : "t-ok"),
      (prefix ? prefix + ": " : "") + (c ? "admin consent required" : "no admin consent"));
  }
  function kv(dl, k, v) {
    dl.appendChild(el("dt", null, k));
    var dd = el("dd");
    if (typeof v === "string") dd.textContent = v; else if (v) dd.appendChild(v);
    dl.appendChild(dd);
  }

  /* ---------- what the shell already rendered, read back rather than recomputed ---------- */
  function shellMeta(inner) {
    var out = [], dl = inner.querySelector("dl.cat-meta");
    if (!dl) return out;
    var kids = [].slice.call(dl.children);
    for (var i = 0; i < kids.length - 1; i++)
      if (kids[i].tagName === "DT" && kids[i + 1].tagName === "DD")
        out.push([kids[i].textContent.trim(), kids[i + 1].textContent.trim()]);
    return out;
  }
  function shellPublished(inner) {
    /* the shell prints one COLUMN per scheme; v13 prints one CARD per scheme, so transpose */
    var t = inner.querySelector("table.proptable");
    if (!t) return null;
    var heads = [].slice.call(t.querySelectorAll("thead th")).map(function (x) { return x.textContent.trim(); });
    var cols = heads.slice(1), rows = [];
    [].slice.call(t.querySelectorAll("tbody tr")).forEach(function (tr) {
      var rh = tr.querySelector("th"); if (!rh) return;
      rows.push([rh.textContent.trim(), [].slice.call(tr.querySelectorAll("td")).map(function (td) { return td.textContent.trim(); })]);
    });
    return { cols: cols, rows: rows };
  }

  /* ---------- sections ---------- */
  function glance(name, d, inner) {
    var sec = el("div", "sec"); sec.appendChild(el("h3", null, "At a glance"));
    var dl = el("dl", "kv");
    var meta = shellMeta(inner), seen = {};
    ["Kind", "Object type", "Origin", "API", "Entity"].forEach(function (want) {
      meta.forEach(function (p) { if (p[0].toLowerCase() === want.toLowerCase() && !seen[want]) { kv(dl, p[0], p[1]); seen[want] = 1; } });
    });
    var sch = (d && d.s) || {};
    if (Object.keys(sch).length) {
      var lw = el("span");
      Object.keys(sch).forEach(function (k, i) {
        if (i) lw.appendChild(document.createTextNode(" · "));
        lw.appendChild(document.createTextNode(k + ": "));
        lw.appendChild(lvlChip(sch[k].l));
      });
      kv(dl, "Privilege level", lw);
      var cw = el("span");
      Object.keys(sch).forEach(function (k, i) {
        if (i) cw.appendChild(document.createTextNode(" "));
        cw.appendChild(consentChip(sch[k].c, k));
      });
      kv(dl, "Admin consent", cw);
    }
    if (d && d.eps) {
      var eps = decode(d.eps), least = keyset(decode(d.least)), byM = {};
      eps.forEach(function (x) { byM[x.m] = (byM[x.m] || 0) + 1; });
      var n = 0; eps.forEach(function (x) { if (least[x.m + " " + x.p]) n++; });
      kv(dl, "Endpoints", eps.length + " across " + Object.keys(byM).sort().map(function (m) { return m + " " + byM[m]; }).join(", "));
      kv(dl, "Least privilege", n + " of " + eps.length + " endpoints list this permission as least privileged");
    }
    meta.forEach(function (p) {
      var k = p[0].toLowerCase();
      if (k === "published by microsoft" || k === "first tracked" || k === "consent") kv(dl, p[0], p[1]);
    });
    Object.keys((d && d.ids) || {}).forEach(function (k) {
      var s = el("span", "mono", d.ids[k]); kv(dl, "Permission ID · " + k, s);
    });
    sec.appendChild(dl);
    return sec;
  }

  function published(d, inner) {
    var pub = shellPublished(inner);
    if (!pub || !pub.cols.length) return null;
    var sec = el("div", "sec"); sec.appendChild(el("h3", null, "Published by Microsoft"));
    var sch = (d && d.s) || {};
    pub.cols.forEach(function (colName, ci) {
      var card = el("div", "scheme"), head = el("div", "sh");
      head.appendChild(el("span", "nm", colName));
      var key = Object.keys(sch).filter(function (k) { return k.toLowerCase().indexOf(colName.toLowerCase()) >= 0 || colName.toLowerCase().indexOf(k.toLowerCase()) >= 0; })[0];
      if (key) { head.appendChild(lvlChip(sch[key].l)); head.appendChild(consentChip(sch[key].c)); }
      card.appendChild(head);
      var dl = el("dl", "kv");
      pub.rows.forEach(function (r) {
        var v = r[1][ci];
        if (v !== undefined && v !== "" && v !== "—") kv(dl, r[0], v);
      });
      card.appendChild(dl); sec.appendChild(card);
    });
    return sec;
  }

  function epsSec(d, api, isPerm) {
    /* Sekcja istnieje ZAWSZE — inaczej panel wpisu bez mapy wyglada jak inny uklad,
       a wlasciciel zglosil 7 wrzesnia: „sposob przedstawiania szczegolow tak samo,
       a mialo byc 1:1". Brak mapy jest ZDANIEM, nie brakiem sekcji. */
    if (!d || !d.eps) {
      var s0 = el("div", "sec"), det0 = el("details", "eps epsinject"), sum0 = el("summary");
      sum0.appendChild(el("span", "sm-t", "What this permission can call"));
      sum0.appendChild(el("span", "badge t-grey", "no endpoint map"));
      det0.appendChild(sum0);
      det0.appendChild(el("p", "note",
        !isPerm
          ? ("This entry sits on the " + (api || "another") + " surface. Microsoft's endpoint map covers " +
             "Microsoft Graph only, so there is nothing to list here — and that absence is the honest " +
             "answer, not a gap in this page.")
          : ("Microsoft's permissions.json carries no pathSet for this name" +
             ((GM && GM.commit) ? (" at commit " + GM.commit) : "") + ", so no endpoint can be listed. " +
             "The entry is real; the map is silent about it.")));
      s0.appendChild(det0);
      return s0;
    }
    var eps = decode(d.eps), least = keyset(decode(d.least)), byM = {};
    eps.forEach(function (x) { byM[x.m] = (byM[x.m] || 0) + 1; });
    var nL = 0; eps.forEach(function (x) { if (least[x.m + " " + x.p]) nL++; });

    var sec = el("div", "sec"), det = el("details", "eps epsinject");
    var sum = el("summary");
    sum.appendChild(el("span", "sm-t", "What this permission can call"));
    sum.appendChild(el("span", "badge t-acc", eps.length + " endpoint" + (eps.length === 1 ? "" : "s")));
    det.appendChild(sum);

    var mf = el("div", "mf");
    function chip(lab, key) {
      var b = el("button", null, lab); b.type = "button"; b.dataset.m = key;
      b.setAttribute("aria-pressed", String(key === "ALL")); mf.appendChild(b);
    }
    chip("All " + eps.length, "ALL");
    Object.keys(byM).sort().forEach(function (m) { chip(m + " " + byM[m], m); });
    if (nL) chip("Least privilege " + nL, "LEAST");
    det.appendChild(mf);

    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), tr = el("tr");
    ["Method", "Endpoint", "Privilege", "Change", "Source"].forEach(function (h) { tr.appendChild(el("th", null, h)); });
    th.appendChild(tr); tb.appendChild(th);
    var body = el("tbody");
    eps.sort(function (a, b) { return a.p < b.p ? -1 : a.p > b.p ? 1 : (a.m < b.m ? -1 : 1); });
    eps.forEach(function (x) {
      var isL = !!least[x.m + " " + x.p], r = el("tr");
      r.dataset.m = x.m; r.dataset.least = isL ? "1" : "0";
      var c0 = el("td"); c0.appendChild(el("span", "m m-" + x.m, x.m)); r.appendChild(c0);
      var c1 = el("td", "p"); c1.appendChild(el("span", "mono", x.p)); r.appendChild(c1);
      var c2 = el("td");
      if (isL) c2.appendChild(el("span", "badge t-ok", "least privilege"));
      r.appendChild(c2);
      var c3 = el("td"), when = (d["new"] || {})[String(x.i)];
      if (when) c3.appendChild(el("span", "badge t-acc", "added " + when));
      r.appendChild(c3);
      var c4 = el("td"); c4.appendChild(srcLink()); r.appendChild(c4);
      body.appendChild(r);
    });
    tb.appendChild(body); tw.appendChild(tb); det.appendChild(tw);
    var note = el("p", "note",
      "Read from Microsoft's own permissions.json in microsoftgraph/microsoft-graph-devx-content, commit " +
      ((GM && GM.commit) || "unknown") + ". The change column comes from that file's git history, so the date is Microsoft's, not the date this brief noticed.");
    det.appendChild(note);

    mf.addEventListener("click", function (ev) {
      var b = ev.target.closest("button"); if (!b) return;
      [].forEach.call(mf.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var m = b.dataset.m;
      [].forEach.call(body.querySelectorAll("tr"), function (r) {
        r.hidden = !(m === "ALL" || (m === "LEAST" ? r.dataset.least === "1" : r.dataset.m === m));
      });
    });
    sec.appendChild(det);
    return sec;
  }

  function rolesSec(d) {
    var sec = el("div", "sec");
    sec.appendChild(el("h3", null, "Entra roles that can do this"));
    var rb = el("div", "rulebox");
    rb.appendChild(el("b", null, "How this list is derived, and what Microsoft does not publish."));
    rb.appendChild(document.createTextNode(" " + ((GM && GM.rule) || "")));
    var n = el("p", "note");
    n.appendChild(el("b", null, (GM && GM.ruleNote) || "Derived by this brief, not published by Microsoft."));
    rb.appendChild(n); sec.appendChild(rb);

    var rows = (d && d.roles) || [];
    if (!d) {
      sec.appendChild(el("p", "empty",
        "No endpoint map for this entry, so no role coverage is derived. The rule above still says how it " +
        "would be derived, and what Microsoft does not publish."));
      return sec;
    }
    if (!rows.length) {
      sec.appendChild(el("p", "empty",
        "No Entra directory role holds an action on any resource this permission reaches. That is a result, not a gap: the resources sit outside the microsoft.directory namespace, and 33 of the 136 built-in roles publish no directory action at all, so their absence here is not evidence."));
      return sec;
    }
    var total = d.eps ? decode(d.eps).length : 0;
    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), tr = el("tr");
    ["Entra role", "Coverage", "Depth", "Matched directory actions", "Endpoints covered", "Source"]
      .forEach(function (h) { tr.appendChild(el("th", null, h)); });
    th.appendChild(tr); tb.appendChild(th);
    var body = el("tbody");
    rows.forEach(function (r) {
      var nm = r[0], pct = r[1], broad = r[2], acts = r[3] || [], cov = r[4], slug = r[5];
      var t = el("tr");
      t.appendChild(el("td", "rname", nm));
      var c1 = el("td"); c1.appendChild(el("b", null, pct + "%")); t.appendChild(c1);
      var c2 = el("td");
      c2.appendChild(el("span", "badge " + (broad ? "t-ok" : "t-warn"), broad ? "whole resource" : "selected properties only"));
      t.appendChild(c2);
      var c3 = el("td", "actlist");
      acts.slice(0, 4).forEach(function (a) { var s = el("div"); s.appendChild(el("span", "mono", a)); c3.appendChild(s); });
      if (acts.length > 4) c3.appendChild(el("div", "note", "… and " + (acts.length - 4) + " more"));
      t.appendChild(c3);
      t.appendChild(el("td", null, (cov !== undefined ? cov : Math.round(total * pct / 100)) + " of " + total));
      var c5 = el("td"), a = el("a", "lnk", "Role reference");
      a.href = ROLEREF + (slug || nm.toLowerCase().replace(/[^a-z0-9]+/g, "-"));
      a.target = "_blank"; a.rel = "noopener"; c5.appendChild(a); t.appendChild(c5);
      body.appendChild(t);
    });
    tb.appendChild(body); tw.appendChild(tb); sec.appendChild(tw);
    sec.appendChild(el("p", "note",
      rows.length + " role" + (rows.length === 1 ? "" : "s") + " shown, ranked by the share of this permission's " +
      total + " endpoints the role also carries as a directory action. Whole resource beats property-limited at equal coverage."));
    return sec;
  }


  /* ---------- the worked example, and the missing Exact match ----------
     The 7 Sep page carried a single server-rendered "Worked example — User.Read.All"
     above the catalog: an endpoint table and a role table attached to no selection,
     which is what the owner saw as "it shows something and I do not know what it
     relates to". Once every panel carries its own, the example is redundant and
     confusing, so it is hidden — never deleted, because the run owns that markup.
     The Exact match box lived in a SEPARATE query widget, not on the catalog's own
     search, so searching the green box could not find it. It belongs where the
     reader types. */
  function tidySection() {
    var body = document.querySelector('#graph > .sec-body');
    if (!body) return;
    var kids = [].slice.call(body.children), start = -1, end = -1;
    kids.forEach(function (x, i) {
      if (start < 0 && x.tagName === "H3" && /worked example/i.test(x.textContent || "")) start = i;
      if (start >= 0 && x.classList && x.classList.contains("rnote")) end = i;
    });
    if (start >= 0) {
      if (end < start) end = kids.length - 1;
      for (var i = start; i <= end; i++) { kids[i].hidden = true; kids[i].dataset.s6hidden = "1"; }
      var note = el("p", "wnote s6note");
      note.textContent = "The worked example that stood here is now on every permission: open any entry " +
        "in the catalog below and its own endpoint list and role table are in its panel.";
      body.insertBefore(note, kids[start]);
    }
  }

  /* ---------- four kinds of query in ONE box (§5ah), and the examples row ----------
     A GUID, a path, a directory action and a name are four different namespaces.
     The shell's list searches names only and rebuilds itself from them, so for the
     other three the answer is a NOTE that names what was found, with each name a
     button — the same shape SCRIPT 7 uses in Roles. */
  var PATHIDX = null;
  function pathIndex() {
    if (PATHIDX) return PATHIDX;
    PATHIDX = {};
    var P = (GM && GM.p) || [];
    Object.keys((GM && GM.perms) || {}).forEach(function (n) {
      decode((GM.perms[n] || {}).eps).forEach(function (x) {
        (PATHIDX[x.p] = PATHIDX[x.p] || {})[n] = 1;
      });
    });
    return PATHIDX;
  }
  function byGuid(g) {
    var out = [];
    Object.keys((GM && GM.perms) || {}).forEach(function (n) {
      var ids = GM.perms[n].ids || {};
      Object.keys(ids).forEach(function (k) {
        if (String(ids[k]).toLowerCase() === g) out.push(n + " · " + k);
      });
    });
    return out;
  }
  function resolveQuery(v) {
    var s2 = (v || "").trim();
    if (!s2) return { kind: "", names: null, note: "" };
    if (/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(s2)) {
      var hit = byGuid(s2.toLowerCase());
      return { kind: "permission ID", names: hit.map(function (x) { return x.split(" · ")[0]; }),
               note: hit.length ? ("That permission ID belongs to " + hit.join(", ") + ".")
                                : "No permission in Microsoft's map carries that ID." };
    }
    if (s2.charAt(0) === "/") {
      var idx = pathIndex(), hits = {}, n2 = 0;
      Object.keys(idx).forEach(function (p) {
        if (p.toLowerCase().indexOf(s2.toLowerCase()) >= 0) {
          n2++; Object.keys(idx[p]).forEach(function (nm) { hits[nm] = 1; });
        }
      });
      var names = Object.keys(hits).sort();
      return { kind: "endpoint", names: names,
               note: names.length ? (n2 + " path" + (n2 === 1 ? "" : "s") + " match, reachable with " +
                                     names.length + " permission" + (names.length === 1 ? "" : "s") + ".")
                                  : "No path in Microsoft's map matches that." };
    }
    if (s2.toLowerCase().indexOf("microsoft.") === 0) {
      var ri = window.__socRoleIndex, roles = [];
      if (ri && ri.byAction) Object.keys(ri.byAction).forEach(function (k) {
        if (k.toLowerCase().indexOf(s2.toLowerCase()) >= 0)
          ri.byAction[k].forEach(function (r) { if (roles.indexOf(r) < 0) roles.push(r); });
      });
      return { kind: "directory action", names: [],
               note: "That is an Entra directory action, not a Graph endpoint" +
                     (roles.length ? (" — " + roles.length + " role" + (roles.length === 1 ? "" : "s") +
                                      " carry it: " + roles.slice(0, 8).join(", ") +
                                      (roles.length > 8 ? " …" : "") + ". Open the Roles tab to see them.")
                                   : ". No role in this catalog publishes it.") };
    }
    return { kind: "permission name", names: null, note: "" };
  }

  function exactMatch() {
    var cat = document.querySelector('.catalog[data-catalog="graph"]');
    if (!cat || cat.querySelector(".s6exact")) return;
    var row = cat.querySelector(".cat-searchrow"), input = cat.querySelector("input.cat-search");
    if (!row || !input) return;
    var lab = el("label", "s6exact");
    var box = document.createElement("input"); box.type = "checkbox"; box.id = "s6exact";
    lab.appendChild(box); lab.appendChild(document.createTextNode(" Exact match"));
    var cnt = row.querySelector(".rowcount");
    if (cnt) row.insertBefore(lab, cnt); else row.appendChild(lab);

    var why = el("p", "s7why"); why.hidden = true;
    var list0 = cat.querySelector(".cat-list");
    if (list0 && list0.parentNode) list0.parentNode.insertBefore(why, list0);

    /* the same clickable examples v16 carries; each one is a query this box answers */
    var tips = el("div", "s7tips");
    tips.appendChild(el("span", "lab", "Examples — click one"));
    [["name", "User.Read.All"], ["endpoint", "/users/{id}/manager"],
     ["permission ID", (function () {
        var p0 = (GM && GM.perms) ? GM.perms["User.Read"] : null;
        return p0 && p0.ids ? p0.ids[Object.keys(p0.ids)[0]] : "";
      })()],
     ["directory action", "microsoft.directory/users/inviteGuest"]].forEach(function (t) {
      if (!t[1]) return;
      var b = el("button", null, ""); b.type = "button";
      b.appendChild(el("b", null, t[0])); b.appendChild(document.createTextNode(t[1]));
      b.addEventListener("click", function () {
        input.value = t[1];
        input.dispatchEvent(new Event("input", { bubbles: true }));
        setTimeout(apply, 0); input.focus();
      });
      tips.appendChild(b);
    });
    if (row.parentNode) row.parentNode.insertBefore(tips, row);

    var list = cat.querySelector(".cat-list"), applying = false;
    function apply() {
      if (applying || !list) return;
      applying = true;
      try {
        var r = resolveQuery(input.value);
        why.textContent = ""; why.hidden = !r.note;
        if (r.note) {
          why.appendChild(document.createTextNode(r.note));
          if (r.names && r.names.length) {
            why.appendChild(document.createTextNode(" The list below searches names, so it does not answer this " +
              "question — open a permission from here:"));
            var hb = el("span", "s7hits");
            r.names.slice(0, 12).forEach(function (n) {
              var b2 = el("button", null, n); b2.type = "button";
              b2.addEventListener("click", function () {
                input.value = "";
                input.dispatchEvent(new Event("input", { bubbles: true }));
                setTimeout(function () {
                  var inner = window.__socOpenPerm && window.__socOpenPerm(n);
                  if (inner && inner.scrollIntoView) inner.scrollIntoView({ block: "start" });
                }, 140);
              });
              hb.appendChild(b2);
            });
            if (r.names.length > 12) hb.appendChild(el("span", "note", " … and " + (r.names.length - 12) + " more"));
            why.appendChild(hb);
          }
        }
        var q = (input.value || "").trim().toLowerCase(), on = box.checked && q, shown = 0;
        [].forEach.call(list.querySelectorAll(".cat-item"), function (b) {
          if (on) {
            var nm = ((b.querySelector(".ci-name") || {}).textContent ||
                      (b.dataset.id || "").replace(/^[a-z0-9]+-/, "")).trim().toLowerCase();
            if (nm !== q) { b.hidden = true; return; }
          }
          if (b.dataset.s6hid === "1") { b.hidden = false; }
          if (!b.hidden) shown++;
        });
        if (cnt && on) cnt.textContent = shown + " exact";
      } finally { applying = false; }
    }
    box.addEventListener("change", apply);
    /* apply() now also writes the note for the three other namespaces, so it must run
       on EVERY keystroke, not only when Exact match is ticked. */
    input.addEventListener("input", function () { setTimeout(apply, 0); setTimeout(apply, 200); });
    if (window.MutationObserver && list)
      new MutationObserver(function () { if (box.checked) apply(); }).observe(list, { childList: true });
  }

  /* ---------- rebuild ---------- */
  function build(inner) {
    if (!inner || inner.querySelector(".v13pane")) return;
    var h = inner.querySelector(".cat-title");
    if (!h) return;
    var name = (h.textContent || "").trim();
    var sel = document.querySelector('.catalog[data-catalog="graph"] .cat-item[aria-selected="true"]');
    var id = sel ? (sel.dataset.id || "") : "";
    var api = "";
    shellMeta(inner).forEach(function (p) { if (/^(api|surface)$/i.test(p[0])) api = p[1]; });
    /* The SAME name exists on two surfaces (SharePoint's `Sites.Selected` and Graph's),
       so the endpoint map is read only for a Microsoft Graph entry. The discriminator is
       the entry's SURFACE, not a prefix on `data-id`: measured 7 September 2026, the ids
       in this catalog are not uniformly prefixed — `perm-` exists, but so do bare names
       and entity-derived ids, and gating on `perm-` silently refused most entries. Only
       SharePoint uses a prefix (`spo-`), and it also carries the surface. The PANEL is
       built for every entry either way, because one layout means one layout. */
    var onGraph = !api || /microsoft graph/i.test(api);
    var isPerm = onGraph && id.indexOf("spo-") !== 0;
    var d = (isPerm && GM && GM.perms) ? GM.perms[name] : null;

    var pane = el("div", "v13pane");
    var head = el("header"), h2 = el("h2", "mono", name);
    head.appendChild(h2);
    var chips = el("div", "chips"), src = inner.querySelector(".cat-badges");
    if (src) [].forEach.call(src.querySelectorAll(".badge"), function (b) {
      chips.appendChild(el("span", "badge t-grey", b.textContent.trim()));
    });
    head.appendChild(chips); pane.appendChild(head);

    pane.appendChild(glance(name, d, inner));
    /* §5al: the 14-day section is SECOND in BOTH panels. The owner's point 2 of
       7 September was a position, not a preference, so it is set here and in
       SCRIPT 7 by the same rule. SCRIPT 8 owns the ledger and builds the node. */
    if (window.__socHistSection) {
      var hs = window.__socHistSection("perm", name);
      if (hs) pane.appendChild(hs);
    }
    var pb = published(d, inner); if (pb) pane.appendChild(pb);
    var ep = epsSec(d, api, isPerm); if (ep) pane.appendChild(ep);
    pane.appendChild(rolesSec(d));

    /* the two panels this pane replaces are hidden, never removed: script 3 owns them */
    [].forEach.call(inner.querySelectorAll("section.cat-panel"), function (s) {
      var t = (s.querySelector("h4") || {}).textContent || "";
      if (/at a glance|published by microsoft/i.test(t)) s.hidden = true;
    });
    /* and so is the shell's own head: the pane carries the name and the chips, and
       the owner saw the title printed twice. */
    var ch = inner.querySelector(".cat-head"); if (ch) ch.hidden = true;
    var after = inner.querySelector(".cat-head");
    if (after && after.nextSibling) inner.insertBefore(pane, after.nextSibling);
    else inner.insertBefore(pane, inner.firstChild);
  }

  /* the catalog's own rendering, on demand — SCRIPT 8's `+` clones what this
     returns, so the history row and the catalog show ONE panel, not two builds */
  window.__socOpenPerm = function (name) {
    var cat = document.querySelector('.catalog[data-catalog="graph"]');
    if (!cat) return null;
    var want = null;
    [].forEach.call(cat.querySelectorAll(".cat-item"), function (b) {
      var nm = ((b.querySelector(".ci-name") || {}).textContent ||
                (b.dataset.id || "").replace(/^[a-z0-9]+-/, "")).trim();
      if (!want && nm === name && (b.dataset.id || "").indexOf("perm-") === 0) want = b;
    });
    if (!want) return null;
    want.click();
    return cat.querySelector(".cat-detail .cat-detail-inner");
  };


  /* A row on the /diff/ page cannot open a panel: that page carries no catalog by
     design (§3). It can point at one. `#graph:perm=<name>` selects the entry
     here, so a link from the change page lands on the panel itself. */
  function fromHash() {
    var m = /^#graph:perm=(.+)$/.exec(decodeURIComponent(location.hash || ""));
    if (!m) return;
    var name = m[1];
    setTimeout(function () {
      var inner = window.__socOpenPerm && window.__socOpenPerm(name);
      if (inner && inner.scrollIntoView) inner.scrollIntoView({ block: "start" });
    }, 260);
  }
  /* ---------- the left strip: what v16 puts next to a permission ----------
     v16 shows the schemes the permission is published under; the shell shows the
     change kind, `beta`, abbreviations and a date. Same rule as in SCRIPT 7: hide
     the shell's row, append ours, re-decorate on every render. */
  function decorate() {
    var cat = document.querySelector('.catalog[data-catalog="graph"]');
    if (!cat) return;
    var list = cat.querySelector(".cat-list"); if (!list) return;
    [].forEach.call(list.querySelectorAll(".cat-item"), function (b) {
      if (b.dataset.v16 === "1") return;
      var nm = ((b.querySelector(".ci-name") || {}).textContent || "").trim();
      b.dataset.v16 = "1";
      var d = (GM && GM.perms) ? GM.perms[nm] : null;
      var keys = d && d.s ? Object.keys(d.s) : [];
      var m = el("div", "ci-v16");
      var old = b.querySelector(".ci-meta");
      if (keys.length) {
        keys.forEach(function (k) { m.appendChild(el("span", "badge t-grey", k)); });
      } else if (old) {
        /* Not in Microsoft's map — a catalog correction or another surface. It still
           gets OUR chips, rewritten from what the shell knows, because a list that
           speaks two visual languages is the thing the owner keeps pointing at. */
        var seen = {};
        [].forEach.call(old.querySelectorAll(".badge"), function (x) {
          var t = (x.textContent || "").trim();
          if (!t || seen[t.toLowerCase()]) return;
          seen[t.toLowerCase()] = 1;
          var cls = /correction|catalog/i.test(t) ? "t-warn"
                  : /beta|preview/i.test(t) ? "t-acc"
                  : /deleg|app/i.test(t) ? "t-grey" : "t-grey";
          m.appendChild(el("span", "badge " + cls, t));
        });
      }
      if (m.childNodes.length) {
        if (old) old.hidden = true;
        b.appendChild(m);
      }
    });
  }
  function watchList() {
    var cat = document.querySelector('.catalog[data-catalog="graph"]');
    var list = cat && cat.querySelector(".cat-list"); if (!list) return;
    var busy = false;
    function run() { if (busy) return; busy = true; try { decorate(); var i2 = cat.querySelector("input.cat-search"); if (i2) i2.placeholder = "Search permissions"; } finally { busy = false; } }
    run();
    if (window.MutationObserver)
      new MutationObserver(function () { if (!busy) run(); }).observe(list, { childList: true });
  }

  function boot() {
    /* Bez mapy panel nadal powstaje — At a glance i tresc Microsoftu pochodza z tego,
       co powloka juz wyrenderowala. Milczenie dawaloby DWA rozne uklady w jednej
       zakladce, a to jest dokladnie ta rozbieznosc, przed ktora stoi §0a. */
    tidySection(); exactMatch(); watchList(); fromHash();
    window.addEventListener("hashchange", fromHash);
    [].forEach.call(document.querySelectorAll('.catalog[data-catalog="graph"] .cat-detail'), function (det) {
      build(det.querySelector(".cat-detail-inner"));
      if (window.MutationObserver)
        new MutationObserver(function () { build(det.querySelector(".cat-detail-inner")); })
          .observe(det, { childList: true, subtree: false });
    });
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", function () { setTimeout(boot, 120); });
  else setTimeout(boot, 120);
})();
```

## 5ai. Klonowanie — sparse i blobless, bo repozytorium ma juz 111 MB

Zmierzone 6 wrzesnia 2026. `MS_SOC` sklonowane plytko to **111 MB i 5,05 s**, z czego `site/` to
107 MB: `history/` 64 MB i `data/` 38 MB. Przy okolo 7 MB dziennie to 2,5 GB rocznie, a **kazdy
z czterech przebiegow dnia placi ten koszt od nowa**, choc trzy z nich potrzebuja jednego pliku.

| co przebieg robi | polecenie | zmierzone |
|---|---|---|
| **tylko czyta `CLAUDE.md`** | `git clone --depth 1 --filter=blob:none --sparse <repo> x` + `git -C x sparse-checkout set /CLAUDE.md` | **660 kB, 1,13 s** |
| **pisze strone, nie rusza archiwum** | to samo, dalej `git -C x sparse-checkout set --no-cone '/CLAUDE.md' '/site/**' '!/site/history/**' '!/site/data/**'` | **6,5 MB, ~1,2 s** |
| pelny plytki klon (stan sprzed) | `git clone --depth 1 <repo>` | 111 MB, 5,05 s |
| `permissions/` z devx (§5ah) | `git clone --depth 1 --filter=blob:none --sparse … devx` + `sparse-checkout set permissions` | **8,4 MB, 2,0 s** |

**Trzy rzeczy, ktore trzeba wiedziec, zeby to nie skasowalo archiwum:**

1. **Tryb stozkowy przyjmuje KATALOGI, nie pliki.** `sparse-checkout set /CLAUDE.md site/index.html`
   nie zmaterializuje `site/` w ogole — sprawdzone, katalog po prostu nie powstal. Wykluczenia
   (`!`) wymagaja `--no-cone`.
2. **Plik niezmaterializowany NIE jest skasowany.** Po commicie w klonie bez `site/history/`
   drzewo nadal ma wszystkie 22 pliki archiwum — sprawdzone przed i po. Zasada 2 („nie usuwaj
   plikow z `history/`") jest wiec bezpieczna.
3. **Nowy plik w wykluczonym katalogu wymaga `git add --sparse`.** Zwykle `git add` odmawia
   z komunikatem o regulach rzadkosci. Przebieg, ktory przenosi wczorajsza strone do
   `site/history/RRRR-MM-DD-poranny.html`, robi wiec `git add --sparse <sciezka>`. Sprawdzone:
   commit przechodzi, archiwum rosnie z 22 do 23 plikow, nic nie ginie.

**Wszystkie cztery prompty klonuja tak samo.** Przebieg, ktory sklonuje repozytorium w calosci,
nie jest bledny — jest po prostu dziesiec razy wolniejszy i pisze o tym w odpowiedzi.

### Mapa Graph API idzie do `site/data/<data>.json` W CALOSCI — i to jest pomiar, nie wygoda

Planowalem 6 wrzesnia zapisywac tam tylko commit devx i dzienna delte, bo mapa ma 0,55 MB, a
`site/data/` juz wazy 38 MB. **Pomiar to obalil.** Dwa kolejne dni tej samej mapy, rozniace sie
czterema endpointami, w prawdziwym repozytorium git:

| | rozmiar pliku | przyrost `.git` po `gc` |
|---|---|---|
| dzien 1 | 546 546 B | 240 kB |
| dzien 2 | 546 556 B | **0 kB** |

Git pakuje ten plik delta wzgledem wczorajszego i **drugi dzien nie kosztuje nic**. Liczba „730 kB
dziennie" byla rozmiarem NIESKOMPRESOWANYM i nie opisywala kosztu w repozytorium.

Konsekwencja jest merytoryczna, nie tylko oszczednosciowa: **`diff_graphmap` porownuje dwa stany,
wiec wczorajszy plik danych MUSI niesc cala mape.** Gdyby niosl sama delte, wczorajszy stan bylby
pusty i kazdy endpoint wygladalby na dodany dzisiaj — czyli dokladnie ten falszywy alarm, przed
ktorym broni pozycja 42 listy §0.

## 5aj. Rejestr zmian z oknem 14 dni — bo diff pokazuje JEDEN dzien i potem znika

Wlasciciel zapytal 6 wrzesnia 2026: *„w kazdej zakladce jak cos zbieramy, to ja musze w jasny
i czytelny sposob widziec, co Microsoft zmienial, dodal itd., bo sie pogubie. Kiedy to realizuje
diff? Ale co jesli diff wlacze dzisiaj, pokaze on zmiany, a potem diff wlacze jutro? To juz tych
zmian nie zobacze? Moze jakos historie trzymac przez 14 dni?"*

Ma racje i to jest dziura, nie nieporozumienie. `/diff/` (§3) porownuje **dwa stany** i jego wyjscie
jest nadpisywane przy kazdym przebiegu. Zmiany z wczoraj zostaja wylacznie jako HTML
w `site/history/` — nie do przeszukania, nie do zsumowania, nie widoczne z zadnej zakladki briefu.
Czytelnik, ktory nie otworzyl `/diff/` we wtorek, we srode nie ma **zadnego** sposobu, zeby sie
dowiedziec, co sie we wtorek ruszylo.

**To jest ta sama choroba co §5z, §5ab i §5ac, tylko w osi czasu zamiast w osi progu:** dane sa,
prezentacja je gubi, bo kazdy widok pokazuje jedna chwile.

### Rejestr — `site/data/changelog.json`, DOPISYWANY, nigdy nadpisywany

```json
{"retentionDays":90, "pageWindowDays":14,
 "runs":[{"date":"2026-09-06","kind":"morning","at":"07:12","entries":23},
         {"date":"2026-09-05","kind":"morning","at":"07:09","entries":0}],
 "entries":[
   {"seen":"2026-09-06","tab":"Graph API","kind":"added","id":"IdentityDiagnostic.Read",
    "field":null,"before":null,"after":null,"product":"Graph","weight":1,"tier0":false,
    "msDate":"2026-02-21","url":"https://…","note":"Deployed in the service, not in this tenant"},
   {"seen":"2026-09-06","tab":"Deadlines","kind":"changed","id":"MC1448379",
    "field":"deadline","before":"2026-11-03","after":"2026-11-17","product":"Entra",
    "weight":1,"tier0":false,"msDate":"2026-09-05","url":"https://…"}
 ]}
```

- **`seen`** to data, w ktorej TEN raport wykryl zmiane. **`msDate`** to data Microsoftu, gdy
  istnieje, i `null`, gdy nie — te dwie daty nigdy sie nie zastepuja (§5q).
- **`tab`** wyliczasz tak samo jak w §3a (`TIER_TAB`), zeby wpis stanal w tej samej zakladce,
  w ktorej brief go renderuje. Jeden wpis na `(id, pole)`, nie jeden na pozycje.
- **`weight` i `tier0`** kopiujesz z pozycji stanu, zeby dalo sie filtrowac rejestr waga (§5p).
- **`runs`** to lista przebiegow, ktore do rejestru pisaly — z liczba wpisow, takze zerowa.
  **Bez niej „5 wrzesnia nic sie nie zmienilo" jest nieodroznialne od „5 wrzesnia przebieg nie
  wystartowal"**, a to jest dokladnie to rozroznienie, ktorego pilnuje `coverageByArea` w §7.

### Zasady

1. **Dopisywanie, nigdy edycja.** Wpis raz zapisany nie zmienia sie. Poprawka wczorajszego wpisu to
   NOWY wpis z `kind:"corrected"` i `note` mowiacym, co bylo i co jest — slownik z §8 C obowiazuje.
   Rejestr, ktory da sie przepisac, przestaje byc dowodem.
2. **`make_diff.py` jest jedynym pisarzem.** Ta sama funkcja, ktora liczy strone `/diff/`, dopisuje
   rejestr — flaga `--ledger site/data/changelog.json`. Dwa niezalezne liczenia tej samej rzeczy
   rozjezdzaja sie (§0a) i nie ma powodu powtarzac tego bledu.
3. **Deduplikacja po `(seen, tab, kind, id, field)`.** Przebieg popoludniowy i poranny tego samego
   dnia moga zobaczyc te sama zmiane; drugi jej nie dubluje. Ta sama pozycja zmieniona 1 i 3
   wrzesnia daje natomiast DWA wpisy — o to wlasnie chodzi.
4. **Przycinanie tylko po `retentionDays` (90).** Strona renderuje `pageWindowDays` (14). Oba
   numery sa wydrukowane, zeby czytelnik wiedzial, czego nie widzi.
5. **Przed dopisaniem przebieg kopiuje `changelog.json` do `changelog.prev.json`.** Bez tej kopii
   pozycja 47 nie ma z czym porownac i daje `BRAK „brak punktu odniesienia"`, nie OK. Kopia jest
   nadpisywana co przebieg i nie jest archiwum — archiwum jest sam rejestr.
6. **Rejestru nie da sie odtworzyc z niczego innego** — jest jedynym miejscem, gdzie zmiana
   z przeszlosci zyje po nadpisaniu `/diff/`. Przebieg, ktory go nie zapisal, mowi to w odpowiedzi
   jako `BRAK`, a nie milczy.

### Gdzie to widac

> **Od 7 wrzesnia 2026 wieczorem ten blok buduje SKRYPT 8 (§5al), a nie przebieg.** Markup ponizej
> zostaje jako opis tego, co ma powstac; rozniace sie od niego szczegoly — brak kolumny `Tab`
> wewnatrz wlasnej zakladki, podpisy obu osi wykresu, `+` przy kazdym wierszu — sa w §5al i to one
> obowiazuja. Przebieg wkleja do bloku stanu `ledger14` (okno `pageWindowDays` z `changelog.json`)
> i nie renderuje tej tabeli sam: dwa niezalezne renderowania tej samej rzeczy rozjezdzaja sie (§0a).

**W KAZDEJ zakladce tresciowej briefu**, jako pierwszy element pod `.panelhead`:

```html
<details class="chg14"><summary><span class="sm-t">What changed in the last 14 days</span>
<span class="badge t-acc">23 changes &middot; 9 days with a run</span></summary>
  <div class="daystrip">…jeden kafelek na dzien, wysokosc = liczba zmian…</div>
  <div class="tw"><table><thead><tr><th>Day</th><th>What</th><th>Item</th><th>Field</th>
  <th>Before &rarr; after</th><th>Source</th></tr></thead><tbody>…</tbody></table></div>
</details>
```

- **Zwiniete domyslnie, ale licznik jest w podpisie** — liczbe widac bez klikania, a tabela nie
  spycha tresci zakladki w dol. To ten sam ksztalt co lista endpointow w §5ah.
- **Filtrowane do TEJ zakladki.** Zakladka Graph API pokazuje zmiany katalogu Graph, Deadlines —
  ruchy terminow. Zakladka bez zmian pokazuje zdanie `No change recorded in the last 14 days;
  N runs looked.` — **zdanie z liczba przebiegow, nigdy pusty element**.
- **`<del>` i `<ins>`** w kolumnie `Before → after`, jak wszedzie indziej (§4).
- **Pasek dni** to `N` kafelkow, jeden na dzien okna: wysokosc to liczba zmian, dzien bez przebiegu
  ma kafelek pusty z obwodka przerywana i tytulem `no run`. Dzien z przebiegiem i zerem zmian ma
  kafelek plaski i tytul `checked, nothing moved`. **Trzy stany, trzy wyglady** — inaczej „zero"
  i „nie wiadomo" wygladaja tak samo.

**Na stronie `/diff/`** dochodzi sekcja `<section id="last14">` pod `bytab`: ten sam pasek dni dla
calego okna i jedna tabela ze wszystkich zakladek, `Day | Tab | What | Item | Field | Before → after`.
Dzieki niej otwarcie `/diff/` w dowolny dzien odpowiada na oba pytania naraz — „co sie zmienilo od
rana" i „co sie zmienilo przez dwa tygodnie".

**W pigulce naglowka** briefu: `<a class="count" href="#chg14"><b>N</b> changes in 14 days<span>&middot; M days with a run</span></a>`.

### Zmierzone

Rozmiar: dzien zmian to zwykle kilkanascie do kilkudziesieciu wpisow (zmierzone w §3: 6 wpisow
przy porownaniu ranek-wieczor, 34 przy porownaniu dwoch dni, 157 przy porownaniu z 31 sierpnia).
Rejestr 90-dniowy przy sredniej 30 wpisow dziennie to okolo 2 700 wpisow, **okolo 700 kB surowo
i 40 kB gzip** — mniej niz jeden dzien `site/data/*.json`. Renderowane okno 14 dni to okolo
420 wierszy rozdzielonych na dziesiec zakladek.

### Walidator — pozycje 45-47 listy §0

- **45** — `site/data/changelog.json` istnieje, ma `runs` z wpisem na DZISIEJSZY przebieg (takze
  gdy zmian bylo zero) i zaden wpis nie jest starszy niz `retentionDays`.
- **46** — kazda zakladka tresciowa ma `details.chg14`, ktorego licznik w podpisie rowna sie
  liczbie wierszy w srodku; zakladka bez zmian ma zdanie z liczba przebiegow, nie pusty element.
- **47** — **rejestr nie zostal przepisany**: wpisy o dacie wczesniejszej niz dzisiejsza sa
  identyczne co do bajtu z tymi z poprzedniego przebiegu. Roznica znaczy, ze przebieg edytowal
  historie, i jest **przebiegiem NIEUDANYM**. Bramka porownuje z kopia z `site/data/` sprzed
  commita; przy pierwszym przebiegu pozycja daje `BRAK „brak punktu odniesienia"`, nie OK.

## 5al. Roles i Graph API to JEDEN uklad — i historia otwiera sie w ten sam panel

Wlasciciel zatwierdzil 7 wrzesnia 2026 podglad v16 i powiedzial wprost: *„doklanide taki sam
layout i sposob zbierania i wyswietlania danych"*. Ta sekcja jest tym ukladem zapisanym KODEM,
a nie opisem — bo lekcja z 7 wrzesnia (§5ak) brzmi: **wlasciciel zatwierdza uklad, a specyfikacja,
ktora niesie opis zamiast kodu, produkuje cos innego.** Dlatego SKRYPT 7 i SKRYPT 8 sa tu w calosci
i kopiuje sie je co do bajtu, tak samo jak skrypty 4, 5 i 6.

### Cztery punkty wlasciciela z 7 wrzesnia i przyczyna kazdego

| zgloszenie | przyczyna | naprawa |
|---|---|---|
| „nie wiem co jest na osi x a co y" | pasek dni nie mial ZADNEGO podpisu osi, a `preserveAspectRatio="none"` rozciagalo napisy | obie osie podpisane NA rysunku, zdanie „How to read this" nad nim, liczba na kazdym slupku, `viewBox` 1200x250 bez rozciagania |
| „w roles sekcja 14 dni na dole, a w graph api na gorze" | gore obu zakladek budowaly dwa rozne kawalki kodu | **JEDNA funkcja buduje gore OBU zakladek**: kafelki, zwiniete wyliczenie, historia. Pozycja wynika z konstrukcji, nie ze starannosci |
| „jak nacisne + to powinienem miec taki sam widok jak w panelu" (Graph API) | historia byla tabela tekstowa bez zwiazku z katalogiem | `+` **prosi KATALOG o panel** i klonuje to, co katalog wyrenderowal — nie drugi render tych samych danych, tylko ten sam |
| „ten sam + ze szczegolami dla rol" | panelu roli w ogole nie bylo — czytelnik widzial render powloki | SKRYPT 7 buduje panel roli w tym samym ksztalcie co panel uprawnienia |

### Kolejnosc sekcji w OBU panelach — wiazaca

1. **At a glance**
2. **What changed on this &lt;role|permission&gt; in the last 14 days**
3. tresc wydawcy: `Published by Microsoft` (uprawnienie) albo `What Microsoft says this role is for` (rola)
4. zwijana lista: `What this permission can call` albo `What this role can do`
5. derywacja: `Entra roles that can do this` albo `Graph permissions this role covers`

Pozycja druga jest wiazaca i jest odpowiedzia na punkt 2 — **to jest pozycja, nie preferencja.**
Sekcje 14 dni buduje SKRYPT 8 (`window.__socHistSection`), a skrypty 6 i 7 tylko ja wstawiaja:
jeden pisarz, dwa czytania, wiec nie da sie ich rozjechac (ta sama zasada co `--ledger` w §5aj).

### Kontrakt danych — `ledger14` w bloku `soc-brief-state`

Przebieg wycina z `site/data/changelog.json` (§5aj) okno `pageWindowDays` i wkleja je do bloku stanu:

```json
"ledger14":{"retentionDays":90,"pageWindowDays":14,
  "runs":[{"date":"2026-09-07","kind":"morning","at":"07:12","entries":23}],
  "entries":[{"seen":"2026-09-07","tab":"Graph API","kind":"changed","id":"User.Read",
              "field":"endpoints","before":null,"after":"+3",
              "detail":"endpoint added: GET /users/{id}/manager, …"}]}
```

**Trzeciego bloku JSON NIE dokladasz** — bramka lustra (§0a) zada dokladnie dwoch i trzeci wywraca
caly przebieg. `ledger14` jest kluczem w istniejacym bloku stanu, tak samo jak `graphMap` (§5ah).

Trzy reguly ksztaltu, kazda z bledu zmierzonego 7 wrzesnia 2026:

- **`id` to PRZEDMIOT zmiany, nigdy zdanie.** W rejestrze z tego dnia stalo
  `"id": "AuditLog.Read.All → 1 new endpoint"`, wiec zaden kod nie mogl powiazac wiersza z wpisem
  katalogu. Przedmiot idzie do `id`, pole do `field`, wartosci do `before`/`after`, przyklady do
  `detail`.
- **Rejestr trzyma ZNAKI, nie encje HTML.** `&mdash;` zapisane w danych wraca potem w kazdym widoku,
  ktory je czyta. `make_diff.py` normalizuje je przy zapisie (§3).
- **Ruch endpointow dopisuje sie PER UPRAWNIENIE**: `field:"endpoints"`, `after:"+41"`, trzy przyklady
  w `detail`. Jeden wpis na endpoint dawal **9 736 wierszy** pierwszego dnia z mapa; panel uprawnienia
  i tak wymienia wszystkie endpointy, wiec liczba plus przyklady odpowiadaja na to samo pytanie.

Wpis bez `id` (baseline) **nie dostaje przycisku `+`** — nie ma czego otwierac, i to tez jest wynik.

### Migracja przy odczycie — stary rejestr nie unieważnia nowej reguły

Rejestr zapisany PRZED ta poprawka wozi wpisy w starym ksztalcie. Zmierzone w repozytorium
7 wrzesnia 2026 wieczorem: `site/data/changelog.json` ma **73 wpisy, z tego 33 ze zdaniem w polu
`id`** (`"AuditLog.Read.All → 1 new endpoint"`) i jeden z encja `&mdash;`. §5aj zabrania
przepisywania historii, a pozycja 47 listy §0 sprawdza to co do bajtu — wiec **pliku sie nie rusza**.

**Przebieg naprawia to przy ODCZYCIE, gdy wycina okno do `ledger14`:**

```python
def norm_entry(e):
    """Stary wpis -> nowy ksztalt. Plik zrodlowy zostaje nietkniety."""
    ENT = (("&mdash;", "\u2014"), ("&rarr;", "\u2192"), ("&minus;", "\u2212"),
           ("&middot;", "\u00b7"), ("&amp;", "&"))
    e = dict(e)
    for k, v in list(e.items()):
        if isinstance(v, str):
            for a, b in ENT: v = v.replace(a, b)
            e[k] = v
    iid = e.get("id") or ""
    if "\u2192" in iid:                      # "X → 1 new endpoint"
        head, tail = [x.strip() for x in iid.split("\u2192", 1)]
        e["id"] = head
        if not e.get("field"): e["field"] = "endpoints"
        if not e.get("after"):
            m = re.match(r"(\d+)", tail)
            e["after"] = ("+" + m.group(1)) if m else tail
        e["detail"] = e.get("detail") or tail
    return e
```

Dzieki temu pozycja 50 listy §0 jest zielona od pierwszego przebiegu po zmianie, a historia
w pliku zostaje taka, jaka byla — bo to sa dwa rozne pytania: „czy strona niesie czyste dane"
i „czy przebieg przepisal przeszlosc".

### Gora zakladki — identyczna w Roles i w Graph API

`kafelki liczbowe` → `zwiniete wyliczenie` → `historia 14 dni (otwarta)` → tresc zakladki.
Kafelki licza sie ZE STANU, nigdy nie sa wpisywane, a **licznik wiodacy musi byc ten sam, co pokazuje
reszta strony**: 7 wrzesnia kafelek mowil „139 roles tracked" tuz pod pigulka powloki „137", i to jest
dokladnie to „jak moze byc 137 of 136", o ktore wlasciciel pytal 5 wrzesnia. Zwiniete wyliczenie
drukuje cala arytmetyke:

```
136  ról na opublikowanej referencji Microsoftu
 +3  dopisane przez ten brief (nazwane z imienia)
=139 rekordow trzymanych tutaj
 -2  trzymane, ale poza licznikiem inwentarza (nazwane z imienia)
=137 liczone w katalogu i na plakietce zakladki
```

### Wiersz historii otwiera panel — jak dokladnie

`+` wola `window.__socOpenPerm(nazwa)` albo `window.__socOpenRole(nazwa)`, ktore **klikaja wpis
w katalogu** i zwracaja `.cat-detail-inner`; SKRYPT 8 klonuje ten wezel, usuwa z klonu jego wlasna
sekcje 14 dni (inaczej historia zawieralaby historie) i wstawia go pod wierszem. Nazwa, ktorej
katalog dzis nie ma, daje **zdanie**, nie pusty box: *„named in the ledger but carries no entry in the
catalog as it stands today"* — to jest znalezisko, nie brak.

Zakladki, ktore nie maja katalogu (New, Deadlines, Component versions), dostaja zamiast `+` strzalke
`↗`, ktora przewija do wiersza `[data-id]` na stronie (§5ac gwarantuje, ze taki wiersz istnieje).

### Gleboki link ze strony zmian

Strona `/diff/` z zalozenia nie ma katalogu (§3), wiec nie otworzy panelu u siebie — ale wskazuje na
niego. Skrypty 6 i 7 czytaja kotwice **`#graph:perm=<nazwa>`** i **`#roles:role=<nazwa>`** (wartosc
zakodowana procentowo) i zaznaczaja ten wpis po zaladowaniu oraz przy `hashchange`. `make_diff.py`
dopisuje te kotwice do kazdego wiersza sekcji `catalog`, a jego `verify()` tego pilnuje.

### Wyszukiwanie w zakladce Roles — trzy rodzaje zapytania, i to, czego NIE da sie zrobic

Pole przyjmuje **nazwe roli**, **akcje katalogowa** (`microsoft.directory/...`) i **template ID**, i za
kazdym razem MOWI, ktora przestrzen nazw dopasowalo. Obok pola stoi `Exact match`, a nad nim rzad
KLIKALNYCH przykladow (placeholder z czterema mozliwosciami jest na telefonie obcinany).

**Dwie rzeczy zmierzone tego dnia, obie wiazace:**

1. **O widocznosc wpisu w liscie powloki NIE walczy sie atrybutem `hidden`.** Powloka filtruje ta sama
   liste po nazwie i robi to PO nas: przy zapytaniu `administrator` `apply()` wykonalo sie **ponad 200
   razy** i zablokowalo watek strony. `Exact match` wyraza sie wiec REGULA w arkuszu
   (`<style id="s7filter">`), ktora przezywa przerysowanie listy i nie ma z czym walczyc.
2. **Akcja katalogowa nie ma odpowiedzi w liscie, bo powloka PRZEBUDOWUJE liste z nazw** i zostawia
   w DOM zero wpisow. Odpowiedzia jest wiec NOTA, ktora nazywa znalezione role, a **kazda nazwa jest
   przyciskiem otwierajacym te role** — ta sama zasada co nota przy sciezce w §5ah.

### Co dokladnie robia skrypty 7 i 8 z panelami powloki

**Ukrywaja, nigdy nie usuwaja.** SKRYPT 7 chowa panele powloki `At a glance`, `What this role is for`
i `Directory actions`; reszta panelu roli (`What Microsoft changed`, `Version history`,
`Not published by Microsoft`, `Sources`) zostaje nietknieta pod spodem. **Lista dozwolonych zmian
w trzech skryptach powloki sie NIE zmienia** — nadal sa to `KIND_BADGE` (§5e) i trzy linie
`facetCandidates()` (§5w).

### Zmierzone 7 wrzesnia 2026 na OPUBLIKOWANEJ stronie

Skrypty 6 (v16), 7 i 8 plus arkusz wstrzykniete w plik z tego dnia, render headless, oba motywy,
1500 / 1280 / 760 / 390 px, **kazda z dziesieciu zakladek po kolei, z rozwinietym wierszem historii**:

| co | wynik |
|---|---|
| bledy konsoli i strony | **0** |
| `documentElement.scrollWidth === clientWidth` | wszedzie |
| elementy szersze od rodzica | **0** — dwa znalezione tego dnia (`<dt>` 319>298 w Roles, chip linku 294>237 w Component versions) sa STARSZE niz ta sekcja i zostaly przy okazji poprawione |
| sekcja 14 dni | w kazdej z pieciu zakladek tresciowych, na tej samej pozycji |
| Roles: 11 zmian / 10 przyciskow `+` / 7 kafelkow · Graph API: 40 zmian / 39 przyciskow `+` / 5 kafelkow | zgodne z rejestrem |
| panel roli | `At a glance` · `14 dni` · `What Microsoft says` · `99 directory actions` w 8 chipach filtra · `25` wierszy pokrycia Graph |
| panel uprawnienia | ta sama kolejnosc, `User.Read.All` 215 endpointow |
| `+` w Graph API na trzech roznych wierszach | 28 / 85 / 179 endpointow — trzy rozne panele, nie trzy kopie jednego |
| `+` w Roles na trzech roznych wierszach | 1 / 81 / 99 akcji katalogowych |
| `Exact match` | `administrator` 96 wpisow, z `Exact match` **0** (zadna rola nie nazywa sie tak doslownie); `User Administrator` 2 → **1** |
| akcja `microsoft.directory/users/inviteGuest` | nota nazywa **3 role**, kazda jako przycisk; klikniecie otwiera panel i przywraca pelna liste 137 |
| gleboki link | `#graph:perm=User.Read.All` → panel z 215 endpointami; `#roles:role=Global%20Reader` → panel z 99 akcjami |

### Siedem rzeczy zmierzonych po PIERWSZYM podgladzie — i one sa cala roznica

Wlasciciel obejrzal podglad calego portalu i powiedzial: *„layout sie nie zgadza … lewy pasek
zupelnie inny, sposob przedstawiania szczegolow tak samo, a mialo byc wszystko 1:1"*. Mial racje
w kazdym punkcie, a przyczyny sa mechaniczne, nie gustowe. Kazda z nich jest tu zapisana, bo kazda
wroci przy nastepnym skrypcie.

1. **Nazwa klasy, ktora arkusz JUZ ZNA, po cichu przejmuje twoj element.** `details.rank`
   dziedziczylo `display:inline-flex` po istniejacej w powloce klasie `.rank` (chip rankingu):
   blok mial 20 px wysokosci, jego wlasna tabela renderowala sie POZA nim i nachodzila na katalog,
   a dokument rozpychal sie do 1 599 px przy oknie 1 500. Klasa nazywa sie teraz `rolerank`.
   To jest bliznie podobne do `.tabn` z §5ae, tylko odwrotnie: tam celowalem w klase, ktorej NIE MA,
   tu uzylem klasy, ktora JEST. **Przed napisaniem selektora sprawdzasz w arkuszu powloki OBIE
   rzeczy: czy klasa istnieje i czy nie istnieje.**
2. **Powierzchnie wpisu rozstrzygaja DANE, nie prefiks `data-id`.** `perm-` istnieje w tym katalogu,
   ale obok niego stoja bare nazwy i identyfikatory encji; brama `id.indexOf("perm-") === 0`
   odrzucala **wiekszosc** wpisow, wiec panel v13 dostawala garstka, a reszta zostawala przy
   renderze powloki — i to jest dokladnie „sposob przedstawiania szczegolow tak samo". Skrypt 6
   czyta teraz `surface` / `API` z tego, co powloka wyrenderowala. Pulapka dwoch powierzchni
   (SharePoint `Sites.Selected` kontra Graph) zostaje zamknieta, tylko po danych.
3. **Panel powstaje dla KAZDEGO wpisu.** Wpis bez wpisu w mapie (poprawka katalogu, nazwa spoza
   `permissions.json`) dostaje ten sam uklad i ZDANIE w miejscu listy endpointow: *„permissions.json
   carries no pathSet for this name at commit …"*. Milczenie dawaloby dwa rozne uklady w jednej
   zakladce.
4. **Naglowek powloki chowa sie, gdy panel go zastepuje.** `.cat-head` niesie te sama nazwe i te
   same chipy co naglowek panelu — wlasciciel zobaczyl tytul wydrukowany dwa razy.
5. **Lista katalogu jest JEDNA karta z wloskowatymi liniami, kolumna ma 300 px.** Powloka rysuje
   stos osobnych pudelek z lewym paskiem; podglad v16 ma jedna karte. To jest ten „zupelnie inny
   lewy pasek" i naprawia to piec regul CSS, bez dotykania skryptu 3.
6. **Tytul panelu nie jest ozdoba.** Powloka nadaje `h2` w sekcji `text-transform:uppercase`,
   `letter-spacing:1.5px` i 12,5 px, przez co `User.Read.All` czytalo sie jako `USER.READ.ALL`.
   Nazwa uprawnienia jest napisem, ktory sie kopiuje — 17 px, bez transformacji, monospace tylko
   dla uprawnienia.
7. **Ta sama liczba nie stoi dwa razy pod soba.** `.panelhead` powloki drukuje `137 roles in the
   catalog` i moj kafelek drukowal to samo. Kafelek, ktorego etykiete I wartosc panel juz niesie,
   jest pomijany — porownanie idzie po wyrenderowanym tekscie, wiec dopasowuje sie samo.

**Osma rzecz jest o tabeli, nie o skrypcie.** Sekcja Roles otwierala sie tabela dwudziestu rol pod
golym „Search 20 rows…", z dwoma selektami `All of those, whole resource` i `All dominant depth` —
powloka buduje fasete z NAGLOWKA KOLUMNY, a faseta na kolumnie liczbowej nie grupuje niczego
(§5s, ta sama choroba co wykres samych jedynek). Tabela jest wartosciowa; nic nie mowilo, czym
jest. SKRYPT 7 **nazywa ja, mowi jednym zdaniem co szereguje, zwija ja i stawia tuz nad katalogiem**,
zabiera do srodka jej pasek i note, chowa fasete liczbowa i nadaje drugiej nazwe `All depth`.
Przy okazji **podpis zwiniety w polowie zdania** (powloka tnie na 88 znakach, wiec czytelnik
widzial „Recounted in…") dostaje pierwsze PELNE zdanie z tresci.

### Dlaczego podglad i portal rozjezdzaly sie po raz drugi — regula procesu

Wlasciciel zapytal 7 wrzesnia wieczorem: *„jak my dzialamy, podajesz mi jakis layout, ktorego
potem nie potrafisz zaimplementowac do naszych sched tasks i routines?"*. Pytanie jest sluszne
i odpowiedz jest jedna, moja: **v16 powstal jako STRONA SAMODZIELNA, w ktorej sam pisalem kazdy
element. Portal renderuje te dwie zakladki SKRYPTEM 3 powloki, ktorego §5w zabrania edytowac.**
Makieta, ktora nie stoi na prawdziwym DOM, zawsze bedzie sie roznic — i roznica nie byla w panelu
(ten dalo sie odtworzyc co do sekcji), tylko w tym, czego makieta nie miala, a powloka rysuje:
pasek trybow i okien czasu, piec selektow oraz chipy przy wpisach listy.

**Regula, ktora z tego wynika i ktora obowiazuje od teraz:**

> **Podglad ukladu robi sie przez WSTRZYKNIECIE do kopii opublikowanej strony, nigdy jako osobny
> plik.** Wtedy to, co wlasciciel zatwierdza, jest dokladnie tym, co pojdzie na produkcje, a roznice
> miedzy makieta a portalem nie maja gdzie powstac. Plik `/tmp/s7/test.html` z tego dnia jest
> wzorcem takiego podgladu: opublikowana strona + arkusz §5al + skrypty 6, 7 i 8.

To jest ta sama lekcja co §5ak („wlasciciel zatwierdza uklad, a specyfikacja z opisem zamiast kodu
produkuje cos innego"), o jeden poziom wyzej: **kod bez prawdziwego otoczenia tez jest opisem.**

### Co robimy z paskiem filtrow powloki — decyzja wlasciciela z 7 wrzesnia

Powloka rysuje w obu katalogach trzy przyciski trybu (`Microsoft changes`, `Catalog notes`, `All`),
szesc przyciskow okna czasu i do pieciu selektow. v16 nie ma ich wcale, ale **one robia prawdziwa
robote** — `Microsoft changes 449` to filtr, o ktory wlasciciel sam prosil. Nie kasujemy ich wiec,
tylko **skladamy pod `<details class="morefilters">`**, jedna funkcja SKRYPTU 8 dla obu zakladek,
zeby nie mogly sie rozjechac. Na wierzchu zostaje dokladnie v16: rzad klikalnych przykladow,
zielone pole, `Exact match`, licznik.

**Pionowy pasek listy tez jest kontraktem, nie ozdoba.** Powloka pisze przy wpisie rodzaj zmiany
i date; v16 pisze to, miedzy czym czytelnik wybiera. Chipy sa wiec liczone ze stanu:

| katalog | chipy przy wpisie |
|---|---|
| Roles | `PRIV` (gdy Microsoft tak oznacza) · `N actions` albo `no actions table` · `N perms` (pokrycie Graph) |
| Graph API | schematy z mapy: `DelegatedWork`, `Application`, `DelegatedPersonal` |

Wiersz chipow powloki jest **chowany, nigdy usuwany**, a nasz dokladany; liste powloka przerysowuje
przy kazdym filtrze, wiec dekoracja wraca po kazdym renderze, pod strazą flagi — inaczej dwa
obserwatory goniłyby sie nawzajem (§5al, ta sama pulapka co `Exact match` w Roles).

**Chip w pasku listy jest SAMODZIELNY, nie pozycza sie od powloki.** Zmierzone 7 wrzesnia wieczorem
na moim wlasnym podgladzie: powloka deklaruje `.badge` bez tla, z `border-radius:3px` i
`text-transform:uppercase`, a kolory `t-grey`/`t-bad`/`t-info` zyja **tylko pod `.v13pane`** — moje
chipy wyszly wiec jako czarny, wersalikowy tekst bez ramki, i wlasciciel zobaczyl to od razu.
Regula `.catalog .cat-item .ci-v16 .badge` niesie wlasne tlo, promien 999 px, wage i brak wersalikow,
w obu motywach. **Wpis, ktorego nie ma w mapie Microsoftu, tez dostaje NASZE chipy** przepisane
z tego, co powloka o nim wie — lista mowiaca dwoma jezykami wizualnymi jest dokladnie tym, na co
wlasciciel wskazywal trzy razy z rzedu.

**Nazwa wpisu jest w foncie tekstowym, nie monospace**, a pole szukania mowi `Search permissions` /
`Search roles` zamiast `Search 1076 entries by name, API, entity or impact…` — powloka nadpisuje ten
placeholder przy kazdym renderze, wiec ustawia sie go w tym samym obserwatorze.

### Cztery rodzaje zapytania w zakladce Graph API — dopiero teraz sa PRAWDZIWE

§5ah obiecywala je od 6 wrzesnia, a SKRYPT 6 mial tylko `Exact match`: chip zapowiadajacy szukanie
po endpoincie, ktore nic nie robi, jest gorszy niz brak chipa. Zmierzone po dolozeniu:

| wpisane | odpowiedz |
|---|---|
| `/users/{id}/manager` | *„1 path match, reachable with 6 permissions"* + kazda nazwa jako przycisk otwierajacy panel |
| `e1fe6dd8-ba31-4d61-89e7-88639da4683d` | *„That permission ID belongs to User.Read · DelegatedWork"* + przycisk |
| `microsoft.directory/users/inviteGuest` | *„That is an Entra directory action, not a Graph endpoint — 3 roles carry it: Directory Writers, Guest Inviter, User Administrator"* |
| `User.Read.All` | zwykle zawezenie listy, `3 of 1076` |

Indeks sciezek budowany jest **leniwie, przy pierwszym zapytaniu zaczynajacym sie od `/`** —
dekodowanie 24 099 par dla 923 uprawnien na starcie strony byloby zmarnowana sekunda dla kazdego,
kto po endpoincie nie szuka.

### Arkusz — blok dopisywany na koncu `<style>`

Razem z blokami z §1a, §5e, §5k, §5t, §5w, §5x, §5y, §5ad, §5ae i §5ak sa to JEDYNE dozwolone
dopisane reguly CSS. Kazdy selektor zaczyna sie od klasy, ktora tworzy wylacznie skrypt 7 albo 8,
albo od `.v13pane` — nic stad nie wycieka na reszte strony. Zmienne sa te, ktore arkusz juz
deklaruje (§5t).

```css
/* §5al — the top of a content tab (counts, the arithmetic, the last 14 days) and
   the role panel in the same shape as the permission panel. Every selector starts
   from a class only SCRIPT 7 or SCRIPT 8 creates, or from `.v13pane`, so nothing
   here leaks onto the rest of the page. Variables are the ones the sheet already
   declares (§5t): `--surface-2`, never `--surface2`. */
.s8top{margin:0 0 18px}
.s8top .factgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:8px;margin:0 0 12px}
.s8top .fact{border:1px solid var(--border);border-radius:10px;background:var(--surface);padding:9px 12px}
.s8top .fact b{display:block;font-size:21px;line-height:1.15;font-variant-numeric:tabular-nums}
.s8top .fact span{display:block;font-size:11.5px;text-transform:uppercase;letter-spacing:.05em;
 color:var(--muted);font-weight:700;margin-top:2px}
.s8top .fact.acc b{color:var(--accent)}.s8top .fact.ok b{color:var(--ok)}
.s8top .fact.bad b{color:var(--bad)}.s8top .fact.warn b{color:var(--warn)}.s8top .fact.info b{color:var(--info)}
details.sumfold{border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:10px;
 background:var(--surface);margin:0 0 12px;font-size:13.5px}
details.sumfold>summary{list-style:none;cursor:pointer;padding:9px 13px;display:flex;gap:10px;align-items:center}
details.sumfold>summary::-webkit-details-marker{display:none}
details.sumfold>summary::before{content:"+";font-family:var(--mono);font-weight:700;width:20px;height:20px;
 flex:0 0 20px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;
 background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
details.sumfold[open]>summary::before{content:"−"}
details.sumfold .sum{padding:0 13px 11px;font-size:13px}
details.sumfold .sum table{border-collapse:collapse;margin:0}
details.sumfold .sum td{padding:2px 14px 2px 0;border:0}
details.sumfold .sum td:first-child{font-variant-numeric:tabular-nums;font-weight:700;text-align:right;min-width:52px}
/* ---- the 14-day block ---- */
details.chg14{border:1px solid var(--border);border-radius:12px;background:var(--surface);margin:0 0 14px}
details.chg14>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:12px 16px}
details.chg14>summary::-webkit-details-marker{display:none}
details.chg14>summary::before{content:"+";font-family:var(--mono);font-size:15px;font-weight:700;width:22px;
 height:22px;flex:0 0 22px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;
 background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
details.chg14[open]>summary::before{content:"−"}
details.chg14>summary .sm-t{font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;font-weight:700;color:var(--muted)}
details.chg14>summary .sm-r{font-size:12.5px;color:var(--muted)}
details.chg14>*{margin-left:16px;margin-right:16px}
details.chg14>summary{margin:0}
details.chg14>.tw{margin-bottom:14px}
.howto{background:var(--surface-2);border:1px solid var(--border);border-left:4px solid var(--accent);
 border-radius:10px;padding:9px 12px;font-size:13px;color:var(--text);margin:12px 0 0}
.chartwrap{margin:12px 0 6px;overflow-x:auto}
.chartwrap svg{display:block;width:100%;min-width:900px;height:auto}
.chartwrap .b-chg{fill:var(--accent)}
.chartwrap .b-quiet{fill:var(--grey-soft);stroke:var(--border)}
.chartwrap .b-norun{fill:none;stroke:var(--border);stroke-dasharray:3 3}
.chartwrap .trend{fill:none;stroke:var(--warn);stroke-width:2.5;vector-effect:non-scaling-stroke;
 stroke-linejoin:round;stroke-linecap:round}
.chartwrap .gl{stroke:var(--border);stroke-width:1;vector-effect:non-scaling-stroke}
.chartwrap .ax{fill:var(--muted);font-size:13px;font-family:var(--sans)}
.chartwrap .axt{fill:var(--muted);font-size:13px;font-weight:700;font-family:var(--sans);
 letter-spacing:.04em;text-transform:uppercase}
details.chg14 .legend{display:flex;gap:14px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin:4px 0 10px}
details.chg14 .legend i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;vertical-align:-1px}
details.chg14 .legend i.k-chg{background:var(--accent)}
details.chg14 .legend i.k-quiet{background:var(--grey-soft);box-shadow:inset 0 0 0 1px var(--border)}
details.chg14 .legend i.k-norun{background:transparent;box-shadow:inset 0 0 0 1px var(--border)}
details.chg14 .legend i.k-trend{background:var(--warn);height:3px;border-radius:2px;margin-bottom:3px}
/* ---- a history row opens the real panel ---- */
td.xc{width:34px;padding-left:8px;padding-right:0}
.xb{font:inherit;font-family:var(--mono);font-size:14px;font-weight:700;width:24px;height:24px;line-height:1;
 display:inline-flex;align-items:center;justify-content:center;border-radius:6px;background:var(--accent-soft);
 color:var(--accent);border:1px solid var(--accent);cursor:pointer;padding:0;text-decoration:none}
.xb:hover{background:var(--accent);color:var(--surface)}
.xn{color:var(--muted)}
tr.hrow[aria-expanded=true]>td{background:var(--accent-soft)}
tr.hdet>td{padding:0;background:var(--surface-2);box-shadow:inset 3px 0 0 var(--accent)}
.hd-in{padding:12px 14px}
.hd-in .cat-detail-inner.embed{background:none;padding:0;border:0}
.hd-in .v13pane{margin:0}
.hd-lead{font-size:12px;color:var(--muted);margin:0 0 9px;text-transform:uppercase;letter-spacing:.05em;font-weight:700}
.s8flash{outline:3px solid var(--accent);outline-offset:-3px}
/* ---- the roles search: examples you can click, and Exact match ---- */
.s7tips{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin:0 0 9px}
.s7tips .lab{font-size:11px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;color:var(--muted)}
.s7tips button{font:inherit;font-size:12px;font-family:var(--mono);padding:4px 10px;border-radius:999px;
 border:1px solid var(--border);background:var(--surface);color:var(--accent);cursor:pointer}
.s7tips button b{font-family:var(--sans);color:var(--muted);font-weight:700;margin-right:6px}
label.s7exact{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:600;color:var(--text);
 white-space:nowrap;margin-left:10px;cursor:pointer}
p.s7why{background:var(--info-soft);border:1px solid var(--info);color:var(--text);border-radius:9px;
 padding:8px 12px;font-size:13px;margin:0 0 10px}
p.s7why[hidden]{display:none!important}
/* the role panel reuses the permission panel's own rules; only the action cell differs */
.v13role td.act code{font-family:var(--mono);font-size:12px;white-space:nowrap;display:inline-block}
.v13role td.act .what{color:var(--muted);font-size:12.5px;margin-top:2px;white-space:normal}
.v13role .rname{font-family:var(--sans);font-weight:600;min-width:150px}
@media (max-width:760px){
  details.chg14>summary,details.sumfold>summary{flex-wrap:wrap}
  details.chg14>summary .badge{white-space:nowrap}
  details.chg14>summary .sm-t{flex:1 1 100%}
  details.chg14>*{margin-left:11px;margin-right:11px}
  .s7tips button{white-space:normal;text-align:left;max-width:100%}
}
.s7hits{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 0}
.s7hits button{font:inherit;font-size:12.5px;font-weight:600;padding:4px 11px;border-radius:999px;
 border:1px solid var(--accent);background:var(--surface);color:var(--accent);cursor:pointer}
.s7hits button:hover{background:var(--accent);color:var(--surface)}
/* Two overflows measured on the published page of 7 September 2026, both older
   than this section and both a plain §5x break: the shell's `not published` list
   in the Roles tab pushed a 319 px <dt> into a 298 px column at 390, and a link
   chip in Component versions ran 294 px in a 237 px cell at 1280. Neither is
   caused by scripts 7 and 8; both are fixed here because the rule that forbids
   them is ours. */
.catalog dl dt,.catalog dl dd{min-width:0;overflow-wrap:anywhere}
#tab-components .sec-body a.lnk,#tab-components .sec-body a[href^="http"]{white-space:normal;overflow-wrap:anywhere}
/* ---- v16 1:1: lista katalogu jest JEDNA karta z wloskowatymi liniami, a nie
   stosem pudelek; szerokosc kolumny i promienie jak w podgladzie v16. ---- */
.catalog .cat-split{grid-template-columns:300px minmax(0,1fr)}
.catalog .cat-list{gap:0;border:1px solid var(--border);border-radius:12px;background:var(--surface);
 padding:0;overflow:auto}
.catalog .cat-item{border:0;border-bottom:1px solid var(--border);border-left:0;border-radius:0;
 background:none;padding:9px 12px;gap:4px}
.catalog .cat-item:last-child{border-bottom:0}
.catalog .cat-item[aria-selected="true"]{background:var(--accent-soft);box-shadow:inset 3px 0 0 var(--accent)}
.catalog .ci-name{font-size:13px;font-weight:700;line-height:1.3}
.catalog .cat-detail{border-radius:12px}
@media (max-width:999px){.catalog .cat-split{grid-template-columns:minmax(0,1fr)}}
/* ---- ranking rol: nazwany, zwiniety, pod historia ---- */
details.rolerank{border:1px solid var(--border);border-radius:12px;background:var(--surface);margin:0 0 14px}
details.rolerank>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:12px 16px}
details.rolerank>summary::-webkit-details-marker{display:none}
details.rolerank>summary::before{content:"+";font-family:var(--mono);font-size:15px;font-weight:700;width:22px;
 height:22px;flex:0 0 22px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;
 background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
details.rolerank[open]>summary::before{content:"−"}
details.rolerank>summary .sm-t{font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;font-weight:700;color:var(--muted)}
details.rolerank>*{margin-left:16px;margin-right:16px}
details.rolerank>summary{margin:0}
details.rolerank>.tw{margin-bottom:14px}
/* Tytul panelu: powloka nadaje `h2` w sekcji `text-transform:uppercase`,
   `letter-spacing:1.5px` i 12,5 px — zmierzone 7 wrzesnia 2026, przez co
   `User.Read.All` czytalo sie jako `USER.READ.ALL`, a nazwa uprawnienia jest
   napisem, ktory sie kopiuje, nie naglowkiem ozdobnym. Podglad v16 ma ja
   zapisana tak, jak brzmi. */
.catalog .cat-detail .v13pane>header h2{font-size:17px;text-transform:none;letter-spacing:0;
 line-height:1.25;margin:0 0 7px;color:var(--text);font-weight:700}
.catalog .cat-detail .v13pane.v13role>header h2{font-family:var(--sans)}
.catalog .cat-detail .v13pane>header h2.mono{font-family:var(--mono)}
/* ---- v16 1:1: pionowy pasek listy i schowany pasek filtrow powloki ---- */
.catalog .ci-name{font-family:var(--sans);font-weight:700;font-size:13px}
.catalog .cat-item .ci-v16{display:flex;gap:5px;flex-wrap:wrap;margin-top:4px}
.catalog .cat-item .ci-meta[hidden]{display:none!important}
details.morefilters{margin:8px 0 0;border:1px solid var(--border);border-radius:10px;background:var(--surface)}
details.morefilters>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;
 padding:8px 12px;flex-wrap:wrap}
details.morefilters>summary::-webkit-details-marker{display:none}
details.morefilters>summary::before{content:"+";font-family:var(--mono);font-weight:700;width:20px;height:20px;
 flex:0 0 20px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;
 background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
details.morefilters[open]>summary::before{content:"−"}
details.morefilters>summary .sm-t{font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;
 font-weight:700;color:var(--muted)}
details.morefilters>summary .sm-r{font-size:12.5px;color:var(--muted)}
details.morefilters>.cat-toolbar{margin:0 12px 12px}
/* Chipy w pionowym pasku listy sa SAMODZIELNE. Zmierzone 7 wrzesnia 2026: powloka
   deklaruje `.badge` bez tla, z `border-radius:3px` i `text-transform:uppercase`,
   a kolory (`t-grey`, `t-bad`, `t-info`) zyja tylko pod `.v13pane` — moje chipy
   wychodzily wiec jako czarny, wersalikowy tekst bez ramki. Ta regula nie opiera
   sie na zadnej klasie powloki poza sama nazwa `.badge`. */
.catalog .cat-item .ci-v16{display:flex;gap:5px;flex-wrap:wrap;margin-top:5px}
.catalog .cat-item .ci-v16 .badge{display:inline-block;font-family:var(--sans);font-size:11px;
 font-weight:700;line-height:1.5;padding:1px 9px;border-radius:999px;letter-spacing:0;
 text-transform:none;white-space:nowrap;background:var(--grey-soft);color:var(--grey);
 box-shadow:inset 0 0 0 1.5px var(--border)}
.catalog .cat-item .ci-v16 .badge.t-bad{background:var(--bad-soft);color:var(--bad);box-shadow:inset 0 0 0 1.5px var(--bad)}
.catalog .cat-item .ci-v16 .badge.t-info{background:var(--info-soft);color:var(--info);box-shadow:inset 0 0 0 1.5px var(--info)}
.catalog .cat-item .ci-v16 .badge.t-warn{background:var(--warn-soft);color:var(--warn);box-shadow:inset 0 0 0 1.5px var(--warn)}
.catalog .cat-item .ci-v16 .badge.t-ok{background:var(--ok-soft);color:var(--ok);box-shadow:inset 0 0 0 1.5px var(--ok)}
.catalog .cat-item .ci-v16 .badge.t-acc{background:var(--accent-soft);color:var(--accent);box-shadow:inset 0 0 0 1.5px var(--accent)}
```

### SKRYPT 7 — panel roli. Na koniec `<body>`, jako SIODMY blok `<script>`

```js
/* ===========================================================================
   SCRIPT 7 — THE ENTRA ROLE PANEL, IN THE SAME v13/v16 SHAPE AS THE PERMISSION
   PANEL (CLAUDE.md 5al). ADDED, never a replacement: shell scripts 1-3 and the
   added scripts 4 (5y), 5 (5ad), 6 (5ak) are untouched.

   The owner, 5 and 7 September 2026: the Roles tab was prose where the Graph API
   tab was a panel, its filters said "All of those / whole resource" which name
   nothing, its action table did not fit, searching for a directory action
   returned 0, and it had no Exact match. All five have one cause: nothing was
   rebuilding that panel, so the reader saw shell script 3's own rendering.

   This script reads the catalog entry the shell already rendered plus
   `graphMap` in the state block, and builds the panel in the SAME ORDER as the
   permission panel:
       At a glance -> what changed in the last 14 days -> what Microsoft says
       this role is for -> what this role can do -> Graph permissions it covers.
   The 14-day section sits SECOND in both panels; that is the owner's point 2 of
   7 September, and it is a position, not a preference.
   ALL UI TEXT IS ENGLISH.
   =========================================================================== */
(function () {
  "use strict";
  var ROLEREF = "https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#";
  var GUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x !== undefined) n.textContent = x; return n; }
  function jsonBlock(id) {
    var s = document.getElementById(id);
    if (!s) return null;
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }
  var ST = jsonBlock("soc-brief-state") || {};
  var CAT = jsonBlock("soc-catalog") || {};
  var GM = ST.graphMap || null;
  var ROLES = {};
  (CAT.roles || []).forEach(function (r) { if (r && r.name) ROLES[r.name] = r; });

  /* ---- the reverse of graphMap: which permissions does THIS role cover ----
     Computed in the browser from the same array the permission panel prints, so
     the two tabs can never disagree: one derivation, two readings of it. */
  var COVER = {};
  if (GM && GM.perms) {
    Object.keys(GM.perms).forEach(function (p) {
      (GM.perms[p].roles || []).forEach(function (r) {
        var nm = r[0];
        (COVER[nm] = COVER[nm] || []).push({ perm: p, pct: r[1], broad: !!r[2], eps: r[4] });
      });
    });
    Object.keys(COVER).forEach(function (k) {
      COVER[k].sort(function (a, b) { return (b.pct - a.pct) || (b.broad - a.broad) || (a.perm < b.perm ? -1 : 1); });
    });
  }
  /* ---- directory action -> roles, so the search box can answer it ---- */
  var BYACTION = {};
  Object.keys(ROLES).forEach(function (n) {
    (ROLES[n].actionsFull || []).forEach(function (a) {
      (BYACTION[a.action] = BYACTION[a.action] || []).push(n);
    });
  });
  var BYTEMPLATE = {};
  Object.keys(ROLES).forEach(function (n) {
    var t = ROLES[n].templateId; if (t) BYTEMPLATE[String(t).toLowerCase()] = n;
  });
  window.__socRoleIndex = { byAction: BYACTION, byTemplate: BYTEMPLATE, cover: COVER };

  function kv(dl, k, v) {
    dl.appendChild(el("dt", null, k));
    var dd = el("dd");
    if (typeof v === "string") dd.textContent = v; else if (v) dd.appendChild(v);
    dl.appendChild(dd);
  }
  function chip(text, cls) { return el("span", "badge " + (cls || "t-grey"), text); }

  /* ---------------- sections, in the order the permission panel uses --------------- */
  function glance(r) {
    var acts = r.actionsFull || [];
    var npriv = 0, ns = {};
    acts.forEach(function (a) { if (a.privileged) npriv++; ns[String(a.action).split("/")[0]] = 1; });
    var cov = COVER[r.name] || [];
    var broad = 0; cov.forEach(function (c) { if (c.broad) broad++; });

    var sec = el("div", "sec"); sec.appendChild(el("h3", null, "At a glance"));
    var dl = el("dl", "kv");
    kv(dl, "Object type", r.objectType || "Role");
    kv(dl, "Scope", r.scope || "");
    var pv = el("span");
    pv.appendChild(chip(r.privileged === true || r.privileged === "True" ? "PRIVILEGED" : "not privileged",
      (r.privileged === true || r.privileged === "True") ? "t-bad" : "t-grey"));
    if (r.privilegedNote) { var pn = el("span", "note"); pn.style.display = "inline"; pn.style.marginLeft = "8px"; pn.textContent = r.privilegedNote; pv.appendChild(pn); }
    kv(dl, "Privileged", pv);
    if (acts.length) {
      kv(dl, "Directory actions", acts.length + ", of which " + npriv + " privileged, across " +
        Object.keys(ns).length + " namespace" + (Object.keys(ns).length === 1 ? "" : "s"));
    } else {
      var na = el("span", "note"); na.style.display = "inline";
      na.textContent = "Microsoft publishes no Actions table for this role.";
      kv(dl, "Directory actions", na);
    }
    if (cov.length) {
      kv(dl, "Graph permissions covered", cov.length + " at 50% or better — " + broad +
        " whole resource, " + (cov.length - broad) + " selected properties only");
    } else {
      var nc = el("span", "note"); nc.style.display = "inline";
      nc.textContent = GM ? "None reach 50%." : "The endpoint map is not on this page, so coverage is not computed.";
      kv(dl, "Graph permissions covered", nc);
    }
    kv(dl, "Template ID", el("span", "mono", r.templateId || "not published"));
    kv(dl, "Documented at Microsoft", (r.docStatus || "") + (r.docCheckedOn ? " · checked " + r.docCheckedOn : ""));
    kv(dl, "First tracked", r.firstTracked || r.firstSeen || "");
    if (r.url) {
      var a = el("a", "lnk", "Microsoft’s role reference");
      a.href = r.url; a.target = "_blank"; a.rel = "noopener";
      kv(dl, "Source", a);
    }
    sec.appendChild(dl);
    return sec;
  }

  function purpose(r) {
    if (!r.description && !(r.tasks && r.tasks.length)) return null;
    var sec = el("div", "sec");
    sec.appendChild(el("h3", null, "What Microsoft says this role is for"));
    if (r.description) { var p = el("p", null, r.description); p.style.margin = "0 0 8px"; sec.appendChild(p); }
    if (r.tasks && r.tasks.length) {
      var ul = el("ul"); ul.style.cssText = "margin:0;padding-left:19px;font-size:13.5px";
      r.tasks.slice(0, 8).forEach(function (t) { ul.appendChild(el("li", null, t)); });
      sec.appendChild(ul);
    }
    return sec;
  }

  function actions(r) {
    var acts = (r.actionsFull || []).slice();
    if (!acts.length) return null;
    acts.sort(function (a, b) { return a.action < b.action ? -1 : 1; });
    var npriv = 0, ns = {};
    acts.forEach(function (a) { if (a.privileged) npriv++; var k = String(a.action).split("/")[0]; ns[k] = (ns[k] || 0) + 1; });

    var sec = el("div", "sec"), det = el("details", "eps actinject"), sum = el("summary");
    sum.appendChild(el("span", "sm-t", "What this role can do"));
    sum.appendChild(chip(acts.length + " directory actions", "t-acc"));
    if (npriv) sum.appendChild(chip(npriv + " privileged", "t-bad"));
    det.appendChild(sum);

    /* Filter chips name what they filter — the owner's point 3 of 5 September:
       "All of those" and "whole resource" named nothing he could act on. */
    var mf = el("div", "mf");
    function fchip(lab, key, on) {
      var b = el("button", null, lab); b.type = "button"; b.dataset.f = key;
      b.setAttribute("aria-pressed", String(!!on)); mf.appendChild(b);
    }
    fchip("All " + acts.length, "ALL", true);
    if (npriv) fchip("Privileged " + npriv, "PRIV", false);
    Object.keys(ns).sort(function (a, b) { return ns[b] - ns[a]; }).slice(0, 6)
      .forEach(function (k) { fchip(k + " " + ns[k], k, false); });
    det.appendChild(mf);

    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), hr = el("tr");
    hr.appendChild(el("th", null, "Directory action — and what it allows"));
    th.appendChild(hr); tb.appendChild(th);
    var body = el("tbody");
    acts.forEach(function (a) {
      var tr = el("tr");
      tr.dataset.ns = String(a.action).split("/")[0];
      tr.dataset.priv = a.privileged ? "1" : "0";
      var td = el("td", "act");
      td.appendChild(el("code", null, a.action));
      if (a.privileged) { td.appendChild(document.createTextNode(" ")); td.appendChild(chip("privileged", "t-bad")); }
      if (a.description) { var w = el("div", "what", a.description); td.appendChild(w); }
      tr.appendChild(td); body.appendChild(tr);
    });
    tb.appendChild(body); tw.appendChild(tb); det.appendChild(tw);
    if (r.actionsProvenance) det.appendChild(el("p", "note", String(r.actionsProvenance).slice(0, 400)));

    mf.addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest("button") : null; if (!b) return;
      [].forEach.call(mf.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var f = b.dataset.f;
      [].forEach.call(body.querySelectorAll("tr"), function (tr) {
        tr.hidden = !(f === "ALL" || (f === "PRIV" ? tr.dataset.priv === "1" : tr.dataset.ns === f));
      });
    });
    sec.appendChild(det);
    return sec;
  }

  function coverage(r) {
    var cov = COVER[r.name] || [];
    var sec = el("div", "sec");
    sec.appendChild(el("h3", null, "Graph permissions this role covers"));
    if (!GM) {
      sec.appendChild(el("p", "empty", "The endpoint map is not carried on this page, so nothing is derived here."));
      return sec;
    }
    var rb = el("div", "rulebox");
    rb.appendChild(el("b", null, "How this list is derived, and what Microsoft does not publish."));
    rb.appendChild(document.createTextNode(" " + (GM.rule || "")));
    var n = el("p", "note");
    n.appendChild(el("b", null, GM.ruleNote || "Derived by this brief, not published by Microsoft."));
    rb.appendChild(n); sec.appendChild(rb);
    if (!cov.length) {
      sec.appendChild(el("p", "empty",
        "This role covers no Graph permission at 50% or better. That is a result, not a gap: the role's actions " +
        "sit outside the resources those permissions reach."));
      return sec;
    }
    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), hr = el("tr");
    ["Graph permission", "Coverage", "Depth", "Endpoints"].forEach(function (h) { hr.appendChild(el("th", null, h)); });
    th.appendChild(hr); tb.appendChild(th);
    var body = el("tbody");
    cov.slice(0, 25).forEach(function (c) {
      var tr = el("tr");
      var c0 = el("td", "rname mono", c.perm); tr.appendChild(c0);
      var c1 = el("td"); c1.appendChild(el("b", null, c.pct + "%")); tr.appendChild(c1);
      var c2 = el("td");
      c2.appendChild(chip(c.broad ? "whole resource" : "selected properties only", c.broad ? "t-ok" : "t-warn"));
      tr.appendChild(c2);
      tr.appendChild(el("td", null, (c.eps || 0) + " endpoints"));
      body.appendChild(tr);
    });
    tb.appendChild(body); tw.appendChild(tb); sec.appendChild(tw);
    sec.appendChild(el("p", "note", cov.length + " permissions reach 50% or better; the " +
      Math.min(25, cov.length) + " strongest are shown. Whole resource beats property-limited at equal coverage."));
    return sec;
  }

  /* ---------------- build ---------------- */
  function build(inner) {
    if (!inner || inner.querySelector(".v13pane")) return;
    var h = inner.querySelector(".cat-title");
    if (!h) return;
    var name = (h.textContent || "").trim();
    var r = ROLES[name];
    if (!r) return;                       /* not a role entry: stay silent */

    var pane = el("div", "v13pane v13role");
    var head = document.createElement("header");
    head.appendChild(el("h2", null, name));
    var chips = el("div", "chips"), src = inner.querySelector(".cat-badges");
    if (src) [].forEach.call(src.querySelectorAll(".badge"), function (b) {
      chips.appendChild(chip(b.textContent.trim(), "t-grey"));
    });
    head.appendChild(chips); pane.appendChild(head);

    pane.appendChild(glance(r));
    if (window.__socHistSection) {
      var hs = window.__socHistSection("role", name);   /* SCRIPT 8 owns the ledger */
      if (hs) pane.appendChild(hs);
    }
    var p = purpose(r); if (p) pane.appendChild(p);
    var a = actions(r); if (a) pane.appendChild(a);
    pane.appendChild(coverage(r));

    /* the shell's own versions of these panels are HIDDEN, never removed:
       script 3 owns that markup and this script does not edit script 3. */
    [].forEach.call(inner.querySelectorAll("section.cat-panel"), function (s) {
      var t = (s.querySelector("h4") || {}).textContent || "";
      if (/at a glance|what this role is for|what this role can do|directory actions/i.test(t)) s.hidden = true;
    });
    /* the shell's own head carries the same name and the same chips as this pane's
       header; leaving both printed the role name twice, which the owner saw */
    var ch = inner.querySelector(".cat-head"); if (ch) ch.hidden = true;
    var after = inner.querySelector(".cat-head");
    if (after && after.nextSibling) inner.insertBefore(pane, after.nextSibling);
    else inner.appendChild(pane);
  }

  /* a panel built on demand, for SCRIPT 8's `+` in the history table */
  window.__socOpenRole = function (name) {
    var cat = document.querySelector('.catalog[data-catalog="roles"]');
    if (!cat) return null;
    var items = [].slice.call(cat.querySelectorAll(".cat-item"));
    var want = null;
    items.forEach(function (b) {
      var nm = ((b.querySelector(".ci-name") || {}).textContent || "").trim();
      if (!want && nm === name) want = b;
    });
    if (!want) return null;
    want.click();
    return cat.querySelector(".cat-detail .cat-detail-inner");
  };

  /* ---------------- Exact match and three kinds of query on the roles search ---------------- */
  function search() {
    var cat = document.querySelector('.catalog[data-catalog="roles"]');
    if (!cat || cat.querySelector(".s7exact")) return;
    var row = cat.querySelector(".cat-searchrow"), input = cat.querySelector("input.cat-search");
    if (!row || !input) return;
    var lab = el("label", "s7exact");
    var box = document.createElement("input"); box.type = "checkbox"; box.id = "s7exact";
    lab.appendChild(box); lab.appendChild(document.createTextNode(" Exact match"));
    var cnt = row.querySelector(".rowcount");
    if (cnt) row.insertBefore(lab, cnt); else row.appendChild(lab);

    var why = el("p", "s7why"); why.hidden = true;
    var list = cat.querySelector(".cat-list");
    if (list && list.parentNode) list.parentNode.insertBefore(why, list);

    /* Examples the reader can CLICK. A placeholder listing four kinds of query is
       truncated on a phone and cannot be acted on; a chip can. */
    var tips = el("div", "s7tips");
    tips.appendChild(el("span", "lab", "Examples — click one"));
    [["role name", "Global Reader"],
     ["directory action", "microsoft.directory/users/inviteGuest"],
     ["template ID", (function () { var k = Object.keys(BYTEMPLATE)[0]; return k || ""; })()]]
      .forEach(function (t) {
        if (!t[1]) return;
        var b = el("button", null, ""); b.type = "button";
        b.appendChild(el("b", null, t[0])); b.appendChild(document.createTextNode(t[1]));
        b.addEventListener("click", function () {
          input.value = t[1];
          input.dispatchEvent(new Event("input", { bubbles: true }));
          setTimeout(apply, 0); input.focus();
        });
        tips.appendChild(b);
      });
    if (row.parentNode) row.parentNode.insertBefore(tips, row);

    function resolve(v) {
      var s = (v || "").trim();
      if (!s) return { kind: "", names: null, note: "" };
      if (GUID.test(s)) {
        var n = BYTEMPLATE[s.toLowerCase()];
        return { kind: "template ID", names: n ? [n] : [],
                 note: n ? ("That template ID belongs to " + n + ".") : "No role in this catalog carries that template ID." };
      }
      if (s.toLowerCase().indexOf("microsoft.") === 0) {
        var exact = BYACTION[s] || null, hits = [], nmatch = 0;
        if (exact) hits = exact.slice();
        else {
          Object.keys(BYACTION).forEach(function (k) {
            if (k.toLowerCase().indexOf(s.toLowerCase()) >= 0) {
              nmatch++;
              BYACTION[k].forEach(function (r) { if (hits.indexOf(r) < 0) hits.push(r); });
            }
          });
        }
        return { kind: "directory action", names: hits,
          note: hits.length
            ? (exact ? (hits.length + " role" + (hits.length === 1 ? "" : "s") + " carry exactly " + s + ": " +
                        hits.slice(0, 8).join(", ") + (hits.length > 8 ? " …" : "") + ".")
                     : (nmatch + " action" + (nmatch === 1 ? "" : "s") + " match, carried by " + hits.length +
                        " role" + (hits.length === 1 ? "" : "s") + "."))
            : "No role in this catalog publishes an action matching that." };
      }
      return { kind: "role name", names: null, note: "" };
    }

    /* The filter is expressed in the STYLESHEET, never by writing `hidden` on the
       shell's list items. Measured: writing there made the shell re-render, which
       made this filter run again, 200+ times, and the page stopped responding.
       A rule survives a re-render and cannot fight with one. */
    var sty = document.getElementById("s7filter");
    if (!sty) { sty = document.createElement("style"); sty.id = "s7filter"; document.head.appendChild(sty); }
    function idOf(name) { var r = ROLES[name]; return r && r.id ? String(r.id) : null; }
    function esc2(v) { return String(v).replace(/\\/g, "\\\\").replace(/"/g, '\\"'); }
    function setFilter(ids) {
      if (!ids) { sty.textContent = ""; return; }
      var base = '.catalog[data-catalog="roles"] .cat-list .cat-item{display:none!important}';
      if (!ids.length) { sty.textContent = base; return; }
      sty.textContent = base + "\n" + ids.map(function (i) {
        return '.catalog[data-catalog="roles"] .cat-list .cat-item[data-id="' + esc2(i) + '"]';
      }).join(",") + "{display:flex!important}";
    }

    function apply() {
      if (!list) return;
      var v = (input.value || "").trim(), ex = box.checked, r = resolve(v);
      /* A role NAME is a question the shell's own list already answers; Exact match
         only narrows what it produced, and it narrows it with a rule. An ACTION or
         a TEMPLATE ID is a different namespace: the shell rebuilds its list from
         names and leaves nothing in the DOM — measured, zero entries — so the
         answer there is the note, with every role named and each name a button. */
      if (!r.names && v && ex) {
        var keep = [];
        Object.keys(ROLES).forEach(function (n) {
          if (n.toLowerCase() === v.toLowerCase()) { var i2 = idOf(n); if (i2) keep.push(i2); }
        });
        setFilter(keep);
      } else setFilter(null);

      var shown = 0;
      [].forEach.call(list.querySelectorAll(".cat-item"), function (b) {
        if (b.offsetParent !== null || getComputedStyle(b).display !== "none") shown++;
      });

      why.textContent = "";
      why.hidden = !r.note;
      if (r.note) {
        why.appendChild(document.createTextNode(r.note));
        if (r.names && r.names.length) {
          why.appendChild(document.createTextNode(" The list below searches role names, so it does not answer this " +
            "question — open a role from here:"));
          var box2 = el("span", "s7hits");
          r.names.slice(0, 12).forEach(function (n) {
            var b2 = el("button", null, n); b2.type = "button";
            b2.addEventListener("click", function () {
              input.value = "";
              input.dispatchEvent(new Event("input", { bubbles: true }));
              setTimeout(function () {
                var inner = window.__socOpenRole && window.__socOpenRole(n);
                if (inner && inner.scrollIntoView) inner.scrollIntoView({ block: "start" });
              }, 120);
            });
            box2.appendChild(b2);
          });
          if (r.names.length > 12) box2.appendChild(el("span", "note", " … and " + (r.names.length - 12) + " more"));
          why.appendChild(box2);
        }
      }
      if (cnt && v) cnt.textContent = r.names ? (r.names.length + " roles · " + r.kind)
                                              : (shown + (ex ? " exact" : "") + (r.kind ? " · " + r.kind : ""));
    }
    box.addEventListener("change", function () { setTimeout(apply, 0); });
    input.addEventListener("input", function () { setTimeout(apply, 0); setTimeout(apply, 180); });

  }


  /* A row on the /diff/ page cannot open a panel: that page carries no catalog by
     design (§3). It can point at one. `#roles:role=<name>` selects the entry
     here, so a link from the change page lands on the panel itself. */
  function fromHash() {
    var m = /^#roles:role=(.+)$/.exec(decodeURIComponent(location.hash || ""));
    if (!m) return;
    var name = m[1];
    setTimeout(function () {
      var inner = window.__socOpenRole && window.__socOpenRole(name);
      if (inner && inner.scrollIntoView) inner.scrollIntoView({ block: "start" });
    }, 260);
  }
  /* ---------- the section's own table, and two filters that named nothing ----------
     Measured on the published page of 7 September 2026: the Roles section opens with
     a 20-row table under a bare "Search 20 rows…", two selects reading "All of those,
     whole resource" and "All dominant depth" — the shell builds a facet from the
     column HEADER, and a numeric column makes a facet that cannot group anything
     (§5s, the same disease as a chart of ones). The table itself is useful; nothing
     said what it was. So: name it, say what it ranks, fold it under the history, and
     drop the facet that cannot work. */
  function rankTable() {
    var sec = document.getElementById("roles");
    if (!sec || sec.querySelector("details.rolerank")) return;
    var body = sec.querySelector(".sec-body"); if (!body) return;
    var tw = null;
    [].forEach.call(body.children, function (x) {
      if (!tw && x.classList && x.classList.contains("tw")) tw = x;
    });
    if (!tw) return;
    var rows = tw.querySelectorAll("tbody tr").length;
    if (!rows) return;
    /* The toolbar and the filter banner are inserted by the shell at load time as
       SIBLINGS of the table, and the note under it belongs to it too. Take the whole
       block, or the reader gets a search box floating above nothing. */
    var bar = [], k;
    for (k = tw.previousElementSibling; k; k = k.previousElementSibling) {
      if (k.classList && (k.classList.contains("tbar") || k.classList.contains("filterbanner"))) bar.unshift(k);
      else break;
    }
    var after = [];
    for (k = tw.nextElementSibling; k; k = k.nextElementSibling) {
      if (k.classList && (k.classList.contains("rnote") || k.classList.contains("filterbanner"))) after.push(k);
      else break;
    }

    var det = el("details", "rolerank");
    var sum = el("summary");
    sum.appendChild(el("span", "sm-t", "Roles ranked by the Graph permissions they cover"));
    sum.appendChild(el("span", "badge t-acc", rows + " roles"));
    det.appendChild(sum);
    det.appendChild(el("p", "note",
      "The " + rows + " roles that cover the most Graph permissions at 50% or better, derived by this brief " +
      "and not published by Microsoft. Depth says whether the matching directory action reaches the whole " +
      "resource or only selected properties; at equal coverage, whole resource is the stronger one. " +
      "Every role in the catalog below has its own panel carrying the same figures."));
    bar.forEach(function (x) { det.appendChild(x); });
    det.appendChild(tw);
    after.forEach(function (x) { det.appendChild(x); });

    /* A facet built from a NUMERIC column groups nothing — "All of those, whole
       resource" is a filter over counts. Hide it rather than leave it lying there;
       the depth facet is real, so it only gets a name a reader can act on. */
    bar.forEach(function (b2) {
      [].forEach.call(b2.querySelectorAll("select"), function (sl) {
        var first = (sl.options[0] || {}).textContent || "";
        if (/^all of those/i.test(first)) sl.hidden = true;
        else if (/^all dominant depth$/i.test(first)) sl.options[0].textContent = "All depth";
      });
      var si = b2.querySelector("input[type=search]");
      if (si) si.placeholder = "Search these " + rows + " roles\u2026";
    });

    var cat = body.querySelector(".catalog");
    if (cat) body.insertBefore(det, cat); else body.appendChild(det);
  }

  /* A summary cut at 88 characters ends mid-thought — "Recounted in…" tells the reader
     nothing about whether to open it. The body is untouched; only the label changes,
     to the first complete sentence. */
  function fixFoldSummaries() {
    [].forEach.call(document.querySelectorAll("details.foldnote > summary"), function (sm) {
      if (sm.dataset.s7fix === "1") return;
      var body = sm.parentNode.querySelector(".foldnote-body");
      var full = ((body && body.textContent) || "").trim();
      if (!full) return;
      var m = /^(.{20,150}?[.!?])(\s|$)/.exec(full);
      if (!m) return;
      sm.dataset.s7fix = "1";
      sm.textContent = m[1];
    });
  }

  /* ---------- the left strip: what v16 puts next to a role ----------
     The shell writes the change kind and a date; v16 writes what the reader is
     choosing between — privileged, how many directory actions, how many Graph
     permissions it covers. The shell's own chip row is HIDDEN, never removed, and
     ours is appended; the list is rebuilt on every filter, so we re-decorate on
     each render, guarded so the two cannot chase each other. */
  function decorate() {
    var cat = document.querySelector('.catalog[data-catalog="roles"]');
    if (!cat) return;
    var list = cat.querySelector(".cat-list"); if (!list) return;
    [].forEach.call(list.querySelectorAll(".cat-item"), function (b) {
      if (b.dataset.v16 === "1") return;
      var nm = ((b.querySelector(".ci-name") || {}).textContent || "").trim();
      var r = ROLES[nm]; if (!r) return;
      b.dataset.v16 = "1";
      var old = b.querySelector(".ci-meta"); if (old) old.hidden = true;
      var m = el("div", "ci-v16");
      if (r.privileged === true || r.privileged === "True") m.appendChild(chip("PRIV", "t-bad"));
      var na = (r.actionsFull || []).length;
      m.appendChild(chip(na ? (na + " actions") : "no actions table", na ? "t-grey" : "t-warn"));
      var nc = (COVER[nm] || []).length;
      if (nc) m.appendChild(chip(nc + " perms", "t-info"));
      b.appendChild(m);
    });
  }
  function watchList() {
    var cat = document.querySelector('.catalog[data-catalog="roles"]');
    var list = cat && cat.querySelector(".cat-list"); if (!list) return;
    var busy = false;
    function run() {
      if (busy) return;
      busy = true;
      try { decorate(); var i2 = cat.querySelector("input.cat-search"); if (i2) i2.placeholder = "Search roles"; } finally { busy = false; }
    }
    run();
    if (window.MutationObserver)
      new MutationObserver(function () { if (!busy) run(); }).observe(list, { childList: true });
  }

  function boot() {
    if (!Object.keys(ROLES).length) return;
    search(); rankTable(); fixFoldSummaries(); watchList(); fromHash();
    /* the shell builds that toolbar on its own schedule; one late pass, guarded by
       the `details.rolerank` check, costs nothing and catches the other ordering */
    setTimeout(function () { rankTable(); fixFoldSummaries(); decorate(); }, 400);
    window.addEventListener("hashchange", fromHash);
    [].forEach.call(document.querySelectorAll('.catalog[data-catalog="roles"] .cat-detail'), function (det) {
      build(det.querySelector(".cat-detail-inner"));
      if (window.MutationObserver)
        new MutationObserver(function () { build(det.querySelector(".cat-detail-inner")); })
          .observe(det, { childList: true, subtree: false });
    });
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", function () { setTimeout(boot, 140); });
  else setTimeout(boot, 140);
})();
```

### SKRYPT 8 — gora zakladki i rejestr 14 dni. Jako OSMY blok `<script>`

```js
/* ===========================================================================
   SCRIPT 8 — THE TOP OF EVERY CONTENT TAB: COUNTS, THE ARITHMETIC BEHIND THEM,
   AND THE LAST 14 DAYS (CLAUDE.md 5al, extending 5aj). ADDED, never a
   replacement.

   Three findings from the owner, 7 September 2026, and one cause each:
   1. "I do not know what is on the x axis and what on the y" — the strip had no
      axis titles at all. Both are now printed ON the drawing, and a sentence
      above it says how to read it.
   2. "in Roles that section is at the bottom, in Graph API at the top" — the two
      tabs were laid out by two different pieces of code. ONE function now builds
      the top of BOTH tabs, so they cannot drift: tiles, folded arithmetic,
      history. Position is enforced by construction, not by care.
   3. "when I press + I should get the same view as the panel below" — every
      history row carries a `+` that asks the CATALOG for its panel and clones
      what it renders. Not a second rendering of the same data: the same one.
   ALL UI TEXT IS ENGLISH.
   =========================================================================== */
(function () {
  "use strict";
  var TABS = [
    { id: "tab-roles",      ledger: ["Roles"],                          kind: "role" },
    { id: "tab-graph",      ledger: ["Graph API", "Graph endpoints"],   kind: "perm" },
    { id: "tab-new",        ledger: ["New"],                            kind: "row"  },
    { id: "tab-deadlines",  ledger: ["Deadlines"],                      kind: "row"  },
    { id: "tab-components", ledger: ["Component versions"],             kind: "row"  }
  ];
  var MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x !== undefined) n.textContent = x; return n; }
  function sv(t, a) { var n = document.createElementNS("http://www.w3.org/2000/svg", t);
    for (var k in a) if (Object.prototype.hasOwnProperty.call(a, k)) n.setAttribute(k, a[k]); return n; }
  function jsonBlock(id) {
    var s = document.getElementById(id); if (!s) return null;
    try { return JSON.parse(s.textContent); } catch (e) { return null; }
  }
  var ST = jsonBlock("soc-brief-state") || {};
  var CAT = jsonBlock("soc-catalog") || {};
  var GM = ST.graphMap || null;
  var L = ST.ledger14 || null;
  var ENTRIES = (L && L.entries) || [];
  var RUNS = {}; ((L && L.runs) || []).forEach(function (r) { RUNS[r.date] = r; });
  var WINDOW_DAYS = (L && L.pageWindowDays) || 14;
  var TODAY = ST.briefDate || (new Date()).toISOString().slice(0, 10);

  function nameOf(entry) {
    /* the ledger writer has packed a sentence into `id` before now; take the
       subject either way, and never guess what the rest of it meant */
    return String(entry.id || "").split("→")[0].replace(/&mdash;|—/g, "").trim();
  }

  /* ---------------- the chart, with BOTH axes named on the drawing ---------------- */
  function chart(rows, label) {
    var per = {}, i;
    rows.forEach(function (r) { per[r.seen] = (per[r.seen] || 0) + 1; });
    var t = new Date(TODAY + "T00:00:00Z"), ds = [], vals = [];
    for (i = WINDOW_DAYS - 1; i >= 0; i--) {
      var d = new Date(t.getTime() - i * 86400000).toISOString().slice(0, 10);
      ds.push(d); vals.push(per[d] || 0);
    }
    var mx = Math.max.apply(null, vals.concat([1]));
    var W = 1200, H = 250, PADL = 92, PADR = 14, PADT = 34, PADB = 74;
    var plotW = W - PADL - PADR, plotH = H - PADT - PADB, bw = plotW / WINDOW_DAYS;
    var s = sv("svg", { viewBox: "0 0 " + W + " " + H, role: "img",
      "aria-label": label + " per day over the last " + WINDOW_DAYS + " days, with a seven-day moving average" });
    [0, 0.5, 1].forEach(function (g) {
      var y = PADT + plotH - plotH * g;
      s.appendChild(sv("line", { x1: PADL, y1: y, x2: W - PADR, y2: y, "class": "gl" }));
      var tx = sv("text", { x: PADL - 8, y: y + 5, "class": "ax", "text-anchor": "end" });
      tx.textContent = Math.round(mx * g); s.appendChild(tx);
    });
    s.appendChild(sv("line", { x1: PADL, y1: PADT, x2: PADL, y2: PADT + plotH, "class": "gl" }));
    var pts = [];
    ds.forEach(function (d, i2) {
      var n = vals[i2], x = PADL + i2 * bw, cx = x + bw / 2, r;
      if (!RUNS[d]) {
        r = sv("rect", { x: x + 4, y: PADT + plotH - 6, width: bw - 8, height: 6, rx: 2, "class": "b-norun" });
        r.appendChild(sv("title")).textContent = d + " — no run, so nothing was recorded";
      } else if (!n) {
        r = sv("rect", { x: x + 4, y: PADT + plotH - 6, width: bw - 8, height: 6, rx: 2, "class": "b-quiet" });
        r.appendChild(sv("title")).textContent = d + " — a run looked and nothing moved";
      } else {
        var h = Math.max(7, plotH * n / mx);
        r = sv("rect", { x: x + 4, y: PADT + plotH - h, width: bw - 8, height: h, rx: 3, "class": "b-chg" });
        r.appendChild(sv("title")).textContent = d + " — " + n + " " + (n === 1 ? label.replace(/s$/, "") : label);
        var vt = sv("text", { x: cx, y: PADT + plotH - h - 6, "class": "ax", "text-anchor": "middle" });
        vt.textContent = n; s.appendChild(vt);
      }
      s.appendChild(r);
      var win = [], j;
      for (j = Math.max(0, i2 - 6); j <= i2; j++) if (RUNS[ds[j]]) win.push(vals[j]);
      if (win.length) {
        var avg = win.reduce(function (a, b) { return a + b; }, 0) / win.length;
        pts.push(cx.toFixed(1) + "," + (PADT + plotH - plotH * avg / mx).toFixed(1));
      }
      var dd = new Date(d + "T00:00:00Z");
      var lt = sv("text", { x: cx, y: PADT + plotH + 18, "class": "ax", "text-anchor": "middle" });
      lt.textContent = dd.getUTCDate(); s.appendChild(lt);
      if (i2 === 0 || dd.getUTCDate() === 1) {
        var mt = sv("text", { x: cx, y: PADT + plotH + 34, "class": "ax", "text-anchor": "middle" });
        mt.textContent = MON[dd.getUTCMonth()]; s.appendChild(mt);
      }
    });
    if (pts.length > 1) s.appendChild(sv("polyline", { points: pts.join(" "), "class": "trend" }));
    var yt = sv("text", { "class": "axt", transform: "translate(20," + (PADT + plotH / 2) + ") rotate(-90)", "text-anchor": "middle" });
    yt.textContent = label + " per day"; s.appendChild(yt);
    var xt = sv("text", { "class": "axt", x: PADL + plotW / 2, y: H - 14, "text-anchor": "middle" });
    xt.textContent = "day of month · oldest on the left · today on the right"; s.appendChild(xt);

    var wrap = el("div");
    var how = el("p", "howto");
    how.appendChild(el("b", null, "How to read this. "));
    how.appendChild(document.createTextNode(
      "The upright axis counts " + label + " recorded on that day — the number is printed on each bar and again " +
      "on the scale at the left. The flat axis is the day, one bar per day, the oldest " + WINDOW_DAYS +
      " days ago on the left and today on the right. The orange line is the seven-day moving average, so it " +
      "shows the trend without one busy day standing for the fortnight."));
    wrap.appendChild(how);
    var cw = el("div", "chartwrap"); cw.appendChild(s); wrap.appendChild(cw);
    var lg = el("div", "legend");
    [["k-chg", "a day with " + label], ["k-quiet", "a run looked, nothing moved"],
     ["k-norun", "no run that day, so nothing is known"], ["k-trend", "seven-day moving average"]]
      .forEach(function (p) {
        var sp = el("span"); sp.appendChild(el("i", p[0])); sp.appendChild(document.createTextNode(p[1])); lg.appendChild(sp);
      });
    wrap.appendChild(lg);
    return wrap;
  }

  /* ---------------- one history row, and the `+` that opens the real panel ---------------- */
  function valueCell(e2) {
    var td = el("td");
    /* An increment is not a transition: "+3 endpoints" has no `before`, and
       printing "not set → +3" invents a previous value that never existed. */
    if (!e2.before && e2.after && /^[+\u2212-]\d/.test(String(e2.after))) {
      var ins0 = document.createElement("ins"); ins0.textContent = e2.after;
      ins0.title = "gained since the previous run";
      td.appendChild(ins0);
      return td;
    }
    if (e2.before || e2.after) {
      if (e2.before) { var d = document.createElement("del"); d.textContent = e2.before; td.appendChild(d); }
      else td.appendChild(el("span", "none", "not set"));
      td.appendChild(el("span", "arrow", " → "));
      if (e2.after) { var i2 = document.createElement("ins"); i2.textContent = e2.after; td.appendChild(i2); }
      else td.appendChild(el("span", "none", "cleared"));
    } else td.appendChild(document.createTextNode(e2.detail || "—"));
    return td;
  }

  function table(rows, kind, ledgerTabs) {
    /* No `Tab` column: inside the Graph API tab every row said "Graph API".
       A second ledger tab under the same panel — Graph endpoints — is marked on
       the row instead, because there the distinction carries something. */
    var multi = (ledgerTabs || []).length > 1;
    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), hr = el("tr");
    ["", "Day", "What", "Item", "Field", "Before → after"].forEach(function (h) { hr.appendChild(el("th", null, h)); });
    th.appendChild(hr); tb.appendChild(th);
    var body = el("tbody");
    rows.forEach(function (e2) {
      var key = nameOf(e2);
      var tr = el("tr", "hrow");
      var c0 = el("td", "xc");
      if (key && kind !== "row") {
        var b = el("button", "xb", "+");
        b.type = "button"; b.dataset.kind = kind; b.dataset.key = key;
        b.setAttribute("aria-expanded", "false");
        b.title = "Show the full panel for " + key;
        c0.appendChild(b);
      } else if (key && kind === "row") {
        var a = el("a", "xb", "↗");
        a.href = "#"; a.title = "Jump to the row for " + key;
        a.addEventListener("click", function (ev) {
          ev.preventDefault();
          var t2 = document.querySelector('[data-id="' + (window.CSS && CSS.escape ? CSS.escape(key) : key) + '"]');
          if (t2) { t2.scrollIntoView({ block: "center" }); t2.classList.add("s8flash");
                    setTimeout(function () { t2.classList.remove("s8flash"); }, 2000); }
        });
        c0.appendChild(a);
      } else c0.appendChild(el("span", "xn", "—"));
      tr.appendChild(c0);
      tr.appendChild(el("td", null, e2.seen || ""));
      var kc = el("td");
      kc.appendChild(document.createTextNode(e2.kind || ""));
      if (multi && e2.tab && e2.tab !== (ledgerTabs || [])[0]) {
        kc.appendChild(document.createTextNode(" "));
        kc.appendChild(el("span", "badge t-grey", e2.tab));
      }
      tr.appendChild(kc);
      tr.appendChild(el("td", "rname", key || "—"));
      var fc = el("td"); if (e2.field) fc.appendChild(el("code", null, e2.field)); tr.appendChild(fc);
      tr.appendChild(valueCell(e2));
      body.appendChild(tr);
      var det = el("tr", "hdet"); det.hidden = true;
      var dc = el("td"); dc.setAttribute("colspan", "6");
      dc.appendChild(el("div", "hd-in")); det.appendChild(dc); body.appendChild(det);
    });
    tb.appendChild(body); tw.appendChild(tb);
    return tw;
  }

  function embed(box, kind, key) {
    var inner = null;
    if (kind === "perm" && window.__socOpenPerm) inner = window.__socOpenPerm(key);
    if (kind === "role" && window.__socOpenRole) inner = window.__socOpenRole(key);
    /* the catalog renders on the next tick; clone what it produced */
    setTimeout(function () {
      var src = inner || null;
      if (!src) {
        box.innerHTML = "";
        box.appendChild(el("p", "empty", key + " is named in the ledger but carries no entry in the catalog as " +
          "it stands today, so there is no panel to open. That absence is itself the finding: the entry was " +
          "withdrawn, or it lives on a surface this catalog does not cover."));
        return;
      }
      box.innerHTML = "";
      box.appendChild(el("p", "hd-lead", "The full panel for " + key + ", the same one the catalog below shows"));
      var c = src.cloneNode(true);
      c.classList.add("embed");
      var h = c.querySelector("[data-hist]"); if (h && h.parentNode) h.parentNode.removeChild(h);
      box.appendChild(c);
    }, 90);
  }

  document.addEventListener("click", function (ev) {
    var b = ev.target.closest ? ev.target.closest("button.xb") : null; if (!b) return;
    var tr = b.closest("tr"), det = tr.nextElementSibling;
    if (!det || !det.classList.contains("hdet")) return;
    var box = det.querySelector(".hd-in");
    if (box && box.dataset.built !== "1") {
      box.dataset.built = "1";
      box.appendChild(el("p", "note", "Opening …"));
      embed(box, b.dataset.kind, b.dataset.key);
    }
    var open = det.hidden;
    det.hidden = !open;
    b.textContent = open ? "−" : "+";
    b.setAttribute("aria-expanded", String(open));
    tr.setAttribute("aria-expanded", String(open));
  });

  /* ---------------- the per-item section scripts 6 and 7 place SECOND ---------------- */
  window.__socHistSection = function (kind, key) {
    var mine = ENTRIES.filter(function (e2) { return nameOf(e2) === key; });
    var sec = el("div", "sec"); sec.dataset.hist = "1";
    sec.appendChild(el("h3", null, "What changed on this " + (kind === "role" ? "role" : "permission") +
      " in the last " + WINDOW_DAYS + " days"));
    if (!L) {
      sec.appendChild(el("p", "empty", "This page carries no change ledger, so nothing can be shown here."));
      return sec;
    }
    if (!mine.length) {
      sec.appendChild(el("p", "empty", "Nothing moved on this " + (kind === "role" ? "role" : "permission") +
        " in the window. " + Object.keys(RUNS).length + " runs looked; that is a result, not a gap."));
      return sec;
    }
    var tw = el("div", "tw"), tb = el("table"), th = el("thead"), hr = el("tr");
    ["Day", "What", "Field", "Before → after"].forEach(function (h) { hr.appendChild(el("th", null, h)); });
    th.appendChild(hr); tb.appendChild(th);
    var body = el("tbody");
    mine.forEach(function (e2) {
      var tr = el("tr");
      tr.appendChild(el("td", null, e2.seen || ""));
      tr.appendChild(el("td", null, e2.kind || ""));
      var fc = el("td"); if (e2.field) fc.appendChild(el("code", null, e2.field)); tr.appendChild(fc);
      tr.appendChild(valueCell(e2));
      body.appendChild(tr);
    });
    tb.appendChild(body); tw.appendChild(tb); sec.appendChild(tw);
    return sec;
  };

  /* ---------------- fact tiles and the arithmetic behind them ---------------- */
  function tiles(spec, panel) {
    /* The shell's own `.panelhead` already prints some of these numbers. Printing
       the same figure twice, one under the other, is how a page starts to look
       unreliable — so a tile whose label AND value the panel already carries is
       dropped here rather than repeated. The check is on the rendered text, so it
       self-adjusts when either side changes. */
    var have = {};
    if (panel) [].forEach.call(panel.querySelectorAll(".panelhead .stat"), function (st) {
      have[(st.textContent || "").replace(/\s+/g, "").toLowerCase()] = 1;
    });
    var g = el("div", "factgrid");
    spec.forEach(function (t) {
      var key = (t[0] + t[1]).replace(/\s+/g, "").toLowerCase();
      if (have[key]) return;
      var f = el("div", "fact" + (t[2] ? " " + t[2] : ""));
      f.appendChild(el("b", null, t[0])); f.appendChild(el("span", null, t[1]));
      g.appendChild(f);
    });
    return g;
  }
  function fold(summaryNodes, rows, note) {
    var d = el("details", "sumfold"), s = el("summary"), sp = el("span");
    summaryNodes.forEach(function (n) { sp.appendChild(typeof n === "string" ? document.createTextNode(n) : n); });
    s.appendChild(sp); d.appendChild(s);
    var box = el("div", "sum"), tb = el("table"), body = el("tbody");
    rows.forEach(function (r) {
      var tr = el("tr");
      tr.appendChild(el("td", null, r[0]));
      var td = el("td"); td.innerHTML = r[1]; tr.appendChild(td);
      body.appendChild(tr);
    });
    tb.appendChild(body); box.appendChild(tb);
    if (note) box.appendChild(el("p", "note", note));
    d.appendChild(box);
    return d;
  }
  function nfmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }

  function rolesTop(panel) {
    var R = CAT.roles || [];
    if (!R.length) return null;
    var ref = 0, acts = 0, priv = 0, privRole = 0, extra = [], outOfInv = [];
    R.forEach(function (r) {
      if (r.fromReference) ref++; else extra.push(r.name);
      if (r.inInventory === false) outOfInv.push(r.name);
      (r.actionsFull || []).forEach(function (a) { acts++; if (a.privileged) priv++; });
      if (r.privileged === true || r.privileged === "True") privRole++;
    });
    /* The tab badge and the shell's own stat say 137 while this catalog holds 139
       records; the owner asked on 5 September "how can it be 137 of 136?". The lead
       tile therefore carries the SAME number the rest of the page carries, and the
       fold below prints the whole arithmetic instead of leaving him to infer it. */
    var inCat = R.length - outOfInv.length;
    var cov = window.__socRoleIndex ? Object.keys(window.__socRoleIndex.cover).length : 0;
    var withAct = R.filter(function (r) { return (r.actionsFull || []).length; }).length;
    var frag = document.createDocumentFragment();
    frag.appendChild(tiles([
      [nfmt(inCat), "roles in the catalog", "acc"],
      [nfmt(ref), "published by Microsoft", ""],
      ["+" + extra.length, "carried by this brief", "warn"],
      [nfmt(acts), "directory actions", "info"],
      [nfmt(priv), "privileged actions", "bad"],
      [nfmt(privRole), "privileged roles", "bad"],
      [nfmt(cov), "roles covering a Graph permission", "ok"]
    ], panel));
    frag.appendChild(fold(
      [el("b", null, nfmt(inCat)), " in the catalog, ", el("b", null, nfmt(R.length)),
       " records held, ", el("b", null, nfmt(ref)), " published by Microsoft \u2014 how the count is made up"],
      [[nfmt(ref), "roles on Microsoft\u2019s published reference"],
       ["+" + extra.length, "carried by this brief: " + extra.join(" \u00b7 ")],
       ["= " + nfmt(R.length), "records held here"],
       ["\u2212 " + outOfInv.length, "held but outside the inventory count: " + (outOfInv.join(" \u00b7 ") || "none")],
       ["= " + nfmt(inCat), "counted in the catalog and on the tab badge"]],
      withAct + " of them publish an Actions table; " + (R.length - withAct) +
      " do not, and Microsoft is the reason, not this brief."));
    return frag;
  }

  function graphTop(panel) {
    if (!GM || !GM.perms) return null;
    var n = Object.keys(GM.perms).length;
    var withRoles = 0, roleSet = {};
    Object.keys(GM.perms).forEach(function (p) {
      var rs = GM.perms[p].roles || [];
      if (rs.length) withRoles++;
      rs.forEach(function (r) { roleSet[r[0]] = 1; });
    });
    var frag = document.createDocumentFragment();
    frag.appendChild(tiles([
      [nfmt(GM.permissions || n), "permissions in Microsoft\u2019s map", "acc"],
      [nfmt(GM.pairs || 0), "endpoint and method pairs", "info"],
      [nfmt(GM.paths || 0), "distinct paths", ""],
      [nfmt(withRoles), "permissions with a derived role list", ""],
      [nfmt(Object.keys(roleSet).length), "roles appearing in those lists", "ok"]
    ], panel));
    frag.appendChild(fold(
      [el("b", null, nfmt(GM.permissions || n)), " permissions · ",
       el("b", null, nfmt(GM.pairs || 0)), " endpoint and method pairs — where these numbers come from"],
      [[nfmt(GM.permissions || n), "permissions in <span class=\"mono\">permissions/new/permissions.json</span>, commit " + (GM.commit || "")],
       [nfmt(GM.pairs || 0), "method-and-path pairs, counted by decoding every <span class=\"mono\">pathSet</span>"],
       [nfmt(GM.paths || 0), "distinct paths behind those pairs"],
       [nfmt(withRoles), "permissions carrying a derived Entra role list"]],
      "Read on " + (GM.readOn || "") + ". The role list is derived by this brief, not published by Microsoft; " +
      "the rule is printed in every permission panel."));
    return frag;
  }

  /* ---------------- v16 controls: one row of examples, a green box, Exact match,
     and everything the shell adds folded under "More filters" ----------------
     The owner, 7 September 2026, comparing the portal against the approved v16:
     "lewy pasek zupelnie inny". Measured, the difference was never the panel — it
     was this row. The shell renders three mode buttons, six period buttons and up
     to five selects; v16 has none of them. They do real work, so they are folded,
     not deleted, and ONE function does it for both catalogs so the two tabs cannot
     drift apart. */
  function foldFilters() {
    [].forEach.call(document.querySelectorAll(".catalog[data-catalog]"), function (cat) {
      var ctl = cat.querySelector(".cat-controls"); if (!ctl) return;
      var bar = ctl.querySelector(".cat-toolbar");
      if (!bar || bar.dataset.folded === "1") return;
      bar.dataset.folded = "1";
      var d = el("details", "morefilters");
      var sm = el("summary");
      sm.appendChild(el("span", "sm-t", "More filters"));
      sm.appendChild(el("span", "sm-r", "Microsoft changes · catalog notes · time window · API and entity"));
      d.appendChild(sm);
      bar.parentNode.insertBefore(d, bar.nextSibling);
      d.appendChild(bar);
      var inp = cat.querySelector("input.cat-search");
      if (inp) inp.placeholder = cat.getAttribute("data-catalog") === "roles"
        ? "Search roles" : "Search permissions";
    });
  }

  function build() {
    TABS.forEach(function (T) {
      var panel = document.getElementById(T.id);
      if (!panel || panel.querySelector(".s8top")) return;
      var rows = ENTRIES.filter(function (e2) { return T.ledger.indexOf(e2.tab) >= 0; });
      var box = el("div", "s8top");

      var top = (T.id === "tab-roles") ? rolesTop(panel) : (T.id === "tab-graph" ? graphTop(panel) : null);
      if (top) box.appendChild(top);

      if (L) {
        var det = el("details", "chg14"); det.open = true;
        var sum = el("summary");
        sum.appendChild(el("span", "sm-t", "What changed in the last " + WINDOW_DAYS + " days"));
        sum.appendChild(el("span", "badge t-acc", rows.length + (rows.length === 1 ? " change" : " changes")));
        sum.appendChild(el("span", "sm-r", "· " + Object.keys(RUNS).length + " days with a run"));
        det.appendChild(sum);
        if (rows.length) {
          var lead = el("p", "note");
          lead.textContent = "Only this tab's changes are listed: an entry is counted in the one tab that is its " +
            "home, so nothing appears twice." + (T.kind === "row"
              ? " Press ↗ on any row to jump to it on this page."
              : " Press + on any row to open the same panel the catalog below shows for it.");
          det.appendChild(lead);
          det.appendChild(chart(rows, T.id === "tab-roles" ? "role changes" :
                                      T.id === "tab-graph" ? "catalog changes" : "changes"));
          det.appendChild(table(rows, T.kind, T.ledger));
          det.appendChild(el("p", "note", "Read from site/data/changelog.json, which is appended to and never " +
            "rewritten; it keeps " + ((L && L.retentionDays) || 90) + " days and this page renders " + WINDOW_DAYS + "."));
        } else {
          det.appendChild(el("p", "empty", "No change recorded in this tab in the last " + WINDOW_DAYS +
            " days; " + Object.keys(RUNS).length + " runs looked. That is a result, not a gap."));
        }
        box.appendChild(det);
      }

      var head = panel.querySelector(".panelhead");
      if (head && head.nextSibling) panel.insertBefore(box, head.nextSibling);
      else if (head) panel.appendChild(box);
      else panel.insertBefore(box, panel.firstChild);
    });
  }

  function boot() {
    try { build(); } catch (e) { if (window.console) console.error("[chg14]", e); }
    try { foldFilters(); setTimeout(foldFilters, 400); } catch (e) { if (window.console) console.error("[folds]", e); }
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", function () { setTimeout(boot, 160); });
  else setTimeout(boot, 160);
})();
```

### Walidator — pozycje 49-52 listy §0

- **49** — panel roli jest zbudowany: `.v13pane.v13role` w `.cat-detail-inner` katalogu rol, a jego
  pierwsze dwie sekcje to `At a glance` i `What changed on this role in the last 14 days`.
  Panel uprawnienia ma te sama pierwsza dwojke — **kolejnosc jest pozycja, nie preferencja.**
- **50** — `ledger14` jest w bloku stanu, ma `runs` i `entries`, blokow JSON nadal DWA, a **zaden
  wpis nie niesie encji HTML ani zdania w polu `id`**.
- **51** — kazda zakladka tresciowa ma `details.chg14` zbudowane przez SKRYPT 8: licznik w podpisie
  rowny liczbie wierszy, obie osie wykresu podpisane, a kazdy wiersz z przedmiotem ma `+` (albo `↗`
  w zakladce bez katalogu). Zakladka bez zmian ma zdanie z liczba przebiegow, nie pusty element.
- **52** — `+` otwiera panel: skrypt niesie `__socOpenPerm` i `__socOpenRole`, a klon w wierszu
  historii **nie ma wlasnej sekcji 14 dni**. Bramka czyta plik, wiec sprawdza obecnosc obu funkcji
  i klas; to, czy panel sie wypelnia, sprawdza Playwright (§5h) — i to rozroznienie jest tu cala
  pointa, bo poprzednia wersja bramki dala 45/46 na stronie, ktorej panel byl pusty (§5ak).

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
- Blog: https://techcommunity.microsoft.com/category/microsoft-security/blog/microsoft-defender-xdr-blog
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

### Defender for Office 365
- https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new
- Blog: https://techcommunity.microsoft.com/category/microsoft-security/blog/microsoftdefenderforoffice365blog

### Microsoft Intune
- https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new
- In development: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/in-development
- Blog: https://techcommunity.microsoft.com/category/microsoft-intune/blog/microsoftintuneblog
- **Intune Customer Success** — INNY blog niz powyzszy, nie mylic: https://techcommunity.microsoft.com/blog/intunecustomersuccess

### Microsoft Purview
- https://learn.microsoft.com/en-us/purview/whats-new

### KQL / Hunting
- https://learn.microsoft.com/en-us/kusto/query/
- Azure Data Explorer release notes: https://learn.microsoft.com/en-us/azure/data-explorer/release-notes-cloud

### Poprawki, luki i zdrowie platformy — WSZYSTKIE NOWE, dodane 6 wrzesnia 2026

Wlasciciel przyslal 6 wrzesnia wlasne zestawienie zrodel i porownanie z ta sekcja dalo **15 pozycji
juz obecnych, 9 luk i 1 czesciowa**. Ponizsze dziewiec to te luki. Najwazniejsza jest pierwsza:
**MSRC to Patch Tuesday i zero-daye, i nie bylo ich w tym briefie w ogole.**

- **MSRC Security Update Guide** (Patch Tuesday, zero-daye, CVE): https://msrc.microsoft.com/update-guide
- **Windows Release Health** (znane problemy, wycofania, incydenty): https://learn.microsoft.com/en-us/windows/release-health/
- **M365 Apps — poprawki bezpieczenstwa**: https://learn.microsoft.com/en-us/officeupdates/microsoft365-apps-security-updates
- **Security Copilot blog**: https://techcommunity.microsoft.com/category/microsoft-security/blog/microsoft-security-copilot-blog
- **Windows 365 Cloud PC**: https://learn.microsoft.com/en-us/windows-365/enterprise/whats-new
- **Azure Virtual Desktop**: https://learn.microsoft.com/en-us/azure/virtual-desktop/whats-new

### Wersje komponentow — co da sie zrodlowac, a czego NIE

Wlasciciel poprosil 6 wrzesnia 2026 o zestawienie wersji: Authenticator na iOS i Androida, sensory
MDI i MDE, najnowsze iOS / macOS / watchOS, GSA, Entra Connect, wersja poprzednia (−1) i koniec
wsparcia. **Kazdy adres ponizej zostal tego dnia pobrany i sprawdzony — piec dziala w calosci,
jeden czesciowo, jeden nie dziala wcale, a jednego zrodla po prostu nie ma.** Roznica jest zapisana
co do adresu, bo regula „nigdy nie wymyslaj numeru wersji" obowiazuje tak samo jak dla GUID-ow.
**Wynik negatywny tez jest wynikiem i tez sie go zapisuje** — inaczej nastepny przebieg sprawdza
to samo od zera albo, gorzej, wpisuje numer, ktorego nie widzial.

| co | zrodlo | zmierzone 6 wrzesnia 2026 |
|---|---|---|
| **MDE — Windows, macOS, Linux, Android, iOS naraz** | `learn.microsoft.com/defender-endpoint/microsoft-defender-endpoint-releases` | JEDNA tabela: OS, build, miesiac, wersja silnika i sygnatur, szesc miesiecy wstecz. Ta strona **byla juz w §7** — po prostu nie wyciagalismy z niej wersji |
| **MDI sensor** | `learn.microsoft.com/defender-for-identity/whats-new` | tabela `Version number / Updates`, pelny numer (np. `2.255.19295.47272`); takze migracja v2.x → v3.x |
| **Entra Connect, Cloud Sync, GSA Windows/macOS, Private Access Sensor, private network connector** | strony release history juz wymienione wyzej w §7 | bez zmian |
| **iOS, iPadOS, macOS, watchOS, tvOS, visionOS, Safari** | `support.apple.com/en-us/100100` | **dziala** — plain HTML table, produkt + wersja + data wydania, wszystkie systemy Apple i Safari w jednym miejscu |
| **macOS: wersja biezaca i POPRZEDNIE gałęzie** | `support.apple.com/pl-pl/109033` | **dziala, ale tylko macOS** — tabela „ktora wersja jest najnowsza" per wydanie glowne. To jest zrodlo dla „wersji −1": Tahoe 26.6.2, Sequoia 15.7.9, Sonoma 14.8.9 |
| **Authenticator iOS — ZRODLO KANONICZNE** | `itunes.apple.com/lookup?id=983156458&country=us` | **dziala w calosci** — oficjalne API Apple, czysty JSON: `version` `6.8.54`, `currentVersionReleaseDate` **`2026-08-31T20:00:12Z`**, `minimumOsVersion` `17.0`, `fileSizeBytes` `233716736`, `sellerName` `Microsoft Corporation`. **To API rozwiazuje problem daty wzglednej** — podaje date pelna, z sekundami, zamiast `5d ago` ze strony sklepu |
| **Authenticator iOS — strona sklepu** | `apps.apple.com/us/app/microsoft-authenticator/id983156458` | **dziala polowicznie, wiec juz jej nie uzywamy do daty** — numer i minimalne iOS sa, ale data jest WZGLEDNA (`5d ago`), a „What's New" to staly tekst marketingowy. Zostaje wylacznie jako kontrola krzyzowa numeru |
| **Authenticator Android — oficjalny Google Play** | `play.google.com/store/apps/details?id=com.azure.authenticator` | **NIE podaje numeru wersji przy odczycie server-side.** Zmierzone 6 wrzesnia 2026, dwa adresy: strona glowna zwraca wylacznie `Updated on Aug 26, 2026`, a podstrona `datasafety` konczy sie `ROBOTS_DISALLOWED`. Numer siedzi w bloku `AF_initDataCallback` za modalem „Informacje o aplikacji", ktorego konwersja do markdown nie widzi — i **innej drogi nie probujemy** (zasada systemowa: czego nie da sie pobrac WebFetch-em, tego nie pobiera sie curl-em ani Pythonem) |
| **Authenticator Android — historia wersji u Microsoftu** | — | **NIE ISTNIEJE.** Wyszukanie 6 wrzesnia 2026 po `learn.microsoft.com` zwrocilo same watki Q&A **pytajace** o release notes tej aplikacji, ani jednej strony je publikujacej |
| **Authenticator Android — TRZY LUSTRA, werdykt przez ZGODNOSC** | `apkmirror.com/apk/microsoft-corporation/microsoft-authenticator/` · `appglint.com/app/google-play/com.azure.authenticator` · `global.app.mi.com/details?id=com.azure.authenticator` | **wszystkie trzy dzialaja i wszystkie trzy podaja `6.2608.5658`.** APKMirror daje pelna historie (10 wydan wstecz, wiec **stad bierzemy wersje −1**: `6.2607.4697`); AppGlint to lustro metadanych Google Play i podaje **pelny znacznik czasu** `8/26/2026, 10:44:11 PM`, zgodny z oficjalnym `Updated on Aug 26, 2026` u Google; Xiaomi podaje `6.2608.5658`, `27.08.2026`, `60.9 MB` |
| **Authenticator Android — lustro Aptoide, czwarta kontrola** | `microsoft-corporation-authenticator.en.aptoide.com/versions` | ten sam numer `6.2608.5658`. **Kolumna daty jest niespojna** — wiersze 4 i 5 niosa `5/9/2026` i `4/9/2026` przy STARSZYCH numerach kompilacji |

**Trzy reguly, ktore z tego wynikaja i sa wiazace:**

1. **Data wzgledna nie jest data — ale dla iOS mamy juz date prawdziwa.** Strona App Store podaje
   `5d ago`; **API `itunes.apple.com/lookup` podaje `currentVersionReleaseDate` z sekundami**, wiec
   dla Authenticatora na iOS `released` jest wypelnione data z API, a nie `null`. Regula zostaje
   w mocy wszedzie indziej: **nigdy nie przeliczasz `5d ago` ani `Updated on` na date wydania**
   i nie podajesz jej jako daty Microsoftu. `versionSeenOn` = data przebiegu, zawsze.
2. **Wersja Authenticatora na Androida ma trzy pola i powstaje przez ZGODNOSC LUSTER, nie przez
   zaufanie jednemu.** Zadne oficjalne, maszynowo czytelne zrodlo jej nie podaje: Google Play nie
   wystawia numeru przy odczycie server-side, a Microsoft nie publikuje historii wersji tej aplikacji
   wcale. Procedura, zmierzona 6 wrzesnia 2026 na czterech lustrach:
   - `officialUpdated` — data `Updated on` z Google Play, `vendorConfirmed:true`. **Jedyna liczba
     z oficjalnego zrodla** i tylko ona stoi bez przypisu.
   - `mirrorVersion` — numer, ktory podalo **co najmniej DWA niezalezne lustra**, z lista `mirrors`
     (nazwa, adres, odczytana wartosc, data odczytu) i `vendorConfirmed:false`. Zmierzone: APKMirror,
     AppGlint, Xiaomi i Aptoide podaly **identycznie `6.2608.5658`**, a AppGlint dolozyl znacznik
     `8/26/2026, 10:44:11 PM` zgodny z oficjalnym `Updated on Aug 26, 2026`.
   - `previousVersion` — wersja −1, brana z APKMirror, ktory jako jedyny wozi historie
     (`6.2607.4697` na ten dzien).
   - **Jedno lustro to nie werdykt.** Przy zgodzie jednego zrodla wpis dostaje
     `consensus:"single-source"` i chip `unconfirmed`; strona pokazuje numer, ale mowi, ze potwierdzila
     go jedna strona. Rozjazd miedzy lustrami jest ZNALEZISKIEM i drukuje sie obie wartosci.
   - **Zgodnosc trzech luster nie jest trzema niezaleznymi obserwacjami** — lustra przepisuja od
     siebie i od Google. Dlatego zgodnosc podnosi zaufanie, ale **nie zamienia lustra w zrodlo**
     (§5, §5d): numer nigdy nie jest drukowany jako liczba Microsoftu, zawsze z przypisem nazywajacym
     lustra i date odczytu.
   - **DATY z luster nie bierzemy w ogole.** Zmierzone tego dnia: APKMirror `September 1, 2026`,
     AppGlint `8/26/2026`, Xiaomi `27.08.2026`, Aptoide `26/8/2026` — cztery rozne daty dla jednego
     numeru, bo kazde lustro datuje WLASNE przyjecie pliku. Data pochodzi wylacznie z `Updated on`
     Google Play. Rozjazd wiekszy niz tydzien miedzy nimi daje `mirrorStale:true` z obiema datami.
   - Pole `whatsNew` zostaje `null` dla obu platform: Apple drukuje tam staly tekst marketingowy,
     a Google nie drukuje nic. Puste pole z powodem, nigdy zmyslone zdanie.
   **Rozmiaru pobierania nie porownujesz miedzy zrodlami.** Google podaje go per urzadzenie
   (61 MB dla Samsunga SM-A176B kontra 64 MB u Aptoide, 60,9 MB u Xiaomi) — to nie jest rozbieznosc,
   tylko trzy rozne wielkosci, i wiersz albo nazywa urzadzenie, albo w ogole nie ma tej kolumny.

2a. **Trzy pulapki parsowania luster, kazda zmierzona na prawdziwej tresci — nie powtarzaj ich.**
   Wziely sie z gotowego skryptu PowerShell, ktory wlasciciel przyslal 6 wrzesnia; metoda jest dobra,
   te trzy szczegoly nie:
   - **„Najwyzszy numer na stronie" to nie „najnowsza wersja stabilna".** APKMirror publikuje buildy
     beta, a wzorzec `(\d+\.\d+\.\d+)` obcina sufiks `-beta`, wiec `max()` wybiera bete. Bierzesz
     **pierwszy wiersz listy wydan**, nie maksimum, i odrzucasz wiersz z `beta` albo `alpha` w tekscie.
   - **Wzorzec `(?:Version|Wersja)\s*[\r\n\t ]*(\d+\.\d+\.\d+)` lapie takze wymaganie systemu.**
     Na tresci `Android version 8.0.0 required` zwraca `8.0.0` obok wlasciwego numeru. Kotwicz wzorzec
     na nazwie pakietu albo na naglowku sekcji, nie na samym slowie „Version".
   - **Porownanie wersji idzie po LICZBACH, nie po napisie.** `6.9.1` kontra `6.10.1`: sortowanie
     tekstowe malejaco daje `6.9.1`, bo `9` > `1`. Rozbijasz na krotke liczb calkowitych.

3. **Apple to nie Microsoft, i strona ma to mowic.** Wiersze z `support.apple.com` niosa
   `vendor:"Apple"`, zeby czytelnik nie wzial ich za komunikat Microsoftu. Sa w briefie dlatego, ze
   minimalna wersja iOS/macOS rozstrzyga, czy sensor MDE albo Authenticator w ogole ruszy.

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
