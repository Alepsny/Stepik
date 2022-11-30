'''
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.

Формат входных данных
На вход программе подается число (n≥1).

Формат выходных данных
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

Тестовые данные 🟢
Sample Input 1:

4
Sample Output 1:

1
1 1
1 2 1
1 3 3 1
Sample Input 2:

5
Sample Output 2:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Sample Input 3:

2
Sample Output 3:

1
1 1
'''


n, new = int(input()), [1]
pascal = [[1], [1, 1]]
for i in range(2, n + 1):
    for j in range(1, i):
        new.append(pascal[i-1][j-1] + pascal[i-1][j])
    new.append(1)
    pascal.append(new)
    new = [1]
for i in range(n):
    print(*pascal[i])
