#Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 5 до 500.

import numpy as np
import random
n = 10
a = np.zeros((n),dtype=int)
doubt = 1
for i in range(n):
    a[i] = random.randint(5,500)
    if a[i]%3 == 0 and a[i]%9 == 0:
        doubt *= a[i]
print(f'Your arr:{a}')
if doubt == 1:
    print('You have no doubt')
else:
    print(f'Your doubt:{doubt}')