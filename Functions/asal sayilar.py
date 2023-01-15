def asal(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi):  # 2 den buyuk sayiya kadar olan sayilar
            if (sayi % i == 0):
                return False
        return True


# fonksiyonumuzu olusturduk
