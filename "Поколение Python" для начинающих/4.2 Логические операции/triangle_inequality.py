'''
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

Формат входных данных
На вход программе подаётся три положительных целых числа.

Формат выходных данных
Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

Примечание. Треугольник существует, если выполняется неравенство треугольника.

Тестовые данные 🟢
Sample Input 1:

5
2
3
Sample Output 1:

NO
Sample Input 2:

3
4
6
Sample Output 2:

YES
Sample Input 3:

8
2
4
Sample Output 3:

NO
'''


a, b, c = int(input()), int(input()), int(input())
if a < b + c and b < a + c and c < b + a:
    print("YES")
else:
    print("NO")
