'''
Дано натуральное число n, (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×5 в соответствии с условием.

Примечание. В конце строки может быть пробел.

Тестовые данные 🟢
Sample Input 1:

3
Sample Output 1:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
Sample Input 2:

6
Sample Output 2:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
6 6 6 6 6
Sample Input 3:

1
Sample Output 3:

1 1 1 1 1
'''


n = int(input())
for i in range(1, n + 1):
    for j in range(5):
        print(i, end = " ")
    print()
