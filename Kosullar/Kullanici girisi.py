print("""************************
Kullanici Girisi
************************""")

sys_kulanici = "bir"
sys_parola = "1234"

giris=3

while True:
    kul = input("kulanici adi: ")
    sif = input("sifreniz: ")
    if (sys_kulanici == kul and sys_parola==sif):
        print("Hosgeldin {}".format(sys_kulanici))
        break

    elif (sys_kulanici == kul and sys_parola!=sif):
        print("---parolan yanlis")
        giris = giris - 1

    else :
        print("---sistemde boyle birisi yok")
        giris = giris - 1
    if giris == 0:
        print("hakkin bitti...sifereni unuttuysan eyvah!..")
        break




