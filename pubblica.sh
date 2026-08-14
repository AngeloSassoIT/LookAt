#!/bin/bash
# Pubblica il sito su GitHub Pages, e VERIFICA che sia arrivato tutto.
#
#   ./pubblica.sh
#
# Perché esiste: il caricamento a mano con «Add file → Upload files» del 14 ago
# 2026 si è fermato a metà senza dire niente. Erano arrivate 20 pagine su 39
# (l'ultima completa era `fr/`, poi `it/index.html` e basta) e mancava anche
# `.nojekyll`, perché il trascinamento del browser scarta i file che iniziano
# con un punto. Nessun errore a schermo, sito apparentemente online.
#
# Un push git non ha quel difetto: o arriva tutto, o fallisce dicendolo. E il
# controllo finale qui sotto chiama davvero le 39 pagine, perché «git ha detto
# ok» non è la stessa cosa di «la pagina risponde».
#
# La prima volta serve l'accesso a GitHub (una sola volta per sempre):
#   gh auth login          → HTTPS → autenticazione via browser
set -euo pipefail
cd "$(dirname "$0")"

# ⚠️ Maiuscole come le scrive GitHub: con `angelosassoit` il push funziona lo
# stesso ma risponde «This repository moved», perché il nome canonico
# dell'account è AngeloSassoIT. L'indirizzo del sito resta invece tutto
# minuscolo: quello è un nome di host.
REPO="https://github.com/AngeloSassoIT/LookAt.git"
RAMO="main"
SITO="https://angelosassoit.github.io/LookAt"

command -v git >/dev/null || { echo "git non installato"; exit 1; }

# ── 1. il sito deve essere quello rigenerato, non uno stato intermedio
python3 _sorgenti/genera-sito.py --base-url "$SITO" --scrivi-url-asc

# ── 2. repository locale, allineato al remoto
if [ ! -d .git ]; then
  git init -b "$RAMO" >/dev/null
  git remote add origin "$REPO"
fi
git remote set-url origin "$REPO"

# `git reset` (mixed) porta HEAD e indice al commit remoto SENZA toccare i file:
# subito dopo, `git add -A` mette in stagione esattamente la differenza fra ciò
# che è online e ciò che c'è qui — file mancanti compresi.
git fetch origin "$RAMO"
git reset "origin/$RAMO" >/dev/null 2>&1 || true

git add -A
if git diff --cached --quiet; then
  echo "· niente da pubblicare: il repository è già allineato"
else
  git -c user.name="SimpleBuild" -c user.email="support@simplebuild.it" \
      commit -q -m "Sito LookAt: 13 lingue complete, canonical/hreflang/sitemap"
  git push origin "$RAMO"
  echo "· push eseguito — GitHub Pages ricostruisce in un minuto circa"
fi

# ── 3. controllo vero: ogni pagina deve rispondere **ed essere quella nuova**
#
# ⚠️ Non basta il 200. Il 14 ago 2026 il sito era già aggiornato e la CDN di
# GitHub Pages continuava a servire la versione precedente: tutte le pagine
# rispondevano 200 con dentro un testo che avevamo appena tolto. Quindi si
# confronta l'impronta del file servito con quella del file locale, e la
# richiesta porta un parametro variabile per non ripescare la stessa cache.
echo "· attendo la ricostruzione di GitHub Pages…"
LINGUE=("" "en-us/" "it/" "es-es/" "es-mx/" "fr/" "de/" "pt-br/" "nl/" "ja/" "ko/" "zh-hans/" "zh-hant/")
for tentativo in 1 2 3 4 5 6 7 8 9 10; do
  rotte=0
  vecchie=0
  ultima=""
  for L in "${LINGUE[@]}"; do
    for P in index privacy support; do
      atteso=$(shasum -a 256 "$L$P.html" | cut -d' ' -f1)
      servito=$(curl -s -m 20 -H "Cache-Control: no-cache" "$SITO/$L$P.html?v=$(date +%s)$RANDOM" \
                | shasum -a 256 | cut -d' ' -f1)
      c=$(curl -s -o /dev/null -w "%{http_code}" -m 20 "$SITO/$L$P.html" || echo 000)
      if [ "$c" != "200" ]; then
        rotte=$((rotte + 1)); ultima="$L$P.html (HTTP $c)"
      elif [ "$atteso" != "$servito" ]; then
        vecchie=$((vecchie + 1)); ultima="$L$P.html (versione vecchia)"
      fi
    done
  done
  [ "$rotte" -eq 0 ] && [ "$vecchie" -eq 0 ] && {
    echo "✓ 39 pagine su 39 rispondono 200 e sono identiche ai file locali"; break; }
  echo "  $rotte non servite · $vecchie non aggiornate (ultima: $ultima) — riprovo fra 30 s [$tentativo/10]"
  sleep 30
done
rotte=$((rotte + vecchie))

if [ "${rotte:-1}" -ne 0 ]; then
  echo "⛔ dopo cinque minuti mancano ancora $rotte pagine."
  echo "   Controlla Settings → Pages (ramo $RAMO, cartella /) e la scheda Actions del repo."
  exit 1
fi

echo
echo "Ora gli indirizzi si possono caricare sulla scheda App Store:"
echo "   cd ../AppStore && fastlane urls"
