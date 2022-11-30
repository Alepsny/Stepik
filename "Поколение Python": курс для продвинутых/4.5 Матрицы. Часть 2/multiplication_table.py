'''
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице. Создайте матрицу mult размером n×m и заполните её таблицей 
умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nnи m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа (для этого используйте строковый метод ljust()).

Тестовые данные 🟢
Sample Input 1:

4
6
Sample Output 1:

0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
Sample Input 2:

3
5
Sample Output 2:

0  0  0  0  0
0  1  2  3  4
0  2  4  6  8
Sample Input 3:

6
6
Sample Output 3:

0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
0  4  8  12 16 20
0  5  10 15 20 25
'''


n, m = int(input()), int(input())
mult = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = str(i * j)
for i in range(n):
    for j in range(m):
        print(mult[i][j].ljust(3), end='')
    print()
