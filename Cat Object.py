class Cat():
    def __init__(self,name):
        self.name = name
        self.hungry=True
        self.dirty=True
    def cat_info(self):
        return f"{self.name}"

    def meow(self):
        return "Meooww!"

    def clean(self):
        self.dirty=True
        return f"Now:{self.name} is clean"


cat1=Cat("Chick")
print(cat1.cat_info(),cat1.meow(),cat1.clean())
