from tkinter import *
import json,re
from difflib import get_close_matches

root = Tk()
root.geometry("200x360")
frame = Frame(root)
frame.pack()

Birkan=["test","birkan","icine","bak","tara","basar","dene","choose","trust","last","items"]
lb = Label(root, text="")

def Choose_movie_list(self):
    global lb
    global enrty_inside_type

    #print(mylist.curselection())
    lb.destroy()
    print(movie_Search_list.get(movie_Search_list.curselection()))
    lb=Label(root,text=str(movie_Search_list.get(movie_Search_list.curselection())),fg="red")
    lb.pack()


    #print(mylist.curselection())
def Accept_movie():
    print(movie_Search_list.get(movie_Search_list.curselection()))
    print(Entry_search_movie.get())
    lb2 = Label(root, text="you choose !!!"+str(movie_Search_list.get(movie_Search_list.curselection())), fg="red")
    lb2.pack()
    movie_Search_list.config(state=DISABLED)
    buton_accept.config(state=DISABLED)


def Entry_test():
    #print(Entry_search_movie.get())
    pass

def Callback_entry(auto_entry):
    #print (auto_entry.get())
    def suggest_name():
        global movie_Search_list
        list_find_close=[]
        json_path = "/Users/birkankalyon/phyton/Tkinter/movie.json"
        with open(json_path) as json_file:
            data = json.load(json_file)
        while True:
            movie_name =auto_entry.get().capitalize().strip()
            movie_name = movie_name.capitalize()
            title_prapere = []
            title = ""
            for k, v in data.items():
                title_list = v[0]  # title of name
                title_prapere.append(title_list)
                if movie_name == title_list:
                    title = movie_name
                    break
                else:
                    continue
            if title != "":
                print(len(movie_name))
            if len(movie_name)<1:

                print("Search!")
                break
            else:
                match = get_close_matches(movie_name, title_prapere)
                match = list(dict.fromkeys(match))  # delete Duplicate
                if len(match) != 0:
                    enrty_inside_type = (get_close_matches(movie_name, list(title_prapere), cutoff=0.5))[0]
                    print(enrty_inside_type)
                    list_find_close.append(enrty_inside_type)
                    # list_find_close = list(dict.fromkeys(list_find_close))
                    break
                else:
                    break
        movie_Search_list.delete(0, 'end')
        for line in list_find_close:
            movie_Search_list.insert(END, line)
            movie_Search_list.bind('<<ListboxSelect>>', Choose_movie_list)
            #movie_Search_list.config(width=10, height=5)
            enrty_inside_type=[]

        return title
    suggest_name()



frame_TAKE = Frame(root)
frame_TAKE.pack()

frame_LIST = Frame(root)
frame_LIST.pack()

#____________enrty_________
auto_entry = StringVar()
auto_entry.trace("w", lambda name, index, mode, auto_entry=auto_entry: Callback_entry(auto_entry))

Entry_search_movie = Entry(root, textvariable=auto_entry)
Entry_search_movie.pack()
Entry_search_movie.focus()
#__________________________



search_movie_scroll = Scrollbar(frame_LIST)
search_movie_scroll.pack(side=RIGHT,fill = Y)


movie_Search_list = Listbox(frame_LIST, yscrollcommand = search_movie_scroll.set , height= 2)
movie_Search_list.pack(side=LEFT, fill=BOTH)


search_movie_scroll.config(command=movie_Search_list.yview)


buton_accept=Button(root, text='Choose', command=Accept_movie,fg="gray22")
buton_accept.pack()
#
# buton_Search=Button(frame_TAKE, text='Uptade', command=Entry_test,fg="gray22")
# buton_Search.pack()


root.mainloop()