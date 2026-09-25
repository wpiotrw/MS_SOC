# MS_SOC — Microsoft SOC Brief

| Pole | Wartość |
|---|---|
| Autor | Piotr Wiśniewski — APN Promise S.A. |
| Strona | https://orange-ground-019f30603.7.azurestaticapps.net/ |
| Źródło prawdy dla kodu i reguł | `CLAUDE.md` (ten plik tylko opisuje całość i to, czego nie ma w `CLAUDE.md`) |

Codzienny portal zmian Microsoftu dla SOC: brief poranny (strona główna), strona zmian `/diff/`, przegląd tygodnia `/week/`, kanał RSS `/feed.xml`. Treść budują zadania Claude (scheduled task i routines) według `CLAUDE.md`; GitHub Actions publikuje katalog `site/` w Azure Static Web Apps.

**Po co ten plik:** żeby po zmianie tenanta, konta Azure albo repozytorium dało się wszystko odtworzyć bez zgadywania. Wszystko, co leży poza repozytorium (aplikacja Entra, zasób Static Web App, sekrety, harmonogramy), jest opisane niżej razem z identyfikatorami.

## Skróty

| Skrót | Rozwinięcie |
|---|---|
| SOC | Security Operations Center — centrum operacji bezpieczeństwa |
| SWA | Azure Static Web Apps — hosting strony |
| OIDC | OpenID Connect — tu: token GitHub Actions wymieniany na token Entra |
| WIF | Workload Identity Federation — logowanie aplikacji Entra tokenem OIDC, bez sekretu |
| FPA | First-party apps — aplikacje Microsoftu w Entra ID |
| MC | Message Center — komunikaty Microsoft 365 |
| CA | Conditional Access — dostęp warunkowy Entra |
| FOCI | Family of Client IDs — rodzina aplikacji Microsoftu współdzielących token odświeżania |

## 1. Jak to działa (przepływ dnia)

Czasy w strefie Europe/Warsaw (w nawiasie UTC przy czasie letnim).

| Kiedy | Co | Gdzie działa | Wynik |
|---|---|---|---|
| 05:30 (03:30) | `.github/workflows/fpa-tenant.yml` — migawka tenanta dla zakładki First-party apps | GitHub Actions | `site/data/fpa-tenant.json` (commit na `main`) |
| 06:00 (04:00) | scheduled task „raport poranny” — buduje artefakt briefu wg `CLAUDE.md` (kolektory, blok stanu, skrypty 4–17) | Claude (chmura) | artefakt claude.ai z briefem dnia |
| 07:00 (05:00) | routine „raport poranny v2” — lustro artefaktu (`mirror_artifact.py --brief`) | Claude (chmura) | `site/index.html`, `site/data/<data>.json`, `site/feed.xml`, `site/data/history.json`, `site/week/index.html` |
| 21:00 (19:00) | scheduled task popołudniowy — dopisuje sekcję `#pmdelta` do artefaktu i publikuje artefakt „Microsoft SOC Delta” (`make_diff.py`) | Claude (chmura) | artefakt dnia (nowa wersja) i artefakt Delta |
| 22:00 (20:00) | routine „zmiany v2” — buduje `/diff/` (`make_diff.py` z `CLAUDE.md`) | Claude (chmura) | `site/diff/index.html`, plik stanu końcowego dnia |
| każdy push na `main` w `site/**` | `.github/workflows/azure-static-web-apps-orange-ground-019f30603.yml` | GitHub Actions | wdrożenie na SWA |
| push na gałąź `claude/**` w `site/**` | `.github/workflows/publish.yml` — przenosi `site/` z gałęzi rutyny na `main` | GitHub Actions | commit na `main` → wdrożenie |

Zasady, które trzymają całość w ryzach (szczegóły w `CLAUDE.md`):

- Kod dodawany do strony (skrypty 4–17, bloki CSS, kolektory, `gate.py`, `make_diff.py`, `mirror_artifact.py`) **wycina się z `CLAUDE.md`** skryptem `extract_code.py` (§0c) — nigdy nie przepisuje się go ręcznie ani nie kopiuje z wczorajszej strony. Prompty zadań wskazują na `CLAUDE.md`, więc zmiana kodu nie wymaga zmiany promptów.
- `gate.py` (§0b) to bramka publikacji; pozycje klasy B są raportowane, nie blokują.
- Rejestr uzgodnień (§0f) mówi, co jest zbudowane, a co tylko zaspecyfikowane.

