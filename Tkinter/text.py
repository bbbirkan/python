from tkinter import *

root = Tk()
menu_bar = Menu(root)

def clicked(menu):
    menu.entryconfigure(1, label="Clicked!")
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label="An example item", command=lambda: clicked(file_menu))

file_menu.add_command(label="New", command=donothing)
file_menu.add_command(label="Open", command=donothing)
file_menu.add_command(label="Save", command=donothing)
file_menu.add_command(label="Save as...", command=donothing)
file_menu.add_command(label="Close", command=donothing)
menu_bar.add_cascade(label="File", menu=file_menu)



root.config(menu=menu_bar)
root.mainloop()