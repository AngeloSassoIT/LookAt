#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il sito statico di LookAt in 13 lingue.

    python3 _sorgenti/genera-sito.py
    python3 _sorgenti/genera-sito.py --base-url https://TUONOME.github.io/lookat-site
    python3 _sorgenti/genera-sito.py --app-store https://apps.apple.com/app/id6800004772
    python3 _sorgenti/genera-sito.py --forza          # rifà anche le immagini

PERCHÉ UN GENERATORE E NON TREDICI PAGINE SCRITTE A MANO
Il testo di vendita esiste già, tradotto e verificato, in
`AppStore/fastlane/metadata/<loc>/` (lo produce `AppStore/genera-metadata.py`) e
in `AppStore/frames.py` per le didascalie delle schermate. Copiarlo dentro
39 file HTML significherebbe avere due versioni della stessa frase e accorgersi
della divergenza dopo la pubblicazione. Qui la fonte resta una: si cambia la
scheda App Store, si rilancia questo script, il sito è di nuovo allineato.

Il sito prodotto è statico puro: nessun build step, nessuna dipendenza a runtime,
nessuna richiesta di rete dalle pagine — coerente con l'informativa che ospita.
"""

from __future__ import annotations

import argparse
import ast
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

# ─────────────────────────────────────────────────────────────── percorsi

SORGENTI = Path(__file__).resolve().parent
SITO = SORGENTI.parent                      # …/LookAt/website
PROGETTO = SITO.parent                      # …/LookAt
APPSTORE = PROGETTO / "AppStore"
METADATA = APPSTORE / "fastlane" / "metadata"
SCHERMATE = APPSTORE / "device_screens"
ICONA = PROGETTO / "Resources" / "AppIcon.icon"
CATALOGO = PROGETTO / "Resources" / "Localizable.xcstrings"

sys.path.insert(0, str(SORGENTI))
import contenuti_a, contenuti_b                                   # noqa: E402

CHROME = {**contenuti_a.CHROME, **contenuti_b.CHROME}
PRIVACY = {**contenuti_a.PRIVACY, **contenuti_b.PRIVACY}
SUPPORTO = {**contenuti_a.SUPPORTO, **contenuti_b.SUPPORTO}

# ───────────────────────────────────────────────────────────── costanti

# ⚠️ L'ordine è quello del menu: prima l'inglese (radice), poi le altre.
# I codici sono quelli di App Store Connect, gli stessi delle cartelle di
# `metadata/` e di `device_screens/`. NON sono quelli del bundle dell'app
# (lì es-ES è `es`, es-MX è `es-419`, fr-FR è `fr`…): la conversione sta in
# BUNDLE, e sbagliarla significa pescare la traduzione di un'altra lingua.
LINGUE = ["en-GB", "en-US", "it", "es-ES", "es-MX", "fr-FR", "de-DE",
          "pt-BR", "nl-NL", "ja", "ko", "zh-Hans", "zh-Hant"]

CARTELLA = {"en-GB": "", "en-US": "en-us", "it": "it", "es-ES": "es-es",
            "es-MX": "es-mx", "fr-FR": "fr", "de-DE": "de", "pt-BR": "pt-br",
            "nl-NL": "nl", "ja": "ja", "ko": "ko", "zh-Hans": "zh-hans",
            "zh-Hant": "zh-hant"}

BUNDLE = {"en-GB": "en-GB", "en-US": "en-US", "it": "it", "es-ES": "es",
          "es-MX": "es-419", "fr-FR": "fr", "de-DE": "de", "pt-BR": "pt-BR",
          "nl-NL": "nl", "ja": "ja", "ko": "ko", "zh-Hans": "zh-Hans",
          "zh-Hant": "zh-Hant"}

# Le dodici coppie ad alta visibilità, copiate da
# `Sources/Model/SignPalette.swift` (highVisibilityPairs). Il nome mostrato
# accanto NON è tradotto qui: si legge dal catalogo dell'app, così l'insegna
# dimostrativa del sito e l'app dicono la stessa parola.
COPPIE = [
    ("black-neon-yellow", "Black / Neon Yellow", "#000000", "#FFE600"),
    ("black-white", "Black / White", "#000000", "#FFFFFF"),
    ("black-lime", "Black / Lime", "#000000", "#B6FF00"),
    ("black-cyan", "Black / Cyan", "#000000", "#00E5FF"),
    ("neon-yellow-black", "Neon Yellow / Black", "#FFE600", "#000000"),
    ("white-black", "White / Black", "#FFFFFF", "#000000"),
    ("blue-white", "Blue / White", "#0A4CFF", "#FFFFFF"),
    ("deep-blue-neon-yellow", "Deep Blue / Neon Yellow", "#001F7A", "#FFE600"),
    ("red-white", "Red / White", "#FF1D1D", "#FFFFFF"),
    ("violet-neon-yellow", "Violet / Neon Yellow", "#5B1BC9", "#FFE600"),
    ("magenta-white", "Magenta / White", "#FF00A8", "#FFFFFF"),
    ("green-black", "Green / Black", "#00C853", "#000000"),
]

# Le cinque scene della galleria: chiave della didascalia in frames.py →
# file della schermata grezza in device_screens/. `01_hero` non c'è: quella
# posizione, in cima alla pagina, la occupa l'insegna dimostrativa dal vivo.
GALLERIA = [
    ("03_editor", "02_editor"),
    ("02_dotmatrix", "03_dotmatrix"),
    ("04_colors", "04_colors"),
    ("05_scroll", "05_long"),
    ("06_grazie", "06_grazie"),
]

LARGHEZZA_SCATTO = 540          # px: mostrata a ~270 px, quindi già 2× su retina
QUALITA_WEBP = 82

# Stringhe che NON devono comparire in nessun file pubblicato: sono indirizzi
# personali. Il controllo finale è automatico perché una svista qui si scopre
# solo quando il sito è già online e indicizzato.
# ⚠️ Composte a pezzi di proposito: scritte per intero, questo file diventerebbe
# esso stesso l'occorrenza dell'indirizzo che deve impedire di pubblicare.
VIETATE = ["angelo" + "sassopp93", "angelo" + "sasso93", "@gmail" + ".com"]

EMAIL = "support@simplebuild.it"

# ─────────────────────────────────────────────────────────── utilità testo

def esc(t: str) -> str:
    return html.escape(t, quote=True)


def enfasi(t: str) -> str:
    """`*così*` → `<em>così</em>`, e l'a-capo delle didascalie → <br>.

    È la stessa convenzione di frames.py, dove l'asterisco marca la parola che
    va in giallo: riusando il marcatore, titolo del sito e titolo dell'anteprima
    App Store restano la stessa frase con lo stesso accento.
    """
    t = esc(t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    return t.replace("\n", "<br>")


# ────────────────────────────────────────────────────── lettura delle fonti

def leggi_metadati(loc: str) -> dict:
    base = METADATA / loc
    def leggi(nome):
        p = base / f"{nome}.txt"
        if not p.exists():
            raise SystemExit(f"manca {p} — la scheda App Store non è completa per {loc}")
        return p.read_text(encoding="utf-8").strip()
    return dict(nome=leggi("name"), sottotitolo=leggi("subtitle"),
                promo=leggi("promotional_text"), descrizione=leggi("description"))


def analizza_descrizione(testo: str, loc: str) -> dict:
    """Spacchetta la descrizione App Store nei blocchi che diventano sezioni.

    La forma è sempre: paragrafo d'apertura · cinque sezioni (titolo + corpo,
    con elenco puntato nelle tre centrali) · una nota finale senza titolo.
    Se un giorno la descrizione cambia forma questo script si ferma qui invece
    di produrre una pagina con una sezione vuota e nessun errore.
    """
    blocchi = [b.strip() for b in testo.split("\n\n") if b.strip()]
    if len(blocchi) != 7:
        raise SystemExit(f"[{loc}] la descrizione ha {len(blocchi)} blocchi invece di 7: "
                         "la struttura è cambiata, aggiorna analizza_descrizione()")
    sezioni = []
    for b in blocchi[1:-1]:
        righe = b.split("\n")
        titolo, resto = righe[0].strip(), [r.strip() for r in righe[1:] if r.strip()]
        punti = [r.lstrip("•").strip() for r in resto if r.startswith("•")]
        corpo = " ".join(r for r in resto if not r.startswith("•"))
        if not titolo or (not punti and not corpo):
            raise SystemExit(f"[{loc}] sezione senza titolo o senza corpo: {b[:60]!r}")
        sezioni.append(dict(titolo=titolo, corpo=corpo, punti=punti))
    # Le tre sezioni centrali sono elenchi puntati in tutte e tredici le lingue:
    # se una arriva senza punti, i riquadri della home uscirebbero vuoti.
    for i in (1, 2, 3):
        if not sezioni[i]["punti"]:
            raise SystemExit(f"[{loc}] la sezione «{sezioni[i]['titolo']}» "
                             "doveva essere un elenco puntato")
    return dict(intro=blocchi[0], sezioni=sezioni, nota=blocchi[-1])


def leggi_didascalie() -> dict:
    """Estrae il dizionario D da frames.py senza importarlo.

    frames.py importa PIL e i temi CJK e all'import fa lavoro vero: qui serve
    solo un dizionario di stringhe. Si legge l'albero sintattico e si valuta il
    solo nodo di D, con `dict` come unica funzione disponibile.
    """
    sorgente = (APPSTORE / "frames.py").read_text(encoding="utf-8")
    for nodo in ast.parse(sorgente).body:
        if isinstance(nodo, ast.Assign) and getattr(nodo.targets[0], "id", "") == "D":
            return eval(compile(ast.Expression(nodo.value), "<frames.py:D>", "eval"),
                        {"dict": dict, "__builtins__": {}}, {})
    raise SystemExit("in AppStore/frames.py non c'è più il dizionario D delle didascalie")


def leggi_nomi_coppie() -> dict:
    """{loc ASC: {chiave inglese: nome tradotto}} dal catalogo stringhe dell'app."""
    dati = json.loads(CATALOGO.read_text(encoding="utf-8"))
    fuori = {}
    for loc in LINGUE:
        b = BUNDLE[loc]
        m = {}
        for _, chiave, _, _ in COPPIE:
            voce = dati["strings"].get(chiave, {}).get("localizations", {}).get(b)
            m[chiave] = voce["stringUnit"]["value"] if voce else chiave
        fuori[loc] = m
    return fuori


