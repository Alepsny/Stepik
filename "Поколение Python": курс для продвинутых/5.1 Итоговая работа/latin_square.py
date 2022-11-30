'''
Латинским квадратом порядка nn называется квадратная матрица размером n×n, каждая строка и каждый столбец которой содержат все числа от 1 до n. 
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

Тестовые данные 🟢
Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:

YES
Sample Input 2:

3
1 2 3
3 2 1
2 3 4
Sample Output 2:

NO
'''


n = int(input())
mat = [[int(j) for j in input().split()] for i in range(n)]
mat1 = [[mat[j][i] for j in range(n)] for i in range(n)]
example, flag = [i for i in range(1, n + 1)], True
for i in range(n):
    mat[i], mat1[i] = sorted(mat[i]), sorted(mat1[i])
    if mat[i] != example or mat1[i] != example:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
