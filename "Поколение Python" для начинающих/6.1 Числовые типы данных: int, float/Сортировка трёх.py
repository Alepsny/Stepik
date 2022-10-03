'''
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Тестовые данные 🟢
Sample Input 1:

132
129
135
Sample Output 1:

135
132
129
Sample Input 2:

150
160
156
Sample Output 2:

160
156
150
Sample Input 3:

161
139
148
Sample Output 3:

161
148
139
'''


a1, a2, a3 = int(input()), int(input()), int(input())
print(max(a1, a2, a3))
print(a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3))
print(min(a1, a2, a3))
