# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = str(input("Введите текст для подстчета символов: "))
text = 'a a a b c a a d c d d'
# print(text.split())
# print(text.split(' '))

text_l = text.split()
print(text_l)

uniq_dict = {}

for letter in text_l:
    if letter not in uniq_dict:
        uniq_dict[letter] = 0
        print(letter, end=' ')
    else:
        uniq_dict[letter] += 1
        print(letter + '_' + str(uniq_dict[letter]), end= ' ')

