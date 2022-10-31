'''
На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения (1+1/2+1/3+…+1/n)−ln(n).

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

Тестовые данные 🟢
Sample Input 1:

10
Sample Output 1:

0.6263831609742079
Sample Input 2:

1
Sample Output 2:

1.0
Sample Input 3:

100
Sample Output 3:

0.5822073316515288
'''


from math import log

total = 1
n = int(input())
for i in range(2, n + 1):
    total += 1 / i
print(total - log(n))
