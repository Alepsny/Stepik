'''
Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.

Формат входных данных
На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введённые три строки через разделитель.

Тестовые данные 🟢
Sample Input 1:

*
Раз
Два
Три
Sample Output 1:

Раз*Два*Три
Sample Input 2:

##
Money often
costs
too much
Sample Output 2:

Money often##costs##too much
Sample Input 3:

python
1
2
3
Sample Output 3:

1python2python3
'''


sep = input()
print(input(), input(), input(), sep=sep)
