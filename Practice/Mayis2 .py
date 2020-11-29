# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


var1 = "birkan"
tipi = type(var1)
print(var1)


var1 = "birkan"
var2 = "caglar"
var3 = var1+var2

uzunluk=len(var3) 
     
# integer = (int) sayilar ornek 10
# string = (str)  kelime ornek "dogukan"
# double (float)  ondalikli sayilar ornek 10.0
# bosluk koyar bolum olusturur bu #%% uc bes kodun arasina basina sonuna koyulur.
#%%

#Float sayilarini yuvarlama rakamlara cevirme

float_sayi= 10.6

float(10)

int(float_sayi)# sonuc 10 cikacak
round(float_sayi)# somnuc 11 cikacak

# yazi formatini integer sayilara cevirmek

stringyazi = "55" 

int(stringyazi)
#olup olmadugunu ogrenmek icin consolda yaz
type(int(stringyazi))
#sonuc int yani dogru
#%%
#yeni fonksiyon yaratma
sayi1 = 30 #ornek sayilar olacak
sayi2 = 60

# Kendi fonksiyonunu olusturma ayni type ya da print fonksiyonlari gibi 

def ilkfonksiyon(a,b):
        output =((a*b)+(a+b))/4
        return output
# Simdi sira deneme 

deneme = ilkfonksiyon(sayi1,sayi2)
#sonuc 472.5 cikiyor spider consola deneme yazarsaniz 

#ikinci fonksiyonumuzu yazalim outputsuz  icine illa birsey doldurmak zorundada degiliz
def ikincifon():
    """
    Bu yere fonksiyonun yorumunu
    ne ise yaradigini
    bu isareterle ve 
    onemli tab boslugu birakarak
    yazabilirisiniz
    """
    print("buraya ne yazarsam o cikacak konsolda boyle cikacak consola ikincifon() yaz")
    
    
#simdi sira cemberin cevresini bulma fonksiyonu yapalim
#2*pi*r 
    
def cember_hesap(r): 
    """ 
    buraya tanim yazin baskasi da anlasin diye
    cember cevresi hesapla
    input(parametre) : r
    output = cemberin cevresi
    
    """
    output = 2*3.14*r
    return output
#cember_hesap(2)
#Out[8]: 12.56 bu sonucu aldik consolda
    
#%%
# default fonksiyonlari yapmak ayni ornek ile gosterecem pi sayisina dikkat


def cember_hesap(r,pi=3.14): 
    """ 
    buraya tanim yazin baskasi da anlasin diye
    cember cevresi hesapla
    input(parametre) : r
    output = cemberin cevresi
    
    """
    output = 2*pi*r
    return output

#cember_hesap(2)
#Out[10]: 12.56 ayni sonuc yine
    
#%%
    
#flexible fonksiyonlar
    
def hesapla(boy,kilo,*onemsiz): 
    output = (boy+kilo)*onemsiz[1]
    return output
#neden *onemsiz yazdigini soylemedi ama onemsiz yazarsan calismiyor 
#hesapla(2,1,5,10,15)  2 boy  - 1 kilo - onemsiz[1] photonda 0 1 2 3 diye saydigindan onemsiz sayialrdan ikinci siradakini aliyor 
#Out[12]: 30 
    # sonucta (2+1)*10
 
#%%    
#test bolumu kucuk projemiz olsun 
    
    
#int variable yas
#string name isim
#fonksiyonumuz
#print fonksiyonu print(type(),len,float())
#*args soyisim -  olacak
#sabit parametremizde - default paramatre yani ayakkabi numasi olacak


yas = 32
isim = "birkan"
soyisim = "kalyon"

def fonk_test(yas,name,*args,ayakkabi_no=42):
    print("Fonksiyonu yazanin ismi-",isim,"Yasi-",yas,"Ayakkabi numarasi-",ayakkabi_no)
    print(type(ayakkabi_no))
    print(float(yas))
    
    output = args[0]*yas
    return output

fonksiyonumuzu_deniyoruz = fonk_test(yas,isim,soyisim)
print("SONUC:",fonksiyonumuzu_deniyoruz)

#Fonksiyonu yazanin ismi- birkan Yasi- 32 Ayakkabi numarasi- 42
#<class 'int'>
#32.0
#SONUC: kalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyonkalyon

