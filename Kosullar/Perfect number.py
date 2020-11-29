
"""

2p−1(2p−1) formülüne göre, ilk 40 çift mükemmel sayıyı hesaplamak için p değişkeninin değeri şunlardan biri olabilir: p = 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609. Bu sayılar arasında başka mükemmel sayılar (çift veya tek) olup olunmadığı bilinmemektedir.

Kaynak : http://www.bilimist.com/blog-41/mukemmel-sayilar-nedir-.html

"""

liste=[]
degil=[]
n=int(input("'xxx' sayiya kadar mmukemel sayilar:\n"))
sayi =n
for bak in range(n):
    i = 1
    toplam = 0
    while (i < bak):
        if (bak % i == 0):
            toplam += i
        i += 1

    if (toplam == bak):

        liste.append(bak)
    else:

        degil.append(bak)
print(liste, "mükemmel bir sayıdir.")
#print(degil, "mükemmel bir sayı değildir.")

"""
def perfect_number(n):
    sum = 0
    for x in range(30):
        if n % x == 0:
            sum=sum+ x
    return sum == n
print(perfect_number(6))



________________
liste=[]
b=1
t=b-1
p=0
x=0

while  b<10:
    b = b + 1
    if p % b == 0:
        t = b - 1
        p=(2**t)*((2**b)-1)
        liste.append(p)
        print(p)

_____________________


liste=[]
b=1
t=b-1
p=0

sayilar=(1,2,3,5,7,11,13,17)
for b in list(kk):
    b=b+1
    t = b - 1
    p=(2**t)*((2**b)-1)

    liste.append(p)
    print(p)

________________________









2p−1(2p−1)
p = 7 için: 26(27−1) = 8128
2p−1(2p−1)
    
    
liste=[]
b=1
c=[]
while  b<10:
    b= b+1

    for kalansiz in range(1,10):
        if kalansiz % b == 0:
            liste.append(kalansiz)
    print(liste)



100%5
a%b=0
perfect=1
for i in perfect.range(45):



liste1=[2,4,3,7,84,45,76,23]

for xax in liste1:
    if xax %2==0:
        print(xax)

-----v.append(k)-------
while True:
    x = input("Faktorunu almak istedigini sayiyi girin yada c basin :")
    if(x == "c"):
        print("cikis yapildi...")
        break
    else:
        x = int(x)
        f=1

        for i in range(1,x+1):
            print("faktor !",i,'=')
            f=f*i
            print(f,"'dir")

b=0

while b<5:
    print(b)
    b= b+1 
0
2
4

liste =[1,4,6,7,8,9]

d=0
while (d < 3):
    print(d,"ci basamaginda",liste[d]) 
    d = d +1
0 ci basamaginda 1
1 ci basamaginda 4
2 ci basamaginda 6  



* 6, * 28, * 496, * 8128, * 33550336, * 8589869056, * 137438691328, * 2305843008139952128, * 2658455991569831744654692615953842176,

Kaynak : http://www.bilimist.com/blog-41/mukemmel-sayilar-nedir-.html 
"""