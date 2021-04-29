from tkinter import *
from tkinter import font
root = Tk()
# main_show_text = Text(root, height=5, width=45, wrap=WORD, pady=0,background="red",fg="gray22")
# main_show_text.pack()
main_font = font.names()[1]
word_study = Label(root, text="school", borderwidth=5, height=2, width=15,relief="ridge",font=main_font + " 43")
word_study.pack()

root.mainloop()