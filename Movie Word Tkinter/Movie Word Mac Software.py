from tkinter import *
from tkinter.ttk import Progressbar
import threading
#----------------------
import os.path,re,time,pickle,inflect,sys,contextlib,pathlib,sys

import requests
import json
from difflib import get_close_matches
import ast
import string
import struct
from xmlrpc.client import ServerProxy
from pprint import pprint
import gzip
# from mpyg321.mpyg321 import MPyg321Player
# player = MPyg321Player()
# from tqdm import tqdm
# import sounddevice as sd
# from scipy.io.wavfile import write
# from pydub import AudioSegment
# from pydub.playback import play
# from gtts import gTTS #speech
# from pynput import keyboard
# import pathlib
# import pexpect
# from gtts import gTTS
#--- delete after change
# from textblob import Word
# from tkinter import filedialog as bir
#-------------------------

#+---------------Location----------------------+
def Location_Main():
    global main_l
    print("Your main location:", os.getcwd())
    main_l= os.getcwd()
    return main_l
Location_Main()
def Location_folder(folder_location):
    try:
        os.getcwd()  # main folder location
        os.chdir(folder_location)  # change main data
        print("Your Current location:", os.getcwd())
    except IOError:
        n=-1
        for i in os.listdir():
            n=n+1
            print(n," - "+i)
        print("Your Current location:", os.getcwd())
        print(folder_location + ' is Not in this location please write in correct location')
        while True:
            z = (input("Write number here:"))
            if z.isdigit() == False:
                print("Thats not a number please write number.")
            else:
                z = int(z)
                break
        folder_location = ""+(os.listdir()[z])+""
        Location_folder(folder_location)
        print("Correct location now",os.getcwd())
        # print(os.mkdir("new"))# create folder maybe update for future
#|-------------------------------------|
Location_folder("json_data")

root = Tk()
root.geometry("700x360")
imbd=[]
label_show_choose = Label()
error_label= Label()
label_show_choose = Label()
progress = Progressbar()
label_loading = Label()

