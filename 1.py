#Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в один рядок через кому. Отримайте для масиву середнє арифметичне.

import numpy as np
n = 5
a = np.zeros((n), dtype=int)
k = 0
for i in range(n):
    a[i] = int(input(f'Enter {i+1} element of array: '))
    k += a[i]
print(f'Your array: {a}')
k = k//5
print(f'Your result :{k}')
