#Знайти суму всіх елементів масиву цілих чисел, які менше середнього арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 150 до 300.

import numpy as np
import random
n = 20
sum = 0
a = np.zeros((n),dtype=int)
middle = 0
for i in range(n):
    a[i] = random.randint(150,300)
    middle += a[i]
middle /= 20
for i in range(n):
    if a[i] < middle:
        sum += a[i]
print(f'Your arr:{a}\nYour middle value:{middle}\nYour sum:{sum}')