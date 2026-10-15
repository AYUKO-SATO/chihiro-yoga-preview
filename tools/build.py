#!/usr/bin/env python3
"""Builds the static client-preview pages (index / terms / privacy / tokushoho).

Run from the repository root:  python3 tools/build.py
Design source: Figma file dDopAVcEA54rMN5ch7XFbN (ちひろヨガ_Mobile375 + legal pages).
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = "20261015b"  # bump when images change (cache busting)
EMAIL = "paloma.yoga.studio@gmail.com"
LINE = "https://lin.ee/5bhqEXA"
RESERVE = "https://airrsv.net/chihiroyoga/calendar"
INSTA = "https://www.instagram.com/yoga_studio_paloma/"
YT = "q2wwzRbcwj4"

e = html.escape


def br(s):
    return e(s).replace("\n", "<br>")


# ---------- icons ----------
IC_INSTA = '<svg viewBox="0 0 38 38" aria-hidden="true"><rect x="4.5" y="4.5" width="29" height="29" rx="8" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="19" cy="19" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="27" cy="11" r="1.6" fill="currentColor"/></svg>'
IC_LINE = '<svg viewBox="0 0 38 38" aria-hidden="true"><path d="M19 6c-8 0-14.5 5-14.5 11.5 0 3.7 2.2 7 5.6 9.100-.2 1.600-.9 3.300-2 4.800 2.700-.3 5-1.400 6.700-2.900 1.300.3 2.800.5 4.200.5 8 0 14.500-5 14.500-11.500S27 6 19 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'
IC_MENU = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 14h32M8 24h32M8 34h32" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
IC_CLOSE = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M12 12l24 24M36 12L12 36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
IC_CHEV = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
IC_CAL = '<svg viewBox="0 0 18 18" aria-hidden="true"><rect x="2" y="3.5" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M2 7.500h14M6 2v3M12 2v3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>'
IC_BUBBLE = '<svg viewBox="0 0 18 18" aria-hidden="true"><path d="M9 2C4.900 2 1.500 4.700 1.500 8c0 1.800 1 3.400 2.600 4.500-.1.900-.5 1.700-1.100 2.400 1.400-.2 2.500-.7 3.300-1.400.7.200 1.400.3 2.100.3 4.100 0 7.500-2.700 7.500-6S13.100 2 9 2z" fill="currentColor"/></svg>'
IC_PREV = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M10 3L5 8l5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
IC_NEXT = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------- shared chrome ----------
NAV = [
    ("ホーム", "index.html#top"),
    ("お知らせ", "index.html#news"),
    ("コンセプト", "index.html#concept"),
    ("スタジオ紹介", "index.html#about"),
    ("レッスンメニュー", "index.html#lesson"),
    ("料金", "index.html#price"),
    ("スケジュール", "index.html#schedule"),
    ("講師紹介", "index.html#instructor"),
    ("お客様の声", "index.html#voice"),
    ("よくある質問", "index.html#faq"),
    ("アクセス", "index.html#access"),
    ("ご予約", "index.html#reservation"),
]


def head(title, desc, rel=""):
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={V}">
</head>
<body>
<div class="notice">クライアント確認用テストサイト（デザイン案）｜スマホでご覧ください</div>
<div class="app">
"""


def header():
    items = "".join(f'<li><a href="{h}">{e(t)}</a></li>' for t, h in NAV)
    return f"""<header class="hdr">
  <a class="hdr-logo" href="index.html#top" aria-label="ちひろヨガスタジオ"><img src="img/logo_h.png?v={V}" alt="ちひろ ヨガスタジオ" width="155" height="56"></a>
  <div class="hdr-icons">
    <a href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram" class="ico38">{IC_INSTA}</a>
    <a href="{LINE}" target="_blank" rel="noopener" aria-label="公式LINE" class="ico38">{IC_LINE}</a>
    <button class="menu-btn" type="button" aria-label="メニューを開く" aria-expanded="false" aria-controls="drawer">{IC_MENU}</button>
  </div>
</header>
<nav id="drawer" class="drawer" aria-label="メインメニュー" hidden>
  <button class="drawer-close" type="button" aria-label="メニューを閉じる">{IC_CLOSE}</button>
  <ul>{items}</ul>
  <ul class="drawer-legal">
    <li><a href="privacy.html">プライバシーポリシー</a></li>
    <li><a href="terms.html">利用規約</a></li>
    <li><a href="tokushoho.html">特定商取引法に基づく表記</a></li>
  </ul>
</nav>
"""


