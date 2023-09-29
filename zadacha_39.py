# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                 Вывод:
# 7                     3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1        (каждое число вводится с новой строки)

import random
import time

size1 = random.randint(5, 10)
first_lst = [random.randint(0, 20) for _ in range(size1)]
print(first_lst)
size2 = random.randint(5, 10)
second_lst = [random.randint(0, 20) for _ in range(size2)]
print(second_lst)

for num in first_lst:
    if num not in second_lst:
        print(num)
        time.sleep(2)


