
with open ("/Users/BirkanMac/Desktop/Phton/isim.txt" ,"r+" ,encoding="utf-8") as file:
    kiz = list()
    erkek = list()
    ortak=[]
    file.seek(0)
    for i in file:
        i=i[:-1]
        a=i

        satirlar=i.split ( "'")
        print(satirlar[3])





        if satirlar[3]=="Kız":
            kiz.append(satirlar[1]+ satirlar[2]+ satirlar[3] +"\n")

        elif (satirlar[3]=="Erkek/Kız"):
            ortak.append(satirlar[1]+ satirlar[2]+ satirlar[3] +"\n")
        else:
            erkek.append(satirlar[1]+ satirlar[2]+ satirlar[3] +"\n")




with open ("/Users/BirkanMac/Desktop/Phton/kiz.txt" ,"w" ,encoding="utf-8") as file2:
    for i in kiz:
        file2.write(i)
with open ("/Users/BirkanMac/Desktop/Phton/ortak.txt" ,"w" ,encoding="utf-8") as file3:
    for i in ortak:
        file3.write(i)

with open ("/Users/BirkanMac/Desktop/Phton/erkek.txt" ,"w" ,encoding="utf-8") as file4:
    for i in erkek:
        file4.write(i)