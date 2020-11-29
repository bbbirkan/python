i=0

liste2 = [ i for i in range(100) if i % 2 == 0]
print(liste2)


liste=[]

for eleman in range(1,50):
    if eleman % 2 == 0:
        liste.append(eleman)
        print(eleman)
print(liste)