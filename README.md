# Sito di LookAt — statico, 13 lingue

Sito di marketing, supporto e privacy per **LookAt**. Nessun build step, nessuna
dipendenza, nessuna richiesta di rete dalle pagine: si carica così com'è su
GitHub Pages (o su qualunque hosting statico) e funziona.

I due URL che oggi **bloccano l'invio in App Store Connect** (`AppStore/scheda-non-testuale.md`)
li fornisce questo sito:

| Campo di App Store Connect | Da incollare |
|---|---|
| URL di assistenza | `…/support.html` |
| URL informativa privacy | `…/privacy.html` |
| URL marketing (facoltativo) | `…/` |

---

Il sito è online su **<https://angelosassoit.github.io/LookAt/>**.
Gli indirizzi da incollare in App Store Connect, lingua per lingua, stanno in
[`../AppStore/URL-SCHEDA.md`](../AppStore/URL-SCHEDA.md).

---

## 0. Aggiornare il sito online (il modo giusto)

```bash
cd "iOS DEV/LookAt/website"
./pubblica.sh
```

Rigenera il sito, lo manda su GitHub e poi **chiama davvero le 39 pagine** per
verificare che rispondano 200. La prima volta serve l'accesso, una sola volta:

```bash
gh auth login      # HTTPS → autenticazione via browser
```

> ⚠️ **Non usare più «Add file → Upload files» del sito di GitHub.** Il 14 ago 2026
> quel caricamento si è fermato a metà **senza dare alcun errore**: erano arrivate
> 20 pagine su 39 e mancava `.nojekyll` (il trascinamento scarta i file che
> iniziano con un punto). Il sito sembrava online e sei lingue rispondevano 404.

Il §1 qui sotto resta come procedura di emergenza, se git non è disponibile.

## 1. Caricare su GitHub Pages (a mano, senza git)

1. Su GitHub: **New repository** → nome `lookat-site` → pubblico → **Create**.
2. Nel repo vuoto: **uploading an existing file** → trascina **tutto il contenuto
   di questa cartella** (non la cartella: il *contenuto*), cioè `index.html`,
   `404.html`, `.nojekyll`, `robots.txt`, `assets/`, e le dodici cartelle di
   lingua `it/`, `de/`, `ja/`… → **Commit changes**.
   > `_sorgenti/` puoi caricarla o no: serve solo a rigenerare il sito, non a
   > farlo funzionare. Caricarla conviene, così la fonte sta col risultato.
   > `robots.txt` la esclude comunque dai motori di ricerca.
3. **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   Branch `main` / `/ (root)` → **Save**.
4. Dopo un paio di minuti il sito è online su
   `https://<tuo-utente>.github.io/lookat-site/`.
5. **Rigenera con l'indirizzo vero** (vedi §3): senza, mancano `canonical`,
   `hreflang` e `sitemap.xml`. Poi ricarica i file cambiati.

> Il trascinamento del browser **non carica le cartelle vuote** e a volte perde
> i file che iniziano con un punto: se `.nojekyll` non compare nel repo, crealo
> con **Add file → Create new file**, nome `.nojekyll`, contenuto vuoto. Senza,
> GitHub Pages passa i file per Jekyll e le cartelle che iniziano con `_` non
> vengono pubblicate.

## 2. Cosa c'è dentro

```
website/
├── index.html            inglese (GB) — è la radice del sito
├── support.html          supporto + FAQ
├── privacy.html          informativa privacy
├── en-us/ it/ es-es/ es-mx/ fr/ de/ pt-br/ nl/ ja/ ko/ zh-hans/ zh-hant/
│                         le altre dodici lingue, stesse tre pagine
├── 404.html              stile incorporato: funziona a qualsiasi profondità
├── robots.txt            (con la riga Sitemap solo se il sito è stato generato
│                          con --base-url)
├── .nojekyll             dice a GitHub Pages di servire i file così come sono
├── assets/
│   ├── css/style.css     un solo foglio di stile
│   ├── js/site.js        lingua + insegna dimostrativa (il sito regge anche senza)
│   └── img/              icona, anteprima social, 5 schermate × 13 lingue (WebP)
└── _sorgenti/            il generatore — non serve al sito pubblicato
    ├── genera-sito.py
    ├── contenuti_a.py    testi del sito: en, it, es, fr, de
    ├── contenuti_b.py    testi del sito: pt, nl, ja, ko, zh
    └── statici/          style.css e site.js originali (copiati in assets/)
```

Peso totale del sito pubblicabile: **~1,9 MB**, di cui 1,5 MB di schermate.
Una singola pagina ne carica circa 250 KB, e solo le schermate della sua lingua.

## 3. Rigenerare

```bash
cd "iOS DEV/LookAt/website"
python3 _sorgenti/genera-sito.py
```

Due parametri cambiano il risultato, ed entrambi vanno passati appena si sanno:

