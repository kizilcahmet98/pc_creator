import time
class Pc():

    def __init__(self, sahibi = "Yok", cpu = "P4", ram = [1, 0, 0, 0], gpu = "Onboard", depolama = 80, psu = 200, durum = "Kapalı"):
        self.sahibi = sahibi
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.depolama = depolama
        self.psu = psu
        self.durum = durum

    def __str__(self):
        return "Sahibi= {}\nİşlemci= {}\nRam= {}\nEkran Kartı= {}\nDepolama= {}\nPower Supply= {}".format(self.sahibi, self.cpu, self.ram, self.gpu, self.depolama, self.psu)

    def calistir(self):
        if self.durum == "Kapalı":
            print("Bilgisayar Açılıyor...")
            time.sleep(7)
            print("Hoş Geldiniz.")
            self.durum = "Açık"
        else:
            print("Bilgisayar Çalışıyor")

    def kapat(self):
        if self.durum == "Açık":
            print("Bilgisayar Kapanıyor...")
            time.sleep(7)
            self.durum = "Kapalı"

    def sahibi_degistir(self):
        yeni_sahip = input("Yeni sahip: ")
        self.sahibi = yeni_sahip

    def cpu_degistir(self):
        if self.durum == "Açık":
            print("Lütfen bilgisayarı kapatın.")
        else:
            yeni_islemci = input("Yeni işlemci: ")
            self.cpu = yeni_islemci

    def ram_degistir(self):
        if self.durum == "Açık":
            print("Lütfen bilgisayarı kapatın.")
        else:
            yeni_ram = input("Yeni ram listesi:       (',' ile ayırarak girin:)")
            self.ram = yeni_ram.split(",")

    def gpu_degistir(self):
        if self.durum == "Açık":
            print("Lütfen bilgisayarı kapatın.")
        else:
            yeni_gpu = input("Yeni ekran kartı: ")
            self.gpu= yeni_gpu

    def depolama_degistir(self):
        if self.durum == "Açık":
            print("Lütfen bilgisayarı kapatın.")
        else:
            yeni_depolama = input("Yeni Depolama Miktarı: ")
            self.depolama = yeni_depolama

    def psu_degistir(self):
        if self.durum == "Açık":
            print("Lütfen bilgisayarı kapatın.")
        else:
            yeni_psu = input("Yeni PSU WATT: ")
            self.psu = yeni_psu