def Accept_movie():
    global label_show_choose
    global imbd
    global imbd_number
    global error_label
    global progress
    global label_loading

    label_show_choose.destroy()
    error_label.destroy()
    progress.destroy()
    label_loading.destroy()

    try:
        index_second_list = movie_choose_list.index(movie_choose_list.curselection())+1
        temp[temp.get(index_second_list)] = imbd
        imbd_number_more = temp.get(index_second_list)
        you_choose = str(movie_choose_list.get(movie_choose_list.curselection()))
    except:
        error_label= Label(root, text="Choose your movie from left side list! ", fg="gray22")
        error_label.pack()


    try:
        label_show_choose = Label(frame_progress, text=you_choose, fg="gray22")
        imbd_number=imbd_number_more
    except(TypeError):
        label_show_choose = Label(frame_progress, text=you_choose, fg="gray22")
    #print(imbd_number)
    label_show_choose.pack()

    movie_Search_list.config(state=DISABLED)
    movie_choose_list.config(state=DISABLED)
    buton_accept.config(state=DISABLED)
    # --------Progress------------
    progress = Progressbar(frame_progress, orient=HORIZONTAL, length=200, mode='determinate')
    progress.pack()
    label_loading = Label(frame_progress, text="Loading..!", fg="gray22")
    label_loading.pack()

    def Progress_fonction():
        progress['value'] = 5
        # DO SOMETHING
        # -------------
        # def Opensubtitle_Download(imdb_id):
        #     global saved_file_name
        #     alldata={}
        #     url = "https://www.opensubtitles.com/api/v1/login"
        #     headers = {'api-key': 'JCa5AqZVFIqhxKTZlg4KGE4LftaUA5Mu', 'content-type': 'application/json'}
        #     user = {'username': 'birkank', 'password': "yEue!DFbbbb%$3"}
        #
        #     try:
        #         login_response = requests.post(url, data=json.dumps(user), headers=headers)
        #         login_response.raise_for_status()
        #         login_json_response = login_response.json()
        #         login_token = login_json_response['token']
        #     except:
        #         print("Something wrong check again...")
        #
        #     headers = {
        #         'Api-Key': 'JCa5AqZVFIqhxKTZlg4KGE4LftaUA5Mu',
        #     }
        #     params = (
        #         ('imdb_id', imdb_id),
        #     )
        #     query_response = requests.get('https://www.opensubtitles.com/api/v1/subtitles?', params=params,
        #                                   headers=headers)
        #     query_json_response = query_response.json()
        #     print("Report:", query_response)
        #     # pprint(query_json_response)# All data here...
        #     try:
        #         query_file_name = query_json_response['data'][0]['attributes']['files'][0]['file_name']
        #         query_file_no = query_json_response['data'][0]['attributes']['files'][0]['file_id']
        #         movie_img = query_json_response['data'][0]['attributes']['related_links']['img_url']
        #     except:
        #         query_file_name = "N/A"
        #         query_file_no = "N/A"
        #         movie_img = "N/A"
        #
        #     while True:
        #         if query_file_no != "N/A":
        #             print("Movie Image url:", movie_img)
        #             print("File Number:", query_file_no)
        #             print("Subtile File Name:", query_file_name)
        #
        #             Location_folder(main_l)  # Main Location Folder
        #             Location_folder("movie")  # Enter Movie folder inside
        #
        #             from PIL import Image
        #             ImgRequest = requests.get(movie_img)
        #             img = open("temp.jpg", "wb")
        #             img.write(ImgRequest.content)
        #             img.close()
        #             img = Image.open("temp.jpg")
        #             img.show()
        #
        #             download_url = "https://www.opensubtitles.com/api/v1/download"
        #             download_headers = {'api-key': 'JCa5AqZVFIqhxKTZlg4KGE4LftaUA5Mu',
        #                                 'authorization': login_token,
        #                                 'content-type': 'application/json'}
        #
        #             download_file_id = {'file_id': query_file_no}
        #             download_response = requests.post(download_url, data=json.dumps(download_file_id),
        #                                               headers=download_headers)
        #             download_json_response = download_response.json()
        #             #pprint(query_json_response)# All data here...**********************************************8
        #             print('Beginning file download with requests')
        #             print("Report:", download_response)
        #
        #             link = download_json_response['link']
        #             saved_file_name = "subtitle.srt"
        #             r = requests.get(link)
        #             with open(saved_file_name, 'wb') as f:
        #                 f.write(r.content)
        #             left = download_json_response['remaining']
        #             print("Subtitle File Downloaded")
        #             print("How many request left:", left)
        #
        #             alldata[imbd_id] = {
        #                 "title": movie_last_name,
        #                 "image": str(movie_img),
        #                 "subtitle": str(r.content)}
        #
        #             Location_folder(main_l)  # Main Location Folder
        #             Location_folder("json_data")  # Enter Movie folder inside
        #
        #             with open("Subtitle.json", "r") as jsonFile:
        #                 mergee = json.load(jsonFile)
        #             merge_dic = {**alldata, **mergee}  # merge 2 dictionary
        #
        #
        #             with open("Subtitle.json", 'w', encoding='utf8') as f3:
        #                 json.dump(merge_dic, f3, ensure_ascii=False, indent=1)
        #             Location_folder(main_l)  # Main Location Folder
        #             Location_folder("movie")  # Enter Movie folder inside
        #             break
        #         else:
        #             print("Done! with the error")
        #             saved_file_name="0"
        #             break



        # -------------
        progress['value'] = 100
        label_show_choose.config(text="Done")
        time.sleep(2)

        frame_progress.destroy()
        frame_choose_buton.destroy()
        frame_Search.destroy()
        frame_secondlist.destroy()

        Entry_search_movie.destroy()
        movie_Search_list.destroy()
        search_movie_label.destroy()
        movie_choose_list.destroy()
        search_movie_scroll.destroy()
        label_show_choose.destroy()
        progress.destroy()


        frame_LIST.destroy()
        frame_Search.destroy()
        frame_choose_buton.destroy()
        frame_secondlist.destroy()
        frame_progress.destroy()
        frame_info=Frame(height = 1000,width = 940)
        frame_info.pack()


    threading.Thread(target=Progress_fonction).start()
    # --------------------------------
    return imbd_number

def Callback_entry(auto_entry): #Entery type focus automation
    global data
    global suggest_name
    global movie_Search_list
    global imbd
    global label_show_choose
    label_show_choose.destroy()
    error_label.destroy()
    buton_accept.config(state=DISABLED)
    empty_enter = Entry_search_movie.get()
    movie_choose_list.config(state=NORMAL)
    movie_choose_list.delete(0, 'end')
    if len(empty_enter) < 1:
        movie_choose_list.delete(0, 'end')
        movie_choose_list.insert(0, " Your movie will be here!")
        movie_choose_list.config(state=DISABLED)
    else:
        pass
    def suggest_name():
        global movie_Search_list
        global data
        global match
        global movie_name
        list_find_close=[]
        Location_folder("json_data")
        json_path = "movie.json"
        with open(json_path) as json_file:
            data = json.load(json_file)
        while True:
            title_prapere = []
            title = ""
            movie_Search_list.bind('<<ListboxSelect>>', Choose_movie_list)

            movie_name =auto_entry.get().capitalize().strip()
            movie_name = movie_name.capitalize()

            for k, v in data.items():
                title_list = v[0]  # title of name
                title_prapere.append(title_list)
                if movie_name == title_list:
                    title = movie_name
                    break
                else:
                    continue
            movie_Search_list.config(state=NORMAL)
            if len(movie_name)<1:
                print("delete0")
                #movie_Search_list.forget()
                movie_Search_list.delete(0, 'end')
                movie_Search_list.insert(0, " Suggest Name Section!")
                movie_Search_list.config(state=DISABLED)
                print("Search!")
                break
            else:
                match = get_close_matches(movie_name, title_prapere)
                match = list(dict.fromkeys(match))  # delete Duplicatemovie_choose_list.focus()
            movie_Search_list.delete(0, 'end')
            for line in match:
                movie_Search_list.insert(END, line)
            break
        return title
    suggest_name()