```bash
# quando conosci l'indirizzo pubblico → canonical, hreflang e sitemap.xml
python3 _sorgenti/genera-sito.py --base-url https://TUOUTENTE.github.io/lookat-site

# quando l'app è pubblicata → il bottone diventa un link vero
python3 _sorgenti/genera-sito.py \
  --base-url https://TUOUTENTE.github.io/lookat-site \
  --app-store https://apps.apple.com/app/id6800004772

# --forza rifà anche le immagini (altrimenti riusa quelle già presenti)

# scrive anche gli indirizzi per la scheda App Store:
#   AppStore/metadata/<loc>/{privacy,support,marketing}_url.txt   → li carica fastlane
#   AppStore/URL-SCHEDA.md                                        → la tabella da consultare
python3 _sorgenti/genera-sito.py --base-url https://angelosassoit.github.io/LookAt --scrivi-url-asc
```

**Finché non passi `--app-store` il bottone dice «Presto su App Store» e non è un
link.** È voluto: un `href="#"` o un URL App Store che risponde 404 mentre l'app
non è ancora pubblicata è, in review, un motivo di rifiuto.

**Finché non passi `--base-url` non vengono scritti `canonical`, `hreflang` né
`sitemap.xml`.** Anche questo è voluto: un canonical sbagliato fa più danno di un
canonical assente.

### Da dove viene il testo

Il generatore **non contiene** il testo di vendita. Lo legge da dove è già
tradotto e verificato:

| Cosa | Da dove |
|---|---|
| Nome, sottotitolo, testo promozionale, descrizione | `AppStore/fastlane/metadata/<loc>/*.txt` |
| Titoli e didascalie delle schermate | il dizionario `D` di `AppStore/frames.py` |
| Nomi delle dodici coppie di colori | `Resources/Localizable.xcstrings` (le stesse parole dell'app) |
| Schermate | `AppStore/device_screens/<loc>/*.png`, ridotte a 540 px e convertite in WebP |
| Icona | i livelli di `Resources/AppIcon.icon`, composti sul gradiente dichiarato in `icon.json` |

Conseguenza pratica: **se cambi la scheda App Store, rilancia questo script** e
il sito è di nuovo allineato. Non correggere il testo dentro l'HTML: si perde al
primo rilancio.

Quello che invece vive **solo** qui — struttura delle pagine, informativa privacy,
risposte di supporto — sta in `_sorgenti/contenuti_a.py` e `contenuti_b.py`.

### Verifiche che lo script fa da solo

Si ferma con errore se: la descrizione App Store cambia struttura; manca una
lingua nei contenuti; un link interno punta a un file inesistente; una pagina
contiene un indirizzo e-mail personale; la FAQ cita un nome di carattere diverso
da quello che l'app mostra in quella lingua.

## 4. Scelte già prese (e perché)

- **Contatto: `support@simplebuild.it`**, come su tutti gli altri siti
  (OpenBook, EasySplit, Colorimetro, iNoise, VerseOn). Nessun indirizzo personale
  compare da nessuna parte, ed è una verifica automatica del generatore.
- **Una cartella per lingua**, non tutte le lingue dentro la stessa pagina.
  Con 13 lingue il metodo «tutto in linea» di EasySplit e OpenBook porterebbe
  ogni pagina a pesare tredici volte tanto per mostrarne un tredicesimo.
- **La radice è l'inglese britannico**, la lingua di sviluppo del bundle
  (`project.yml`, `developmentLanguage: en-GB`). Chi arriva alla radice viene
  portato alla propria lingua una volta sola e solo se non ha già scelto; il
  selettore in alto a destra funziona anche senza JavaScript.
- **L'insegna della home è dal vivo**, non è un'immagine: si scrive il proprio
  messaggio e si scelgono le dodici coppie di colori vere dell'app, con lo stesso
  rapporto di contrasto WCAG che l'app calcola sul telefono. Con «riduci
  movimento» attivo lo scorrimento si ferma e il testo resta intero — esattamente
  come si comporta l'app.
- **Niente cookie, niente tracciamento, niente font o script esterni**: il sito
  è coerente con l'informativa che ospita, e non ha bisogno di banner.

## 5. Provato

- Generazione delle 39 pagine + 65 schermate: **eseguita**.
- Nessun traboccamento orizzontale a 360, 390, 440, 744 e 1440 pt: **misurato**.
- Testata su una sola riga in tutte le lingue, giapponese e cinese compresi:
  **misurato** (56 pt).
- `axe-core` (WCAG 2.0/2.1/2.2 A e AA) su sei pagine: **0 violazioni**, con
  controllo positivo per assicurarsi che lo strumento stesse davvero verificando.
- Insegna dimostrativa, contrasto, menu delle lingue, tasto Esc, rinvio
  automatico per `it-IT`, `de-CH`, `zh-TW`, `pt-PT`, `sv-SE`: **provati in
  browser**, nessun errore in console.
- **Non provato**: il sito su GitHub Pages vero (dipende dal caricamento) e la
  resa su Safari iOS reale — le prove sono state fatte con Chromium.
