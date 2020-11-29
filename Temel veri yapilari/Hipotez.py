print("Pisagor Teoremi (Pisagor Bağıntısı)")
print("Formulumuz Hipotenüs uzunluğunu   a^2 + b^2 = c^2")
print("Lutfen sayilarinizi girin")
print( ('\nornek \nh^2 = 32 + 42\nh^2 = 9 + 16\nh^2 = 25\nh = √25\nh = 5 birim\n'))



a=int(input("a sayisi:"))
b=int(input("b sayisi:"))




c=a**2 + b**2

sonuc=c**0.5
print("Dik üçgenin dik olan iki kenarının hipotenüsu:",int(sonuc))

print("Extra: Bu dik ucgenin cevre uzunluklari:",int(sonuc+a+b),"'dir")

