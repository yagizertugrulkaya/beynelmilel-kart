# _hepsi.png: üç mockup alt alta, altlarında varyant adı.
from PIL import Image, ImageDraw, ImageFont
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = [('A', 'A · Monogram Kabartma'), ('B', 'B · Bronz Çizgi'), ('C', 'C · Yalnız İsim (yalnız isim + QR)')]
ims = [Image.open(os.path.join(OUT, f'mockup-{v}.png')).convert('RGB') for v, _ in rows]
LABEL = 90
W = max(i.width for i in ims); H = sum(i.height + LABEL for i in ims)
sheet = Image.new('RGB', (W, H), '#1E1E1C')
d = ImageDraw.Draw(sheet)
try: font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 34)
except OSError: font = ImageFont.load_default()
y = 0
for (v, name), im in zip(rows, ims):
    sheet.paste(im, (0, y)); y += im.height
    d.text((48, y + 26), name, fill='#D9D6CE', font=font); y += LABEL
sheet.save(os.path.join(OUT, '_hepsi.png'))
print(sheet.size)
