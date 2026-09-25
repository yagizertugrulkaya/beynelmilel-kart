# İçerik — Beynelmilel dijital kartvizit (TR + EN)

Kural: her cümlenin kaynağı köşeli parantezde. Kaynak kısaltmaları:
- `seed` = `C:\Users\Admin\beynelmilel-agency\src\lib\seed\seed-data.ts`
- `plan90` = `studia\00_Inbox\Plan - 90 Gun Gelir Plani - 2026-09-07.md`
- `ozet*` = `studia\ozet*.md`
- `dataroom` = `Masaüstü\Beynelmilel Yatırımcı Sunumu\data-room\`
- `kullanıcı` = 2026-09-25 oturumunda kullanıcı cevabı

---

## 1. Kart (ilk ekran, kaydırmadan görünür)

| Alan | TR | EN | Kaynak |
|---|---|---|---|
| Ad | Yağız Ertuğrul Kaya | Yağız Ertuğrul Kaya | IP Devir Beyanı:13 |
| Unvan | Yazılım Geliştirici & Kurucu · Beynelmilel | Software Developer & Founder · Beynelmilel | kullanıcı |
| Konum | Bursa, Türkiye | Bursa, Türkiye | plan90:35 |
| Tek cümle | İşletmeniz için sistem, web sitesi ve reklam — kendi ürünlerimizi kurduğumuz özenle. | Systems, websites and advertising for your business — built with the care we give our own products. | kullanıcı seçimi "A", 2026-09-25 (önceki "Ara sıra sizinkini de" müşteriyi arka plana atıyordu) |

Butonlar (sıra önemli — WhatsApp birincil):

| Buton | TR etiket | EN etiket | href |
|---|---|---|---|
| WhatsApp | WhatsApp'tan yaz | Message on WhatsApp | `https://wa.me/905334765595` |
| E-posta | E-posta gönder | Send an e-mail | `mailto:yagizkaya43@gmail.com` |
| Rehber | Rehbere ekle | Save contact | `yagiz-ertugrul-kaya.vcf` (TR) / `../yagiz-ertugrul-kaya.vcf` (EN) |
| Instagram | Instagram | Instagram | `https://www.instagram.com/yagizertugrulkaya/` |
| LinkedIn | LinkedIn | LinkedIn | `https://www.linkedin.com/in/ya%C4%9F%C4%B1z-ertu%C4%9Frul-kaya-4b47281bb/` |

Dil anahtarı: `TR · EN` (aktif olan `aria-current="page"`). TR sayfada EN linki `en/`, EN sayfada TR linki `../`.

---

## 2. Beynelmilel ne yapar

**TR**
Beynelmilel, Bursa'dan çalışan bir yazılım stüdyosu ve ajans. [seed:556 "Türkiye'den çalışan" → Bursa: plan90:35]
Sattığımız her şeyi önce kendimiz için kurduk: pilates stüdyoları için yönetim sistemi kurarken çok kiracılı mimariyi, Erasmus öğrencileri için sosyal ağ kurarken moderasyon ve veri güvenliğini, yapay zekâ ürünleri kurarken maliyet-performans dengesini kendi paramızla öğrendik. [seed:556-558]
Müşteri işine bu birikimle geliriz. [seed:558]

Üç ilke (kısa başlık + tek cümle):
- **Her işe tam sorumluluk.** Evet dediğimiz işe tasarımdan yayına uçtan uca sahip çıkarız. [seed:562 uyarlaması — "az proje / az işe evet deriz" müşteriyi geri plana attığı için çıkarıldı, kullanıcı 2026-09-25]
- **Güvenlik sonradan eklenmez.** Satır bazlı erişim denetimi ve ayrık yetki tabloları her projenin sıfırıncı gününde vardır. [seed:563 — "düzenli sızma testleri" ifadesi kanıtsız olduğu için çıkarıldı]
- **Canlıya kadar.** Tasarım dosyası değil, yayında çalışan ürün teslim ederiz. [seed:564]

**EN**
Beynelmilel is a software studio and agency working from Bursa, Türkiye. [seed:571]
Everything we sell, we first built for ourselves: we learned multi-tenant architecture building a management system for Pilates studios, moderation and data safety building a social network for Erasmus students, and cost-performance trade-offs building AI products — all with our own money. [seed:573]
We arrive at client work carrying that experience. [seed:573]

- **Full responsibility for every project.** What we say yes to, we own end-to-end — from design to launch. [seed:577 uyarlaması]
- **Security is not an add-on.** Row-level access control and separated privilege tables exist from day zero of every project. [seed:578, pentest ifadesi çıkarıldı]
- **All the way to production.** We deliver products that run in production — not design files. [seed:579]

---