## 2. Repozytorium

| Ścieżka | Zawartość |
|---|---|
| `CLAUDE.md` | reguły, kod i kontrakt strony (jedyne źródło kodu) |
| `community_sources.json`, `microsoftblogs_sources.json`, `microsoftlearn_sources.json` | listy źródeł czytanych przez kolektory |
| `site/` | to, co publikuje SWA (strona, `diff/`, `week/`, `data/`, `history/`, `shell/`, `kql/`, `feed.xml`, `staticwebapp.config.json`) |
| `site/data/<RRRR-MM-DD>.json` | stan dnia (blok `soc-brief-state` + `soc-catalog`); `/diff/` i historia liczą z nich zmiany |
| `site/data/fpa-tenant.json` | migawka tenanta dla zakładki First-party apps (pkt 5) |
| `tools/fpa_tenant.py` | skrypt tej migawki (uruchamia go workflow) |
| `.github/workflows/` | wdrożenie SWA, publikacja z gałęzi rutyn, migawka tenanta |

## 3. Azure Static Web App (hosting)

| Pole | Wartość |
|---|---|
| Adres | https://orange-ground-019f30603.7.azurestaticapps.net/ |
| Nazwa zasobu (z nazwy hosta i workflow) | `orange-ground-019f30603` |
| Wdrożenie | GitHub Actions, `Azure/static-web-apps-deploy@v1`, `action: upload`, `app_location: /site`, `skip_app_build: true` (strona jest gotowym HTML, nic się nie buduje) |
| Sekret w GitHub (Settings → Secrets and variables → Actions) | `AZURE_STATIC_WEB_APPS_API_TOKEN_ORANGE_GROUND_019F30603` — token wdrożeniowy SWA |
| Konfiguracja strony | `site/staticwebapp.config.json`: `navigationFallback` → `/index.html` z wyłączeniem `/diff/*`, `/history/*`, `/data/*`, `*.json`; nagłówki `cache-control: public, max-age=300, must-revalidate`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer`; typy MIME dla `.json` i `.html` |
| Subskrypcja, grupa zasobów, plan (SKU), region | **do uzupełnienia** — nie są zapisane w repozytorium, a aplikacja Lokka nie ma ról Azure, więc nie dało się ich odczytać 25 IX 2026. Odczyt: Azure Portal → Static Web Apps → `orange-ground-019f30603` → Overview |

**Odtworzenie w nowej subskrypcji / nowym tenancie Azure**

1. Azure Portal → Create → Static Web App; źródło wdrożenia **Other** (nie łączymy z GitHubem z portalu, workflow już jest).
2. Po utworzeniu: Overview → **Manage deployment token** → skopiuj token.
3. GitHub → repozytorium → Settings → Secrets and variables → Actions → sekret o nazwie z workflow (albo zmień nazwę sekretu w `.github/workflows/azure-static-web-apps-orange-ground-019f30603.yml`).
4. Nowa strona ma inny adres `*.azurestaticapps.net`. Zmień go w: `CLAUDE.md` (wyszukaj `orange-ground-019f30603`), `mirror_artifact.py` w `CLAUDE.md` (`site_url` w `write_feed`, `write_week`), w tym pliku i ewentualnie w nazwie pliku workflow.
5. Uruchom workflow wdrożenia ręcznie (Actions → Azure Static Web Apps CI/CD → Run workflow) i sprawdź `/`, `/diff/`, `/week/`, `/feed.xml`.

## 4. Zadania Claude (scheduled task i routines)

| Nazwa | Rodzaj | Czas | Co robi |
|---|---|---|---|
| raport poranny | scheduled task | 06:00 | buduje artefakt briefu wg `CLAUDE.md` |
| raport poranny v2 | routine | 07:00 | lustro artefaktu do `site/` |
| popołudniowy (Delta) | scheduled task | 21:00 | `#pmdelta` w artefakcie dnia, artefakt „Microsoft SOC Delta” |
| zmiany v2 | routine | 22:00 | `/diff/` |

