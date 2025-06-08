import time


class Ram:
    """Basit RAM tanimi."""

    def __init__(self, size: int):
        self.size = int(size)

    def __str__(self):
        return f"{self.size}GB"


class Pc:

    def __init__(self, sahibi="Yok", cpu="P4", ram=None, gpu="Onboard", depolama=80, psu=200, durum="Kapalı"):
        self.sahibi = sahibi
        self.cpu = cpu
        self.ram = [Ram(r) for r in (ram or [1, 0, 0, 0])]
        self.gpu = gpu
        self.depolama = int(depolama)
        self.psu = int(psu)
        self.durum = durum

    def __str__(self):
        ram_list = ', '.join(str(r) for r in self.ram)
        return (
            f"Sahibi= {self.sahibi}\n"
            f"İşlemci= {self.cpu}\n"
            f"Ram= {ram_list}\n"
            f"Ekran Kartı= {self.gpu}\n"
            f"Depolama= {self.depolama}GB\n"
            f"Power Supply= {self.psu}W"
        )

    def calistir(self):
        if self.durum == "Kapalı":
            print("Bilgisayar Açılıyor...")
            time.sleep(1)
            print("Hoş Geldiniz.")
            self.durum = "Açık"
        else:
            print("Bilgisayar Çalışıyor")

    def kapat(self):
        if self.durum == "Açık":
            print("Bilgisayar Kapanıyor...")
            time.sleep(1)
            self.durum = "Kapalı"

    def sahibi_degistir(self, yeni_sahip: str):
        self._degisiklik_kontrol()
        self.sahibi = yeni_sahip

    def cpu_degistir(self, yeni_islemci: str):
        self._degisiklik_kontrol()
        self.cpu = yeni_islemci

    def ram_degistir(self, yeni_ram_list):
        self._degisiklik_kontrol()
        self.ram = [Ram(r) for r in yeni_ram_list]

    def gpu_degistir(self, yeni_gpu: str):
        self._degisiklik_kontrol()
        self.gpu = yeni_gpu

    def depolama_degistir(self, yeni_depolama: int):
        self._degisiklik_kontrol()
        self.depolama = int(yeni_depolama)

    def psu_degistir(self, yeni_psu: int):
        self._degisiklik_kontrol()
        self.psu = int(yeni_psu)

    def kaydet_dosyaya(self, yol: str):
        with open(yol, "w", encoding="utf-8") as f:
            f.write(str(self))

    def _degisiklik_kontrol(self):
        if self.durum == "Açık":
            raise RuntimeError("Lütfen bilgisayarı kapatın.")
