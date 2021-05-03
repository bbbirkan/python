import json,re
from pprint import pprint
from difflib import get_close_matches




def suggest_name():
    global data
    json_path = "/Users/birkankalyon/phyton/Tkinter/movie.json"
    with open(json_path) as json_file:
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

        if title != "":
            break
        if title != movie_name.capitalize():
            match = get_close_matches(movie_name, title_prapere)
            match = list(dict.fromkeys(match))  # delete Duplicate
            if len(match) != 0:
                print("Did you want write?", match)
            else:
                pass

            try:
                first = (get_close_matches(movie_name, list(title_prapere), cutoff=0.5))[0]

                recommend = input("Did you mean %s instead %s? (Y/N)" % (first, movie_name))
                if recommend.lower() == 'y':
                    title = first
                    break
                elif recommend.lower() == 'n':
                    print("We couldn't find '%s' in the movie list. Sorry!" % (movie_name))
                    print("")

            except:
                print("We couldn't find the movie. Sorry! Try Again...\n")
        else:
            print("We didn't understand your response")
    return title
suggest_name()

