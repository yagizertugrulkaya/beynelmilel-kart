# Tasarım yönleri — Beynelmilel dijital kartvizit (2026-09-25)

Önizleme: `tasarim-onizleme.html`. Üstteki sekmelerle geçiş yapılır. `#v1`, `#v2` ve `#v3` ile doğrudan açılabilir. "Telefon 412" düğmesi aynı sayfayı telefon genişliğinde gösterir; düzen container query kullandığı için bu görünüm gerçek mobil düzendir.
Her varyantta ilk ekran, "Ne yapıyoruz" ve "Yaptığımız işler" bölümleri `kaynak/icerik.md` metniyle birebir yer alıyor. Kalan bölümler seçilen dilde ikinci turda yapılacak.

Ortak kurallar:
- Hareket token'ları pilates variant-4'ten alındı: `--d1..d4` (160–560ms) ve `--eo` expo-out.
- Kaydırmada görünme `.rv → .in` ile ve IntersectionObserver üzerinden çalışıyor, 60–80ms kademeyle.
- `no-js` sınıfı var. JS kapalıyken bütün içerik görünür.
- `prefers-reduced-motion` bloğu var.
- Yalnız transform ve opacity anime ediliyor.
- Fontlar yerel woff2 olarak yükleniyor (`kaynak/assets/fonts/`, latin + latin-ext, `unicode-range`, `font-display: swap`).

---

## 1 · Yaldız Kart

- **Tez:** QR'ı okutan kişi elindeki basılı kartın dijital ikizini görür. Kart, sayfanın üstünde duran bir nesne olarak tasarlandı: arkasında lacivert ikinci kart, kenarında bronz sıcak baskı yaldızı var. Bronzun "yalnız ince vurgu" kuralı burada fiziksel bir gerekçeye dayanıyor: kartvizitteki yaldız çizgisi. Masaüstünde kart sol rayda sabit kalır, içerik yanından akar. Tam ajans sitesinde bu ray kimlik sütunu olur.
- **Font:** Instrument Sans, değişken (wdth 75–100, wght 400–700), tek aile. Ad ve başlıklar dar kesimle (%84–88), gövde normal genişlikte. Lisans SIL OFL 1.1, kaynak Google Fonts (gstatic).
- **Palet:** #F6F4F1 zemin · #FDFCFA kart · #17181A mürekkep · #55565B ikincil · #1F3864 lacivert (CTA, arka kart) · #8A6D2F bronz (yalnız yaldız çizgisi ve Reklamcılık madde işaretleri) · #DCD7CF ayraç.
- **Hareket:** Kart hafif bir eğimle masaya bırakılır gibi yerine oturur (rotateX, 560ms). Arka kart yelpaze gibi açılır ve yaldızdan bir kez ışık geçer. Bölümler sakin yükselir. İş görselleri, destekleyen tarayıcıda `animation-timeline: view()` ile kaydırmaya bağlı; uygulama-içi tarayıcıda `.rv/.in` yedeğine düşer. Masaüstünde kart imlece ±5° eğilir (rAF).
- **Durum etiketleri:** Yayında ve Canlı lacivert zeminli, dolu noktalı; Yakında ve hazırlanıyor çerçeveli, boş noktalı. Konsept çalışması kesik bronz çerçeveli, köşeli ve noktasız; görseli de kesik çerçeveli "paspartu" içinde duruyor.
- **Güçlü:** En kolay büyüyen yön (sol ray + içerik iskeleti). "Kartvizit" vaadini birebir karşılıyor. Sakin, güven veriyor.
- **Zayıf:** Üçü arasında en az sürprizli olanı. Kart nesnesi iyi işçilik ister; kaba uygulanırsa "skeuomorfik oyuncak" gibi durabilir.
- **Uyar:** Kurumsal, muhafazakâr KOBİ sahibi. Aynı sayfayı yabancı bağlantılara da göstermek isteyen kullanıcı.

## 2 · Sohbet

