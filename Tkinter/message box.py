from tkinter import *
#import tkMessageBox


root= Tk()


Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.grid(row=3,column=0)

root.mainloop()