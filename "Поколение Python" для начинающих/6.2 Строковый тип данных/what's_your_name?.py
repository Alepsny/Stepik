'''
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

«Hello [введенное имя] [введенная фамилия]! You just delved into Python».

Формат входных данных
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Между firstname lastname вставьте пробел =)

Тестовые данные 🟢
Sample Input 1:

Anthony
Joshua
Sample Output 1:

Hello Anthony Joshua! You just delved into Python
Sample Input 2:

Michael
Jordan
Sample Output 2:

Hello Michael Jordan! You just delved into Python
Sample Input 3:

Leonardo
DiCaprio
Sample Output 3:

Hello Leonardo DiCaprio! You just delved into Python
'''


f = input()
l = input()
print("Hello " + f + " " + l + "! You just delved into Python")
