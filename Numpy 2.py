import numpy as np

data_list = [1,2,3]


x= np.array(data_list)
print(x)
# Yazilimi boyle
data_list2 =[[10,20,30],[30,50,60],[70,80,90]]
# matrix olusturmamizi sagliyor
u= np.array(data_list2)
print("data list2 \n",u)
#
k=u[2,2]
print("3cus satir 3 sira \n",k)
#sayi 0 dan baslar yani 3,3 matris goster deriz
l=np.arange(5,64)
print(l)
# 5 ten baslayip 64 te biter
p=np.arange(0,100,4)
print("4 er atlar \n",p)
#0 dan 100 kadar 4 er 4 er atlayarak yazar
l=np.zeros(6)
print("0 lar\n",l)
#6 tane sifir yazar
k=np.ones(4)
print("1 lar\n",k)
#4 tane bir yazar
y=np.zeros((3,3))
print("y\n",y)
#3 tane satirlik  matris yopar sifirlarla

t=np.zeros((2,5))
print("t\n",t)
#3 li 5 matris

r=np.linspace(0,200,6)
print("r\n",r)
#0 la 200 u 6 esit parcalara bol

r2=np.linspace(0,1,6)
print("r2\n",r2)
#6 esit parcalara bol

r3=np.eye(6)
print("r3\n",r3)
#6ya 6 lik matris olacak koseleri bire esit oluyor

r4=np.random.randint(0,6)
print("r4\n",r4)
#rastgele sayi verir

r5=np.random.randint(7)
print("r5\n",r5)
#rastgele sayi verir 0 dan baslar

v=np.random.randint(7)
print("v\n",v)
#rastgele sayi verir 0 dan baslar

v1=np.random.randint(2,50,5)
print("v1\n",v1)
#ikiden 50 ye kadar sayi donsun 5 tane secsin

v2=np.random.randn(7)
print("v2\n",v2)
#o dan 7 ye kadar 7 deger

v3=np.random.randn(7)
print("v3\n",v3)
#o dan 7 ye kadar 7 deger eksi degerleride kulanir
yupp=np.arange(25)
w= yupp.reshape(5,5)
print("w \n",w)

nope=np.random.seed(101)
ayni=np.random.randint(0,100,10)
print("nope \n",nope)
print("ayni \n",ayni)
print(ayni.max())
#ayni matrixin max sayi degerini verdi
print(ayni.argmax())
#maximium sayinin yerini gosterir
print(ayni.min())
#ayni matrixin min sayi degerini verdi
print(ayni.mean())
#ayni matrixin ortalama sayi degerini verdi

print(ayni.reshape((5,2)))
#10 tane sayimiz var bu ornekte bunu matris seklinde goster diyoruz
#10 sayisini bulmazsan gostermez 2,5 yada 5,2 yazabiliriz

print(np.arange(0,100))
#100 tane sayi yazdi 1 tane matriste

print("Duzenleme \n",np.arange(0,100).reshape(5,20))
#100 tane sayiyi aldi 5 metris icinde 20 sayi sayi yerelestirdi

sayi=np.arange(0,100).reshape(5,20)
satir=3
basamak=3
sayi[satir,basamak]
print(sayi[satir,basamak])
"""
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]]

4. satirin 4. basamagini secti "63" oda -sayilar 0 dan baslar pyhtonda
"""
print(sayi[:,3])
#[ 3 23 43 63 83]

print(sayi[:,3].reshape(5,1))
""""
 [[ 3]
 [23]
 [43]
 [63]
 [83]]
 """

print(sayi[3,:])
#[60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]

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
