'''
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 00.

Тестовые данные 🟢
Sample Input 1:

4
-22
1
Sample Output 1:

5
Sample Input 2:

33
55
63
Sample Output 2:

151
Sample Input 3:

-1
37
62
Sample Output 3:

99
'''


a, b, c = int(input()), int(input()), int(input())
sumpos = 0
if a > 0:
    sumpos += a
if b > 0:
    sumpos += b
if c > 0:
    sumpos += c
print(sumpos)
