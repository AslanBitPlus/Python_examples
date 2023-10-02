import os
from data_create import *

def input_data():
    fn = input_fname()
    ln = input_lname()
    tn = input_telnum()
    ad = input_address()

    with open('phone_book.txt', 'a', encoding = 'utf-8') as data:
        data.write(f"{fn}\n{ln}\n{tn}\n{ad}\n\n")

def print_data():
    os.system('cls')
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        print(data.read())

def search_data():
    print("Выберите вариант действия:\n"\
            "1: Поиск по имени\n"\
            "2: Поиск по фамилии\n"\
            "3: Поиск по номеру телефона\n"\
            "4: Поиск по Адресу" )
    cmd = input("Введите вариант: ")
    while cmd not in ('1', '2', '3', '4'):
        print("Вы ввели неправильную команду")
    search = str(input("Введите значение поиска: ")).title()
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        text = data.read().strip().split('\n\n')
        for line in text:
            new_line = line.replace(' ', '\n').strip().split('\n')
            if search in new_line[int(cmd) - 1]:
                print(line)
                print()
            # if search in line:
            #     print(line)

def edit_data():
    search = ''
    new_search = ''
    print("Выберите вариант действия:\n"\
            "1: Поиск по имени\n"\
            "2: Поиск по фамилии\n"\
            "3: Поиск по номеру телефона\n"\
            "4: Поиск по Адресу" )
    cmd = input("Введите вариант: ")
    while cmd not in ('1', '2', '3', '4'):
        print("Вы ввели неправильную команду")
    search = str(input("Введите значение поиска: ")).title()
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        text = data.read().strip().split('\n\n')
        # text = data.read()
        print(text)


        for line in text:
            # new_line = line.replace(' ', '\n').strip().split('\n')
            if search + '\n' in line:
                print(line)
                print()
                ind = line.find(search)
                # print(ind)
                new_search = str(input(f"На что заменить {search} :")).title()
                new_line = line.replace(search + '\n', new_search + '\n')
                print(new_line)

    if new_search != '':
        with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
            text = data.read()
            print('============================================')
            print(text)
            print(search, new_search)

            print('============================================')
            text = text.replace(search + '\n', new_search + '\n')
            print(text)
            print('============================================')
        with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
            data.write(text)
            print(f"Значение {search} заменен на {new_search} ")
            
'''
# Read in the file
with open('file.txt', 'r') as file :
  filedata = file.read()
# Replace the target string
filedata = filedata.replace('abcd', 'ram')
# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)
'''