## 3. Hizmetler (fiyat YOK)

Bölüm üst başlığı — TR: "Ne yapıyoruz" · EN: "What we do"
Bölüm alt cümlesi — TR: "Her türlü sistem ve profesyonel web sitesi; reklamı da biz yapıyoruz." [kullanıcı] · EN: "Any kind of system or professional website; we run the advertising too."

| # | TR başlık | TR açıklama | EN başlık | EN açıklama | Kaynak |
|---|---|---|---|---|---|
| 1 | Sistemler & SaaS | İşletmenize özel yönetim sistemi: üyeler, randevu, ödeme, personel — tek panelde. WhatsApp randevu botu: menü, 24 saat ve 2 saat önce hatırlatma, iptal, yönetim paneli. | Systems & SaaS | Custom management systems for your business: members, appointments, payments, staff — in one panel. WhatsApp booking bot: menu, 24-hour and 2-hour reminders, cancellations, admin panel. | plan90:163-164; seed:410 |
| 2 | Profesyonel web sitesi | Vitrin site: 4-6 sayfa, mobil uyumlu, temel SEO, KVKK ve çerez metinleri. Vitrin+: İngilizce/Almanca, ürün kataloğu, teklif formu, Google Business kaydı. | Professional websites | Showcase site: 4-6 pages, mobile-first, baseline SEO, privacy and cookie texts. Showcase+: English/German, product catalogue, quote form, Google Business listing. | plan90:161-162 |
| 3 | Reklamcılık | Sosyal medya yönetimi · Meta ve Google reklamları · Reklam kreatifi (görsel ve video) · Google Business ve yerel SEO. | Advertising | Social media management · Meta and Google Ads · Ad creative (visuals and video) · Google Business and local SEO. | kullanıcı |
| 4 | Bakım & denetim | Bakım: güncelleme, yedek, izleme. Teknik denetim: güvenlik ve KVKK teknik raporu. | Maintenance & audit | Maintenance: updates, backups, monitoring. Technical audit: security and data-protection (KVKK/GDPR) technical report. | plan90:165-166 |

---

## 4. FlowDesk vitrini

| Alan | TR | EN | Kaynak |
|---|---|---|---|
| Ad | FlowDesk | FlowDesk | ozetflowdesk |
| Slogan | Klinikten fabrikaya: tek çatı altında işletme yönetimi. | From clinic to factory: business management under one roof. | seed:406-407 |
| Özet | Klinik, stüdyo, oto yıkama ve atölye gibi randevulu işletmelerin ortak ihtiyaçlarını tek platformda toplayan çok kiracılı yönetim çatısı. Studia'da kanıtlanan desenlerin genelleştirilmiş hâli. | A multi-tenant management umbrella that unifies the shared needs of appointment-based businesses — clinics, studios, car washes, workshops. The generalised form of patterns proven in Studia. | seed:410-411 |
| Nasıl | Her sektöre ayrı yazılım yazmak yerine ortak omurgayı bir kez ve doğru yazmak: üyeler, takvim, ödeme, personel. Sektör farkları modül olarak eklenir. | Instead of separate software per industry, the shared backbone is written once and correctly: members, calendar, payments, staff. Industry differences plug in as modules. | seed:415-416 |
| Kanıt satırı | 98 veritabanı testi + 49 birim testi yeşil · KVKK/GDPR paketi: veri dışa aktarma, silme hakkı, rıza akışı | 98 database tests + 49 unit tests green · KVKK/GDPR toolkit: data export, right to erasure, consent flow | ozetflowdesk:141-148 |
| Dikeyler | Klinik · Stüdyo · Fabrika · Oto yıkama | Clinic · Studio · Factory · Car wash | ozetflowdesk:119-121 |
| Linkler | Tanıtım: `https://flowdesksolutions.com` · Uygulama: `https://app.flowdesksolutions.com` | same | ozetflowdesk:123-128 |
| Logo | `assets/flowdesk-mark-indigo.svg` (açık zemin) · marka indigo #3A34C9 | | flowdesk-logo/OKU.txt |
| Görsel | `assets/flowdesk.webp` (1200×750 ekran görüntüsü, kırpma yok) | | Yatırımcı Sunumu/assets |

---

## 5. Referanslar (müşteri işleri)

Bölüm başlığı — TR: "Yaptığımız işler" · EN: "Work we delivered"

