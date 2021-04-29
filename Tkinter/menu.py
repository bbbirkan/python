from tkinter import *

root = Tk()
root.title('Test Tk menu on mac Catalina Python 3.7.4 tkinter 8.6')

mymenubar = Frame(root, relief='raised', bd=2)
mymenubar.pack(fill=X)

mymenubutton = Menubutton(mymenubar, text='File', )
mymenubutton.pack(side=LEFT)

mymenu = Menu(mymenubutton, tearoff=0)
mymenubutton['menu'] = mymenu
mymenu.add('command', label='Open') # Add Sub Menu 1

mb2 = Menubutton(mymenubar, text='Edit', )
mb2.pack(side=LEFT)
menudd = Menu(mb2, tearoff=0)
mb2['menu'] = menudd
menudd.add('command', label='Cut') # Add Sub Menu 2

myframe1 = Frame(root, bd=2, relief=SUNKEN)
myframe1.pack(side=LEFT)

Label(myframe1, text='As you can see this works in tkinter with:\nPython v3.7.4:e09359112e, Jul 8 2019, 14:54:52,\ntkinter 8.6 and\n mac os 10.15').pack()
Label(myframe1, text='There is a way - or was when I last tried - to do real mac menus in tkinter.\n'
'Be that as it may this would be perfectly OK and consistent across platforms.').pack()
root.mainloop()