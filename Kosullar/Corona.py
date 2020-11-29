print("""Corona Virus Dagilma Hizi

Bir kisi bir x  kisiye virus bulastiriyorsa 
Eger ikiye katlanma gun sayilari ayni ise;

 """)
# 2, 4, 12 ,36
#""" input("""1=gunde\n3=hafta\n4=ay\nLutfen sayiyi secin:""")"""

while True:
   x=1
   k = int(input("Kac kiside virus var suan?:\n"))
   b = float(input("Bir kisi kac kisiye bulastiracak sayi girin'(R0)':\n"))
   elaman = 0
   c = int(input("Kac gun sonrayi tahmin etmek istiyorsunuz\n"))
   g = int(input("Kac gunde sayi iki katina cikiyor?\n"))

   gun=(c/g)
   gun=gun-1




   if (b==0) or (b==1):

     break

   elif(gun >= 200):

      print("kucuk sayi giriniz")
      continue
   else:

        break

v=[k]
for x in range (int(gun)):
   print("Yeni {:.1f}".format(k),"insana yayildi")
   k=(k*b)



   v.append(k)
   print(g,"gunde ikiye katliniyor")
   print("Bir kisi", (b),'insana bulastiriyor'"\n")


for xxx in v:
   elaman=elaman+xxx

list =v
list_of_floats = []
for item in list:
    list_of_floats.append(int(item))


print(c,"Gun sonra",list_of_floats,'basamak katlanarak toplamda',int(elaman),"enfekte insan sayisina ulasti")

