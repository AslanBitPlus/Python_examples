# Вывод данных
# a = 5
# b = 5.8
# c = 'Hello'
# print(a, b, c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}" .format(a, b, c))


# Ввод данных СТРОКИ
# print("Введите первое число: ")
# a = input()
# print(f"a = {a}")
# b = input("Введите второе число: ")
# print(f"b = {b}")
# print(a, " + ", b, " = ", a + b)


# Ввод данных INT
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(f"a = {a}")
# print(f"b = {b}")
# print(a, " + ", b, " = ", a + b)


# Округление чисел
# a = 2.56723
# b = 3.69104
# print(round(a * b, 2))


# Цикл (if)
# a = 5
# b = 7
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else :
#     print("a = b")


# Цикл (while)
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 15
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Хватит уже!")


# Цикл (for range())=====================
# for i in 1, 6, 9, 5, 7:
#     print(i)

# a = range(5)
# for i in a:
#     print(i)

# a = range(100, 0, -20 )
# for i in a:
#     print(i)

# a = "qwerty"
# print(a[1]) # Первый элемент w, нумерация идет с нуля
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

text = "Трансформаторная подстанция"
print(len(text))
print("подстанция" in text)
print(text.lower())
print(text.upper())
print(text.replace("Трансформаторная", "Генераторная"))

print(text[len(text) - 1]) # Печать последней буквы (элемента)
print(text[-1]) # Печать последней буквы (элемента)

print(text[:]) # Вывод всех элементов
print(text[:5]) # Вывод с первого по 5-й элемент

print(text[len(text) - 2:]) # Вывод последних двухэлементов
print(text[0: 13]) # Вывод со 2-го по 15-й элемент
print(text[0: -18])
print(text[0: len(text): 2])
print(text[:: 2])


# Работа со строками

