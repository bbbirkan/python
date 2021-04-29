from tkinter import *
from random import randint

root = Tk()
root.title("Flashcard App!")
root.geometry("400x400")

frame1 = Frame(root, width=400, height=400, bg="red")
frame1.pack(fill="both")
frame2 = Frame(root, width=400, height=400,bg="blue")
frame2.pack(fill="both")
def bir():
	pass

a_button = Button(frame1, text="Addition Flashcards", command=bir,bg="red")
a_button.pack()
b_button = Button(frame2, text="Subtraction Flashcards", command=bir,bg="red")
b_button.pack()

a_button.pack()
b_button.pack()
# def subtract():
# 	hide_menu_frames()
# 	subtract_frame.pack(fill="both", expand=1)
#
# def hide_menu_frames():
# 	# Destroy the children widgets in each frame
# 	for widget in add_frame.winfo_children():
# 		widget.destroy()
#

root.mainloop()