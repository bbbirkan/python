# import numpy as np
# from numpy import random
# p=np.random.choice(range(50),size=(5, 5), replace=False)
# p[2,2]=0
# print(p)
check=[]
import random
mtr_second =[]
i = 0

while i < 5:
    mtr = []
    j = 0
    i+=1
    while j < 5:
            numbers = random.randint(1, 75)
            check.append(numbers)
            if numbers in mtr_second:
                pass
            else:

                mtr.append(numbers)
                j += 1
    mtr_second.append(mtr)
for i in range(5):
    for j in range(5):
        print(str(mtr_second[i][j]).ljust(3), end=' ')
    print()