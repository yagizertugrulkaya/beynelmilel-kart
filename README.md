# beynelmilel-kart

Beynelmilel dijital kartvizit — QR ile açılan tek sayfa (TR + EN). Sıfır bağımlılık, statik HTML.
Yayın: GitHub Pages (`main` dalı, `/docs` klasörü) → https://beynelmilel.org/

## Klasörler
- `kaynak/` — düzenlenen kaynak: `index.html` (TR), `en/index.html` (EN), `assets/`, `yagiz-ertugrul-kaya.vcf`, `icerik.md` (metinlerin kaynak etiketli tek listesi)
- `docs/` — ÜRETİLEN yayın klasörü (elle düzenleme; `site-build.py` her seferinde siler ve yeniden yazar)
- `tools/` — `site-build.py` (yayın üretici), `qr-uret.py` (QR)
- `qr/` — kalıcı QR (`.svg` matbaa, `.png` dijital); `qr/_test/` test QR'ları (BASMA)
- `tasarim/` — varyant önizlemesi ve QA ekran görüntüleri

## Değişiklik yayınlama (4 adım)
1. `kaynak/index.html` ve `kaynak/en/index.html` düzenle (metin kaynağı: `kaynak/icerik.md`).
2. `python tools/site-build.py beynelmilel.org`
3. `$env:Path += ";C:\Program Files\nodejs"; python C:\Users\Admin\epot-muhendislik\tools\dogrula.py docs/index.html docs/en/index.html` → iki satır `OK`
4. `git add -A; git commit -m "..."; git push` → Pages 1-2 dakikada yayınlar.

## Kalıcı QR
`python tools/qr-uret.py https://beynelmilel.org/ beynelmilel-org` — yalnız domain canlı ve HTTPS doğrulanmışken. Baskı: en az 2×2 cm, 4 modül beyaz kenar.
