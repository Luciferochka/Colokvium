#Знайти суму додатніх елементів лінійного масиву цілих чисел.Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.

import numpy as np
import random
n = 10
a = np.zeros((n),dtype=int)
sum = 0
for i in range(n):
    a[i] = int(input(f'Enter your {i+1} el:'))
    if a[i] > 0:
        sum += a[i]
print(f'Your arr:{a}\nYour sum:{sum}')