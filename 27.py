#Лінійний масив містить відомості про кількість опадів, що випали за кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.

import numpy as np
n = 12
a = np.zeros((n),dtype=int)
sum = 0
count = 0
min = 1000
mid = 0
h = 0
for i in range(n):
    a[i] = int(input(f'Enter your value for {i+1} month'))
    sum += a[i]
    mid += a[i]
    if a[i] <= 30:
        count += 1
    if a[i] < min:
        min = a[i]
        h = i
mid /= 12
print(f'Your arr:{a}\nYour sum:{sum}\nYour middle value:{mid}\nYour count of bad months:{count}')
if h == 0:
    print('The worst month is January')
elif h == 1:
    print('The worst month is February')
elif h ==2 :
    print('The worst month is March')
elif h == 3:
    print('The worst month is April')
elif h == 4:
    print('The worst month is May')
elif h == 5:
    print('The worst month is June')
elif h == 6:
    print('The worst month is July')
elif h == 7:
    print('The worst month is August')
elif h == 8:
    print('The worst month is September')
elif h == 9:
    print('The worst month is October')
elif h == 10:
    print('The worst month is November')
elif h == 11:
    print('The worst month is December')