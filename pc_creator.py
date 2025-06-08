from create import Pc

asus = Pc()

print("""

1 - Bilgisayar Bilgilerini Getir
2 - Bilgisayarı Çalıştır
3 - Bilgisayarı Kapat
4 - Bilgisayar Sahibini Değiştir
5 - İşlemciyi Değiştir
6 - Ram Değiştir
7 - Ekran Kartı Değiştir
8 - Depolama Miktarı Değiştir
9 - PSU Watt Değiştir
10 - Bilgileri Dosyaya Kaydet
0 - Programdan Çıkış

""")

while True:
    try:
        x = int(input("Fonksiyon numarası girin: "))
    except ValueError:
        print("Geçersiz seçim.")
        continue
    if x == 0:
        break
    elif x == 1:
        print(asus)
    elif x == 2:
        asus.calistir()
    elif x == 3:
        asus.kapat()
    elif x == 4:
        yeni = input("Yeni sahip: ")
        asus.sahibi_degistir(yeni)
    elif x == 5:
        yeni = input("Yeni işlemci: ")
        asus.cpu_degistir(yeni)
    elif x == 6:
        yeni = input("Yeni ram listesi: (',' ile ayırarak girin:) ")
        try:
            ram_list = [int(i) for i in yeni.split(',') if i.strip()]
        except ValueError:
            print("Geçersiz ram değeri")
            continue
        asus.ram_degistir(ram_list)
    elif x == 7:
        yeni = input("Yeni ekran kartı: ")
        asus.gpu_degistir(yeni)
    elif x == 8:
        try:
            yeni = int(input("Yeni Depolama Miktarı: "))
        except ValueError:
            print("Geçersiz değer")
            continue
        asus.depolama_degistir(yeni)
    elif x == 9:
        try:
            yeni = int(input("Yeni PSU WATT: "))
        except ValueError:
            print("Geçersiz değer")
            continue
        asus.psu_degistir(yeni)
    elif x == 10:
        dosya = input("Kaydedilecek dosya yolu: ")
        try:
            asus.kaydet_dosyaya(dosya)
        except Exception as e:
            print(f"Kaydetme hatası: {e}")
    else:
        print("Hatalı fonksiyon numarası")
