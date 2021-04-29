from tkinter import *
import tkinter as tk
from tkinter import font
eng="book"
tr="kitap"
text0=("Movie sentences test")
text1="Lorem ipsum, or lipsum as it is sometimes known, " \
          "is dummy text used in laying out print, graphic or" \
          " web designs. The passage is attributed to an unknown."
text3="Lorem Ipsum, dizgi ve baskı" \
           " endüstrisinde kullanılan mıgır " \
           "metinlerdir. Lorem Ipsum, adı bilinmeyen" \
           " bir matbaacının bir hurufat numune kitabı" \
           " oluşturmak üzere bir yazı galerisini alarak"

root = Tk()
root.geometry("690x370")
#-------------Remember------------------
frame_show_text_all=Frame(root)
frame_show_text_all.pack()

frame_show_buton=Frame(frame_show_text_all,width=618,height=30)
frame_show_buton.pack()

buton_delete = Button(frame_show_buton, text="Delete",fg="gray22")#,command=root.destroy
buton_delete.place(relx = 0.0, rely = 0.0)
# buton_delete.grid(row=0, column=0,ipadx=14,columnspan=3,padx=84)
# -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
# buton_delete.pack( side = LEFT,padx=0,pady=3)
buton_add_I_know_word = Button(frame_show_buton, text="Add know word list",fg="gray22")
buton_add_I_know_word.place(relx = 0.38, rely = 0.0)# anchor = NE
# buton_add_I_know_word.grid(row=0, column=3,padx=180)
# buton_add_I_know_word.pack(side= LEFT,padx=0)


def Remember(in_movie_text,show_eng_text,show_tra_text,eng_word,tra_word):
    pass
    show_text_word = eng_word+"\n----\n"+tra_word
    show_eng_text_print="("+in_movie_text+")\n"+show_eng_text
    main_font = font.names()[1]
    original_background = root.cget("background")  # solition for backrgound

    frame_show_main = Frame(frame_show_text_all)
    frame_show_main.pack()

    frame_fake = Label(frame_show_main,borderwidth=5, height=2, width=15, relief="ridge", font=main_font + " 43")
    frame_fake.pack()

    main_show_text = Text(frame_fake, height=4, width=40, wrap=WORD, pady=4,
                          background=original_background,fg="gray22")
                          #background='systemWindowBody''SystemButtonFace'
    main_show_text.tag_configure("center", justify='center')
    main_show_text.insert(1.0, show_eng_text_print)
    main_show_text.tag_add("center", "1.0", "end")
    main_show_text.configure(state='disabled')  # ,padx=115
    main_show_text.pack()

    main_show_text2 = Text(frame_fake, height=3, width=40, wrap=WORD, foreground="gray22",
                          background=original_background, pady=0, font=main_font + " 23")
    main_show_text2.tag_configure("center", justify='center')
    main_show_text2.insert(1.0, show_text_word)
    main_show_text2.tag_add("center", "1.0", "end")
    main_show_text2.configure(state='disabled')
    main_show_text2.pack()

    main_show_text3 = Text(frame_fake, height=4, width=40, pady=4,wrap=WORD, foreground="gray22",
                          background=original_background)
    main_show_text3.tag_configure("center", justify='center')
    main_show_text3.insert(1.0, show_tra_text)
    main_show_text3.tag_add("center", "1.0", "end")
    main_show_text3.configure(state='disabled')
    main_show_text3.pack()


Remember(text0,text1,text3,eng,tr)


buton_next= Button(frame_show_text_all, text="Next",fg="gray22")
buton_next.pack(fill="none")
buton_pronunciation = Button(frame_show_text_all, text="Pronunciation",fg="gray22")
buton_pronunciation.pack(fill="none")
tk.mainloop()