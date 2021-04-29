from tkinter import *
import tkinter as tk
from tkinter import font

eng = "book"
tr = "kitap"

root = Tk()
root.geometry("600x270")
# -------------Remember------------------
s_frame_show_text_all = Frame(root)
s_frame_show_text_all.pack()

s_buton_show_frame = Frame(s_frame_show_text_all)
s_buton_show_frame.pack(fill=BOTH)
s_buton_add_I_know_word = Button(s_buton_show_frame, text="Add I know this word", fg="gray22")
s_buton_add_I_remmaber = Button(s_buton_show_frame, text="Add remember word list", fg="gray22")  # ,command=root.destroy
s_buton_add_I_know_word.grid(row=0, column=0)
s_buton_add_I_remmaber.grid(row=0, column=1,padx=104)

main_font = font.names()[1]
frame_show_main = Frame(s_frame_show_text_all)

def Study_show(word):
    frame_show_main.pack()
    word_study = Label(s_frame_show_text_all, text=word, borderwidth=5,
                       height=2, width=15, relief="ridge", font=main_font + " 43")
    word_study.pack(fill="none",side=LEFT)

Study_show(eng)
s_buton_tra = Button(s_frame_show_text_all, text="Next", width=6,fg="gray22")
s_buton_tra.pack(pady=0,side=RIGHT)
s_buton_next = Button(s_frame_show_text_all, text="Show",width=2,height=1, fg="gray22",font=main_font + " 13")
s_buton_next.pack(fill="none",side=LEFT,padx=3)

tk.mainloop()