'''
Напишите программу, которая считывает целое положительное число n, n∈[1;9] и выводит значение числа n+\overline{nn}+\overline{nnn}.

Формат входных данных
На вход программе подаётся одно целое положительное число n, n∈[1;9].

Формат выходных данных
Программа должна вывести число n+\overline{nn}+\overline{nnn}.

Примечание. Для первого теста 1 + 11 + 111 = 123.

Тестовые данные 🟢
Sample Input 1:

1
Sample Output 1:

123
Sample Input 2:

2
Sample Output 2:

246
Sample Input 3:

3
Sample Output 3:

369
Sample Input 4:

9
Sample Output 4:

1107
'''


n = int(input())
nn = int(str(n) * 2)
nnn = int(str(n) * 3)
print(n + nn + nnn)
