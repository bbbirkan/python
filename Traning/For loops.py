keywords="a","b","c","d"
message=""
for i, keyword in enumerate(keywords): # THIS IS FOR IN ONE LINE, 2 ITEMS SAME TIME
    message += keyword + " "
    if i % 2 == 1:
        message += "\n"
print(message)
"""
output:
a b 
c d 
"""