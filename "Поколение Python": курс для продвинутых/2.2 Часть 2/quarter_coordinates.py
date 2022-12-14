'''
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.



Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – x, затем ордината – y),
разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.

Тестовые данные 🟢
Sample Input 1:

4
0 -1
1 2
0 9
-9 -5
Sample Output 1:

Первая четверть: 1
Вторая четверть: 0
Третья четверть: 1
Четвертая четверть: 0
Sample Input 2:

10
4 8
-3 -1
-4 9
4 0
-4 0
5 -2
0 0
1 1
13 -3
-43 3
Sample Output 2:

Первая четверть: 2
Вторая четверть: 2
Третья четверть: 1
Четвертая четверть: 2
'''


n = int(input())
q1, q2, q3, q4 = 0, 0, 0, 0
for i in range(n):
    x, y = input().split()
    if int(x) > 0 and int(y) > 0:
        q1 += 1
    elif int(x) < 0 and int(y) > 0:
        q2 += 1
    elif int(x) < 0 and int(y) < 0:
        q3 += 1
    elif int(x) > 0 and int(y) < 0:
        q4 += 1
print('Первая четверть:', q1)
print('Вторая четверть:', q2)
print('Третья четверть:', q3)
print('Четвертая четверть:', q4)
