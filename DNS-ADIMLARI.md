# beynelmilel.org → GitHub Pages DNS adımları (Natro paneli)

Kaynak: GitHub Docs "Managing a custom domain for your GitHub Pages site" (2026-09-25'te teyit edildi).

## A) Önce domain doğrulama (takeover'a karşı, 2 dk)
1. github.com → sağ üst profil → **Settings** → sol menü **Pages** → "Add a domain" → `beynelmilel.org` → Add.
2. GitHub bir TXT kaydı verir: ad `_github-pages-challenge-yagizertugrulkaya`, değer uzun bir kod.
3. Natro DNS'e bu TXT kaydını ekle → GitHub sayfasında **Verify**.

## B0) Natro engeli (2026-09-25 tespit)
Natro, hosting'siz domainde kayıt düzenlemeyi ücretli "DNS Hizmeti" (0,10 $/ay) ile açıyor. Mevcut durum: NS = ns1/ns2.natrohost.com, A = 85.159.66.93 (park), www → redirect.natrocdn.com.
Seçenekler: (a) Natro'da "Siparişe Ekle" ile DNS hizmetini al → B) tablosunu Natro'da gir; (b) **ÖNERİLEN: Cloudflare (ücretsiz)** → cloudflare.com → Add a domain → beynelmilel.org → Free → taranan park kayıtlarını sil → B) tablosunu gir (Proxy: **DNS only / gri bulut**) → Cloudflare'in verdiği 2 nameserver'ı Natro'da "Nameserver değiştir" ile kaydet (ücretsiz). Yayılma 15 dk – birkaç saat.

## B) DNS kayıtları (Natro DNS paneli veya Cloudflare)
| Tür | Ad / Host | Değer | TTL |
|---|---|---|---|
| A | `@` | `185.199.108.153` | 3600 |
| A | `@` | `185.199.109.153` | 3600 |
| A | `@` | `185.199.110.153` | 3600 |
| A | `@` | `185.199.111.153` | 3600 |
| AAAA (isteğe bağlı) | `@` | `2606:50c0:8000::153` | 3600 |
| AAAA (isteğe bağlı) | `@` | `2606:50c0:8001::153` | 3600 |
| AAAA (isteğe bağlı) | `@` | `2606:50c0:8002::153` | 3600 |
| AAAA (isteğe bağlı) | `@` | `2606:50c0:8003::153` | 3600 |
| CNAME | `www` | `yagizertugrulkaya.github.io` | 3600 |

Notlar:
- Natro'nun varsayılan "park" A kaydı varsa SİL; `@` için yalnız yukarıdaki A kayıtları kalsın.
- MX/TXT (e-posta) kayıtlarına dokunma.
- Yayılma 5 dk – birkaç saat. Kontrol: `nslookup beynelmilel.org` dört A kaydını göstermeli.

## C) Sonrası (Claude yapar)
- `python tools/site-build.py beynelmilel.org` → `docs/CNAME` oluşur → push.
- `gh api -X PUT repos/yagizertugrulkaya/beynelmilel-kart/pages -f cname=beynelmilel.org` → sertifika (Let's Encrypt) otomatik, "Enforce HTTPS" 24 saate kadar sürebilir.
- Yeşil olunca kalıcı QR üretilir (`tools/qr-uret.py https://beynelmilel.org/ beynelmilel-org`).
