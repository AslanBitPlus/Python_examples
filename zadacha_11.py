# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input("Введите натуральное число А больше 1: "))

f1 = 0
f2 = 1
num = 2
flag = 0
n = 2

while f2 < a:
    f2, f1 = f2 + f1, f2
    num += 1
    
    if f2 == a:
        print(f"Номер числа Фибоначи - {num}")
        flag = 1
if not flag:
    print(f"{a} НЕ является числом Фибоначи")


