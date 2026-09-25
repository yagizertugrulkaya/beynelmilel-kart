"""QR üretici (segno, saf Python). Kullanım:
    python tools/qr-uret.py <url> <cikti-adi> [--logo]
Çıktı: qr/<cikti-adi>.svg (vektör, matbaa) + qr/<cikti-adi>.png (~1500px, dijital).
Varsayılan hata düzeltme Q; --logo ile H (ortaya logo yerleştirmek için pay bırakır; logo ayrıca yerleştirilir).
Kalıcı QR yalnız https://beynelmilel.org/ canlı + doğrulanmış olunca üretilir (KARARLAR.md #9)."""
import os, sys
import segno

if len(sys.argv) < 3:
    sys.exit(__doc__)
url, name = sys.argv[1], sys.argv[2]
err = "h" if "--logo" in sys.argv else "q"
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
outdir = os.path.join(root, "qr", "_test") if name.upper().startswith("TEST") else os.path.join(root, "qr")
os.makedirs(outdir, exist_ok=True)

qr = segno.make(url, error=err, micro=False)
svg = os.path.join(outdir, name + ".svg")
png = os.path.join(outdir, name + ".png")
qr.save(svg, scale=10, border=4, dark="#17181A", light="#FFFFFF")
qr.save(png, scale=40, border=4, dark="#17181A", light="#FFFFFF")
print("url      :", url)
print("version  :", qr.version, "| error:", qr.error, "| moduller:", qr.symbol_size()[0], "x", qr.symbol_size()[1])
print("svg      :", svg)
print("png      :", png, "(%dpx)" % (qr.symbol_size(scale=40, border=4)[0]))
print("baski    : min 2 cm x 2 cm, 4 modul beyaz kenar (quiet zone) korunmali")
