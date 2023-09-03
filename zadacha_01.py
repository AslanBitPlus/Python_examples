# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2


import math

speed = int(input("Введите скорость: "))
dist = int(input("Введите дистанцию: "))

days = math.ceil(dist / speed) # С использованием округления вверх
days2 = (dist + speed - 1) // speed # второй метод
days3 = (dist // speed) + bool(dist%speed) # третий метод
print(days)
print(days2)
print(days3)
