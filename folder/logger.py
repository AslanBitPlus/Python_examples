import os
from data_create import *

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
