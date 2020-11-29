
"""Bir aracın kilometrede ne kadar yaktığı ve
kaç kilometre yol yaptığı bilgilerini alın
ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."""

print("Masraf Hesap\n")

bir_km = int(input("Araciniz Bir galon kac mil gidiyor?: "))
benzin_fiyati=float(input("Suanki 1 galon benzin fiyatini girin: "))
km = int(input("Kac mil yol gideceksiniz?:"))
toplam=(benzin_fiyati/bir_km) * km
print("Toplamda:",int(toplam),"$ yolculuk maliyeti")
