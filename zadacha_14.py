# Задача 14: Требуется вывести все целые степени 
# двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число n: "))

k = 0
num = 0
while num < n:
    num = 2 ** k
    k += 1
    if num <= n:
        print(num) 

