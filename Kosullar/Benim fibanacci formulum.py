print("""Fibonacci Sayıları Hesaplama

Fibonacci dizisi, Her sayının kendisinden önce gelen iki sayının toplanması ile elde edilen bir sayı dizisidir. İtalyan matematikçi Leonardo Fibonacci‘den adını alır.

Fibonacci Sayıları Ornek:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,  89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946

 """)


while True:
   a = 0
   b = int(input("Hangi sayidan baslamak istediginizi yazin"))
   c = int(input("Kac basamakli Fibonacci dizisi olusturmak istiyorsunuz? Max '20' girebilirsiniz."))
   c = (c - 1)
   if (b==0):
     b=(1)
     break




   elif(c >= 21):
      print("kucuk sayi giriniz")
      continue
   else:

        break
fibonacci = [a, b]
for i in range (c):
   print(fibonacci, "\n"'a:', a, "b:", b)
   a=a+b
   print("a+b=a sayisi",a)



   a, b = (b, a)
   print('a:', a, "b:", b, "a~b yer degistirdi")
   print(b, "Bu yeni 'b' sayisi oldu.")
   print("'b' Sayisini sona ekle komutu\n")

   fibonacci.append(b)



print("Fibonacci Sayilari:",fibonacci[1:],'dir')

