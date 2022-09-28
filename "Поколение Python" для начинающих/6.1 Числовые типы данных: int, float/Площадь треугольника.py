'''
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

Формат входных данных
На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести одно число – площадь треугольника.

Тестовые данные 🟢
Sample Input 1:

443
390
Sample Output 1:

86385.0
Sample Input 2:

32.2
25.5
Sample Output 2:

410.55
Sample Input 3:

5544.25
6100.0
Sample Output 3:

16909962.5
'''


a, b = float(input()), float(input())
print(0.5 * a * b)
