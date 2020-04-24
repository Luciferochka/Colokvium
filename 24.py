#Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8 одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими числами від 500 до 1000.

import numpy as np
import random
n = 30
sum = 0
a = np.zeros((n),dtype=int)
for i in range(n):
    a[i] = random.randint(150,300)
    if a[i]%5 == 0 and a[i]%8 == 0:
        sum += a[i]
print(f'Your arr:{a}\nYour sum:{sum}')