# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os, time

def input_fname():
    fnam = str(input("Введите имя: "))
    return fnam

def input_lname():
    lnam = str(input("Введите фамилию: "))
    return lnam

def input_telnum():
    tel_nam = str(input("Введите номер телефона: "))
    return tel_nam

def input_address():
    adr = str(input("Введите адрес: "))
    return adr

def input_data():
    fn = input_fname()
    ln = input_lname()
    tn = input_telnum()
    ad = input_address()

    with open('phone_book.txt', 'a', encoding = 'utf-8') as data:
        data.write(f"{fn} {ln}\n{tn}\n{ad}\n\n")

def print_data():
    os.system('cls')
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        print(data.read())

def search_data():
    search = str(input("Введите значение поиска: "))
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        text = data.read().split('\n\n')[:-1]
        print(text)
        # data.seek(0) # возврат к началу файла
        # list_data = data.readlines()
        # print(list_data)
        for line in text:
            if search in line:
                print(line)


def interface():
    cmd = ''
    while cmd != '4':
        print("Выберите вариант действия:\n"\
            "1: Ввод нового абонента\n"\
            "2: Чтение справочника\n"\
            "3: Поиск абонента\n"\
            "4: Выход" )
        cmd = input("Введите вариант: ")
        while cmd not in ('1', '2', '3', '4'):
            print("Вы ввели неправильную команду")
            return
        if cmd == '1':
            input_data()
        elif cmd == '2':
            print_data()
        elif cmd == '3':
            search_data()







# input_data()
# print_data()
# search_data()

interface()


