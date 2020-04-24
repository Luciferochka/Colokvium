#Змінній t привласнити значення істина, якщо в одновимірному масиві є хоча б одне від’ємне і парне число.

import numpy as np
import random
n = int(input('Enter your count of els:'))
a = np.zeros((n), dtype=int)
count = 0
Flag = False
for i in range(n):
    a[i] = random.randint(-15, 20)
    if a[i] < 0 and a[i]%2 == 0:
        Flag = True
print(f'Your arr:{a}\nAnd your t is {t}')