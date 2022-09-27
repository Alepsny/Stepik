'''
Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

Формат входных данных
На вход программе подаётся целое число x.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается. 

Тестовые данные 🟢
Sample Input 1:

-332
Sample Output 1:

Не принадлежит
Sample Input 2:

-30
Sample Output 2:

Не принадлежит
Sample Input 3:

-21
Sample Output 3:

Принадлежит
'''


x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")
