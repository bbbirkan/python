class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maaş, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

class Yönetici(Çalışan):

    def __init__(self, isim, maaş, departman, kişi_sayısı):  # Sorumlu olduğu kişi sayısı
        super().__init__(isim, maaş,
                         departman)  # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz.

        print("Yönetici sınıfının init fonksiyonu")

        self.kişi_sayısı = kişi_sayısı  # Ekstra özelliği de kendimiz yazıyoruz.

    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")

        print(
            "İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maaş, self.departman,
                                                                                   self.kişi_sayısı))

    def zam_yap(self, zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı


help(Yönetici)
