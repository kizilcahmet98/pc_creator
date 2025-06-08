# pc_creator

Bu depo, temel OOP (nesne yönelimli programlama) pratiklerini denemek icin hazirlanmis basit bir **bilgisayar konfigürasyon** uygulamasi içerir. Amaci, sınıf yapısını ve metodlarla bir nesnenin durumunun nasil degistirilebilecegini gormek isteyenlere ornek saglamaktir.

## Dosya Yapisi

1. **`create.py`**
   - `Pc` sinifini tanimlar. Bilgisayar sahibini ve CPU, RAM, GPU, depolama ile PSU gibi bilesenleri saklar.
   - Bilgisayari acma/kapatma (`calistir`, `kapat`) ve donanim bilgilerini degistirme (`cpu_degistir`, `ram_degistir`, `gpu_degistir`, vb.) gibi metotlar icerir.
   - Ornek amacli yazildigi icin girdi/çikti islemlerini `input()` ile dogrudan sinif icinde yapmaz; metotlar parametre alir.

2. **`pc_creator.py`**
   - `Pc` sinifini kullanarak bir bilgisayar nesnesi olusturur.
   - Komut satirinda secim yapabileceginiz basit bir menu sunar. Bilgisayari calistirma, kapatma ve bilesen degisikligi gibi islemler menude yer alir.
   - Kullanici `0` yazana kadar dongu devam eder.

3. **`README.md`**
   - Depoyu ve kodun amacini kisaca aciklayan bu dosya.

## Bilinmesi Gerekenler

- Kod, OOP temellerini gosterme amaciyla basit tutulmustur.
- Turkce karakterler kaynakli bozukluklar cikabilir; terminalinizde dogru goruntulenmeyebilir.
- Otomatik test veya kapsamli girdi dogrulama bulunmaz; kod dogrudan terminalden kullanici girdisi bekler.

## Sonraki Asamada Yapilacaklar

- **Birim testleri:** Sınıfların davranışını `unittest` kullanarak sınamak.
- **Menü yapısı:** Komut satırı argümanlarıyla çalışabilen modüler bir CLI tasarlamak.
- **Donanım sınıfları:** GPU, depolama ve PSU için ayrı sınıflar eklemek.
- **Dosya desteği:** Bilgisayar konfigürasyonunu dosyadan okuyup yazabilmek.

Bu repo, yeni baslayanlarin OOP temellerini denemesi icin basit ve kisa bir ornek sunar. Once mevcut sinif yapisini ve metotlarini incelemenizi, ardindan kod duzenleme ve test ekleme uzerinde calismanizi oneririz.
