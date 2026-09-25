"""Yayın klasörünü üretir: kaynak/ -> docs/ (GitHub Pages, main + /docs).
Kullanım:
    python tools/site-build.py                   # domainsiz (geçici github.io adresi; canonical/og/CNAME YOK)
    python tools/site-build.py beynelmilel.org   # domainli (canonical, og, hreflang, robots, sitemap, CNAME)
Kaynak dosyalara dokunmaz; her çalıştırmada docs/ yeniden üretilir.
Pilates `tools/site-build.py` deseninden uyarlandı: iki dil, GÖRELİ yollar (github.io alt dizini), CNAME/.nojekyll.
"""
import io, os, re, shutil, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "kaynak")
OUT = os.path.join(ROOT, "docs")
DOMAIN = sys.argv[1].strip().lower().rstrip("/") if len(sys.argv) > 1 else None
BASE = ("https://%s/" % DOMAIN) if DOMAIN else None
NAVY = (31, 56, 100)          # #1F3864
PAPER = (246, 244, 241)       # #F6F4F1
INK = (23, 24, 26)            # #17181A
LASTMOD = "2026-09-25"

PAGES = [  # (kaynak, çıktı, göreli kök öneki, lang, og:locale)
    ("index.html", "index.html", "", "tr", "tr_TR"),
    (os.path.join("en", "index.html"), os.path.join("en", "index.html"), "../", "en", "en_US"),
]

# ---- klasör
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "en"))
shutil.copytree(os.path.join(SRC, "assets"), os.path.join(OUT, "assets"))
shutil.copy(os.path.join(SRC, "yagiz-ertugrul-kaya.vcf"), OUT)
io.open(os.path.join(OUT, ".nojekyll"), "w").write("")

# ---- favicon seti (logo_mark_300.png: lacivert işaret, şeffaf, 300x264 -> kare kanvas)
mark = Image.open(os.path.join(SRC, "assets", "logo_mark_300.png")).convert("RGBA")
side = max(mark.size)
square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
square.alpha_composite(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
def sq(size, pad=0.0):
    inner = round(size * (1 - 2 * pad))
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    im.alpha_composite(square.resize((inner, inner), Image.LANCZOS), ((size - inner) // 2, (size - inner) // 2))
    return im
sq(32, 0.05).save(os.path.join(OUT, "favicon-32.png"), optimize=True)
sq(16, 0.0).save(os.path.join(OUT, "favicon-16.png"), optimize=True)
sq(192, 0.08).save(os.path.join(OUT, "icon-192.png"), optimize=True)
apple = Image.new("RGBA", (180, 180), PAPER + (255,))
apple.alpha_composite(sq(180, 0.14))
apple.convert("RGB").save(os.path.join(OUT, "apple-touch-icon.png"), optimize=True)
sq(48, 0.04).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])

# ---- og.png 1200x630: kırık beyaz zemin + lacivert işaret + ad/unvan (sistem TTF; web fontu PIL okuyamaz)
def font(size, bold=False):
    cands = ["GeorgiaPro-CondSemiBold.ttf" if bold else "GeorgiaPro-CondRegular.ttf", "georgia.ttf", "arial.ttf"]
    for c in cands:
        p = os.path.join(r"C:\Windows\Fonts", c)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()
og = Image.new("RGB", (1200, 630), PAPER)
d = ImageDraw.Draw(og)
m = sq(300, 0.0)
og.paste(m, (90, 165), m)
d.text((430, 205), "Yağız Ertuğrul Kaya", font=font(74, True), fill=NAVY)
d.text((432, 300), "Yazılım Geliştirici & Kurucu · Beynelmilel", font=font(36), fill=INK)
d.text((432, 360), "Sistemler · Web siteleri · Reklam", font=font(30), fill=(90, 90, 90))
d.rectangle([432, 430, 1110, 434], fill=NAVY)
d.text((432, 452), DOMAIN or "Bursa, Türkiye", font=font(30), fill=NAVY)
og.save(os.path.join(OUT, "og.png"), optimize=True)

# ---- html
STRIP = re.compile(r'^\s*<(?:link rel="(?:icon|apple-touch-icon|canonical|alternate)"|meta (?:property="og:|name="twitter:|name="theme-color")).*?>\s*\n', re.M)
for src_rel, out_rel, pre, lang, locale in PAGES:
    s = io.open(os.path.join(SRC, src_rel), encoding="utf-8").read()
    s = STRIP.sub("", s)  # kaynakta kalmış eski head etiketlerini temizle (tek üretim noktası burası)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
    desc = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    head = [
        '<link rel="icon" href="%sfavicon.ico" sizes="48x48">' % pre,
        '<link rel="icon" type="image/png" sizes="32x32" href="%sfavicon-32.png">' % pre,
        '<link rel="icon" type="image/png" sizes="16x16" href="%sfavicon-16.png">' % pre,
        '<link rel="apple-touch-icon" sizes="180x180" href="%sapple-touch-icon.png">' % pre,
        '<meta name="theme-color" content="#F6F4F1">',
    ]
    if BASE:
        here = BASE + ("" if lang == "tr" else "en/")
        head += [
            '<link rel="canonical" href="%s">' % here,
            '<link rel="alternate" hreflang="tr" href="%s">' % BASE,
            '<link rel="alternate" hreflang="en" href="%sen/">' % BASE,
            '<link rel="alternate" hreflang="x-default" href="%s">' % BASE,
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Beynelmilel">',
            '<meta property="og:title" content="%s">' % title,
            '<meta property="og:description" content="%s">' % desc,
            '<meta property="og:url" content="%s">' % here,
            '<meta property="og:image" content="%sog.png">' % BASE,
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            '<meta property="og:locale" content="%s">' % locale,
            '<meta property="og:locale:alternate" content="%s">' % ("en_US" if lang == "tr" else "tr_TR"),
            '<meta name="twitter:card" content="summary_large_image">',
        ]
    m = re.search(r'<meta name="description"[^>]*/?>\n', s)
    assert m, "meta description yok: " + src_rel
    s = s[:m.end()] + "\n".join(head) + "\n" + s[m.end():]
    io.open(os.path.join(OUT, out_rel), "w", encoding="utf-8", newline="\n").write(s)

if BASE:
    io.open(os.path.join(OUT, "CNAME"), "w", encoding="utf-8", newline="\n").write(DOMAIN + "\n")
    io.open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
        "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % BASE)
    io.open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n'
        '  <url><loc>%sen/</loc><lastmod>%s</lastmod></url>\n</urlset>\n' % (BASE, LASTMOD, BASE, LASTMOD))

print("docs/ hazir:", sorted(os.listdir(OUT)), "| domain:", DOMAIN or "- (gecici github.io)")
