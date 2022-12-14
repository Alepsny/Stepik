'''
Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше") Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану, чтобы угадать число Тимура.

Тестовые данные 🟢
Sample Input 1:

8
Sample Output 1:

3
Sample Input 2:

20
Sample Output 2:

5
Sample Input 3:

100
Sample Output 3:

7
'''


import math

def Divide(number):
    i = 0
    while number != 1:
        number = math.ceil(number / 2)
        i += 1
    return i
number = int(input())
print(Divide(number))
