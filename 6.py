#Створіть масив А [1..8] за допомогою генератора випадкових чисел з елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних елементів масиву.

import numpy as np
import random
n = 8
count = 0
a = np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(-10,10)
    if a[i] < 0:
        count += 1
print(f'Your arr:{a}')
print(f'Your count: {count}')