- **Tez:** Hedef kitle sayfayı zaten WhatsApp'ın ya da Instagram'ın içinden açıyor. Sayfa da onların her gün kullandığı arayüzün dilini konuşur: profil başlığı, mesaj baloncukları, bağlantı önizlemeleri (referanslar ekran görüntüsü + başlık + alan adı biçiminde). Ana buton ekrandan çıkınca alttan bir yazma çubuğu gelir ve doğrudan wa.me'ye açılır. Böylece amaç olan WhatsApp'a yazmak, sayfanın doğal devamı hâline gelir.
- **Font:** Atkinson Hyperlegible Next + Atkinson Hyperlegible Mono (alan adları için). Aile, Braille Institute tarafından az gören okurlar için tasarlandı; 40–60 yaş ve küçük ekran için gerekçesi var. Lisans SIL OFL 1.1, kaynak Google Fonts.
- **Palet:** #F7F7F4 zemin · #FFFFFF baloncuk · #17181A mürekkep · #4E5057 ikincil · #1F3864 lacivert (CTA, gönder düğmesi, başlıklar) · #0E1F33 rozet · #8A6D2F bronz (yalnız bölüm çipinin ince çerçevesi). WhatsApp yeşili bilinçli olarak kullanılmadı; marka taklidi olmaması için lacivert kaldı.
- **Hareket:** Üç nokta kısa bir an "yazıyor" görünür (320ms), ardından baloncuk hafifçe yaylanarak açılır (spring bezier). Kaydırdıkça baloncuklar sırayla, küçük bir sekmeyle düşer. Yazma çubuğu hem girişte hem çıkışta animasyonlu.
- **Durum etiketleri:** Gerçek işler düz beyaz baloncukta, noktalı etiketle. Konsept çalışmaları kesik bronz çerçeveli ve zeminsiz "taslak" baloncukta.
- **Güçlü:** Dönüşüm odaklı. Kitleye en tanıdık arayüz bu. En büyük okuma puntosu burada (18px gövde). İmza öğesi, yani yazma çubuğu, doğrudan işe yarıyor.
- **Zayıf:** Tam ajans sitesine büyürken metafor zorlanır; hizmet ve vaka sayfalarında sohbet dilinin gevşetilmesi gerekir. Masaüstünde dar sütun boş görünebilir.
- **Uyar:** "30 saniyede WhatsApp'a bastırmak" hedefi birinci öncelikse.

## 3 · Kaşe

- **Tez:** Türkiye'de işletme sahibinin güvendiği işaret kaşedir: faturanın, sözleşmenin, irsaliyenin altındaki mühür. Kart, lacivert mürekkepli çift çerçeveli bir firma kaşesi olarak basılır. Yayındaki işler köşelerine "onay kaşesi" alır (Yayında ve Canlı dolu, Yakında ve Yayına hazırlanıyor çerçeveli). Konsept çalışmaları kaşesizdir; kesik çizgili bir taslak notuyla ayrılır ve bu fark içeriğin gerçek durumunu kodlar. Hizmetler form alanları gibi, başlık çerçeveyi kesen etiket biçiminde duruyor.
- **Font:** Bitter (slab serif; evrak, resmî belge ve daktilo çağrışımı) + Public Sans (nötr form gövdesi). İkisinin de lisansı SIL OFL 1.1, kaynak Google Fonts.
- **Palet:** #F6F4F1 kâğıt · #FFFFFF evrak · #1F3864 kaşe mürekkebi · #17181A mürekkep · #505259 ikincil · #8A6D2F bronz (yalnız taslak notu ve konsept görsel çerçevesi) · #C5CBD6 alan çerçevesi.
- **Hareket:** Kaşe hızlanarak kâğıda iner ve küçük bir sekmeyle oturur (320ms; ease-in, ardından expo-out). İş kartlarındaki kaşeler görünür oldukları anda aynı tok vuruşla basılır. Geri kalan her şey kısa ve sert (240–280ms).
- **Güçlü:** Kitleye en yerel ve en akılda kalan yön. Durum etiketlerine anlam yükleyen tek varyant bu. Kişisel ve samimi, ama kurumsal güveni de taşıyor.
- **Zayıf:** Kaşe metaforu fazla tekrarlanırsa oyuncaklaşır; tam sitede yalnızca kimlik ve onay anlarında kullanılmalı. Slab serif, uluslararası bağlantılara biraz "yerel" okunabilir.
- **Uyar:** Bursa'daki üretici ve sanayici KOBİ sahibi (EPOT, Akademika, AY Plastik profili).

---

## Font dosyaları (`kaynak/assets/fonts/`)

| Dosya | Boyut |
|---|---|
| instrumentsans-latin.woff2 / -latin-ext.woff2 | 57.3 KB / 18.9 KB |
| atkinsonnext-latin.woff2 / -latin-ext.woff2 | 34.0 KB / 19.1 KB |
| atkinsonmono-latin.woff2 / -latin-ext.woff2 | 17.8 KB / 10.7 KB |
| bitter-latin.woff2 / -latin-ext.woff2 | 34.1 KB / 32.7 KB |
| publicsans-latin.woff2 / -latin-ext.woff2 | 26.8 KB / 18.5 KB |

Seçim yapılınca kullanılmayan aileler silinecek.

## Not
`yagiz-ertugrul-kaya.vcf` yalnızca önizlemedeki "Rehbere ekle" bağlantısı kırık kalmasın diye `tasarim/` altına kondu. Final aşamada `docs/` köküne taşınacak.
