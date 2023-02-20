'''
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения по одному и тому же ключу, 
в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо присвоить переменной result.
'''


dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
result.update(dict1)
result.update(dict2)
for i in result:
    if i in dict1 and i in dict2:
        result[i] = dict1[i] + dict2[i]
    elif i in dict1:
        result[i] = dict1[i]
    else:
        result[i] = dict2[i]