Prompty zadań są zarchiwizowane w projekcie Claude „SchedTasks & Routines” (`claude/backup/…`). Zadań utworzonych przez API nie edytuje się z sesji — zmiany w zachowaniu robi się w `CLAUDE.md`, który prompty czytają.

## 5. Zakładka First-party apps (od 26 IX 2026, `CLAUDE.md` §5bl)

Aplikacje Microsoftu w Entra ID: które istnieją, jakie uprawnienia do API mogą uzyskać (z poziomem L1–L4 Microsoftu), co się zmieniło dzień do dnia, jakie zgody i role mają w naszym tenancie. Sekcja `#fpa` na `/diff/`, eksport CSV (nazwa, appId, uprawnienia).

### 5.1 Źródła publiczne (czyta `collect_fpa.py` w przebiegu porannym)

| Źródło | Plik | Daje | Licencja |
|---|---|---|---|
| merill/microsoft-info | `_info/MicrosoftApps.json` | appId, nazwa, tenant właściciela (sweep Graph w tenancie demo autora, 2× dziennie) | MIT |
| dirkjanm/ROADtools | `roadtx/roadtools/roadtx/firstpartyscopes.json` | uprawnienia per API, FOCI, public client, redirect URI (aktualizowane ręcznie co 1–3 mies.) | MIT |
| zh54321/GraphPreConsentExplorer | `lists/GraphPreConsent.json` | uprawnienia Graph, auth code, device code, FOCI | MIT |
| microsoftgraph/microsoft-graph-devx-content | `permissions/new/permissions.json` | poziom L1–L4 i opis uprawnień Graph | MIT |
| f-bader/entrascopes.com | `resources.json`, `bypasses.json` | nazwy API, znane obejścia CA | brak pliku licencji — tylko odczyt, z podaniem autorów |

Microsoft nie publikuje listy swoich aplikacji ani uprawnień, które nadaje im bez zgody (pre-authorization). Te uprawnienia **wykrywa się, logując się każdą aplikacją** — tak powstają dane ROADtools i Graph Pre-Consent Explorer.

### 5.2 Migawka tenanta (GitHub Actions, bez sekretu)

Źródła publiczne mówią, co aplikacje Microsoftu **mogą** uzyskać. Migawka tenanta mówi, co **zostało im nadane u nas**: zgody delegowane (`oauth2PermissionGrants`) i role aplikacyjne (`appRoleAssignments`) aplikacji spoza naszego tenanta. Czyta ją `tools/fpa_tenant.py`, uruchamiany codziennie przez workflow `fpa-tenant.yml`.

| Pole | Wartość |
|---|---|
| Tenant | Contoso, `ea0d500a-496c-42eb-a3c0-d834e723edc2` (`m365b327862.onmicrosoft.com`) |
| Aplikacja Entra | **MS-SOC First-party apps reader** |
| Application (client) ID | `373c2197-64a1-41a4-a8b4-70719dc89a27` |
| Object ID aplikacji | `7c947ef0-62f1-4228-8ed9-25a1e77733e3` |
| Object ID service principala | `a38f1760-8903-43d4-901c-dd795e8864cb` |
| Uprawnienia (Application, tylko odczyt) | Microsoft Graph → **Application.Read.All** (service principale i ich role aplikacyjne) + **DelegatedPermissionGrant.Read.All** (tylko zgody delegowane) |
| Dlaczego nie Directory.Read.All | Directory.Read.All czyta cały katalog: użytkowników, grupy, urządzenia. Dokumentacja Microsoftu podaje go jako „least privileged” dla `GET /oauth2PermissionGrants`, ale Graph ma węższą rolę **DelegatedPermissionGrant.Read.All** („Read all delegated permission grants”). Jeśli Graph jej nie przyjmie (403), skrypt zapisze migawkę bez zgód delegowanych, z polem `grantsNote`, i nie przerwie działania — wtedy decydujemy, czy dodać Directory.Read.All |
| Zgoda administratora | **DO WYKONANIA RAZ** — pkt 5.3, krok 1 |
| Poświadczenie federacyjne | nazwa `github-ms-soc-main`, issuer `https://token.actions.githubusercontent.com`, subject `repo:wpiotrw/MS_SOC:ref:refs/heads/main`, audience `api://AzureADTokenExchange` |
| Sekrety | **brak** |
| Workflow | `.github/workflows/fpa-tenant.yml` (codziennie 03:30 UTC i ręcznie); do czasu przeniesienia leży w `tools/fpa-tenant.yml` — pkt 5.3, krok 2 |
| Wynik | `site/data/fpa-tenant.json` |
| Utworzono | 25 IX 2026 przez Microsoft Graph (narzędzie Lokka, aplikacja „Lokka-CA-Automation” z Application.ReadWrite.All); pierwsza migawka zrobiona ręcznie tym samym narzędziem |

