print('Diskriminant Formülü (Delta) ile 2. derceden 1 bilinmeyen denklemler')
print("Formulumuz Delta = b**2+4a*c")
print("Cikan sonuc kokleri bulma\nBirinci kok:(-b - delta^2 0.5)/(2*a)\nIkinci kok:(-b + delta^2 0.5)/(2*a)\n ")


print("Lutfen sayilarinizi girin")

a=int(input("a sayisi:"))
b=int(input("b sayisi:"))
c=int(input("c sayisi:"))


delta = b ** 2 - 4*(a*c)


birinci =(-b - delta**0.5) / (2*a)
ikinci =(-b + delta**0.5) / (2*a)



print("Birincikok: {}\nIkincikok {}\n".format(birinci,ikinci))
