#Створіть масив А [1..7] за допомогою генератора випадкових чисел і виведіть його на екран. Збільште всі його елементи в 2 рази.

import numpy as np
import random
n = 7
a = np.zeros((n), dtype=int)
for i in range(n):
    a[i] = random.randint(0,15)
print(f'Your arr:{a}')
for i in range (n):
    a[i] = a[i] * 2
print(f'Your new arr:{a}')