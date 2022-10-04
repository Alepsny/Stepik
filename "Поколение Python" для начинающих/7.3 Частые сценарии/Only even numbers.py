'''
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

Тестовые данные 🟢
Sample Input 1:

2
4
6
8
10
12
14
16
18
20
Sample Output 1:

YES
Sample Input 2:

1
2
3
4
5
6
7
8
9
10
Sample Output 2:

NO
'''


flag = True
for i in range(10):
    if int(input()) % 2 != 0:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")
