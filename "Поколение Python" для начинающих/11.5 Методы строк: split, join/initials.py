'''
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу, которая выводит инициалы человека.

Формат входных данных
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input:

Владимир Семенович Высоцкий
Sample Output:

В.С.В.
'''


l = input().split()
p = []
for i in range(len(l)):
    p.extend(l[i][0])
print(*p, sep=".", end=".")
