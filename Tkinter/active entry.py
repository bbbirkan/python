import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame)
entry.configure(state=tk.DISABLED)
entry.pack()

def activation_handler(event):
    print('handled event: {}'.format(event))

entry.bind('<Activate>', activation_handler)

button = tk.Button(frame, text='Toggle enable')
button.pack()

def do():
    if entry.cget('state') == tk.NORMAL:
        entry.configure(state=tk.DISABLED)
    else:
        entry.configure(state=tk.NORMAL)
        entry.event_generate("<<Activate>>")

button.configure(command=do)

root.mainloop()

entry.bind('<<Activate>>', activation_handler)
...
