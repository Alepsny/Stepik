'''
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, 
далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢
Sample Input 1:

2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3
Sample Output 1:

4 4 4 6
6 9 8 4
Sample Input 2:

3 3
9 6 3
3 1 1
4 7 5

0 3 2
1 7 8
4 2 3
Sample Output 2:

9 9 5
4 8 9
8 9 8
Sample Input 3:

1 1
1

1
Sample Output 3:

2
'''


n, m = [int(i) for i in input().split()]
mat1 = [[int(j) for j in input().split()] for i in range(n)]
input()
mat2 = [[int(j) for j in input().split()] for i in range(n)]
mat_new = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        mat_new[i][j] = mat1[i][j] + mat2[i][j]
for i in range(n):
    print(*mat_new[i])

