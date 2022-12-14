'''
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), система примет и такое решение 😇

Тестовые данные 🟢
Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
Sample Input 2:

3 4
Sample Output 2:

1  2  4  7
3  5  8  10
6  9  11 12
Sample Input 3:

2 2
Sample Output 3:

1  2
3  4
Sample Input 4:

8 1
Sample Output 4:

1
2
3
4
5
6
7
8
Sample Input 5:

8 2
Sample Output 5:

1  2
3  4
5  6
7  8
9  10
11 12
13 14
15 16
'''


n, m = [int(i) for i in input().split()]
mat, count = [[0 for j in range(m)] for i in range(n)], 1
for i in range(n + m):
    for j in range(min(i, m -1), -1, -1):
        if i - j < n:
            mat[i-j][j] = count
            count += 1
for i in range(n):
    print(*mat[i])


