from tkinter import *
from tkinter import filedialog as take_x
import os
main_tikinter=Tk()
#------------Variables--------------------
sec = ""
test_label = Label(main_tikinter)
test_list = ["go", "school", "book", "spin"]
index = -1

#-------------Main Geometri--------------------
main_tikinter.geometry("800x400+350+200")
main_tikinter.minsize(300,150)
main_tikinter.maxsize(1100,700)
#main_tikinter.resizable(FALSE,TRUE)#Frame can't change

#-----------Title---------------------
main_tikinter.title("Movie Word")

#------------Setting Save--------------------
def Save_setting():
    global sec
    try:
        sec = sec.get()
    except(AttributeError):
        pass
    frame_x.destroy()


#------------Fonction 1--------------------
def saveAsFile():
    try:
        content = str("iii")
        url = take_x.asksaveasfile(mode='w', defaultextension=".txt",filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
        url.write(content)
        url.close()
        # self.parent.title("NotePad - Now Editing " + str(url.split('/')[-1]))
    except:
        return

#------------Enter--------------------
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

def Upload_Subtitle():
    Hide()
    take_from_pc = take_x.askopenfilename(initialdir = "/",title="Select a subtitle",filetypes=(("Subtitle files", "*.srt"), ("Text files", "*.txt")))
    test = Label(main_tikinter, text=take_from_pc)
    test.place(rely=0.6, relx=0.12)

def Upload_Movie():
    Hide()
    take_from_pc2 = take_x.askopenfilename(initialdir = "/",title="Select a movie",filetypes=(("Movie files", "*.mkv"), ("All files", "*.*")))
    test = Label(main_tikinter, text=take_from_pc2)
    test.place(rely=0.6, relx=0.12)

def Hide():
    for i in frame_s.winfo_children():
        i.destroy()
    lab_yourmovie.place_forget()
    input_movie_name.place_forget()
    entery_buton.place_forget()
    lab_yourUpload.place_forget()
    Upload_pc.place_forget()
    lab_movieUpload.place_forget()
    Upload_moviepc.place_forget()
#------------Main Menu--------------------
def Show():
    Save_setting()
    frame_s.place_forget()
    lab_yourmovie.place(rely=0.35, relx=0.12)
    input_movie_name.place(rely=0.4,relx=0.12)
    entery_buton.place(rely=0.5, relx=0.12)
    lab_yourUpload.place(rely=0.35, relx=0.4)
    Upload_pc.place(rely=0.4, relx=0.4)
    lab_movieUpload.place(rely=0.35, relx=0.65)
    input_movie_name.place(rely=0.4, relx=0.12)
    Upload_moviepc.place(rely=0.4,relx=0.65)

#-------------Language--------------------
frame_x = Frame(main_tikinter)
frame_s = Frame(main_tikinter)
#--------------Study--------------------
def Study():
    global index
    global test_label
    global frame_s
    Save_setting()
    index = (index) + 1
    test_label.destroy()
    frame_s = Frame(main_tikinter)
    frame_s.place(relx=.5, rely=.6, anchor="center")
    try:
        test_label = Label(frame_s, text=test_list[index],font="Helvetica 24",fg="gray22")
    except(IndexError):
        test_label = Label(frame_s, text="Done",font="Helvetica 24",fg="gray22")
    test_label.pack(fill="none", expand=True)

#--------------Setting--------------------
def Setting():
    global my_label
    global frame_x
    global sec
    Hide()

    frame_x.destroy()
    my_label = Label(main_tikinter, text="")
    frame_x = Frame(main_tikinter)
    frame_x.place(relx=.5, rely=.5, anchor="center") #,rowspan=2 # fill="none", expand=True

    def radio():
        global my_label
        my_label.destroy()
        if sec.get() == str("tr"):
            my_label = Label(frame_x, fg="black", text="Your language is Turkish")
        elif sec.get() == str("ru"):
            my_label = Label(frame_x, fg="black", text="Your language is Russian")
        else:
            my_label = Label(frame_x, fg="black", text="Your language is Spanish")
        my_label.pack(pady=10, fill="none", expand=True)


    sec = StringVar(main_tikinter,sec)

    values = {"Turkish - Türkçe": "tr",
              "Russian - Pусский": "ru",
              "Spanish - Español": "es",
              }
    for (text, value) in values.items():
        radi = Radiobutton(frame_x, text=text, fg="black", variable=sec, value=value, width=23, indicator=0,
                           background="#CCCCFF", command=radio)
        radi.pack(ipady=5)

#-------------Buton--------------------
quit=Button(text="Quite",fg="gray22",command=main_tikinter.quit)#bg"arkaplan"
quit.place(rely=0.1,relx=0.02)
#------------Label--------------------
lab1=Label(text="Movie Word", fg="gray22", font="Helvetica 24",pady=5,padx=10)#underline cursor="oclock"\n - \t
lab1.place(rely=0.0,relx=0.4)

#-------------Buton--------------------
exit_main_menu=Button(text="Main Menu",fg="gray22",command=Show)#bg"arkaplan",width=12,height=1
exit_main_menu.place(rely=0.17,relx=0.02)#relwidth=1,relheight=0.1

#-------------Entry--------------------
lab_yourmovie=Label(text="Choose your movie ", fg="gray22",font="Helvetica 13")
lab_yourmovie.place(rely=0.35,relx=0.12)
input_movie_name=Entry()
input_movie_name.place(rely=0.4,relx=0.12)
entery_buton=Button(text="Enter",width=13,height=1,fg="gray22",command=Test2)#bg"arkaplan"
entery_buton.place(rely=0.5,relx=0.12)

lab_yourUpload=Label(text="Upload subtitle from pc", fg="gray22",font="Helvetica 13")
lab_yourUpload.place(rely=0.35,relx=0.4)
Upload_pc=Button(text="Upload subtitle",width=13,height=1,fg="gray22",command=Upload_Subtitle)#bg"arkaplan"
Upload_pc.place(rely=0.4,relx=0.4)

lab_movieUpload=Label(text="Upload movie from pc", fg="gray22",font="Helvetica 13")
lab_movieUpload.place(rely=0.35,relx=0.65)
Upload_moviepc=Button(text="Upload Movie",width=13,height=1,fg="gray22",command=Upload_Movie)#bg"arkaplan"
Upload_moviepc.place(rely=0.4,relx=0.65)


# #-------------Buton  Menu--------------------
pdf=PhotoImage(file ="/Users/birkankalyon/phyton/Tkinter/icon/study.png")
photoimage0 = pdf.subsample(10,10)#small size
iknow_button=Button(text="Study",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage0, compound=TOP,command=Study)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.3)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "/Users/birkankalyon/phyton/Tkinter/icon/remember.png")
photoimage1 = pdf.subsample(10,10)#small size
remember_button=Button(text="Remember List",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage1, compound=TOP)#bg"arkaplan",width=7,height=5
remember_button.place(rely=0.1,relx=0.377)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "/Users/birkankalyon/phyton/Tkinter/icon/iknow.png")
photoimage2 = pdf.subsample(10,10)#small size
iknow_button=Button(text="Iknow List",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage2, compound=TOP)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.489)#relwidth=1,relheight=0.1

pdf=PhotoImage(file = "/Users/birkankalyon/phyton/Tkinter/icon/pdf.png")
photoimage3 = pdf.subsample(10,10)#small size
iknow_button=Button(text="PDF",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage3, compound=TOP, command=saveAsFile)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.567)#relwidth=1,relheight=0.1

setting=PhotoImage(file = "/Users/birkankalyon/phyton/Tkinter/icon/setting.png")
photoimage4 = setting.subsample(10,10)#small size
iknow_button=Button(text="Setting",width=7,height=4,fg="gray22",font="Helvetica 11",image = photoimage4, compound=TOP,command=Setting)#bg"arkaplan",width=7,height=5
iknow_button.place(rely=0.1,relx=0.64)#relwidth=1,relheight=0.1


# #-------------Check Buton--------------------
# lab_Check_Buton=Label(text="Do you want to took off this from subtitle?", fg="gray22")
# lab_Check_Buton.place(rely=0.7,relx=0.0)
# music_section=Checkbutton(text="Music Section")
# music_section.place(rely=0.8,relx=0.0)
# sound_section=Checkbutton(text="Sound Section")
# sound_section.place(rely=0.9,relx=0.0)


#--------------------Menu--------------------------
# def fake():
#     pass
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