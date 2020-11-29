import time


class Takromania():
    def __init__(self,tip=["Canlılık (Biota)"],
                 super_alan_superdomain=["Arkeler ve Ökaryotlar (Neomura)"],
                 alan=["Ökarya (Eukarya)"],
                 klad=["Amipler, Hayvanlar, Mantarlar (Unikonta)"],
                 klad1=["Arkadan Kamcılılar"],
                 klad2=["Hayvanlar ve Tek Hücreli Yakin Akrabaları (Holozoa)"],
                 alem=["Hayvanlar (Animalia)"],
                 alt_alem=["Gerçek Dokulular (Eumetazoa)"],
                 klad_ana=["Çift Yanlı Simetrikler (Bilateria)"],
                 ust_sube=["İkincil Ağızlılar (Deuterostomia)"],
                 sube_filum=["Kordalılar (Chordata)"],
                 alt_sube=["Omurgalılar (Vertebrata)"],
                 infra_sube_Infraphylum=["Gerçekçeneliler (Gnathostomata)"],
                 ust_sinif=["Dört Üyeliler (Tetrapoda)"],
                 sinif=["Memeliler (Mammalia)"],
                 alt_sinif=["Doğuran Memeliler (Theriiformes)"],
                 infra_sinif_Infraclass=["Plasentalı Memeliler, Eteneliler (Eutheria,Placentalia)"],
                 ust_takim_Superorder=["Kemiriciler, Tavşanımsılar, Sivri Sincapçıkgiller, Primatlar, Abalı Memeliler (Euarchontoglires)"],
                 takim=["Primatlar,İri Beyinli Yüksek Memeliler (Primata)"],
                 alt_takim=["Kuru Burunlu Primatlar (Haplorrhini)"],
                 infra_takim_Infraorder=["Maymunlar (Simiiformes, Simians)"],
                 gecis_takimi_Parvorder=["Eski Dünya Maymunları ve Kuyruksuz Maymunlar (Catarrhini)"],
                 ust_familya=["Kuyruksuz Maymunlar İnsansılar (Hominoidea, Apes)"],
                 aile_familya=["Büyük Kuyruksuz Maymunlar (Hominidae, Great Apes)"],
                 alt_familya=["insanlar, Şempanzeler, Goriller ve Ataları (Homininae)"],
                 oymak_tribu=["İnsanlar, Şempanzeler ve Ataları (Hominini)"],
                 alt_oymak=["İnsanlar ve Ataları (Hominina)"],
                 cins=["İnsan (Homo)"],
                 tur=["Anatomik Olarak Modern İnsanlar, Bilge İnsanlar (Homo sapiens)"],
                 alt_tur=["Modern Bilge İnsan (Homo sapiens sapiens)"]
                 ):
        self.tip =tip
        self.super_alan_superdomain=super_alan_superdomain
        self.alan=alan
        self.klad=klad
        self.klad1=klad1
        self.klad2=klad2
        self.alem= alem
        self.alt_alem=alt_alem
        self.klad_ana=klad_ana
        self.ust_sube=ust_sube
        self.sube_filum=sube_filum
        self.alt_sube=alt_sube
        self.infra_sube_Infraphylum=infra_sube_Infraphylum
        self.ust_sinif=ust_sinif
        self.sinif=sinif
        self.alt_sinif=alt_sinif
        self.infra_sinif_Infraclass=infra_sinif_Infraclass
        self.ust_takim_Superorder=ust_takim_Superorder
        self.takim=takim
        self.alt_takim=alt_takim
        self.infra_takim_Infraorder=infra_takim_Infraorder
        self.gecis_takimi_Parvorder=gecis_takimi_Parvorder
        self.ust_familya=ust_familya
        self.aile_familya=aile_familya
        self.alt_familya=alt_familya
        self.oymak_tribu=oymak_tribu
        self.alt_oymak=alt_oymak
        self.cins=cins
        self.tur=tur
        self.alt_tur=alt_tur

    def __str__(self):
        return "Tip:{}\nSuper Alan Superdomain:{}\nAlan:{}\nKlad:{}\nKlad1:{}\nKlad2:{}\nAlem:{}\nAlt Alem:{}\nKlad Ana:{}\nUst Sube:{}\nSube Filum:{}\nAlt Sube:{}\nInfra Sube Infraphylum:{}\nUst Sinif:{}\nSinif:{}\nAlt Sinif:{}\nInfra Sinif Infraclass:{}\nUst Takim Superorder:{}\nTakim:{}\nAlt takim:{}\nInfra Takim Infraorder:{}\nGecis Takimi Parvorder:{}\nUst Familya:{}\nAile Familya:{}\nAlt Familya:{}\nOymak Tribu:{}\nAlt Oymak:{}\nCins:{}\nTur:{}\nAlt_tur:{}\n".format(self.tip,self.super_alan_superdomain,self.alan,self.klad,self.klad1,self.klad2,self.alem,self.alt_alem,self.klad_ana,self.ust_sube,self.sube_filum,self.alt_sube,self.infra_sube_Infraphylum,self.ust_sinif,self.sinif,self.alt_sinif,self.infra_sinif_Infraclass,self.ust_takim_Superorder,self.takim,self.alt_takim,self.infra_takim_Infraorder,self.gecis_takimi_Parvorder,self.ust_familya,self.aile_familya,self.alt_familya,self.oymak_tribu,self.alt_oymak,self.cins,self.tur,self.alt_tur)

class Sapiens(Takromania):

    pass





