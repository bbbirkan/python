
#Beden kilo endexi
#formul=vucut agirligi/boyunun karesine
print("Beden Kitle İndeksinizi bulalim")

boy=float(input("Boyunuz"))
kilo=int(input("Kilonuz"))

x= kilo / boy**2

print("Beden kilo endesiniz:",(x))

if (x <= 18.5):
    print("Beden kilo endesiniz:{:.2f}".format(x),"Zayifsisiniz" )

elif (x <= 25):
    print("Beden kilo endesiniz:{:.2f}".format(x),"Normal" )

elif (x <= 30 ):
    print("Beden kilo endesiniz:{:.2f}".format(x),"dana gibi olmussun" )

else :
    print("Beden kilo endesiniz:{:.2f}".format(x), "oha lan biraz az ye")