#### Jak działa logowanie bez sekretu (poświadczenie federacyjne)

1. GitHub Actions dla każdego uruchomienia workflow wystawia **token OIDC** (JWT podpisany przez GitHub) z polami m.in. `iss = https://token.actions.githubusercontent.com` i `sub = repo:wpiotrw/MS_SOC:ref:refs/heads/main`. Workflow może go pobrać tylko wtedy, gdy ma `permissions: id-token: write`.
2. W aplikacji Entra zapisane jest **poświadczenie federacyjne**: „ufaj tokenom od tego wystawcy, z tym `sub` i audience `api://AzureADTokenExchange`”. To zastępuje sekret albo certyfikat.
3. `tools/fpa_tenant.py` (funkcja `token()`):
   - pobiera token OIDC z `ACTIONS_ID_TOKEN_REQUEST_URL` z audience `api://AzureADTokenExchange`;
   - wysyła go do `https://login.microsoftonline.com/<tenant>/oauth2/v2.0/token` jako `client_assertion` (`client_assertion_type = urn:ietf:params:oauth:client-assertion-type:jwt-bearer`, `grant_type = client_credentials`, `scope = https://graph.microsoft.com/.default`);
   - Entra sprawdza podpis GitHuba i zgodność `iss`/`sub`/`aud` z poświadczeniem i wydaje token Graph z uprawnieniami aplikacji.
4. Token Graph żyje około godziny i istnieje tylko w pamięci przebiegu. Nie ma czego ukraść ani odnawiać: token OIDC wystawiony dla innego repozytorium, innej gałęzi albo forka ma inny `sub` i zostanie odrzucony.

Poświadczenie utworzono wywołaniem Graph `POST /applications/7c947ef0-62f1-4228-8ed9-25a1e77733e3/federatedIdentityCredentials` z polami z tabeli wyżej. Skrypt `fpa_tenant.py` go **nie tworzy**, tylko z niego korzysta. Tworzy je skrypt odtworzeniowy niżej (`New-MgApplicationFederatedIdentityCredential`).

#### Dlaczego GitHub Actions i co nam to daje

- **Działa bez nikogo i bez komputera.** Harmonogram GitHuba uruchamia workflow codziennie, niezależnie od sesji Claude i od tego, czy Twój komputer jest włączony.
- **Tożsamość bez sekretu.** Tylko GitHub Actions (i inne systemy z tokenami OIDC) mogą logować się do Entra przez poświadczenie federacyjne. Zadania Claude takiego tokenu nie mają, więc musiałyby trzymać sekret aplikacji w prompcie albo w pliku, a to nie wchodzi w grę.
- **Uprawnienia są przypięte do repozytorium i gałęzi.** Poświadczenie przyjmuje tylko tokeny z `wpiotrw/MS_SOC` i gałęzi `main`, więc kopia repozytorium albo inna gałąź nic nie dostanie.
- **Ślad i powtarzalność.** Każde uruchomienie ma log w zakładce Actions, a każda zmiana migawki jest commitem w historii repozytorium.
- **Jedno miejsce publikacji.** GitHub Actions już wdraża stronę na Static Web App (push w `site/**`) i przenosi wyniki rutyn z gałęzi `claude/**` na `main`. Migawka tenanta jest trzecim workflow w tym samym mechanizmie. Jej commit uruchamia wdrożenie, a poranny przebieg Claude czyta plik z klonu repozytorium.
- **Koszt:** w publicznym repozytorium minuty GitHub Actions są bezpłatne; w prywatnym mieszczą się w limicie darmowym (przebieg trwa około minuty).

