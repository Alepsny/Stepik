'''
Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, ..., n^2 так, что суммы по каждому столбцу, 
каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
8 1 6
3 5 7
4 9 2
Sample Output 1:

YES
Sample Input 2:

3
8 2 6
3 5 7
4 9 1
Sample Output 2:

NO
Sample Input 3:

3
4 9 2
3 5 7
8 1 6
Sample Output 3:

YES
'''


n, flag, col1, col2, dig1, dig2, row1, row2 = int(input()), True, 0, None, 0, 0, 0, None
mat = [[int(i) for i in input().split()] for j in range(n)]
bef = mat[0][0]
for i in range(n):
    for j in range(n):
        col1 += mat[j][i]
        row1 += mat[i][j]
        if i != 0 and bef == mat[i][j] or mat[i][j] == 0:
            flag = False
            break
        bef = mat[i][j]
    if col2 != None and col2 != col1:
        flag = False
        break
    if row2 != None and row2 != col1:
        flag = False
        break
    col2, col1 = col1, 0
    row2, row1 = row1, 0
    dig1 += mat[i][i]
    dig2 += mat[n - i - 1][n - i - 1]
if dig1 != dig2:
    flag = False
if flag:
    print('YES')
else:
    print('NO')
