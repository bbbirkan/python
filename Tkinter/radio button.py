from tkinter import *
master = Tk()
master.geometry("375x175")

#-------------Language--------------------
my_label = Label(master, text="")
frame_x = Frame(master)
frame_x.pack(fill="none", expand=True)
def radio():
    global my_label
    my_label.destroy()
    if v.get() == str("tr"):
        my_label = Label(frame_x,fg="black", text="Your language is Turkish")
    elif v.get() == str("ru"):
        my_label = Label(frame_x,fg="black", text="Your language is Russian")
    else:
        my_label = Label(frame_x,fg="black", text="Your language is Spanish")
    my_label.pack(pady=10,fill="none", expand=True)
v = StringVar(master, "tr")
values = {"Turkish - Türkçe": "tr",
          "Russian - Pусский": "ru",
          "Spanish - Español": "es",
          }
for (text, value) in values.items():
    print(value),print(text)
    radi=Radiobutton(frame_x, text=text, fg="black", variable=v,value=value,width=23,indicator=0,background="#CCCCFF", command=radio)
    radi.pack(ipady=5)
mainloop()