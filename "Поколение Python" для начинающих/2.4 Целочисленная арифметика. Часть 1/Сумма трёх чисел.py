'''
Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.

Формат входных данных
На вход программе подаётся три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму введенных чисел.

Тестовые данные 🟢
Sample Input 1:

9
11
2
Sample Output 1:

22
Sample Input 2:

-1
10
1
Sample Output 2:

10
Sample Input 3:

-7
-10
-3
Sample Output 3:

-20
'''


one, two, three = int(input()), int(input()), int(input())
print(one + two + three)
