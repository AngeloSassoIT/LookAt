/* ==========================================================================
   LookAt — sito statico. Nessuna dipendenza, nessuna richiesta di rete.
   Tre cose soltanto: la lingua, l'insegna dimostrativa, il menu delle lingue.
   Se JavaScript è disattivato il sito resta completo: la lingua si sceglie con
   i link del <details>, l'insegna mostra comunque il messaggio d'esempio.
   ========================================================================== */
(function () {
  "use strict";

  /* Cartella di ogni lingua, relativa alla radice del sito. La radice è
     l'inglese britannico: è la lingua di sviluppo del bundle (project.yml,
     developmentLanguage: en-GB) e quella su cui ricade chi non parla nessuna
     delle altre. */
  var CARTELLE = {
    "en-GB": "", "en-US": "en-us/", "it": "it/", "es-ES": "es-es/", "es-MX": "es-mx/",
    "fr-FR": "fr/", "de-DE": "de/", "pt-BR": "pt-br/", "nl-NL": "nl/", "ja": "ja/",
    "ko": "ko/", "zh-Hans": "zh-hans/", "zh-Hant": "zh-hant/"
  };
  var CHIAVE = "lookat-lingua";

  var html = document.documentElement;
  var linguaCorrente = html.getAttribute("data-lingua") || "en-GB";
  var radice = html.getAttribute("data-radice") || "";
  var pagina = (html.getAttribute("data-pagina") || "index") + ".html";

  function memorizza(v) { try { localStorage.setItem(CHIAVE, v); } catch (e) {} }
  function memoria() { try { return localStorage.getItem(CHIAVE); } catch (e) { return null; } }

  /* Dal codice del browser alla lingua del sito. navigator.language dà "it-CH",
     "pt-PT", "zh-TW": la corrispondenza esatta è l'eccezione, non la regola. */
  function riconosci(codice) {
    if (!codice) return null;
    var c = codice.replace("_", "-");
    if (CARTELLE[c] !== undefined) return c;
    var base = c.split("-")[0].toLowerCase();
    var regione = (c.split("-")[1] || "").toUpperCase();
    if (base === "zh") {
      // Taiwan, Hong Kong e Macao leggono il tradizionale; il resto il semplificato.
      if (/^(Hant|TW|HK|MO)$/.test(c.split("-")[1] || "")) return "zh-Hant";
      return "zh-Hans";
    }
    if (base === "en") return regione === "US" ? "en-US" : "en-GB";
    if (base === "es") return (regione && regione !== "ES") ? "es-MX" : "es-ES";
    if (base === "pt") return "pt-BR";
    if (base === "fr") return "fr-FR";
    if (base === "de") return "de-DE";
    if (base === "nl") return "nl-NL";
    if (base === "it") return "it";
    if (base === "ja") return "ja";
    if (base === "ko") return "ko";
    return null;
  }

  function linguaPreferita() {
    var elenco = navigator.languages && navigator.languages.length
      ? navigator.languages : [navigator.language];
    for (var i = 0; i < elenco.length; i++) {
      var esito = riconosci(elenco[i]);
      if (esito) return esito;
    }
    return null;
  }

  /* Il parametro ?lang= arriva dai link del selettore: serve a ricordare una
     scelta ESPLICITA, che deve vincere sulla lingua del browser per sempre. */
  var param = new URLSearchParams(location.search).get("lang");
  if (param && CARTELLE[param] !== undefined) {
    memorizza(param);
    if (history.replaceState) history.replaceState(null, "", location.pathname + location.hash);
  }

  /* Il rinvio automatico parte SOLO dalla radice e SOLO senza una scelta già
     fatta: chi è già dentro una lingua ci resta, altrimenti tornare all'inglese
     diventa impossibile. */
  if (linguaCorrente === "en-GB" && radice === "" && !param) {
    var voluta = memoria() || linguaPreferita();
    if (voluta && CARTELLE[voluta] !== undefined && voluta !== "en-GB") {
      location.replace(CARTELLE[voluta] + pagina);
      return;
    }
  } else if (!param && !memoria()) {
    memorizza(linguaCorrente);
  }

  document.addEventListener("DOMContentLoaded", function () {

    /* ── menu delle lingue: si chiude cliccando fuori o con Esc ── */
    var menu = document.querySelector(".lingue");
    if (menu) {
      document.addEventListener("click", function (e) {
        if (menu.open && !menu.contains(e.target)) menu.open = false;
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && menu.open) { menu.open = false; menu.querySelector("summary").focus(); }
      });
    }

    /* ── insegna dimostrativa ── */
    var insegna = document.querySelector(".insegna");
    if (!insegna) return;
    var nastro = insegna.querySelector(".nastro");
    var copie = nastro.querySelectorAll("span");
    var campo = document.getElementById("testo");
    var uscita = document.getElementById("contrasto");
    var esito = document.getElementById("esito");
    var bottoni = document.querySelectorAll(".coppia");
    var fermo = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function luminanza(hex) {
      var n = parseInt(hex.slice(1), 16);
      var c = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map(function (v) {
        v /= 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    }

    /* Stesso rapporto WCAG 2.1 che calcola l'app (SignSettings.contrastRatio) e
       stessa soglia di avviso: 4.5:1. Se il numero qui e quello nell'app non
       coincidessero, il sito starebbe promettendo un'altra app. */
    function contrasto(sfondo, testo) {
      var a = luminanza(sfondo), b = luminanza(testo);
      var alto = Math.max(a, b), basso = Math.min(a, b);
      return (alto + 0.05) / (basso + 0.05);
    }

    function aggiornaMisura(sfondo, testo) {
      if (!uscita) return;
      var r = contrasto(sfondo, testo);
      uscita.textContent = r.toFixed(1) + ":1";
      if (esito) {
        var ok = r >= 4.5;
        esito.textContent = esito.getAttribute(ok ? "data-ok" : "data-basso");
        esito.className = "esito " + (ok ? "ok" : "basso");
      }
    }

    /* La durata è proporzionale alla larghezza: a durata fissa un messaggio
       lungo sfreccia e uno corto striscia. ~110 px/s è la velocità a cui il
       testo resta leggibile mentre passa. */
    function rilancia() {
      nastro.style.animation = "none";
      // Lettura forzata: senza, il browser accorpa le due scritture e
      // l'animazione non riparte da capo al cambio di messaggio.
      void nastro.offsetWidth;
      var larghezza = copie[0].getBoundingClientRect().width;
      var entra = larghezza <= insegna.getBoundingClientRect().width - 24;
      insegna.classList.toggle("ferma", entra || fermo);
      if (entra || fermo) return;
      nastro.style.animation = "scorri " + Math.max(6, larghezza / 110).toFixed(1) + "s linear infinite";
    }

    function scrivi(testo) {
      for (var i = 0; i < copie.length; i++) copie[i].textContent = testo;
      rilancia();
    }

    if (campo) {
      campo.addEventListener("input", function () {
        var v = this.value.toUpperCase();
        scrivi(v.trim() ? v : this.getAttribute("data-esempio") || "LOOKAT");
      });
    }

    for (var i = 0; i < bottoni.length; i++) {
      bottoni[i].addEventListener("click", function () {
        var sfondo = this.getAttribute("data-sfondo");
        var testo = this.getAttribute("data-testo");
        insegna.style.setProperty("--fondo", sfondo);
        insegna.style.setProperty("--testo", testo);
        for (var j = 0; j < bottoni.length; j++) bottoni[j].setAttribute("aria-pressed", "false");
        this.setAttribute("aria-pressed", "true");
        aggiornaMisura(sfondo, testo);
      });
    }

    var iniziale = document.querySelector('.coppia[aria-pressed="true"]');
    if (iniziale) aggiornaMisura(iniziale.getAttribute("data-sfondo"), iniziale.getAttribute("data-testo"));

    rilancia();
    // I font di sistema arrivano dopo il primo layout: senza questo giro la
    // larghezza misurata è quella del ripiego e la durata esce sbagliata.
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(rilancia);
    var attesa;
    window.addEventListener("resize", function () {
      clearTimeout(attesa);
      attesa = setTimeout(rilancia, 180);
    });
  });
})();
