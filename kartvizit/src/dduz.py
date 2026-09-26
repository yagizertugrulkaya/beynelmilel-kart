# D-duz.png: D1 (üst, ana teslim) ve D2 (alt) düz yüzler; ince kesim çerçevesi + kesik güvenli alan çizgisi.
from PIL import Image, ImageDraw, ImageFont
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PX = 300 / 25.4
BLEED = round(3 * PX)
W, PAD, GAP, LABEL = 2000, 70, 60, 70
cw = (W - 2 * PAD - GAP) // 2
rows = [('D1', 'D1 · birebir brief (ana öneri)'), ('D2', 'D2 · + iletişim satırı ve alan adı')]
try:
    f1 = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 30); f2 = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)
except OSError:
    f1 = f2 = ImageFont.load_default()
cards = {}
for v, _ in rows:
    for s in ('on', 'arka'):
        im = Image.open(os.path.join(OUT, f'{v}-{s}.png')).convert('RGB')
        im = im.crop((BLEED, BLEED, im.width - BLEED, im.height - BLEED))
        cards[v, s] = im.resize((cw, round(im.height * cw / im.width)), Image.LANCZOS)
ch = cards['D1', 'on'].height
H = PAD + len(rows) * (LABEL + ch + 40 + GAP) + 20
sheet = Image.new('RGB', (W, H), '#FFFFFF')
d = ImageDraw.Draw(sheet)
def dashed(box, color, dash=10, gap=8):
    x0, y0, x1, y1 = box
    for x in range(x0, x1, dash + gap):
        d.line((x, y0, min(x + dash, x1), y0), fill=color); d.line((x, y1, min(x + dash, x1), y1), fill=color)
    for y in range(y0, y1, dash + gap):
        d.line((x0, y, x0, min(y + dash, y1)), fill=color); d.line((x1, y, x1, min(y + dash, y1)), fill=color)
y = PAD
for v, name in rows:
    d.text((PAD, y), name, fill='#1F3864', font=f1); y += LABEL
    for i, s in enumerate(('on', 'arka')):
        x = PAD + i * (cw + GAP)
        sheet.paste(cards[v, s], (x, y))
        d.rectangle((x - 1, y - 1, x + cw, y + ch), outline='#B8BCC4')
        k = round(4 * PX * cw / (85 * PX))
        dashed((x + k, y + k, x + cw - k, y + ch - k), '#9DC9C1')
        d.text((x, y + ch + 12), 'Ön yüz' if s == 'on' else 'Arka yüz', fill='#6A6F78', font=f2)
    y += ch + 40 + GAP
d.text((PAD, H - 44), 'Gri çerçeve: kesim çizgisi (85 × 55 mm)   ·   Kesik çizgi: güvenli alan (kenardan 4 mm)', fill='#8A8F98', font=f2)
sheet.save(os.path.join(OUT, 'D-duz.png'))
print(sheet.size)
