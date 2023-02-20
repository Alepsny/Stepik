'''
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, 
выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов 
в тексте нет.

Тестовые данные 🟢
Sample Input 1:

home sweet home
Sample Output 1:

sweet
Sample Input 2:

home sweet home sweet.
Sample Output 2:

home
'''


s = [word.strip('.,!?:;-') for word in input().lower().split()]

set_t = tuple(s)
result = {}
for i in set_t:
    result.setdefault(i, s.count(i))
max_w = min(result.values())
for i in sorted(result):
    if result[i] == max_w:
        print(i)
        break