def footer():
    return f"""<footer class="ftr">
  <img class="ftr-logo" src="img/logo_v.png?v={V}" alt="ちひろ ヨガスタジオ" width="88" height="124">
  <ul class="ftr-nav">
    <li><a href="privacy.html">プライバシーポリシー</a></li>
    <li><a href="terms.html">利用規約</a></li>
    <li><a href="tokushoho.html">特定商取引法に基づく表記</a></li>
  </ul>
  <div class="ftr-sns">
    <a href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram" class="ico45">{IC_INSTA}</a>
    <a href="{LINE}" target="_blank" rel="noopener" aria-label="公式LINE" class="ico45">{IC_LINE}</a>
  </div>
  <p class="ftr-copy">© ちひろヨガスタジオ. All Rights Reserved.</p>
</footer>
<div class="sticky">
  <a class="sticky-reserve" href="{RESERVE}" target="_blank" rel="noopener">{IC_CAL}<span>予約はこちら</span></a>
  <a class="sticky-line" href="{LINE}" target="_blank" rel="noopener">{IC_BUBBLE}<span>公式LINE登録</span></a>
</div>
</div>
<script src="js/main.js?v={V}" defer></script>
</body>
</html>
"""


def heading(eyebrow, title):
    return f'<div class="sh"><span class="sh-en">{e(eyebrow)}</span><h2 class="sh-ja">{e(title)}</h2><i class="sh-bar"></i></div>'


def btn(label, href, cls="btn", ext=True):
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{cls}" href="{href}"{t}>{e(label)}</a>'


def cta_band():
    return f'<section class="cta"><p>レッスンのご予約はこちらから</p>{btn("ご予約はこちら", RESERVE, "btn btn-white")}</section>'


# ---------- index ----------
HERO = [
    ("hero1.jpg", True), ("hero2.jpg", True), ("hero3.jpg", True), ("hero4.jpg", True), ("hero5.jpg", False),
]


def hero():
    slides = ""
    for i, (img, copy) in enumerate(HERO):
        alt = "" if copy else "移転前にYOGA studio PALOMAで体験レッスンを受けられます。身体が硬い方も、初めての方も。"
        txt = ""
        if copy:
            txt = '<div class="hero-copy"><p class="hero-kicker">町田・相模原 ヨガ教室</p><p class="hero-h">私にも、<br>できるかも</p></div>'
        cls = "hero-btn" + ("" if copy else " hero-btn-c")
        shade = ' hero-shade' if i < 3 else ''
        slides += f'''<div class="hero-slide{shade}{' is-active' if i == 0 else ''}" data-i="{i}"><img src="img/{img}?v={V}" alt="{e(alt)}" width="375" height="460"{' loading="lazy"' if i else ''}>{txt}<a class="{cls}" href="{RESERVE}" target="_blank" rel="noopener">体験予約はこちら</a></div>'''
    dots = "".join(f'<button type="button" class="dot{" is-active" if i == 0 else ""}" aria-label="スライド{i+1}" data-go="{i}"></button>' for i in range(5))
    return f'<section class="hero" id="top" aria-roledescription="carousel"><div class="hero-track">{slides}</div><div class="dots">{dots}</div></section>'


NEWS = [("2026.09.10", "秋の新クラス「陰陽ヨガ」開講のお知らせ"), ("2026.08.28", "お盆期間の営業について")]
BLOG = [("2026.09.05", "初心者さんがヨガを始めるときのポイント"), ("2026.08.20", "肩こり・首こりに効くおすすめストレッチ")]


def cards(items):
    out = ""
    for d, t in items:
        out += f'<article class="card"><div class="card-thumb"></div><div class="card-text"><time>{d}</time><h3>{e(t)}</h3></div></article>'
    return f'<div class="carousel"><div class="car-row">{out}</div><button class="car-btn car-prev" type="button" aria-label="前へ">{IC_PREV}</button><button class="car-btn car-next" type="button" aria-label="次へ">{IC_NEXT}</button></div>'


