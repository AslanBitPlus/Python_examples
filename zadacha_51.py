# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# 1
def same_by_1(characteristic, objects: list):
    char_0 = characteristic(objects[0])
    for num in objects[1:]:
        if char_0 != characteristic(num):
            return False
    return True

# 2
def same_by_2(characteristic, objects: list):
    tmp = list(filter(characteristic, objects))
    if len(tmp) == 0 or len(tmp) == len(objects):
        return True
    else:
        return False

# 3
def same_by_3(characteristic, objects: list):
    tmp = list(map(characteristic, objects))
    print(tmp)
    if sum(tmp) == 0 or sum(tmp) == sum(objects):
        return True
    return False
    # return len(objects) == len(len_obj)


values = [0, 2, 10, 6] 
if same_by_3(lambda x: x % 2, values):
    print('same')
else:
    print('different')