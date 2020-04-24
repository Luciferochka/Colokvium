#Дані про температуру повітря за декаду грудня зберігаються в масиві. Визначити, скільки раз температура була вище середньої за цю декаду.

import numpy as np
import random
n = 31
a = np.zeros((n),dtype=int)
middle = 0
count = 0
for i in range(n):
    a[i] = random.randint(-20,5)
    middle += a[i]
print(f'Your decade results:{a}')
middle = middle//31
for i in range(n):
    if a[i] > middle:
        count += 1
print(f'Your middle value: {middle}\n Your count of days with temp above of middle:{count}')