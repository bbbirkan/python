print("""
************************
Birkan Bank ATM 
Bankimiza Hosgeldiniz.

Islemler
1.Bakiye Sorgulama
2.Para Yatirma
3.Para Cekme
Cikis icin: c yazin
************************
""")
bakiye = 950 #kulanicinin bakiyesi


while True:

    islem = input("Islem numaranizi yazin: ")

    if (islem == "c"):
        print("Yine bekleriz. Gule Gule")
        break

    elif (islem == "1"):
        print('Bakiyeniz {} $ dolardir.\n'.format(bakiye))

    elif (islem == "2"):
       yatirma= int(input('Lutfen Yatiracaginiz Miktari Yazin: '))
       bakiye = bakiye + yatirma
       print('Iselminiz basariyla gerceklesti bakiyeniz {}$ dolardir.\n'.format(bakiye))

    elif (islem == "3"):
        cekim=int(input('Lutfen Cekceginiz Miktari Yazin: '))
        if (cekim > bakiye):
            print("Bakiyeniz yetersiz\n")
        else:
            bakiye= bakiye - cekim
            print('Iselminiz basariyla gerceklesti bakiyeniz {}$ dolardir.\n'.format(bakiye))
        continue
    else:
        print('Gecersiz islem\n')




