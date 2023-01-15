
def asal(kaca_kadar):
    if kaca_kadar < 1:
        return
    elif kaca_kadar == 2:
        liste.append(2)
        return
    else:
        for i in range(2, kaca_kadar):
            bolundu = False
            for j in range(2, i):
                if i % j == 0:
                    bolundu = True
                    break
            if bolundu == False:
                liste.append(i)
liste=[]
liste2=[]



asal(100)


bak=0
for bak in liste:
    kare = bak - 1
    bak = (2 ** kare) * ((2 ** bak) - 1)
    liste2.append(bak)
print(liste2)











"""
for bak in liste:
    i = 1
    toplam = 0
    while (i < bak):
        if (bak % i == 0):
            toplam += i
        i += 1
    if (toplam == bak):
        liste3.append(bak)
        liste2.append(bak)
        m = m + 1
        if m == k:
            break
    else:
        degil.append(bak)
print(degil, "mükemmel bir sayı değildir.")
print(liste2, "mükemmel bir sayıdir.")
print("Mukemmel sayilar{}".format(liste3[1:]))
"""

"""
add=[]
def asal(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi):  # 2 den buyuk sayiya kadar olan sayilar
            if (sayi % i == 0):
                return False
        return True
"""

"""
-------------------------------------------

    # www.yazilimkodlama.com
    sayac = 0
    sayi = input('Sayı: ')
    for i in range(2, int(sayi)):
        if (int(sayi) % i == 0):
            sayac += 1
            break
    if (sayac != 0):
        print("Sayı Asal Değil")
    else:
        print("Sayı Asal")
-------------------------------------------

# 1000 tane asal sayı bulan program

print 2
# xrange değil henüz...
for i in range(3,1000):

    bolundu = False
    for j in range(2,i):
            if i % j == 0:
                bolundu=True
                # break yok...
    if bolundu == False:
        print i
----------------------------------------------


"""