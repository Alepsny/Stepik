'''
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

Тестовые данные 🟢
Sample Input 1:

11111
Sample Output 1:

YES
Sample Input 2:

11112111
Sample Output 2:

NO
'''


flag = True
d = int(input())
ld = d % 10
while d != 0:
    if d % 10 != ld:
        flag = False
    d //= 10
if flag == True:
    print("YES")
else:
    print("NO")
