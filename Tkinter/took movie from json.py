import json,re
from pprint import pprint
from difflib import get_close_matches

def suggest_name():
    global data
    with open('movie.json') as json_file:
        data = json.load(json_file)
    while True:
        movie_name = input("Find movie?:").capitalize().strip()
        movie_name = movie_name.capitalize()

        # print (movie_name)
        title_prapere = []
        title = ""

        for k, v in data.items():
            title_list = v[0]  # title of name
            title_prapere.append(title_list)
            if movie_name == title_list:
                title = movie_name
            else:
                continue

        if title !="":
            break
        if title != movie_name.capitalize():
            match = get_close_matches(movie_name, title_prapere)
            match = list(dict.fromkeys(match))  # delete Duplicate
            print("Did you want write?", match)
            first = (get_close_matches(movie_name, list(title_prapere), cutoff=0.5))[0]
            recommend = input("Did you mean %s instead %s? (Y/N)" % (first, movie_name))
            if recommend.lower() == 'y':
                title = first
                break
            elif recommend.lower() == 'n':
                print("We couldn't find '%s' in the movie list. Sorry!" % (movie_name))
            else:
                print("We didn't understand your response")


    return title

def movie_title(title):
    global imbd_number
    global movie_last_name
    movie_movie = title
    l = list()
    show = {}
    for k, v in data.items():
        # print(v[0]) title of name
        if movie_movie in v[0]:
            l.append(k)
            show[v[0] + " - " + v[1]] = k
            year = " - " + v[1]

    imbd_number = ''
    movie_last_name = ''
    temp = {}
    name={}
    if len(show) == 0:
        pass
    elif len(show) == 1:
        imbd_number = show.get(movie_movie + year)
        movie_last_name = movie_movie + year
        temp[movie_movie] = show.get(movie_movie)

    else:
        for number, (index, imbd) in enumerate(zip(show.keys(), l), start=1):
            print(number, "-", index)
            temp[int(number)] = imbd
            name[int(number)]= index

        while True:
            z = (input("Write number here:"))

            if z.isdigit() == False:
                print("Thats not a number please write number.")
            else:
                z = int(z)

                # temp[temp.get(z)] = imbd
                imbd_number = temp.get(z)
                print()
                movie_last_name = name.get(z)
                # print(temp.get(z))
                # print(index)
                break

    # print(temp)
    print(imbd_number)
    print(movie_last_name)
    return movie_last_name , imbd_number
movie_title(suggest_name())


#pprint([list(data.values())])
#print(list(data.keys())[list(data.values()).index('Kate & Leopold')])
            #print(data.get(movie_name))
