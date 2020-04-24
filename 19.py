#Знайти суму всіх елементів масиву цілих чисел що задовольняють умові: остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 200 до 300.

import numpy as np
import random
n = 20
a = np.zeros((n),dtype=int)
sum = 0
for i in range(n):
    a[i] = random.randint(200,300)
    if a[i]%2 == 3:
        sum += a[i]
print(f'Your arr:{a}')
if sum == 0:
    print('You have no sum')
else:
    print(f'Your sum:{sum}')