#Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.

import numpy as np
import random
n = 15
a = np.zeros((n),dtype=int)
doubt = 1
for i in range(n):
    a[i] = random.randint(10,50)
    if a[i]%7 == 0:
        k = a[i]
        doubt = doubt*k
        k = 0
print(f'Your arr:{a}')
if doubt == 1:
    print('You have no doubt')
else:
    print(f'Your doubt:{doubt}')