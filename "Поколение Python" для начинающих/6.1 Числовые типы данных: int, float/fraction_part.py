'''
Дано положительное действительное число. Выведите его дробную часть.

Формат входных данных
На вход программе подается положительное действительное число.

Формат выходных данных
Программа должна вывести дробную часть числа в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

44.45
Sample Output 1:

0.45
Sample Input 2:

39483.2
Sample Output 2:

0.2
Sample Input 3:

322.4958
Sample Output 3:

0.4958
'''


print(float(input()) % 1)

