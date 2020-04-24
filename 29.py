#Знайти кількість парних елементів одновимірного масиву до першого зустрінутого числа рівного наперед заданому числу а.

import numpy as np
import random
n = int(input('Enter count of elements'))
a = np.zeros((n), dtype=int)
count = 0
h = int(input('Enter your num'))
for i in range(n):
    a[i] = random.randint(0,10)
for i in range(n):
    if a[i]%2 == 0:
        count += 1
        if a[i] == h:
            break

print(f'Your arr:{a}\nYour count of pair nums:{count-1}')