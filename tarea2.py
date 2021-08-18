from random import random
from numpy.random import rand
from numpy.random import uniform
import matplotlib.pyplot as plt
import numpy as np



data = [0, 5, 15, 20, 24, 24.5, 25, 25.2, 25.4, 26, 26.5, 27, 27.5, 28, 28.2, 28.3, 28.2, 28] 
a = [1000]

data2 = [0, 3.2, 9.5, 12.7, 15.3, 15.6, 15.9, 16.9, 19.7, 28.5, 36.9, 46.5, 58.3, 75.2, 87.1, 100, 112.9, 124.8] 
b = [0.001]

y = np.multiply(data, a)
x = np.multiply(data2, b)

area = [0.2]
deformacion = x / area
esfuerzo = y / area


print(deformacion / area)
print(esfuerzo / area)

plt.plot(deformacion, esfuerzo)
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
