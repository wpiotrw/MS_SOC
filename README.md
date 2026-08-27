# MS_SOC

Automatyczny monitoring zmian w dokumentacji Microsoft, rolach i uprawnieniach Graph.

- Raport poranny: strona glowna
- Zmiany od rana: `/diff/`

Tresc generuja scheduled tasks (Claude Code routines) i commituja do `site/`.
Push do `main` uruchamia deploy do Azure Static Web Apps.

Szczegoly w `CLAUDE.md`.
