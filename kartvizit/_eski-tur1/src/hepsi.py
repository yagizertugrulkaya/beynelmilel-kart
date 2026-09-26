# _hepsi.png kontak sayfası: her varyant bir satır (ön | arka), kesim çizgisine kırpılmış.
from PIL import Image, ImageDraw, ImageFont
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLEED = round(3 * 300 / 25.4)  # 35 px
rows = ['v1','v2','v3','v4']
names = {'v1':'V1 Künye','v2':'V2 Gece Mührü','v3':'V3 Tek Eksen','v4':'V4 Yalnız İsim (yalnız isim + QR)'}
cards = {}
for r in rows:
    for s in ('on','arka'):
        im = Image.open(os.path.join(OUT, f'{r}-{s}.png')).convert('RGB')
        cards[r, s] = im.crop((BLEED, BLEED, im.width - BLEED, im.height - BLEED))
PAD, GAP, LABEL = 70, 60, 70
colw = max(c.width for c in cards.values())
W = PAD * 2 + colw * 2 + GAP
H = PAD + sum(LABEL + max(cards[r,'on'].height, cards[r,'arka'].height) + GAP for r in rows)
sheet = Image.new('RGB', (W, H), '#E4E5E8')
d = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 30)
except OSError: font = ImageFont.load_default()
y = PAD
for r in rows:
    d.text((PAD, y), names[r] + '   —   ön  |  arka', fill='#3A3D43', font=font)
    y += LABEL
    h = max(cards[r,'on'].height, cards[r,'arka'].height)
    for i, s in enumerate(('on','arka')):
        c = cards[r, s]
        x = PAD + i * (colw + GAP) + (colw - c.width) // 2
        d.rectangle((x - 1, y - 1, x + c.width, y + c.height), outline='#B9BCC2')
        sheet.paste(c, (x, y))
    y += h + GAP
sheet.save(os.path.join(OUT, '_hepsi.png'))
print(sheet.size)
