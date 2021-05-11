from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading



root = Tk()
root.geometry("700x360")
frame_progress=Frame(root)
frame_progress.pack()
label_show_choose1 = Label(frame_progress, text="Loading:", fg="gray22")
label_show_choose1.pack()
progress = Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
#btn = Button()
def traitement():
    def Progress_fonction():
        progress.pack()
        #progress.start()
        #time.sleep(2)
        progress['value'] = 20
        time.sleep(1)
        progress['value'] = 50
        time.sleep(1)
        progress['value'] = 75
        for i in range(10):
            print(i)
            time.sleep(0.04)
        progress['value'] = 100
        #progress.stop()
        progress.destroy()
        btn.forget()
        btn['state'] = 'normal'
        btn['state'] = 'disabled'
    threading.Thread(target=Progress_fonction).start()



btn = Button(text='Traitement', command=traitement())
btn.pack()





root.mainloop()