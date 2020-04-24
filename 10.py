#Дані про температуру повітря за декаду листопада зберігаються в масиві. Визначити, скільки разів температура опускалася нижче -10 градусів.

import numpy as np
import random
n = 31
a = np.zeros((n), dtype=int)
count = 0
for i in range(n):
    a[i] = random.randint(-20,5)
    if a[i] < -10:
        count += 1
print(f'Your temperature array:{a}\n Your counts of low temp :{count}')