
import math
from math import *
#help(math)
help(fsum)
print("""************************
Hesap Makinasi

1 Toplam 
2 Cikarma 
3 Carpma 
4 Bolme 
5 Kalan Bulma 
6 Logaritmasını Hesapla 
7 Faktoriyel
8 Euler sabitinin kuvveti

************************""")



islem= int(input("isleminiz secin"))

if islem <7:
    a = int(input("Birinci Sayi:"))
    b = int(input("Ikinci Sayi:"))
else:
    a = int(input("Birinci Sayi:"))

if islem ==1 :
    print("Birinci Sayi{},{}. islemi ile secilip {} toplandiginda sonuc:{}\n".format(a,islem,b,a+b))
elif islem ==2 :
    print("Birinci Sayi{},{}. islemi ile secilip {} cikarildginda sonuc:{}\n".format(a,islem,b,a-b))
elif islem ==3 :
    print("Birinci Sayi{},{}. islemi ile secilip {} carpmildiginda sonuc:{}\n".format(a,islem,b,a*b))
elif islem ==4 :
    print("Birinci Sayi{},{}. islemi ile secilip {} bolmundugunda sonuc:{}\n".format(a,islem,b,a/b))
elif islem ==5 :
    print("Birinci Sayi{},{}. islemi ile secilip {} bolmundugunden kalan:{}\n".format(a,islem,b,fmod(a,b)))
elif islem ==6 :
    print("Birinci Sayi{},{}. islemi ile secilip {} logaritmasını:{}\n".format(a,islem,b,log(a,b)))
elif islem ==7 :
    print("Birinci Sayi{},{}. islemi ile secilip faktoriyeli:{}\n".format(a, islem, factorial(a)))
elif islem ==8 :
    print("Birinci Sayi{},{}. islemi ile secilip Euler sabitinin kuvveti:{}\n".format(a, islem, exp(a)))

else:
    print("hata var")






"""


-----------------


math.gcd()
Verilen iki sayının EBOB’unu veriyor.

ath.exp()
euler sabitinin kuvvetini alır. Yani yaptığı iş şudur:math.e ** x


math.sqrt()
Verilen sayının karekökünü hesaplar.


math.cosh()
Verilen değerin hiperbolik kosinüsünü döndürür.

math.sinh()
Verilen değerin hiperbolik sinüsünü döndürür.

math.tanh()
Verilen değerin hiperbolik tanjantını döndürür.

"""