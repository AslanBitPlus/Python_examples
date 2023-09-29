# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого 
# множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

size1 = int(input("Введите количество элементов первого множества: "))
size2 = int(input("Введите количество элементов второго множества: "))

num1 = [randint(0, size1) for _ in range(size1)]
num2 = [randint(0, size2) for _ in range(size2)]

print(f"Множество 1: {num1}")
print(f"Множество 2: {num2}")

num3 = []

for value in num1:
    if (value in num2) and (value not in num3):
        num3.append(value)

print(f"Пересечение: {sorted(num3)}")