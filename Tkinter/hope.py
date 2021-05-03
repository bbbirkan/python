import tkinter as tk

root=tk.Tk()               #create window

frame1=tk.Frame(root)                                #container: root
frame1.pack(fill=tk.BOTH,expand=True)
frame1.columnconfigure(0,weight=1)
frame1.rowconfigure(0,weight=1)
frame1.rowconfigure(1,weight=1)

listbox=tk.Listbox(frame1)                            #container: frame1
listbox.grid(row=0,rowspan=2,column=0,padx=5,pady=5,sticky='nsew')

btn1=tk.Button(frame1,text='Demo1')                   #container: frame1
btn1.grid(row=0,column=1, padx=5, pady=5)

btn2=tk.Button(frame1,text='Demo2')                   #container: frame1
btn2.grid(row=1,column=1, padx=5, pady=5)

frame2=tk.Frame(root)                                 #container: root
frame2.pack()

btn3=tk.Button(frame2,text='Demo3')                   #container: frame2
btn3.grid(row=0,column=0)

root.mainloop()