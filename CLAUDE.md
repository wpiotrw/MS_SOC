# MS_SOC — instrukcja dla scheduled tasks (routines)

Repozytorium hostuje statyczna strone publikowana automatycznie do Azure Static Web Apps.
Kazdy push do `main`, ktory dotyka katalogu `site/`, uruchamia deploy.

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

   To jedyna dozwolona zmiana w skryptach powloki i jest to zmiana danych, nie logiki.
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

Render headless at 1500x1000 in light AND dark and assert — every one of these has caught a real regression: no console or page errors; exactly one visible `.tabpanel`; `nav.anchors .tab` is 9, labels human, strip not overflowing, also at 1280px; **`header.top .hdr-tools` holds the Theme button and a `select.globalfilter` whose first option is `All products`, and every `header.top .counts a.count` is mirrored into a `#tab-overview .stat` tile**; **every panel except Overview and Sources has exactly one `.panelhead`, built by the script, carrying ≥1 `.stat` and ≥1 `figure.chart`**; **every panel that lists a deadline inside 60 days shows a `🔥 under 30 days` or `⚠️ 30–60 days` chip — absent means the rows lack the emoji**; **`.badge` count across the page is in the hundreds, not the tens**; a picks product chip leaves only that product's rows, raises a `.filterbanner`, Clear filter restores them; **`.filterbanner[hidden]` computes to `display:none`, and with a filter active the banner is visible with a non-empty `.fb-msg`**; **`.cat-controls` is `position:sticky` at desktop width and the search input stays in the viewport after scrolling `.cat-split` into view**; both catalogs render a non-zero count and three modes — Microsoft changes / Catalog notes / All — defaulting to the first with no `catalog`/`brief` entry in it; **`.badge.b-undoc` and `.badge.b-elsewhere` both have a non-transparent background and a non-zero `border-radius` in both themes, and each is carried by at least one rendered chip**; **`.cat-changed` scrollHeight may exceed its clientHeight but `.cat-searchrow` is within 480 px of the panel top; `details.foldnote>summary` computes a font-size of at least 14 px; `.card-title` has a non-transparent background and a non-zero border-radius; every open `details.foldnote` body contains a `ul` and no bare `p` over 40 words**; `scrollWidth` never exceeds client width; **open a role with actions: the action table holds exactly as many rows as `actionsFull`, the count line carries the provenance sentence, `.cp-privbtn` filters to privileged-only with `aria-pressed="true"` and toggles back, and `.cp-verify` links a real `entra-docs/blob/main/.../includes/<slug>.md` URL**. Skip this step rather than failing the run if Playwright is missing.

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
```

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
