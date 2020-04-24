#Знайти суму елементів масиву дійсних чисел, що мають непарні номери. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100 до 200.

import numpy as np
import random
n = 20
a = np.zeros((n),dtype=int)
sum = 0
for i in range(n):
    a[i] = random.randint(100,200)
    if i%2 != 0:
        sum += a[i]
print(f'Your arr:{a}\nYour sum:{sum}')