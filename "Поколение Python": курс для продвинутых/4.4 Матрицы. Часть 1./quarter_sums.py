'''
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.



Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.

Тестовые данные 🟢
Sample Input 1:

4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4
Sample Output 1:

Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
Sample Input 2:

5
1 4 3 4 7
5 6 7 8 4
3 8 5 6 1
1 2 9 4 8
5 6 1 5 8
Sample Output 2:

Верхняя четверть: 18
Правая четверть: 19
Нижняя четверть: 21
Левая четверть: 17
Sample Input 3:

2
99 72
65 11
Sample Output 3:

Верхняя четверть: 0
Правая четверть: 0
Нижняя четверть: 0
Левая четверть: 0
'''


n, a, sum_q1, sum_q2, sum_q3, sum_q4 = int(input()), [], 0, 0, 0, 0
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(n):
        if i < j and i < (n - 1 - j):
            sum_q1 += a[i][j]
        elif i < j and i > (n - 1 - j):
            sum_q2 += a[i][j]  
        elif i > j and i > (n - 1 - j):
            sum_q3 += a[i][j]
        elif i > j and i < (n - 1 - j):
            sum_q4 += a[i][j]
print('Верхняя четверть:', sum_q1)
print('Правая четверть:', sum_q2)
print('Нижняя четверть:', sum_q3)
print('Левая четверть:', sum_q4)