LESSONS = [
    ("おつかれリセットヨガ", "月・水 19:00〜20:15", "lesson_reset.jpg", "一日の疲れがたまりやすい肩・首・腰まわりを、やさしい動きと呼吸でゆるめます。身体が硬い方やヨガが初めての方も安心して参加できる、夜のリセットヨガです。\n※初回体験は女性限定・お一人様1回限りです。"),
    ("アロマキャンドルヨガ", "金曜 19:00〜20:15（月2回）", "lesson_aroma.jpg", "アロマの香りとキャンドルの灯りに包まれながら、ゆったりと身体をほぐします。深い呼吸とやさしい動きで、一日の緊張をほどき、心と身体をリラックスへ導きます。"),
    ("フローヨガ", "水曜 9:45〜11:00", "lesson_flow.jpg", "呼吸に合わせて流れるようにポーズをつなぎ、全身を心地よく動かします。身体をしっかり動かしたい方、運動不足を解消してリフレッシュしたい方におすすめです。\n※フローヨガは2回目からご参加いただけます。"),
    ("プライベートレッスン", "予約制", "lesson_private.jpg", "お一人おひとりの身体やお悩みに合わせて行う、オーダーメイドのヨガレッスンです。周りを気にせず、自分のペースでじっくり身体と向き合います。"),
    ("自律神経ケア", "予約制", "lesson_autonomic.jpg", "「眠っても疲れがとれない」「頭痛や肩こりを繰り返す」「更年期の不調や気分の波がつらい」「病院では異常がないけれどなんとなく調子が悪い」。そんな不調を我慢していませんか？\n専用の測定器で今の状態を確認し、その日の状態に合わせて呼吸・やさしい運動・筋膜ケアを行います。\n初回は、自律神経測定の結果をまとめたデータをお渡し。ご自宅で続けられるセルフケアもアドバイスします。"),
]


def paras(s):
    return "".join(f"<p>{e(p)}</p>" for p in s.split("\n"))


def acc_lesson():
    out = ""
    for n, m, img, body in LESSONS:
        out += f'''<div class="acc lesson"><button class="acc-head" type="button" aria-expanded="false"><img src="img/{img}?v={V}" alt="" width="92" height="92" loading="lazy"><span class="l-col"><span class="l-name">{e(n)}</span><span class="l-meta">{e(m)}</span></span><span class="chev">{IC_CHEV}</span></button><div class="acc-body"><div class="acc-in">{paras(body)}</div></div></div>'''
    return f'<div class="lesson-list">{out}</div>'


def row(label, price, note=None, first=False):
    n = f'<p class="pr-note">{e(note)}</p>' if note else ""
    return f'<div class="pr-row{" first" if first else ""}"><div class="pr-line"><span>{e(label)}</span><b>{e(price)}</b></div>{n}</div>'


def note_row(text, first=False):
    return f'<div class="pr-row{" first" if first else ""}"><p class="pr-note">{e(text)}</p></div>'


def pcard(title, sub, rows):
    s = f'<p class="pc-sub">{e(sub)}</p>' if sub else ""
    return f'<div class="pcard"><div class="pc-title"><h3>{e(title)}</h3>{s}</div>{"".join(rows)}</div>'


def price():
    cards_ = [
        pcard("初回体験", "女性限定", [row("おつかれリセットヨガ", "¥1,500", "お一人様1回限り", True)]),
        pcard("通常レッスン", "おつかれリセットヨガ／アロマキャンドルヨガ／フローヨガ", [row("1回", "¥2,500"), row("5回券", "¥12,000", "有効期限 2026年12月末まで")]),
        pcard("プライベートヨガ", "75分", [row("非会員", "¥8,800"), row("PALOMA会員", "¥7,700"), note_row("姿勢評価・ヨガポーズ・パーソナルトレーニング含む"), row("15分延長ごとに", "+¥1,100", None, True)]),
        pcard("自律神経ケア", None, [row("初回（90分）", "¥8,800", "測定・データ添付・カウンセリング込み"), row("2回目以降（75分）", "¥7,700"), row("呼吸ケア（45分）", "¥4,500"), row("15分延長または測定追加", "+¥1,100")]),
        pcard("セミプライベートヨガ", "90分・最大4名", [row("非会員", "¥5,000"), row("PALOMA会員", "¥4,500")]),
        pcard("回数券", "PALOMA会員限定", [row("3回券", "¥10,500", "1回 ¥3,500"), row("5回券", "¥16,500", "1回 ¥3,300"), note_row("有効期限 2か月")]),
    ]
    return f'''<section class="sec sec-green" id="price">{heading("PRICE", "料金")}
<div class="join"><span>入会金</span><b>なし</b></div>
{"".join(cards_)}
<div class="pfoot"><p>ヨガマット＋補助具付き<br>動きやすい服装・お水をご持参ください</p><a class="btn btn-green btn-wide" href="{LINE}" target="_blank" rel="noopener">ご予約・ご相談はLINEのトークから</a></div></section>'''


