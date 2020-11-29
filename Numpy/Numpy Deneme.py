import numpy as np

array =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,])
print(array.shape)

x = array.reshape(3,5)
print("shape:",x.shape)
print("dimension", x.ndim)

print("data ty")
