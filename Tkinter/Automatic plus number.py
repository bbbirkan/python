import tkinter as tk
from tkinter import *
root=tk.Tk()

X0=IntVar()
X1=IntVar()

E0=Entry(root, textvariable=X0)
E0.grid()
E1=Entry(root, textvariable=X1)
E1.grid()

def Add():
    x=X0.get()
    y=X1.get()
    E1.delete(0,END)
    E1.insert(END,x+y)

B=Button(root, command=lambda: Add())
B.grid()

root.mainloop()