#Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які розташовані за першим по порядку мінімальним елементом.

import numpy as np
import random
n = int(input('Enter your count of els:'))
a = np.zeros((n), dtype=int)
mid = 0
min = 0
minn = 0
for i in range(n):
    a[i] = random.randint(-100,100)
    if a[i] < min:
        min = a[i]
        minn = i
for i in range(n):
    if i > minn:
        mid += a[i]
mid /= n - minn
print(f'Your arr:{a}\nYour min el:{min}\nYour middle value:{mid}')