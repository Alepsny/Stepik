'''
На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.

Формат выходных данных
Программа должна вывести столбчатую диаграмму.

Тестовые данные 🟢
Sample Input 1:

1 2 3 4 5
Sample Output 1:

+
++
+++
++++
+++++
Sample Input 2:

5 3 1 7 10 2
Sample Output 2:

+++++
+++
+
+++++++
++++++++++
++
'''


s = input().split()
for i in range(len(s)):
    print("+" * int(s[i]))
