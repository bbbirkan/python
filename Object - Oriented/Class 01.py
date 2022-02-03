# class student:
#     name_surname=""
#     point1=0
#     point2=0
#
# st=student()
# st.name_surname=input("Enter the name:")
# st.point1=int(input("Math 1"))
# st.point2=int(input("Math 2"))
#
# avarege=(st.point1+st.point1/2)
# print(avarege)
#
# class Product:
#     def __init__(self,name,model,price,isActive=False):
#         self.name=name
#         self.model=model
#         self.price=price
#         self.isActive=isActive
# p1=Product("Alfa Remeo","2002","2000",True)
# p2=Product("Volvo","2020","1500")
# print(p1.name,p2.isActive)

class Test:
    def __init__(self, username,name,surname,birthday):
        self.username = username
        self.name =name
        self.surname = surname
        self.birthday=birthday
    def info(self):
        return f"{self.username} kullanici adiyla {self.name}{self.surname} kayit olmustur"
    def Calculate(self):
        return f"{2022-self.birthday} Yasinda"

u1 = Test("kkKalyon","Birkan","Kalyon",1987)
print(u1.info(),u1.Calculate())

