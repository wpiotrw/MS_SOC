# mirror/ — własna kopia stron Microsoft Learn używanych przez portal

| Pole | Wartość |
|---|---|
| Autor | Piotr Wiśniewski — APN Promise S.A. |
| Od | 2026-09-29 (CLAUDE.md §5cf) |
| Workflow | `.github/workflows/learn-mirror.yml`, 4 razy na dobę |
| Narzędzie | `tools/learn-mirror/learn-mirror.js` (kopia `merill/learn-mirror`, MIT) |

## Po co
Microsoft zamyka publiczne repozytoria dokumentacji (zapowiedź z 23 IX 2026, koniec „do końca
grudnia 2026”). Zamknięte repozytorium znika razem z historią, więc nie da się już sprawdzić, co
zmieniło się W ŚRODKU strony. Ten folder trzyma historię tych stron w naszym repozytorium,
niezależnie od Microsoftu i od cudzych mirrorów.

## Co jest w środku
- `learn/<obszar>/` — obszar to pierwszy segment adresu Learn (`entra`, `intune`, `azure`, `graph`…).
  Strona leży pod ścieżką pliku źródłowego, z którego Learn ją zbudował (`source_path`).
- `learn/<obszar>/.learn-mirror/seed-urls.txt` — strony z zakresu; plik tylko rośnie.
- `learn/<obszar>/.learn-mirror/state.json` — ETagi i metadane publikacji.

Zakres liczy `tools/mirror_scope.py` przy każdym przebiegu: każdy adres Learn z najnowszego
`site/data/RRRR-MM-DD.json` i każdy z `microsoftlearn_sources.json`. Strona raz zacytowana zostaje
w kopii; znika tylko wtedy, gdy Learn odpowie 404 albo przekierowaniem.

Historia zmian strony: `git log -p -- mirror/learn/<obszar>/<ścieżka>.md`.

## Licencja i autorstwo treści
Treść stron w `learn/` to © Microsoft Corporation, publikowana na Microsoft Learn na licencji
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
Źródłem każdej strony jest adres `https://learn.microsoft.com/en-us/<…>` zapisany w jej nagłówku
(`canonicalUrl`, `original_content_git_url`). Treść jest zapisana tak, jak Learn ją podaje w formacie
Markdown; usunięte są tylko pola, które Learn przepisuje przy każdej publikacji (`updated_at`,
`git_commit_id`, `gitcommit`, `word_count`).