FAQ = [
    ("身体が硬く、ヨガが初めてでも参加できますか？", "はい、大丈夫です。身体の柔らかさや経験に関係なく、ご自身のペースでご参加いただけます。\nポーズの完成を目指すのではなく、その日の身体に合わせて無理なく動いていきます。"),
    ("肩や腰、膝などに不調があっても参加できますか？", "体調を確認しながら、負担の少ない動きへ調整いたします。\n治療中の方や医師から運動について指示を受けている方は、事前に医師へご相談ください。ご予約時にも、現在のお身体の状態をお知らせください。"),
    ("どのクラスを選べばよいか分かりません。", "クラスの内容や運動量を参考にお選びいただけます。\n迷われる場合は、現在のお悩みや運動経験を公式LINEからお知らせください。お身体の状態や目的に合うクラスをご案内いたします。"),
    ("グループレッスンとプライベートレッスンの違いは何ですか？", "グループレッスンは、少人数で一緒にヨガを楽しむクラスです。\nプライベートレッスンは、体調やお悩み、目的に合わせて内容を組み立てます。周りを気にせず、ご自身のペースで取り組みたい方はもちろん、ご家族や大切な方と一緒に、ゆっくり過ごしたい方にもおすすめです。"),
    ("プライベートレッスンは、どのような方におすすめですか？", "慢性的な肩こりや腰まわりの不調がある方、運動に不安がある方、じっくり身体を見てほしい方におすすめです。\nヨガが初めての方や、グループレッスンへ参加する前に基本を知りたい方にもご利用いただけます。"),
    ("自律神経ケアでは、どのようなことをしますか？", "現在の体調や生活の様子を伺い、自律神経の状態を測定します。\nその結果をもとに、呼吸、やさしい運動、筋膜ケアなどを組み合わせ、お身体に合ったセルフケアをご提案します。"),
    ("自律神経ケアは、どのような悩みに向いていますか？", "眠りの浅さ、疲れが取れにくい、頭痛、胃腸の不調、更年期による変化など、心身のバランスが気になる方におすすめです。\n医療行為や病気の診断・治療を行うものではありません。通院中の方は、必要に応じて医師へご相談ください。"),
    ("持ち物や服装を教えてください。", "動きやすい服装でお越しください。お飲み物と汗拭き用のタオルをお持ちください。\nヨガマットやレッスンに使用する道具は、スタジオにご用意しています。簡易のお着替えスペースもございます。"),
    ("予約やキャンセルはどのようにすればよいですか？", "レッスンは予約制です。予約サイトまたは公式LINEからお申し込みください。\nグループレッスンのキャンセルは、開始2時間前までにお願いいたします。2時間を過ぎてからのキャンセルは、回数券1回分を消化させていただきます。回数券の有効期限内に振替クラスをご予約ください。\nプライベートレッスンと自律神経ケアのキャンセルは、前日の23:59までにお願いいたします。"),
    ("講師の都合で休講になった場合はどうなりますか？", "講師の体調不良などにより休講となる場合は、公式LINEなどからご連絡いたします。\nグループレッスンの回数券は消化せず、有効期限を延長いたします。プライベートレッスンと自律神経ケアは、別の日程へ振り替えをお願いいたします。"),
    ("参加に年齢や性別の制限はありますか？", "年齢にかかわらず、ご自身の体調に合わせてご参加いただけます。\n女性を中心にご案内していますが、男性の方のご参加についても事前にご相談を承っています。公式LINEからお問い合わせください。"),
    ("暑さが苦手ですが、ヨガはできますか？", "はい、ご参加いただけます。\n当スタジオは、常温ヨガ教室です。室温に配慮しながらレッスンを行い、暑さがつらい場合は、途中で休んだり水分補給をしたりしていただけます。無理をせず、ご自身の体調に合わせてご参加ください。"),
    ("ヨガの流派はありますか？", "特定の流派に限定していません。\n呼吸と身体の基本的な使い方を大切にしながら、フローヨガ・陰ヨガ・ヨガセラピーなど、これまで学んできたさまざまな要素を取り入れています。クラスの目的や参加される方の体調に合わせて、無理なく行える内容をお伝えしています。"),
]


