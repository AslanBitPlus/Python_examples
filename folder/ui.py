from logger import *

def interface():
    cmd = ''
    while cmd != '5':
        print("Выберите вариант действия:\n"\
            "1: Ввод нового абонента\n"\
            "2: Чтение справочника\n"\
            "3: Поиск абонента\n"\
            "4: Редактирование абонента\n"\
            "5: Выход" )
        cmd = input("Введите вариант: ")
        while cmd not in ('1', '2', '3', '4', '5'):
            print("Вы ввели неправильную команду")
            return
        if cmd == '1':
            input_data()
        elif cmd == '2':
            print_data()
        elif cmd == '3':
            search_data()
        elif cmd == '4':
            edit_data()
    print("Всего доброго!")