class Kopek(Takromania):
    def __init__(self,
                 takim=["Carnivora (Etçiller)"],
                 familya=["Canidae (Köpekgiller)"],
                 oymak=["Canini (Asıl köpekler)"],
                 alt_tur=["C l familiaris (Köpek)"],
                 cins=[]):

        super().__init__(
            tip=["Canlılık (Biota)"],
            super_alan_superdomain=["Arkeler ve Ökaryotlar (Neomura)"],
            alan=["Ökarya (Eukarya)"],
            klad=["Amipler, Hayvanlar, Mantarlar (Unikonta)"],
            klad1=["Arkadan Kamcılılar"],
            klad2=["Hayvanlar ve Tek Hücreli Yakin Akrabaları (Holozoa)"],
            alem=["Hayvanlar (Animalia)"],
            alt_alem=["Gerçek Dokulular (Eumetazoa)"],
            klad_ana=["Çift Yanlı Simetrikler (Bilateria)"],
            ust_sube=["İkincil Ağızlılar (Deuterostomia)"],
            sube_filum=["Kordalılar (Chordata)"],
            alt_sube=["Omurgalılar (Vertebrata)"],
            infra_sube_Infraphylum=["Gerçekçeneliler (Gnathostomata)"],
            ust_sinif=["Dört Üyeliler (Tetrapoda)"],
            sinif=["Memeliler (Mammalia)"],
            alt_sinif=["Doğuran Memeliler (Theriiformes)"])
        self.takim=takim
        self.familya =familya
        self.oymak=oymak
        self.alt_tur=alt_tur
        self.cins=cins
    def __str__(self):
        return  "Tip:{}\nSuper Alan Superdomain:{}\nAlan:{}\nKlad:{}\nKlad1:{}\nklad2{}\nAlem:{}\nAlt Alem:{}\nKlad Ana:{}\nUst Sube:{}\nSube Filum:{}\nAlt Sube:{}\nInfra Sube Infraphylum:{}\nUst Sinif:{}\nSinif:{}\nAlt Sinif:{}\nTakim:{}\nFamilya{}\nOymak{}\nAlt Tur{}\nCins{}".format(self.tip,self.super_alan_superdomain,self.alan,self.klad,self.klad1,self.klad2,self.alem,self.alt_alem,self.klad_ana,self.ust_sube,self.sube_filum,self.alt_sube,self.infra_sube_Infraphylum,self.ust_sinif,self.sinif,self.alt_sinif,self.takim,self.familya,self.oymak,self.alt_tur,self.cins)


    def __len__(self):
        return len(self.cins)

    def kopek_ekle(self, kopek):
        print("kopek ekleniyor.....n\lutffen bekleyin......")
        time.sleep(0.5)
        self.cins.append(kopek)
        print("kopek eklendi...")
        print(self.cins)
        return
class Kus(Takromania):
    def __init__(self,alt_sube=["(Vertebrata)"],sinif=["Kuşlar (Aves)"]):

        super().__init__(
            tip=["Canlılık (Biota)"],
            super_alan_superdomain=["Arkeler ve Ökaryotlar (Neomura)"],
            alan=["Ökarya (Eukarya)"],
            klad=["Amipler, Hayvanlar, Mantarlar (Unikonta)"],
            klad1=["Arkadan Kamcılılar"],
            klad2=["Hayvanlar ve Tek Hücreli Yakin Akrabaları (Holozoa)"],
            alem=["Hayvanlar (Animalia)"],
            alt_alem=["Gerçek Dokulular (Eumetazoa)"],
            klad_ana=["Çift Yanlı Simetrikler (Bilateria)"],
            ust_sube=["İkincil Ağızlılar (Deuterostomia)"],
            sube_filum=["Kordalılar (Chordata)"])
        self.alt_sube = alt_sube
        self.sinif = sinif

    def __str__(self):
        return "Tip:{}\nSuper Alan Superdomain:{}\nAlan:{}\nKlad:{}\nKlad1:{}\nklad2{}\nAlem:{}\nAlt Alem:{}\nKlad Ana:{}\nUst Sube:{}\nSube Filum:{}\nalt_sube:{}\nsinif:{}\n".format(self.tip,self.super_alan_superdomain,self.alan,self.klad,self.klad1,self.klad2,self.alem,self.alt_alem,self.klad_ana,self.ust_sube,self.sube_filum,self.alt_sube,self.sinif)


insan=Sapiens()
kopek=Kopek()
kus=Kus()

print("""
**************************
     Canlini sec  
Taksonomi Semasini gor 
Istersen Cinsleri Gir ve 
Veriyi genislet...!

0 Insan
1 Kopek
2 Kus
q Cikis
***************************

""")

"""
x=int(input("Sayi"))

if (x==0):
    print(kopek)

"""


while True:

    gir = input("\nİşlemi Seçiniz:\n")
    if (gir == "q"):
        print("Programdan Çıkılıyor...")
        break
    elif (gir == "0"):
        print(insan)

    elif (gir == "1"):
        print(kopek)

        while True:
            kliste = input("isterseniz kopek cinslerini 'virgul ile ayrirak girin\nya da 'cik ile sonlandrin...\n")
            if (kliste =="cik"):

                break
            else:

                kliste = kliste.split(",")
                for ekle in kliste:
                    kopek.kopek_ekle(ekle)
                    print("Kopek Cinsleri Listesi Başarıyla Güncellendi. Tesekkurler")
                    print("listede suan:",len(kopek),"cins var")



    elif (gir == "2"):
        print(kus)
    else:
        print("Geçersiz İşlem...")