def faq():
    out = ""
    for q, a in FAQ:
        out += f'<div class="acc faq"><button class="acc-head" type="button" aria-expanded="false"><span class="qb">Q</span><span class="q">{e(q)}</span><span class="chev">{IC_CHEV}</span></button><div class="acc-body"><div class="acc-in">{paras(a)}</div></div></div>'
    return f'<div class="faq-list">{out}</div>'


MESSAGE = "私自身、子育てで心身ともに疲れていたときにヨガに出会いました。身体がほぐれると心までふっと軽くなる。その実感が、今も伝え続けている理由です。ヨガは、できることを増やすためだけのものではありません。\n今日の自分はどんなふうに感じているのか？何が心地良い？どこまでなら無理なくいられるのか？\n静かに自分へ問いかけながらその日の自分に合った選択を重ねていく。\nその小さな積み重ねが、「私にもできるかもしれない」という、かすかな光のような自信につながっていきます。\n頑張ることが当たり前になり自分を後回しにしてしまう人へ心と身体にそっと目を向ける時間を届けたいです。\n身体が硬くても大丈夫。\nできないことより「できるかも」を一緒に見つけましょう。"
QUALS = "・Barkan Method Hot Yoga TT Level 1・2・3 修了\n・ブリスベイビー マタニティ・産後ヨガ 修了\n・David Kim 陰ヨガ Level 1・2 修了\n・Kelly Haas ヨガセラピー TT 修了\n・Philosophy of Five Elements Yoga® 修了\n・整形外科ヨガ 認定者\n・AFAA Personal Fitness Trainer\n・JMF 自律神経ケアセラピスト"
BIO = "育児中に感じた身体の不調をきっかけにホットヨガを始めました。\nヨガを続ける中で、身体だけでなく気持ちにも変化が生まれることを実感。より深く学ぶためにフロリダへ渡り「Berkan Method Hot Yoga」の指導トレーニングを修了しました。\n帰国後は、ヨガスタジオやスポーツクラブ、企業などで指導経験を重ね外ヨガ「chihiroyoga」を開始。2019年から「YOGA studio PALOMA」を運営。\nその後、陰ヨガや機能解剖学を学ぶ中で同じポーズでも心地よい形は一人ひとり違うことを改めて実感しました。\n自身も更年期の不調を経験したことをきっかけに、身体・呼吸・生活習慣と自律神経の関係を学び、現在はヨガ指導に加えて、自律神経測定器を使った専門的なケアも提供しています。\n少人数制レッスンだからこそ一人ひとりが自分に合う方法を見つけ「私にもできるかも」と思える時間をお届けしたいと考えています。"


def card_acc(label, body, small=False):
    return f'<div class="acc card-acc{" small" if small else ""}"><button class="acc-head" type="button" aria-expanded="false"><span class="ca-label">{e(label)}</span><span class="chev">{IC_CHEV}</span></button><div class="acc-body"><div class="acc-in">{paras(body)}</div></div></div>'


