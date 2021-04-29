from tkinter import *

root = Tk()

L3 = Label(root, text="This")
L2 = Label(root, text="That")

L2.pack()
L3.pack()
#"flat", "raised", "sunken", "ridge", "solid","groove"
l1 = Label(root, text="This", borderwidth=2, fg="red", relief="solid")
l1.pack()
root.mainloop()