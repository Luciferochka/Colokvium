#З 8 до 20 години температура повітря вимірювалася щогодини. Відомо, що протягом цього часу температура знижувалася. Визначте, о котрій годині було вперше зафіксовано від'ємну температуру.

import random
a = [random.randint(-0, 16) for x in range(8, 21)]
print('°C, '.join(map(str, a)), end='°C\n')
min = max(a)
k = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        k = i
print(f'Lowest temperature {min}°C was firstly spotted at {k + 8} hours')