def index():
    return head("ちひろヨガスタジオ｜町田・相模原のヨガ教室（テスト版）", "「私にもできるかも」が芽生える時間を。町田・相模原のヨガ教室ちひろヨガスタジオ。") + header() + f'''<main>
{hero()}
<section class="sec sec-white msg"><h2>移転前に、<br>ヨガを体験してみませんか？</h2><i class="sh-bar"></i>
<p>新しいスタジオへの移転に先がけて、<br>現在の「YOGA studio PALOMA」で<br>体験レッスンを受けていただけます。</p>
<p>身体が硬い方も、ヨガが初めての方も。<br>一人ひとりのペースを大切に、<br>無理なく身体を動かし、<br>ゆっくり呼吸を整えていきます。</p>
<p class="msg-strong">「私にもできるかも」<br>そんな気持ちで、<br>気軽にいらしてください。</p>
<p>レッスンのご案内・ご予約は、<br>公式LINEから承っております。</p>
<a class="btn btn-line" href="{LINE}" target="_blank" rel="noopener">公式LINEで予約・ご相談</a></section>

<section class="sec sec-ivory" id="news">{heading("NEWS", "お知らせ・ニュース")}{cards(NEWS)}{btn("もっと読む", "#news", "btn btn-outline", False)}</section>

<section class="sec sec-white sec-banner"><a href="{RESERVE}" target="_blank" rel="noopener"><img class="banner" src="img/campaign.jpg?v={V}" alt="新規メンバー募集中 体験レッスン1回1,500円 当日入会すると入会金無料" width="335" height="188" loading="lazy"></a></section>

{cta_band()}

<section class="sec sec-ivory concept" id="concept">{heading("CONCEPT", "コンセプト")}
<h3 class="lead">「私にもできるかも」が芽生える時間</h3>
<p class="quote">「頑張るためではなく、私に戻るために」</p>
<p class="body-c">ヨガと呼吸で身体をほどき<br>自分のペースを取り戻す<br><br>「私にもできるかも」が<br>芽生える時間を届けます</p>
<button class="video" type="button" data-yt="{YT}" aria-label="コンセプト動画を再生する"><img src="https://img.youtube.com/vi/{YT}/maxresdefault.jpg" alt="" width="327" height="184" loading="lazy"><span class="play"><svg viewBox="0 0 18 20" aria-hidden="true"><path d="M1 1.500v17l15-8.500z" fill="#3e5443"/></svg></span></button></section>

<section class="sec sec-white" id="about">{heading("ABOUT", "スタジオ紹介")}
<h3 class="lead">はじめてでも<br>ほっとできる場所</h3>
<p class="body-c">ちひろヨガスタジオは<br>身体が硬い方や運動が苦手な方も<br>安心して通える常温ヨガスタジオです。<br><br>一人ひとりの身体やその日の体調を見ながら<br>無理のない動きや休み方を<br>丁寧にお伝えします。<br><br>マットや補助具もご用意していますので、<br>自分のペースで気軽にご参加いただけます。</p>
<div class="features"><figure><img src="img/feature_mat.jpg?v={V}" alt="" width="162" height="160" loading="lazy"><figcaption>マット＋プロップス完備</figcaption></figure><figure><img src="img/feature_studio.jpg?v={V}" alt="" width="162" height="160" loading="lazy"><figcaption>スタジオ空間</figcaption></figure></div></section>

{cta_band()}

<section class="sec sec-ivory" id="lesson">{heading("LESSON", "レッスンメニュー")}{acc_lesson()}</section>

{price()}

<section class="sec sec-white" id="schedule">{heading("SCHEDULE", "スケジュール")}<div class="sched"><span>カレンダー画像（準備中）</span></div><div class="mini-dots"><i class="on"></i><i></i><i></i></div></section>

{cta_band()}

<section class="sec sec-ivory" id="instructor">{heading("INSTRUCTOR", "講師紹介")}
<img class="avatar" src="img/instructor.jpg?v={V}" alt="講師 加藤千尋" width="140" height="140" loading="lazy">
<p class="i-name">加藤千尋</p>
<p class="i-role">ちひろスタジオ代表<br>ヨガ講師｜自律神経ケアセラピスト</p>
<div class="bio">{paras(BIO)}</div>
{card_acc("MESSAGE", MESSAGE)}{card_acc("資格情報", QUALS, True)}</section>

<section class="sec sec-white" id="voice">{heading("VOICE", "お客様の声")}
<article class="voice"><div class="v-top"><span class="v-av"></span><b>Aさん</b></div><h3>良い先生に巡り会えたことに、感謝！</h3><p>毎週お世話になってます。日頃から身体を動かす機会がないのでこちらでお世話になっております。肩が痛いのと坐骨神経痛が酷く毎日がとても辛かったです。週に一度レッスンに出ると痛みが和らぎます。その日の夜は熟睡できます。最近は、体力がついてきたのを実感しております。良い先生に巡り会えてとても感謝しております。</p></article></section>

<section class="sec sec-ivory" id="blog">{heading("BLOG", "ブログ")}{cards(BLOG)}<a class="tla" href="#blog"><span>ブログ一覧はこちら</span><em>＞</em></a></section>

<section class="sec sec-white" id="faq">{heading("FAQ", "よくある質問")}{faq()}</section>

<section class="sec sec-ivory" id="access">{heading("ACCESS", "店舗情報")}
<div class="info"><p>〒252-0318<br>神奈川県相模原市南区上鶴間本町2-11-21<br>YOGA studio PALOMA</p><p class="sub">【定休日】不定休</p></div>
<div class="map"><iframe title="地図" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%E7%9B%B8%E6%A8%A1%E5%8E%9F%E5%B8%82%E5%8D%97%E5%8C%BA%E4%B8%8A%E9%B6%B4%E9%96%93%E6%9C%AC%E7%94%BA2-11-21&amp;output=embed"></iframe></div></section>

<section class="sec sec-white" id="reservation">{heading("RESERVATION", "ご予約")}
<p class="resv-text">ご予約は予約サイトまたは公式LINEより<br>お願いいたします</p>
<a class="btn btn-outline btn-ico" href="{LINE}" target="_blank" rel="noopener">{IC_BUBBLE}<span>公式LINEから連絡する</span><em>＞</em></a></section>

<section class="sec sec-ivory" id="instagram"><a class="ig-handle" href="{INSTA}" target="_blank" rel="noopener">{IC_INSTA}<span>@yoga_studio_paloma</span></a><div class="ig-grid">{"<i></i>"*9}</div></section>
</main>
''' + footer()


