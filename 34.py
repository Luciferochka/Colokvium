#Дано два лінійних масиву однакової розмірності. Скласти третій масив з добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.

import numpy as np
import random

n = int(input('Enter your amount'))
a = np.zeros((n), dtype=int)
b = np.zeros((n), dtype=int)
c = np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(-10, 10)
    b[i] = random.randint(-10, 10)
    c[i] = a[i] * b[i]
print(f'Your 1 arr:{a}\nYour 2 arr:{b}\nYour 3 arr:{c}')