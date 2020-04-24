#Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями, пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.

import numpy as np
n = 10
a = np.zeros((n),dtype=float)
for i in range(n):
    higth = (9.8 * i**2) / 2
    a[i] = higth
    print(f'Distance after:{i+1} seconds was:{a[i]} meters')