#Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.

import numpy as np
n = 10
a = np.zeros((n), dtype=int)
doubt = 1
for i in range(n):
    a[i] = int(input(f'Enter your {i+1} num'))
    if a[i] < 0:
        doubt *= a[i]
print(f'Your arr:{a}')
if doubt == 1:
    print('You have no doubt')
else:
    print(f'Your doubt:{doubt}')