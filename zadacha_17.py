# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Первый метод ======================
# size = int(input("Введите размер списка: "))
# num = []

# for i in range(size):
#     n = int(input(f"Введите {i}-й элемент списка: "))
#     num.append(n)
# print(num)


# print(len(set(num)))
# ====================================
# Второй метод =======================
import random

size = random.randint(5, 10)
num = [random.randint(0, 10) for _ in range(size)]
print(f"Размер списка: {size}")
print(f"Список: {num}")

temp = []
count = 0
for i in num:
    if not i in temp:
        temp.append(i)
        count +=1
print(f"Количество уникальных элементов в списке {count}")
# ==================================== 
