import tkinter as tk

root = tk.Tk()
e1 = tk.Entry(root)
e1.pack()


def handleReturn(event):
    print("return: event.widget is",event.widget)
    print("focus is:", root.focus_get())
    print("Type is:", e1.get())

e1.bind("<Return>", handleReturn)

root.mainloop()

import tkinter as tk

root = tk.Tk()
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.pack()
e2.pack()

def handleReturn(event):
    print("return: event.widget is",event.widget)
    print("focus is:", root.focus_get())

e1.bind("<Return>", handleReturn)

root.mainloop()