import tkinter
from tkinter import *


def callback(input):
    print(input)
    return True


root = Tk()

e = Entry(root)
e.pack()
reg = root.register(callback)

e.config(validate="key",validatecommand=(reg, 'd'))

root.mainloop()