# Beynelmilel kartvizit — matbaa notu

Hazırlayan: Yağız Ertuğrul Kaya · +90 533 476 55 95 · yagizkaya43@gmail.com
Tarih: 26.09.2026

## 1. Ölçü

| | Net (kesim) | Taşmalı dosya | Güvenli alan |
|---|---|---|---|
| V1, V3, V4 (yatay) | 85 × 55 mm | 91 × 61 mm | kesimden içeri 4 mm |
| V2 (dikey) | 55 × 85 mm | 61 × 91 mm | kesimden içeri 4 mm |

- Dosyalarda her kenarda **3 mm taşma** var ve dolu. Kesim işareti ya da renk barı **yok**; lütfen kendi montajınızda ekleyin.
- Tüm metinler kesimden en az 4 mm içeride.
- PDF sayfa boyutu Chrome'un nokta yuvarlaması yüzünden 91,02 × 61,04 mm (V2'de 61,04 × 91,02 mm). Fark 0,05 mm'nin altında; merkezden hizalayın.
- Fontlar PDF'e gömülü. Metin ve logo vektör, QR vektör. Dosyalarda raster görsel yok.
- Dosyalar **RGB** olarak hazırlandı. CMYK/spot dönüşümünü aşağıdaki değerlerle yapın ve **ıslak prova ya da renk provası** gönderin.

## 2. Renkler

| Rol | RGB hex | Yaklaşık CMYK | Spot önerisi |
|---|---|---|---|
| Lacivert (çıpa) | #1F3864 | C100 M82 Y31 K20 | Pantone 534 C |
| Bronz (yalnız folyo) | #8A6D2F | C30 M45 Y95 K30 (düz baskı gerekirse) | Sıcak folyo: bronz / antik altın, mat ya da yarı mat (parlak altın değil). Renk kartından seçim yapılacak. |
| Mürekkep (metin, QR) | #17181A | **Yalnız K100** | — |
| İkincil gri (V1) | #565B63 | K75 (tek kanal) | — |
| Kırık beyaz metin (V2) | #F3F2EE | Boşaltma (kağıt beyazı) ya da opak beyaz | — |
| İkincil açık metin (V2) | #BCC4D3 | Boşaltma + C20 M10 ton ya da kağıt beyazı | Sade üretim için beyazla birleştirilebilir |

- **QR ve küçük siyah metin 4 renkli zengin siyah OLMASIN**; tek kanal K100 basılsın (register kayması QR'ı okunmaz yapar).
- V3 ve V4'teki kırık beyaz tonlar **kağıdın kendi rengidir**, baskı değildir. PDF'te zemin beyaz (mürekkepsiz) bırakıldı.

## 3. Varyant bazında üretim

| Varyant | Kağıt | Baskı | Özel işlem |
|---|---|---|---|
| **V1 Künye** (yatay, açık) | 400 g mat kuşe veya 450 g Munken Pure | Ofset 2+2 (lacivert + K) | **Kenar boyama** lacivert (Pantone 534 C). Laminasyon yok. |
| **V2 Gece Mührü** (dikey, koyu) | A) Lacivert boyalı karton (ör. Colorplan Navy, 540 g) veya B) 400 g kuşe + tam lacivert ofset + mat selefon | A) opak beyaz serigrafi, B) boşaltma beyaz | **Yalnız B işareti bronz sıcak folyo.** QR paneli kağıt beyazı ya da çift kat opak beyaz; panelin üstüne başka baskı yok. |
| **V3 Tek Eksen** (yatay, açık) | 600 g %100 pamuklu (Crane Lettra, Gmund Cotton) | **Letterpress 1+1**: ön yüz lacivert, arka yüz siyah | Laminasyon yok. QR için önce deneme baskısı; dolma olursa arka yüz ofset/dijital. |
| **V4 Yalnız İsim** (yatay, açık) | 700–800 g çift katlı (duplex) beyaz pamuklu | Ön: **bronz sıcak folyo** (yalnız isim). Arka: QR ofset/dijital K100 | QR asla folyo ile basılmaz. İnce serif harfler için hassas folyo klişesi. |

Folyo ve letterpress için ayrı spot/kalıp dosyası gerekirse (yalnız folyo katmanı, yalnız mürekkep katmanı) talep üzerine ayrıca verilir; ekteki PDF'ler kompozit görünümdür.

## 4. QR kodu (tüm varyantlarda)

- İçerik: `http://beynelmilel.org/` · hata düzeltme seviyesi **H** · 29 × 29 modül.
- Baskıdaki boyut: **sembol 18,0 mm**, çevresinde 4 modül (2,5 mm) beyaz sessiz alan; toplam 23 mm. **Küçültmeyin.**
- Sessiz alanın içine hiçbir baskı, folyo, lak ya da renk girmesin. Koyu zeminde (V2) QR beyaz panel içinde: panel 29 × 29 mm.
- QR'ın üstüne spot UV, folyo, kabartma ya da gofre **uygulanmasın**; kabartma kart arkasında QR bölgesine denk gelmesin.
- Her arka yüz PNG'si dijital olarak okutuldu ve `http://beynelmilel.org/` döndü. Provada telefonla tekrar okutun.

## 5. Dosya listesi

| Dosya | Açıklama |
|---|---|
| `v1-on.pdf`, `v1-arka.pdf` | V1 Künye, 91 × 61 mm, taşmalı |
| `v2-on.pdf`, `v2-arka.pdf` | V2 Gece Mührü, 61 × 91 mm (dikey), taşmalı |
| `v3-on.pdf`, `v3-arka.pdf` | V3 Tek Eksen, 91 × 61 mm, taşmalı |
| `v4-on.pdf`, `v4-arka.pdf` | V4 Yalnız İsim, 91 × 61 mm, taşmalı |
| `v*-on.png`, `v*-arka.png` | Her yüzün 300 dpi önizlemesi (yalnızca kontrol içindir, baskıya girmez) |
| `_hepsi.png` | Tüm varyantların kesilmiş hâli, tek sayfada |
| `onizleme.html` | Taşma, kesim ve güvenli alan kılavuzlu ekran önizlemesi |

Baskı için yalnız **PDF** dosyalarını kullanın.
