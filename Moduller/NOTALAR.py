def nothesap(x):
    x=x[:-1]

    liste=x.split(",")
    isim1 =liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    finalnot=not1*(3/10) + not2*(3/10) + not3 * (4/10)

    if (finalnot >= 90):
        harf="AA"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 85):
        harf="BA"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 80):
        harf="BB"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 75):
        harf="CB"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 70):
        harf="CC"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 65):
        harf="DC"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 60):
        harf="DD"
        (gecenler.append(isim1+ "\n"))
    elif (finalnot >= 55):
        harf = "FD"
        (kalanlar.append(isim1+ "\n"))
    else:
        harf = "FF"
        (kalanlar.append(isim1+ "\n"))
    return isim1 + "-----------"+ harf + "\n"

with open ("/Users/BirkanMac/Desktop/Phton/Notlar.txt","r+",encoding="utf-8") as file:
    ekle=[]
    kalanlar=[]
    gecenler=[]
    for i in file:
        ekle.append(nothesap(i))

    with open("/Users/BirkanMac/Desktop/Phton/notcikti.txt", "w", encoding="utf-8") as file2:
        for i in ekle:
            file2.write(i)


    with open("/Users/BirkanMac/Desktop/Phton/gecenler.txt", "w", encoding="utf-8") as file3:
        for i in gecenler:
            file3.write(i)


    with open("/Users/BirkanMac/Desktop/Phton/kalanlar.txt", "w", encoding="utf-8") as file4:
        for i in kalanlar:
            file4.write(i)

    print(ekle)

