sekil=input("üçgenin mi dörtgenin mi tipini bulmak istiyorsun?\n"
            " Buraya 'ucgen' yada 'dortgen' yaz:")

if (sekil == "dortgen"):
     k1 = int(input(" 1.kenari girin:"))
     k2 = int(input(" 2.kenari girin:"))
     k3 = int(input(" 3.kenari girin:"))
     k4 = int(input(" 4.kenari girin:"))
     if (k1 == k2 == k3 == k4):
         print("Bu bir karedir. Butun kenarlari birbirine esit")
     elif(k1 == k3 and k2 == k4 ):
         print("Bu bir dikdortgendir. iki kenarlari birbirine esit")
     else:
         print(" Bu bir dört kenarı olan bir çokgendir.")
elif (sekil == "ucgen"):
    a = int(input(" 1.kenari girin:"))
    b = int(input(" 2.kenari girin:"))
    c = int(input(" 3.kenari girin:"))
    if ((a < b + c and b < a + c and c < a + b) and (a > abs(b - c) and b > abs(a - c) and c > abs(a - b))):
       if (a == b or b == c or c == a):
        print(" Bu üçgen ikizkenardir")
       else:
        (print(" Bu Çeşitkenar ucgendir"))

    else:
        print("Malmisin orta okulada mi gitmedin Üçgen degil bu :)")

"""Üçgende ;  Herhangi bir kenar , diğer iki kenarın toplamından küçük olmak zorundadır.
   Üçgende ; bir kenar , diğer iki kenarın farkından büyük olmak zorundadır.
 
 a b c   (a<b+c and b<a+c and c<a+b) or (a>abs(b-c) and b>abs(a-c)  and  c>abs(a-b))
 """
