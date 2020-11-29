
print("""Fibonacci Sayıları Hesaplama

FİBONACCİ DİZİSİ NEDİR: Fibonacci dizisi, 0 ve 1 ile başlayan ve her sayının
kendisinden önce gelen iki sayının toplanması ile elde edildiği bir sayı dizisidir.
İtalyan matematikçi Leonardo Fibonacci‘den adını alır.

Fibonacci Sayıları

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
Fibonacci Sayıları
 """)
print("a=0\nb=1\nSayilari bir onceki sayi ile toplayarak ilerliyoruz\n")


a=0
b=1
fibonacci=[a,b]
for i in range (10):

    print(fibonacci,"\n"'a:', a, "b:", b)
    a,b=(b,a)

    print('a:',a,"b:", b,"a~b yer degistirdi")
    print("(a+b) topladik :",a + b,"yeni 'b' sayisi")
    print("'b' Sayisini sona ekle komutu\n")

    b=a+b
    fibonacci.append(b)



print("Fibonacci Sayilari:",fibonacci)
















