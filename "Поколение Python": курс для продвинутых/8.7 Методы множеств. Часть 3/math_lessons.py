'''
Даны по 1010-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит множество оценок, имеющихся у учеников, которые встречаются 
не более, чем у двух из указанных учеников.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.

Тестовые данные 🟢
Sample Input 1:

1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 10 2 10 2 6 7 10 10 6
1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:

0 1 2 3 4 5 7 8 9 10
Sample Input 2:

2 9 3 4 6 9
2 3 4 5 2 10
2 3 4 5 3 10
Sample Output 2:

5 6 9 10
Sample Input 3:

3 4 5 6 2 10 3 9 8 8
5 7 8 9 2 7 4 6 8 2
2 6 7 1 3 6 5 9 2 6
Sample Output 3:

1 3 4 7 8 10
'''


a, b, c, new = set(input().split()), set(input().split()), set(input().split()), set()
new = (a | b | c) - (a & b & c)
new = [int(i) for i in new]
print(*sorted(new))
