from tkinter import *
main_tikinter=Tk()
#-------------Main Geometri--------------------
main_tikinter.geometry("800x400+350+200")
main_tikinter.minsize(300,150)
main_tikinter.maxsize(1100,700)
#main_tikinter.resizable(FALSE,TRUE)#Frame can't change
#-----------Title---------------------
main_tikinter.title("Movie Word")

#------------Fonction 1--------------------
def Open_folder():
    pass

#------------Fonction 2--------------------
def Delete_entry():
    input_movie_name.delete(0,END)
    pass

#------------Fonction 3--------------------
def Test2():
    pass
#-------------Language--------------------
my_label = Label(main_tikinter, text="")
frame_x = Frame(main_tikinter)
frame_x.grid(row=13, column=3)#fill="none", expand=True
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
v = StringVar(main_tikinter, "tr")
values = {"Turkish - Türkçe": "tr",
          "Russian - Pусский": "ru",
          "Spanish - Español": "es",
          }
for (text, value) in values.items():
    print(value),print(text)
    radi=Radiobutton(frame_x, text=text, fg="black", variable=v,value=value,width=23,indicator=0,background="#CCCCFF", command=radio)
    radi.pack(ipady=5)
#-------------Frame1--------------------
frame1=Frame()
frame1.grid(row=0,column=0)
#frame1.grid(row=0,column=0)
#------------Label--------------------
lab1=Label(text="Movie Word", fg="gray22", font="Helvetica 24")#underline cursor="oclock"\n - \t
lab1.grid(row=1,column=2)

#-------------Frame2--------------------
frame2=Frame()
frame2.grid(row=2,column=0)

#-------------Entry--------------------
input_movie_name=Entry()
#input_movie_name.place(rely=0.9,relx=0.0)
#-------------Buton--------------------
exit_mainmenu=Button(frame2,text="Exit Mainmenu",width=13,height=1,fg="gray22")#bg"arkaplan"
exit_mainmenu.grid(row=0,column=0,padx=6)

delete=Button(text="Delete Entery",width=13,height=1,fg="gray22",command=Delete_entry)#bg"arkaplan"
delete.grid(row=4,column=0)

quit=Button(text="Quite",fg="gray22",command=main_tikinter.quit)#bg"arkaplan"
quit.grid(row=5,column=0)

#-------------Check Buton--------------------
lab_Check_Buton=Label(text="Do you want to took off this from subtitle?", fg="gray22")
lab_Check_Buton.grid(row=6,column=0)
music_section=Checkbutton(text="Music Section")
music_section.grid(row=7,column=0)
sound_section=Checkbutton(text="Sound Section")
sound_section.grid(row=7,column=2)





mainloop()