'''
Напишите программу, которая определяет наименьшее из четырёх чисел.

Формат входных данных
На вход программе подаётся четыре целых числа.

Формат выходных данных
Программа должна вывести наименьшее из четырёх чисел.

Тестовые данные 🟢
Sample Input 1:

1
2
3
4
Sample Output 1:

1
Sample Input 2:

10
9
11
12
Sample Output 2:

9
Sample Input 3:

100
200
5
300
Sample Output 3:

5
'''


a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)
