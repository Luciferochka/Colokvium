#Дані про температуру води на Чорноморському узбережжі за декаду вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для купання.

import numpy as np
import random
n = 30
a = np.zeros((n),dtype=int)
count = 0
for i in range(n):
    a[i] = random.randint(5,25)
    if a[i] > 15:
        count += 1
print(f'Your temperature array:{a}\n Counts of good days :{count}')