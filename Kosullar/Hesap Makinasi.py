print("""************************
Hesap Makinasi

Toplam 1
Cikarma 2
Carpma 3
Bolme 4
************************""")

a= int(input("Birinci Sayi:"))
b= int(input("Ikinci Sayi:"))

islem= int(input("isleminiz secin"))

if islem ==1 :
    print("Birinci Sayi{},{} islemi ile secilip {} toplandiginda sonuc:{}".format(a,islem,b,a+b))
elif islem ==2 :
    print("Birinci Sayi{},{} islemi ile secilip {} cikarildginda sonuc:{}".format(a,islem,b,a-b))
elif islem ==3 :
    print("Birinci Sayi{},{} islemi ile secilip {} carpmildiginda sonuc:{}".format(a,islem,b,a*b))
elif islem ==4 :
    print("Birinci Sayi{},{} islemi ile secilip {} bolmundugunda sonuc:{}".format(a,islem,b,a/b))
else:
    print("hata var")