'''
На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество одинаковых соседних символов.

Тестовые данные 🟢
Sample Input 1:

abcd
Sample Output 1:

0
Sample Input 2:

aabbcc
Sample Output 2:

3
Sample Input 3:

aaa
Sample Output 3:

2
'''


s, count = input(), 0
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        count += 1
else:
    print(count)
