import numpy as np

data_list = [1,2,3]
"""
[1 2 3]
"""

x= np.array(data_list)
print(x)
# Yazilimi boyle
data_list2 =[[10,20,30],[30,50,60],[70,80,90]]
# matrix olusturmamizi sagliyor
u= np.array(data_list2)
print("data list2 \n",u)
"""
data list2 
 [[10 20 30]
 [30 50 60]
 [70 80 90]]
 """

k=u[2,2]
print("3cus satir 3 sira \n",k)
#sayi 0 dan baslar yani 3,3 matris goster deriz
"""
3cus satir 3 sira 
90
"""



l=np.arange(5,64)
print(l)
# 5 ten baslayip 64 te biter
"""
[ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
 53 54 55 56 57 58 59 60 61 62 63]
"""


p=np.arange(0,100,4)
print("4 er atlar \n",p)
#0 dan 100 kadar 4 er 4 er atlayarak yazar
"""
[ 0  4  8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92
 96]
"""

l=np.zeros(6)
print("0 lar\n",l)
#6 tane sifir yazar
"""
0 lar
[0. 0. 0. 0. 0. 0.]
"""

k=np.ones(4)
print("1 lar\n",k)
#4 tane bir yazar
"""
1 lar
[1. 1. 1. 1.]
"""

y=np.zeros((3,3))
print("y\n",y)
#3 tane satirlik  matris yopar sifirlarla
"""
y
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
"""



t=np.zeros((2,5))
print("t\n",t)
#3 li 5 matris
"""
t
 [[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
"""

r=np.linspace(0,200,6)
print("r\n",r)
#0 la 200 u 6 esit parcalara bol
"""
r
 [  0.  40.  80. 120. 160. 200.]
"""

r2=np.linspace(0,1,6)
print("r2\n",r2)
#6 esit parcalara bol
"""
r2
 [0.  0.2 0.4 0.6 0.8 1. ]
"""

r3=np.eye(6)
print("r3\n",r3)
#6ya 6 lik matris olacak koseleri bire esit oluyor
"""
r3
 [[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]]

"""

r4=np.random.randint(0,6)
print("r4\n",r4)
#rastgele sayi verir
"""
r4
 1
"""
r5=np.random.randint(7)
print("r5\n",r5)
#rastgele sayi verir 0 dan baslar
"""
r5
 0
"""
v=np.random.randint(7)
print("v\n",v)
#rastgele sayi verir 0 dan baslar
"""
v
 5
"""
v1=np.random.randint(2,50,5)
print("v1\n",v1)
#ikiden 50 ye kadar sayi donsun 5 tane secsin
"""
v1
 [ 6 11 29 45 27]
"""
v2=np.random.randn(7)
print("v2\n",v2)
#o dan 7 ye kadar 7 deger
"""
v2
 [-0.84829715  3.1828921  -0.80409494  2.37925531  0.72302049 -1.04206014
  0.86094942]
"""
v3=np.random.randn(7)
print("v3\n",v3)
#o dan 7 ye kadar 7 deger eksi degerleride kulanir
"""
v3
 [-0.34364363  1.70500991 -1.06758615 -1.27525045  0.90303221 -0.44029292
 -0.17729857]
"""

yupp=np.arange(25)
w= yupp.reshape(5,5)
print("w \n",w)
"""
w 
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

"""
nope=np.random.seed(101)
ayni=np.random.randint(0,100,10)
print("nope \n",nope)
print("ayni \n",ayni)
print(ayni.max())
#ayni matrixin max sayi degerini verdi =nope biliyorum

"""
nope 
 None 
ayni 
 [95 11 81 70 63 87 75  9 77 40]

"""
print(ayni.argmax())
#maximium sayinin yerini gosterir
"""
95
"""
print(ayni.min())
#ayni matrixin min sayi degerini verdi
"""
9
"""
print(ayni.mean())
#ayni matrixin ortalama sayi degerini verdi
"""
60.8
"""
print(ayni.reshape((5,2)))
#10 tane sayimiz var bu ornekte bunu matris seklinde goster diyoruz
#10 sayisini bulmazsan gostermez 2,5 yada 5,2 yazabiliriz
"""
[[95 11]
 [81 70]
 [63 87]
 [75  9]
 [77 40]]
"""
print(np.arange(0,100))
#100 tane sayi yazdi 1 tane matriste
"""
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
"""
print("Duzenleme \n",np.arange(0,100).reshape(5,20))
#100 tane sayiyi aldi 5 metris icinde 20 sayi sayi yerelestirdi
"""
Duzenleme 
 [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]]
"""
sayi=np.arange(0,100).reshape(5,20)
satir=3
basamak=3
sayi[satir,basamak]
print("Sayi")
print(sayi[satir,basamak])
#4. satirin 4. basamagini secti "63" oda -sayilar 0 dan baslar pyhtonda
"""
Sayi
63
"""
print(sayi[:,3])
"""
[ 3 23 43 63 83]
"""

