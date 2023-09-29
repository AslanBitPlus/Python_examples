# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

'''
list_1 = [1, 3, 3, 3, 4]
print(list_1)

min = max = list_1[0]
for i in range(1, len(list_1)):
    if list_1[i] < min:
        min = list_1[i]
    if list_1[i] > max:
        max = list_1[i]

for i in range(0, len(list_1)):
    if list_1[i] == max:
        list_1[i] = min
print(list_1)
'''
import random
marks = [random.randint(1, 5) for _ in range(random.randint(5, 10))]
print(marks)

min = max = marks[0]

for i in range(1, len(marks)):
    if marks[i] < min:
        min = marks[i]
    elif marks[i] > max:
        max = marks[i]

for i in range(0, len(marks)):
    if marks[i] == max:
        marks[i] = min
print(marks)
