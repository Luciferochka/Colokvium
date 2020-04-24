#Знайти суму всіх елементів масиву дійсних чисел, більших за задане число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 50 до 100.

import numpy as np
import random
h = int(input('Enter your num: '))
n = 20
sum = 0
a = np.zeros((n),dtype=int)
sum = 0
for i in range(n):
    a[i] = random.randint(50,100)
    if a[i] > h:
        sum += a[i]
print(f'Your arr:{a}\nYour sum:{sum}')