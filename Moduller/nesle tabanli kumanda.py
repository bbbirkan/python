import random
import time


class tvkumanda():

    def __init__ (self, durum = "kapali",ses=0,kanal="cnn",liste=["cnn"]):

        self.durum=durum
        self.ses=ses
        self.liste =liste
        self.kanal=kanal

    def tvac(self):

        if (self.durum == "acik"):
            print("televiyon zaten acik..!")

        else:
            print("televizyon aciliyor....")
            self.durum = "acik"
            time.sleep(0.5)
            print("televizyon acildi!")



    def tvkapat(self):

         if (self.durum=="kapali"):
             print("Zaten televizyon kapali")
         else:
             print("televizyon kapaniyor...!")
             self.durum="kapali"

    def ses_ac(self):
        while True:
            x=input("\nSes Azalt '-' yaz\nses artir '+' yaz\nSesten cikis 'c' yaz")

            if(x=="-"):
                if(self.ses!=0):
                    self.ses=self.ses-1
                    print("ses",self.ses)

            elif (x=="+"):
                 if(self.ses !=31):
                     self.ses = self.ses + 1
                     print("ses", self.ses)

            else:
                print('sesten ciktik',self.ses)
                break

    def kanal_ekle(self, kanall):
        print("kanal ekleniyor.....n\lutffen bekleyin......")
        time.sleep(0.5)
        self.liste.append(kanall)
        print("kanal eklendi...")

    def rastgele(self):
        rastgele=random.randint(0,len(self.liste)-1)
        self.kanal=self.liste[rastgele]
        print("suankki kanal",self.kanal)


    def __len__(self):
        return len(self.liste)


    def __str__(self):
        return"Tv durum:{}\nTv ses:{}\nTv kanal list:{}\nSu anki kanal:{}".format(self.durum,self.ses,self.liste, self.kanal)

    def mute(self):
        self.ses=0
        print("ses kapandi",self.ses)

    def uyku(self):
        while True:
            u = input("kac saniye sonra uykuya dalsin ")
            k=int(u)

            if (u=="c"):
                print("cikildi")
                break

            elif (k>6):
                print('kucuk saniye girin')
            else:
                if (u=="c"):
                    print("cikildi")
                    break
                else:

                    print(k, "saniye sonra uykuya dalacak")
                    k= k- 2
                    time.sleep(k)
                    print("2", "saniye sonra uykuya dalacak.... iptal icin 'c'")
                    time.sleep(1)
                    print("Televiyon kapatiliyor!!! 'c'")
                    self.durum="kapali"
                    break



print(tvkumanda)

kumanda = tvkumanda()
print("""
**********************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Sesi aninda kapatir

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

8. Uyku Modu

9. Televizyon Bilgileri


Çıkmak için 'q' ya basın.
*************************
""")

while True:

    gir = input("\nİşlemi Seçiniz:\n")
    if (gir == "q"):
        print("Programdan Çıkılıyor...")
        break
    elif(gir=="1"):
        kumanda.tvac()
    elif (gir == "2"):
        kumanda.tvkapat()
    elif (gir == "3"):
        kumanda.mute()
    elif (gir == "4"):
        print("Kanal Sayisi",len(kumanda))
    elif (gir == "5"):
        kliste=input("kanal isimlerini 'virgul ile ayrirak girin")
        kliste=kliste.split(",")
        for ekle in kliste:
            kumanda.kanal_ekle(ekle)
            print("Kanal Listesi Başarıyla Güncellendi.")
    elif (gir == "6"):
        kumanda.rastgele()
    elif (gir == "7"):
        kumanda.ses_ac()
    elif (gir == "8"):
        kumanda.uyku()
    elif (gir == "9"):
        print(kumanda)
    else:
        print("Geçersiz İşlem...")





