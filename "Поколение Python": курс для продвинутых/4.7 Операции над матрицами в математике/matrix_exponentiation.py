'''
Напишите программу, которая возводит квадратную матрицу в -ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2
Sample Output 1:

30 36 42
66 81 96
102 126 150
Sample Input 2:

3
1 2 1
3 3 3
1 2 1
5
Sample Output 2:

1666 2222 1666
3333 4443 3333
1666 2222 1666
Sample Input 3:

5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3
Sample Output 3:

133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
'''


def mat_def(n, mat, mat_):
    mat_new = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat_new[i][j] += mat[i][k] * mat_[k][j]
    return mat_new


n = int(input())
mat = [[int(j) for j in input().split()] for i in range(n)]
mat_ = mat
m = int(input())

for i in range(m - 1):
    mat = mat_def(n, mat, mat_)
for i in range(n):
    print(*mat[i])
