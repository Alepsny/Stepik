'''
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая находит длину самого длинного слова.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input:

проспал почти всю ночь
Sample Output:

7
'''


print(max([len(i) for i in input().split()]))

