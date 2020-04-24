#Створіть масив А [1..12] за допомогою генератора випадкових чисел з елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи масиву числом 0.

import numpy as np
import random
n = 12
count = 0
a = np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(-20,10)
print(f'Your arr:{a}')
for i in range (n):
    if a[i] < 0:
        a[i] = 0
print(f'Your new arr: {a}')