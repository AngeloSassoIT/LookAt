# -*- coding: utf-8 -*-
"""Testi del sito — parte 1: en-GB, en-US, it, es-ES, es-MX, fr-FR, de-DE.

⚠️ Qui NON si scrive il testo di vendita dell'app: nome, sottotitolo, testo
promozionale e descrizione arrivano già tradotti da
`AppStore/fastlane/metadata/<loc>/*.txt`, e le didascalie delle schermate da
`AppStore/frames.py`. Duplicarli qui significherebbe averne due versioni e
scoprirlo dopo la pubblicazione.

Qui c'è solo ciò che esiste unicamente sul sito: la struttura delle pagine,
l'informativa privacy e le risposte di supporto.
"""

CHROME = {}
PRIVACY = {}
SUPPORTO = {}

# ─────────────────────────────────────────────────────────────── en-GB
CHROME["en-GB"] = dict(
    lingua="English (UK)", sigla="EN",
    nav_home="Home", nav_supporto="Support", nav_privacy="Privacy",
    salta="Skip to content", lingua_etichetta="Language", altre_lingue="Other languages",
    cta_attesa="Coming soon on the App Store",
    cta_scarica="Download on the App Store",
    microcopy="Free · iPhone and iPad · iOS 18 or later",
    demo_titolo="Try it right here",
    demo_etichetta="Your message",
    demo_placeholder="TYPE SOMETHING",
    demo_esempio="SOFIA — PLAY MY SONG!",
    demo_coppie="Colour pair",
    demo_contrasto="Contrast",
    demo_ok="readable", demo_basso="marginal",
    demo_nota="The same twelve pairs and the same WCAG calculation the app runs on your phone.",
    sez_schermate="Inside the app",
    sez_domande="Common questions",
    chiusura_titolo="Hold up your phone.",
    chip=["No account", "No ads", "No tracking", "No network"],
    titolo_supporto="Support", titolo_privacy="Privacy policy",
    meta_supporto="How to make a sign that reads from the back row, and how to reach a human about LookAt.",
    meta_privacy="LookAt collects nothing: no account, no analytics, no network. What you type never leaves your phone.",
    data_aggiornamento="Updated 14 August 2026",
    contatto_titolo="Write to us",
    contatto_testo="One person reads this inbox, and answers. Tell us your iPhone or iPad model and your iOS version — a screenshot helps more than a paragraph.",
    piede_nota="No account. No ads. No tracking. No network.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Back to LookAt",
)
PRIVACY["en-GB"] = [
    ("The short version", [
        "LookAt collects nothing. There is no account, no advertising, no analytics and no network access at all — what you type never leaves your phone."]),
    ("Who we are", [
        "LookAt is made by SimpleBuild. For anything in this policy, write to <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Data we collect", [
        "None. Specifically, LookAt does not collect, transmit or store on any server:",
        "<ul><li>your name, e-mail address or any other personal detail;</li>"
        "<li>the messages you write on the sign;</li>"
        "<li>usage or diagnostic statistics;</li>"
        "<li>advertising identifiers or any other identifier;</li>"
        "<li>your location, contacts, photos or microphone.</li></ul>",
        "The app asks for no permission at all: there is no dialogue to accept, because there is nothing to grant."]),
    ("What stays on your device", [
        "Your draft message, your saved presets and your colour, typeface and motion settings are stored on the device itself, in the standard iOS preferences area of the app. They never leave it and we cannot read them.",
        "Deleting the app deletes them. If you have iCloud or an encrypted computer backup enabled, iOS may include them in that backup: that copy is inside your Apple account, under your control, and is governed by Apple's terms, not by ours."]),
    ("No network", [
        "LookAt has no networking code. It works in aeroplane mode, in an aircraft cabin, in a basement venue and on a phone with no SIM. This is not a promise about our intentions: it is a property of the app you can test in ten seconds."]),
    ("Third parties", [
        "There is no advertising library, no analytics kit and no third-party SDK of any kind. LookAt never shows the tracking permission request, because it has nothing to track.",
        "Apple operates the App Store and, as the distributor, records downloads and any purchase according to <a href=\"https://www.apple.com/legal/privacy/\" rel=\"noopener\">Apple's privacy policy</a>. In App Store Connect we see only aggregate figures — how many downloads in a country, for instance — never a person."]),
    ("Children", [
        "LookAt is rated 4+ and has no content from other people, no links out and nothing to buy. Because nothing at all is collected, nothing about a child is collected either."]),
    ("Your rights", [
        "Under the GDPR you have the right to access, correct and erase your personal data. We hold none: there is nothing for us to send you and nothing for us to delete. To remove the data on your device, delete the app.",
        "If you believe this is not the case, write to us — and you may also complain to your national data protection authority."]),
    ("Changes to this policy", [
        "If the app ever changes what it does, this page changes first, and the date at the top changes with it."]),
    ("Contact", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["en-GB"] = dict(
    intro="Most of what goes wrong with a phone sign is a matter of letter height and contrast, and both are fixable in a few seconds. Start here; if the answer is not below, write and a human will reply.",
    faq=[
        ("Does LookAt need an internet connection?",
         "No — not once. The app has no networking code at all, so it works in aeroplane mode, underground and on a phone with no SIM. Nothing you type leaves your phone."),
        ("Nobody can read my sign. What should I change?",
         "Four things, in this order. <strong>Shorten the message</strong>: the letters are as tall as the screen allows, so fewer characters means bigger letters. <strong>Use Expanded</strong>, the widest face. <strong>Pick a pair with real contrast</strong> — the app shows you the measured ratio and warns you below 4.5:1. <strong>Turn the phone sideways</strong> for a wider sign. And one honest limit: in direct sunlight, or beyond a few dozen metres, a phone screen loses to daylight and distance no matter what you choose."),
        ("The screen dims, or turns off, while the sign is up.",
         "While the sign is showing, LookAt raises brightness to maximum and stops the screen from sleeping, then puts your own brightness back the moment you leave. Two things can still dim it and no app can override them: Low Power Mode, and iOS reducing brightness when the phone gets hot. If the phone is warm, let it cool and it comes back."),
        ("How do I save a message and use it again?",
         "Save it as a preset — up to 24 of them. Saving under a name you already used overwrites that preset instead of creating a second one with the same name."),
        ("Does it work on iPad?",
         "Yes. LookAt is one app for iPhone and iPad, and needs iOS or iPadOS 18 or later. On iPad the sign is simply wider."),
        ("Scrolling and blinking do not work.",
         "Check Settings → Accessibility → Motion → Reduce Motion. When that is on, LookAt deliberately stops both scrolling and blinking — a six-times-a-second flash is exactly the stimulus that setting exists to damp — and shows the whole message, still and fully visible."),
        ("Is it really free?",
         "Yes: free, with nothing to buy inside, no advertising and no account."),
        ("How do I delete my data?",
         "Delete the app. Everything — draft, presets, settings — lives on the device and goes with it. There is no account to close and no server to write to."),
    ],
)

# ─────────────────────────────────────────────────────────────── en-US
CHROME["en-US"] = dict(CHROME["en-GB"],
    lingua="English (US)", sigla="EN",
    demo_coppie="Color pair",
    demo_nota="The same twelve pairs and the same WCAG calculation the app runs on your phone.",
    microcopy="Free · iPhone and iPad · iOS 18 or later",
    data_aggiornamento="Updated August 14, 2026",
    meta_supporto="How to make a sign that reads from the back row, and how to reach a human about LookAt.",
)
PRIVACY["en-US"] = [
    ("The short version", [
        "LookAt collects nothing. There is no account, no advertising, no analytics and no network access at all — what you type never leaves your phone."]),
    ("Who we are", [
        "LookAt is made by SimpleBuild. For anything in this policy, write to <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Data we collect", [
        "None. Specifically, LookAt does not collect, transmit or store on any server:",
        "<ul><li>your name, email address or any other personal detail;</li>"
        "<li>the messages you write on the sign;</li>"
        "<li>usage or diagnostic statistics;</li>"
        "<li>advertising identifiers or any other identifier;</li>"
        "<li>your location, contacts, photos or microphone.</li></ul>",
        "The app asks for no permission at all: there is no dialog to accept, because there is nothing to grant."]),
    ("What stays on your device", [
        "Your draft message, your saved presets and your color, typeface and motion settings are stored on the device itself, in the standard iOS preferences area of the app. They never leave it and we cannot read them.",
        "Deleting the app deletes them. If you have iCloud or an encrypted computer backup enabled, iOS may include them in that backup: that copy is inside your Apple account, under your control, and is governed by Apple's terms, not by ours."]),
    ("No network", [
        "LookAt has no networking code. It works in airplane mode, in an aircraft cabin, in a basement venue and on a phone with no SIM. This is not a promise about our intentions: it is a property of the app you can test in ten seconds."]),
    ("Third parties", [
        "There is no advertising library, no analytics kit and no third-party SDK of any kind. LookAt never shows the tracking permission request, because it has nothing to track.",
        "Apple operates the App Store and, as the distributor, records downloads and any purchase according to <a href=\"https://www.apple.com/legal/privacy/\" rel=\"noopener\">Apple's privacy policy</a>. In App Store Connect we see only aggregate figures — how many downloads in a country, for instance — never a person."]),
    ("Children", [
        "LookAt is rated 4+ and has no content from other people, no links out and nothing to buy. Because nothing at all is collected, nothing about a child is collected either."]),
    ("Your rights", [
        "Privacy laws such as the GDPR and the CCPA give you the right to access, correct and delete your personal information. We hold none: there is nothing for us to send you and nothing for us to delete. To remove the data on your device, delete the app.",
        "We do not sell or share personal information, because we have none to sell."]),
    ("Changes to this policy", [
        "If the app ever changes what it does, this page changes first, and the date at the top changes with it."]),
    ("Contact", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["en-US"] = dict(SUPPORTO["en-GB"])
SUPPORTO["en-US"]["faq"] = [
    (d, r.replace("aeroplane mode", "airplane mode").replace("colour", "color").replace("metres", "meters"))
    for d, r in SUPPORTO["en-GB"]["faq"]
]

# ────────────────────────────────────────────────────────────────── it
CHROME["it"] = dict(
    lingua="Italiano", sigla="IT",
    nav_home="Home", nav_supporto="Supporto", nav_privacy="Privacy",
    salta="Vai al contenuto", lingua_etichetta="Lingua", altre_lingue="Altre lingue",
    cta_attesa="Presto su App Store",
    cta_scarica="Scarica su App Store",
    microcopy="Gratis · iPhone e iPad · iOS 18 o successivo",
    demo_titolo="Provalo qui",
    demo_etichetta="Il tuo messaggio",
    demo_placeholder="SCRIVI QUALCOSA",
    demo_esempio="SOFIA · TI AMO",
    demo_coppie="Coppia di colori",
    demo_contrasto="Contrasto",
    demo_ok="si legge", demo_basso="al limite",
    demo_nota="Le stesse dodici coppie e lo stesso calcolo WCAG che l'app fa sul telefono.",
    sez_schermate="Dentro l'app",
    sez_domande="Domande frequenti",
    chiusura_titolo="Alza il telefono.",
    chip=["Nessun account", "Nessuna pubblicità", "Nessun tracciamento", "Nessuna rete"],
    titolo_supporto="Supporto", titolo_privacy="Informativa sulla privacy",
    meta_supporto="Come si fa un cartello che si legge dall'ultima fila, e come si parla con una persona vera.",
    meta_privacy="LookAt non raccoglie nulla: nessun account, nessuna statistica, nessuna rete. Quello che scrivi non esce dal telefono.",
    data_aggiornamento="Aggiornata il 14 agosto 2026",
    contatto_titolo="Scrivici",
    contatto_testo="Questa casella la legge una persona, e risponde. Indica il modello di iPhone o iPad e la versione di iOS: uno screenshot aiuta più di un paragrafo.",
    piede_nota="Nessun account. Nessuna pubblicità. Nessun tracciamento. Nessuna rete.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Torna a LookAt",
)
PRIVACY["it"] = [
    ("In breve", [
        "LookAt non raccoglie nulla. Non c'è un account, non c'è pubblicità, non ci sono statistiche e non c'è alcun accesso alla rete: quello che scrivi non esce dal telefono."]),
    ("Chi siamo", [
        "LookAt è sviluppata da SimpleBuild. Per qualsiasi cosa riguardi questa informativa scrivi a <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Dati che raccogliamo", [
        "Nessuno. Nello specifico, LookAt non raccoglie, non trasmette e non conserva su alcun server:",
        "<ul><li>il tuo nome, il tuo indirizzo e-mail o qualunque altro dato personale;</li>"
        "<li>i messaggi che scrivi sul cartello;</li>"
        "<li>statistiche d'uso o dati diagnostici;</li>"
        "<li>identificativi pubblicitari o identificativi di altro tipo;</li>"
        "<li>la tua posizione, i contatti, le foto o il microfono.</li></ul>",
        "L'app non chiede alcun permesso: non c'è nessuna finestra da accettare, perché non c'è nulla da concedere."]),
    ("Cosa resta sul dispositivo", [
        "La bozza del messaggio, i preset salvati e le impostazioni di colore, carattere e movimento restano sul dispositivo, nell'area preferenze standard di iOS riservata all'app. Non escono da lì e noi non possiamo leggerli.",
        "Se disinstalli l'app, spariscono con essa. Se hai attivo il backup su iCloud o un backup cifrato sul computer, iOS può includerli in quella copia: quella copia sta dentro il tuo account Apple, è sotto il tuo controllo ed è regolata dalle condizioni di Apple, non dalle nostre."]),
    ("Nessuna rete", [
        "Nel codice di LookAt non esiste alcuna funzione di rete. Funziona in modalità aereo, in cabina, in un locale interrato e su un telefono senza SIM. Non è una promessa sulle nostre intenzioni: è una proprietà dell'app che puoi verificare in dieci secondi."]),
    ("Terze parti", [
        "Non c'è alcuna libreria pubblicitaria, alcun sistema di statistiche né alcun SDK di terze parti. LookAt non mostra mai la richiesta di autorizzazione al tracciamento, perché non ha nulla da tracciare.",
        "L'App Store è gestito da Apple che, in quanto distributore, registra i download e gli eventuali acquisti secondo la <a href=\"https://www.apple.com/it/legal/privacy/\" rel=\"noopener\">informativa sulla privacy di Apple</a>. In App Store Connect vediamo solo numeri aggregati — quanti download in un Paese, per esempio — mai una persona."]),
    ("Minori", [
        "LookAt ha classificazione 4+, non contiene contenuti scritti da altre persone, non porta fuori dall'app e non ha nulla da comprare. Poiché non viene raccolto nulla, non viene raccolto nulla nemmeno sui minori."]),
    ("I tuoi diritti", [
        "Il GDPR ti dà diritto di accedere ai tuoi dati personali, correggerli e cancellarli. Noi non ne abbiamo: non c'è nulla che possiamo inviarti e nulla che possiamo cancellare. Per eliminare i dati che stanno sul dispositivo, disinstalla l'app.",
        "Se ritieni che le cose non stiano così, scrivici — e puoi comunque rivolgerti al Garante per la protezione dei dati personali."]),
    ("Modifiche a questa informativa", [
        "Se un giorno l'app cambierà quello che fa, questa pagina cambierà prima, e con essa la data in cima."]),
    ("Contatti", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["it"] = dict(
    intro="Quasi tutto quello che non funziona in un cartello fatto col telefono è una questione di altezza delle lettere e di contrasto, e si risolve in pochi secondi. Parti da qui; se la risposta non c'è, scrivi: risponde una persona.",
    faq=[
        ("LookAt ha bisogno di una connessione a internet?",
         "No, mai. Nel codice dell'app non c'è alcuna funzione di rete: funziona in modalità aereo, sottoterra e su un telefono senza SIM. Quello che scrivi non esce dal telefono."),
        ("Il mio cartello non si legge. Cosa devo cambiare?",
         "Quattro cose, in quest'ordine. <strong>Accorcia il messaggio</strong>: le lettere sono alte quanto lo schermo permette, quindi meno caratteri significa lettere più grandi. <strong>Usa Espanso</strong>, il carattere con le aste più larghe. <strong>Scegli una coppia con contrasto vero</strong>: l'app mostra il rapporto misurato e ti avvisa sotto 4,5:1. <strong>Gira il telefono</strong> per un cartello più largo. E un limite onesto: in pieno sole, o oltre qualche decina di metri, lo schermo di un telefono perde comunque, qualunque colore tu scelga."),
        ("Lo schermo si abbassa, o si spegne, mentre il cartello è alzato.",
         "Finché il cartello è a schermo, LookAt porta la luminosità al massimo e impedisce allo schermo di spegnersi, poi rimette la <em>tua</em> luminosità appena esci. Due cose possono comunque abbassarla e nessuna app può impedirlo: il risparmio energetico e la riduzione che iOS applica quando il telefono si scalda. Se è caldo, lascialo raffreddare e torna come prima."),
        ("Come salvo un messaggio per riusarlo?",
         "Salvalo come preset: se ne tengono fino a 24. Salvando con un nome già usato si sovrascrive quel preset, invece di crearne un secondo con lo stesso nome."),
        ("Funziona su iPad?",
         "Sì. LookAt è una sola app per iPhone e iPad e richiede iOS o iPadOS 18 o successivo. Su iPad il cartello è semplicemente più largo."),
        ("Lo scorrimento e il lampeggio non funzionano.",
         "Controlla Impostazioni → Accessibilità → Movimento → Riduci movimento. Quando è attivo LookAt ferma di proposito sia lo scorrimento sia il lampeggio — un lampo sei volte al secondo è esattamente lo stimolo che quell'impostazione serve a smorzare — e mostra il messaggio intero, fermo e completamente visibile."),
        ("È davvero gratis?",
         "Sì: gratis, senza nulla da comprare dentro, senza pubblicità e senza account."),
        ("Come cancello i miei dati?",
         "Disinstalla l'app. Tutto — bozza, preset, impostazioni — sta sul dispositivo e se ne va con lei. Non c'è un account da chiudere né un server a cui scrivere."),
    ],
)

# ─────────────────────────────────────────────────────────────── es-ES
CHROME["es-ES"] = dict(
    lingua="Español (España)", sigla="ES",
    nav_home="Inicio", nav_supporto="Soporte", nav_privacy="Privacidad",
    salta="Ir al contenido", lingua_etichetta="Idioma", altre_lingue="Otros idiomas",
    cta_attesa="Pronto en el App Store",
    cta_scarica="Consíguelo en el App Store",
    microcopy="Gratis · iPhone y iPad · iOS 18 o posterior",
    demo_titolo="Pruébalo aquí",
    demo_etichetta="Tu mensaje",
    demo_placeholder="ESCRIBE ALGO",
    demo_esempio="SOFÍA · TE QUIERO",
    demo_coppie="Pareja de colores",
    demo_contrasto="Contraste",
    demo_ok="se lee", demo_basso="al límite",
    demo_nota="Las mismas doce parejas y el mismo cálculo WCAG que la app hace en tu móvil.",
    sez_schermate="Dentro de la app",
    sez_domande="Preguntas frecuentes",
    chiusura_titolo="Levanta el móvil.",
    chip=["Sin cuenta", "Sin anuncios", "Sin rastreo", "Sin red"],
    titolo_supporto="Soporte", titolo_privacy="Política de privacidad",
    meta_supporto="Cómo hacer una pancarta que se lea desde el fondo, y cómo hablar con una persona de verdad.",
    meta_privacy="LookAt no recoge nada: sin cuenta, sin estadísticas, sin red. Lo que escribes no sale del móvil.",
    data_aggiornamento="Actualizada el 14 de agosto de 2026",
    contatto_titolo="Escríbenos",
    contatto_testo="Este buzón lo lee una persona, y contesta. Indica el modelo de iPhone o iPad y la versión de iOS: una captura ayuda más que un párrafo.",
    piede_nota="Sin cuenta. Sin anuncios. Sin rastreo. Sin red.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Volver a LookAt",
)
PRIVACY["es-ES"] = [
    ("En resumen", [
        "LookAt no recoge nada. No hay cuenta, no hay publicidad, no hay estadísticas y no hay ningún acceso a la red: lo que escribes no sale del móvil."]),
    ("Quiénes somos", [
        "LookAt está desarrollada por SimpleBuild. Para cualquier cosa relacionada con esta política escribe a <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Datos que recogemos", [
        "Ninguno. En concreto, LookAt no recoge, no transmite y no guarda en ningún servidor:",
        "<ul><li>tu nombre, tu correo electrónico ni ningún otro dato personal;</li>"
        "<li>los mensajes que escribes en la pancarta;</li>"
        "<li>estadísticas de uso ni datos de diagnóstico;</li>"
        "<li>identificadores publicitarios ni de ningún otro tipo;</li>"
        "<li>tu ubicación, contactos, fotos o micrófono.</li></ul>",
        "La app no pide ningún permiso: no hay ninguna ventana que aceptar, porque no hay nada que conceder."]),
    ("Qué se queda en tu dispositivo", [
        "El borrador del mensaje, los ajustes guardados y tus preferencias de color, tipografía y movimiento se quedan en el dispositivo, en el área de preferencias estándar de iOS reservada a la app. No salen de ahí y nosotros no podemos leerlos.",
        "Si desinstalas la app, desaparecen con ella. Si tienes activada la copia en iCloud o una copia cifrada en el ordenador, iOS puede incluirlos en esa copia: esa copia está dentro de tu cuenta de Apple, bajo tu control, y se rige por las condiciones de Apple, no por las nuestras."]),
    ("Sin red", [
        "En el código de LookAt no existe ninguna función de red. Funciona en modo avión, en un avión, en una sala subterránea y en un móvil sin SIM. No es una promesa sobre nuestras intenciones: es una propiedad de la app que puedes comprobar en diez segundos."]),
    ("Terceros", [
        "No hay ninguna biblioteca publicitaria, ningún sistema de analítica ni ningún SDK de terceros. LookAt nunca muestra la solicitud de permiso de seguimiento, porque no tiene nada que seguir.",
        "El App Store lo gestiona Apple que, como distribuidor, registra las descargas y las compras según la <a href=\"https://www.apple.com/es/legal/privacy/\" rel=\"noopener\">política de privacidad de Apple</a>. En App Store Connect solo vemos cifras agregadas —cuántas descargas en un país, por ejemplo—, nunca una persona."]),
    ("Menores", [
        "LookAt tiene clasificación 4+, no contiene contenido escrito por otras personas, no lleva fuera de la app y no tiene nada que comprar. Como no se recoge nada, tampoco se recoge nada sobre un menor."]),
    ("Tus derechos", [
        "El RGPD te da derecho a acceder a tus datos personales, corregirlos y suprimirlos. Nosotros no tenemos ninguno: no hay nada que podamos enviarte ni nada que podamos borrar. Para eliminar los datos del dispositivo, desinstala la app.",
        "Si crees que no es así, escríbenos — y puedes además reclamar ante la Agencia Española de Protección de Datos."]),
    ("Cambios en esta política", [
        "Si algún día la app cambia lo que hace, esta página cambiará antes, y con ella la fecha de arriba."]),
    ("Contacto", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["es-ES"] = dict(
    intro="Casi todo lo que falla en una pancarta hecha con el móvil es cuestión de altura de letra y de contraste, y se arregla en unos segundos. Empieza por aquí; si la respuesta no está, escribe: contesta una persona.",
    faq=[
        ("¿LookAt necesita conexión a internet?",
         "No, nunca. En el código de la app no hay ninguna función de red: funciona en modo avión, bajo tierra y en un móvil sin SIM. Lo que escribes no sale del teléfono."),
        ("Mi pancarta no se lee. ¿Qué cambio?",
         "Cuatro cosas, en este orden. <strong>Acorta el mensaje</strong>: las letras son tan altas como permite la pantalla, así que menos caracteres significa letras más grandes. <strong>Usa Expandida</strong>, la tipografía de trazo más ancho. <strong>Elige una pareja con contraste real</strong>: la app muestra la proporción medida y te avisa por debajo de 4,5:1. <strong>Gira el móvil</strong> para una pancarta más ancha. Y un límite honesto: a pleno sol, o a más de unas decenas de metros, la pantalla de un móvil pierde igualmente, elijas el color que elijas."),
        ("La pantalla se atenúa, o se apaga, con la pancarta levantada.",
         "Mientras la pancarta está en pantalla, LookAt sube el brillo al máximo e impide que la pantalla se apague, y devuelve <em>tu</em> brillo en cuanto sales. Dos cosas pueden bajarlo igualmente y ninguna app puede evitarlo: el modo de bajo consumo y la reducción que aplica iOS cuando el móvil se calienta. Si está caliente, déjalo enfriar y vuelve a ser el de antes."),
        ("¿Cómo guardo un mensaje para reutilizarlo?",
         "Guárdalo como ajuste preestablecido: caben hasta 24. Si guardas con un nombre que ya existe, se sobrescribe ese ajuste en vez de crear un segundo con el mismo nombre."),
        ("¿Funciona en iPad?",
         "Sí. LookAt es una sola app para iPhone y iPad, y necesita iOS o iPadOS 18 o posterior. En el iPad la pancarta es simplemente más ancha."),
        ("El desplazamiento y el parpadeo no funcionan.",
         "Comprueba Ajustes → Accesibilidad → Movimiento → Reducir movimiento. Cuando está activado, LookAt detiene a propósito tanto el desplazamiento como el parpadeo —un destello seis veces por segundo es justo el estímulo que ese ajuste existe para amortiguar— y muestra el mensaje entero, quieto y totalmente visible."),
        ("¿Es gratis de verdad?",
         "Sí: gratis, sin nada que comprar dentro, sin publicidad y sin cuenta."),
        ("¿Cómo borro mis datos?",
         "Desinstala la app. Todo —borrador, ajustes guardados, preferencias— está en el dispositivo y se va con ella. No hay cuenta que cerrar ni servidor al que escribir."),
    ],
)

# ─────────────────────────────────────────────────────────────── es-MX
CHROME["es-MX"] = dict(CHROME["es-ES"],
    lingua="Español (Latinoamérica)", sigla="ES",
    demo_esempio="SOFÍA · TE AMO",
    microcopy="Gratis · iPhone y iPad · iOS 18 o posterior",
    demo_nota="Las mismas doce parejas y el mismo cálculo WCAG que la app hace en tu celular.",
    chiusura_titolo="Levanta el celular.",
    meta_privacy="LookAt no recoge nada: sin cuenta, sin estadísticas, sin red. Lo que escribes no sale del celular.",
    contatto_testo="Este buzón lo lee una persona, y contesta. Indica el modelo de iPhone o iPad y la versión de iOS: una captura ayuda más que un párrafo.",
)
PRIVACY["es-MX"] = [
    ("En resumen", [
        "LookAt no recoge nada. No hay cuenta, no hay publicidad, no hay estadísticas y no hay ningún acceso a la red: lo que escribes no sale del celular."]),
    ("Quiénes somos", [
        "LookAt está desarrollada por SimpleBuild. Para cualquier cosa relacionada con esta política escribe a <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Datos que recogemos", [
        "Ninguno. En concreto, LookAt no recoge, no transmite y no guarda en ningún servidor:",
        "<ul><li>tu nombre, tu correo electrónico ni ningún otro dato personal;</li>"
        "<li>los mensajes que escribes en el letrero;</li>"
        "<li>estadísticas de uso ni datos de diagnóstico;</li>"
        "<li>identificadores publicitarios ni de ningún otro tipo;</li>"
        "<li>tu ubicación, contactos, fotos o micrófono.</li></ul>",
        "La app no pide ningún permiso: no hay ninguna ventana que aceptar, porque no hay nada que conceder."]),
    ("Qué se queda en tu dispositivo", [
        "El borrador del mensaje, los ajustes guardados y tus preferencias de color, tipografía y movimiento se quedan en el dispositivo, en el área de preferencias estándar de iOS reservada a la app. No salen de ahí y nosotros no podemos leerlos.",
        "Si desinstalas la app, desaparecen con ella. Si tienes activado el respaldo en iCloud o un respaldo cifrado en la computadora, iOS puede incluirlos en esa copia: esa copia está dentro de tu cuenta de Apple, bajo tu control, y se rige por las condiciones de Apple, no por las nuestras."]),
    ("Sin red", [
        "En el código de LookAt no existe ninguna función de red. Funciona en modo avión, en un avión, en un lugar subterráneo y en un celular sin SIM. No es una promesa sobre nuestras intenciones: es una propiedad de la app que puedes comprobar en diez segundos."]),
    ("Terceros", [
        "No hay ninguna biblioteca publicitaria, ningún sistema de analítica ni ningún SDK de terceros. LookAt nunca muestra la solicitud de permiso de seguimiento, porque no tiene nada que seguir.",
        "El App Store lo opera Apple que, como distribuidor, registra las descargas y las compras según la <a href=\"https://www.apple.com/mx/legal/privacy/\" rel=\"noopener\">política de privacidad de Apple</a>. En App Store Connect solo vemos cifras agregadas —cuántas descargas en un país, por ejemplo—, nunca una persona."]),
    ("Menores", [
        "LookAt tiene clasificación 4+, no contiene contenido escrito por otras personas, no lleva fuera de la app y no tiene nada que comprar. Como no se recoge nada, tampoco se recoge nada sobre un menor."]),
    ("Tus derechos", [
        "Las leyes de protección de datos te dan derecho a acceder a tus datos personales, corregirlos y eliminarlos. Nosotros no tenemos ninguno: no hay nada que podamos enviarte ni nada que podamos borrar. Para eliminar los datos del dispositivo, desinstala la app."]),
    ("Cambios en esta política", [
        "Si algún día la app cambia lo que hace, esta página cambiará antes, y con ella la fecha de arriba."]),
    ("Contacto", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["es-MX"] = dict(
    intro="Casi todo lo que falla en un letrero hecho con el celular es cuestión de altura de letra y de contraste, y se arregla en unos segundos. Empieza por aquí; si la respuesta no está, escribe: contesta una persona.",
    faq=[
        ("¿LookAt necesita conexión a internet?",
         "No, nunca. En el código de la app no hay ninguna función de red: funciona en modo avión, bajo tierra y en un celular sin SIM. Lo que escribes no sale del teléfono."),
        ("Mi letrero no se lee. ¿Qué cambio?",
         "Cuatro cosas, en este orden. <strong>Acorta el mensaje</strong>: las letras son tan altas como permite la pantalla, así que menos caracteres significa letras más grandes. <strong>Usa Expandida</strong>, la tipografía de trazo más ancho. <strong>Elige una pareja con contraste real</strong>: la app muestra la proporción medida y te avisa por debajo de 4.5:1. <strong>Gira el celular</strong> para un letrero más ancho. Y un límite honesto: a pleno sol, o a más de unas decenas de metros, la pantalla de un celular pierde igual, elijas el color que elijas."),
        ("La pantalla se atenúa, o se apaga, con el letrero levantado.",
         "Mientras el letrero está en pantalla, LookAt sube el brillo al máximo e impide que la pantalla se apague, y devuelve <em>tu</em> brillo apenas sales. Dos cosas pueden bajarlo igualmente y ninguna app puede evitarlo: el modo de bajo consumo y la reducción que aplica iOS cuando el celular se calienta. Si está caliente, déjalo enfriar y vuelve a ser el de antes."),
        ("¿Cómo guardo un mensaje para reutilizarlo?",
         "Guárdalo como preajuste: caben hasta 24. Si guardas con un nombre que ya existe, se sobrescribe ese preajuste en vez de crear un segundo con el mismo nombre."),
        ("¿Funciona en iPad?",
         "Sí. LookAt es una sola app para iPhone y iPad, y necesita iOS o iPadOS 18 o posterior. En el iPad el letrero es simplemente más ancho."),
        ("El desplazamiento y el parpadeo no funcionan.",
         "Revisa Configuración → Accesibilidad → Movimiento → Reducir movimiento. Cuando está activado, LookAt detiene a propósito tanto el desplazamiento como el parpadeo —un destello seis veces por segundo es justo el estímulo que ese ajuste existe para amortiguar— y muestra el mensaje entero, quieto y totalmente visible."),
        ("¿Es gratis de verdad?",
         "Sí: gratis, sin nada que comprar dentro, sin publicidad y sin cuenta."),
        ("¿Cómo borro mis datos?",
         "Desinstala la app. Todo —borrador, preajustes, preferencias— está en el dispositivo y se va con ella. No hay cuenta que cerrar ni servidor al que escribir."),
    ],
)

# ─────────────────────────────────────────────────────────────── fr-FR
CHROME["fr-FR"] = dict(
    lingua="Français", sigla="FR",
    nav_home="Accueil", nav_supporto="Assistance", nav_privacy="Confidentialité",
    salta="Aller au contenu", lingua_etichetta="Langue", altre_lingue="Autres langues",
    cta_attesa="Bientôt sur l'App Store",
    cta_scarica="Télécharger dans l'App Store",
    microcopy="Gratuit · iPhone et iPad · iOS 18 ou version ultérieure",
    demo_titolo="Essayez ici",
    demo_etichetta="Votre message",
    demo_placeholder="ÉCRIVEZ QUELQUE CHOSE",
    demo_esempio="SOFIA · JE T'AIME",
    demo_coppie="Duo de couleurs",
    demo_contrasto="Contraste",
    demo_ok="lisible", demo_basso="limite",
    demo_nota="Les douze mêmes duos et le même calcul WCAG que l'app effectue sur votre téléphone.",
    sez_schermate="Dans l'app",
    sez_domande="Questions fréquentes",
    chiusura_titolo="Levez votre téléphone.",
    chip=["Aucun compte", "Aucune publicité", "Aucun suivi", "Aucun réseau"],
    titolo_supporto="Assistance", titolo_privacy="Politique de confidentialité",
    meta_supporto="Comment faire une pancarte lisible du fond de la salle, et comment joindre une vraie personne.",
    meta_privacy="LookAt ne collecte rien : aucun compte, aucune statistique, aucun réseau. Ce que vous écrivez ne quitte pas le téléphone.",
    data_aggiornamento="Mise à jour le 14 août 2026",
    contatto_titolo="Écrivez-nous",
    contatto_testo="Cette boîte est lue par une personne, qui répond. Indiquez le modèle d'iPhone ou d'iPad et la version d'iOS : une capture d'écran aide plus qu'un paragraphe.",
    piede_nota="Aucun compte. Aucune publicité. Aucun suivi. Aucun réseau.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Retour à LookAt",
)
PRIVACY["fr-FR"] = [
    ("En bref", [
        "LookAt ne collecte rien. Pas de compte, pas de publicité, pas de statistiques et aucun accès au réseau : ce que vous écrivez ne quitte pas le téléphone."]),
    ("Qui nous sommes", [
        "LookAt est développée par SimpleBuild. Pour toute question sur cette politique, écrivez à <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Données collectées", [
        "Aucune. Concrètement, LookAt ne collecte pas, ne transmet pas et ne conserve sur aucun serveur :",
        "<ul><li>votre nom, votre adresse e-mail ni aucune autre donnée personnelle ;</li>"
        "<li>les messages que vous écrivez sur la pancarte ;</li>"
        "<li>de statistiques d'utilisation ni de données de diagnostic ;</li>"
        "<li>d'identifiant publicitaire ni d'identifiant d'aucune sorte ;</li>"
        "<li>votre position, vos contacts, vos photos ou votre micro.</li></ul>",
        "L'app ne demande aucune autorisation : il n'y a aucune fenêtre à accepter, puisqu'il n'y a rien à accorder."]),
    ("Ce qui reste sur votre appareil", [
        "Le brouillon du message, les préréglages enregistrés et vos réglages de couleur, de police et de mouvement restent sur l'appareil, dans la zone de préférences standard d'iOS réservée à l'app. Ils n'en sortent pas et nous ne pouvons pas les lire.",
        "Si vous supprimez l'app, ils disparaissent avec elle. Si vous avez activé la sauvegarde iCloud ou une sauvegarde chiffrée sur ordinateur, iOS peut les y inclure : cette copie se trouve dans votre compte Apple, sous votre contrôle, et relève des conditions d'Apple, pas des nôtres."]),
    ("Aucun réseau", [
        "Le code de LookAt ne contient aucune fonction réseau. L'app fonctionne en mode Avion, en cabine, dans une salle en sous-sol et sur un téléphone sans SIM. Ce n'est pas une promesse sur nos intentions : c'est une propriété de l'app, vérifiable en dix secondes."]),
    ("Tiers", [
        "Aucune régie publicitaire, aucun outil de mesure d'audience, aucun SDK tiers. LookAt n'affiche jamais la demande d'autorisation de suivi, car elle n'a rien à suivre.",
        "L'App Store est exploité par Apple qui, en tant que distributeur, enregistre les téléchargements et les achats éventuels conformément à la <a href=\"https://www.apple.com/fr/legal/privacy/\" rel=\"noopener\">politique de confidentialité d'Apple</a>. Dans App Store Connect, nous ne voyons que des chiffres agrégés — combien de téléchargements dans un pays, par exemple — jamais une personne."]),
    ("Enfants", [
        "LookAt est classée 4+, ne contient aucun contenu écrit par d'autres personnes, ne renvoie nulle part et n'a rien à vendre. Puisque rien n'est collecté, rien n'est collecté non plus au sujet d'un enfant."]),
    ("Vos droits", [
        "Le RGPD vous donne le droit d'accéder à vos données personnelles, de les rectifier et de les effacer. Nous n'en détenons aucune : nous n'avons rien à vous transmettre et rien à effacer. Pour supprimer les données présentes sur l'appareil, supprimez l'app.",
        "Si vous pensez que ce n'est pas le cas, écrivez-nous — et vous pouvez aussi saisir la CNIL."]),
    ("Modifications de cette politique", [
        "Si un jour l'app change ce qu'elle fait, cette page changera d'abord, et la date en haut avec elle."]),
    ("Contact", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["fr-FR"] = dict(
    intro="Presque tout ce qui cloche sur une pancarte faite avec un téléphone tient à la hauteur des lettres et au contraste, et se règle en quelques secondes. Commencez ici ; si la réponse n'y est pas, écrivez : c'est une personne qui répond.",
    faq=[
        ("LookAt a-t-elle besoin d'une connexion internet ?",
         "Non, jamais. Le code de l'app ne contient aucune fonction réseau : elle marche en mode Avion, en sous-sol et sur un téléphone sans SIM. Ce que vous écrivez ne quitte pas le téléphone."),
        ("Ma pancarte est illisible. Que changer ?",
         "Quatre choses, dans cet ordre. <strong>Raccourcissez le message</strong> : les lettres sont aussi hautes que l'écran le permet, donc moins de caractères veut dire des lettres plus grandes. <strong>Utilisez Étendue</strong>, la police aux traits les plus larges. <strong>Choisissez un duo réellement contrasté</strong> : l'app affiche le rapport mesuré et vous avertit sous 4,5:1. <strong>Tournez le téléphone</strong> pour une pancarte plus large. Et une limite honnête : en plein soleil, ou au-delà de quelques dizaines de mètres, l'écran d'un téléphone perd de toute façon, quelles que soient les couleurs."),
        ("L'écran s'assombrit ou s'éteint pendant que la pancarte est levée.",
         "Tant que la pancarte est affichée, LookAt met la luminosité au maximum et empêche l'écran de s'éteindre, puis rétablit <em>votre</em> luminosité dès que vous sortez. Deux choses peuvent quand même la baisser, et aucune app ne peut s'y opposer : le mode économie d'énergie et la réduction appliquée par iOS quand le téléphone chauffe. S'il est chaud, laissez-le refroidir et tout revient."),
        ("Comment enregistrer un message pour le réutiliser ?",
         "Enregistrez-le comme préréglage : on peut en garder 24. Enregistrer sous un nom déjà utilisé remplace ce préréglage au lieu d'en créer un deuxième portant le même nom."),
        ("Est-ce que ça marche sur iPad ?",
         "Oui. LookAt est une seule app pour iPhone et iPad, et demande iOS ou iPadOS 18 ou version ultérieure. Sur iPad, la pancarte est simplement plus large."),
        ("Le défilement et le clignotement ne fonctionnent pas.",
         "Vérifiez Réglages → Accessibilité → Mouvement → Réduire les animations. Quand c'est activé, LookAt arrête volontairement le défilement et le clignotement — un éclat six fois par seconde est exactement le stimulus que ce réglage sert à atténuer — et affiche le message entier, fixe et entièrement visible."),
        ("Est-ce vraiment gratuit ?",
         "Oui : gratuit, sans rien à acheter à l'intérieur, sans publicité et sans compte."),
        ("Comment supprimer mes données ?",
         "Supprimez l'app. Tout — brouillon, préréglages, réglages — est sur l'appareil et part avec elle. Il n'y a aucun compte à fermer ni serveur à contacter."),
    ],
)

# ─────────────────────────────────────────────────────────────── de-DE
CHROME["de-DE"] = dict(
    lingua="Deutsch", sigla="DE",
    nav_home="Start", nav_supporto="Support", nav_privacy="Datenschutz",
    salta="Zum Inhalt springen", lingua_etichetta="Sprache", altre_lingue="Weitere Sprachen",
    cta_attesa="Demnächst im App Store",
    cta_scarica="Laden im App Store",
    microcopy="Kostenlos · iPhone und iPad · iOS 18 oder neuer",
    demo_titolo="Gleich hier ausprobieren",
    demo_etichetta="Deine Nachricht",
    demo_placeholder="SCHREIB ETWAS",
    demo_esempio="SOFIA · ICH LIEBE DICH",
    demo_coppie="Farbpaar",
    demo_contrasto="Kontrast",
    demo_ok="lesbar", demo_basso="grenzwertig",
    demo_nota="Dieselben zwölf Paare und dieselbe WCAG-Berechnung, die die App auf dem Telefon durchführt.",
    sez_schermate="In der App",
    sez_domande="Häufige Fragen",
    chiusura_titolo="Halt dein Telefon hoch.",
    chip=["Kein Konto", "Keine Werbung", "Kein Tracking", "Kein Netz"],
    titolo_supporto="Support", titolo_privacy="Datenschutzerklärung",
    meta_supporto="Wie ein Schild entsteht, das in der letzten Reihe lesbar ist — und wie du einen Menschen erreichst.",
    meta_privacy="LookAt erhebt nichts: kein Konto, keine Statistik, kein Netz. Was du tippst, verlässt das Telefon nicht.",
    data_aggiornamento="Aktualisiert am 14. August 2026",
    contatto_titolo="Schreib uns",
    contatto_testo="Dieses Postfach liest ein Mensch, und er antwortet. Nenne dein iPhone- oder iPad-Modell und die iOS-Version — ein Screenshot hilft mehr als ein Absatz.",
    piede_nota="Kein Konto. Keine Werbung. Kein Tracking. Kein Netz.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Zurück zu LookAt",
)
PRIVACY["de-DE"] = [
    ("Kurz gesagt", [
        "LookAt erhebt nichts. Es gibt kein Konto, keine Werbung, keine Statistik und keinerlei Netzzugriff — was du tippst, verlässt das Telefon nicht."]),
    ("Wer wir sind", [
        "LookAt wird von SimpleBuild entwickelt. Bei allem, was diese Erklärung betrifft, schreib an <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Welche Daten wir erheben", [
        "Keine. Konkret erhebt, überträgt und speichert LookAt auf keinem Server:",
        "<ul><li>deinen Namen, deine E-Mail-Adresse oder sonstige personenbezogene Angaben;</li>"
        "<li>die Nachrichten, die du auf das Schild schreibst;</li>"
        "<li>Nutzungs- oder Diagnosedaten;</li>"
        "<li>Werbe-IDs oder Kennungen jeder anderen Art;</li>"
        "<li>deinen Standort, deine Kontakte, Fotos oder das Mikrofon.</li></ul>",
        "Die App fragt keine einzige Berechtigung ab: Es gibt kein Fenster zum Zustimmen, weil es nichts zu erteilen gibt."]),
    ("Was auf dem Gerät bleibt", [
        "Der Entwurf deiner Nachricht, die gespeicherten Voreinstellungen und deine Farb-, Schrift- und Bewegungseinstellungen bleiben auf dem Gerät, im normalen iOS-Einstellungsbereich der App. Sie verlassen ihn nicht und wir können sie nicht lesen.",
        "Löschst du die App, verschwinden sie mit ihr. Ist iCloud-Backup oder ein verschlüsseltes Computer-Backup aktiv, kann iOS sie in diese Sicherung aufnehmen: Diese Kopie liegt in deinem Apple-Account, unter deiner Kontrolle, und unterliegt Apples Bedingungen, nicht unseren."]),
    ("Kein Netz", [
        "Im Code von LookAt gibt es keine Netzwerkfunktion. Die App läuft im Flugmodus, in der Flugzeugkabine, im Kellerclub und auf einem Telefon ohne SIM. Das ist kein Versprechen über unsere Absichten, sondern eine Eigenschaft der App, die du in zehn Sekunden prüfen kannst."]),
    ("Dritte", [
        "Es gibt keine Werbebibliothek, kein Analyse-Kit und kein SDK von Dritten. LookAt zeigt nie die Tracking-Abfrage, weil es nichts zu verfolgen gibt.",
        "Den App Store betreibt Apple und erfasst als Vertriebspartner Downloads und etwaige Käufe gemäß der <a href=\"https://www.apple.com/de/legal/privacy/\" rel=\"noopener\">Datenschutzrichtlinie von Apple</a>. In App Store Connect sehen wir nur aggregierte Zahlen — etwa wie viele Downloads in einem Land — nie eine Person."]),
    ("Kinder", [
        "LookAt ist ab 4 Jahren freigegeben, enthält keine Inhalte anderer Personen, führt nirgendwohin hinaus und hat nichts zu verkaufen. Da überhaupt nichts erhoben wird, wird auch über ein Kind nichts erhoben."]),
    ("Deine Rechte", [
        "Die DSGVO gibt dir das Recht auf Auskunft, Berichtigung und Löschung deiner personenbezogenen Daten. Wir haben keine: Wir können dir nichts schicken und nichts löschen. Um die Daten auf dem Gerät zu entfernen, lösche die App.",
        "Wenn du das anders siehst, schreib uns — und du kannst dich zudem an deine zuständige Datenschutzaufsichtsbehörde wenden."]),
    ("Änderungen dieser Erklärung", [
        "Sollte die App eines Tages etwas anderes tun, ändert sich zuerst diese Seite, und mit ihr das Datum oben."]),
    ("Kontakt", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["de-DE"] = dict(
    intro="Fast alles, was an einem Telefon-Schild nicht klappt, ist eine Frage der Buchstabenhöhe und des Kontrasts — und beides ist in Sekunden behoben. Fang hier an; steht die Antwort nicht dabei, schreib uns: Es antwortet ein Mensch.",
    faq=[
        ("Braucht LookAt eine Internetverbindung?",
         "Nein, kein einziges Mal. Im Code der App gibt es keine Netzwerkfunktion: Sie läuft im Flugmodus, unter der Erde und auf einem Telefon ohne SIM. Was du tippst, verlässt das Telefon nicht."),
        ("Mein Schild ist nicht lesbar. Was soll ich ändern?",
         "Vier Dinge, in dieser Reihenfolge. <strong>Kürze die Nachricht</strong>: Die Buchstaben sind so hoch, wie der Bildschirm erlaubt — weniger Zeichen heißt größere Buchstaben. <strong>Nimm Breit</strong>, die Schrift mit den breitesten Strichen. <strong>Wähle ein Paar mit echtem Kontrast</strong>: Die App zeigt das gemessene Verhältnis und warnt unter 4,5:1. <strong>Dreh das Telefon quer</strong>, dann wird das Schild breiter. Und eine ehrliche Grenze: In direkter Sonne oder über einige Dutzend Meter hinaus verliert ein Telefonbildschirm ohnehin, egal welche Farben."),
        ("Der Bildschirm wird dunkler oder geht aus, während das Schild oben ist.",
         "Solange das Schild zu sehen ist, stellt LookAt die Helligkeit auf Maximum und verhindert, dass der Bildschirm einschläft — und stellt <em>deine</em> Helligkeit wieder her, sobald du zurückgehst. Zwei Dinge können sie trotzdem senken, und keine App kann das übergehen: der Stromsparmodus und die Drosselung, die iOS bei warmem Gerät vornimmt. Ist das Telefon heiß, lass es abkühlen, dann ist alles wie zuvor."),
        ("Wie speichere ich eine Nachricht für später?",
         "Als Voreinstellung — bis zu 24 Stück. Speicherst du unter einem bereits vergebenen Namen, wird diese Voreinstellung überschrieben, statt eine zweite mit demselben Namen anzulegen."),
        ("Läuft es auf dem iPad?",
         "Ja. LookAt ist eine App für iPhone und iPad und braucht iOS oder iPadOS 18 oder neuer. Auf dem iPad ist das Schild schlicht breiter."),
        ("Laufschrift und Blinken funktionieren nicht.",
         "Prüf Einstellungen → Bedienungshilfen → Bewegung → Bewegung reduzieren. Ist das an, stoppt LookAt bewusst Laufschrift und Blinken — sechs Blitze pro Sekunde sind genau der Reiz, den diese Einstellung dämpfen soll — und zeigt die ganze Nachricht still und vollständig sichtbar."),
        ("Ist es wirklich kostenlos?",
         "Ja: kostenlos, ohne etwas zu kaufen, ohne Werbung und ohne Konto."),
        ("Wie lösche ich meine Daten?",
         "Lösch die App. Alles — Entwurf, Voreinstellungen, Einstellungen — liegt auf dem Gerät und geht mit ihr. Es gibt kein Konto zu schließen und keinen Server, dem man schreiben müsste."),
    ],
)
