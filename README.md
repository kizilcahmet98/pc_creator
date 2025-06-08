# pc_creator

Bu depo, temel OOP (nesne yönelimli programlama) pratiklerini denemek icin hazirlanmis basit bir **bilgisayar konfigürasyon** uygulamasi içerir. Amaci, sınıf yapısını ve metodlarla bir nesnenin durumunun nasıl değiştirilebileceğini gormek isteyenlere ornek saglamaktir.

## Dosya Yapisi

1. **`create.py`**
   - `Pc` sinifini tanimlar. Bilgisayar sahibini ve CPU, RAM, GPU, depolama ile PSU gibi bilesenleri saklar.
   - Bilgisayari acma/kapatma (`calistir`, `kapat`) ve donanim bilgilerini degistirme (`cpu_degistir`, `ram_degistir`, `gpu_degistir`, vb.) gibi metotlar icerir.
   - Ornek amacli yazildigi icin girdi/çıktı islemlerini `input()` ile dogrudan sinif icinde yapar ve Turkce mesajlar kullanir.

2. **`pc_creator.py`**
   - `Pc` sinifini kullanarak bir bilgisayar nesnesi olusturur.
   - Komut satirinda secim yapabileceginiz basit bir menu sunar. Bilgisayari calistirma, kapatma ve bilesen degisikligi gibi islemler menude yer alir.
   - Kullanici `0` yazana kadar dongu devam eder.

3. **`README.md`**
   - Depoyu ve kodun amacini kisaca aciklayan bu dosya.

## Bilinmesi Gerekenler

- Kod, OOP temellerini gosterme amaciyla basit tutulmustur.
- Turkce karakterler kaynakli bozukluklar cikabilir; terminalinizde dogru goruntulenmeyebilir.
- `pc_creator.py` icindeki menudeki numaralar ve metot cagrilarinda birkac tutarsizlik bulunabilir.
- Otomatik test veya girdi dogrulama bulunmaz; kod dogrudan terminalden kullanici girdisi bekler.

## Sonraki Asamada Ogrenilebilecekler

- **Kod düzeni ve bakim:** Dosya isimlerini duzeltmek (`creat.py` yerine `create.py` gibi) ve karakter bozukluklarini gidermek okunabilirligi artiracaktir.
- **Girdi/çıktı ayrimi:** Sinif metotlarinin `input()` yerine parametre alacak sekilde yazilmasi test edilebilirligi kolaylastirir.
- **Hata yönetimi ve testler:** Girdi dogrulama ekleyip birim testleri yazmak iyi bir gelisim adimi olabilir.
- **Genişleme:** RAM gibi bilesenleri nesne haline getirmek ya da bilgisayar bilgilerini dosyaya kaydetmek gibi ek ozellikler eklenebilir.

Bu repo, yeni baslayanlarin OOP temellerini denemesi icin basit ve kisa bir ornek sunar. Once mevcut sinif yapisini ve metotlarini incelemenizi, ardindan kod duzenleme ve test ekleme uzerinde calismanizi oneririz.

