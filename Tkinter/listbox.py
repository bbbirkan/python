from tkinter import *

root = Tk()
root.geometry("200x260")
frame = Frame(root)
frame.pack()

Birkan=["test","birkan","icine","bak","tara","basar","dene","choose","trust","last","items"]
lb = Label(root, text="")

def Choose_movie_list(self):
    global lb
    #print(mylist.curselection())
    lb.destroy()
    print(mylist.get(mylist.curselection()))
    lb=Label(root,text=str(mylist.get(mylist.curselection())),fg="red")
    lb.pack()


    #print(mylist.curselection())
def Accept_movie():
    print(mylist.get(mylist.curselection()))
    print(enter_movie.get())
    lb2 = Label(root, text="you choose !!!"+str(mylist.get(mylist.curselection())), fg="red")
    lb2.pack()
    mylist.config(state=DISABLED)
    buton.config(state=DISABLED)


def Entry_test():
    print(enter_movie.get())



frame_TAKE = Frame(root)
frame_TAKE.pack()
enter_movie=Entry(frame_TAKE,text="test")
enter_movie.bind('<<ListboxSelect>>',Choose_movie_list)
enter_movie.pack()
myscroll = Scrollbar(frame_TAKE)
myscroll.pack(side=RIGHT,fill = Y)                                            
mylist = Listbox(frame_TAKE, yscrollcommand = myscroll.set )
for line in Birkan:
    mylist.insert(END, line)
    mylist.bind('<<ListboxSelect>>',Choose_movie_list)    


mylist.pack(side=LEFT, fill=BOTH)
myscroll.config(command=mylist.yview)

buton=Button(root, text='Print', command=Accept_movie)
buton.pack()



root.mainloop()