


print("""
*********************************
Faktoriel
********************************
Cikmak icin 'c' basin""")
'''
n!=n.(n-1)!
n!=n.(n-1).(n-2)!
n!=n.(n-1).(n-2).(n-3)!

0!=1
1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120

n! = n * (n-1)!

'''
while True:
    x = input("Faktorunu almak istedigini sayiyi girin yada c basin :")
    if(x == "c"):
        print("cikis yapildi...")
        break
    else:
        x = int(x)
        f=1

        for i in range(1,x+1):
            print("faktor !",i,'=')
            f=f*i
            print(f,"'dir")







