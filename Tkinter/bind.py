from tkinter import *
main_tikinter=Tk()
main_tikinter.geometry("160x200+350+200")

def clear_text(event):
    event.widget.delete(0, "end")
label_mac_adress = Label(main_tikinter, text="Mac Adress", fg="gray22", font="Helvetica 9")
mac_adress=Entry(main_tikinter,width=15)
mac_adress.insert(0, "ff.ff.ff.ff.ff.ff")
mac_adress.bind("<FocusIn>", clear_text)


main_tikinter.mainloop()
