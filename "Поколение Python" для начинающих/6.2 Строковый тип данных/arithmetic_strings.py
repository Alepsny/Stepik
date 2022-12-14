'''
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

Тестовые данные 🟢
Sample Input 1:

abc
a
abcde
Sample Output 1:

YES
Sample Input 2:

2434
90099
21
Sample Output 2:

NO
Sample Input 3:

aaaaaaaaaa10
1111111Nm
22222r
Sample Output 3:

YES
'''


s1, s2, s3 = input(), input(), input()
l1, l2, l3 = len(s1), len(s2), len(s3)
s1 = min(l1, l2 ,l3)
s3 = max(l1, l2, l3)
if l1 != s1 and l1 != s3:
    s2 = l1
elif l2 != s1 and l2 != s3:
    s2 = l2
else:
    s2 = l3
if s3 - s2 == s2 - s1:
    print("YES")
else:
    print("NO")
