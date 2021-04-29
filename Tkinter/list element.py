
from tkinter import *
from tkinter import ttk

root = Tk()
def func(name):
    print(name)
mylist = ['item1', 'item2', 'item3']
for item in mylist:
    button = Button(root, text=item, command=lambda x=item: func(x))
    button.pack()

root.mainloop()