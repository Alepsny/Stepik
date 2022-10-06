'''
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести число, записанное в обратном порядке.

Тестовые данные 🟢
Sample Input 1:

5086334
Sample Output 1:

4336805
Sample Input 2:

450098
Sample Output 2:

890054
Sample Input 3:

5088531157
Sample Output 3:

7511358805
'''


d = int(input())
while d != 0:
    ld = d % 10
    print(ld, end = "")
    d //= 10
