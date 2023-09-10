list_1 = {"V": "S001", "V": "S002", "VI": "S001", "V":"S009", 
          "VI": "S005", "VII": "S005", "V":"S009", "VIII":"S007"}

print(list_1) # {'V': 'S009', 'VI': 'S005', 'VII': 'S005', 'VIII': 'S007'}
print('\n')
      
for key in list_1:
    print(key, end=' ') # V VI VII VIII
print('\n')

print(list_1.keys()) # dict_keys(['V', 'VI', 'VII', 'VIII'])
for key in list_1.keys():
    print(key, end=' ') # V VI VII VIII
print('\n')

print(list_1.values()) # dict_values(['S009', 'S005', 'S005', 'S007'])
for value in list_1.values():
    print(value, end=' ') # S009 S005 S005 S007
print('\n')

print(list_1.items()) # dict_items([('V', 'S009'), ('VI', 'S005'), ('VII', 'S005'), ('VIII', 'S007')])
for item in list_1.items():
    print(item, end=' ') # ('V', 'S009') ('VI', 'S005') ('VII', 'S005') ('VIII', 'S007')
print('\n')

print(list_1.items()) # dict_items([('V', 'S009'), ('VI', 'S005'), ('VII', 'S005'), ('VIII', 'S007')])
for key, value in list_1.items():
    print(key, value, sep = ': ', end=', ') # V: S009, VI: S005, VII: S005, VIII: S007,
print('\n')

list_1['XI'] = list_1.pop('VI') 
print(list_1) # {'V': 'S009', 'VII': 'S005', 'VIII': 'S007', 'XI': 'S005'}
print('\n')

list_1['XII'] = 0
print(list_1) # {'V': 'S009', 'VII': 'S005', 'VIII': 'S007', 'XI': 'S005', 'XII': 0}
list_1['XII'] += 1
print(list_1) # {'V': 'S009', 'VII': 'S005', 'VIII': 'S007', 'XI': 'S005', 'XII': 1}
print('\n')

print(sorted(list_1)) # ['V', 'VII', 'VIII', 'XI', 'XII']
print(sorted('dfjklasditn4')) # ['4', 'a', 'd', 'd', 'f', 'i', 'j', 'k', 'l', 'n', 's', 't']
