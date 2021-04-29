from tkinter import *  # from tkinter import *
from tkinter import *
root = Tk()
myFrame = Frame(root).place(x=50, y=100)
myList = ["a", "b", "c"]
for i in myList:
    Label(myFrame, text = "● "+i).pack() #you can use a bullet point emoji.
root.mainloop()