#Розсортуйте заданий лінійний масив по зростанню.

import numpy as np
import random
n = int(input('Enter your amount'))
a = np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(0,30)
print(f'Your array:{a}')
n = len(a)
for i in range(1, n):
    for j in range(n-1, i-1, -1):
        if (a[j-1] > a[j]):
            a[j], a[j-1] = a[j-1], a[j]
print(f'Your new array: {a}')