import random
import time


class Calisan():
    zamoran = 1.8
    sayac=0
    def __init__(self,isim,soyisim,maas):

        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas

        Calisan.sayac = Calisan.sayac+1  #onemli!!!!

    def giveNameSurname(self):
        return self.isim+" "+self.soyisim

    def zamyap(self):
        self.maas = self.maas + self.maas * self.zamoran



calisan1=Calisan("selim","kalyon",100)
print(calisan1.giveNameSurname())
print('ilk maas',calisan1.maas)
calisan1.zamyap()
print('son durum: zam ile',int(calisan1.maas))
calisan2=Calisan("dogukan","kartal",200)
print(Calisan.sayac,"calisan var")


calisan3=Calisan("birkan","kalyon",120)
calisan4=Calisan("caglar","su",150)
calisan5=Calisan("emre","s",90)
calisan6=Calisan("ogulcan","kartal",500)

liste=[calisan1,calisan2,calisan3,calisan4,calisan5,calisan6]

enyuksekmaas=0
giris=0
for i in liste:
    if(i.maas>enyuksekmaas):
        enyuksekmaas=i.maas
        giris=i
print("en yuksek maas alan calisan",enyuksekmaas,"$")
print(giris.giveNameSurname())