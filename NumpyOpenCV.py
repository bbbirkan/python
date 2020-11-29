import numpy as np
import matplotlib.pyplot as plt
import keras
from PIL import Image



resim =Image.open('/Users/birkankalyon/Desktop/RUZ.jpg')
print(type(resim))
resim_dizi=np.asarray(resim)
print(type(resim_dizi))
#resimi aldik numpyla dizi formatinda cevirdik
print(resim_dizi.shape)
"""
<class 'PIL.JpegImagePlugin.JpegImageFile'>
<class 'numpy.ndarray'>
(5196, 7776, 3)
"""
# %matplotlib inline
# plt.imshow(resim_dizi) birlikte jupiterde kullanilir
plt.imshow(resim_dizi)

plt.savefig('resim_dizi')
#ekrana cikmadi herneyse

#



