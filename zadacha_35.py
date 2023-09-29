# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


'''
def simp(n):
    count = 0
    d = 2
    while d <= n // 2:
        if n % d == 0:
            count += 1
        d += 1
    if count == 0:
        return 'Yes'
    return 'No'

num = int(input("Введите число :"))
print(simp(num))
'''

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return 'No'
    
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return 'No'
    return 'Yes'

num = int(input("Введите натуральное число :"))
print(is_prime(num))