# ---------- legal pages ----------
def lcard(title, body, chip=None):
    c = f'<span class="chip">{e(chip)}</span>' if chip else ""
    return f'<section class="lcard"><h2>{e(title)}</h2>{c}<p>{br(body)}</p></section>'


def legal(title_en, title_ja, lead, inner, doc_title, desc):
    return head(f"{doc_title}｜ちひろヨガスタジオ", desc) + header() + f'''<main>
<section class="legal-top">{heading(title_en, title_ja)}<p>{br(lead)}</p></section>
<div class="legal-body">{inner}</div>
</main>
''' + footer()


TERMS = [
    ("第1条　適用", "本規約は、ちひろヨガスタジオ（以下「当スタジオ」）が提供するレッスンおよび関連するサービスのすべてに適用されます。ご予約・ご参加をもって、本規約にご同意いただいたものとみなします。", None),
    ("第2条　サービス内容", "当スタジオのレッスンは、心身を整え、運動習慣やリラックスのきっかけをつくることを目的としています。医療行為ではなく、病気の治療や診断を目的とするものではありません。", None),
    ("第3条　男性のご参加について", "グループ体験レッスンは女性限定です。男性の方は、プライベートまたはセミプライベートレッスンで承ります。ご希望の方は事前にご相談ください。", None),
    ("第4条　体調について", "発熱など、体調がすぐれないときは無理をせず、お休みください。持病・妊娠・けがなどがある方は、レッスン前に講師へお知らせください。通院中の方は、事前に主治医へご相談のうえご参加ください。", None),
    ("第5条　レッスン中の安全について", "身体の硬さや経験は気にせず、ご自身のペースでご参加ください。痛みや違和感があるときはお休みいただき、遠慮なく講師にお知らせください。", None),
    ("第6条　ご予約・キャンセル", "・ご予約は、当スタジオ指定の予約フォームまたは公式LINEから承ります。\n・キャンセル・日時の変更は、レッスン開始の○時間前までにご連絡ください。\n・期限を過ぎてのキャンセル、またはご連絡のない欠席の場合は、レッスン料の全額（または○％）を頂戴することがあります。\n・当スタジオの都合や天候・災害等でレッスンを中止する場合は、振替または返金で対応します。", "サンプル文面｜キャンセル規定は確定後に差し替えます"),
    ("第7条　料金・お支払い", "レッスン料金は、ホームページの料金表に記載のとおりです。お支払い方法・時期は、当スタジオが指定する方法に従ってください。", None),
    ("第8条　写真・動画撮影について", "他の方が写る撮影やSNSへの掲載は、必ずご本人の了承を得てください。スタジオで撮影する際も事前に確認し、同意をいただいたうえで使用します。", None),
    ("第9条　勧誘・営業行為について", "皆さまが安心して過ごせるよう、宗教・政治・営業等の勧誘や、チラシなどの配布はご遠慮ください。参加者への個別の勧誘も控えてください。", None),
    ("第10条　貴重品・お持ち物について", "貴重品やお持ち物は、ご自身での管理をお願いします。お帰りの際は、忘れ物がないかご確認ください。紛失・盗難について、当スタジオは責任を負いかねます。", None),
    ("第11条　プライバシーについて", "ここで知り得た個人情報やお話は、ご本人の了承なく、外部やSNSに公開しないようお願いします。お互いのプライバシーを大切にしましょう。当スタジオによる個人情報の取扱いは、プライバシーポリシーに定めます。", None),
    ("第12条　心地よい場をつくるために", "お互いを尊重し、安心できる時間を一緒につくっていきましょう。迷惑行為やハラスメントがある場合は、ご参加をお断りすることがあります。", None),
    ("第13条　免責事項", "ご自身の責任でご参加ください。当スタジオは、故意または重大な過失がある場合を除き、レッスン中の事故やけが等について責任を負いません。", None),
    ("第14条　規約の変更", "法令の改正や運営上の必要に応じて、本規約を改定することがあります。変更後の内容は、ホームページに掲載した時点から効力を生じます。", None),
    ("お問い合わせ", "ちひろヨガスタジオ\n" + EMAIL + "\n公式LINEからもご連絡いただけます。", None),
]

