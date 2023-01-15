from functools import reduce
dataset = {1,2,3}

# Creating powerset
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

print(f(dataset))
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]