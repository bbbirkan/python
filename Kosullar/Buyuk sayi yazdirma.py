a= float(input("Birinci Sayi:"))
b= float(input("Ikinci Sayi:"))
c= float(input("Ucuncu Sayi:"))




if (a>b ) and (a>c ):
    print("buyuk sayi Birinci Sayi", int(a))
elif(b>a) and (b>c ):
    print("buyuk sayi Ikinci Sayi", int(b))
elif(c>a) and (c>b):
    print("buyuk sayi Ucuncu Sayi", int(c))
else:
    print('Sayilar esit')

