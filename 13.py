#Створіть масив з 15 цілочисельних елементів і визначте серед них мінімальне значення.

import numpy as np
import random
n = 15
a = np.zeros((n),dtype=int)
min = 0
for i in range(n):
    a[i] = random.randint(-15,15)
    if a[i] < min:
        min = a[i]
print(f'Your array:{a}\nYour min value:{min}')