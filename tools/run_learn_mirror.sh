#!/usr/bin/env bash
# §5cf (29 IX 2026): jeden przebieg wlasnej kopii stron Learn dla wszystkich grup mirror/learn/*.
# Uzywa go workflow learn-mirror.yml i mozna go uruchomic recznie z katalogu repozytorium.
#   tools/run_learn_mirror.sh [minuty na grupe] [plik na opis commita]
# Nie commituje — robi to wywolujacy. Kod wyjscia != 0 tylko gdy WSZYSTKIE grupy zawiodly
# albo wykryto kolizje sciezek; pojedyncza nieudana grupa jest wypisana i zostaje na nastepny raz.
set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
MIN="${1:-6}"
MSG="${2:-$REPO/.git/learn-mirror-message.txt}"
TOOL="$REPO/tools/learn-mirror/learn-mirror.js"

python3 "$REPO/tools/mirror_scope.py" "$REPO" || exit 1

: > "$MSG.body"
ok=0; failed=0; changed=0
for d in "$REPO"/mirror/learn/*/; do
  g="$(basename "$d")"
  [ -f "$d/learn-mirror.config.json" ] || continue
  m="$(mktemp)"
  if (cd "$d" && node "$TOOL" --max-minutes="$MIN" --message-file="$m" >"$m.log" 2>&1); then
    ok=$((ok+1))
    if [ -s "$m" ] && grep -q '^Mirror Learn:' "$m" && ! grep -q '^Mirror Learn: metadata only' "$m"; then
      changed=$((changed+1))
      { echo "## $g"; sed -n '1p;/^[AMD] /p' "$m"; echo; } >> "$MSG.body"
    fi
    echo "OK   $g: $(grep -E '^📥|No content changes' "$m.log" | tr '\n' ' ')"
  else
    failed=$((failed+1))
    echo "FAIL $g: $(tail -3 "$m.log" | tr '\n' ' ')"
  fi
  rm -f "$m" "$m.log"
done

{ echo "mirror: Learn pages $(date -u +%F) - $changed of $((ok+failed)) groups changed, $failed failed"; echo;
  cat "$MSG.body"; } > "$MSG"
rm -f "$MSG.body"
echo "groups ok=$ok failed=$failed changed=$changed"

python3 "$REPO/tools/mirror_scope.py" "$REPO" --check || exit 3
[ "$ok" -gt 0 ] || exit 2
