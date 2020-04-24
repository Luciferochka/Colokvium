#Знайти добуток всіх елементів масиву дійсних чисел, менших заданого числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 50 до 100.

import numpy as np
import random
h = int(input('Enter your noun:'))
n = 10
a = np.zeros((n), dtype=int)
doubt = 1
for i in range(n):
    a[i] = random.randint(50,100)
    if a[i] > h:
        doubt *= a[i]
print(f'Your arr:{a}')
if doubt == 1:
    print('You have no doubt')
else:
    print(f'Your doubt:{doubt}')