### 5.3 Do zrobienia raz (właściciel)

**Krok 1 — zgoda administratora (formatka w Entra)**

1. Otwórz stronę uprawnień aplikacji w Entra admin center (konto z rolą Privileged Role Administrator albo Global Administrator):
   https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/CallAnAPI/appId/373c2197-64a1-41a4-a8b4-70719dc89a27/isMSAApp~/false
   Jeśli link nie otworzy właściwej strony: **Entra admin center → Identity → Applications → App registrations → All applications → MS-SOC First-party apps reader → API permissions**.
2. Sprawdź, że lista zawiera dokładnie dwie pozycje Microsoft Graph typu **Application**: `Application.Read.All` i `DelegatedPermissionGrant.Read.All`.
3. Kliknij **Grant admin consent for Contoso** → **Yes**. Kolumna Status pokaże zielone „Granted for Contoso”.

**Krok 2 — przeniesienie workflow do `.github/workflows` (PowerShell + git + gh)**

Narzędzia Claude nie mogą zapisywać w `.github/workflows` (ochrona plików CI), dlatego plik czeka w `tools/fpa-tenant.yml`.

```powershell
# 1. Klon repozytorium (ten sam, przez który Claude wypycha zmiany)
Set-Location "$env:LOCALAPPDATA\Temp\mssoc-repo"   # katalog Temp: jesli go nie ma, sklonuj: git clone https://github.com/wpiotrw/MS_SOC.git
git pull origin main

# 2. Przeniesienie pliku do katalogu workflow
git mv tools/fpa-tenant.yml .github/workflows/fpa-tenant.yml
git commit -m "ci: workflow migawki tenanta dla zakladki First-party apps"

# 3. Push. Zmiana pliku workflow wymaga tokenu z zakresem "workflow".
#    Git na tym komputerze loguje sie przez Git Credential Manager (credential.helper = manager),
#    ktory zwykle ma ten zakres. Jesli push zwroci "refusing to allow ... to create or update workflow",
#    dodaj zakres w gh i ustaw gh jako pomocnika logowania gita, potem powtorz push:
#    gh auth refresh -h github.com -s workflow
#    gh auth setup-git
git push origin main

# 4. Pierwsze uruchomienie i podglad (bez czekania do 05:30).
#    gh nie jest w PATH na komputerze apn-k622-2024 (sprawdzone 25 IX 2026);
#    instalacja: winget install --id GitHub.cli, potem nowe okno PowerShell i: gh auth login
#    Bez gh: github.com/wpiotrw/MS_SOC -> Actions -> "First-party apps tenant snapshot" -> Run workflow (main)
gh workflow run fpa-tenant.yml --repo wpiotrw/MS_SOC --ref main
Start-Sleep -Seconds 10
gh run list --repo wpiotrw/MS_SOC --workflow fpa-tenant.yml --limit 1
gh run watch --repo wpiotrw/MS_SOC $(gh run list --repo wpiotrw/MS_SOC --workflow fpa-tenant.yml --limit 1 --json databaseId --jq ".[0].databaseId")
```

Poprawny przebieg kończy się linią `OK site/data/fpa-tenant.json: …` i commitem `data: first-party apps tenant snapshot …` na `main`. Jeśli pojawi się `AADSTS70021` (brak pasującego poświadczenia federacyjnego), workflow nie uruchomił się z gałęzi `main`. Błąd `403` przy `servicePrincipals` oznacza, że krok 1 nie został wykonany.

**Odtworzenie na innym tenancie** (Graph PowerShell, konto z rolą Cloud Application Administrator albo wyższą; nadanie zgody wymaga Privileged Role Administrator albo Global Administrator):

