'''
Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное число.

Формат выходных данных
Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

Тестовые данные 🟢
Sample Input 1:

123
Sample Output 1:

Сумма цифр = 6
Произведение цифр = 6
Sample Input 2:

333
Sample Output 2:

Сумма цифр = 9
Произведение цифр = 27
Sample Input 3:

101
Sample Output 3:

Сумма цифр = 2
Произведение цифр = 0
'''


num = int(input())
dig1 = num // 100
dig2 = num // 10 % 10
dig3 = num % 10
print("Сумма цифр =", dig1 + dig2 + dig3)
print("Произведение цифр =", dig1 * dig2 * dig3)
