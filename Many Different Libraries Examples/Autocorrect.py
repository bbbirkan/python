"pip install autocorrect"
"textdistance"

from autocorrect import Speller
check = Speller("en")
a=check("builtiins")
print(a)
print(dir(Speller))

# from autocorrect.word_count import count_words
# count_words('ruwiki-latest-pages-articles.xml', 'ru')