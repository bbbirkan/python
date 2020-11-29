

a=0
c=0
toplam=0
liste=[]
while True:
    a = input("Sayi")



    if (a == "q"):
        break
    else:
        liste.append(int(a))
        print(liste)
for eleman in liste:
    toplam =eleman+toplam


print("Toplam",toplam)
print("islemden cikildi")




