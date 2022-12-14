'''
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого введенного числаxx выводит значение функции 
f(x) = x^2+2x+1, каждое на отдельной строке.

Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.

Примечание. Для первого теста имеем:
f(1)=1^2+2⋅1+1=4,
f(2)=2^2+2⋅2+1=9,
f(3)=3^2+2⋅3+1=16,…

Тестовые данные 🟢
Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

1
2
3
4
5

4
9
16
25
36
Sample Input 2:

3
10
20
30
Sample Output 2:

10
20
30

121
441
961
'''


n, l, r = int(input()), [], []
for i in range(n):
    l.append(int(input()))
    r.append(l[i] ** 2 + 2 * l[i] + 1)
print(*l, sep="\n")
print()
print(*r, sep="\n")

