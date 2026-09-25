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

| Pole | Wartość |
|---|---|
| Tenant | Contoso, `ea0d500a-496c-42eb-a3c0-d834e723edc2` (`m365b327862.onmicrosoft.com`) |
| Aplikacja Entra | **MS-SOC First-party apps reader** |
| Application (client) ID | `373c2197-64a1-41a4-a8b4-70719dc89a27` |
| Object ID aplikacji | `7c947ef0-62f1-4228-8ed9-25a1e77733e3` |
| Object ID service principala | `a38f1760-8903-43d4-901c-dd795e8864cb` |
| Uprawnienie | Microsoft Graph → **Directory.Read.All (Application)**, tylko odczyt; to najmniejsze uprawnienie, które Microsoft podaje dla `GET /oauth2PermissionGrants`, i obejmuje też service principale i przypisania ról aplikacyjnych |
| Zgoda administratora | **DO WYKONANIA RAZ** (stan na 25 IX 2026): Entra admin center → App registrations → MS-SOC First-party apps reader → API permissions → **Grant admin consent for Contoso**. Aplikacja Lokka, którą utworzono aplikację, nie ma `AppRoleAssignment.ReadWrite.All`, więc nie mogła nadać zgody sama (odpowiedź Graph 403) |
| Poświadczenie federacyjne | nazwa `github-ms-soc-main`, issuer `https://token.actions.githubusercontent.com`, subject `repo:wpiotrw/MS_SOC:ref:refs/heads/main`, audience `api://AzureADTokenExchange` |
| Sekrety | **brak** — token OIDC GitHub jest asercją klienta |
| Workflow | `.github/workflows/fpa-tenant.yml` (codziennie 03:30 UTC i ręcznie) — **plik czeka w `tools/fpa-tenant.yml`**: narzędzia Claude nie mogą zapisywać w `.github/workflows` (ochrona plików CI), więc przeniesienie robi się raz ręcznie: `git mv tools/fpa-tenant.yml .github/workflows/fpa-tenant.yml`, commit, push; `permissions: id-token: write, contents: write`, zmienne `AZURE_TENANT_ID` i `AZURE_CLIENT_ID` wpisane w pliku (nie są tajne) |
| Wynik | `site/data/fpa-tenant.json`: liczba service principali, zgody delegowane i role aplikacyjne aplikacji spoza tenanta |
| Utworzono | 25 IX 2026 przez Graph (Lokka, aplikacja „Lokka-CA-Automation”); pierwsza migawka zrobiona ręcznie tym samym narzędziem |

**Odtworzenie na innym tenancie** (Graph PowerShell, konto z rolą Cloud Application Administrator albo wyższą; nadanie zgody wymaga Privileged Role Administrator albo Global Administrator):

```powershell
$TenantId = "00000000-0000-0000-0000-000000000000"   # wpisz ID nowego tenanta
Connect-MgGraph -TenantId $TenantId -Scopes "Application.ReadWrite.All","AppRoleAssignment.ReadWrite.All"
$graph = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"
$role  = $graph.AppRoles | Where-Object Value -eq "Directory.Read.All"
$app = New-MgApplication -DisplayName "MS-SOC First-party apps reader" -SignInAudience AzureADMyOrg `
  -RequiredResourceAccess @{ ResourceAppId = $graph.AppId; ResourceAccess = @(@{ Id = $role.Id; Type = "Role" }) }
$sp  = New-MgServicePrincipal -AppId $app.AppId
New-MgApplicationFederatedIdentityCredential -ApplicationId $app.Id -BodyParameter @{
  name = "github-ms-soc-main"; issuer = "https://token.actions.githubusercontent.com"
  subject = "repo:wpiotrw/MS_SOC:ref:refs/heads/main"; audiences = @("api://AzureADTokenExchange") }
New-MgServicePrincipalAppRoleAssignedTo -ServicePrincipalId $graph.Id -BodyParameter @{
  principalId = $sp.Id; resourceId = $graph.Id; appRoleId = $role.Id }
"AZURE_TENANT_ID=$((Get-MgContext).TenantId)  AZURE_CLIENT_ID=$($app.AppId)"
```

Potem wpisz obie wartości w `env:` pliku `.github/workflows/fpa-tenant.yml` i uruchom workflow ręcznie. Jeśli zmieni się nazwa repozytorium albo gałąź, zmień `subject` poświadczenia federacyjnego (`repo:<właściciel>/<repo>:ref:refs/heads/<gałąź>`).

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
| Kolumna „consented here” pusta | brak `site/data/fpa-tenant.json` albo workflow kończy się błędem 403 — brak zgody administratora (pkt 5.2) |
| `/diff/` pokazuje „baseline” przy First-party apps | pierwszy dzień z kluczem `fpa` albo poprzedni stan go nie ma — to poprawne |

## Historia zmian

| Data | Zmiana |
|---|---|
| 2026-09-25 | Pełny opis: przepływ dnia, repozytorium, Azure Static Web App (z pozycjami do uzupełnienia), zadania Claude, zakładka First-party apps ze źródłami, aplikacją Entra „MS-SOC First-party apps reader”, poświadczeniem federacyjnym, instrukcją odtworzenia na innym tenancie, pliki danych, diagnostyka. Poprzednia wersja miała 11 linii. |