```powershell
$TenantId = "00000000-0000-0000-0000-000000000000"   # wpisz ID nowego tenanta
Connect-MgGraph -TenantId $TenantId -Scopes "Application.ReadWrite.All","AppRoleAssignment.ReadWrite.All"
$graph = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"
$roles = $graph.AppRoles | Where-Object { $_.Value -in "Application.Read.All","DelegatedPermissionGrant.Read.All" }
$app = New-MgApplication -DisplayName "MS-SOC First-party apps reader" -SignInAudience AzureADMyOrg `
  -RequiredResourceAccess @{ ResourceAppId = $graph.AppId; ResourceAccess = @($roles | ForEach-Object { @{ Id = $_.Id; Type = "Role" } }) }
$sp  = New-MgServicePrincipal -AppId $app.AppId
New-MgApplicationFederatedIdentityCredential -ApplicationId $app.Id -BodyParameter @{
  name = "github-ms-soc-main"; issuer = "https://token.actions.githubusercontent.com"
  subject = "repo:wpiotrw/MS_SOC:ref:refs/heads/main"; audiences = @("api://AzureADTokenExchange") }
foreach ($r in $roles) {
  New-MgServicePrincipalAppRoleAssignedTo -ServicePrincipalId $graph.Id -BodyParameter @{
    principalId = $sp.Id; resourceId = $graph.Id; appRoleId = $r.Id } | Out-Null }
"AZURE_TENANT_ID=$((Get-MgContext).TenantId)  AZURE_CLIENT_ID=$($app.AppId)"
```

Wypisane wartości wpisz w `env:` pliku `.github/workflows/fpa-tenant.yml` i uruchom workflow ręcznie. Jeśli zmieni się nazwa repozytorium albo gałąź, zmień `subject` poświadczenia (`repo:<właściciel>/<repo>:ref:refs/heads/<gałąź>`).

**Usunięcie** (gdy zakładka nie jest już potrzebna): usuń aplikację w App registrations (usuwa też service principal i poświadczenie) oraz plik workflow.

## 6. Pliki danych na stronie

| Plik | Pisze | Uwagi |
|---|---|---|
| `site/data/<data>.json` | lustro poranne; przebieg wieczorny nadpisuje stanem końcowym dnia | od 26 IX 2026 zawiera klucz `fpa` |
| `site/data/history.json` | lustro poranne (`write_history`) | historia wartości wpisów z 14 dni |
| `site/data/fpa-tenant.json` | workflow `fpa-tenant.yml` | migawka tenanta |
| `site/feed.xml` | lustro poranne (`write_feed`) | RSS: terminy ≤ 7 dni, nowe, zmiany Graph i ról |
| `site/week/index.html` | lustro poranne (`write_week`) | przegląd tygodnia, druk do PDF |

## 7. Gdy coś przestanie działać

| Objaw | Gdzie patrzeć |
|---|---|
| Strona nie odświeżyła się rano | GitHub → Actions: ostatni przebieg wdrożenia SWA i `publish.yml`; historia uruchomień rutyny w Claude |
| Zakładka First-party apps mówi „No first-party app data” | przebieg poranny nie uruchomił `collect_fpa.py` (pozycja 114 bramki); źródło nieodczytane widać w panelu źródeł zakładki |
| Kolumna „consented here” pusta | brak `site/data/fpa-tenant.json` albo workflow kończy się błędem 403 — brak zgody administratora (pkt 5.3); pole `grantsNote` w pliku = Graph nie przyjął DelegatedPermissionGrant.Read.All |
| `/diff/` pokazuje „baseline” przy First-party apps | pierwszy dzień z kluczem `fpa` albo poprzedni stan go nie ma — to poprawne |

## Historia zmian

| Data | Zmiana |
|---|---|
| 2026-09-25 | Uprawnienia aplikacji zawężone z Directory.Read.All do Application.Read.All + DelegatedPermissionGrant.Read.All; opis logowania federacyjnego, uzasadnienie GitHub Actions, instrukcja zgody administratora i przeniesienia workflow (PowerShell, git, gh). |
| 2026-09-25 | Pełny opis: przepływ dnia, repozytorium, Azure Static Web App (z pozycjami do uzupełnienia), zadania Claude, zakładka First-party apps ze źródłami, aplikacją Entra „MS-SOC First-party apps reader”, poświadczeniem federacyjnym, instrukcją odtworzenia na innym tenancie, pliki danych, diagnostyka. Poprzednia wersja miała 11 linii. |
