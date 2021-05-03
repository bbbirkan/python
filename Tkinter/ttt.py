from tkinter import *
from tkinter import messagebox


def listMessageBox(arr):
    window = Tk()
    listbox = Listbox(window , width=10, height=5)
    listbox.pack()  # adds listbox to window
    [listbox.insert(END, row) for row in arr]  # one line for loop
    window.mainloop()


arr = ['a', 'b', 'c', '1', '2', '3']

listMessageBox(arr)