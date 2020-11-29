


def sayi_yaz(a):
    b = str(a)
    soz = {"1": "bir", "2": "iki", "3": "uc", "4": "dort", "5": "bes", "6": "alti", "7": "yedi", "8": "sekiz",
           "9": "dokuz", }
    ondalik = {"1": "on", "2": "yirmi", "3": "otuz", "4": "kirk", "5": "elli", "6": "altmis", "7": "yetmis",
               "8": "seksen", "9": "doksan", }

    while True:
        if b[1] == "0":
            print(ondalik[b[0]])
            break
        else:
            print(ondalik[b[0]], soz[b[1]])
            break

a=input("iki basamakli sayi yaz\n")
sayi_yaz(a)

