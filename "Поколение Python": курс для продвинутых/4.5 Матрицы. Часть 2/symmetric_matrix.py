'''
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
0 1 2
1 2 3
2 3 4
Sample Output 1:

YES
Sample Input 2:

3
0 1 2
1 2 7
2 3 4
Sample Output 2:

NO
Sample Input 3:

2
1 2
3 4
Sample Output 3:

NO
'''


n, flag = int(input()), True
mat = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if mat[i][j] != mat[j][i]:
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')