PRIV = [
    ("1．個人情報の取得", "ご予約やお問い合わせの際に、お名前、メールアドレス、電話番号、体調に関するお申し出など、必要な範囲で個人情報をお預かりします。", None),
    ("2．利用目的", "・レッスンのご予約・運営のため\n・お問い合わせへの対応のため\n・日程変更や休講などのご連絡のため\n・緊急時の連絡や、安全なレッスン提供のため", None),
    ("3．安全管理", "お預かりした個人情報は、漏えい・滅失・改ざんを防ぐよう、適切に管理します。", None),
    ("4．第三者への提供", "法令に基づく場合を除き、ご本人の同意なく第三者に提供することはありません。", None),
    ("5．外部サービスの利用", "予約システム、LINE、ホームページの運営などで外部サービスを利用します。個人情報を取り扱う場合は、適切な管理を行います。", None),
    ("6．Cookie等の利用", "ホームページの利便性向上やアクセス状況の把握のため、Cookie等を利用することがあります。ブラウザの設定により無効にすることもできます。", None),
    ("7．開示・訂正・削除", "ご本人からの請求には、本人確認のうえ、法令に従って対応します。", None),
    ("8．プライバシーポリシーの見直し", "法令の改正や運営上の必要に応じて内容を見直し、ホームページに掲載します。", None),
    ("9．お問い合わせ窓口", "ちひろヨガスタジオ\n" + EMAIL, None),
]

TOKU = [
    ("販売事業者", "ちひろヨガスタジオ", None),
    ("運営責任者", "ちひろ", "氏名の正式表記は確認後に記載"),
    ("所在地", "請求があった場合、遅滞なく開示いたします。", None),
    ("レッスン会場", "〒252-0318\n神奈川県相模原市南区上鶴間本町2-11-21\nYOGA studio PALOMA", None),
    ("電話番号", "請求があった場合、遅滞なく開示いたします。お問い合わせは、メールまたは公式LINEにてお願いします。", None),
    ("メールアドレス", EMAIL, None),
    ("販売価格", "ホームページの料金表に記載のとおりです。", None),
    ("お支払い方法・時期", "当スタジオが指定する方法・時期によります。", None),
    ("サービス提供時期", "ご予約いただいた日時に、レッスンを提供します。", None),
    ("キャンセル・返金", "レッスン開始の○時間前までにご連絡ください。期限を過ぎた場合は、レッスン料を頂戴することがあります。レッスン実施後の返金はできません。当スタジオの都合や災害等で中止する場合は、振替または返金で対応します。", "サンプル文面｜確定後に差し替えます"),
]


def toku_rows():
    out = ""
    for k, v, chip in TOKU:
        c = f'<span class="chip">{e(chip)}</span>' if chip else ""
        out += f'<div class="lrow"><h2>{e(k)}</h2>{c}<p>{br(v)}</p></div>'
    return f'<section class="lcard lrows">{out}</section>'


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content) // 1024, "KB")


if __name__ == "__main__":
    write("index.html", index())
    write("terms.html", legal("TERMS", "利用規約", "安心して、自分のペースで\n過ごしていただくために", "".join(lcard(*a) for a in TERMS), "利用規約", "ちひろヨガスタジオの利用規約です。"))
    write("privacy.html", legal("PRIVACY POLICY", "プライバシーポリシー", "ちひろヨガスタジオは、お預かりする個人情報を大切に取り扱います。", "".join(lcard(*a) for a in PRIV), "プライバシーポリシー", "ちひろヨガスタジオのプライバシーポリシーです。"))
    write("tokushoho.html", legal("LEGAL", "特定商取引法に基づく表記", "ご利用にあたっての事業者情報・お支払い・キャンセル等についてご案内します。", toku_rows(), "特定商取引法に基づく表記", "ちひろヨガスタジオの特定商取引法に基づく表記です。"))
    write("robots.txt", "User-agent: *\nDisallow: /\n")
