from tkinter import *
from tkinter import font
root = Tk()

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

def Remember(in_movie_text,show_eng_text,show_tra_text,eng_word,tra_word):
    pass
    show_text_word = eng_word+"\n----\n"+tra_word
    show_eng_text_print="("+in_movie_text+")\n"+show_eng_text
    main_font = font.names()[1]
    original_background = root.cget("background")  # solition for backrgound

    frame_show_main = Frame(root)
    frame_show_main.pack()
    main_show_text = Text(frame_show_main, height=4, width=85, wrap=WORD, pady=0,
                          background=original_background,fg="gray22")
                          #background='systemWindowBody''SystemButtonFace'

    main_show_text.tag_configure("center", justify='center')
    main_show_text.insert(1.0, show_eng_text_print)

    main_show_text.tag_add("center", "1.0", "end")
    main_show_text.configure(state='disabled')  # ,padx=115
    main_show_text.pack()

    main_show_text = Text(frame_show_main, height=3, width=85, wrap=WORD, foreground="gray22",
                          background=original_background, pady=2, font=main_font + " 23")
    main_show_text.tag_configure("center", justify='center')
    main_show_text.insert(1.0, show_text_word)
    main_show_text.tag_add("center", "1.0", "end")
    main_show_text.configure(state='disabled')
    main_show_text.pack()

    main_show_text = Text(frame_show_main, height=4, width=85, pady=15,wrap=WORD, foreground="gray22",
                          background=original_background)
    main_show_text.tag_configure("center", justify='center')
    main_show_text.insert(1.0, show_tra_text)
    main_show_text.tag_add("center", "1.0", "end")
    main_show_text.configure(state='disabled')
    main_show_text.pack()
Remember(text0,text1,text3,eng,tr)

root.mainloop()