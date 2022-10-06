'''
На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа. 
Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, 
то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести цифровой корень введенного числа.

Примечание. Используйте вложенные циклы while.

Тестовые данные 🟢
Sample Input:

192
Sample Output:

3
'''


n, q = int(input()), 0
while q > -1 :
    q += n % 10
    n //= 10
    if n == 0 and q > 9:
        n, q = q, 0
    elif n == 0 and q < 10:
        print(q)
        break