| Proje | TR tanım | EN tanım | Durum TR / EN | Link | Görsel | Kaynak |
|---|---|---|---|---|---|---|
| Yağız Lastik Sanayi | Bursa'dan dünyaya üreten bir fabrika için üç dilli (TR/EN/DE) kurumsal site. Framework yok, bağımlılık yok, kırılacak parça yok. | A trilingual (TR/EN/DE) corporate site for a factory manufacturing from Bursa to the world. No framework, no dependencies, nothing to break. | Yayında / Live | `https://yagizlastik.com` | `assets/yagizlastik.webp` | seed:308-320; ozetyagizlastik |
| Studia | Pilates stüdyoları için uçtan uca yönetim: üyeler, ders programı, yoklama, paketler ve taksitli ödemeler tek panelde. İlk stüdyo canlıda ve her gün kullanılıyor. | End-to-end management for Pilates studios: members, class schedules, attendance, packages and instalment payments in one panel. The first studio is live and uses it every day. | Canlı / Live | `https://viva-pilates-sigma.vercel.app` | `assets/studia.webp` | seed:53-58 |
| AY Plastik | 1976'dan beri plastik ambalaj üreten Bursa fabrikası için TR+EN kurumsal site; 32 sayfa, ürün künyeleri. | A TR+EN corporate site for a Bursa plastics-packaging factory founded in 1976; 32 pages with product specifications. | Yayına hazırlanıyor / Launching | `https://ayplastik.vercel.app` | `assets/ayplastik.webp` | ozetayplastik:3,15 |
| Pilates Ebru Coşar | Nilüfer'deki reformer stüdyosu için tek sayfa tanıtım sitesi. | A one-page showcase site for a reformer studio in Nilüfer, Bursa. | Yakında / Coming soon | `https://pilates-ebru-cosar.vercel.app` | `assets/pilatesebrucosar.webp` | ozetpilatesebrucosar:11-16 |
| Astro Marin | Doğum haritasından astrokartografiye, tam kapsamlı astroloji platformu. | A full-scope astrology platform, from natal charts to astrocartography. | Canlı / Live | `https://astromarin-app.vercel.app` | `assets/astro.webp` | seed:251-252; ozetastromarin |
| EPOT Mühendislik | 1980'den beri harmonik filtreli kompanzasyon üreten Bursa firması için altı tasarım konsepti. | Six design concepts for a Bursa company that has built harmonic-filtered compensation panels since 1980. | Konsept çalışması / Concept study | `https://epot-tasarim-onerileri.vercel.app` | `assets/epot.webp` | ozetepot:10-16 |

---

## 6. Kendi ürünlerimiz

Bölüm başlığı — TR: "Kendi ürünlerimiz" · EN: "Our own products"
Alt cümle — TR: "Kendi paramızla, kendi adımızla canlıya taşıdıklarımız." [seed:541] · EN: "Taken live with our own money and our own name on them." [seed:544]

| Ürün | TR | EN | Link | Kaynak |
|---|---|---|---|---|
| FlowDesk | Klinikten fabrikaya: tek çatı altında işletme yönetimi. | From clinic to factory: business management under one roof. | `https://flowdesksolutions.com` | seed:406 |
| Solavoy | Nereye ve kaç parayla — gerisini Solavoy planlar. Sekiz dilde yapay zekâ destekli seyahat planlayıcı. | Where to, on what budget — Solavoy plans the rest. An AI-assisted travel planner in eight languages. | `https://www.solavoy.com` | seed:164-165; ozetsolavoy:8 |
| Erasocial | Erasmus öğrencileri, aynı şehirde buluşuyor. | Erasmus students, meeting in the same city. | `https://erasocial.vercel.app` | seed:111-112 |
| Sanayi AI | Türk sanayicisinin yapay zekâ masası. | The Turkish manufacturer's AI desk. | `https://sanayiaiapp.com` | seed:208-209 |
| Bütçem | Banka bağlantısı yok, sürpriz yok: bilinçli bütçe. | No bank connection, no surprises: mindful budgeting. | `https://butcem-three.vercel.app` | seed:347-348 |

### 6b. Atölyede (henüz yayında olmayan kendi işlerimiz — LİNKSİZ kartlar, "Geliştirmede / In development" etiketi)

Alt başlık — TR: "Atölyede" · EN: "In the workshop"
Alt cümle — TR: "Henüz yayında olmayan, masamızda büyüyen işler." [kullanıcı 2026-09-25: tüm projeler görünsün] · EN: "Not yet public — growing on our desk."

