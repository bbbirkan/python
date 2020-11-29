print(""" KARSILASILABILECEK EBOB PROBLEMLERI
1) Bidonlarda, varillerde, şişelerde, çuvallarda, kaplarda bulunan malzemeler daha küçük başka kaplara aktarılıyorsa,

2) Tarlanın etrafına eşit aralıklarla ağaç veya direk dikiliyorsa,

3) İnsanlardan oluşan gruplar için kaç uçak, otobüs, araba veya oda gerekir diye soruluyorsa,

4) Dikdörtgenler prizması şeklindeki odanın, kutunun, deponun içine kaç küp sığar diye soruluyorsa,

5) Kumaşlar, bezler, demir çubuklar parçalara ayrılacaksa,

6) Dikdörtgen şeklindeki kartondan küçük kare kartonlar elde ediliyorsa ebob kullanılır.

ÖRNEK: 80cm ve 120cm uzunluğunda iki demir çubuk, boyları birbirine eşit parçalara ayrılacaktır.Bir parçanın uzunluğu en fazla kaç cm olur?

"""

)


"""
a  b
6  8
ekok 24

ebob= a*b(48)/24

"""

liste=[]


def ebob(a,b):
    i = 1
    while (i < 10):
        if (b < a):
            a, b = b, a
        i += 1
        z = i * a
        t = i * b
        liste.append(z)
        liste.append(t)
    for y in liste:
        if y % a == 0 and y % b == 0:
            print(y, "EKOK")
            break

    ebob = a * b // y
    print(ebob, "EBOB")
a=int(input("A Sayisi"))
b=int(input("B Sayisi"))
ebob(a,b)


