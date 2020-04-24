#Знайти кількість парних елементів одновимірного масиву.

import numpy as np
import random
n = int(input('Enter count of elements'))
a = np.zeros((n), dtype=int)
count = 0
for i in range(n):
    a[i] = random.randint(-100,100)
    if a[i]%2 == 0:
        count += 1
print(f'Your arr:{a}\nYour count of pair nums:{count}')