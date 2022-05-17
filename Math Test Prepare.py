import math
import numpy as np
from fractions import Fraction
#___________________________________________________
print("2.Dereceden Bir Denklemin Kökünü Bulma")
# y=ax^2+bx+c
a = 1
b = 3
c = 0
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci Kök : {}\nİkinci Kök : {}".format(x1, x2))
#___________________________________________________
print("---------------------------------")
a=400


b=17
c=0.44
d=0
print("toplam:",a+b)
print("carpim:",a*b)
print("bolum:",a/b)
print("kalan:",a%b)
print("tam sayi bolme:",a//b)
print("kuvvet:",a**b)
print("karesi:",math.sqrt(25))
print("radians:",math.radians(30))

print("---------------------------------")
miktar=200
bolum = 1 / 4
yuzde = bolum * miktar
print("sayisinin yuzdesi:",yuzde)

print("---------------------------------")
birim=32500
yuzdelik=1
indirim=0
zamli_fiyat=birim*(1+(yuzdelik/100))
indirimli_fiyat=zamli_fiyat*(1-(indirim/100))

print(birim,"sayisinin" ,"%" ,yuzdelik,"'i=",zamli_fiyat-birim,"'eder toplamda (+)",zamli_fiyat)
print("CIKIS:",indirimli_fiyat)


print("---------------------------------")
tek=9 #inch
karsilik=2#feet
isten_miktar=7
sonuc=(tek*isten_miktar)/karsilik
print("00 eldeki sonuc",sonuc)
#print("1. sonuc:",18/21*7)


iki=400 #sayisinin
bir=10  #yuzdesi
#  ===
"""
saying "56 out of 100 animals are dogs," we can say "56%
"""
formul=(bir/iki)*100
print("%",formul)
print("0 fraction",Fraction(0.5).limit_denominator())

bir=100
#  ===
iki=100

uc=3
#  ===
dort=4

print("1 fraction",Fraction(iki,bir))
print("2 fraction arti",5 + Fraction(iki, bir))
print("3 fraction bolu",Fraction(dort, uc) / Fraction(iki, bir))


