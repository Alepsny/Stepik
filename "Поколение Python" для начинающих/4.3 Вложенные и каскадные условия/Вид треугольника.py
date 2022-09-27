'''
Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

Формат входных данных
На вход программе подаются три числа – длины сторон существующего треугольника.

Формат выходных данных
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

Тестовые данные 🟢
Sample Input 1:

145
145
139
Sample Output 1:

Равнобедренный
Sample Input 2:

59
59
59
Sample Output 2:

Равносторонний
Sample Input 3:

890
199
700
Sample Output 3:

Разносторонний
'''


a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a == b != c or a != b == c or a == c != b:
    print("Равнобедренный")
else:
    print("Разносторонний")
