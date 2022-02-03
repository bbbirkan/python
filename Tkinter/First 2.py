from tkinter import *
main_tikinter=Tk()
#-------------Main Geometri--------------------
main_tikinter.geometry("800x400+350+200")
main_tikinter.minsize(300,150)
main_tikinter.maxsize(1100,700)
#main_tikinter.resizable(FALSE,TRUE)#Frame can't change
#-----------Title---------------------
main_tikinter.title("Movie Word")

def fake():
    pass

#------------Fonction 1--------------------
def Open_folder():
    pass

#------------Fonction 2--------------------


#------------Fonction 3--------------------
test_label = Label(main_tikinter)
test_list = ["1333", "2", "3", "4"]

index = -1
def Test2():
    global index
    global test_label
    index = (index) + 1
    test_label.destroy()
    try:
        test_label = Label(main_tikinter, text=test_list[index])
    except(IndexError):
        test_label = Label(main_tikinter, text="Done")
    test_label.place(rely=0.6, relx=0.12)
    # test_label = Label(main_tikinter, text=input_movie_name.get())


def Delete_entry():
    pass
    #input_movie_name.delete(0,END)


def frame3():
    Hide()
    frame12.place(rely=0.65,relx=0.139)

def frame():
    Hide()
    frame2.place(rely=0.65,relx=0.139)

def Hide():
    # test_label = Label(main_tikinter)
    # test_label.place_forget()
    # test_label.destroy()
    frame12.place_forget()
    frame2.place_forget()


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

#-------------Buton--------------------
quit=Button(text="Quite",fg="gray22",command=main_tikinter.quit)#bg"arkaplan"
quit.place(rely=0.1,relx=0.02)
#------------Label--------------------
lab1=Label(text="Movie Word", fg="gray22", font="Helvetica 24",pady=5,padx=10)#underline cursor="oclock"\n - \t
lab1.place(rely=0.0,relx=0.4)

#-------------Frame1--------------------
frame2=Frame(main_tikinter,width=550,height=100,bd=2,bg="blue", relief="sunken")
labf=Label(frame2,text="Movie Word", fg="gray22", font="Helvetica 24",pady=5,padx=10)#underline cursor="oclock"\n - \t
labf.grid(row=0, column=0, padx=200, pady=30)

frame12=Frame(main_tikinter,width=550,height=100,bd=2,bg="blue", relief="sunken")
labf1=Label(frame12,text="Test", fg="gray22", font="Helvetica 24",pady=5,padx=10)
labf1.grid(row=0, column=0, padx=200, pady=30)
#-------------Frame2--------------------
# frame1=Frame(main_tikinter,width=550,height=100,bd=2,bg="blue", relief="sunken")
# frame1.place(rely=0.65,relx=0.155)



#-------------Buton--------------------
exit_main_menu=Button(text="Exit Mainmenu",fg="gray22")#bg"arkaplan",width=12,height=1
exit_main_menu.place(rely=0.17,relx=0.02)#relwidth=1,relheight=0.1



pdf=PhotoImage(file ="icon/study.png")
photoimage0 = pdf.subsample(10,10)#small size
iknow_button=Button(text="Iknow List",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage0, compound=TOP)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.3)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "icon/remember.png")
photoimage1 = pdf.subsample(10,10)#small size
remember_button=Button(text="Remember List",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage1, compound=TOP)#bg"arkaplan",width=7,height=5
remember_button.place(rely=0.1,relx=0.377)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "icon/iknow.png")
photoimage2 = pdf.subsample(10,10)#small size
iknow_button=Button(text="Iknow List",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage2, compound=TOP)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.489)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "icon/pdf.png")
photoimage3 = pdf.subsample(10,10)#small size
iknow_button=Button(text="PDF",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage3, compound=TOP)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.567)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "icon/setting.png")
photoimage4 = pdf.subsample(10,10)#small size
iknow_button=Button(text="Setting",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage4, compound=TOP)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.64)#relwidth=1,relheight=0.1


#-------------Entry--------------------
lab_yourmovie=Label(text="Choose your movie ", fg="gray22",font="Helvetica 13")
lab_yourmovie.place(rely=0.35,relx=0.12)
input_movie_name=Entry()
input_movie_name.place(rely=0.4,relx=0.12)
entery_buton=Button(text="Enter",width=13,height=1,fg="gray22",command=Test2)#bg"arkaplan"
entery_buton.place(rely=0.5,relx=0.12)


lab_yourUpload=Label(text="Upload subtitle from pc", fg="gray22",font="Helvetica 13")
lab_yourUpload.place(rely=0.35,relx=0.4)
Upload_pc=Button(text="Upload subtitle",width=13,height=1,fg="gray22",command=frame)#bg"arkaplan"
Upload_pc.place(rely=0.4,relx=0.4)

lab_movieUpload=Label(text="Upload movie from pc", fg="gray22",font="Helvetica 13")
lab_movieUpload.place(rely=0.35,relx=0.65)
Upload_moviepc=Button(text="Upload Movie",width=13,height=1,fg="gray22",command=frame3)#bg"arkaplan"
Upload_moviepc.place(rely=0.4,relx=0.65)




# #-------------Check Buton--------------------
# lab_Check_Buton=Label(text="Do you want to took off this from subtitle?", fg="gray22")
# lab_Check_Buton.place(rely=0.7,relx=0.0)
# music_section=Checkbutton(text="Music Section")
# music_section.place(rely=0.8,relx=0.0)
# sound_section=Checkbutton(text="Sound Section")
# sound_section.place(rely=0.9,relx=0.0)


#--------------------Menu--------------------------
# #define menu for windows
# first_menu=Menu(main_tikinter)
# main_tikinter.config(menu=first_menu)
# # #create menu
# setting_menu=Menu(first_menu)
# first_menu.add_cascade(label="Account", menu=first_menu)
# setting_menu.add_command(Label="New",command=fake)
# #setting_menu.add_command(Label="Exit",command=main_tikinter.quit)


#menu for mac cross platform
# mymenubar = Frame(main_tikinter, relief='raised', bd=1)
# mymenubar.grid(row=0,column=0)#sticky=W+E
#
# mymenubutton = Menubutton(mymenubar, text='File', )
# mymenubutton.grid(row=0,column=0)
#
# mymenu = Menu(mymenubutton, tearoff=0)
# mymenubutton['menu'] = mymenu
# mymenu.add('command', label='Open') # Add Sub Menu 1
#
# mb2 = Menubutton(mymenubar, text='Edit', )
# mb2.grid(row=0,column=1)
# menudd = Menu(mb2, tearoff=0)
# mb2['menu'] = menudd
# menudd.add('command', label='Cut') # Add Sub Menu 2
# menudd.add('command', label='ook') # Add Sub Menu 3
# myframe1 = Frame(main_tikinter, bd=2, relief=SUNKEN)
# myframe1.grid(row=0,column=1)
# #-----------------Image--------------------
# from PIL import ImageTk, Image
# first_image=ImageTk.PhotoImage(Image.open("test.png"))
# image_label=Label(imag=first_image)
# image_label.place(rely=0.6, relx=0.0)

mainloop()