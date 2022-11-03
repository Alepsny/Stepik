'''
Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.

Тестовые данные 🟢
Sample Input 1:

12345
Sample Output 1:

54321
Sample Input 2:

987654
Sample Output 2:

945678
Sample Input 3:

25000
Sample Output 3:

52
Sample Input 4:

560000
Sample Output 4:

500006
'''


d = input()
if len(d) == 6:
    d1, d = d[:1], d[1:]
    print(d1 + d[::-1])
else:
    print(int(d[::-1]))
