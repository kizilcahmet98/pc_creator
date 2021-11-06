from creat import Pc

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
0 - Programdan Çıkış 

""")

while True:
    x = int(input("Fonksiyon numarası girin: "))
    if x == 0:
        break
    elif x == 1:
        print(asus)
    elif x == 2:
        asus.calistir()
    elif x == 3:
        asus.kapat()
    elif x == 4:
        asus.cpu_degistir()
    elif x == 5:
        asus.gpu_degistir()
    elif x == 6:
        asus.ram_degistir()
    elif x == 7:
        asus.psu_degistir()
    elif x == 8:
        asus.depolama()
    elif x == 9:
        asus.psu_degistir()
    else:
        print("Hatalı fonksiyon numarası")