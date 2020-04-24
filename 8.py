#Створіть цілочисельний масив А [1..15] за допомогою генератора випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте найбільший елемент масиву і його індекс.

import numpy as np
import random
n = 15
count = 0
a = np.zeros((n), dtype=int)
pos = 0
max = 0
for i in range(n):
    a[i] = random.randint(-15,30)
    if a[i] > max:
        max = a[i]
        pos = i
print(f'Your array: {a}\n Your max el is: {max}\n On position :{pos} ')