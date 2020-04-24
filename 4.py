#Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які починаються з певної букви, яка вводиться з клавіатури.

a = []
k = input('Enter your letter')
for i in range (5):
   a.append(input(f'Enter {i+1} surname'))
print(f'New array with letter {k}')
for i in a:
    for j in i:
        if j[0] == k:
            print(i)