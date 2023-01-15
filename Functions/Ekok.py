print(""" KARSILASILABILECEK EKOK PROBLEMLERI
1) Cevizler, fındıklar, şekerler, bilyeler üçer-beşer-vb sayılıyorsa veya bunlar sayıldıktan sonra artan oluyorsa,

2) Gemiler, arabalar, yarışçılar beraber yola çıkıp bir yerde karşılaşıyorsa,

3) Sınıfta öğrenciler ikişer-üçer-vb sıralara oturuyorlarsa veya bunlardan ayakta kalanlar oluyorsa,

4) Ziller, saatler birlikte ne zaman bir daha çalar diye soruluyorsa,

5) Dikdörtgenler prizması şeklindeki tuğlalardan küp yapılıyorsa ekok kullanılır.

"""

      )




liste=[]

def katlar(a,b):
    i = 1
    while (i < 20):
        if (b < a):
            a,b=b,a
        i += 1
        z = i * a
        t = i * b
        liste.append(z)
        liste.append(t)

    print("ortak liste katlari",liste)
    return

def ekok(a,b):
    katlar(a, b)
    for y in liste:
        if y % a == 0 and y % b == 0:
            print(y, "EKOK")
            return
            break



a=int(input("A Sayisi"))
b=int(input("B Sayisi"))
ekok(a,b)




