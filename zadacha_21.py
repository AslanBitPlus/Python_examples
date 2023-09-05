# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001", " V ":" S009"},
# {"VI": "S005"}, {"VII": " S005"}, {"V":" S009"}, {"VIII":" S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001", "V":"S009"},
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

print("Original list: ", lst)
# Первый метод ======================
# res_set = set()
# for cur_dict in lst:
#     for key in cur_dict:
#         res_set.add(cur_dict[key])
# print(res_set)
# ====================================

# Второй метод =======================
res_set = set()
for cur_dict in lst:
    print(cur_dict.keys())
    print(cur_dict.values())
    print(cur_dict.items())
    for key in cur_dict:
        res_set.add(cur_dict[key])
print(*res_set, sep='\n')