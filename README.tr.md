<div align="center">

# V E K T R A

**BYD gösterge paneliniz, sizin tarzınızda.**

BYD DiLink 3 araçlarda direksiyon arkasındaki ekran için özel gösterge paneli.

**SÜRÜM 1.8.1** · yayın tarihi 26 Ekim 2026 · 43.0 MB

[**Uygulamayı indir**](https://giino01.github.io/Vektra/Vektra-1.8.1.apk) · [**Proje sayfası**](https://giino01.github.io/Vektra/)

[Français](README.md) · [English](README.en.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · **Türkçe**

</div>

---

## Genel bakış

![Mavi ortamda gösterge](img/combine-normal.png)

Soldan sağa: tarih, 220 km/s'e kadar bölümlenmiş **ibreli hız göstergesi**, hangi uygulama çalarsa çalsın **çalan parça**, moda göre seçilen üç değer, batarya boşalırken kırmızı sağa, dolarken yeşil sola giden **enerji akış çizgisi**, ardından **hareketli hava durumu** ve dört **lastiğin basıncı** (bar).

![Kırmızı ortamda gösterge, Sport modu](img/combine-sport.png)

Sport modunda ortam kırmızıya döner, bir `SPORT` rozeti belirir ve alttaki üç değer değişir: tüketim ve batarya yerine güç, motor devri ve gaz pedalı konumu.

> Bu sayfadaki görüntüler her yayında **yayınlanan sürümün kodu tarafından çizilir**, örnek değerlerle. Dolayısıyla burada sunulandan eski bir sürümü gösteremezler.

## Sekiz tema

**Tema** tuşu sekiz gösterge düzeni arasında geçiş yapar: Karbon, Karbon 3D, Grand Tourer, Enerji akışı, Obsidyen, Kırmızı Spor, Lumen ve Bulutsu. Bir dokunuş sonrakine geçer. Seçim hatırlanır ve açılışta geri gelir.

![Aynı tema açık arka planda](img/clair-theme-hyperos3d.png)

Her tema koyu ve açık olarak vardır. Açık arka plan, fotoğraf üzerinden ölçülen BYD arayüzünün mavi-grisini alır; böylece uygulama üstüne oturmak yerine içine karışır. **Görünüm** ayarı birini, diğerini seçer ya da tableti izler.

## Gerekenler

- **DiLink 3'lü bir BYD** (Android 10). Seal U DM-i üzerinde geliştirildi; diğer DiLink 3 modelleri doğrulanmadı.
- Tablet, **dışarıdan uygulama kurulumunu** kabul etmelidir (sideload).
- Tablette **ağ üzerinden ADB hata ayıklama** etkin, 5555 numaralı bağlantı noktası. VEKTRA buna tabletin kendi üzerinden yerel olarak bağlanır — araçtan hiçbir şey dışarı çıkmaz.
- Hava durumu ve güncellemeler için tablette internet bağlantısı. Geri kalan her şey çevrimdışı çalışır.

**Neden ADB.** Gösterge ekranını serbest bırakan komutlara yalnızca Android'in `shell` kullanıcısı yetkilidir. Sıradan bir uygulama bunları gönderemez. VEKTRA bu nedenle bu yetkiyi almak için tabletin kendi ADB'sini yerel olarak kullanır.

## Kurulum

1. Uygulama dosyasını bu sayfadan tablete indirin.
2. Açın ve kurulumu onaylayın. Android reddederse kullandığınız dosya yöneticisi için "bilinmeyen kaynaklar"a izin verin.
3. VEKTRA'yı açın. İlk açılışta karşılama ekranı dili sorar.
4. **Devam**'a dokunun. Ana ekran açılır.
5. Gönderilen ilk komut **"USB hata ayıklamaya izin verilsin mi?"** sorusunu getirir. **Her zaman izin ver**'i işaretleyip onaylayın. Bu yalnızca bir kez çıkar.

![Karşılama ekranı ve dil seçimi](img/accueil-langue.png)

Altı dil mevcut: Fransızca, İngilizce, İtalyanca, Almanca, Brezilya Portekizcesi ve Türkçe.

## Göstergeyi açmak

1. **Kontrol** bölümünde **Denetle · ADB ve tanılama**'ya dokunun. Hata ayıklama iznini bu tetikler ve bağlantının çalıştığını doğrular.
2. **Gösterge**'ye dönün ve **Göstergede göster**'e dokunun.
3. Fabrika göstergesi uykuya geçer, sanal gösterge ekranı oluşturulur, ardından VEKTRA orada görünür. İşlem yaklaşık on saniye sürer.
4. Tabletin ortasındaki önizleme, direksiyon arkasında çizileni canlı gösterir. **Önizleme** düğmesi, durum tablosunu tercih ederseniz bunu kapatır.

**Geri dönmek için** **Özgün haline döndür**'e dokunun: BYD göstergesi yeniden devralır. Dönmezse kontağı kapatıp açın.

## Dört bölüm

| Bölüm | Ne işe yarar |
| --- | --- |
| **Gösterge** | Canlı önizleme, görüntüleme düğmesi, ekran, mod ve tema seçimi. |
| **Kontrol** | Algılanan donanımın tam dökümü, hepsini kopyalamak için bir düğmeyle. |
| **Günlük** | Gönderilen her komut ve alınan her yanıt. |
| **Ayarlar** | Dil, görünüm, otomatik başlatma, müzik erişimi, güncellemeler, hava durumu. |

![Gösterge](img/tablette-combine.png)

![Ayarlar](img/tablette-reglages.png)

## Müzik

Çalan parçayı göstermek için VEKTRA'nın **bildirim erişimine** ihtiyacı vardır: ses oturumlarını okumak için Android'in kuralı budur. **Bildirim erişimi** satırına dokunun; uygulama bunu mevcut listeden hiçbir şey silmeden ADB üzerinden kendine verir. Verildikten sonra başlık, sanatçı, kapak ve ilerleme, **hangi uygulama çalarsa çalsın** görünür — radyo, Bluetooth ya da kurulu bir uygulama.

## Otomatik başlatma ve durdurma

Bu ayar açıkken VEKTRA, araç çalıştırılır çalıştırılmaz göstergeyi alır ve kapatılır kapatılmaz geri verir. Araç durumu **doğrudan araçtan**, saniyede bir okunur: 0 kapalı, 1 aksesuar, 2 kontak açık. Ekranın geri verilmesi için kapanmanın arka arkaya iki kez doğrulanması gerekir — tek bir kesinti yolda göstergeyi kaybettirmemelidir.

## Görünüm

Koyu, açık veya otomatik — görünüm o zaman tableti izler. Ayar yalnızca göstergeyi ilgilendirir: tablet ekranı her koşulda koyu kalır, orası bir kokpittir.

## Güncelleme

VEKTRA her açılışta kendisi denetler. Bir sürüm mevcut olduğunda bir pencere yenilikleri gösterir ve **Daha sonra** ya da **İndir ve kur** seçeneklerini sunar. Kabul ederseniz uygulama kendini indirir, üzerine kurar ve kendiliğinden yeniden açılır. Tüm sürümler **aynı imzayı** taşır: bir güncelleme, Android reddetmeden ve ayarlar kaybolmadan her zaman öncekinin yerine geçer.

## Bir sorun olursa

- **Gösterge donuk kalıyor.** *Özgün haline döndür*'e dokunup yeniden deneyin. Değişmezse kontağı kapatıp açın.
- **Veri yok, yalnızca tire.** Aracın SDK'sı yanıt vermedi. Kontrol bölümü hangi aygıtlara ulaşılabildiğini söyler.
- **Müzik görünmüyor.** Bildirim erişimi verilmemiş: yukarıya bakın. Ayrıca gerçekten bir şey çaldığını doğrulayın.
- **Güncelleme "Kullanılamıyor" diyor.** Tablet kaynağa ulaşamadı. İnternet bağlantısını denetleyip yeniden deneyin: kesin neden görüntülenir.
- **Başka bir şey.** *Kontrol*'ü açın, *Taramanın tamamını kopyala*'ya dokunun ve metni gönderin. Anlamak için gereken her şeyi içerir.

## Yenilikler: 1.8.1

- Theme Store: sol menüde yeni bölüm, "Tema" tuşuyla da açılır. Karbon 3D yerleşik varsayılan tema olarak kalır; Aston teması önizleme, boyut, ilerleme, Uygula, Güncelle ve Kaldır ile tek dokunuşla indirilir. Her tema kurulmadan önce doğrulanır (Vektra imzası); başka yoldan gelen bir .vektra dosyası "Tema içe aktar" ile de kurulur. Gelecek temalar da aynı yoldan gelecek.
- Vektra 3D harita: tablet tarafından doğrudan çizilen, 3D binalı, aracı kesintisiz izleyen akıcı bir harita. Artık tüm ekranların haritası: "Navigasyon" sekmesi, Karbon 3D Navigasyon widget'ı, Aston teması ve tam gösterge haritası; ok gidilen yolda kalır ve mavi çizgi oktan başlar (geçilen kısım kaybolur). Ayarlar'da yeni "Harita" bölümü: stil, 3D binalar ve yakınlaştırma.
- Aston teması (Theme Store'da): iki gösterge, P R N D vites, uyarı lambaları ve ortada müzik, hava durumu veya harita; tabletten başlatılan bir rota göstergede görünür (sonraki dönüş, mesafe, kalan süre, varış saati, gerçek radarlar).
- Navigasyon: rehberlik artık aracı rota boyunca izler. Sonraki talimat yolculuk ilerledikçe güncellenir, kalan mesafe ve süre rota üzerinde ölçülür, her manevra anons edilir ve varış bildirilir. Rotadan çıkıldığında veya ters yönde gidildiğinde rota aracın gittiği yönde otomatik olarak yeniden hesaplanır. Harita artık her GPS konumunda yavaşlamaz.
- Artık uydurma değer yok: araç verisi yoksa ekranlar demo hız, batarya, lastik basıncı, hız sınırı veya parça yerine "--" gösterir; rotaya eklenen veya sesli anons edilen sahte radarlar kaldırıldı; M veya S vitesi artık "D" olarak gösterilmez.
- Widget ve tema içe aktarma: arka planda okuma (büyük bir dosya ekranı artık dondurmaz), sınırlı boyut, göstergeye göre küçültülen görseller; gerçekten desteklenen biçimler belirtilir (görseller, Vektra .json widget, .json düzen, .zip, .vektra); KWGT, SVG, HTML veya XML widget'ı açıklamayla reddedilir.
- Düzenleme: gizli veya içe aktarılmamış bir widget artık dokunuşları yakalamaz, büyük Navigasyon widget'ı seçimi artık tutmaz, genel yakınlaştırma harita kenarlarına artık iki kez uygulanmaz ve tablet önizlemesinde harita yerinde artık boşluk kalmaz.
- Arayüz: tüm pencereler (ses, ses dili, içe aktarma, değişkenler, güncelleme kaynağı, bağış) ve tüm mesajlar uygulamanın tarzında; klavye adres alanında açılır.
- Gösterge ekranı: otomatik başlatma uygulamayı yeniden başlattığında VEKTRA'nın tam ekranı göstergede kendiliğinden geri gelir (kapalı kalabiliyordu) ve harita yeniden başlatmadan sonra artık kaybolmaz; VektraUI artık üstünde Karbon 3D öğeleri olmadan temiz görüntülenir.

---

Kişisel bir proje, BYD ile hiçbir bağlantısı yoktur. Kurulum ve kullanım kendi sorumluluğunuzdadır. Gösterilen bilgiler aracın sisteminden gelir ve yanlış olabilir: araç kullanırken asla bunlara güvenmeyin.