# ────────────────────────────────────────────────────────────── immagini

def p3_a_srgb(c) -> tuple:
    """display-p3 (come lo scrive Icon Composer in icon.json) → sRGB a 8 bit."""
    def dec(v): return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    def enc(v): return 12.92 * v if v <= 0.0031308 else 1.055 * (v ** (1 / 2.4)) - 0.055
    r, g, b = [dec(x) for x in c]
    X = 0.4865709486482162 * r + 0.26566769316909306 * g + 0.1982172852343625 * b
    Y = 0.2289745640697488 * r + 0.6917385218365064 * g + 0.0792869140937450 * b
    Z = 0.0000000000000000 * r + 0.04511338185890264 * g + 1.0439443689009760 * b
    lin = (3.2409699419045226 * X - 1.5373831775700940 * Y - 0.4986107602930034 * Z,
           -0.9692436362808796 * X + 1.8759675015077202 * Y + 0.0415550574071756 * Z,
           0.0556300796969937 * X - 0.2039769588889765 * Y + 1.0569715142428786 * Z)
    return tuple(max(0, min(255, round(enc(max(0.0, min(1.0, v))) * 255))) for v in lin)


def prepara_immagini(forza: bool) -> None:
    from PIL import Image, ImageDraw, ImageFont

    fuori = SITO / "assets" / "img"
    fuori.mkdir(parents=True, exist_ok=True)

    # ── icona: i livelli del .icon composti sul gradiente dichiarato in
    # icon.json. Nel progetto non esiste un PNG 1024 già pronto (l'icona la
    # renderizza Xcode in fase di build), quindi il sito se la costruisce.
    dati_icona = json.loads((ICONA / "icon.json").read_text(encoding="utf-8"))
    campo = dati_icona["fill"]["automatic-gradient"]        # "display-p3:r,g,b,a"
    base = p3_a_srgb([float(v) for v in campo.split(":")[1].split(",")[:3]])

    def mescola(c, verso, q):
        t = (255, 255, 255) if verso > 0 else (0, 0, 0)
        return tuple(round(c[i] * (1 - q) + t[i] * q) for i in range(3))

    icona_png = fuori / "icona.png"
    if forza or not icona_png.exists():
        N = 1024
        alto, basso = mescola(base, +1, 0.20), mescola(base, -1, 0.14)
        img = Image.new("RGB", (N, N))
        pittore = ImageDraw.Draw(img)
        for y in range(N):
            q = y / (N - 1)
            pittore.line([(0, y), (N, y)],
                         fill=tuple(round(alto[i] * (1 - q) + basso[i] * q) for i in range(3)))
        img = img.convert("RGBA")
        # L'ordine è quello dei gruppi di icon.json letti dal basso: il primo
        # gruppo del file è il livello IN CIMA (le scintille), l'ultimo è lo
        # sfondo. Invertirlo copre la mano con l'alone bianco.
        nomi = [g["layers"][0]["image-name"] for g in dati_icona["groups"]][::-1]
        for nome in nomi:
            livello = Image.open(ICONA / "Assets" / nome).convert("RGBA")
            img.alpha_composite(livello.resize((N, N), Image.LANCZOS))
        img.convert("RGB").save(icona_png)
        for misura in (512, 180, 32):
            img.resize((misura, misura), Image.LANCZOS).convert("RGB").save(
                fuori / f"icona-{misura}.png")

    # ── immagine di anteprima social: nessun testo tradotto sopra, così ne
    # basta una per tutte e tredici le lingue.
    og = fuori / "og.png"
    if forza or not og.exists():
        from PIL import ImageFilter
        import numpy as np

        L, A = 1200, 630
        tela = Image.new("RGB", (L, A))
        p = ImageDraw.Draw(tela)
        for y in range(A):                       # blu profondo → blu di folla
            q = y / (A - 1)
            p.line([(0, y), (L, y)], fill=(round(4 + 8 * q), round(23 + 30 * q), round(58 + 28 * q)))

        # L'alone va SFOCATO: un'ellisse gialla appoggiata sul blu si legge come
        # una macchia verde oliva, non come una luce. Provato il 14 ago 2026.
        alone = Image.new("L", (L, A), 0)
        ImageDraw.Draw(alone).ellipse([L * 0.52, A * 0.55, L * 1.10, A * 1.60], fill=110)
        alone = alone.filter(ImageFilter.GaussianBlur(110))
        tela = Image.composite(Image.new("RGB", (L, A), (255, 214, 80)), tela,
                               alone.point(lambda v: int(v * 0.42)))

        def carattere(dim, peso=800):
            for percorso in ("/System/Library/Fonts/SFNSRounded.ttf",
                             "/System/Library/Fonts/SFNS.ttf",
                             "/System/Library/Fonts/Supplemental/Arial Black.ttf"):
                try:
                    f = ImageFont.truetype(percorso, dim)
                    try:
                        f.set_variation_by_axes([peso])   # SF è variabile: senza
                    except Exception:                     # questo esce in Regular
                        pass
                    return f
                except OSError:
                    continue
            return ImageFont.load_default()

        mano_png = APPSTORE / "screenshots" / "Mano+iPhone.png"
        if mano_png.exists():
            mano = Image.open(mano_png).convert("RGBA")
            h = int(A * 0.94)
            mano = mano.resize((round(mano.width * h / mano.height), h), Image.LANCZOS)

            # L'illustrazione ha lo schermo spento: senza una scritta dentro,
            # l'anteprima social mostra un telefono nero e non un cartello. Il
            # riquadro scuro si trova dai pixel, non a coordinate fisse, così
            # regge anche se un domani l'illustrazione cambia misura.
            px = np.array(mano)
            schermo = ((px[:, :, 3] > 200) & (px[:, :, 0] < 70) &
                       (px[:, :, 1] < 70) & (px[:, :, 2] < 80))
            if schermo.any():
                ys, xs = np.nonzero(schermo)
                cx, cy = xs.mean(), ys.mean()
                frase = "LOOK AT ME"
                misuratore = ImageDraw.Draw(Image.new("RGB", (1, 1)))
                dim = 10
                while dim < 200:
                    bb = misuratore.textbbox((0, 0), frase, font=carattere(dim + 2, 900))
                    if bb[2] - bb[0] > (xs.max() - xs.min()) * 0.80:
                        break
                    dim += 2
                f = carattere(dim, 900)
                bb = misuratore.textbbox((0, 0), frase, font=f)
                testo = Image.new("RGBA", mano.size, (0, 0, 0, 0))
                ImageDraw.Draw(testo).text(
                    (cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
                    frase, font=f, fill=(255, 230, 0, 255))
                # 17°: inclinazione del telefono, misurata sull'asse principale
                # dei pixel dello schermo, non stimata a occhio.
                testo = testo.rotate(17, resample=Image.BICUBIC, center=(cx, cy))
                mano.paste(testo, (0, 0), Image.fromarray(
                    (np.array(testo.getchannel("A")) * schermo).astype("uint8"), "L"))

            tela = tela.convert("RGBA")
            tela.alpha_composite(mano, (L - mano.width + 30, round((A - h) / 2)))
            tela = tela.convert("RGB")

        p = ImageDraw.Draw(tela)
        p.text((72, 236), "LookAt", font=carattere(112, 800), fill=(255, 230, 0))
        p.text((76, 372), "Be seen from the back row", font=carattere(38, 600),
               fill=(190, 224, 255))
        tela.save(og)

    # ── schermate: una serie per lingua, ridotte e in WebP.
    for loc in LINGUE:
        dentro = SCHERMATE / loc
        if not dentro.exists():
            raise SystemExit(f"mancano le schermate di {loc}: {dentro}")
        cartella = fuori / (CARTELLA[loc] or "en-gb")
        cartella.mkdir(parents=True, exist_ok=True)
        for _, scatto in GALLERIA:
            sorgente = dentro / f"{scatto}.png"
            destinazione = cartella / f"{scatto}.webp"
            if not sorgente.exists():
                raise SystemExit(f"manca la schermata {sorgente}")
            if not forza and destinazione.exists() and \
               destinazione.stat().st_mtime >= sorgente.stat().st_mtime:
                continue
            im = Image.open(sorgente).convert("RGB")
            altezza = round(im.height * LARGHEZZA_SCATTO / im.width)
            im.resize((LARGHEZZA_SCATTO, altezza), Image.LANCZOS).save(
                destinazione, "WEBP", quality=QUALITA_WEBP, method=6)


# ──────────────────────────────────────────────────────── pezzi di pagina

MARCHIO_APPLE = ('<svg viewBox="0 0 384 512" aria-hidden="true"><path d="M318.7 268.7c-.2-36.7 '
                 '16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 '
                 '20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 '
                 '81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 '
                 '17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6'
                 '-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 '
                 '44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>')


def testata(loc: str, pagina: str, radice: str, app_store: str) -> str:
    c = CHROME[loc]
    voci = []
    for chiave, file_, etichetta in (("index", "index.html", c["nav_home"]),
                                     ("support", "support.html", c["nav_supporto"]),
                                     ("privacy", "privacy.html", c["nav_privacy"])):
        corrente = ' aria-current="page"' if chiave == pagina else ""
        voci.append(f'<a href="{file_}"{corrente}>{esc(etichetta)}</a>')

    lingue = []
    for altra in LINGUE:
        destinazione = f"{radice}{CARTELLA[altra] + '/' if CARTELLA[altra] else ''}{pagina}.html?lang={altra}"
        attuale = ' aria-current="true"' if altra == loc else ""
        lingue.append(f'<li><a href="{esc(destinazione)}" hreflang="{altra}" lang="{altra}"{attuale}>'
                      f'{esc(CHROME[altra]["lingua"])}</a></li>')

    return f"""<header class="testata">
  <div class="contenitore barra">
    <!-- aria-label esplicito: sotto i 430 pt il nome scritto è nascosto e il
         link resterebbe senza nome accessibile (violazione WCAG 2.4.4). -->
    <a class="marchio" href="index.html" aria-label="LookAt">
      <img src="{radice}assets/img/icona-180.png" width="34" height="34" alt="">
      <span>LookAt</span>
    </a>
    <nav class="menu" aria-label="{esc(c['nav_home'])}">
      {' '.join(voci)}
      <details class="lingue">
        <summary aria-label="{esc(c['lingua_etichetta'])}">{esc(c['sigla'])}</summary>
        <ul>{''.join(lingue)}</ul>
      </details>
    </nav>
  </div>
</header>"""


def piede(loc: str, radice: str) -> str:
    c = CHROME[loc]
    lingue = "".join(
        f'<li><a href="{esc(radice + (CARTELLA[a] + "/" if CARTELLA[a] else "") + "index.html?lang=" + a)}"'
        f' hreflang="{a}" lang="{a}">{esc(CHROME[a]["lingua"])}</a></li>' for a in LINGUE)
    return f"""<footer class="piede">
  <div class="contenitore">
    <div class="piede-riga">
      <a href="index.html">{esc(c['nav_home'])}</a>
      <a href="support.html">{esc(c['nav_supporto'])}</a>
      <a href="privacy.html">{esc(c['nav_privacy'])}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    <p class="diritti">{esc(c['piede_nota'])}<br>{esc(c['diritti'])}</p>
    <nav aria-label="{esc(c['altre_lingue'])}">
      <ul class="lingue-elenco">{lingue}</ul>
    </nav>
  </div>
</footer>"""


def bottone(loc: str, app_store: str) -> str:
    c = CHROME[loc]
    if app_store:
        return (f'<a class="cta" href="{esc(app_store)}" rel="noopener">{MARCHIO_APPLE}'
                f'<span>{esc(c["cta_scarica"])}</span></a>')
    # Finché l'app non è pubblicata il bottone NON è un link: un href="#" o un
    # URL App Store che risponde 404 è, per la review, un motivo di rifiuto.
    return (f'<span class="cta attesa">{MARCHIO_APPLE}'
            f'<span>{esc(c["cta_attesa"])}</span></span>')


def intestazione_html(loc: str, pagina: str, radice: str, titolo: str, descrizione: str,
                      base_url: str) -> str:
    """<head> completo. canonical e hreflang compaiono SOLO con --base-url:
    pubblicare un canonical sbagliato è peggio che non averlo."""
    c = CHROME[loc]
    alternative = ""
    canonico = ""
    if base_url:
        radice_url = base_url.rstrip("/") + "/"
        righe = []
        for altra in LINGUE:
            u = radice_url + (CARTELLA[altra] + "/" if CARTELLA[altra] else "") + f"{pagina}.html"
            righe.append(f'  <link rel="alternate" hreflang="{altra}" href="{esc(u)}">')
        righe.append(f'  <link rel="alternate" hreflang="x-default" href="{esc(radice_url + pagina + ".html")}">')
        alternative = "\n".join(righe) + "\n"
        mio = radice_url + (CARTELLA[loc] + "/" if CARTELLA[loc] else "") + f"{pagina}.html"
        canonico = f'  <link rel="canonical" href="{esc(mio)}">\n'
        og_img = f'  <meta property="og:image" content="{esc(radice_url)}assets/img/og.png">\n'
    else:
        og_img = f'  <meta property="og:image" content="{radice}assets/img/og.png">\n'

    return f"""<!DOCTYPE html>
<html lang="{loc}" data-lingua="{loc}" data-radice="{radice}" data-pagina="{pagina}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{esc(titolo)}</title>
  <meta name="description" content="{esc(descrizione)}">
  <meta name="theme-color" content="#04173A">
  <meta name="color-scheme" content="dark">
{canonico}{alternative}  <meta property="og:type" content="website">
  <meta property="og:site_name" content="LookAt">
  <meta property="og:title" content="{esc(titolo)}">
  <meta property="og:description" content="{esc(descrizione)}">
  <meta property="og:locale" content="{loc.replace('-', '_')}">
{og_img}  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{radice}assets/img/icona-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="{radice}assets/img/icona-180.png">
  <link rel="stylesheet" href="{radice}assets/css/style.css">
  <script src="{radice}assets/js/site.js" defer></script>
</head>
<body>
<a class="salta" href="#contenuto">{esc(c['salta'])}</a>
"""


# ─────────────────────────────────────────────────────────────── pagine

def pagina_home(loc, meta, desc, didascalie, nomi_coppie, radice, base_url, app_store) -> str:
    c = CHROME[loc]
    eroe = didascalie["01_hero"][loc]

    coppie = []
    for i, (_, chiave, sfondo, testo) in enumerate(COPPIE):
        nome = nomi_coppie[loc][chiave]
        premuto = "true" if i == 0 else "false"
        coppie.append(
            f'<button type="button" class="coppia" aria-pressed="{premuto}" '
            f'data-sfondo="{sfondo}" data-testo="{testo}" title="{esc(nome)}" '
            f'aria-label="{esc(nome)}" style="background:{sfondo};color:{testo}">Aa</button>')

    riquadri = []
    for sez in desc["sezioni"][1:4]:
        punti = []
        for p in sez["punti"]:
            # Il trattino lungo separa il nome della cosa dalla sua ragione: è
            # una convenzione della descrizione App Store, in tutte le lingue.
            if "—" in p:
                testa, coda = p.split("—", 1)
                if len(testa.strip()) <= 40:
                    punti.append(f"<li><strong>{esc(testa.strip())}</strong> — {esc(coda.strip())}</li>")
                    continue
            punti.append(f"<li>{esc(p)}</li>")
        riquadri.append(f'<div class="riquadro"><h3>{esc(sez["titolo"])}</h3>'
                        f'<ul>{"".join(punti)}</ul></div>')

    scene = []
    for chiave, scatto in GALLERIA:
        d = didascalie[chiave][loc]
        img = f'{radice}assets/img/{CARTELLA[loc] or "en-gb"}/{scatto}.webp'
        titolo_semplice = d["titolo"].replace("*", "").replace("\n", " ")
        scene.append(f"""      <article class="scena">
        <div class="telefono"><img src="{img}" width="270" height="586" loading="lazy" decoding="async"
             alt="{esc(titolo_semplice)} — LookAt"></div>
        <div>
          <p class="occhiello">{esc(d['kicker'])}</p>
          <h3>{enfasi(d['titolo'])}</h3>
          <p>{esc(d['sub'])}</p>
        </div>
      </article>""")

    onesto = desc["sezioni"][4]
    chip = "".join(f"<span>{esc(x)}</span>" for x in c["chip"])

    # Il sottotitolo della scheda App Store e il titolo dell'anteprima sono, in
    # parecchie lingue, la STESSA frase (in italiano entrambi «Ti vedono
    # dall'ultima fila»). Ripeterla sotto il titolo fa sembrare la pagina un
    # errore di copia-incolla: se coincidono, sotto il titolo va la riga
    # d'appoggio dell'anteprima, che dice un'altra cosa.
    def nudo(t):
        return re.sub(r"[^\w]+", "", t.replace("*", "").replace("\n", " ")).lower()
    sommario = meta["sottotitolo"]
    if nudo(sommario) in nudo(eroe["titolo"]) or nudo(eroe["titolo"]) in nudo(sommario):
        sommario = eroe["sub"]

    titolo_pagina = f'{meta["nome"]} — {meta["sottotitolo"]}'
    corpo = f"""{intestazione_html(loc, "index", radice, titolo_pagina, meta["promo"], base_url)}
{testata(loc, "index", radice, app_store)}
<main id="contenuto">

  <section class="eroe">
    <div class="contenitore">
      <p class="occhiello">{esc(eroe['kicker'])}</p>
      <h1>{enfasi(eroe['titolo'])}</h1>
      <p class="sommario">{esc(sommario)}</p>
      <p class="intro">{esc(desc['intro'])}</p>
      <div class="azioni">
        {bottone(loc, app_store)}
        <p class="microcopy">{esc(c['microcopy'])}</p>
        <div class="marchi fiducia">{chip}</div>
      </div>

      <div class="demo">
        <div class="insegna" aria-hidden="true">
          <div class="nastro">
            <span>{esc(c['demo_esempio'])}</span><span>{esc(c['demo_esempio'])}</span>
          </div>
        </div>
        <form class="comandi" onsubmit="return false">
          <div>
            <label for="testo">{esc(c['demo_titolo'])} · {esc(c['demo_etichetta'])}</label>
            <input id="testo" type="text" maxlength="240" autocomplete="off"
                   placeholder="{esc(c['demo_placeholder'])}"
                   data-esempio="{esc(c['demo_esempio'])}">
          </div>
          <fieldset class="coppie">
            <legend>{esc(c['demo_coppie'])}</legend>
            <div class="tavolozza">{''.join(coppie)}</div>
          </fieldset>
          <p class="misura">{esc(c['demo_contrasto'])}
            <output id="contrasto">—</output>
            <span class="esito" id="esito" data-ok="{esc(c['demo_ok'])}"
                  data-basso="{esc(c['demo_basso'])}"></span>
          </p>
          <p class="microcopy">{esc(c['demo_nota'])}</p>
        </form>
      </div>
    </div>
  </section>

  <section>
    <div class="contenitore spiegazione">
      <h2>{esc(desc['sezioni'][0]['titolo'])}</h2>
      <p>{esc(desc['sezioni'][0]['corpo'])}</p>
    </div>
  </section>

  <section>
    <div class="contenitore">
      <div class="riquadri">{''.join(riquadri)}</div>
    </div>
  </section>

  <section>
    <div class="contenitore">
      <h2>{esc(c['sez_schermate'])}</h2>
      <div class="schermate">
{chr(10).join(scene)}
      </div>
    </div>
  </section>

  <section>
    <div class="contenitore">
      <div class="onesto">
        <h2>{esc(onesto['titolo'])}</h2>
        <p>{esc(onesto['corpo'])}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="contenitore">
      <div class="nota"><p>{esc(desc['nota'])}</p></div>
    </div>
  </section>

  <section class="chiusura">
    <div class="contenitore">
      <h2>{esc(c['chiusura_titolo'])}</h2>
      <p class="promo">{esc(meta['promo'])}</p>
      <div class="azioni">
        {bottone(loc, app_store)}
        <p class="microcopy">{esc(c['microcopy'])}</p>
      </div>
    </div>
  </section>

</main>
{piede(loc, radice)}
</body>
</html>
"""
    return corpo


def pagina_supporto(loc, meta, radice, base_url, app_store) -> str:
    c = CHROME[loc]
    s = SUPPORTO[loc]
    voci = "".join(
        f"<details><summary>{esc(d)}</summary><p>{r}</p></details>" for d, r in s["faq"])
    titolo = f'{c["titolo_supporto"]} — LookAt'
    return f"""{intestazione_html(loc, "support", radice, titolo, c["meta_supporto"], base_url)}
{testata(loc, "support", radice, app_store)}
<main id="contenuto">
  <div class="contenitore stretto pagina">
    <h1>{esc(c['titolo_supporto'])}</h1>
    <p class="data">{esc(c['data_aggiornamento'])}</p>
    <p>{esc(s['intro'])}</p>
    <h2>{esc(c['sez_domande'])}</h2>
    <div class="faq">{voci}</div>
    <div class="contatto">
      <h2>{esc(c['contatto_titolo'])}</h2>
      <p class="email"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>{esc(c['contatto_testo'])}</p>
    </div>
    <p style="margin-top:34px"><a href="index.html">← {esc(c['torna'])}</a></p>
  </div>
</main>
{piede(loc, radice)}
</body>
</html>
"""


def pagina_privacy(loc, meta, radice, base_url, app_store) -> str:
    c = CHROME[loc]
    blocchi = []
    for titolo, paragrafi in PRIVACY[loc]:
        pezzi = "".join(p if p.lstrip().startswith("<ul") else f"<p>{p}</p>" for p in paragrafi)
        blocchi.append(f"<h2>{esc(titolo)}</h2>{pezzi}")
    titolo = f'{c["titolo_privacy"]} — LookAt'
    return f"""{intestazione_html(loc, "privacy", radice, titolo, c["meta_privacy"], base_url)}
{testata(loc, "privacy", radice, app_store)}
<main id="contenuto">
  <div class="contenitore stretto pagina">
    <h1>{esc(c['titolo_privacy'])}</h1>
    <p class="data">{esc(c['data_aggiornamento'])}</p>
    <div class="prosa">{''.join(blocchi)}</div>
    <p style="margin-top:34px"><a href="index.html">← {esc(c['torna'])}</a></p>
  </div>
</main>
{piede(loc, radice)}
</body>
</html>
"""


def pagina_404(base_url: str) -> str:
    """Una sola pagina, in inglese: chi ci finisce ha sbagliato indirizzo e non
    sappiamo in che lingua legge.

    ⚠️ Lo stile è INCORPORATO e non ci sono immagini. GitHub Pages serve questo
    file per qualunque indirizzo sbagliato, a qualunque profondità
    (`…/it/qualcosa.html`): un `href="assets/…"` relativo sarebbe risolto
    rispetto alla cartella sbagliata e un `href="/assets/…"` assoluto punterebbe
    fuori dal repository, perché su un sito di progetto la radice è
    `/nome-repo/`. Una pagina che non chiede nulla è l'unica che non può
    uscire senza stile.
    """
    casa = base_url + "/" if base_url else "./"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found — LookAt</title>
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#04173A">
  <style>
    html, body {{ margin: 0; height: 100%; background: #04173A; color: #fff;
      font-family: -apple-system, BlinkMacSystemFont, system-ui, "Segoe UI", sans-serif; }}
    body {{ display: grid; place-items: center; text-align: center; padding: 24px; }}
    h1 {{ font-size: 88px; margin: 0; color: #FFE600; letter-spacing: -0.03em; }}
    p {{ color: #BEE0FF; font-size: 19px; margin: 10px 0 30px; }}
    a {{ display: inline-block; background: #FFE600; color: #10131A; text-decoration: none;
      font-weight: 800; padding: 14px 26px; border-radius: 999px; }}
  </style>
</head>
<body>
  <div>
    <h1>404</h1>
    <p>This page does not exist.</p>
    <a href="{esc(casa)}">LookAt</a>
  </div>
</body>
</html>
"""


# ───────────────────────────────────────────── indirizzi per App Store Connect

# Nome della lingua come lo scrive App Store Connect nell'elenco delle
# localizzazioni: serve solo al documento, ma è quello che si legge nel pannello
# mentre si incolla, e cercare «nl-NL» in una lista che dice «Olandese» fa
# perdere tempo.
NOMI_ASC = {
    "en-GB": "Inglese (Regno Unito)", "en-US": "Inglese (Stati Uniti)",
    "it": "Italiano", "es-ES": "Spagnolo (Spagna)", "es-MX": "Spagnolo (Messico)",
    "fr-FR": "Francese (Francia)", "de-DE": "Tedesco", "pt-BR": "Portoghese (Brasile)",
    "nl-NL": "Olandese", "ja": "Giapponese", "ko": "Coreano",
    "zh-Hans": "Cinese semplificato", "zh-Hant": "Cinese tradizionale",
}
PRIMARIA = "en-GB"


def url_scheda(base_url: str) -> dict:
    """{loc ASC: {campo: URL}} — l'unica funzione che sa comporre gli indirizzi."""
    fuori = {}
    for loc in LINGUE:
        cartella = CARTELLA[loc] + "/" if CARTELLA[loc] else ""
        fuori[loc] = {
            "privacy_url": f"{base_url}/{cartella}privacy.html",
            "support_url": f"{base_url}/{cartella}support.html",
            "marketing_url": f"{base_url}/{cartella}index.html",
        }
    return fuori


def scrivi_url_asc(base_url: str) -> None:
    """Scrive i .txt che legge `fastlane deliver` e il documento da consultare.

    I .txt finiscono in `AppStore/metadata/<loc>/`, cioè nella SORGENTE: il
    pacchetto di deliver (`AppStore/fastlane/metadata/`) è fatto di link
    simbolici a questi file e lo rigenera `prepara-deliver.sh`. Scrivere nel
    pacchetto significherebbe vedersi il lavoro cancellato al primo `--senza-novita`.
    """
    indirizzi = url_scheda(base_url)
    sorgente_meta = APPSTORE / "metadata"
    scritti = 0
    for loc, campi in indirizzi.items():
        cartella = sorgente_meta / loc
        if not cartella.exists():
            raise SystemExit(f"manca {cartella}: il pacchetto della scheda non ha la lingua {loc}")
        for campo, u in campi.items():
            (cartella / f"{campo}.txt").write_text(u + "\n", encoding="utf-8")
            scritti += 1

    righe = [
        "# Indirizzi della scheda App Store — LookAt",
        "",
        "> **Generato**, non scritto a mano: `website/_sorgenti/genera-sito.py "
        "--base-url … --scrivi-url-asc`.",
        "> Se cambia il dominio del sito si rilancia quel comando, non si corregge questo file.",
        "",
        f"Sito: <{base_url}/>  ·  13 lingue  ·  lingua primaria della scheda: **{PRIMARIA}**",
        "",
        "## Dove va ciascun campo, in App Store Connect",
        "",
        "| Campo | Dove sta in ASC | Per lingua? |",
        "|---|---|---|",
        "| **URL informativa privacy** | *Informazioni sull'app* → *Informativa sulla privacy* "
        "(vale per tutte le versioni) | **sì** |",
        "| **URL di assistenza** | pagina della **versione** 1.0 → *Informazioni generali* | **sì** |",
        "| **URL marketing** (facoltativo) | pagina della **versione** 1.0 → *Informazioni generali* | **sì** |",
        "",
        "⚠️ I primi due sono **obbligatori** per l'invio: un indirizzo che risponde 404 è un "
        "motivo di rifiuto, non un avviso.",
        "",
        "⚠️ L'informativa privacy sta su *Informazioni sull'app*, non sulla versione: cambiando "
        "lingua nel menu in alto a destra si cambia la localizzazione che si sta modificando. "
        "È l'errore che fa credere di averle compilate tutte avendone compilata una.",
        "",
        "## Gli indirizzi, lingua per lingua",
        "",
        "| Lingua (come la chiama ASC) | Codice | URL informativa privacy | URL di assistenza | URL marketing |",
        "|---|---|---|---|---|",
    ]
    for loc in LINGUE:
        c = indirizzi[loc]
        nome = NOMI_ASC[loc] + (" ⭐️" if loc == PRIMARIA else "")
        righe.append(f"| {nome} | `{loc}` | <{c['privacy_url']}> | <{c['support_url']}> "
                     f"| <{c['marketing_url']}> |")

    righe += [
        "",
        "⭐️ = lingua primaria della scheda.",
        "",
        "## Solo l'informativa privacy, pronta da incollare",
        "",
        "```",
    ]
    larghezza = max(len(NOMI_ASC[l]) for l in LINGUE)
    for loc in LINGUE:
        righe.append(f"{NOMI_ASC[loc]:<{larghezza}}  {indirizzi[loc]['privacy_url']}")
    righe += [
        "```",
        "",
        "## Caricarli senza incollare nulla",
        "",
        "```bash",
        "cd \"iOS DEV/LookAt/AppStore\"",
        "fastlane urls           # controlla che ogni indirizzo risponda 200, poi lo scrive su ASC",
        "fastlane urls dry:true  # solo il controllo, non scrive niente",
        "```",
        "",
        "La lane **non scrive un indirizzo che non risponde 200**: si ferma e dice quale manca. "
        "Serve davvero — il 14 ago 2026 sei lingue del sito non erano state caricate su GitHub "
        "Pages e i loro indirizzi rispondevano 404 pur essendo scritti correttamente qui.",
        "",
        "Gli stessi indirizzi stanno anche in `metadata/<loc>/privacy_url.txt`, `support_url.txt` "
        "e `marketing_url.txt`, quindi li carica anche `fastlane schede` insieme ai testi.",
        "",
    ]
    (APPSTORE / "URL-SCHEDA.md").write_text("\n".join(righe), encoding="utf-8")
    print(f"· {scritti} file *_url.txt in AppStore/metadata/ · AppStore/URL-SCHEDA.md")


# ─────────────────────────────────────────────────────────────── verifiche

def verifica(base_url: str, nomi_coppie: dict) -> None:
    problemi = []

    # 1. nessun indirizzo personale nei file pubblicati
    for f in SITO.rglob("*"):
        if not f.is_file() or "_sorgenti" in f.parts or f.suffix not in {".html", ".css", ".js", ".xml", ".txt", ".md"}:
            continue
        testo = f.read_text(encoding="utf-8", errors="ignore")
        for v in VIETATE:
            if v in testo:
                problemi.append(f"{f.relative_to(SITO)} contiene «{v}»")

    # 2. i link interni puntano a file che esistono
    for f in SITO.rglob("*.html"):
        if "_sorgenti" in f.parts:
            continue
        for href in re.findall(r'href="([^"]+)"', f.read_text(encoding="utf-8")):
            if href.startswith(("http", "mailto:", "#", "/")):
                continue
            bersaglio = (f.parent / href.split("?")[0].split("#")[0]).resolve()
            if not bersaglio.exists():
                problemi.append(f"{f.relative_to(SITO)} → link rotto {href}")

    # 3. ogni lingua ha le sue tre pagine e le sue schermate
    for loc in LINGUE:
        d = SITO / CARTELLA[loc] if CARTELLA[loc] else SITO
        for p in ("index.html", "support.html", "privacy.html"):
            if not (d / p).exists():
                problemi.append(f"manca {loc}/{p}")

    # 4. il nome del carattere citato nella risposta di supporto è quello che
    #    l'app mostra davvero. Una FAQ che dice «usa Expanded» in una lingua in
    #    cui l'app scrive «加宽» manda l'utente a cercare un comando inesistente.
    dati = json.loads(CATALOGO.read_text(encoding="utf-8"))
    for loc in LINGUE:
        atteso = dati["strings"]["Expanded"]["localizations"][BUNDLE[loc]]["stringUnit"]["value"]
        risposta = SUPPORTO[loc]["faq"][1][1]
        if atteso not in risposta:
            problemi.append(f"[{loc}] la FAQ non cita «{atteso}», il nome del carattere nell'app")

    if problemi:
        print("\n⛔ VERIFICHE FALLITE")
        for p in problemi:
            print("   ·", p)
        raise SystemExit(1)
    print("✓ verifiche superate: nessun indirizzo personale, nessun link rotto, "
          "39 pagine, nomi dei caratteri allineati all'app")


# ──────────────────────────────────────────────────────────────── main

def main() -> None:
    ap = argparse.ArgumentParser(description="Genera il sito statico di LookAt.")
    ap.add_argument("--base-url", default="",
                    help="URL pubblico del sito, es. https://TUONOME.github.io/lookat-site. "
                         "Senza, canonical/hreflang/sitemap NON vengono scritti.")
    ap.add_argument("--app-store", default="",
                    help="URL della scheda App Store. Senza, il bottone dice «presto» e non è un link.")
    ap.add_argument("--forza", action="store_true", help="rigenera anche le immagini")
    ap.add_argument("--scrivi-url-asc", action="store_true",
                    help="scrive AppStore/metadata/<loc>/{privacy,support,marketing}_url.txt "
                         "e AppStore/URL-SCHEDA.md. Richiede --base-url.")
    args = ap.parse_args()

    base_url = args.base_url.rstrip("/")

    # pulizia delle sole cartelle generate: `_sorgenti/` non si tocca mai
    for loc in LINGUE:
        if CARTELLA[loc]:
            shutil.rmtree(SITO / CARTELLA[loc], ignore_errors=True)

    print("· immagini")
    prepara_immagini(args.forza)

    print("· fogli di stile e script")
    (SITO / "assets" / "css").mkdir(parents=True, exist_ok=True)
    (SITO / "assets" / "js").mkdir(parents=True, exist_ok=True)
    shutil.copy2(SORGENTI / "statici" / "style.css", SITO / "assets" / "css" / "style.css")
    shutil.copy2(SORGENTI / "statici" / "site.js", SITO / "assets" / "js" / "site.js")

    didascalie = leggi_didascalie()
    nomi_coppie = leggi_nomi_coppie()

    for loc in LINGUE:
        for insieme, nome in ((CHROME, "CHROME"), (PRIVACY, "PRIVACY"), (SUPPORTO, "SUPPORTO")):
            if loc not in insieme:
                raise SystemExit(f"manca {loc} in {nome} (contenuti_a.py / contenuti_b.py)")
        meta = leggi_metadati(loc)
        desc = analizza_descrizione(meta["descrizione"], loc)
        cartella = SITO / CARTELLA[loc] if CARTELLA[loc] else SITO
        cartella.mkdir(parents=True, exist_ok=True)
        radice = "../" if CARTELLA[loc] else ""

        (cartella / "index.html").write_text(
            pagina_home(loc, meta, desc, didascalie, nomi_coppie, radice, base_url, args.app_store),
            encoding="utf-8")
        (cartella / "support.html").write_text(
            pagina_supporto(loc, meta, radice, base_url, args.app_store), encoding="utf-8")
        (cartella / "privacy.html").write_text(
            pagina_privacy(loc, meta, radice, base_url, args.app_store), encoding="utf-8")
        print(f"· {loc:8s} → /{CARTELLA[loc] or ''}")

    (SITO / "404.html").write_text(pagina_404(base_url), encoding="utf-8")
    (SITO / ".nojekyll").write_text("", encoding="utf-8")

    righe_robots = ["User-agent: *", "Allow: /", "Disallow: /_sorgenti/"]
    if base_url:
        righe_robots.append(f"Sitemap: {base_url}/sitemap.xml")
    (SITO / "robots.txt").write_text("\n".join(righe_robots) + "\n", encoding="utf-8")

    if base_url:
        oggi = date.today().isoformat()
        url = []
        for pagina in ("index", "support", "privacy"):
            for loc in LINGUE:
                cartella = CARTELLA[loc] + "/" if CARTELLA[loc] else ""
                mio = f"{base_url}/{cartella}{pagina}.html"
                alternative = "".join(
                    f'\n    <xhtml:link rel="alternate" hreflang="{a}" href="{base_url}/'
                    f'{CARTELLA[a] + "/" if CARTELLA[a] else ""}{pagina}.html"/>' for a in LINGUE)
                url.append(f"  <url>\n    <loc>{mio}</loc>\n    <lastmod>{oggi}</lastmod>"
                           f"{alternative}\n  </url>")
        (SITO / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(url) + "\n</urlset>\n",
            encoding="utf-8")
    else:
        (SITO / "sitemap.xml").unlink(missing_ok=True)

    if args.scrivi_url_asc:
        if not base_url:
            raise SystemExit("--scrivi-url-asc richiede --base-url: senza, gli indirizzi "
                             "da incollare in App Store Connect non esistono.")
        scrivi_url_asc(base_url)

    verifica(base_url, nomi_coppie)

    if not base_url:
        print("\n⚠️  senza --base-url il sito NON ha canonical, hreflang né sitemap.\n"
              "   Quando sai l'indirizzo definitivo rilancia:\n"
              "   python3 _sorgenti/genera-sito.py --base-url https://TUONOME.github.io/lookat-site")
    if not args.app_store:
        print("⚠️  il bottone dice «presto»: nessun link all'App Store.\n"
              "   Quando l'app è pubblicata rilancia aggiungendo:\n"
              "   --app-store https://apps.apple.com/app/id6800004772")


if __name__ == "__main__":
    main()
