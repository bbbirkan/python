
print("""
#    (column,row)
# 1 Table (0, 0)
# 2 Table (0, 1)
# 3 Table (1, 0)
# 4 Table (1, 1)
# 5 Table (2, 0)
# 6 Table (2, 1)
# 7 Table (3, 0)
# 8 Table (3, 1)
# 9 Table (4, 0)
""")

table_number=2
print('Table:{0} \n------'.format(table_number))

#column
if table_number%2==0:
    column=round((table_number/2)-1)
else:
    column = round(((table_number - 1)/2))
print("Column:",column)

#row
if (table_number %2) <= 0:
    row = 1
else:
    row=0
print("Row:",row)