| Proje | TR | EN | Kaynak |
|---|---|---|---|
| djmix | Masaüstü DJ kurulumu ve Auto-Mix motoru: şarkı adlarını yaz, DJ kalitesinde mix al. Canlı Auto DJ, efekt, loop, MIDI. | Desktop DJ setup with an Auto-Mix engine: type the track names, get a DJ-grade mix. Live Auto DJ, FX, loops, MIDI. | INDEX:36 |
| Oto Yıkama randevu | Gelmeyen müşteri, kaybolan gündür. Küçük oto yıkamacılar için WhatsApp'tan randevu alan ve otomatik hatırlatma gönderen sistem. | A no-show customer is a lost day. Takes bookings over WhatsApp and sends automatic reminders, built for small car washes. | seed:378, 383-384 |
| snackboxd | Atıştırmalıklar için Letterboxd: 53 bin ürünlük katalog, puan ve yorum. | Letterboxd for snacks: a 53,000-product catalogue with ratings and reviews. | ozetsnackbox:10 |
| Beynelmilel Platform | Bağlantı analizi, coğrafi-zamansal sorgular ve öznitelik tabanlı erişim denetimi sunan veri füzyon platformu. En iddialı Ar-Ge projemiz. | A data-fusion platform with link analysis, geo-temporal queries and attribute-based access control. Our most ambitious R&D project. | seed:437, 442-443 |
| JARVIS | Görevler, projeler, piyasalar ve gerçek bir Claude terminali — tek masaüstü uygulamasında. Kişisel komuta merkezi. | Tasks, projects, markets and a real Claude terminal — in one desktop app. A personal command centre. | seed:493, 498-499 |
| FablePlanGen | Bir proje fikrini alıp yapılandırılmış, uygulanabilir bir derin plana çeviren masaüstü aracı. | A desktop tool that turns a project idea into a structured, actionable deep plan. | seed:517, 522-523 |
| janestreet-sim | Piyasa yapıcılığı, ETF arbitrajı ve istatistiksel arbitrajı sanal parayla deneyip ölçen quant eğitim simülatörü. | A quant training simulator that tests market making, ETF arbitrage and statistical arbitrage with virtual money. | ozetjanestreet:6 |
| CLI ajanlar | Müşteri adayı araştıran, rakip hareketlerini raporlayan ve SEO içeriği üreten üç komut satırı ajanı. | Three command-line agents: lead research, weekly competitor reports, SEO content drafts. | seed:469, 474-475 |

---

## 7. Hakkımda

**TR**
Yağız Ertuğrul Kaya. Bursa'da yaşıyorum; Beynelmilel'i tek başıma kurdum ve yürütüyorum. [dataroom/00-Genel-Bakis-TR.md:12 "1 kurucu"; plan90:35]
Sattığım her şeyi önce kendim için kurdum; bir işi tasarımdan altyapıya, yayından güvenliğe kadar uçtan uca üstlenirim. [seed:543,556]
Yeni bir iş için en hızlı yol WhatsApp. [kullanıcı — birincil CTA]

**EN**
Yağız Ertuğrul Kaya. I live in Bursa, Türkiye; I founded Beynelmilel and run it on my own. [dataroom:12; plan90:35]
Everything I sell, I first built for myself; I take a project end-to-end, from design to infrastructure, from launch to security. [seed:546,571]
For a new project, WhatsApp is the fastest way to reach me. [kullanıcı]

Görsel: portre YOK (şimdilik) → `assets/logo_badge.svg` rozet. [kullanıcı]

---

## 8. İletişim + footer

| Alan | Değer |
|---|---|
| WhatsApp | +90 533 476 55 95 → `https://wa.me/905334765595` |
| E-posta | yagizkaya43@gmail.com |
| Instagram | @yagizertugrulkaya → `https://www.instagram.com/yagizertugrulkaya/` |
| LinkedIn | `https://www.linkedin.com/in/ya%C4%9F%C4%B1z-ertu%C4%9Frul-kaya-4b47281bb/` |
| Konum | Bursa, Türkiye |
| Web | beynelmilel.org |

Bölüm başlığı — TR: "Konuşalım" · EN: "Let's talk"
Bölüm cümlesi — TR: "Bir fikriniz, bir siparişiniz ya da sadece bir sorunuz varsa yazın; aynı gün dönerim." [kullanıcı onayı bekliyor] · EN: "An idea, an order or just a question — write, and I'll reply the same day."

Footer — TR: "© 2026 Beynelmilel · Bursa" · EN: "© 2026 Beynelmilel · Bursa, Türkiye"

---

## Meta (head)

| | TR | EN |
|---|---|---|
| `<title>` | Yağız Ertuğrul Kaya · Beynelmilel — Yazılım, web sitesi ve reklam | Yağız Ertuğrul Kaya · Beynelmilel — Software, websites and advertising |
| description | Bursa'dan çalışan yazılım stüdyosu ve ajans. İşletmenize özel sistemler, profesyonel web siteleri ve reklam yönetimi. FlowDesk, Yağız Lastik, Studia ve diğer işler. | A software studio and agency working from Bursa, Türkiye. Custom systems, professional websites and advertising. FlowDesk, Yağız Lastik, Studia and more. |
| lang | tr | en |
