
def muk(x):
    liste = []
    sayi = 0
    while sayi in range(x):
        sayi = sayi + 1
        i = 1
        toplam = 0
        while (i < sayi):
            if (sayi % i == 0):
                toplam += i
            i += 1

        if (toplam == sayi):
            liste.append(sayi)
    print("Mükemmel sayıdır.{}".format(liste))






muk(29)

