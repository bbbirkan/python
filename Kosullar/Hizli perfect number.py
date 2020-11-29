k = int(input("'xxx'kac tane mukemmel sayi istiyorsunuz:\n"))
x = k
degil = []
liste = []
liste2 = []
n = x + x + x + 2
b = 1
p = 0
x = 0
i = 1
m = 0
liste3 = [m]

sayi = range(n)
for bak in sayi:
    i = 1
    toplam = 0
    while b < bak:
        b = b + 1
        if p % 2 == 0:
            t = b - 1
            p = (2 ** t) * ((2 ** b) - 1)
            liste.append(p)
print(liste)
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
