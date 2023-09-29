# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint
# Первый метод ======================
# size = randint(5, 10)
num = [randint(-3, 10) for _ in range(randint(5, 10))]
print(num)

result = [num[i] for i in range(1, len(num)) if num[i] > num[i - 1]]
print(result, len(result))
# ====================================

# Второй метод =======================
count = 0
for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        count +=1
print(count)
# ====================================