print(sayi[:,3].reshape(5,1))
""""
 [[ 3]
 [23]
 [43]
 [63]
 [83]]
 """

print(sayi[3,:])
"""
60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
"""

print(sayi[0:3,0:4])
"""
[[ 0  1  2  3]
 [20 21 22 23]
 [40 41 42 43]]
"""

hopa = sayi
hopa[0:3,0:4] = 1
print(hopa)
"""
[[ 1  1  1  1  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
 [ 1  1  1  1 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
 [ 1  1  1  1 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]]
"""
copyalama=hopa.copy()
#yukardainin aynisini kopyaladim
copyalama[0:2,:] = 31
print(copyalama)
"""
iki satiri kople aldi ve 31 yerlestirdi 
[[31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31]
 [31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31]
 [ 1  1  1  1 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]]

"""

topla=np.arange(25)
print("Sayilar",topla)
print(topla.reshape(5,5))
print("Toplama")
print(topla.sum())
#yeni numpy degiskeni olusturdum 5 e 5 olarak degistirdim sonra
#butun sayilari topladim
"""
Sayilar [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
Toplama
300
"""
deter=np.array([[1,2],[3,4]])
print(deter)
print(np.linalg.det(deter))
print(round(np.linalg.det(deter)))
#matris uzerinde determinat bulmaya calistik roundlada kusuratlari yok ettik
"""
[[1 2]
 [3 4]]
-2.0000000000000004
-2
"""
birkan_dizi=np.arange(1,10)
print(birkan_dizi)
print(birkan_dizi[2])
print(birkan_dizi[2:5])
print(birkan_dizi[0:4])
print(birkan_dizi[::2])
"""
[1 2 3 4 5 6 7 8 9]
3
[3 4 5]
[1 2 3 4]
[1 3 5 7 9]
"""

yuy=birkan_dizi[1:3]=65
print(birkan_dizi)
"""
[ 1 65 65  4  5  6  7  8  9]
"""
dizi_1=np.arange(1,10)
dizi_2=dizi_1
print("dizi 1",dizi_1)
print("dizi 2",dizi_2)
#dizi2-dizi1 e esitlendi
"""
dizi 1 [1 2 3 4 5 6 7 8 9]
dizi 2 [1 2 3 4 5 6 7 8 9]
"""
dizi_2[:3]=31
print(dizi_2)
print(dizi_1)
#dizi 2 yi degistirince - dizi 1 de otamatik degisti
"""
[31 31 31  4  5  6  7  8  9]
[31 31 31  4  5  6  7  8  9]
"""

dizi_a=np.arange(1,10)
dizi_b=dizi_a.copy()
# kopya olusturduk bundan sonra dizi a dizi b birbirlerinden bagimsiz

dizi_x=np.arange(1,21)
print(dizi_x)
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

"""

print(dizi_x.reshape(5,4))
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
"""
c = dizi_x.reshape(5,4)
print(c[0,0])
"""
1
"""
print(c[:,:2])
""""
[[ 1  2]
 [ 5  6]
 [ 9 10]
 [13 14]
 [17 18]]
"""

print(c[:3,:3])

"""
[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]]
"""
print(c[:2])
"""
[[1 2 3 4]
 [5 6 7 8]]
"""
print("deneme1")
print(c[:2,:3])

"""deneme1
[[1 2 3]
 [5 6 7]]
"""

print("deneme2")
print(c[:1,:4])

"""
deneme2
[[1 2 3 4]]
"""

print("deneme3")
print(c[:1,:1])

"""
deneme3
[[1]]
"""
print("deneme:4")
print(c[:0,:0])
"""
deneme4
[]
"""
print("deneme:5")
print(c[0,0])
"""
deneme:5
1
"""

print("deneme:6")
print(c[:2,:])
"""
deneme:6
[[1 2 3 4]
 [5 6 7 8]]
"""

print("deneme:7")
print(c[:2])
"""
deneme:7
[[1 2 3 4]
 [5 6 7 8]]
"""

dizi_3=np.arange(1,13)
print(dizi_3)
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12]
"""

text1= dizi_3 > 3
print(text1)
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12]
"""


mantik_dizisi = dizi_3 > 3
print(" mantik_dizisi test:\n",mantik_dizisi)
"""
mantik_dizisi test:
 [False False False  True  True  True  True  True  True  True  True  True]
"""

print(dizi_3[mantik_dizisi])
"""
[ 4  5  6  7  8  9 10 11 12]
"""


print(dizi_3[dizi_3>5])
"""
[ 6  7  8  9 10 11 12]
"""

