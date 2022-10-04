'''
На вход программе подается натуральное число nn. Напишите программу, которая для каждого из чисел от 00 до nn (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

9
Sample Output 1:

Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Квадрат числа 2 равен 4
Квадрат числа 3 равен 9
Квадрат числа 4 равен 16
Квадрат числа 5 равен 25
Квадрат числа 6 равен 36
Квадрат числа 7 равен 49
Квадрат числа 8 равен 64
Квадрат числа 9 равен 81
Sample Input 2:

1
Sample Output 2:

Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Sample Input 3:

2
Sample Output 3:

Квадрат числа 0 равен 0
Квадрат числа 1 равен 1
Квадрат числа 2 равен 4
'''


n = int(input())
for i in range(n + 1):
    print("Квадрат числа", i, "равен", i ** 2)