def Choose_movie_list(self):

    global enrty_inside_type
    global movie_Search_list
    global temp
    global imbd_number
    global imbd

    buton_accept.config(state=DISABLED)
    error_label.destroy()
    try:
        selected_movie=str(movie_Search_list.get(movie_Search_list.curselection()))
    except:
        selected_movie=None

    def movie_title(title):
        global imbd_number
        global movie_last_name
        global movie_Search_list
        global temp
        global imbd
        buton_accept.config(state=DISABLED)
        movie_movie = title
     #---------------------
        l = list()
        show = {} #how many movie inside
        imbd_number = ''
        movie_last_name = ''
        temp = {}
        name = {}
        movie_choose_list.delete(0, 'end')
        for k, v in data.items():
            check_list = (v[0])  # movie names on list
            split_search = re.split(r'\s|s|:|!|:|\?|\.', check_list)  # split with this Character
            for split_words in split_search:
                if title.capitalize() == split_words.capitalize():
                    l.append(k)
                    show[v[0] + " - " + v[1]] = k
                    year = " - " + v[1]
                    print("girdi1")
        if len(show) == 0:
            pass


        elif len(show) == 1:
            print("girdi2")
            imbd_number = show.get(movie_movie + year)
            movie_last_name = movie_movie + year
            temp[movie_movie] = show.get(movie_movie)



        else:
            print("girdi3")
            for number, (index, imbd) in enumerate(zip(show.keys(), l), start=1):
                moviename_and_year=str(number)+ "- "+ str(index)
                movie_choose_list.insert(END, moviename_and_year)
                print(number, "-", index)
                temp[int(number)] = imbd
                name[int(number)] = index


        movie_choose_list.insert(END, (movie_last_name))
        print("imbd ID:",imbd_number )
        imbd = imbd_number
        print(movie_last_name)

        try:
            movie_choose_list.selection_set(first=0)
            list_inside = movie_choose_list.get(movie_choose_list.curselection())
            if len(list_inside) == 0:
                movie_choose_list.selection_set()
                buton_accept.config(state=DISABLED)
            else:
                buton_accept.config(state=NORMAL)
        except:
            pass
        return movie_last_name, imbd_number

    if selected_movie!=None:
        movie_title(selected_movie)
    else:
        pass





#______Frames____________
frame_LIST = Frame(root,highlightbackground= "#CCCCFF")
frame_LIST.pack(pady=20)

frame_Search= Frame(frame_LIST)
frame_Search.pack(side = LEFT)

frame_choose_buton = Frame(root)
frame_choose_buton.pack()

frame_secondlist=Frame(frame_choose_buton)
frame_secondlist.pack()

frame_progress = Frame(root)
frame_progress.pack()
#____________enrty_________
search_movie_label=Label(frame_Search, text='Search Movie', fg="gray22")
search_movie_label.pack()

auto_entry = StringVar()
auto_entry.trace("w", lambda name, index, mode, auto_entry=auto_entry: Callback_entry(auto_entry))
Entry_search_movie = Entry(frame_Search, textvariable=auto_entry,highlightbackground= "#CCCCFF")#highlightthickness=2,highlightcolor= "red",highlightbackground = "#CCCCFF"
Entry_search_movie.pack()
Entry_search_movie.focus()
# selectbackground="red",

#_________First List_________________
movie_Search_list = Listbox(frame_LIST,cursor="sb_right_arrow", height= 5,selectbackground="#CCCCFF",exportselection=False)#exportselection=False thats importatnt for two selection
movie_Search_list.pack( side=LEFT,fill=BOTH,padx=15)
movie_Search_list.config(highlightbackground = "#CCCCFF", highlightcolor= "#CCCCFF",highlightthickness=3,bd=0)#
def a():
    print("g")
#_________Secon List___________________
search_movie_scroll = Scrollbar(frame_LIST)
search_movie_scroll.pack(side=RIGHT,fill = Y)
movie_choose_list = Listbox(frame_LIST,selectbackground="#CCCCFF",width=45,height= 4,yscrollcommand = search_movie_scroll.set,exportselection=False)
movie_choose_list.pack(fill=BOTH,side=LEFT)
movie_choose_list.config(highlightbackground = "#CCCCFF", highlightcolor= "#CCCCFF",highlightthickness=3,bd=0)
search_movie_scroll.config(command=movie_choose_list.yview)




buton_accept=Button(frame_choose_buton, text='Choose', command=Accept_movie,fg="gray22")
buton_accept.pack()
buton_accept.config(state=DISABLED)
# buton_Search=Button(frame_TAKE, text='Uptade', command=Entry_test,fg="gray22")
# buton_Search.pack()

root.mainloop()