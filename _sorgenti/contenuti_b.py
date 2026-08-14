# -*- coding: utf-8 -*-
"""Testi del sito — parte 2: pt-BR, nl-NL, ja, ko, zh-Hans, zh-Hant.

Stessa regola della parte 1: qui NON si duplica il testo della scheda App Store.
"""

CHROME = {}
PRIVACY = {}
SUPPORTO = {}

# ─────────────────────────────────────────────────────────────── pt-BR
CHROME["pt-BR"] = dict(
    lingua="Português (Brasil)", sigla="PT",
    nav_home="Início", nav_supporto="Suporte", nav_privacy="Privacidade",
    salta="Ir para o conteúdo", lingua_etichetta="Idioma", altre_lingue="Outros idiomas",
    cta_attesa="Em breve na App Store",
    cta_scarica="Baixar na App Store",
    microcopy="Grátis · iPhone e iPad · iOS 18 ou posterior",
    demo_titolo="Teste aqui mesmo",
    demo_etichetta="Sua mensagem",
    demo_placeholder="ESCREVA ALGO",
    demo_esempio="SOFIA · EU TE AMO",
    demo_coppie="Par de cores",
    demo_contrasto="Contraste",
    demo_ok="dá pra ler", demo_basso="no limite",
    demo_nota="Os mesmos doze pares e o mesmo cálculo WCAG que o app faz no seu celular.",
    sez_schermate="Dentro do app",
    sez_domande="Perguntas frequentes",
    chiusura_titolo="Levante o celular.",
    chip=["Sem conta", "Sem anúncios", "Sem rastreamento", "Sem rede"],
    titolo_supporto="Suporte", titolo_privacy="Política de privacidade",
    meta_supporto="Como fazer uma plaquinha que se lê da última fileira, e como falar com uma pessoa de verdade.",
    meta_privacy="O LookAt não coleta nada: sem conta, sem estatísticas, sem rede. O que você escreve não sai do celular.",
    data_aggiornamento="Atualizada em 14 de agosto de 2026",
    contatto_titolo="Fale com a gente",
    contatto_testo="Quem lê esta caixa é uma pessoa, e ela responde. Diga o modelo do iPhone ou iPad e a versão do iOS: uma captura de tela ajuda mais que um parágrafo.",
    piede_nota="Sem conta. Sem anúncios. Sem rastreamento. Sem rede.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Voltar ao LookAt",
)
PRIVACY["pt-BR"] = [
    ("Em resumo", [
        "O LookAt não coleta nada. Não há conta, não há publicidade, não há estatísticas e não há nenhum acesso à rede: o que você escreve não sai do celular."]),
    ("Quem somos", [
        "O LookAt é desenvolvido pela SimpleBuild. Para qualquer assunto desta política, escreva para <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Dados que coletamos", [
        "Nenhum. Especificamente, o LookAt não coleta, não transmite e não guarda em servidor algum:",
        "<ul><li>seu nome, seu e-mail ou qualquer outro dado pessoal;</li>"
        "<li>as mensagens que você escreve na plaquinha;</li>"
        "<li>estatísticas de uso ou dados de diagnóstico;</li>"
        "<li>identificadores de publicidade ou de qualquer outro tipo;</li>"
        "<li>sua localização, contatos, fotos ou microfone.</li></ul>",
        "O app não pede nenhuma permissão: não existe janela para aceitar, porque não há nada a conceder."]),
    ("O que fica no seu aparelho", [
        "O rascunho da mensagem, os ajustes salvos e suas preferências de cor, tipografia e movimento ficam no aparelho, na área padrão de preferências do iOS reservada ao app. Não saem dali e nós não conseguimos lê-los.",
        "Se você apagar o app, eles vão junto. Se o backup do iCloud ou um backup criptografado no computador estiver ativo, o iOS pode incluí-los nessa cópia: essa cópia está dentro da sua conta Apple, sob seu controle, e é regida pelos termos da Apple, não pelos nossos."]),
    ("Sem rede", [
        "No código do LookAt não existe nenhuma função de rede. Ele funciona no modo avião, dentro do avião, numa casa de shows no subsolo e num celular sem chip. Não é uma promessa sobre as nossas intenções: é uma propriedade do app que você confere em dez segundos."]),
    ("Terceiros", [
        "Não há biblioteca de anúncios, ferramenta de análise nem SDK de terceiros de espécie alguma. O LookAt nunca mostra o pedido de permissão de rastreamento, porque não tem o que rastrear.",
        "A App Store é operada pela Apple que, como distribuidora, registra os downloads e eventuais compras conforme a <a href=\"https://www.apple.com/br/legal/privacy/\" rel=\"noopener\">política de privacidade da Apple</a>. No App Store Connect vemos apenas números agregados — quantos downloads em um país, por exemplo — nunca uma pessoa."]),
    ("Crianças", [
        "O LookAt é classificado como 4+, não traz conteúdo escrito por outras pessoas, não leva para fora do app e não tem nada a vender. Como nada é coletado, também nada é coletado sobre uma criança."]),
    ("Seus direitos", [
        "A LGPD garante a você acesso, correção e eliminação dos seus dados pessoais. Nós não temos nenhum: não há o que enviar e não há o que apagar. Para eliminar os dados que estão no aparelho, apague o app.",
        "Se você achar que não é assim, escreva para nós — e pode também procurar a Autoridade Nacional de Proteção de Dados."]),
    ("Alterações nesta política", [
        "Se um dia o app mudar o que faz, esta página muda antes, e a data no topo muda junto."]),
    ("Contato", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["pt-BR"] = dict(
    intro="Quase tudo que dá errado numa plaquinha feita com o celular é questão de altura de letra e de contraste, e se resolve em segundos. Comece por aqui; se a resposta não estiver, escreva: quem responde é uma pessoa.",
    faq=[
        ("O LookAt precisa de conexão com a internet?",
         "Não, nunca. No código do app não existe nenhuma função de rede: ele funciona no modo avião, no subsolo e num celular sem chip. O que você escreve não sai do aparelho."),
        ("Minha plaquinha não dá para ler. O que eu mudo?",
         "Quatro coisas, nesta ordem. <strong>Encurte a mensagem</strong>: as letras são tão altas quanto a tela permite, então menos caracteres significa letras maiores. <strong>Use a Expandida</strong>, a tipografia de traços mais largos. <strong>Escolha um par com contraste de verdade</strong>: o app mostra a razão medida e avisa abaixo de 4,5:1. <strong>Vire o celular</strong> para uma plaquinha mais larga. E um limite honesto: sob sol forte, ou a mais de algumas dezenas de metros, a tela de um celular perde de qualquer jeito, seja qual for a cor."),
        ("A tela escurece, ou apaga, com a plaquinha levantada.",
         "Enquanto a plaquinha está na tela, o LookAt leva o brilho ao máximo e impede que a tela durma, e devolve o <em>seu</em> brilho assim que você sai. Duas coisas ainda podem abaixá-lo, e nenhum app consegue impedir: o modo de baixo consumo e a redução que o iOS aplica quando o aparelho esquenta. Se estiver quente, deixe esfriar e tudo volta."),
        ("Como salvo uma mensagem para reutilizar?",
         "Salve como ajuste predefinido: cabem até 24. Salvar com um nome já usado sobrescreve aquele ajuste, em vez de criar um segundo com o mesmo nome."),
        ("Funciona no iPad?",
         "Sim. O LookAt é um app só para iPhone e iPad, e pede iOS ou iPadOS 18 ou posterior. No iPad a plaquinha fica simplesmente mais larga."),
        ("A rolagem e o piscar não funcionam.",
         "Confira Ajustes → Acessibilidade → Movimento → Reduzir Movimento. Com isso ligado, o LookAt para de propósito tanto a rolagem quanto o piscar — um flash seis vezes por segundo é exatamente o estímulo que esse ajuste existe para amortecer — e mostra a mensagem inteira, parada e totalmente visível."),
        ("É grátis mesmo?",
         "Sim: grátis, sem nada para comprar dentro, sem anúncios e sem conta."),
        ("Como apago meus dados?",
         "Apague o app. Tudo — rascunho, ajustes salvos, preferências — está no aparelho e vai junto. Não há conta para encerrar nem servidor para escrever."),
    ],
)

# ─────────────────────────────────────────────────────────────── nl-NL
CHROME["nl-NL"] = dict(
    lingua="Nederlands", sigla="NL",
    nav_home="Home", nav_supporto="Support", nav_privacy="Privacy",
    salta="Naar de inhoud", lingua_etichetta="Taal", altre_lingue="Andere talen",
    cta_attesa="Binnenkort in de App Store",
    cta_scarica="Download in de App Store",
    microcopy="Gratis · iPhone en iPad · iOS 18 of nieuwer",
    demo_titolo="Probeer het hier",
    demo_etichetta="Jouw bericht",
    demo_placeholder="TYP IETS",
    demo_esempio="SOFIA · IK HOU VAN JOU",
    demo_coppie="Kleurenduo",
    demo_contrasto="Contrast",
    demo_ok="leesbaar", demo_basso="op de grens",
    demo_nota="Dezelfde twaalf duo's en dezelfde WCAG-berekening die de app op je telefoon uitvoert.",
    sez_schermate="In de app",
    sez_domande="Veelgestelde vragen",
    chiusura_titolo="Houd je telefoon omhoog.",
    chip=["Geen account", "Geen advertenties", "Geen tracking", "Geen netwerk"],
    titolo_supporto="Support", titolo_privacy="Privacybeleid",
    meta_supporto="Hoe je een bord maakt dat op de laatste rij leesbaar is, en hoe je een mens bereikt.",
    meta_privacy="LookAt verzamelt niets: geen account, geen statistieken, geen netwerk. Wat je typt verlaat je telefoon niet.",
    data_aggiornamento="Bijgewerkt op 14 augustus 2026",
    contatto_titolo="Schrijf ons",
    contatto_testo="Deze mailbox wordt door een mens gelezen, en beantwoord. Noem je iPhone- of iPad-model en je iOS-versie: een schermafbeelding helpt meer dan een alinea.",
    piede_nota="Geen account. Geen advertenties. Geen tracking. Geen netwerk.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="Terug naar LookAt",
)
PRIVACY["nl-NL"] = [
    ("Kort gezegd", [
        "LookAt verzamelt niets. Er is geen account, geen advertentie, geen statistiek en helemaal geen netwerktoegang: wat je typt verlaat je telefoon niet."]),
    ("Wie we zijn", [
        "LookAt wordt gemaakt door SimpleBuild. Voor alles wat dit beleid betreft: <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>."]),
    ("Gegevens die we verzamelen", [
        "Geen. Concreet verzamelt, verstuurt en bewaart LookAt op geen enkele server:",
        "<ul><li>je naam, je e-mailadres of enig ander persoonsgegeven;</li>"
        "<li>de berichten die je op het bord schrijft;</li>"
        "<li>gebruiks- of diagnosegegevens;</li>"
        "<li>advertentie-ID's of identificatoren van welke aard dan ook;</li>"
        "<li>je locatie, contacten, foto's of microfoon.</li></ul>",
        "De app vraagt geen enkele toestemming: er is geen venster om te accepteren, want er valt niets te verlenen."]),
    ("Wat op je apparaat blijft", [
        "Het concept van je bericht, je bewaarde presets en je instellingen voor kleur, lettertype en beweging blijven op het apparaat, in het standaard iOS-voorkeurengebied van de app. Ze gaan daar niet weg en wij kunnen ze niet lezen.",
        "Verwijder je de app, dan verdwijnen ze mee. Staat iCloud-reservekopie of een versleutelde computerreservekopie aan, dan kan iOS ze daarin opnemen: die kopie staat in jouw Apple-account, onder jouw controle, en valt onder de voorwaarden van Apple, niet onder de onze."]),
    ("Geen netwerk", [
        "In de code van LookAt zit geen enkele netwerkfunctie. De app werkt in vliegtuigmodus, in de cabine, in een kelderzaal en op een telefoon zonder simkaart. Dat is geen belofte over onze bedoelingen: het is een eigenschap van de app die je in tien seconden controleert."]),
    ("Derden", [
        "Er is geen advertentiebibliotheek, geen analysepakket en geen SDK van derden, in welke vorm dan ook. LookAt toont nooit het verzoek om toestemming voor tracking, want er valt niets te volgen.",
        "De App Store wordt beheerd door Apple, dat als distributeur downloads en eventuele aankopen registreert volgens het <a href=\"https://www.apple.com/nl/legal/privacy/\" rel=\"noopener\">privacybeleid van Apple</a>. In App Store Connect zien wij alleen geaggregeerde cijfers — hoeveel downloads in een land, bijvoorbeeld — nooit een persoon."]),
    ("Kinderen", [
        "LookAt heeft leeftijdsclassificatie 4+, bevat geen door anderen geschreven inhoud, leidt nergens naartoe en heeft niets te verkopen. Omdat er niets wordt verzameld, wordt er ook over een kind niets verzameld."]),
    ("Jouw rechten", [
        "De AVG geeft je recht op inzage, correctie en verwijdering van je persoonsgegevens. Wij hebben er geen: er is niets om je toe te sturen en niets om te wissen. Wil je de gegevens op het apparaat weg, verwijder dan de app.",
        "Denk je dat het anders zit, schrijf ons — en je kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens."]),
    ("Wijzigingen in dit beleid", [
        "Verandert de app ooit wat ze doet, dan verandert deze pagina eerst, en de datum bovenaan verandert mee."]),
    ("Contact", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["nl-NL"] = dict(
    intro="Bijna alles wat misgaat met een bord van een telefoon is een kwestie van letterhoogte en contrast, en dat is in seconden opgelost. Begin hier; staat het antwoord er niet bij, schrijf ons: er antwoordt een mens.",
    faq=[
        ("Heeft LookAt internet nodig?",
         "Nee, geen enkele keer. In de code van de app zit geen netwerkfunctie: ze werkt in vliegtuigmodus, ondergronds en op een telefoon zonder simkaart. Wat je typt verlaat je telefoon niet."),
        ("Mijn bord is onleesbaar. Wat moet ik veranderen?",
         "Vier dingen, in deze volgorde. <strong>Maak het bericht korter</strong>: de letters zijn zo hoog als het scherm toelaat, dus minder tekens betekent grotere letters. <strong>Gebruik Breed</strong>, het lettertype met de breedste stokken. <strong>Kies een duo met écht contrast</strong>: de app toont de gemeten verhouding en waarschuwt onder 4,5:1. <strong>Draai de telefoon</strong> voor een breder bord. En een eerlijke grens: in direct zonlicht, of verder dan enkele tientallen meters, verliest een telefoonscherm hoe dan ook, welke kleuren je ook kiest."),
        ("Het scherm dimt, of gaat uit, terwijl het bord omhoog is.",
         "Zolang het bord in beeld is zet LookAt de helderheid op maximaal en houdt het scherm wakker, en zet <em>jouw</em> helderheid terug zodra je stopt. Twee dingen kunnen het toch dimmen en geen enkele app kan dat overrulen: de energiebesparingsmodus en de verlaging die iOS toepast als de telefoon warm wordt. Is hij warm, laat hem afkoelen en het komt terug."),
        ("Hoe bewaar ik een bericht om het opnieuw te gebruiken?",
         "Bewaar het als preset: er passen er 24. Bewaren onder een naam die al bestaat overschrijft die preset, in plaats van een tweede met dezelfde naam te maken."),
        ("Werkt het op de iPad?",
         "Ja. LookAt is één app voor iPhone en iPad, en vraagt iOS of iPadOS 18 of nieuwer. Op de iPad is het bord simpelweg breder."),
        ("Schuiven en knipperen werken niet.",
         "Kijk bij Instellingen → Toegankelijkheid → Beweging → Verminder beweging. Staat dat aan, dan stopt LookAt bewust zowel het schuiven als het knipperen — zes flitsen per seconde is precies de prikkel die deze instelling moet dempen — en toont het hele bericht, stil en volledig zichtbaar."),
        ("Is het echt gratis?",
         "Ja: gratis, zonder iets te kopen, zonder advertenties en zonder account."),
        ("Hoe verwijder ik mijn gegevens?",
         "Verwijder de app. Alles — concept, presets, instellingen — staat op het apparaat en gaat mee. Er is geen account om op te zeggen en geen server om te mailen."),
    ],
)

# ────────────────────────────────────────────────────────────────── ja
CHROME["ja"] = dict(
    lingua="日本語", sigla="日本語",
    nav_home="ホーム", nav_supporto="サポート", nav_privacy="プライバシー",
    salta="本文へ移動", lingua_etichetta="言語", altre_lingue="ほかの言語",
    cta_attesa="App Storeで近日公開",
    cta_scarica="App Storeでダウンロード",
    microcopy="無料 · iPhoneとiPad · iOS 18以降",
    demo_titolo="ここで試せます",
    demo_etichetta="あなたのメッセージ",
    demo_placeholder="ここに入力",
    demo_esempio="ソフィア · あの曲を！",
    demo_coppie="配色",
    demo_contrasto="コントラスト",
    demo_ok="読める", demo_basso="ぎりぎり",
    demo_nota="アプリが端末で計算しているのと同じ12組の配色、同じWCAGの計算式です。",
    sez_schermate="アプリの中身",
    sez_domande="よくある質問",
    chiusura_titolo="スマホを掲げよう。",
    chip=["アカウント不要", "広告なし", "トラッキングなし", "通信なし"],
    titolo_supporto="サポート", titolo_privacy="プライバシーポリシー",
    meta_supporto="後ろの席からでも読める看板の作り方と、人に直接連絡する方法。",
    meta_privacy="LookAtは何も集めません。アカウントなし、統計なし、通信なし。入力した内容は端末から出ません。",
    data_aggiornamento="2026年8月14日 更新",
    contatto_titolo="お問い合わせ",
    contatto_testo="このメールは人が読んで、人が返信します。iPhoneまたはiPadの機種とiOSのバージョンを書いてください。スクリーンショットは長い説明より役に立ちます。",
    piede_nota="アカウント不要。広告なし。トラッキングなし。通信なし。",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="LookAtに戻る",
)
PRIVACY["ja"] = [
    ("要点", [
        "LookAtは何も収集しません。アカウントも、広告も、統計もなく、ネットワークへの接続も一切ありません。入力した内容が端末から出ることはありません。"]),
    ("運営者", [
        "LookAtはSimpleBuildが開発しています。このポリシーに関するお問い合わせは <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a> までどうぞ。"]),
    ("収集するデータ", [
        "ありません。具体的に、LookAtは以下をいっさい収集せず、送信せず、どのサーバーにも保存しません。",
        "<ul><li>氏名、メールアドレスその他の個人情報</li>"
        "<li>看板に入力したメッセージ</li>"
        "<li>利用統計や診断情報</li>"
        "<li>広告識別子その他あらゆる識別子</li>"
        "<li>位置情報、連絡先、写真、マイク</li></ul>",
        "アプリは許可をひとつも求めません。承認するダイアログが出ないのは、与えるものが何もないからです。"]),
    ("端末に残るもの", [
        "入力中のメッセージ、保存したプリセット、色・書体・動きの設定は端末に残ります。保存先はアプリ専用のiOS標準の設定領域で、そこから出ることはなく、私たちが読むこともできません。",
        "アプリを削除すれば一緒に消えます。iCloudバックアップや暗号化されたコンピュータのバックアップを有効にしている場合、iOSがそれらをバックアップに含めることがあります。その控えはあなたのApple アカウントの中にあり、あなたの管理下にあり、私たちではなくAppleの条件に従います。"]),
    ("通信をしません", [
        "LookAtのコードにはネットワーク機能そのものがありません。機内モードでも、飛行機の中でも、地下のライブハウスでも、SIMのない端末でも動きます。これは意思の表明ではなく、10秒で確かめられるアプリの性質です。"]),
    ("第三者", [
        "広告ライブラリも、解析ツールも、第三者のSDKもありません。追跡の許可を求める画面が出ないのは、追跡するものがないからです。",
        "App StoreはAppleが運営しており、配信者としてダウンロードや購入を <a href=\"https://www.apple.com/jp/legal/privacy/\" rel=\"noopener\">Appleのプライバシーポリシー</a> に従って記録します。App Store Connectで私たちが見られるのは集計された数値だけです（たとえば、ある国での総ダウンロード数）。個人が分かることはありません。"]),
    ("お子さまについて", [
        "LookAtの年齢制限は4+です。他人が書いた内容も、外部へのリンクも、購入するものもありません。そもそも何も収集していないので、お子さまについても何も収集していません。"]),
    ("あなたの権利", [
        "個人データについては、開示・訂正・削除を求める権利があります。私たちは個人データを一切保有していないため、お送りするものも、削除するものもありません。端末上のデータを消すには、アプリを削除してください。"]),
    ("このポリシーの変更", [
        "将来アプリの動作が変わる場合は、まずこのページを更新し、上部の日付も同時に変えます。"]),
    ("連絡先", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["ja"] = dict(
    intro="スマホの看板がうまくいかない原因は、ほとんどが文字の高さとコントラストで、どちらも数秒で直せます。まずはここから。答えが見つからなければ書いてください。人が返信します。",
    faq=[
        ("LookAtにインターネット接続は必要ですか。",
         "いいえ、一度も必要ありません。アプリのコードにはネットワーク機能がないので、機内モードでも、地下でも、SIMのない端末でも動きます。入力した内容が端末から出ることはありません。"),
        ("看板が読めません。何を変えればいいですか。",
         "次の順に4つです。<strong>メッセージを短く</strong>——文字は画面が許すかぎり大きくなるので、文字数が少ないほど大きくなります。<strong>エクスパンデッドを使う</strong>——線がいちばん太い書体です。<strong>本当に差のある配色を選ぶ</strong>——アプリが実測のコントラスト比を表示し、4.5:1を下回ると警告します。<strong>横向きにする</strong>と看板が広くなります。そして正直な限界がひとつ。直射日光の下や数十メートルを超える距離では、どんな配色でもスマホの画面は負けます。"),
        ("看板を出している間に画面が暗くなる、または消える。",
         "看板を表示している間、LookAtは輝度を最大にして画面が消えないようにし、終了すると<em>あなたの</em>輝度に戻します。それでも輝度が下がる原因が2つあり、どのアプリにも止められません。低電力モードと、本体が熱くなったときにiOSが行う輝度制限です。熱いときは冷ませば元に戻ります。"),
        ("メッセージを保存して使い回すには。",
         "プリセットとして保存します。24件まで保存でき、すでにある名前で保存すると、同じ名前がもう1件増えるのではなく、そのプリセットが上書きされます。"),
        ("iPadでも使えますか。",
         "はい。LookAtはiPhoneとiPadで同じ1本のアプリで、iOSまたはiPadOS 18以降が必要です。iPadでは看板がそのぶん広くなります。"),
        ("スクロールと点滅が動きません。",
         "「設定」→「アクセシビリティ」→「動作」→「視差効果を減らす」を確認してください。これがオンのとき、LookAtはスクロールと点滅を意図的に止めます。毎秒6回の点滅は、まさにこの設定が抑えるためにある刺激だからです。メッセージは静止した状態で、全文が表示されます。"),
        ("本当に無料ですか。",
         "はい。無料で、アプリ内に買うものはなく、広告もアカウントもありません。"),
        ("データを消すには。",
         "アプリを削除してください。下書きもプリセットも設定も端末の中にあり、アプリと一緒に消えます。解約するアカウントも、連絡すべきサーバーもありません。"),
    ],
)

# ────────────────────────────────────────────────────────────────── ko
CHROME["ko"] = dict(
    lingua="한국어", sigla="한국어",
    nav_home="홈", nav_supporto="지원", nav_privacy="개인정보",
    salta="본문으로 건너뛰기", lingua_etichetta="언어", altre_lingue="다른 언어",
    cta_attesa="App Store에 곧 출시",
    cta_scarica="App Store에서 다운로드",
    microcopy="무료 · iPhone과 iPad · iOS 18 이상",
    demo_titolo="여기서 바로 해보세요",
    demo_etichetta="당신의 메시지",
    demo_placeholder="여기에 입력",
    demo_esempio="소피아 · 그 노래 해줘요!",
    demo_coppie="색 조합",
    demo_contrasto="대비",
    demo_ok="읽힘", demo_basso="아슬아슬",
    demo_nota="앱이 기기에서 계산하는 것과 똑같은 12가지 조합, 똑같은 WCAG 계산식입니다.",
    sez_schermate="앱 속으로",
    sez_domande="자주 묻는 질문",
    chiusura_titolo="휴대폰을 들어 올리세요.",
    chip=["계정 없음", "광고 없음", "추적 없음", "네트워크 없음"],
    titolo_supporto="지원", titolo_privacy="개인정보 처리방침",
    meta_supporto="맨 뒷줄에서도 읽히는 표지판 만드는 법, 그리고 사람에게 직접 연락하는 법.",
    meta_privacy="LookAt은 아무것도 수집하지 않습니다. 계정도, 통계도, 네트워크도 없습니다. 입력한 내용은 휴대폰을 벗어나지 않습니다.",
    data_aggiornamento="2026년 8월 14일 갱신",
    contatto_titolo="문의하기",
    contatto_testo="이 메일함은 사람이 읽고 사람이 답합니다. iPhone 또는 iPad 모델과 iOS 버전을 알려 주세요. 스크린샷 한 장이 긴 설명보다 낫습니다.",
    piede_nota="계정 없음. 광고 없음. 추적 없음. 네트워크 없음.",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="LookAt으로 돌아가기",
)
PRIVACY["ko"] = [
    ("요약", [
        "LookAt은 아무것도 수집하지 않습니다. 계정도, 광고도, 통계도 없고 네트워크 접속 자체가 없습니다. 입력한 내용은 휴대폰을 벗어나지 않습니다."]),
    ("만든 곳", [
        "LookAt은 SimpleBuild가 개발합니다. 이 방침에 관한 문의는 <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a> 으로 보내 주세요."]),
    ("수집하는 데이터", [
        "없습니다. 구체적으로 LookAt은 다음을 수집하지 않고, 전송하지 않으며, 어떤 서버에도 저장하지 않습니다.",
        "<ul><li>이름, 이메일 주소를 비롯한 모든 개인정보</li>"
        "<li>표지판에 입력한 메시지</li>"
        "<li>사용 통계나 진단 정보</li>"
        "<li>광고 식별자를 비롯한 모든 식별자</li>"
        "<li>위치, 연락처, 사진, 마이크</li></ul>",
        "앱은 어떤 권한도 요청하지 않습니다. 수락할 창이 뜨지 않는 이유는 허용할 것이 없기 때문입니다."]),
    ("기기에 남는 것", [
        "작성 중인 메시지, 저장한 프리셋, 색·서체·움직임 설정은 기기에 남습니다. 저장 위치는 앱 전용의 iOS 표준 설정 영역이며, 그곳을 벗어나지 않고 저희가 읽을 수도 없습니다.",
        "앱을 삭제하면 함께 사라집니다. iCloud 백업이나 암호화된 컴퓨터 백업을 켜 두었다면 iOS가 이를 백업에 포함할 수 있습니다. 그 사본은 당신의 Apple 계정 안에 있고, 당신의 통제 아래 있으며, 저희가 아니라 Apple의 약관을 따릅니다."]),
    ("네트워크를 쓰지 않습니다", [
        "LookAt의 코드에는 네트워크 기능 자체가 없습니다. 비행기 모드에서도, 기내에서도, 지하 공연장에서도, 유심 없는 기기에서도 작동합니다. 이는 의도에 대한 약속이 아니라 10초면 확인할 수 있는 앱의 성질입니다."]),
    ("제3자", [
        "광고 라이브러리도, 분석 도구도, 제3자 SDK도 없습니다. 추적 권한 요청 화면이 뜨지 않는 이유는 추적할 것이 없기 때문입니다.",
        "App Store는 Apple이 운영하며, 배포자로서 다운로드와 구매를 <a href=\"https://www.apple.com/kr/legal/privacy/\" rel=\"noopener\">Apple 개인정보 처리방침</a>에 따라 기록합니다. App Store Connect에서 저희가 보는 것은 집계된 숫자뿐이며(예: 어떤 국가의 총 다운로드 수), 개인은 알 수 없습니다."]),
    ("어린이", [
        "LookAt의 연령 등급은 4+이며, 다른 사람이 쓴 내용도, 외부로 나가는 링크도, 구매할 것도 없습니다. 애초에 아무것도 수집하지 않으므로 어린이에 관해서도 아무것도 수집하지 않습니다."]),
    ("이용자의 권리", [
        "개인정보에 대해 열람·정정·삭제를 요구할 권리가 있습니다. 저희는 개인정보를 전혀 보유하지 않으므로 보내 드릴 것도, 삭제할 것도 없습니다. 기기에 있는 데이터를 지우려면 앱을 삭제하세요."]),
    ("방침의 변경", [
        "앱이 하는 일이 달라지면 이 페이지가 먼저 바뀌고, 상단의 날짜도 함께 바뀝니다."]),
    ("연락처", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["ko"] = dict(
    intro="휴대폰 표지판에서 잘 안 되는 일은 거의 글자 높이와 대비 문제이고, 둘 다 몇 초면 고칩니다. 여기서 시작하세요. 답이 없으면 메일을 주세요. 사람이 답합니다.",
    faq=[
        ("LookAt에 인터넷 연결이 필요한가요?",
         "아니요, 한 번도 필요하지 않습니다. 앱 코드에는 네트워크 기능이 없어서 비행기 모드에서도, 지하에서도, 유심 없는 기기에서도 작동합니다. 입력한 내용은 휴대폰을 벗어나지 않습니다."),
        ("표지판이 안 읽혀요. 무엇을 바꿔야 하나요?",
         "이 순서로 네 가지입니다. <strong>메시지를 줄이세요</strong> — 글자는 화면이 허용하는 만큼 커지므로 글자 수가 적을수록 커집니다. <strong>확장 서체를 쓰세요</strong> — 획이 가장 굵습니다. <strong>실제로 대비가 큰 조합을 고르세요</strong> — 앱이 측정된 대비율을 보여 주고 4.5:1 아래에서는 경고합니다. <strong>가로로 돌리면</strong> 표지판이 넓어집니다. 그리고 정직한 한계 하나. 직사광선 아래나 수십 미터를 넘는 거리에서는 어떤 색을 골라도 휴대폰 화면이 집니다."),
        ("표지판을 들고 있는 동안 화면이 어두워지거나 꺼집니다.",
         "표지판이 떠 있는 동안 LookAt은 밝기를 최대로 올리고 화면이 꺼지지 않게 하며, 나가면 <em>원래</em> 밝기로 되돌립니다. 그래도 밝기를 낮추는 두 가지가 있고 어떤 앱도 막을 수 없습니다. 저전력 모드, 그리고 기기가 뜨거워질 때 iOS가 적용하는 밝기 제한입니다. 뜨겁다면 식힌 뒤 원래대로 돌아옵니다."),
        ("메시지를 저장해 다시 쓰려면?",
         "프리셋으로 저장하세요. 최대 24개까지 저장되며, 이미 있는 이름으로 저장하면 같은 이름이 하나 더 생기는 대신 그 프리셋이 덮어써집니다."),
        ("iPad에서도 되나요?",
         "네. LookAt은 iPhone과 iPad를 위한 하나의 앱이고 iOS 또는 iPadOS 18 이상이 필요합니다. iPad에서는 표지판이 그만큼 넓어집니다."),
        ("스크롤과 깜박임이 작동하지 않습니다.",
         "설정 → 손쉬운 사용 → 동작 → 동작 줄이기를 확인하세요. 이 설정이 켜져 있으면 LookAt은 스크롤과 깜박임을 의도적으로 멈춥니다. 초당 여섯 번의 번쩍임이야말로 그 설정이 줄이려는 자극이기 때문입니다. 메시지는 멈춘 상태로 전부 보입니다."),
        ("정말 무료인가요?",
         "네. 무료이고, 앱 안에서 살 것도, 광고도, 계정도 없습니다."),
        ("데이터를 어떻게 지우나요?",
         "앱을 삭제하세요. 초안도 프리셋도 설정도 모두 기기 안에 있고 앱과 함께 사라집니다. 해지할 계정도, 연락할 서버도 없습니다."),
    ],
)

# ────────────────────────────────────────────────────────────── zh-Hans
CHROME["zh-Hans"] = dict(
    lingua="简体中文", sigla="简体",
    nav_home="首页", nav_supporto="支持", nav_privacy="隐私",
    salta="跳到正文", lingua_etichetta="语言", altre_lingue="其他语言",
    cta_attesa="即将登陆 App Store",
    cta_scarica="在 App Store 下载",
    microcopy="免费 · iPhone 和 iPad · iOS 18 或更高版本",
    demo_titolo="就在这里试试",
    demo_etichetta="你的信息",
    demo_placeholder="在这里输入",
    demo_esempio="索菲亚 · 点一首歌！",
    demo_coppie="配色",
    demo_contrasto="对比度",
    demo_ok="看得清", demo_basso="临界",
    demo_nota="和 App 在手机上用的是同样的十二组配色、同样的 WCAG 算法。",
    sez_schermate="App 里面",
    sez_domande="常见问题",
    chiusura_titolo="把手机举起来。",
    chip=["无需账号", "没有广告", "不做追踪", "不联网"],
    titolo_supporto="支持", titolo_privacy="隐私政策",
    meta_supporto="怎样做出最后一排也读得出的牌子，以及怎样直接联系到人。",
    meta_privacy="LookAt 什么都不收集：没有账号，没有统计，不联网。你输入的内容不会离开手机。",
    data_aggiornamento="更新于 2026 年 8 月 14 日",
    contatto_titolo="联系我们",
    contatto_testo="这个邮箱由一个人阅读，也由这个人回复。请写明 iPhone 或 iPad 的型号和 iOS 版本：一张截图比一段描述有用得多。",
    piede_nota="无需账号。没有广告。不做追踪。不联网。",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="返回 LookAt",
)
PRIVACY["zh-Hans"] = [
    ("一句话版本", [
        "LookAt 什么都不收集。没有账号，没有广告，没有统计，也完全不访问网络：你输入的内容不会离开手机。"]),
    ("我们是谁", [
        "LookAt 由 SimpleBuild 开发。与本政策有关的任何问题，请写信到 <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>。"]),
    ("我们收集的数据", [
        "没有。具体来说，LookAt 不收集、不传输，也不在任何服务器上保存：",
        "<ul><li>你的姓名、电子邮件地址或任何其他个人信息；</li>"
        "<li>你写在牌子上的信息；</li>"
        "<li>使用统计或诊断数据；</li>"
        "<li>广告标识符或任何其他标识符；</li>"
        "<li>你的位置、通讯录、照片或麦克风。</li></ul>",
        "App 不申请任何权限：没有需要你同意的弹窗，因为根本没有可授予的东西。"]),
    ("留在设备上的内容", [
        "草稿信息、保存的预设，以及颜色、字体和动态设置都留在设备上，存放在这个 App 专属的 iOS 标准偏好设置区域。它们不会离开那里，我们也读不到。",
        "删除 App，它们随之消失。如果你开启了 iCloud 备份或电脑上的加密备份，iOS 可能把它们纳入那份备份：那份副本在你的 Apple 账户里，由你掌控，遵循 Apple 的条款，而不是我们的。"]),
    ("不联网", [
        "LookAt 的代码里根本没有联网功能。它在飞行模式下、在机舱里、在地下的演出场地、在没有 SIM 卡的手机上都能用。这不是关于意图的承诺，而是这个 App 的属性，你十秒就能验证。"]),
    ("第三方", [
        "没有广告库，没有统计工具，也没有任何第三方 SDK。LookAt 从不弹出追踪授权请求，因为它没有可追踪的东西。",
        "App Store 由 Apple 运营，作为分发方，Apple 会按照 <a href=\"https://www.apple.com.cn/legal/privacy/\" rel=\"noopener\">Apple 隐私政策</a> 记录下载和购买。在 App Store Connect 里我们只能看到汇总数字——例如某个国家有多少次下载——看不到任何个人。"]),
    ("儿童", [
        "LookAt 的年龄分级为 4+，没有他人撰写的内容，不会跳出到外部，也没有任何可购买的东西。既然什么都不收集，关于儿童自然也什么都不收集。"]),
    ("你的权利", [
        "关于个人信息，你有权查阅、更正和删除。我们一条也没有：没有什么可以发给你，也没有什么可以删除。要清除设备上的数据，删除 App 即可。"]),
    ("本政策的变更", [
        "如果有一天 App 做的事情变了，这个页面会先变，顶部的日期也会跟着变。"]),
    ("联系方式", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["zh-Hans"] = dict(
    intro="用手机做牌子，出问题的地方几乎都是字高和对比度，两者都能在几秒内解决。先看这里；如果没有答案，就写信来，回信的是一个人。",
    faq=[
        ("LookAt 需要联网吗？",
         "不需要，一次也不需要。App 的代码里没有任何联网功能：飞行模式下、地下、没有 SIM 卡的手机上都能用。你输入的内容不会离开手机。"),
        ("我的牌子看不清，该改什么？",
         "四件事，按这个顺序。<strong>把信息写短</strong>——字高取决于屏幕能给的空间，字数越少字越大。<strong>用加宽</strong>——笔画最粗的字体。<strong>选一组真有对比度的配色</strong>——App 会显示实测的对比度，低于 4.5:1 时提醒你。<strong>把手机横过来</strong>，牌子会更宽。还有一个诚实的限度：在直射阳光下，或者超过几十米的距离，再好的配色也赢不了。"),
        ("举着牌子的时候屏幕变暗，或者熄灭。",
         "牌子显示期间，LookAt 会把亮度调到最高并阻止屏幕休眠，退出时立刻把<em>你原本的</em>亮度还回去。仍有两件事会压低亮度，而且任何 App 都无法覆盖：低电量模式，以及手机发烫时 iOS 主动降低亮度。如果发烫，等它凉下来就会恢复。"),
        ("怎么保存一条信息以便重复使用？",
         "存成预设，最多 24 个。用已有的名字保存会覆盖那个预设，而不是再建一个同名的。"),
        ("iPad 能用吗？",
         "能。LookAt 是 iPhone 和 iPad 共用的一个 App，需要 iOS 或 iPadOS 18 或更高版本。在 iPad 上牌子只是更宽。"),
        ("滚动和闪烁不起作用。",
         "看一下「设置」→「辅助功能」→「动态效果」→「减弱动态效果」。开启时，LookAt 会有意停止滚动和闪烁——每秒六次的闪光正是这个设置要减弱的刺激——并把整条信息静止地完整显示出来。"),
        ("真的免费吗？",
         "是的：免费，里面没有任何要买的东西，没有广告，也不需要账号。"),
        ("怎么删除我的数据？",
         "删除 App。草稿、预设、设置全都在设备上，会跟着一起消失。没有账号要注销，也没有服务器需要联系。"),
    ],
)

# ────────────────────────────────────────────────────────────── zh-Hant
CHROME["zh-Hant"] = dict(
    lingua="繁體中文", sigla="繁體",
    nav_home="首頁", nav_supporto="支援", nav_privacy="隱私權",
    salta="跳至內容", lingua_etichetta="語言", altre_lingue="其他語言",
    cta_attesa="即將在 App Store 推出",
    cta_scarica="在 App Store 下載",
    microcopy="免費 · iPhone 和 iPad · iOS 18 或以上",
    demo_titolo="就在這裡試試",
    demo_etichetta="你的訊息",
    demo_placeholder="在這裡輸入",
    demo_esempio="蘇菲亞 · 點一首歌！",
    demo_coppie="配色",
    demo_contrasto="對比度",
    demo_ok="看得清", demo_basso="臨界",
    demo_nota="和 App 在手機上使用的是同樣的十二組配色、同樣的 WCAG 演算法。",
    sez_schermate="App 裡面",
    sez_domande="常見問題",
    chiusura_titolo="把手機舉起來。",
    chip=["免註冊", "沒有廣告", "不做追蹤", "不連網"],
    titolo_supporto="支援", titolo_privacy="隱私權政策",
    meta_supporto="怎樣做出最後一排也讀得到的看板，以及怎樣直接聯絡到人。",
    meta_privacy="LookAt 什麼都不收集：沒有帳號，沒有統計，不連網。你輸入的內容不會離開手機。",
    data_aggiornamento="更新於 2026 年 8 月 14 日",
    contatto_titolo="聯絡我們",
    contatto_testo="這個信箱由一個人閱讀，也由這個人回覆。請寫明 iPhone 或 iPad 的型號和 iOS 版本：一張截圖比一段敘述有用得多。",
    piede_nota="免註冊。沒有廣告。不做追蹤。不連網。",
    diritti="© 2026 SimpleBuild · LookAt",
    torna="返回 LookAt",
)
PRIVACY["zh-Hant"] = [
    ("一句話版本", [
        "LookAt 什麼都不收集。沒有帳號，沒有廣告，沒有統計，也完全不存取網路：你輸入的內容不會離開手機。"]),
    ("我們是誰", [
        "LookAt 由 SimpleBuild 開發。與本政策有關的任何問題，請寫信到 <a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>。"]),
    ("我們收集的資料", [
        "沒有。具體來說，LookAt 不收集、不傳輸，也不在任何伺服器上保存：",
        "<ul><li>你的姓名、電子郵件地址或任何其他個人資料；</li>"
        "<li>你寫在看板上的訊息；</li>"
        "<li>使用統計或診斷資料；</li>"
        "<li>廣告識別碼或任何其他識別碼；</li>"
        "<li>你的位置、通訊錄、照片或麥克風。</li></ul>",
        "App 不要求任何權限：沒有需要你同意的視窗，因為根本沒有可授予的東西。"]),
    ("留在裝置上的內容", [
        "草稿訊息、儲存的預設組合，以及顏色、字體和動態設定都留在裝置上，存放在這個 App 專屬的 iOS 標準偏好設定區域。它們不會離開那裡，我們也讀不到。",
        "刪除 App，它們就一起消失。如果你開啟了 iCloud 備份或電腦上的加密備份，iOS 可能把它們納入那份備份：那份副本在你的 Apple 帳戶裡，由你掌控，依循 Apple 的條款，而不是我們的。"]),
    ("不連網", [
        "LookAt 的程式碼裡根本沒有連網功能。它在飛航模式下、在機艙裡、在地下的表演場地、在沒有 SIM 卡的手機上都能用。這不是關於意圖的承諾，而是這個 App 的性質，你十秒就能驗證。"]),
    ("第三方", [
        "沒有廣告函式庫，沒有統計工具，也沒有任何第三方 SDK。LookAt 從不跳出追蹤授權要求，因為它沒有可追蹤的東西。",
        "App Store 由 Apple 營運，作為經銷方，Apple 會依照 <a href=\"https://www.apple.com/tw/legal/privacy/\" rel=\"noopener\">Apple 隱私權政策</a> 記錄下載與購買。在 App Store Connect 裡我們只看得到彙總數字——例如某個地區有多少次下載——看不到任何個人。"]),
    ("兒童", [
        "LookAt 的年齡分級為 4+，沒有他人撰寫的內容，不會跳到外部，也沒有任何可購買的東西。既然什麼都不收集，關於兒童自然也什麼都不收集。"]),
    ("你的權利", [
        "關於個人資料，你有權查閱、更正與刪除。我們一筆也沒有：沒有什麼可以寄給你，也沒有什麼可以刪除。要清除裝置上的資料，刪除 App 即可。"]),
    ("本政策的變更", [
        "如果有一天 App 做的事情改變了，這個頁面會先改，頂部的日期也會跟著改。"]),
    ("聯絡方式", [
        "<a href=\"mailto:support@simplebuild.it\">support@simplebuild.it</a>"]),
]
SUPPORTO["zh-Hant"] = dict(
    intro="用手機做看板，出問題的地方幾乎都是字高和對比度，兩者都能在幾秒內解決。先看這裡；如果沒有答案，就寫信來，回信的是一個人。",
    faq=[
        ("LookAt 需要連上網路嗎？",
         "不需要，一次也不需要。App 的程式碼裡沒有任何連網功能：飛航模式下、地下、沒有 SIM 卡的手機上都能用。你輸入的內容不會離開手機。"),
        ("我的看板看不清楚，該改什麼？",
         "四件事，照這個順序。<strong>把訊息寫短</strong>——字高取決於螢幕能給的空間，字數越少字越大。<strong>用加寬</strong>——筆畫最粗的字體。<strong>選一組真有對比的配色</strong>——App 會顯示實測的對比度，低於 4.5:1 時提醒你。<strong>把手機橫過來</strong>，看板會更寬。還有一個誠實的限度：在直射陽光下，或者超過幾十公尺的距離，再好的配色也贏不了。"),
        ("舉著看板的時候螢幕變暗，或者關閉。",
         "看板顯示期間，LookAt 會把亮度調到最高並阻止螢幕休眠，離開時立刻把<em>你原本的</em>亮度還回去。仍有兩件事會壓低亮度，而且任何 App 都無法覆蓋：低耗電模式，以及手機發熱時 iOS 主動降低亮度。如果發熱，等它涼下來就會恢復。"),
        ("怎麼儲存一則訊息以便重複使用？",
         "存成預設組合，最多 24 組。用已有的名稱儲存會覆蓋那一組，而不是再建一組同名的。"),
        ("iPad 能用嗎？",
         "能。LookAt 是 iPhone 和 iPad 共用的一個 App，需要 iOS 或 iPadOS 18 或以上。在 iPad 上看板只是更寬。"),
        ("捲動和閃爍沒有作用。",
         "看一下「設定」→「輔助使用」→「動態效果」→「減少動態效果」。開啟時，LookAt 會刻意停止捲動和閃爍——每秒六次的閃光正是這個設定要減弱的刺激——並把整則訊息靜止地完整顯示出來。"),
        ("真的免費嗎？",
         "是的：免費，裡面沒有任何要買的東西，沒有廣告，也不需要帳號。"),
        ("怎麼刪除我的資料？",
         "刪除 App。草稿、預設組合、設定全都在裝置上，會跟著一起消失。沒有帳號要註銷，也沒有伺服器需要聯絡。"),
    ],
)
