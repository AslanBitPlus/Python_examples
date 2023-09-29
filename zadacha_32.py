# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

size = random.randint(5, 10)
lst_1 = [random.randint(0, 20) for _ in range(size)]
print(lst_1)

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

for i in range(0, size):
    if lst_1[i] > min and lst_1[i] < max:
        print(i, sep=' ')
