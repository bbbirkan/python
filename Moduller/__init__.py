import time
import random
print("""
********************************************************

            --Sayı Tahmin Oyunu--

1 ile 50 arasında rastgele secilmis bir sayi
hadi hislerine guven ve tahmin et sadece 5 hakkin var...!
**********************************************************
""")

tahmin=5

x = random.randint(1, 50)
while True:
    sayi=int(input("TAHMIN ET!\n"))

    if (sayi<x):
        time.sleep(1)
        print("buyuk sayi dene!")
        tahmin=tahmin -1
    elif(sayi>x):
        time.sleep(1)
        print("kucuk bir sayi dene!")
        tahmin = tahmin - 1
    else:
        print(" VOOV Tebriler bildiniz")
        print(x,"Sayiniz Dogru")
        break
    if (tahmin==0):
        print("Upps! Oyun bitti... Yenildiniz.")
        print(x, "Sayi")
        break
