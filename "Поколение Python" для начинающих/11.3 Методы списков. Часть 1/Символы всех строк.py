'''
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.

Формат входных данных
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести список состоящий из символов всех введенных строк.

Примечание. В результирующем списке могут содержаться одинаковые символы.

Тестовые данные 🟢
Sample Input:

3
abc
def
ghi
Sample Output:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
'''


n,  l = int(input()), []
for i in range(n):
    l.extend(input())
print(l)
