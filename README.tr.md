<div align="center">

# V E K T R A

**BYD gösterge paneliniz, sizin tarzınızda.**

BYD DiLink 3 araçlarda direksiyon arkasındaki ekran için özel gösterge paneli.

**SÜRÜM 2.4.9** · yayın tarihi 9 Kasım 2026 · 47.1 MB

[**Uygulamayı indir**](https://giino01.github.io/Vektra/Vektra-2.4.9.apk) · [**Proje sayfası**](https://giino01.github.io/Vektra/)

[Français](README.md) · [English](README.en.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · **Türkçe**

</div>

---

## Genel bakış

![Mavi ortamda gösterge](img/combine-normal.png)

Soldan sağa: tarih, 220 km/s'e kadar bölümlenmiş **ibreli hız göstergesi**, hangi uygulama çalarsa çalsın **çalan parça**, moda göre seçilen üç değer, batarya boşalırken kırmızı sağa, dolarken yeşil sola giden **enerji akış çizgisi**, ardından **hareketli hava durumu** ve dört **lastiğin basıncı** (bar).

![Kırmızı ortamda gösterge, Sport modu](img/combine-sport.png)

Sport modunda ortam kırmızıya döner, bir `SPORT` rozeti belirir ve alttaki üç değer değişir: tüketim ve batarya yerine güç, motor devri ve gaz pedalı konumu.

> Bu sayfadaki görüntüler her yayında **yayınlanan sürümün kodu tarafından çizilir**, örnek değerlerle. Dolayısıyla burada sunulandan eski bir sürümü gösteremezler.

## Temalar

**Tema** tuşu **Theme Store**'u açar ve yüklü temalar arasında geçiş yapar. **Carbone 3D** yerleşik varsayılan, **VektraUI** diğer yerleşik temadır; **Aston** teması tek dokunuşla indirilir. Seçim hatırlanır ve açılışta geri gelir.

![Aynı tema açık arka planda](img/clair-theme-vektraui.png)

Her tema koyu ve açık olarak vardır. Açık arka plan, fotoğraf üzerinden ölçülen BYD arayüzünün mavi-grisini alır; böylece uygulama üstüne oturmak yerine içine karışır. **Görünüm** ayarı birini, diğerini seçer ya da tableti izler.

## Gerekenler

- Otomatik olarak algılanan **DiLink 3.0 (13.1.32 ve 13.1.33), DiLink 4.0 veya DiLink 5.0 / 5.1 donanımlı bir BYD**.
- Tablet, **dışarıdan uygulama kurulumunu** kabul etmelidir (sideload).
- Tablette **ağ üzerinden ADB hata ayıklama** etkin, 5555 numaralı bağlantı noktası. VEKTRA buna tabletin kendi üzerinden yerel olarak bağlanır — araçtan hiçbir şey dışarı çıkmaz.
- Hava durumu ve güncellemeler için tablette internet bağlantısı. Geri kalan her şey çevrimdışı çalışır.

**Neden ADB.** Gösterge ekranını serbest bırakan komutlara yalnızca Android'in `shell` kullanıcısı yetkilidir. Sıradan bir uygulama bunları gönderemez. VEKTRA bu nedenle bu yetkiyi almak için tabletin kendi ADB'sini yerel olarak kullanır.

## Kurulum

1. Uygulama dosyasını bu sayfadan tablete indirin.
2. Açın ve kurulumu onaylayın. Android reddederse kullandığınız dosya yöneticisi için "bilinmeyen kaynaklar"a izin verin.
3. VEKTRA'yı açın. İlk açılışta karşılama ekranı önce dili, sonra araç modelinizi sorar.
4. Dilini, ardından modelini seç; her adımda **Devam**'a dokun. Ana ekran açılır.
5. Gönderilen ilk komut **"USB hata ayıklamaya izin verilsin mi?"** sorusunu getirir. **Her zaman izin ver**'i işaretleyip onaylayın. Bu yalnızca bir kez çıkar.

![Karşılama ekranı ve dil seçimi](img/accueil-langue.png)

On dil mevcut: Fransızca, İngilizce, Felemenkçe, Almanca, İspanyolca, İtalyanca, Brezilya Portekizcesi, Arapça, Türkçe ve Çince.

## Göstergeyi açmak

1. **Kontrol** bölümünde **Denetle · ADB ve tanılama**'ya dokunun. Hata ayıklama iznini bu tetikler ve bağlantının çalıştığını doğrular.
2. **Gösterge**'ye dönün ve **Göstergede göster**'e dokunun.
3. Fabrika göstergesi uykuya geçer, sanal gösterge ekranı oluşturulur, ardından VEKTRA orada görünür. İşlem yaklaşık on saniye sürer.
4. Tabletin ortasındaki önizleme, direksiyon arkasında çizileni canlı gösterir. **Önizleme** düğmesi, durum tablosunu tercih ederseniz bunu kapatır.

**Geri dönmek için** **Özgün haline döndür**'e dokunun: BYD göstergesi yeniden devralır. Dönmezse kontağı kapatıp açın.

## Sol şerit

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

## Yenilikler: 2.4.9

- Correctif : suppression du double basculement (décochage puis recochage immédiat) du Switch de VEKTRA dans l'application native BYD (com.byd.appstartmanagement) grâce à une action unique par étape avec temporisation anti-rebond de 950 ms et vérification d'état stable avant fermeture.
- Correctif : activation matérielle complète des positions mémoire 1, 2 et 3 du siège conducteur ainsi que du Mode Repos / Mode Conduite (déclaration des permissions BYDAUTO_SEAT_*, BYDAUTO_CHAIR_* et BYDAUTO_COMFORT_* dans le Manifest, chargement des JAR framework BYD sous UID 2000 et invocation multi-contrôleurs Setting / Bodywork / Seat / Chair / Comfort).
- Correctif : suppression du blocage sur l'écran de chargement du widget Application sur le combiné et dans l'Aperçu (correction de l'arrêt prématuré du démon AdbVirtualDisplayDaemon, lancement automatique dès la sélection d'une application, et capture de secours matérielle screencap -d pour les applications OpenGL/SurfaceView comme Waze ou Google Maps).
- Correctif : traduction vocale 100 % native de l'Assistant Vektra et du Copilote dans toutes les langues (italien, anglais, allemand, espagnol, néerlandais, portugais, turc, arabe, chinois) sans phrases françaises résiduelles lorsque la langue de l'interface diffère de la langue vocale de l'Assistant.
- Ajout : thème d'interface « BYD Blade » avec logo officiel BYD vectoriel, carte de présentation avec photo/avatar dans le Profil Conducteur, lecture musicale directe sur YT Music Morphe par commande vocale, et mode « Aperçu : Interaction App » épuré avec injection tactile temps réel et clavier natif BYD.

---

Kişisel bir proje, BYD ile hiçbir bağlantısı yoktur. Kurulum ve kullanım kendi sorumluluğunuzdadır. Gösterilen bilgiler aracın sisteminden gelir ve yanlış olabilir: araç kullanırken asla bunlara güvenmeyin.
