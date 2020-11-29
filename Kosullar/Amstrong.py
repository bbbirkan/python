
v=input("sayi giriniz")
b=str(v)
c=int(b)

liste=[]
i=0
while (i < 1):
    i += 1
    if len(b)==2:
        if (int(b[0]) ** 2) + (int(b[1]) ** 2) == c:
            print("Amstrong sayisi")
            liste.append(c)

        else:
            print(c,"degil")
    elif len(b)==3:
        if (int(b[0]) ** 3) + (int(b[1]) ** 3) + (int(b[2]) ** 3)== c:
            print("Amstrong sayisi")
            liste.append(c)
        else:
            print(c,"degil")

    elif len(b)==4:
        if (int(b[0]) ** 4) + (int(b[1]) ** 4) + (int(b[2]) ** 4)+(int(b[3]) ** 4) == c:
            print("Amstrong sayisi")
            liste.append(c)
        else:
            print(c,"degil")
            continue


"""
Hoca yapmis

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")


"""

#a=int(input("sayi giriniz:\n"))
"""
a=5
liste=[]
for ams in range(a):
    ams=ams+1
    liste.append(ams)
    print(liste)
"""
'''
liste2=[1,3,4,5,7]
d=0
while (d <4):
    print(d,"ci basamaginda",liste2[d])
    d = d +1
'''