class Personel:
    def __init__(self, isim, soyad, gorev, demirbas, gunluk_ucret):
        self.isim = isim
        self.soyad = soyad
        self.gorev = gorev
        self.demirbas = demirbas
        self.gunluk_ucret = gunluk_ucret
        self.calisilan_gun = 0

    def gun_ekle(self, gun):
        try:
            if gun < 0:
                raise ValueError("Gün negatif olamaz!")
            self.calisilan_gun += gun
        except Exception as e:
            print("Hata:", e)

    def maas_hesapla(self):
        return self.calisilan_gun * self.gunluk_ucret

    def bilgi(self):
        return f"{self.isim} {self.soyad} | Görev: {self.gorev} | Gün: {self.calisilan_gun} | Maaş: {self.maas_hesapla()} TL"


class Kurum:
    def __init__(self):
        self.personeller = []

    def personel_ekle(self, personel):
        try:
            self.personeller.append(personel)
        except Exception as e:
            print("Hata:", e)

    def personel_cikar(self, isim):
        try:
            self.personeller = [p for p in self.personeller if p.isim != isim]
        except Exception as e:
            print("Hata:", e)

    def tumunu_temizle(self):
        self.personeller.clear()

    def listele(self):
        if not self.personeller:
            print("Personel yok.")
        for p in self.personeller:
            print(p.bilgi())


p1 = Personel("Ahmet", "Mehmet", "Yazılımcı", "Laptop", 500)
p1.gun_ekle(20)

p2 = Personel("Ali", "Veli", "Teknisyen", "Tablet", 300)
p2.gun_ekle(15)

kurum = Kurum()
kurum.personel_ekle(p1)
kurum.personel_ekle(p2)

print("Personel Listesi:")
kurum.listele()

print("\nAli çıkarılıyor...")
kurum.personel_cikar("Ali")
kurum.listele()

print("\nTüm personel siliniyor...")
kurum.tumunu_temizle()
kurum.listele()