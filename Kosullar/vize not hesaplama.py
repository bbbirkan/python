
''' A sayısının Yüzde B'si = (A / 100) x B

    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF'''

vize1= int(input("Birinci Vize Notunu gir: "))
vize2= int(input("Ikinci Vize Notunu gir: ") )
final= int(input("Final Vize Notunu gir: ")  )

yil_sonu= (vize1/100)*30 + (vize2/100)*30 + (final/40)

if (yil_sonu >= 90):
    print("Yil Sonu toplam notun:{:.1f} AA".format(yil_sonu))
elif(yil_sonu >= 85):
    print("Yil Sonu toplam notun:{:.1f} BA".format(yil_sonu))
elif(yil_sonu >= 80):
    print("Yil Sonu toplam notun:{:.1f} BB".format(yil_sonu))
elif(yil_sonu >= 75):
    print("Yil Sonu toplam notun:{:.1f} CB".format(yil_sonu))
elif(yil_sonu >= 70):
    print("Yil Sonu toplam notun:{:.1f} CC".format(yil_sonu))
elif(yil_sonu >= 65):
    print("Yil Sonu6toplam notun:{:.1f} DC".format(yil_sonu))
elif(yil_sonu >= 60):
    print("Yil Sonu toplam notun:{:.1f} DD".format(yil_sonu))
elif(yil_sonu >= 55):
    print("Yil Sonu toplam notun:{:.1f} FD".format(yil_sonu))
elif(yil_sonu < 55):
    print("Yil Sonu toplam notun:{:.1f} FF".format(yil_sonu))