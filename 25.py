#Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до 100.


import numpy as np
import random
n = 10
doubt = 1
a=np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(10,100)
    if a[i]%5 == 0:
        doubt *= a[i]
print(f'Your arr:{a}')
if doubt == 1:
    print('You have no doubt')
else:
    print(f'Your doubt:{doubt}')