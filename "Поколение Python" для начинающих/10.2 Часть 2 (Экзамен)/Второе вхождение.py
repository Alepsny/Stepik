'''
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, 
выведите число -1, а если не встречается ни разу, выведите число -2.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

affective
Sample Output 1:

2
Sample Input 2:

python
Sample Output 2:

-2
Sample Input 3:

father
Sample Output 3:

-1
'''


s = input()
fs = s.find("f")
s2 = s.replace("f", " ", 1)
ss = s2.find("f")
if fs != -1:
    print(ss)
else:
    print(-2)
