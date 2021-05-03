from tkinter import *
root = Tk()
def Callback_entry(auto_entry):
    print (auto_entry.get())



auto_entry = StringVar()
auto_entry.trace("w", lambda name, index, mode, auto_entry=auto_entry: Callback_entry(auto_entry))

Entry_search_movie = Entry(root, textvariable=auto_entry)
Entry_search_movie.pack()
Entry_search_movie.focus()
root.mainloop()
