#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()
window.title('My Window')

window.geometry('500x300')


l = tk.Label()

def print_selection():
    global l
    l.destroy()
    value = lb.get(lb.curselection())
    l = tk.Label(window, font=('Arial', 12), width=10, text=value)
    l.pack()




b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1, 2, 3, 4))
lb = tk.Listbox(window, listvariable=var2)

list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()